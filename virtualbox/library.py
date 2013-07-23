# A Pythonic VirtalBox Main API
#
# By Michael Dorman.
# [mjdorma+pyvbox@gmail.com]
#
# Note: Commenting, and API structure generation was carved from 
#       VirtualBox project's VirtualBox.xidl Main API definition.
#
import re
import inspect
try:
    import __builtin__ as builtin 
except:
    import builtin


__doc__ = """\
  Welcome to the VirtualBox Main API documentation. This documentation
  describes the so-called VirtualBox Main API which comprises all public
  COM interfaces and components provided by the VirtualBox server and by the
  VirtualBox client library.

  VirtualBox employs a client-server design, meaning that whenever any part of
  VirtualBox is running -- be it the Qt GUI, the VBoxManage command-line
  interface or any virtual machine --, a dedicated server process named
  VBoxSVC runs in the background. This allows multiple processes working with
  VirtualBox to cooperate without conflicts. These processes communicate to each
  other using inter-process communication facilities provided by the COM
  implementation of the host computer.

  On Windows platforms, the VirtualBox Main API uses Microsoft COM, a native COM
  implementation. On all other platforms, Mozilla XPCOM, an open-source COM
  implementation, is used.

  All the parts that a typical VirtualBox user interacts with (the Qt GUI
  and the VBoxManage command-line interface) are technically
  front-ends to the Main API and only use the interfaces that are documented
  in this Main API documentation. This ensures that, with any given release
  version of VirtualBox, all capabilities of the product that could be useful
  to an external client program are always exposed by way of this API.

  The VirtualBox Main API (also called the VirtualBox COM library)
  contains two public component classes:
  %VirtualBox.VirtualBox and %VirtualBox.Session, which
  implement IVirtualBox and ISession interfaces respectively. These two classes
  are of supreme importance and will be needed in order for any front-end
  program to do anything useful. It is recommended to read the documentation of
  the mentioned interfaces first.

  The %VirtualBox.VirtualBox class is a singleton. This means that
  there can be only one object of this class on the local machine at any given
  time. This object is a parent of many other objects in the VirtualBox COM
  library and lives in the VBoxSVC process. In fact, when you create an instance
  of the VirtualBox.VirtualBox, the COM subsystem checks if the VBoxSVC
  process is already running, starts it if not, and returns you a reference to
  the VirtualBox object created in this process. When the last reference
  to this object is released, the VBoxSVC process ends (with a 5 second delay to
  protect from too frequent restarts).

  The %VirtualBox.Session class is a regular component. You can create
  as many Session objects as you need but all of them will live in a
  process which issues the object instantiation call. Session objects
  represent virtual machine sessions which are used to configure virtual
  machines and control their execution.

  The naming of methods and attributes is very clearly defined: they all start
  with a lowercase letter (except if they start with an acronym), and are using
  CamelCase style otherwise. This naming only applies to the IDL description,
  and is modified by the various language bindings (some convert the first
  character to upper case, some not). See the SDK reference for more details
  about how to call a method or attribute from a specific programming language.
"""


lib_version = 1.3
lib_app_uuid = '819B4D85-9CEE-493C-B6FC-64FFE759B3C9'
lib_uuid = 'd7569351-1750-46f0-936e-bd127d5bc264'
xidl_hash = '00e579f9eefcd8af7d7eb3f0b9f46d87'


def pythonic_name(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    if hasattr(builtin, name) is True or name in ['global']:
        name += "_p"
    return name


class EnumType(type):
    """EnumType is a metaclass for Enum. It is responsible for configuring
    the Enum class object's values defined in Enum.lookup_label"""
    def __init__(cls, name, bases, dct):
        cls._value = None
        cls._lookup_label = {v:l for l, v, _ in cls._enums}
        cls._lookup_doc = {v:d for _, v, d in cls._enums}
        for l, v, _ in cls._enums:
            setattr(cls, pythonic_name(l), cls(v))

    def __getitem__(cls, k):
        if not hasattr(cls, k):
            raise KeyError("%s has no key %s" % cls.__name__, k)
        return getattr(cls, k)


class Enum(object):
    """Enum objects provide a container for VirtualBox enumerations"""
    _enums = {}
    __metaclass__ = EnumType
    def __init__(self, value=None):
        if value not in self._lookup_label:
            raise ValueError("Can not find enumeration where value=%s" % value)
        self._value = value
        self.__doc__ = self._lookup_doc[self._value]

    def __str__(self):
        if self._value is None:
            return "None"
        return self._lookup_label[self._value]

    def __int__(self):
        return self._value

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self._value)

    def __eq__(self, k):
        return self.__cmp__(k) == 0

    def __cmp__(self, k):
        return cmp(int(self), int(k))

    def __getitem__(self, k):
        return self.__class__[k]


class Interface(object):
    """Interface objects provide a wrapper for the VirtualBox COM objects"""
    def __init__(self, interface=None):
        self._i = interface

    def __nonzero__(self):
        return bool(self._i)

    def _cast_to_valuetype(self, value):
        def cast_to_valuetype(value):
            if isinstance(value, Interface):
                return value._i
            elif isinstance(value, Enum):
                return int(value)
            else:
                return value
        if isinstance(value, list):
            return [cast_to_valuetype(a) for a in value]
        else:
            return cast_to_valuetype(value)

    def _search_attr(self, name, prefix=None):
        attr_name = name
        attr = getattr(self._i, attr_name, None)
        # if a prefix is defined, try to get that prefixed name and use that
        # attribute instead, else, stick with the attr value pulled out above
        if prefix is not None:
            prefix_name = prefix + name[0].upper() + name[1:]
            attr = getattr(self._i, prefix_name, attr)
        if attr is not None:
            return attr
        raise AttributeError("Could not find '%s' in Interface %s" % (name,
                              self._i))

    def _get_attr(self, name):
        attr = self._search_attr(name, prefix='get')
        if inspect.isfunction(attr) or inspect.ismethod(attr):
            return self._call_method(attr)
        else:
            return attr

    def _set_attr(self, name, value):
        attr = self._search_attr(name, prefix='set')
        if inspect.isfunction(attr) or inspect.ismethod(attr):
            return self._call_method(attr, value)
        else:
            return setattr(self._i, name, value)

    def _call(self, name, in_p=[]):
        global vbox_error
        method = self._search_attr(name)
        if inspect.isfunction(method) or inspect.ismethod(method):
            return self._call_method(method, in_p=in_p)
        else:
            return method

    def _call_method(self, method, in_p=[]):
        in_params = [self._cast_to_valuetype(p) for p in in_p]
        try:
            ret = method(*in_params)
        except Exception as exc:
            if hasattr(exc, 'errno'):
                errno = exc.errno & 0xFFFFFFFF
                errclass = vbox_error.get(errno, VBoxError)
                errobj = errclass()
                errobj.value = errno
            else:
                errobj = VBoxError()
            errobj.msg = getattr(exc, 'msg', exc.message)
            raise errobj
        return ret


class VBoxError(Exception): 
    """Generic VBoxError"""
    name = "undef"
    value = -1
    msg = ""
    def __str__(self):
        return "0x%x (%s)" % (self.value, self.msg)


#container lookup for the different error types
vbox_error = {}


class VBoxErrorObjectNotFound(VBoxError):
    """Object corresponding to the supplied arguments does not exist."""
    name = 'VBOX_E_OBJECT_NOT_FOUND'
    value = 0x80BB0001
vbox_error[0x80BB0001] = VBoxErrorObjectNotFound


class VBoxErrorInvalidVmState(VBoxError):
    """Current virtual machine state prevents the operation."""
    name = 'VBOX_E_INVALID_VM_STATE'
    value = 0x80BB0002
vbox_error[0x80BB0002] = VBoxErrorInvalidVmState


class VBoxErrorVmError(VBoxError):
    """Virtual machine error occurred attempting the operation."""
    name = 'VBOX_E_VM_ERROR'
    value = 0x80BB0003
vbox_error[0x80BB0003] = VBoxErrorVmError


class VBoxErrorFileError(VBoxError):
    """File not accessible or erroneous file contents."""
    name = 'VBOX_E_FILE_ERROR'
    value = 0x80BB0004
vbox_error[0x80BB0004] = VBoxErrorFileError


class VBoxErrorIprtError(VBoxError):
    """Runtime subsystem error."""
    name = 'VBOX_E_IPRT_ERROR'
    value = 0x80BB0005
vbox_error[0x80BB0005] = VBoxErrorIprtError


class VBoxErrorPdmError(VBoxError):
    """Pluggable Device Manager error."""
    name = 'VBOX_E_PDM_ERROR'
    value = 0x80BB0006
vbox_error[0x80BB0006] = VBoxErrorPdmError


class VBoxErrorInvalidObjectState(VBoxError):
    """Current object state prohibits operation."""
    name = 'VBOX_E_INVALID_OBJECT_STATE'
    value = 0x80BB0007
vbox_error[0x80BB0007] = VBoxErrorInvalidObjectState


class VBoxErrorHostError(VBoxError):
    """Host operating system related error."""
    name = 'VBOX_E_HOST_ERROR'
    value = 0x80BB0008
vbox_error[0x80BB0008] = VBoxErrorHostError


class VBoxErrorNotSupported(VBoxError):
    """Requested operation is not supported."""
    name = 'VBOX_E_NOT_SUPPORTED'
    value = 0x80BB0009
vbox_error[0x80BB0009] = VBoxErrorNotSupported


class VBoxErrorXmlError(VBoxError):
    """Invalid XML found."""
    name = 'VBOX_E_XML_ERROR'
    value = 0x80BB000A
vbox_error[0x80BB000A] = VBoxErrorXmlError


class VBoxErrorInvalidSessionState(VBoxError):
    """Current session state prohibits operation."""
    name = 'VBOX_E_INVALID_SESSION_STATE'
    value = 0x80BB000B
vbox_error[0x80BB000B] = VBoxErrorInvalidSessionState


class VBoxErrorObjectInUse(VBoxError):
    """Object being in use prohibits operation."""
    name = 'VBOX_E_OBJECT_IN_USE'
    value = 0x80BB000C
vbox_error[0x80BB000C] = VBoxErrorObjectInUse


class SettingsVersion(Enum):
    """Settings version of VirtualBox settings files. This is written to
      the "version" attribute of the root "VirtualBox" element in the settings
      file XML and indicates which VirtualBox version wrote the file."""
    __uuid__ = 'd5b15ca7-3de7-46b2-a63a-ddcce42bfa3f'
    _enums = [\
        ('Null', 0, 
         '''Null value, indicates invalid version.'''),
        ('v1_0', 1, 
         '''Legacy settings version, not currently supported.'''),
        ('v1_1', 2, 
         '''Legacy settings version, not currently supported.'''),
        ('v1_2', 3, 
         '''Legacy settings version, not currently supported.'''),
        ('v1_3pre', 4, 
         '''Legacy settings version, not currently supported.'''),
        ('v1_3', 5, 
         '''Settings version "1.3", written by VirtualBox 2.0.12.'''),
        ('v1_4', 6, 
         '''Intermediate settings version, understood by VirtualBox 2.1.x.'''),
        ('v1_5', 7, 
         '''Intermediate settings version, understood by VirtualBox 2.1.x.'''),
        ('v1_6', 8, 
         '''Settings version "1.6", written by VirtualBox 2.1.4 (at least).'''),
        ('v1_7', 9, 
         '''Settings version "1.7", written by VirtualBox 2.2.x and 3.0.x.'''),
        ('v1_8', 10, 
         '''Intermediate settings version "1.8", understood by VirtualBox 3.1.x.'''),
        ('v1_9', 11, 
         '''Settings version "1.9", written by VirtualBox 3.1.x.'''),
        ('v1_10', 12, 
         '''Settings version "1.10", written by VirtualBox 3.2.x.'''),
        ('v1_11', 13, 
         '''Settings version "1.11", written by VirtualBox 4.0.x.'''),
        ('v1_12', 14, 
         '''Settings version "1.12", written by VirtualBox 4.1.x.'''),
        ('v1_13', 15, 
         '''Settings version "1.13", written by VirtualBox 4.2.x.'''),
        ('v1_14', 16, 
         '''Settings version "1.14", written by VirtualBox 4.3.x.'''),
        ('Future', 99999, 
         '''Settings version greater than "1.13", written by a future VirtualBox version.'''),
        ] 


class AccessMode(Enum):
    """Access mode for opening files."""
    __uuid__ = '1da0007c-ddf7-4be8-bcac-d84a1558785f'
    _enums = [\
        ('ReadOnly', 1, 
         ''''''),
        ('ReadWrite', 2, 
         ''''''),
        ] 


class MachineState(Enum):
    """Virtual machine execution state.

      This enumeration represents possible values of the <link to="IMachine::state"/> attribute.

      Below is the basic virtual machine state diagram. It shows how the state
      changes during virtual machine execution. The text in square braces shows
      a method of the IConsole interface that performs the given state
      transition.

      
            +---------[powerDown()] <- Stuck <--[failure]-+
            V                                             |
    +-> PoweredOff --+-->[powerUp()]--> Starting --+      | +-----[resume()]-----+
    |                |                             |      | V                    |
    |   Aborted -----+                             +--> Running --[pause()]--> Paused
    |                                              |      ^ |                   ^ |
    |   Saved -----------[powerUp()]--> Restoring -+      | |                   | |
    |     ^                                               | |                   | |
    |     |     +-----------------------------------------+-|-------------------+ +
    |     |     |                                           |                     |
    |     |     +-- Saving <--------[takeSnapshot()]<-------+---------------------+
    |     |                                                 |                     |
    |     +-------- Saving <--------[saveState()]<----------+---------------------+
    |                                                       |                     |
    +-------------- Stopping -------[powerDown()]<----------+---------------------+
      

      Note that states to the right from PoweredOff, Aborted and Saved in the
      above diagram are called online VM states. These states
      represent the virtual machine which is being executed in a dedicated
      process (usually with a GUI window attached to it where you can see the
      activity of the virtual machine and interact with it). There are two
      special pseudo-states, FirstOnline and LastOnline, that can be used in
      relational expressions to detect if the given machine state is online or
      not:

      
        if (machine.GetState() >= MachineState_FirstOnline &amp;&amp;
            machine.GetState() <= MachineState_LastOnline)
        {
            ...the machine is being executed...
        }
      

      When the virtual machine is in one of the online VM states (that is, being
      executed), only a few machine settings can be modified. Methods working
      with such settings contain an explicit note about that. An attempt to
      change any other setting or perform a modifying operation during this time
      will result in the @c VBOX_E_INVALID_VM_STATE error.

      All online states except Running, Paused and Stuck are transitional: they
      represent temporary conditions of the virtual machine that will last as
      long as the operation that initiated such a condition.

      The Stuck state is a special case. It means that execution of the machine
      has reached the "Guru Meditation" condition. This condition indicates an
      internal VMM (virtual machine manager) failure which may happen as a
      result of either an unhandled low-level virtual hardware exception or one
      of the recompiler exceptions (such as the too-many-traps
      condition).

      Note also that any online VM state may transit to the Aborted state. This
      happens if the process that is executing the virtual machine terminates
      unexpectedly (for example, crashes). Other than that, the Aborted state is
      equivalent to PoweredOff.

      There are also a few additional state diagrams that do not deal with
      virtual machine execution and therefore are shown separately. The states
      shown on these diagrams are called offline VM states (this includes
      PoweredOff, Aborted and Saved too).

      The first diagram shows what happens when a lengthy setup operation is
      being executed (such as <link to="IMachine::attachDevice"/>).

      
    +----------------------------------(same state as before the call)------+
    |                                                                       |
    +-> PoweredOff --+                                                      |
    |                |                                                      |
    |-> Aborted -----+-->[lengthy VM configuration call] --> SettingUp -----+
    |                |
    +-> Saved -------+
      

      The next two diagrams demonstrate the process of taking a snapshot of a
      powered off virtual machine, restoring the state to that as of a snapshot
      or deleting a snapshot, respectively.

      
    +----------------------------------(same state as before the call)------+
    |                                                                       |
    +-> PoweredOff --+                                                      |
    |                +-->[takeSnapshot()] -------------------> Saving ------+
    +-> Aborted -----+

    +-> PoweredOff --+
    |                |
    |   Aborted -----+-->[restoreSnapshot()    ]-------> RestoringSnapshot -+
    |                |   [deleteSnapshot()     ]-------> DeletingSnapshot --+
    +-> Saved -------+                                                      |
    |                                                                       |
    +---(Saved if restored from an online snapshot, PoweredOff otherwise)---+
      

      Note that the Saving state is present in both the offline state group and
      online state group. Currently, the only way to determine what group is
      assumed in a particular case is to remember the previous machine state: if
      it was Running or Paused, then Saving is an online state, otherwise it is
      an offline state. This inconsistency may be removed in one of the future
      versions of VirtualBox by adding a new state.

      <note internal="yes">
        For whoever decides to touch this enum: In order to keep the
        comparisons involving FirstOnline and LastOnline pseudo-states valid,
        the numeric values of these states must be correspondingly updated if
        needed: for any online VM state, the condition
        FirstOnline <= state <= LastOnline must be
        @c true. The same relates to transient states for which
        the condition FirstOnline <= state <= LastOnline must be
        @c true."""
    __uuid__ = 'ec6c6a9e-113d-4ff4-b44f-0b69f21c97fe'
    _enums = [\
        ('Null', 0, 
         '''Null value (never used by the API).'''),
        ('PoweredOff', 1, 
         '''The machine is not running and has no saved execution state; it has
        either never been started or been shut down successfully.'''),
        ('Saved', 2, 
         '''The machine is not currently running, but the execution state of the machine
        has been saved to an external file when it was running, from where
        it can be resumed.'''),
        ('Teleported', 3, 
         '''The machine was teleported to a different host (or process) and then
        powered off. Take care when powering it on again may corrupt resources
        it shares with the teleportation target (e.g. disk and network).'''),
        ('Aborted', 4, 
         '''The process running the machine has terminated abnormally. This may
        indicate a crash of the VM process in host execution context, or
        the VM process has been terminated externally.'''),
        ('Running', 5, 
         '''The machine is currently being executed.
        <note internal="yes">
          For whoever decides to touch this enum: In order to keep the
          comparisons in the old source code valid, this state must immediately
          precede the Paused state.
          TODO: Lift this spectacularly wonderful restriction.'''),
        ('Paused', 6, 
         '''Execution of the machine has been paused.
        <note internal="yes">
          For whoever decides to touch this enum: In order to keep the
          comparisons in the old source code valid, this state must immediately
          follow the Running state.
          TODO: Lift this spectacularly wonderful restriction.'''),
        ('Stuck', 7, 
         '''Execution of the machine has reached the "Guru Meditation"
        condition. This indicates a severe error in the hypervisor itself.
        <note internal="yes">
          bird: Why this uncool name? Could we rename it to "GuruMeditation" or
                "Guru", perhaps? Or are there some other VMM states that are
                intended to be lumped in here as well?'''),
        ('Teleporting', 8, 
         '''The machine is about to be teleported to a different host or process.
        It is possible to pause a machine in this state, but it will go to the
        @c TeleportingPausedVM state and it will not be
        possible to resume it again unless the teleportation fails.'''),
        ('LiveSnapshotting', 9, 
         '''A live snapshot is being taken. The machine is running normally, but
        some of the runtime configuration options are inaccessible. Also, if
        paused while in this state it will transition to
        @c Saving and it will not be resume the
        execution until the snapshot operation has completed.'''),
        ('Starting', 10, 
         '''Machine is being started after powering it on from a
        zero execution state.'''),
        ('Stopping', 11, 
         '''Machine is being normally stopped powering it off, or after the guest OS
        has initiated a shutdown sequence.'''),
        ('Saving', 12, 
         '''Machine is saving its execution state to a file, or an online
        snapshot of the machine is being taken.'''),
        ('Restoring', 13, 
         '''Execution state of the machine is being restored from a file
        after powering it on from the saved execution state.'''),
        ('TeleportingPausedVM', 14, 
         '''The machine is being teleported to another host or process, but it is
        not running. This is the paused variant of the
        @c state.'''),
        ('TeleportingIn', 15, 
         '''Teleporting the machine state in from another host or process.'''),
        ('FaultTolerantSyncing', 16, 
         '''The machine is being synced with a fault tolerant VM running elsewhere.'''),
        ('DeletingSnapshotOnline', 17, 
         '''Like @c DeletingSnapshot, but the merging of media is ongoing in
        the background while the machine is running.'''),
        ('DeletingSnapshotPaused', 18, 
         '''Like @c DeletingSnapshotOnline, but the machine was paused when the
        merging of differencing media was started.'''),
        ('RestoringSnapshot', 19, 
         '''A machine snapshot is being restored; this typically does not take long.'''),
        ('DeletingSnapshot', 20, 
         '''A machine snapshot is being deleted; this can take a long time since this
        may require merging differencing media. This value indicates that the
        machine is not running while the snapshot is being deleted.'''),
        ('SettingUp', 21, 
         '''Lengthy setup operation is in progress.'''),
        ('FirstOnline', 5, 
         '''Pseudo-state: first online state (for use in relational expressions).'''),
        ('LastOnline', 18, 
         '''Pseudo-state: last online state (for use in relational expressions).'''),
        ('FirstTransient', 8, 
         '''Pseudo-state: first transient state (for use in relational expressions).'''),
        ('LastTransient', 21, 
         '''Pseudo-state: last transient state (for use in relational expressions).'''),
        ] 


class SessionState(Enum):
    """Session state. This enumeration represents possible values of
      <link to="IMachine::sessionState"/> and <link to="ISession::state"/>
      attributes."""
    __uuid__ = 'cf2700c0-ea4b-47ae-9725-7810114b94d8'
    _enums = [\
        ('Null', 0, 
         '''Null value (never used by the API).'''),
        ('Unlocked', 1, 
         '''In <link to="IMachine::sessionState"/>, this means that the machine
        is not locked for any sessions.

        In <link to="ISession::state"/>, this means that no machine is
        currently locked for this session.'''),
        ('Locked', 2, 
         '''In <link to="IMachine::sessionState"/>, this means that the machine
        is currently locked for a session, whose process identifier can
        then be found in the <link to="IMachine::sessionPID"/> attribute.

        In <link to="ISession::state"/>, this means that a machine is
        currently locked for this session, and the mutable machine object
        can be found in the <link to="ISession::machine"/> attribute
        (see <link to="IMachine::lockMachine"/> for details).'''),
        ('Spawning', 3, 
         '''A new process is being spawned for the machine as a result of
        <link to="IMachine::launchVMProcess"/> call. This state also occurs
        as a short transient state during an <link to="IMachine::lockMachine"/>
        call.'''),
        ('Unlocking', 4, 
         '''The session is being unlocked.'''),
        ] 


class CPUPropertyType(Enum):
    """Virtual CPU property type. This enumeration represents possible values of the
      IMachine get- and setCPUProperty methods."""
    __uuid__ = '24d356a6-2f45-4abd-b977-1cbe9c4701f5'
    _enums = [\
        ('Null', 0, 
         '''Null value (never used by the API).'''),
        ('PAE', 1, 
         '''This setting determines whether VirtualBox will expose the Physical Address
        Extension (PAE) feature of the host CPU to the guest. Note that in case PAE
        is not available, it will not be reported.'''),
        ('Synthetic', 2, 
         '''This setting determines whether VirtualBox will expose a synthetic CPU to the guest to allow
        teleporting between host systems that differ significantly.'''),
        ('LongMode', 3, 
         '''This setting determines whether VirtualBox will advertice long mode
        (i.e. 64-bit guest support) and let the guest enter it.'''),
        ] 


class HWVirtExPropertyType(Enum):
    """Hardware virtualization property type. This enumeration represents possible values
      for the <link to="IMachine::getHWVirtExProperty"/> and
      <link to="IMachine::setHWVirtExProperty"/> methods."""
    __uuid__ = '39463ecd-b4b8-401f-b168-76cfa87e11f0'
    _enums = [\
        ('Null', 0, 
         '''Null value (never used by the API).'''),
        ('Enabled', 1, 
         '''Whether hardware virtualization (VT-x/AMD-V) is enabled at all. If
        such extensions are not available, they will not be used.'''),
        ('Exclusive', 2, 
         '''Whether hardware virtualization is used exclusively by VirtualBox. When enabled,
        VirtualBox assumes it can acquire full and exclusive access to the VT-x or AMD-V
        feature of the host. To share these with other hypervisors, you must disable this property.'''),
        ('VPID', 3, 
         '''Whether VT-x VPID is enabled. If this extension is not available, it will not be used.'''),
        ('NestedPaging', 4, 
         '''Whether Nested Paging is enabled. If this extension is not available, it will not be used.'''),
        ('UnrestrictedExecution', 5, 
         '''Whether VT-x unrestricted execution is enabled. If this feature is not available, it will not be used.'''),
        ('LargePages', 6, 
         '''Whether large page allocation is enabled; requires nested paging and a 64-bit host.'''),
        ('Force', 7, 
         '''Whether the VM should fail to start if hardware virtualization (VT-x/AMD-V) cannot be used. If
        not set, there will be an automatic fallback to software virtualization.'''),
        ] 


class FaultToleranceState(Enum):
    """Used with <link to="IMachine::faultToleranceState"/>."""
    __uuid__ = '5124f7ec-6b67-493c-9dee-ee45a44114e1'
    _enums = [\
        ('Inactive', 1, 
         '''No fault tolerance enabled.'''),
        ('Master', 2, 
         '''Fault tolerant master VM.'''),
        ('Standby', 3, 
         '''Fault tolerant standby VM.'''),
        ] 


class LockType(Enum):
    """Used with <link to="IMachine::lockMachine"/>."""
    __uuid__ = '168a6a8e-12fd-4878-a1f9-38a750a56089'
    _enums = [\
        ('Write', 2, 
         '''Lock the machine for writing. This requests an exclusive lock, i.e.
        there cannot be any other API client holding any type of lock for this
        VM concurrently. Remember that a VM process counts as an API client
        which implicitly holds the equivalent of a shared lock during the
        entire VM runtime.'''),
        ('Shared', 1, 
         '''Request only a shared lock for remote-controlling the machine.
        Such a lock allows changing certain VM settings which can be safely
        modified for a running VM.'''),
        ('VM', 3, 
         '''Lock the machine for writing, and create objects necessary for
        running a VM in this process.'''),
        ] 


class SessionType(Enum):
    """Session type. This enumeration represents possible values of the
      <link to="ISession::type"/> attribute."""
    __uuid__ = 'A13C02CB-0C2C-421E-8317-AC0E8AAA153A'
    _enums = [\
        ('Null', 0, 
         '''Null value (never used by the API).'''),
        ('WriteLock', 1, 
         '''Session has acquired an exclusive write lock on a machine
        using <link to="IMachine::lockMachine"/>.'''),
        ('Remote', 2, 
         '''Session has launched a VM process using
        <link to="IMachine::launchVMProcess"/>'''),
        ('Shared', 3, 
         '''Session has obtained a link to another session using
        <link to="IMachine::lockMachine"/>'''),
        ] 


class DeviceType(Enum):
    """Device type."""
    __uuid__ = '6d9420f7-0b56-4636-99f9-7346f1b01e57'
    _enums = [\
        ('Null', 0, 
         '''Null value, may also mean "no device" (not allowed for
        <link to="IConsole::getDeviceActivity"/>).'''),
        ('Floppy', 1, 
         '''Floppy device.'''),
        ('DVD', 2, 
         '''CD/DVD-ROM device.'''),
        ('HardDisk', 3, 
         '''Hard disk device.'''),
        ('Network', 4, 
         '''Network device.'''),
        ('USB', 5, 
         '''USB device.'''),
        ('SharedFolder', 6, 
         '''Shared folder device.'''),
        ] 


class DeviceActivity(Enum):
    """Device activity for <link to="IConsole::getDeviceActivity"/>."""
    __uuid__ = '6FC8AEAA-130A-4eb5-8954-3F921422D707'
    _enums = [\
        ('Null', 0, 
         ''''''),
        ('Idle', 1, 
         ''''''),
        ('Reading', 2, 
         ''''''),
        ('Writing', 3, 
         ''''''),
        ] 


class ClipboardMode(Enum):
    """Host-Guest clipboard interchange mode."""
    __uuid__ = '33364716-4008-4701-8f14-be0fa3d62950'
    _enums = [\
        ('Disabled', 0, 
         ''''''),
        ('HostToGuest', 1, 
         ''''''),
        ('GuestToHost', 2, 
         ''''''),
        ('Bidirectional', 3, 
         ''''''),
        ] 


class DragAndDropMode(Enum):
    """Drag'n'Drop interchange mode."""
    __uuid__ = 'b618ea0e-b6fb-4f8d-97f7-5e237e49b547'
    _enums = [\
        ('Disabled', 0, 
         ''''''),
        ('HostToGuest', 1, 
         ''''''),
        ('GuestToHost', 2, 
         ''''''),
        ('Bidirectional', 3, 
         ''''''),
        ] 


class Scope(Enum):
    """Scope of the operation.

      A generic enumeration used in various methods to define the action or
      argument scope."""
    __uuid__ = '7c91096e-499e-4eca-9f9b-9001438d7855'
    _enums = [\
        ('Global', 0, 
         ''''''),
        ('Machine', 1, 
         ''''''),
        ('Session', 2, 
         ''''''),
        ] 


class BIOSBootMenuMode(Enum):
    """BIOS boot menu mode."""
    __uuid__ = 'ae4fb9f7-29d2-45b4-b2c7-d579603135d5'
    _enums = [\
        ('Disabled', 0, 
         ''''''),
        ('MenuOnly', 1, 
         ''''''),
        ('MessageAndMenu', 2, 
         ''''''),
        ] 


class ProcessorFeature(Enum):
    """CPU features."""
    __uuid__ = '64c38e6b-8bcf-45ad-ac03-9b406287c5bf'
    _enums = [\
        ('HWVirtEx', 0, 
         ''''''),
        ('PAE', 1, 
         ''''''),
        ('LongMode', 2, 
         ''''''),
        ('NestedPaging', 3, 
         ''''''),
        ] 


class FirmwareType(Enum):
    """Firmware type."""
    __uuid__ = 'b903f264-c230-483e-ac74-2b37ce60d371'
    _enums = [\
        ('BIOS', 1, 
         '''BIOS Firmware.'''),
        ('EFI', 2, 
         '''EFI Firmware, bitness detected basing on OS type.'''),
        ('EFI32', 3, 
         '''Efi firmware, 32-bit.'''),
        ('EFI64', 4, 
         '''Efi firmware, 64-bit.'''),
        ('EFIDUAL', 5, 
         '''Efi firmware, combined 32 and 64-bit.'''),
        ] 


class PointingHIDType(Enum):
    """Type of pointing device used in a virtual machine."""
    __uuid__ = 'e44b2f7b-72ba-44fb-9e53-2186014f0d17'
    _enums = [\
        ('None', 1, 
         '''No mouse.'''),
        ('PS2Mouse', 2, 
         '''PS/2 auxiliary device, a.k.a. mouse.'''),
        ('USBMouse', 3, 
         '''USB mouse (relative pointer).'''),
        ('USBTablet', 4, 
         '''USB tablet (absolute pointer).'''),
        ('ComboMouse', 5, 
         '''Combined device, working as PS/2 or USB mouse, depending on guest behavior.
      Using of such device can have negative performance implications.'''),
        ] 


class KeyboardHIDType(Enum):
    """Type of keyboard device used in a virtual machine."""
    __uuid__ = '383e43d7-5c7c-4ec8-9cb8-eda1bccd6699'
    _enums = [\
        ('None', 1, 
         '''No keyboard.'''),
        ('PS2Keyboard', 2, 
         '''PS/2 keyboard.'''),
        ('USBKeyboard', 3, 
         '''USB keyboard.'''),
        ('ComboKeyboard', 4, 
         '''Combined device, working as PS/2 or USB keyboard, depending on guest behavior.
      Using of such device can have negative performance implications.'''),
        ] 


class DhcpOpt(Enum):
    """"""
    __uuid__ = '40d99bd3-3ece-44d2-a07e-1085fe9c4f0b'
    _enums = [\
        ('SubnetMask', 1, 
         ''''''),
        ('TimeOffset', 2, 
         ''''''),
        ('Router', 3, 
         ''''''),
        ('TimeServer', 4, 
         ''''''),
        ('NameServer', 5, 
         ''''''),
        ('DomainNameServer', 6, 
         ''''''),
        ('LogServer', 7, 
         ''''''),
        ('Cookie', 8, 
         ''''''),
        ('LPRServer', 9, 
         ''''''),
        ('ImpressServer', 10, 
         ''''''),
        ('ResourseLocationServer', 11, 
         ''''''),
        ('HostName', 12, 
         ''''''),
        ('BootFileSize', 13, 
         ''''''),
        ('MeritDumpFile', 14, 
         ''''''),
        ('DomainName', 15, 
         ''''''),
        ('SwapServer', 16, 
         ''''''),
        ('RootPath', 17, 
         ''''''),
        ('ExtensionPath', 18, 
         ''''''),
        ('IPForwardingEnableDisable', 19, 
         ''''''),
        ('NonLocalSourceRoutingEnableDisable', 20, 
         ''''''),
        ('PolicyFilter', 21, 
         ''''''),
        ('MaximumDatagramReassemblySize', 22, 
         ''''''),
        ('DefaultIPTime2Live', 23, 
         ''''''),
        ('PathMTUAgingTimeout', 24, 
         ''''''),
        ('IPLayerParametersPerInterface', 25, 
         ''''''),
        ('InterfaceMTU', 26, 
         ''''''),
        ('AllSubnetsAreLocal', 27, 
         ''''''),
        ('BroadcastAddress', 28, 
         ''''''),
        ('PerformMaskDiscovery', 29, 
         ''''''),
        ('MaskSupplier', 30, 
         ''''''),
        ('PerformRouteDiscovery', 31, 
         ''''''),
        ('RouterSolicitationAddress', 32, 
         ''''''),
        ('StaticRoute', 33, 
         ''''''),
        ('TrailerEncapsulation', 34, 
         ''''''),
        ('ARPCacheTimeout', 35, 
         ''''''),
        ('EthernetEncapsulation', 36, 
         ''''''),
        ('TCPDefaultTTL', 37, 
         ''''''),
        ('TCPKeepAliveInterval', 38, 
         ''''''),
        ('TCPKeepAliveGarbage', 39, 
         ''''''),
        ('NetworkInformationServiceDomain', 40, 
         ''''''),
        ('NetworkInformationServiceServers', 41, 
         ''''''),
        ('NetworkTimeProtocolServers', 42, 
         ''''''),
        ('VendorSpecificInformation', 43, 
         ''''''),
        ('Option_44', 44, 
         ''''''),
        ('Option_45', 45, 
         ''''''),
        ('Option_46', 46, 
         ''''''),
        ('Option_47', 47, 
         ''''''),
        ('Option_48', 48, 
         ''''''),
        ('Option_49', 49, 
         ''''''),
        ('IPAddressLeaseTime', 51, 
         ''''''),
        ('Option_64', 64, 
         ''''''),
        ('Option_65', 65, 
         ''''''),
        ('TFTPServerName', 66, 
         ''''''),
        ('BootfileName', 67, 
         ''''''),
        ('Option_68', 68, 
         ''''''),
        ('Option_69', 69, 
         ''''''),
        ('Option_70', 70, 
         ''''''),
        ('Option_71', 71, 
         ''''''),
        ('Option_72', 72, 
         ''''''),
        ('Option_73', 73, 
         ''''''),
        ('Option_74', 74, 
         ''''''),
        ('Option_75', 75, 
         ''''''),
        ('Option_119', 119, 
         ''''''),
        ] 


class VFSType(Enum):
    """Virtual file systems supported by VFSExplorer."""
    __uuid__ = '813999ba-b949-48a8-9230-aadc6285e2f2'
    _enums = [\
        ('File', 1, 
         ''''''),
        ('Cloud', 2, 
         ''''''),
        ('S3', 3, 
         ''''''),
        ('WebDav', 4, 
         ''''''),
        ] 


class VFSFileType(Enum):
    """File types known by VFSExplorer."""
    __uuid__ = '714333cd-44e2-415f-a245-d378fa9b1242'
    _enums = [\
        ('Unknown', 1, 
         ''''''),
        ('Fifo', 2, 
         ''''''),
        ('DevChar', 3, 
         ''''''),
        ('Directory', 4, 
         ''''''),
        ('DevBlock', 5, 
         ''''''),
        ('File', 6, 
         ''''''),
        ('SymLink', 7, 
         ''''''),
        ('Socket', 8, 
         ''''''),
        ('WhiteOut', 9, 
         ''''''),
        ] 


class ImportOptions(Enum):
    """Import options, used with <link to="IAppliance::importMachines"/>."""
    __uuid__ = '0a981523-3b20-4004-8ee3-dfd322202ace'
    _enums = [\
        ('KeepAllMACs', 1, 
         '''Don't generate new MAC addresses of the attached network adapters.'''),
        ('KeepNATMACs', 2, 
         '''Don't generate new MAC addresses of the attached network adapters when they are using NAT.'''),
        ] 


class VirtualSystemDescriptionType(Enum):
    """Used with <link to="IVirtualSystemDescription"/> to describe the type of
    a configuration value."""
    __uuid__ = '303c0900-a746-4612-8c67-79003e91f459'
    _enums = [\
        ('Ignore', 1, 
         ''''''),
        ('OS', 2, 
         ''''''),
        ('Name', 3, 
         ''''''),
        ('Product', 4, 
         ''''''),
        ('Vendor', 5, 
         ''''''),
        ('Version', 6, 
         ''''''),
        ('ProductUrl', 7, 
         ''''''),
        ('VendorUrl', 8, 
         ''''''),
        ('Description', 9, 
         ''''''),
        ('License', 10, 
         ''''''),
        ('Miscellaneous', 11, 
         ''''''),
        ('CPU', 12, 
         ''''''),
        ('Memory', 13, 
         ''''''),
        ('HardDiskControllerIDE', 14, 
         ''''''),
        ('HardDiskControllerSATA', 15, 
         ''''''),
        ('HardDiskControllerSCSI', 16, 
         ''''''),
        ('HardDiskControllerSAS', 17, 
         ''''''),
        ('HardDiskImage', 18, 
         ''''''),
        ('Floppy', 19, 
         ''''''),
        ('CDROM', 20, 
         ''''''),
        ('NetworkAdapter', 21, 
         ''''''),
        ('USBController', 22, 
         ''''''),
        ('SoundCard', 23, 
         ''''''),
        ('SettingsFile', 24, 
         '''Not used/implemented right now, will be added later in 4.1.x.'''),
        ] 


class VirtualSystemDescriptionValueType(Enum):
    """Used with <link to="IVirtualSystemDescription::getValuesByType"/> to describe the value
    type to fetch."""
    __uuid__ = '56d9403f-3425-4118-9919-36f2a9b8c77c'
    _enums = [\
        ('Reference', 1, 
         ''''''),
        ('Original', 2, 
         ''''''),
        ('Auto', 3, 
         ''''''),
        ('ExtraConfig', 4, 
         ''''''),
        ] 


class GraphicsControllerType(Enum):
    """Graphics controller type, used with <link to="IMachine::unregister"/>."""
    __uuid__ = '79c96ca0-9f39-4900-948e-68c41cbe127a'
    _enums = [\
        ('Null', 0, 
         '''Reserved value, invalid.'''),
        ('VBoxVGA', 1, 
         '''Default VirtualBox VGA device.'''),
        ] 


class CleanupMode(Enum):
    """Cleanup mode, used with <link to="IMachine::unregister"/>."""
    __uuid__ = '67897c50-7cca-47a9-83f6-ce8fd8eb5441'
    _enums = [\
        ('UnregisterOnly', 1, 
         '''Unregister only the machine, but neither delete snapshots nor detach media.'''),
        ('DetachAllReturnNone', 2, 
         '''Delete all snapshots and detach all media but return none; this will keep all media registered.'''),
        ('DetachAllReturnHardDisksOnly', 3, 
         '''Delete all snapshots, detach all media and return hard disks for closing, but not removable media.'''),
        ('Full', 4, 
         '''Delete all snapshots, detach all media and return all media for closing.'''),
        ] 


class CloneMode(Enum):
    """Clone mode, used with <link to="IMachine::cloneTo"/>."""
    __uuid__ = 'A7A159FE-5096-4B8D-8C3C-D033CB0B35A8'
    _enums = [\
        ('MachineState', 1, 
         '''Clone the state of the selected machine.'''),
        ('MachineAndChildStates', 2, 
         '''Clone the state of the selected machine and its child snapshots if present.'''),
        ('AllStates', 3, 
         '''Clone all states (including all snapshots) of the machine, regardless of the machine object used.'''),
        ] 


class CloneOptions(Enum):
    """Clone options, used with <link to="IMachine::cloneTo"/>."""
    __uuid__ = '22243f8e-96ab-497c-8cf0-f40a566c630b'
    _enums = [\
        ('Link', 1, 
         '''Create a clone VM where all virtual disks are linked to the original VM.'''),
        ('KeepAllMACs', 2, 
         '''Don't generate new MAC addresses of the attached network adapters.'''),
        ('KeepNATMACs', 3, 
         '''Don't generate new MAC addresses of the attached network adapters when they are using NAT.'''),
        ('KeepDiskNames', 4, 
         '''Don't change the disk names.'''),
        ] 


class AutostopType(Enum):
    """Autostop types, used with <link to="IMachine::autostopType"/>."""
    __uuid__ = '6bb96740-cf34-470d-aab2-2cd48ea2e10e'
    _enums = [\
        ('Disabled', 1, 
         '''Stopping the VM during system shutdown is disabled.'''),
        ('SaveState', 2, 
         '''The state of the VM will be saved when the system shuts down.'''),
        ('PowerOff', 3, 
         '''The VM is powered off when the system shuts down.'''),
        ('AcpiShutdown', 4, 
         '''An ACPI shutdown event is generated.'''),
        ] 


class HostNetworkInterfaceMediumType(Enum):
    """Type of encapsulation. Ethernet encapsulation includes both wired and
      wireless Ethernet connections.
      <link to="IHostNetworkInterface"/>"""
    __uuid__ = '1aa54aaf-2497-45a2-bfb1-8eb225e93d5b'
    _enums = [\
        ('Unknown', 0, 
         '''The type of interface cannot be determined.'''),
        ('Ethernet', 1, 
         '''Ethernet frame encapsulation.'''),
        ('PPP', 2, 
         '''Point-to-point protocol encapsulation.'''),
        ('SLIP', 3, 
         '''Serial line IP encapsulation.'''),
        ] 


class HostNetworkInterfaceStatus(Enum):
    """Current status of the interface.
      <link to="IHostNetworkInterface"/>"""
    __uuid__ = 'CC474A69-2710-434B-8D99-C38E5D5A6F41'
    _enums = [\
        ('Unknown', 0, 
         '''The state of interface cannot be determined.'''),
        ('Up', 1, 
         '''The interface is fully operational.'''),
        ('Down', 2, 
         '''The interface is not functioning.'''),
        ] 


class HostNetworkInterfaceType(Enum):
    """Network interface type."""
    __uuid__ = '67431b00-9946-48a2-bc02-b25c5919f4f3'
    _enums = [\
        ('Bridged', 1, 
         ''''''),
        ('HostOnly', 2, 
         ''''''),
        ] 


class AdditionsFacilityType(Enum):
    """Guest Additions facility IDs."""
    __uuid__ = '98f7f957-89fb-49b6-a3b1-31e3285eb1d8'
    _enums = [\
        ('None', 0, 
         '''No/invalid facility.'''),
        ('VBoxGuestDriver', 20, 
         '''VirtualBox base driver (VBoxGuest).'''),
        ('AutoLogon', 90, 
         '''Auto-logon modules (VBoxGINA, VBoxCredProv, pam_vbox).'''),
        ('VBoxService', 100, 
         '''VirtualBox system service (VBoxService).'''),
        ('VBoxTrayClient', 101, 
         '''VirtualBox desktop integration (VBoxTray on Windows, VBoxClient on non-Windows).'''),
        ('Seamless', 1000, 
         '''Seamless guest desktop integration.'''),
        ('Graphics', 1100, 
         '''Guest graphics mode. If not enabled, seamless rendering will not work, resize hints
        are not immediately acted on and guest display resizes are probably not initiated by
        the guest additions.'''),
        ('All', 2147483646, 
         '''All facilities selected.'''),
        ] 


class AdditionsFacilityClass(Enum):
    """Guest Additions facility classes."""
    __uuid__ = '446451b2-c88d-4e5d-84c9-91bc7f533f5f'
    _enums = [\
        ('None', 0, 
         '''No/invalid class.'''),
        ('Driver', 10, 
         '''Driver.'''),
        ('Service', 30, 
         '''System service.'''),
        ('Program', 50, 
         '''Program.'''),
        ('Feature', 100, 
         '''Feature.'''),
        ('ThirdParty', 999, 
         '''Third party.'''),
        ('All', 2147483646, 
         '''All facility classes selected.'''),
        ] 


class AdditionsFacilityStatus(Enum):
    """Guest Additions facility states."""
    __uuid__ = 'ce06f9e1-394e-4fe9-9368-5a88c567dbde'
    _enums = [\
        ('Inactive', 0, 
         '''Facility is not active.'''),
        ('Paused', 1, 
         '''Facility has been paused.'''),
        ('PreInit', 20, 
         '''Facility is preparing to initialize.'''),
        ('Init', 30, 
         '''Facility is initializing.'''),
        ('Active', 50, 
         '''Facility is up and running.'''),
        ('Terminating', 100, 
         '''Facility is shutting down.'''),
        ('Terminated', 101, 
         '''Facility successfully shut down.'''),
        ('Failed', 800, 
         '''Facility failed to start.'''),
        ('Unknown', 999, 
         '''Facility status is unknown.'''),
        ] 


class AdditionsRunLevelType(Enum):
    """Guest Additions run level type."""
    __uuid__ = 'a25417ee-a9dd-4f5b-b0dc-377860087754'
    _enums = [\
        ('None', 0, 
         '''Guest Additions are not loaded.'''),
        ('System', 1, 
         '''Guest drivers are loaded.'''),
        ('Userland', 2, 
         '''Common components (such as application services) are loaded.'''),
        ('Desktop', 3, 
         '''Per-user desktop components are loaded.'''),
        ] 


class AdditionsUpdateFlag(Enum):
    """Guest Additions update flags."""
    __uuid__ = '726a818d-18d6-4389-94e8-3e9e6826171a'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('WaitForUpdateStartOnly', 1, 
         '''Starts the regular updating process and waits until the
        actual Guest Additions update inside the guest was started.
        This can be necessary due to needed interaction with the guest
        OS during the installation phase.'''),
        ] 


class GuestSessionStatus(Enum):
    """Guest session status. This enumeration represents possible values of
      the <link to="IGuestSession::status"/> attribute."""
    __uuid__ = 'ac2669da-4624-44f2-85b5-0b0bfb8d8673'
    _enums = [\
        ('Undefined', 0, 
         '''Guest session is in an undefined state.'''),
        ('Starting', 10, 
         '''Guest session is being started.'''),
        ('Started', 100, 
         '''Guest session has been started.'''),
        ('Terminating', 480, 
         '''Guest session is being terminated.'''),
        ('Terminated', 500, 
         '''Guest session terminated normally.'''),
        ('TimedOutKilled', 512, 
         '''Guest session timed out and was killed.'''),
        ('TimedOutAbnormally', 513, 
         '''Guest session timed out and was not killed successfully.'''),
        ('Down', 600, 
         '''Service/OS is stopping, guest session was killed.'''),
        ('Error', 800, 
         '''Something went wrong.'''),
        ] 


class GuestSessionWaitForFlag(Enum):
    """Guest session waiting flags. Multiple flags can be combined."""
    __uuid__ = 'bb7a372a-f635-4e11-a81a-e707f3a52ef5'
    _enums = [\
        ('None', 0, 
         '''No waiting flags specified. Do not use this.'''),
        ('Start', 1, 
         '''Wait for the guest session being started.'''),
        ('Terminate', 2, 
         '''Wait for the guest session being terminated.'''),
        ('Status', 4, 
         '''Wait for the next guest session status change.'''),
        ] 


class GuestSessionWaitResult(Enum):
    """Guest session waiting results. Depending on the session waiting flags (for
      more information see <link to="GuestSessionWaitForFlag"/>) the waiting result
      can vary based on the session's current status.

      To wait for a guest session to terminate after it has been
      created by <link to="IGuest::createSession"/> one would specify
      GuestSessionWaitResult_Terminate."""
    __uuid__ = 'c0f6a8a5-fdb6-42bf-a582-56c6f82bcd2d'
    _enums = [\
        ('None', 0, 
         '''No result was returned. Not being used.'''),
        ('Start', 1, 
         '''The guest session has been started.'''),
        ('Terminate', 2, 
         '''The guest session has been terminated.'''),
        ('Status', 3, 
         '''The guest session has changed its status. The status then can
        be retrieved via <link to="IGuestSession::status"/>.'''),
        ('Error', 4, 
         '''Error while executing the process.'''),
        ('Timeout', 5, 
         '''The waiting operation timed out. This also will happen
        when no event has been occured matching the
        current waiting flags in a <link to="IGuestSession::waitFor"/> call.'''),
        ('WaitFlagNotSupported', 6, 
         '''A waiting flag specified in the <link to="IGuestSession::waitFor"/> call
        is not supported by the guest.'''),
        ] 


class FileSeekType(Enum):
    """File seeking types."""
    __uuid__ = '1b73f4f3-3515-4073-a506-76878d9e2541'
    _enums = [\
        ('Set', 0, 
         '''Seek from the start of the file.'''),
        ('Current', 1, 
         '''Seek from the current file position.'''),
        ] 


class ProcessInputFlag(Enum):
    """Guest process input flags."""
    __uuid__ = '5d38c1dd-2604-4ddf-92e5-0c0cdd3bdbd5'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('EndOfFile', 1, 
         '''End of file (input) reached.'''),
        ] 


class ProcessOutputFlag(Enum):
    """Guest process output flags for specifying which
      type of output to retrieve."""
    __uuid__ = '9979e85a-52bb-40b7-870c-57115e27e0f1'
    _enums = [\
        ('None', 0, 
         '''No flags set. Get output from stdout.'''),
        ('StdErr', 1, 
         '''Get output from stderr.'''),
        ] 


class ProcessWaitForFlag(Enum):
    """Process waiting flags. Multiple flags can be combined."""
    __uuid__ = '23b550c7-78e1-437e-98f0-65fd9757bcd2'
    _enums = [\
        ('None', 0, 
         '''No waiting flags specified. Do not use this.'''),
        ('Start', 1, 
         '''Wait for the process being started.'''),
        ('Terminate', 2, 
         '''Wait for the process being terminated.'''),
        ('StdIn', 4, 
         '''Wait for stdin becoming available.'''),
        ('StdOut', 8, 
         '''Wait for data becoming available on stdout.'''),
        ('StdErr', 16, 
         '''Wait for data becoming available on stderr.'''),
        ] 


class ProcessWaitResult(Enum):
    """Process waiting results. Depending on the process waiting flags (for
      more information see <link to="ProcessWaitForFlag"/>) the waiting result
      can vary based on the processes' current status.

      To wait for a guest process to terminate after it has been
      created by <link to="IGuestSession::processCreate"/> or <link to="IGuestSession::processCreateEx"/>
      one would specify ProcessWaitResult_Terminate.

      If a guest process has been started with ProcessCreateFlag_WaitForStdOut
      a client can wait with ProcessWaitResult_StdOut for new data to arrive on
      stdout; same applies for ProcessCreateFlag_WaitForStdErr and
      ProcessWaitResult_StdErr."""
    __uuid__ = '40719cbe-f192-4fe9-a231-6697b3c8e2b4'
    _enums = [\
        ('None', 0, 
         '''No result was returned. Not being used.'''),
        ('Start', 1, 
         '''The process has been started.'''),
        ('Terminate', 2, 
         '''The process has been terminated.'''),
        ('Status', 3, 
         '''The process has changed its status. The status then can
        be retrieved via <link to="IProcess::status"/>.'''),
        ('Error', 4, 
         '''Error while executing the process.'''),
        ('Timeout', 5, 
         '''The waiting operation timed out. This also will happen
        when no event has been occured matching the
        current waiting flags in a <link to="IProcess::waitFor"/> call.'''),
        ('StdIn', 6, 
         '''The process signalled that stdin became available for writing
        and that the process awaits input now.'''),
        ('StdOut', 7, 
         '''Data on stdout became available for reading.'''),
        ('StdErr', 8, 
         '''Data on stderr became available for reading.'''),
        ('WaitFlagNotSupported', 9, 
         '''A waiting flag specified in the <link to="IProcess::waitFor"/> call
        is not supported by the guest.'''),
        ] 


class CopyFileFlag(Enum):
    """File copying flags."""
    __uuid__ = '23f79fdf-738a-493d-b80b-42d607c9b916'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('Recursive', 1, 
         '''Copy directories recursively.'''),
        ('Update', 2, 
         '''Only copy when the source file is newer than the destination file or when the destination file is missing.'''),
        ('FollowLinks', 4, 
         '''Follow symbolic links.'''),
        ] 


class DirectoryCreateFlag(Enum):
    """Directory creation flags."""
    __uuid__ = 'bd721b0e-ced5-4f79-b368-249897c32a36'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('Parents', 1, 
         '''No error if existing, make parent directories as needed.'''),
        ] 


class DirectoryRemoveRecFlag(Enum):
    """Directory recursive removement flags."""
    __uuid__ = '455aabf0-7692-48f6-9061-f21579b65769'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('ContentAndDir', 1, 
         '''Delete the content of the directory and the directory itself.'''),
        ('ContentOnly', 2, 
         '''Only delete the content of the directory, omit the directory it self.'''),
        ] 


class PathRenameFlag(Enum):
    """Path renaming flags."""
    __uuid__ = 'f3baa09f-c758-453d-b91c-c7787d76351d'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('NoReplace', 1, 
         '''Do not replace anything.'''),
        ('Replace', 2, 
         '''This will replace attempt any target which isn't a directory.'''),
        ('NoSymlinks', 4, 
         '''Don't allow symbolic links as part of the path.'''),
        ] 


class ProcessCreateFlag(Enum):
    """Guest process execution flags."""
    __uuid__ = '35192799-bfde-405d-9bea-c735ab9998e4'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('WaitForProcessStartOnly', 1, 
         '''Only use the specified timeout value to wait for starting the guest process - the guest
        process itself then uses an infinite timeout.'''),
        ('IgnoreOrphanedProcesses', 2, 
         '''Do not report an error when executed processes are still alive when VBoxService or the guest OS is shutting down.'''),
        ('Hidden', 4, 
         '''Do not show the started process according to the guest OS guidelines.'''),
        ('NoProfile', 8, 
         '''Do not use the user's profile data when exeuting a process. Only available for Windows guests.'''),
        ('WaitForStdOut', 16, 
         '''The guest process waits until all data from stdout is read out.'''),
        ('WaitForStdErr', 32, 
         '''The guest process waits until all data from stderr is read out.'''),
        ('ExpandArguments', 64, 
         '''Expands environment variables in process arguments.'''),
        ] 


class ProcessPriority(Enum):
    """Process priorities."""
    __uuid__ = 'ee8cac50-e232-49fe-806b-d1214d9c2e49'
    _enums = [\
        ('Invalid', 0, 
         '''Invalid priority, do not use.'''),
        ('Default', 1, 
         '''Default process priority determined by the OS.'''),
        ] 


class SymlinkType(Enum):
    """Symbolic link types."""
    __uuid__ = '37794668-f8f1-4714-98a5-6f8fa2ed0118'
    _enums = [\
        ('Unknown', 0, 
         '''It is not known what is being targeted.'''),
        ('Directory', 1, 
         '''The link targets a directory.'''),
        ('File', 2, 
         '''The link targets a file (or whatever else).'''),
        ] 


class SymlinkReadFlag(Enum):
    """Symbolic link reading flags."""
    __uuid__ = 'b7fe2b9d-790e-4b25-8adf-1ca33026931f'
    _enums = [\
        ('None', 0, 
         '''No flags set.'''),
        ('NoSymlinks', 1, 
         '''Don't allow symbolic links as part of the path.'''),
        ] 


class ProcessStatus(Enum):
    """Process execution statuses."""
    __uuid__ = '4d52368f-5b48-4bfe-b486-acf89139b52f'
    _enums = [\
        ('Undefined', 0, 
         '''Process is in an undefined state.'''),
        ('Starting', 10, 
         '''Process is being started.'''),
        ('Started', 100, 
         '''Process has been started.'''),
        ('Paused', 110, 
         '''Process has been paused.'''),
        ('Terminating', 480, 
         '''Process is being terminated.'''),
        ('TerminatedNormally', 500, 
         '''Process terminated normally.'''),
        ('TerminatedSignal', 510, 
         '''Process terminated via signal.'''),
        ('TerminatedAbnormally', 511, 
         '''Process terminated abnormally.'''),
        ('TimedOutKilled', 512, 
         '''Process timed out and was killed.'''),
        ('TimedOutAbnormally', 513, 
         '''Process timed out and was not killed successfully.'''),
        ('Down', 600, 
         '''Service/OS is stopping, process was killed.'''),
        ('Error', 800, 
         '''Something went wrong.'''),
        ] 


class ProcessInputStatus(Enum):
    """Process input statuses."""
    __uuid__ = 'a4a0ef9c-29cc-4805-9803-c8215ae9da6c'
    _enums = [\
        ('Undefined', 0, 
         '''Undefined state.'''),
        ('Broken', 1, 
         '''Input pipe is broken.'''),
        ('Available', 10, 
         '''Input pipe became available for writing.'''),
        ('Written', 50, 
         '''Data has been successfully written.'''),
        ('Overflow', 100, 
         '''Too much input data supplied, data overflow.'''),
        ] 


class FileStatus(Enum):
    """File statuses."""
    __uuid__ = '8c86468b-b97b-4080-8914-e29f5b0abd2c'
    _enums = [\
        ('Undefined', 0, 
         '''File is in an undefined state.'''),
        ('Opening', 10, 
         '''Guest file is opening.'''),
        ('Open', 100, 
         '''Guest file has been successfully opened.'''),
        ('Closing', 150, 
         '''Guest file closing.'''),
        ('Closed', 200, 
         '''Guest file has been closed.'''),
        ('Down', 600, 
         '''Service/OS is stopping, guest file was closed.'''),
        ('Error', 800, 
         '''Something went wrong.'''),
        ] 


class FsObjType(Enum):
    """File system object type."""
    __uuid__ = 'a1ed437c-b3c3-4ca2-b19c-4239d658d5e8'
    _enums = [\
        ('Undefined', 0, 
         '''Type is undefined / unknown.'''),
        ('FIFO', 1, 
         '''Named pipe.'''),
        ('DevChar', 10, 
         '''Character device.'''),
        ('DevBlock', 11, 
         '''Block device.'''),
        ('Directory', 50, 
         '''Directory.'''),
        ('File', 80, 
         '''File.'''),
        ('Symlink', 100, 
         '''Symlink.'''),
        ('Socket', 200, 
         '''Socket.'''),
        ('Whiteout', 400, 
         '''Whiteout.'''),
        ] 


class DragAndDropAction(Enum):
    """Possible actions within an Drag and Drop operation."""
    __uuid__ = '47f3b162-c107-4fcd-bfa7-54b8135c441e'
    _enums = [\
        ('Ignore', 0, 
         '''Do nothing.'''),
        ('Copy', 1, 
         '''Copy the item to the target.'''),
        ('Move', 2, 
         '''Move the item to the target.'''),
        ('Link', 3, 
         '''Link the item from within the target.'''),
        ] 


class DirectoryOpenFlag(Enum):
    """Directory open flags."""
    __uuid__ = '5138837a-8fd2-4194-a1b0-08f7bc3949d0'
    _enums = [\
        ('None', 0, 
         '''No flag set.'''),
        ('NoSymlinks', 1, 
         '''Don't allow symbolic links as part of the path.'''),
        ] 


class MediumState(Enum):
    """Virtual medium state.
      <link to="IMedium"/>"""
    __uuid__ = 'ef41e980-e012-43cd-9dea-479d4ef14d13'
    _enums = [\
        ('NotCreated', 0, 
         '''Associated medium storage does not exist (either was not created yet or
        was deleted).'''),
        ('Created', 1, 
         '''Associated storage exists and accessible; this gets set if the
        accessibility check performed by <link to="IMedium::refreshState"/>
        was successful.'''),
        ('LockedRead', 2, 
         '''Medium is locked for reading (see <link to="IMedium::lockRead"/>),
        no data modification is possible.'''),
        ('LockedWrite', 3, 
         '''Medium is locked for writing (see <link to="IMedium::lockWrite"/>),
        no concurrent data reading or modification is possible.'''),
        ('Inaccessible', 4, 
         '''Medium accessibility check (see <link to="IMedium::refreshState"/>) has
        not yet been performed, or else, associated medium storage is not
        accessible. In the first case, <link to="IMedium::lastAccessError"/>
        is empty, in the second case, it describes the error that occurred.'''),
        ('Creating', 5, 
         '''Associated medium storage is being created.'''),
        ('Deleting', 6, 
         '''Associated medium storage is being deleted.'''),
        ] 


class MediumType(Enum):
    """Virtual medium type. For each <link to="IMedium"/>, this defines how the medium is
      attached to a virtual machine (see <link to="IMediumAttachment"/>) and what happens
      when a snapshot (see <link to="ISnapshot"/>) is taken of a virtual machine which has
      the medium attached. At the moment DVD and floppy media are always of type "writethrough"."""
    __uuid__ = 'fe663fb5-c244-4e1b-9d81-c628b417dd04'
    _enums = [\
        ('Normal', 0, 
         '''Normal medium (attached directly or indirectly, preserved
        when taking snapshots).'''),
        ('Immutable', 1, 
         '''Immutable medium (attached indirectly, changes are wiped out
        the next time the virtual machine is started).'''),
        ('Writethrough', 2, 
         '''Write through medium (attached directly, ignored when
        taking snapshots).'''),
        ('Shareable', 3, 
         '''Allow using this medium concurrently by several machines.
        Present since VirtualBox 3.2.0, and accepted since 3.2.8.'''),
        ('Readonly', 4, 
         '''A readonly medium, which can of course be used by several machines.
        Present and accepted since VirtualBox 4.0.'''),
        ('MultiAttach', 5, 
         '''A medium which is indirectly attached, so that one base medium can
        be used for several VMs which have their own differencing medium to
        store their modifications. In some sense a variant of Immutable
        with unset AutoReset flag in each differencing medium.
        Present and accepted since VirtualBox 4.0.'''),
        ] 


class MediumVariant(Enum):
    """Virtual medium image variant. More than one flag may be set.
      <link to="IMedium"/>"""
    __uuid__ = '80685b6b-e42f-497d-8271-e77bf3c61ada'
    _enums = [\
        ('Standard', 0, 
         '''No particular variant requested, results in using the backend default.'''),
        ('VmdkSplit2G', 1, 
         '''VMDK image split in chunks of less than 2GByte.'''),
        ('VmdkRawDisk', 2, 
         '''VMDK image representing a raw disk.'''),
        ('VmdkStreamOptimized', 4, 
         '''VMDK streamOptimized image. Special import/export format which is
        read-only/append-only.'''),
        ('VmdkESX', 8, 
         '''VMDK format variant used on ESX products.'''),
        ('Fixed', 65536, 
         '''Fixed image. Only allowed for base images.'''),
        ('Diff', 131072, 
         '''Differencing image. Only allowed for child images.'''),
        ('NoCreateDir', 1073741824, 
         '''Special flag which suppresses automatic creation of the subdirectory.
        Only used when passing the medium variant as an input parameter.'''),
        ] 


class DataType(Enum):
    """"""
    __uuid__ = 'd90ea51e-a3f1-4a01-beb1-c1723c0d3ba7'
    _enums = [\
        ('Int32', 0, 
         ''''''),
        ('Int8', 1, 
         ''''''),
        ('String', 2, 
         ''''''),
        ] 


class DataFlags(Enum):
    """"""
    __uuid__ = '86884dcf-1d6b-4f1b-b4bf-f5aa44959d60'
    _enums = [\
        ('None', 0, 
         ''''''),
        ('Mandatory', 1, 
         ''''''),
        ('Expert', 2, 
         ''''''),
        ('Array', 4, 
         ''''''),
        ('FlagMask', 7, 
         ''''''),
        ] 


class MediumFormatCapabilities(Enum):
    """Medium format capability flags."""
    __uuid__ = '7342ba79-7ce0-4d94-8f86-5ed5a185d9bd'
    _enums = [\
        ('Uuid', 1, 
         '''Supports UUIDs as expected by VirtualBox code.'''),
        ('CreateFixed', 2, 
         '''Supports creating fixed size images, allocating all space instantly.'''),
        ('CreateDynamic', 4, 
         '''Supports creating dynamically growing images, allocating space on
        demand.'''),
        ('CreateSplit2G', 8, 
         '''Supports creating images split in chunks of a bit less than 2 GBytes.'''),
        ('Differencing', 16, 
         '''Supports being used as a format for differencing media (see <link to="IMedium::createDiffStorage"/>).'''),
        ('Asynchronous', 32, 
         '''Supports asynchronous I/O operations for at least some configurations.'''),
        ('File', 64, 
         '''The format backend operates on files (the <link to="IMedium::location"/>
        attribute of the medium specifies a file used to store medium
        data; for a list of supported file extensions see
        <link to="IMediumFormat::describeFileExtensions"/>).'''),
        ('Properties', 128, 
         '''The format backend uses the property interface to configure the storage
        location and properties (the <link to="IMediumFormat::describeProperties"/>
        method is used to get access to properties supported by the given medium format).'''),
        ('TcpNetworking', 256, 
         '''The format backend uses the TCP networking interface for network access.'''),
        ('VFS', 512, 
         '''The format backend supports virtual filesystem functionality.'''),
        ('CapabilityMask', 1023, 
         ''''''),
        ] 


class MouseButtonState(Enum):
    """Mouse button state."""
    __uuid__ = '9ee094b8-b28a-4d56-a166-973cb588d7f8'
    _enums = [\
        ('LeftButton', 1, 
         ''''''),
        ('RightButton', 2, 
         ''''''),
        ('MiddleButton', 4, 
         ''''''),
        ('WheelUp', 8, 
         ''''''),
        ('WheelDown', 16, 
         ''''''),
        ('XButton1', 32, 
         ''''''),
        ('XButton2', 64, 
         ''''''),
        ('MouseStateMask', 127, 
         ''''''),
        ] 


class FramebufferPixelFormat(Enum):
    """Format of the video memory buffer. Constants represented by this enum can
      be used to test for particular values of <link to="IFramebuffer::pixelFormat"/>.

      See also www.fourcc.org for more information about FOURCC pixel formats."""
    __uuid__ = '7acfd5ed-29e3-45e3-8136-73c9224f3d2d'
    _enums = [\
        ('Opaque', 0, 
         '''Unknown buffer format (the user may not assume any particular format of
        the buffer).'''),
        ('FOURCC_RGB', 843204434, 
         '''Basic RGB format (<link to="IFramebuffer::bitsPerPixel"/> determines the
        bit layout).'''),
        ] 


class NetworkAttachmentType(Enum):
    """Network attachment type."""
    __uuid__ = '2ac4bc71-6b82-417a-acd1-f7426d2570d6'
    _enums = [\
        ('Null', 0, 
         '''Null value, also means "not attached".'''),
        ('NAT', 1, 
         ''''''),
        ('Bridged', 2, 
         ''''''),
        ('Internal', 3, 
         ''''''),
        ('HostOnly', 4, 
         ''''''),
        ('Generic', 5, 
         ''''''),
        ] 


class NetworkAdapterType(Enum):
    """Network adapter type."""
    __uuid__ = '3c2281e4-d952-4e87-8c7d-24379cb6a81c'
    _enums = [\
        ('Null', 0, 
         '''Null value (never used by the API).'''),
        ('Am79C970A', 1, 
         '''AMD PCNet-PCI II network card (Am79C970A).'''),
        ('Am79C973', 2, 
         '''AMD PCNet-FAST III network card (Am79C973).'''),
        ('I82540EM', 3, 
         '''Intel PRO/1000 MT Desktop network card (82540EM).'''),
        ('I82543GC', 4, 
         '''Intel PRO/1000 T Server network card (82543GC).'''),
        ('I82545EM', 5, 
         '''Intel PRO/1000 MT Server network card (82545EM).'''),
        ('Virtio', 6, 
         '''Virtio network device.'''),
        ] 


class NetworkAdapterPromiscModePolicy(Enum):
    """The promiscuous mode policy of an interface."""
    __uuid__ = 'c963768a-376f-4c85-8d84-d8ced4b7269e'
    _enums = [\
        ('Deny', 1, 
         '''Deny promiscuous mode requests.'''),
        ('AllowNetwork', 2, 
         '''Allow promicuous mode, but restrict the scope it to the internal
        network so that it only applies to other VMs.'''),
        ('AllowAll', 3, 
         '''Allow promicuous mode, include unrelated traffic going over the wire
        and internally on the host.'''),
        ] 


class PortMode(Enum):
    """The PortMode enumeration represents possible communication modes for
      the virtual serial port device."""
    __uuid__ = '533b5fe3-0185-4197-86a7-17e37dd39d76'
    _enums = [\
        ('Disconnected', 0, 
         '''Virtual device is not attached to any real host device.'''),
        ('HostPipe', 1, 
         '''Virtual device is attached to a host pipe.'''),
        ('HostDevice', 2, 
         '''Virtual device is attached to a host device.'''),
        ('RawFile', 3, 
         '''Virtual device is attached to a raw file.'''),
        ] 


class USBDeviceState(Enum):
    """USB device state. This enumeration represents all possible states
      of the USB device physically attached to the host computer regarding
      its state on the host computer and availability to guest computers
      (all currently running virtual machines).

      Once a supported USB device is attached to the host, global USB
      filters (<link to="IHost::USBDeviceFilters"/>) are activated. They can
      either ignore the device, or put it to USBDeviceState_Held state, or do
      nothing. Unless the device is ignored by global filters, filters of all
      currently running guests (<link to="IUSBController::deviceFilters"/>) are
      activated that can put it to USBDeviceState_Captured state.

      If the device was ignored by global filters, or didn't match
      any filters at all (including guest ones), it is handled by the host
      in a normal way. In this case, the device state is determined by
      the host and can be one of USBDeviceState_Unavailable, USBDeviceState_Busy
      or USBDeviceState_Available, depending on the current device usage.

      Besides auto-capturing based on filters, the device can be manually
      captured by guests (<link to="IConsole::attachUSBDevice"/>) if its
      state is USBDeviceState_Busy, USBDeviceState_Available or
      USBDeviceState_Held.

      
        Due to differences in USB stack implementations in Linux and Win32,
        states USBDeviceState_Busy and USBDeviceState_Unavailable are applicable
        only to the Linux version of the product. This also means that (<link to="IConsole::attachUSBDevice"/>) can only succeed on Win32 if the
        device state is USBDeviceState_Held.
      

      <link to="IHostUSBDevice"/>, <link to="IHostUSBDeviceFilter"/>"""
    __uuid__ = 'b99a2e65-67fb-4882-82fd-f3e5e8193ab4'
    _enums = [\
        ('NotSupported', 0, 
         '''Not supported by the VirtualBox server, not available to guests.'''),
        ('Unavailable', 1, 
         '''Being used by the host computer exclusively,
        not available to guests.'''),
        ('Busy', 2, 
         '''Being used by the host computer, potentially available to guests.'''),
        ('Available', 3, 
         '''Not used by the host computer, available to guests (the host computer
        can also start using the device at any time).'''),
        ('Held', 4, 
         '''Held by the VirtualBox server (ignored by the host computer),
        available to guests.'''),
        ('Captured', 5, 
         '''Captured by one of the guest computers, not available
        to anybody else.'''),
        ] 


class USBDeviceFilterAction(Enum):
    """Actions for host USB device filters.
      <link to="IHostUSBDeviceFilter"/>, <link to="USBDeviceState"/>"""
    __uuid__ = 'cbc30a49-2f4e-43b5-9da6-121320475933'
    _enums = [\
        ('Null', 0, 
         '''Null value (never used by the API).'''),
        ('Ignore', 1, 
         '''Ignore the matched USB device.'''),
        ('Hold', 2, 
         '''Hold the matched USB device.'''),
        ] 


class AudioDriverType(Enum):
    """Host audio driver type."""
    __uuid__ = '4bcc3d73-c2fe-40db-b72f-0c2ca9d68496'
    _enums = [\
        ('Null', 0, 
         '''Null value, also means "dummy audio driver".'''),
        ('WinMM', 1, 
         '''Windows multimedia (Windows hosts only).'''),
        ('OSS', 2, 
         '''Open Sound System (Linux hosts only).'''),
        ('ALSA', 3, 
         '''Advanced Linux Sound Architecture (Linux hosts only).'''),
        ('DirectSound', 4, 
         '''DirectSound (Windows hosts only).'''),
        ('CoreAudio', 5, 
         '''CoreAudio (Mac hosts only).'''),
        ('MMPM', 6, 
         '''Reserved for historical reasons.'''),
        ('Pulse', 7, 
         '''PulseAudio (Linux hosts only).'''),
        ('SolAudio', 8, 
         '''Solaris audio (Solaris hosts only).'''),
        ] 


class AudioControllerType(Enum):
    """Virtual audio controller type."""
    __uuid__ = '7afd395c-42c3-444e-8788-3ce80292f36c'
    _enums = [\
        ('AC97', 0, 
         ''''''),
        ('SB16', 1, 
         ''''''),
        ('HDA', 2, 
         ''''''),
        ] 


class AuthType(Enum):
    """VirtualBox authentication type."""
    __uuid__ = '7eef6ef6-98c2-4dc2-ab35-10d2b292028d'
    _enums = [\
        ('Null', 0, 
         '''Null value, also means "no authentication".'''),
        ('External', 1, 
         ''''''),
        ('Guest', 2, 
         ''''''),
        ] 


class Reason(Enum):
    """Internal event reason type."""
    __uuid__ = 'e7e8e097-299d-4e98-8bbc-c31c2d47d0cc'
    _enums = [\
        ('Unspecified', 0, 
         '''Null value, means "no known reason".'''),
        ('HostSuspend', 1, 
         '''Host is being suspended (power management event).'''),
        ('HostResume', 2, 
         '''Host is being resumed (power management event).'''),
        ('HostBatteryLow', 3, 
         '''Host is running low on battery (power management event).'''),
        ] 


class StorageBus(Enum):
    """The bus type of the storage controller (IDE, SATA, SCSI, SAS or Floppy);
      see <link to="IStorageController::bus"/>."""
    __uuid__ = 'eee67ab3-668d-4ef5-91e0-7025fe4a0d7a'
    _enums = [\
        ('Null', 0, 
         '''@c null value. Never used by the API.'''),
        ('IDE', 1, 
         ''''''),
        ('SATA', 2, 
         ''''''),
        ('SCSI', 3, 
         ''''''),
        ('Floppy', 4, 
         ''''''),
        ('SAS', 5, 
         ''''''),
        ] 


class StorageControllerType(Enum):
    """The exact variant of storage controller hardware presented
      to the guest; see <link to="IStorageController::controllerType"/>."""
    __uuid__ = '8a412b8a-f43e-4456-bd37-b474f0879a58'
    _enums = [\
        ('Null', 0, 
         '''@c null value. Never used by the API.'''),
        ('LsiLogic', 1, 
         '''A SCSI controller of the LsiLogic variant.'''),
        ('BusLogic', 2, 
         '''A SCSI controller of the BusLogic variant.'''),
        ('IntelAhci', 3, 
         '''An Intel AHCI SATA controller; this is the only variant for SATA.'''),
        ('PIIX3', 4, 
         '''An IDE controller of the PIIX3 variant.'''),
        ('PIIX4', 5, 
         '''An IDE controller of the PIIX4 variant.'''),
        ('ICH6', 6, 
         '''An IDE controller of the ICH6 variant.'''),
        ('I82078', 7, 
         '''A floppy disk controller; this is the only variant for floppy drives.'''),
        ('LsiLogicSas', 8, 
         '''A variant of the LsiLogic controller using SAS.'''),
        ] 


class ChipsetType(Enum):
    """Type of emulated chipset (mostly southbridge)."""
    __uuid__ = '8b4096a8-a7c3-4d3b-bbb1-05a0a51ec394'
    _enums = [\
        ('Null', 0, 
         '''@c null value. Never used by the API.'''),
        ('PIIX3', 1, 
         '''A PIIX3 (PCI IDE ISA Xcelerator) chipset.'''),
        ('ICH9', 2, 
         '''A ICH9 (I/O Controller Hub) chipset.'''),
        ] 


class NATAliasMode(Enum):
    """<desc/>"""
    __uuid__ = '67772168-50d9-11df-9669-7fb714ee4fa1'
    _enums = [\
        ('AliasLog', 1, 
         '''<desc/>'''),
        ('AliasProxyOnly', 2, 
         '''<desc/>'''),
        ('AliasUseSamePorts', 4, 
         '''<desc/>'''),
        ] 


class NATProtocol(Enum):
    """Protocol definitions used with NAT port-forwarding rules."""
    __uuid__ = 'e90164be-eb03-11de-94af-fff9b1c1b19f'
    _enums = [\
        ('UDP', 0, 
         '''Port-forwarding uses UDP protocol.'''),
        ('TCP', 1, 
         '''Port-forwarding uses TCP protocol.'''),
        ] 


class BandwidthGroupType(Enum):
    """Type of a bandwidth control group."""
    __uuid__ = '1d92b67d-dc69-4be9-ad4c-93a01e1e0c8e'
    _enums = [\
        ('Null', 0, 
         '''Null type, must be first.'''),
        ('Disk', 1, 
         '''The bandwidth group controls disk I/O.'''),
        ('Network', 2, 
         '''The bandwidth group controls network I/O.'''),
        ] 


class VBoxEventType(Enum):
    """Type of an event.
      See <link to="IEvent"/> for an introduction to VirtualBox event handling."""
    __uuid__ = 'f019b8c7-22a6-468a-9f7c-3443b7b6c40a'
    _enums = [\
        ('Invalid', 0, 
         '''Invalid event, must be first.'''),
        ('Any', 1, 
         '''Wildcard for all events.
        Events of this type are never delivered, and only used in
        <link to="IEventSource::registerListener"/> call to simplify registration.'''),
        ('Vetoable', 2, 
         '''Wildcard for all vetoable events. Events of this type are never delivered, and only
        used in <link to="IEventSource::registerListener"/> call to simplify registration.'''),
        ('MachineEvent', 3, 
         '''Wildcard for all machine events. Events of this type are never delivered, and only used in
        <link to="IEventSource::registerListener"/> call to simplify registration.'''),
        ('SnapshotEvent', 4, 
         '''Wildcard for all snapshot events. Events of this type are never delivered, and only used in
        <link to="IEventSource::registerListener"/> call to simplify registration.'''),
        ('InputEvent', 5, 
         '''Wildcard for all input device (keyboard, mouse) events.
        Events of this type are never delivered, and only used in
        <link to="IEventSource::registerListener"/> call to simplify registration.'''),
        ('LastWildcard', 31, 
         '''Last wildcard.'''),
        ('OnMachineStateChanged', 32, 
         '''See <link to="IMachineStateChangedEvent">IMachineStateChangedEvent</link>.'''),
        ('OnMachineDataChanged', 33, 
         '''See <link to="IMachineDataChangedEvent">IMachineDataChangedEvent</link>.'''),
        ('OnExtraDataChanged', 34, 
         '''See <link to="IExtraDataChangedEvent">IExtraDataChangedEvent</link>.'''),
        ('OnExtraDataCanChange', 35, 
         '''See <link to="IExtraDataCanChangeEvent">IExtraDataCanChangeEvent</link>.'''),
        ('OnMediumRegistered', 36, 
         '''See <link to="IMediumRegisteredEvent">IMediumRegisteredEvent</link>.'''),
        ('OnMachineRegistered', 37, 
         '''See <link to="IMachineRegisteredEvent">IMachineRegisteredEvent</link>.'''),
        ('OnSessionStateChanged', 38, 
         '''See <link to="ISessionStateChangedEvent">ISessionStateChangedEvent</link>.'''),
        ('OnSnapshotTaken', 39, 
         '''See <link to="ISnapshotTakenEvent">ISnapshotTakenEvent</link>.'''),
        ('OnSnapshotDeleted', 40, 
         '''See <link to="ISnapshotDeletedEvent">ISnapshotDeletedEvent</link>.'''),
        ('OnSnapshotChanged', 41, 
         '''See <link to="ISnapshotChangedEvent">ISnapshotChangedEvent</link>.'''),
        ('OnGuestPropertyChanged', 42, 
         '''See <link to="IGuestPropertyChangedEvent">IGuestPropertyChangedEvent</link>.'''),
        ('OnMousePointerShapeChanged', 43, 
         '''See <link to="IMousePointerShapeChangedEvent">IMousePointerShapeChangedEvent</link>.'''),
        ('OnMouseCapabilityChanged', 44, 
         '''See <link to="IMouseCapabilityChangedEvent">IMouseCapabilityChangedEvent</link>.'''),
        ('OnKeyboardLedsChanged', 45, 
         '''See <link to="IKeyboardLedsChangedEvent">IKeyboardLedsChangedEvent</link>.'''),
        ('OnStateChanged', 46, 
         '''See <link to="IStateChangedEvent">IStateChangedEvent</link>.'''),
        ('OnAdditionsStateChanged', 47, 
         '''See <link to="IAdditionsStateChangedEvent">IAdditionsStateChangedEvent</link>.'''),
        ('OnNetworkAdapterChanged', 48, 
         '''See <link to="INetworkAdapterChangedEvent">INetworkAdapterChangedEvent</link>.'''),
        ('OnSerialPortChanged', 49, 
         '''See <link to="ISerialPortChangedEvent">ISerialPortChangedEvent</link>.'''),
        ('OnParallelPortChanged', 50, 
         '''See <link to="IParallelPortChangedEvent">IParallelPortChangedEvent</link>.'''),
        ('OnStorageControllerChanged', 51, 
         '''See <link to="IStorageControllerChangedEvent">IStorageControllerChangedEvent</link>.'''),
        ('OnMediumChanged', 52, 
         '''See <link to="IMediumChangedEvent">IMediumChangedEvent</link>.'''),
        ('OnVRDEServerChanged', 53, 
         '''See <link to="IVRDEServerChangedEvent">IVRDEServerChangedEvent</link>.'''),
        ('OnUSBControllerChanged', 54, 
         '''See <link to="IUSBControllerChangedEvent">IUSBControllerChangedEvent</link>.'''),
        ('OnUSBDeviceStateChanged', 55, 
         '''See <link to="IUSBDeviceStateChangedEvent">IUSBDeviceStateChangedEvent</link>.'''),
        ('OnSharedFolderChanged', 56, 
         '''See <link to="ISharedFolderChangedEvent">ISharedFolderChangedEvent</link>.'''),
        ('OnRuntimeError', 57, 
         '''See <link to="IRuntimeErrorEvent">IRuntimeErrorEvent</link>.'''),
        ('OnCanShowWindow', 58, 
         '''See <link to="ICanShowWindowEvent">ICanShowWindowEvent</link>.'''),
        ('OnShowWindow', 59, 
         '''See <link to="IShowWindowEvent">IShowWindowEvent</link>.'''),
        ('OnCPUChanged', 60, 
         '''See <link to="ICPUChangedEvent">ICPUChangedEvent</link>.'''),
        ('OnVRDEServerInfoChanged', 61, 
         '''See <link to="IVRDEServerInfoChangedEvent">IVRDEServerInfoChangedEvent</link>.'''),
        ('OnEventSourceChanged', 62, 
         '''See <link to="IEventSourceChangedEvent">IEventSourceChangedEvent</link>.'''),
        ('OnCPUExecutionCapChanged', 63, 
         '''See <link to="ICPUExecutionCapChangedEvent">ICPUExecutionCapChangedEvent</link>.'''),
        ('OnGuestKeyboard', 64, 
         '''See <link to="IGuestKeyboardEvent">IGuestKeyboardEvent</link>.'''),
        ('OnGuestMouse', 65, 
         '''See <link to="IGuestMouseEvent">IGuestMouseEvent</link>.'''),
        ('OnNATRedirect', 66, 
         '''See <link to="INATRedirectEvent">INATRedirectEvent</link>.'''),
        ('OnHostPCIDevicePlug', 67, 
         '''See <link to="IHostPCIDevicePlugEvent">IHostPCIDevicePlugEvent</link>.'''),
        ('OnVBoxSVCAvailabilityChanged', 68, 
         '''See <link to="IVBoxSVCAvailabilityChangedEvent">IVBoxSVCAvailablityChangedEvent</link>.'''),
        ('OnBandwidthGroupChanged', 69, 
         '''See <link to="IBandwidthGroupChangedEvent">IBandwidthGroupChangedEvent</link>.'''),
        ('OnGuestMonitorChanged', 70, 
         '''See <link to="IGuestMonitorChangedEvent">IGuestMonitorChangedEvent</link>.'''),
        ('OnStorageDeviceChanged', 71, 
         '''See <link to="IStorageDeviceChangedEvent">IStorageDeviceChangedEvent</link>.'''),
        ('OnClipboardModeChanged', 72, 
         '''See <link to="IClipboardModeChangedEvent">IClipboardModeChangedEvent</link>.'''),
        ('OnDragAndDropModeChanged', 73, 
         '''See <link to="IDragAndDropModeChangedEvent">IDragAndDropModeChangedEvent</link>.'''),
        ('OnNATNetworkChanged', 74, 
         '''See <link to="INATNetworkChangedEvent">INATNetworkChangedEvent</link>.'''),
        ('OnNATNetworkStartStop', 75, 
         '''See <link to="INATNetworkStartStopEvent">INATNetworkStartStopEvent</link>.'''),
        ('OnNATNetworkAlter', 76, 
         '''See <link to="INATNetworkAlterEvent">INATNetworkAlterEvent</link>.'''),
        ('OnNATNetworkCreationDeletion', 77, 
         '''See <link to="INATNetworkCreationDeletionEvent">INATNetworkCreationDeletionEvent</link>.'''),
        ('OnNATNetworkSetting', 78, 
         '''See <link to="INATNetworkSettingEvent">INATNetworkSettingEvent</link>.'''),
        ('OnNATNetworkPortForward', 79, 
         '''See <link to="INATNetworkPortForwardEvent">INATNetworkPortForwardEvent</link>.'''),
        ('OnGuestSessionStateChanged', 80, 
         '''See <link to="IGuestSessionStateChangedEvent">IGuestSessionStateChangedEvent</link>.'''),
        ('OnGuestSessionRegistered', 81, 
         '''See <link to="IGuestSessionRegisteredEvent">IGuestSessionRegisteredEvent</link>.'''),
        ('OnGuestProcessRegistered', 82, 
         '''See <link to="IGuestProcessRegisteredEvent">IGuestProcessRegisteredEvent</link>.'''),
        ('OnGuestProcessStateChanged', 83, 
         '''See <link to="IGuestProcessStateChangedEvent">IGuestProcessStateChangedEvent</link>.'''),
        ('OnGuestProcessInputNotify', 84, 
         '''See <link to="IGuestProcessInputNotifyEvent">IGuestProcessInputNotifyEvent</link>.'''),
        ('OnGuestProcessOutput', 85, 
         '''See <link to="IGuestProcessOutputEvent">IGuestProcessOutputEvent</link>.'''),
        ('OnGuestFileRegistered', 86, 
         '''See <link to="IGuestFileRegisteredEvent">IGuestFileRegisteredEvent</link>.'''),
        ('OnGuestFileStateChanged', 87, 
         '''See <link to="IGuestFileStateChangedEvent">IGuestFileStateChangedEvent</link>.'''),
        ('OnGuestFileOffsetChanged', 88, 
         '''See <link to="IGuestFileOffsetChangedEvent">IGuestFileOffsetChangedEvent</link>.'''),
        ('OnGuestFileRead', 89, 
         '''See <link to="IGuestFileReadEvent">IGuestFileReadEvent</link>.

        <note internal="yes">For performance reasons this is a separate event to
          not unnecessarily overflow the event queue.'''),
        ('OnGuestFileWrite', 90, 
         '''See <link to="IGuestFileWriteEvent">IGuestFileWriteEvent</link>.

        <note internal="yes">For performance reasons this is a separate event to
          not unnecessarily overflow the event queue.'''),
        ('OnVideoCaptureChanged', 91, 
         '''See <link to="IVideoCaptureChangedEvent">IVideoCapturedChangeEvent</link>.'''),
        ('Last', 92, 
         '''Must be last event, used for iterations and structures relying on numerical event values.'''),
        ] 


class GuestMonitorChangedEventType(Enum):
    """How the guest monitor has been changed."""
    __uuid__ = 'ef172985-7e36-4297-95be-e46396968d66'
    _enums = [\
        ('Enabled', 0, 
         '''The guest monitor has been enabled by the guest.'''),
        ('Disabled', 1, 
         '''The guest monitor has been disabled by the guest.'''),
        ('NewOrigin', 2, 
         '''The guest monitor origin has changed in the guest.'''),
        ] 


class IVirtualBoxErrorInfo(Interface):
    """
    The IVirtualBoxErrorInfo interface represents extended error information.

      Extended error information can be set by VirtualBox components after
      unsuccessful or partially successful method invocation. This information
      can be retrieved by the calling party as an IVirtualBoxErrorInfo object
      and then shown to the client in addition to the plain 32-bit result code.

      In MS COM, this interface extends the IErrorInfo interface,
      in XPCOM, it extends the nsIException interface. In both cases,
      it provides a set of common attributes to retrieve error
      information.

      Sometimes invocation of some component's method may involve methods of
      other components that may also fail (independently of this method's
      failure), or a series of non-fatal errors may precede a fatal error that
      causes method failure. In cases like that, it may be desirable to preserve
      information about all errors happened during method invocation and deliver
      it to the caller. The <link to="#next"/> attribute is intended
      specifically for this purpose and allows to represent a chain of errors
      through a single IVirtualBoxErrorInfo object set after method invocation.

      errors are stored to a chain in the reverse order, i.e. the
      initial error object you query right after method invocation is the last
      error set by the callee, the object it points to in the @a next attribute
      is the previous error and so on, up to the first error (which is the last
      in the chain).
    """
    __uuid__ = 'c1bcc6d5-7966-481d-ab0b-d0ed73e28135'
    __wsmap__ = 'managed'
    
    @property
    def result_code(self):
        """Get int value for 'resultCode'
        Result code of the error.
        Usually, it will be the same as the result code returned
        by the method that provided this error information, but not
        always. For example, on Win32, CoCreateInstance() will most
        likely return E_NOINTERFACE upon unsuccessful component
        instantiation attempt, but not the value the component factory
        returned. Value is typed 'long', not 'result',
        to make interface usable from scripting languages.
        
          In MS COM, there is no equivalent.
          In XPCOM, it is the same as nsIException::result.
        """
        ret = self._get_attr("resultCode")
        return ret

    @property
    def result_detail(self):
        """Get int value for 'resultDetail'
        Optional result data of this error. This will vary depending on the
        actual error usage. By default this attribute is not being used.
        """
        ret = self._get_attr("resultDetail")
        return ret

    @property
    def interface_id(self):
        """Get str value for 'interfaceID'
        UUID of the interface that defined the error.
        
          In MS COM, it is the same as IErrorInfo::GetGUID, except for the
          data type.
          In XPCOM, there is no equivalent.
        """
        ret = self._get_attr("interfaceID")
        return ret

    @property
    def component(self):
        """Get str value for 'component'
        Name of the component that generated the error.
        
          In MS COM, it is the same as IErrorInfo::GetSource.
          In XPCOM, there is no equivalent.
        """
        ret = self._get_attr("component")
        return ret

    @property
    def text(self):
        """Get str value for 'text'
        Text description of the error.
        
          In MS COM, it is the same as IErrorInfo::GetDescription.
          In XPCOM, it is the same as nsIException::message.
        """
        ret = self._get_attr("text")
        return ret

    @property
    def next_p(self):
        """Get IVirtualBoxErrorInfo value for 'next'
        Next error object if there is any, or @c null otherwise.
        
          In MS COM, there is no equivalent.
          In XPCOM, it is the same as nsIException::inner.
        """
        ret = self._get_attr("next")
        return IVirtualBoxErrorInfo(ret)


class INATNetwork(Interface):
    """
    TBD: the idea, technically we can start any number of the NAT networks,
        but we should expect that at some point we will get collisions because of
        port-forwanding rules. so perhaps we should support only single instance of NAT
        network.
    """
    __uuid__ = '03DFD6F7-1B78-48A3-8345-C785281E9523'
    __wsmap__ = 'managed'
    
    @property
    def network_name(self):
        """Get or set str value for 'networkName'
        TBD: the idea, technically we can start any number of the NAT networks,
        but we should expect that at some point we will get collisions because of
        port-forwanding rules. so perhaps we should support only single instance of NAT
        network.
        """
        ret = self._get_attr("networkName")
        return ret

    @network_name.setter
    def network_name(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("networkName", value)

    @property
    def enabled(self):
        """Get or set bool value for 'enabled'"""
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def network(self):
        """Get or set str value for 'network'
        This is CIDR IPv4 string. Specifiying it user defines IPv4 addresses
        of gateway (low address + 1) and dhcp server (= low address + 2).
        Note: if there're defined IPv4 port-forward rules update of network
        will be ignored (because new assignment could break existing rules).
        """
        ret = self._get_attr("network")
        return ret

    @network.setter
    def network(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("network", value)

    @property
    def gateway(self):
        """Get str value for 'gateway'
        This attribute is read-only. It's recalculated on changing
        network attribute (low address of network + 1).
        """
        ret = self._get_attr("gateway")
        return ret

    @property
    def i_pv6_enabled(self):
        """Get or set bool value for 'IPv6Enabled'
        This attribute define whether gateway will support IPv6 or not.
        """
        ret = self._get_attr("IPv6Enabled")
        return ret

    @i_pv6_enabled.setter
    def i_pv6_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("IPv6Enabled", value)

    @property
    def i_pv6_prefix(self):
        """Get or set str value for 'IPv6Prefix'
        This a CIDR IPv6 defining prefix for link-local addresses
        autoconfiguration within network. Note: ignored if attribute
        IPv6Enabled is false.
        """
        ret = self._get_attr("IPv6Prefix")
        return ret

    @i_pv6_prefix.setter
    def i_pv6_prefix(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("IPv6Prefix", value)

    @property
    def advertise_default_i_pv6_route_enabled(self):
        """Get or set bool value for 'advertiseDefaultIPv6RouteEnabled'"""
        ret = self._get_attr("advertiseDefaultIPv6RouteEnabled")
        return ret

    @advertise_default_i_pv6_route_enabled.setter
    def advertise_default_i_pv6_route_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("advertiseDefaultIPv6RouteEnabled", value)

    @property
    def need_dhcp_server(self):
        """Get or set bool value for 'needDhcpServer'"""
        ret = self._get_attr("needDhcpServer")
        return ret

    @need_dhcp_server.setter
    def need_dhcp_server(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("needDhcpServer", value)

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'"""
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    @property
    def port_forward_rules4(self):
        """Get str value for 'portForwardRules4'
        Array of NAT port-forwarding rules in string representation,
      in the following format:
      "name:protocolid:[host ip]:host port:[guest ip]:guest port".
        """
        ret = self._get_attr("portForwardRules4")
        return ret

    @property
    def port_forward_rules6(self):
        """Get str value for 'portForwardRules6'
        Array of NAT port-forwarding rules in string representation, in the
      following format: "name:protocolid:[host ip]:host port:[guest ip]:guest port".
        """
        ret = self._get_attr("portForwardRules6")
        return ret

    def add_port_forward_rule(self, is_ipv6, rule_name, proto, host_ip, host_port, guest_ip, guest_port):
        """Protocol handled with the rule.

        in is_ipv6 of type bool

        in rule_name of type str

        in proto of type NATProtocol
            Protocol handled with the rule.

        in host_ip of type str
            IP of the host interface to which the rule should apply.
        An empty ip address is acceptable, in which case the NAT engine
        binds the handling socket to any interface.

        in host_port of type int
            The port number to listen on.

        in guest_ip of type str
            The IP address of the guest which the NAT engine will forward
        matching packets to. An empty IP address is not acceptable.

        in guest_port of type int
            The port number to forward.

        """
        if not isinstance(is_ipv6, bool):
            raise TypeError("is_ipv6 can only be an instance of type bool")
        if type(rule_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(proto, NATProtocol):
            raise TypeError("proto can only be an instance of type NATProtocol")
        if type(host_ip) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(host_port, int):
            raise TypeError("host_port can only be an instance of type int")
        if type(guest_ip) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(guest_port, int):
            raise TypeError("guest_port can only be an instance of type int")
        self._call("addPortForwardRule",
                     in_p=[is_ipv6, rule_name, proto, host_ip, host_port, guest_ip, guest_port])

    def remove_port_forward_rule(self, i_sipv6, rule_name):
        """

        in i_sipv6 of type bool

        in rule_name of type str

        """
        if not isinstance(i_sipv6, bool):
            raise TypeError("i_sipv6 can only be an instance of type bool")
        if type(rule_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("removePortForwardRule",
                     in_p=[i_sipv6, rule_name])

    def start(self, trunk_type):
        """Type of internal network trunk.

        in trunk_type of type str
            Type of internal network trunk.

        """
        if type(trunk_type) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("start",
                     in_p=[trunk_type])

    def stop(self):
        """

        """
        self._call("stop")


class IDHCPServer(Interface):
    """
    The IDHCPServer interface represents the vbox DHCP server configuration.

      To enumerate all the DHCP servers on the host, use the
      <link to="IVirtualBox::DHCPServers"/> attribute.
    """
    __uuid__ = 'ff0774c5-1f62-4bc3-919c-7fc942bf1d25'
    __wsmap__ = 'managed'
    
    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'"""
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    @property
    def enabled(self):
        """Get or set bool value for 'enabled'
        specifies if the DHCP server is enabled
        """
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def ip_address(self):
        """Get str value for 'IPAddress'
        specifies server IP
        """
        ret = self._get_attr("IPAddress")
        return ret

    @property
    def network_mask(self):
        """Get str value for 'networkMask'
        specifies server network mask
        """
        ret = self._get_attr("networkMask")
        return ret

    @property
    def network_name(self):
        """Get str value for 'networkName'
        specifies internal network name the server is used for
        """
        ret = self._get_attr("networkName")
        return ret

    @property
    def lower_ip(self):
        """Get str value for 'lowerIP'
        specifies from IP address in server address range
        """
        ret = self._get_attr("lowerIP")
        return ret

    @property
    def upper_ip(self):
        """Get str value for 'upperIP'
        specifies to IP address in server address range
        """
        ret = self._get_attr("upperIP")
        return ret

    def add_global_option(self, option, value):
        """

        in option of type DhcpOpt

        in value of type str

        """
        if not isinstance(option, DhcpOpt):
            raise TypeError("option can only be an instance of type DhcpOpt")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("addGlobalOption",
                     in_p=[option, value])

    @property
    def global_options(self):
        """Get str value for 'globalOptions'"""
        ret = self._get_attr("globalOptions")
        return ret

    @property
    def vm_configs(self):
        """Get str value for 'vmConfigs'"""
        ret = self._get_attr("vmConfigs")
        return ret

    def add_vm_slot_option(self, vmname, slot, option, value):
        """

        in vmname of type str

        in slot of type int

        in option of type DhcpOpt

        in value of type str

        """
        if type(vmname) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(slot, int):
            raise TypeError("slot can only be an instance of type int")
        if not isinstance(option, DhcpOpt):
            raise TypeError("option can only be an instance of type DhcpOpt")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("addVmSlotOption",
                     in_p=[vmname, slot, option, value])

    def remove_vm_slot_options(self, vmname, slot):
        """

        in vmname of type str

        in slot of type int

        """
        if type(vmname) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(slot, int):
            raise TypeError("slot can only be an instance of type int")
        self._call("removeVmSlotOptions",
                     in_p=[vmname, slot])

    def get_vm_slot_options(self, vmname, slot):
        """

        in vmname of type str

        in slot of type int

        return option of type str

        """
        if type(vmname) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(slot, int):
            raise TypeError("slot can only be an instance of type int")
        option = self._call("getVmSlotOptions",
                     in_p=[vmname, slot])
        return option

    def get_mac_options(self, mac):
        """

        in mac of type str

        return option of type str

        """
        if type(mac) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        option = self._call("getMacOptions",
                     in_p=[mac])
        return option

    def set_configuration(self, ip_address, network_mask, from_ip_address, to_ip_address):
        """configures the server

        in ip_address of type str
            server IP address

        in network_mask of type str
            server network mask

        in from_ip_address of type str
            server From IP address for address range

        in to_ip_address of type str
            server To IP address for address range

        raises E_INVALIDARG
            invalid configuration supplied
        
        """
        if type(ip_address) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(network_mask) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(from_ip_address) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(to_ip_address) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setConfiguration",
                     in_p=[ip_address, network_mask, from_ip_address, to_ip_address])

    def start(self, network_name, trunk_name, trunk_type):
        """Starts DHCP server process.

        in network_name of type str
            Name of internal network DHCP server should attach to.

        in trunk_name of type str
            Name of internal network trunk.

        in trunk_type of type str
            Type of internal network trunk.

        raises E_FAIL
            Failed to start the process.
        
        """
        if type(network_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(trunk_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(trunk_type) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("start",
                     in_p=[network_name, trunk_name, trunk_type])

    def stop(self):
        """Stops DHCP server process.

        raises E_FAIL
            Failed to stop the process.
        
        """
        self._call("stop")


class IVirtualBox(Interface):
    """
    The IVirtualBox interface represents the main interface exposed by the
      product that provides virtual machine management.

      An instance of IVirtualBox is required for the product to do anything
      useful. Even though the interface does not expose this, internally,
      IVirtualBox is implemented as a singleton and actually lives in the
      process of the VirtualBox server (VBoxSVC.exe). This makes sure that
      IVirtualBox can track the state of all virtual machines on a particular
      host, regardless of which frontend started them.

      To enumerate all the virtual machines on the host, use the
      <link to="IVirtualBox::machines"/> attribute.
    """
    __uuid__ = 'fafa4e17-1ee2-4905-a10e-fe7c18bf5554'
    __wsmap__ = 'managed'
    
    @property
    def version(self):
        """Get str value for 'version'
        A string representing the version number of the product. The
        format is 3 integer numbers divided by dots (e.g. 1.0.1). The
        last number represents the build number and will frequently change.

        This may be followed by a _ALPHA[0-9]*, _BETA[0-9]* or _RC[0-9]* tag
        in prerelease builds. Non-Oracle builds may (/shall) also have a
        publisher tag, at the end. The publisher tag starts with an underscore
        just like the prerelease build type tag.
        """
        ret = self._get_attr("version")
        return ret

    @property
    def version_normalized(self):
        """Get str value for 'versionNormalized'
        A string representing the version number of the product,
        without the publisher information (but still with other tags).
        See <link to="#version"/>.
        """
        ret = self._get_attr("versionNormalized")
        return ret

    @property
    def revision(self):
        """Get int value for 'revision'
        The internal build revision number of the product.
        """
        ret = self._get_attr("revision")
        return ret

    @property
    def package_type(self):
        """Get str value for 'packageType'
        A string representing the package type of this product. The
        format is OS_ARCH_DIST where OS is either WINDOWS, LINUX,
        SOLARIS, DARWIN. ARCH is either 32BITS or 64BITS. DIST
        is either GENERIC, UBUNTU_606, UBUNTU_710, or something like
        this.
        """
        ret = self._get_attr("packageType")
        return ret

    @property
    def api_version(self):
        """Get str value for 'APIVersion'
        A string representing the VirtualBox API version number. The format is
        2 integer numbers divided by an underscore (e.g. 1_0). After the
        first public release of packages with a particular API version the
        API will not be changed in an incompatible way. Note that this
        guarantee does not apply to development builds, and also there is no
        guarantee that this version is identical to the first two integer
        numbers of the package version.
        """
        ret = self._get_attr("APIVersion")
        return ret

    @property
    def home_folder(self):
        """Get str value for 'homeFolder'
        Full path to the directory where the global settings file,
        VirtualBox.xml, is stored.

        In this version of VirtualBox, the value of this property is
        always <user_dir>/.VirtualBox (where
        <user_dir> is the path to the user directory,
        as determined by the host OS), and cannot be changed.

        This path is also used as the base to resolve relative paths in
        places where relative paths are allowed (unless otherwise
        expressly indicated).
        """
        ret = self._get_attr("homeFolder")
        return ret

    @property
    def settings_file_path(self):
        """Get str value for 'settingsFilePath'
        Full name of the global settings file.
        The value of this property corresponds to the value of
        <link to="#homeFolder"/> plus /VirtualBox.xml.
        """
        ret = self._get_attr("settingsFilePath")
        return ret

    @property
    def host(self):
        """Get IHost value for 'host'
        Associated host object.
        """
        ret = self._get_attr("host")
        return IHost(ret)

    @property
    def system_properties(self):
        """Get ISystemProperties value for 'systemProperties'
        Associated system information object.
        """
        ret = self._get_attr("systemProperties")
        return ISystemProperties(ret)

    @property
    def machines(self):
        """Get IMachine value for 'machines'
        Array of machine objects registered within this VirtualBox instance.
        """
        ret = self._get_attr("machines")
        return [IMachine(a) for a in ret]

    @property
    def machine_groups(self):
        """Get str value for 'machineGroups'
        Array of all machine group names which are used by the machines which
        are accessible. Each group is only listed once, however they are listed
        in no particular order and there is no guarantee that there are no gaps
        in the group hierarchy (i.e. "/", "/group/subgroup"
        is a valid result).
        """
        ret = self._get_attr("machineGroups")
        return ret

    @property
    def hard_disks(self):
        """Get IMedium value for 'hardDisks'
        Array of medium objects known to this VirtualBox installation.

        This array contains only base media. All differencing
        media of the given base medium can be enumerated using
        <link to="IMedium::children"/>.
        """
        ret = self._get_attr("hardDisks")
        return [IMedium(a) for a in ret]

    @property
    def dvd_images(self):
        """Get IMedium value for 'DVDImages'
        Array of CD/DVD image objects currently in use by this VirtualBox instance.
        """
        ret = self._get_attr("DVDImages")
        return [IMedium(a) for a in ret]

    @property
    def floppy_images(self):
        """Get IMedium value for 'floppyImages'
        Array of floppy image objects currently in use by this VirtualBox instance.
        """
        ret = self._get_attr("floppyImages")
        return [IMedium(a) for a in ret]

    @property
    def progress_operations(self):
        """Get IProgress value for 'progressOperations'"""
        ret = self._get_attr("progressOperations")
        return [IProgress(a) for a in ret]

    @property
    def guest_os_types(self):
        """Get IGuestOSType value for 'guestOSTypes'"""
        ret = self._get_attr("guestOSTypes")
        return [IGuestOSType(a) for a in ret]

    @property
    def shared_folders(self):
        """Get ISharedFolder value for 'sharedFolders'
        Collection of global shared folders. Global shared folders are
        available to all virtual machines.

        New shared folders are added to the collection using
        <link to="#createSharedFolder"/>. Existing shared folders can be
        removed using <link to="#removeSharedFolder"/>.

        
          In the current version of the product, global shared folders are not
          implemented and therefore this collection is always empty.
        """
        ret = self._get_attr("sharedFolders")
        return [ISharedFolder(a) for a in ret]

    @property
    def performance_collector(self):
        """Get IPerformanceCollector value for 'performanceCollector'
        Associated performance collector object.
        """
        ret = self._get_attr("performanceCollector")
        return IPerformanceCollector(ret)

    @property
    def dhcp_servers(self):
        """Get IDHCPServer value for 'DHCPServers'
        DHCP servers.
        """
        ret = self._get_attr("DHCPServers")
        return [IDHCPServer(a) for a in ret]

    @property
    def nat_networks(self):
        """Get INATNetwork value for 'NATNetworks'"""
        ret = self._get_attr("NATNetworks")
        return [INATNetwork(a) for a in ret]

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for VirtualBox events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    @property
    def extension_pack_manager(self):
        """Get IExtPackManager value for 'extensionPackManager'
        The extension pack manager.
        """
        ret = self._get_attr("extensionPackManager")
        return IExtPackManager(ret)

    @property
    def internal_networks(self):
        """Get str value for 'internalNetworks'
        Names of all internal networks.
        """
        ret = self._get_attr("internalNetworks")
        return ret

    @property
    def generic_network_drivers(self):
        """Get str value for 'genericNetworkDrivers'
        Names of all generic network drivers.
        """
        ret = self._get_attr("genericNetworkDrivers")
        return ret

    def compose_machine_filename(self, name, group, create_flags, base_folder):
        """Returns a recommended full path of the settings file name for a new virtual
        machine.

        This API serves two purposes:

        
          It gets called by <link to="#createMachine"/> if @c null or
            empty string (which is recommended) is specified for the
            @a settingsFile argument there, which means that API should use
            a recommended default file name.

          It can be called manually by a client software before creating a machine,
            e.g. if that client wants to pre-create the machine directory to create
            virtual hard disks in that directory together with the new machine
            settings file. In that case, the file name should be stripped from the
            full settings file path returned by this function to obtain the
            machine directory.
        

        See <link to="IMachine::name"/> and <link to="#createMachine"/> for more
        details about the machine name.

        @a groupName defines which additional subdirectory levels should be
        included. It must be either a valid group name or @c null or empty
        string which designates that the machine will not be related to a
        machine group.

        If @a baseFolder is a @c null or empty string (which is recommended), the
        default machine settings folder
        (see <link to="ISystemProperties::defaultMachineFolder"/>) will be used as
        a base folder for the created machine, resulting in a file name like
        "/home/user/VirtualBox VMs/name/name.vbox". Otherwise the given base folder
        will be used.

        This method does not access the host disks. In particular, it does not check
        for whether a machine with this name already exists.

        in name of type str
            Suggested machine name.

        in group of type str
            Machine group name for the new machine or machine group. It is
        used to determine the right subdirectory.

        in create_flags of type str
            Machine creation flags, see <link to="#createMachine"/> (optional).

        in base_folder of type str
            Base machine folder (optional).

        return file_p of type str
            Fully qualified path where the machine would be created.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(group) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(create_flags) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(base_folder) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        file_p = self._call("composeMachineFilename",
                     in_p=[name, group, create_flags, base_folder])
        return file_p

    def create_machine(self, settings_file, name, groups, os_type_id, flags):
        """Creates a new virtual machine by creating a machine settings file at
        the given location.

        VirtualBox machine settings files use a custom XML dialect. Starting
        with VirtualBox 4.0, a ".vbox" extension is recommended, but not enforced,
        and machine files can be created at arbitrary locations.

        However, it is recommended that machines are created in the default
        machine folder (e.g. "/home/user/VirtualBox VMs/name/name.vbox"; see
        <link to="ISystemProperties::defaultMachineFolder"/>). If you specify
        @c null or empty string (which is recommended) for the @a settingsFile
        argument, <link to="#composeMachineFilename"/> is called automatically
        to have such a recommended name composed based on the machine name
        given in the @a name argument and the primary group.

        If the resulting settings file already exists, this method will fail,
        unless the forceOverwrite flag is set.

        The new machine is created unregistered, with the initial configuration
        set according to the specified guest OS type. A typical sequence of
        actions to create a new virtual machine is as follows:

        
          
            Call this method to have a new machine created. The returned machine
            object will be "mutable" allowing to change any machine property.
          

          
            Configure the machine using the appropriate attributes and methods.
          

          
            Call <link to="IMachine::saveSettings"/> to write the settings
            to the machine's XML settings file. The configuration of the newly
            created machine will not be saved to disk until this method is
            called.
          

          
            Call <link to="#registerMachine"/> to add the machine to the list
            of machines known to VirtualBox.
          
        

        The specified guest OS type identifier must match an ID of one of known
        guest OS types listed in the <link to="IVirtualBox::guestOSTypes"/>
        array.

        
          There is no way to change the name of the settings file or
          subfolder of the created machine directly.

        in settings_file of type str
            Fully qualified path where the settings file should be created,
          empty string or @c null for a default folder and file based on the
          @a name argument and the primary group.
        (see <link to="#composeMachineFilename"/>).

        in name of type str
            Machine name.

        in groups of type str
            Array of group names. @c null or an empty array have the same
          meaning as an array with just the empty string or "/", i.e.
          create a machine without group association.

        in os_type_id of type str
            Guest OS Type ID.

        in flags of type str
            Additional property parameters, passed as a comma-separated list of
          "name=value" type entries. The following ones are recognized:
          forceOverwrite=1 to overwrite an existing machine settings
          file, UUID=<uuid> to specify a machine UUID and
          directoryIncludesUUID=1 to switch to a special VM directory
          naming scheme which should not be used unless necessary.

        return machine of type IMachine
            Created machine object.

        raises VBOX_E_OBJECT_NOT_FOUND
            @a osTypeId is invalid.
        
        raises VBOX_E_FILE_ERROR
            Resulting settings file name is invalid or the settings file already
          exists or could not be created due to an I/O error.
        
        raises E_INVALIDARG
            @a name is empty or @c null.
        
        """
        if type(settings_file) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(groups, list):
            raise TypeError("groups can only be an instance of type list")
        for a in groups[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if type(os_type_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(flags) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        machine = self._call("createMachine",
                     in_p=[settings_file, name, groups, os_type_id, flags])
        machine = IMachine(machine)
        return machine

    def open_machine(self, settings_file):
        """Opens a virtual machine from the existing settings file.
        The opened machine remains unregistered until you call
        <link to="#registerMachine"/>.

        The specified settings file name must be fully qualified.
        The file must exist and be a valid machine XML settings file
        whose contents will be used to construct the machine object.

        in settings_file of type str
            Name of the machine settings file.

        return machine of type IMachine
            Opened machine object.

        raises VBOX_E_FILE_ERROR
            Settings file name invalid, not found or sharing violation.
        
        """
        if type(settings_file) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        machine = self._call("openMachine",
                     in_p=[settings_file])
        machine = IMachine(machine)
        return machine

    def register_machine(self, machine):
        """Registers the machine previously created using
        <link to="#createMachine"/> or opened using
        <link to="#openMachine"/> within this VirtualBox installation. After
        successful method invocation, the
        <link to="IMachineRegisteredEvent"/> event is fired.

        
          This method implicitly calls <link to="IMachine::saveSettings"/>
          to save all current machine settings before registering it.

        in machine of type IMachine

        raises VBOX_E_OBJECT_NOT_FOUND
            No matching virtual machine found.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Virtual machine was not created within this VirtualBox instance.
        
        """
        if not isinstance(machine, IMachine):
            raise TypeError("machine can only be an instance of type IMachine")
        self._call("registerMachine",
                     in_p=[machine])

    def find_machine(self, name_or_id):
        """Attempts to find a virtual machine given its name or UUID.

        Inaccessible machines cannot be found by name, only by UUID, because their name
          cannot safely be determined.

        in name_or_id of type str
            What to search for. This can either be the UUID or the name of a virtual machine.

        return machine of type IMachine
            Machine object, if found.

        raises VBOX_E_OBJECT_NOT_FOUND
            Could not find registered machine matching @a nameOrId.
        
        """
        if type(name_or_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        machine = self._call("findMachine",
                     in_p=[name_or_id])
        machine = IMachine(machine)
        return machine

    def get_machines_by_groups(self, groups):
        """Gets all machine references which are in one of the specified groups.

        in groups of type str
            What groups to match. The usual group list rules apply, i.e.
        passing an empty list will match VMs in the toplevel group, likewise
        the empty string.

        return machines of type IMachine
            All machines which matched.

        """
        if not isinstance(groups, list):
            raise TypeError("groups can only be an instance of type list")
        for a in groups[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        machines = self._call("getMachinesByGroups",
                     in_p=[groups])
        machines = [IMachine(a) for a in machines]
        return machines

    def get_machine_states(self, machines):
        """Gets the state of several machines in a single operation.

        in machines of type IMachine
            Array with the machine references.

        return states of type MachineState
            Machine states, corresponding to the machines.

        """
        if not isinstance(machines, list):
            raise TypeError("machines can only be an instance of type list")
        for a in machines[:10]:
            if not isinstance(a, IMachine):
                raise TypeError(\
                        "array can only contain objects of type IMachine")
        states = self._call("getMachineStates",
                     in_p=[machines])
        states = [MachineState(a) for a in states]
        return states

    def create_appliance(self):
        """Creates a new appliance object, which represents an appliance in the Open Virtual Machine
        Format (OVF). This can then be used to import an OVF appliance into VirtualBox or to export
        machines as an OVF appliance; see the documentation for <link to="IAppliance"/> for details.

        return appliance of type IAppliance
            New appliance.

        """
        appliance = self._call("createAppliance")
        appliance = IAppliance(appliance)
        return appliance

    def create_hard_disk(self, format_p, location):
        """Creates a new base medium object that will use the given storage
        format and location for medium data.

        The actual storage unit is not created by this method. In order to
        do it, and before you are able to attach the created medium to
        virtual machines, you must call one of the following methods to
        allocate a format-specific storage unit at the specified location:
        
          <link to="IMedium::createBaseStorage"/>
          <link to="IMedium::createDiffStorage"/>
        

        Some medium attributes, such as <link to="IMedium::id"/>, may
        remain uninitialized until the medium storage unit is successfully
        created by one of the above methods.

        After the storage unit is successfully created, it will be
        accessible through the <link to="#openMedium"/> method and can
        be found in the <link to="#hardDisks"/> array.

        The list of all storage formats supported by this VirtualBox
        installation can be obtained using
        <link to="ISystemProperties::mediumFormats"/>. If the @a format
        attribute is empty or @c null then the default storage format
        specified by <link to="ISystemProperties::defaultHardDiskFormat"/> will
        be used for creating a storage unit of the medium.

        Note that the format of the location string is storage format specific.
        See <link to="IMedium::location"/> and IMedium for more details.

        in format_p of type str
            Identifier of the storage format to use for the new medium.

        in location of type str
            Location of the storage unit for the new medium.

        return medium of type IMedium
            Created medium object.

        raises VBOX_E_OBJECT_NOT_FOUND
            @a format identifier is invalid. See
        
        raises VBOX_E_FILE_ERROR
            @a location is a not valid file name (for file-based formats only).
        
        """
        if type(format_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(location) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        medium = self._call("createHardDisk",
                     in_p=[format_p, location])
        medium = IMedium(medium)
        return medium

    def open_medium(self, location, device_type, access_mode, force_new_uuid):
        """Finds existing media or opens a medium from an existing storage location.

        Once a medium has been opened, it can be passed to other VirtualBox
        methods, in particular to <link to="IMachine::attachDevice"/>.

        Depending on the given device type, the file at the storage location
        must be in one of the media formats understood by VirtualBox:

        
          With a "HardDisk" device type, the file must be a hard disk image
            in one of the formats supported by VirtualBox (see
            <link to="ISystemProperties::mediumFormats"/>).
            After this method succeeds, if the medium is a base medium, it
            will be added to the <link to="#hardDisks"/> array attribute. 
          With a "DVD" device type, the file must be an ISO 9960 CD/DVD image.
            After this method succeeds, the medium will be added to the
            <link to="#DVDImages"/> array attribute.
          With a "Floppy" device type, the file must be an RAW floppy image.
            After this method succeeds, the medium will be added to the
            <link to="#floppyImages"/> array attribute.
        

        After having been opened, the medium can be re-found by this method
        and can be attached to virtual machines. See <link to="IMedium"/> for
        more details.

        The UUID of the newly opened medium will either be retrieved from the
        storage location, if the format supports it (e.g. for hard disk images),
        or a new UUID will be randomly generated (e.g. for ISO and RAW files).
        If for some reason you need to change the medium's UUID, use
        <link to="IMedium::setIds"/>.

        If a differencing hard disk medium is to be opened by this method, the
        operation will succeed only if its parent medium and all ancestors,
        if any, are already known to this VirtualBox installation (for example,
        were opened by this method before).

        This method attempts to guess the storage format of the specified medium
        by reading medium data at the specified location.

        If @a accessMode is ReadWrite (which it should be for hard disks and floppies),
        the image is opened for read/write access and must have according permissions,
        as VirtualBox may actually write status information into the disk's metadata
        sections.

        Note that write access is required for all typical hard disk usage in VirtualBox,
        since VirtualBox may need to write metadata such as a UUID into the image.
        The only exception is opening a source image temporarily for copying and
        cloning (see <link to="IMedium::cloneTo"/> when the image will be closed
        again soon.

        The format of the location string is storage format specific. See
        <link to="IMedium::location"/> and IMedium for more details.

        in location of type str
            Location of the storage unit that contains medium data in one of
          the supported storage formats.

        in device_type of type DeviceType
            Must be one of "HardDisk", "DVD" or "Floppy".

        in access_mode of type AccessMode
            Whether to open the image in read/write or read-only mode. For
        a "DVD" device type, this is ignored and read-only mode is always assumed.

        in force_new_uuid of type bool
            Allows the caller to request a completely new medium UUID for
           the image which is to be opened. Useful if one intends to open an exact
           copy of a previously opened image, as this would normally fail due to
           the duplicate UUID.

        return medium of type IMedium
            Opened medium object.

        raises VBOX_E_FILE_ERROR
            Invalid medium storage file location or could not find the medium
          at the specified location.
        
        raises VBOX_E_IPRT_ERROR
            Could not get medium storage format.
        
        raises E_INVALIDARG
            Invalid medium storage format.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Medium has already been added to a media registry.
        
        """
        if type(location) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(device_type, DeviceType):
            raise TypeError("device_type can only be an instance of type DeviceType")
        if not isinstance(access_mode, AccessMode):
            raise TypeError("access_mode can only be an instance of type AccessMode")
        if not isinstance(force_new_uuid, bool):
            raise TypeError("force_new_uuid can only be an instance of type bool")
        medium = self._call("openMedium",
                     in_p=[location, device_type, access_mode, force_new_uuid])
        medium = IMedium(medium)
        return medium

    def get_guest_os_type(self, id_p):
        """Returns an object describing the specified guest OS type.

        The requested guest OS type is specified using a string which is a
        mnemonic identifier of the guest operating system, such as
        "win31" or "ubuntu". The guest OS type ID of a
        particular virtual machine can be read or set using the
        <link to="IMachine::OSTypeId"/> attribute.

        The <link to="IVirtualBox::guestOSTypes"/> collection contains all
        available guest OS type objects. Each object has an
        <link to="IGuestOSType::id"/> attribute which contains an identifier of
        the guest OS this object describes.

        in id_p of type str
            Guest OS type ID string.

        return type_p of type IGuestOSType
            Guest OS type object.

        raises E_INVALIDARG
            @a id is not a valid Guest OS type.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        type_p = self._call("getGuestOSType",
                     in_p=[id_p])
        type_p = IGuestOSType(type_p)
        return type_p

    def create_shared_folder(self, name, host_path, writable, automount):
        """Creates a new global shared folder by associating the given logical
        name with the given host path, adds it to the collection of shared
        folders and starts sharing it. Refer to the description of
        <link to="ISharedFolder"/> to read more about logical names.
        
          In the current implementation, this operation is not
          implemented.

        in name of type str
            Unique logical name of the shared folder.

        in host_path of type str
            Full path to the shared folder in the host file system.

        in writable of type bool
            Whether the share is writable or readonly

        in automount of type bool
            Whether the share gets automatically mounted by the guest
          or not.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(host_path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(writable, bool):
            raise TypeError("writable can only be an instance of type bool")
        if not isinstance(automount, bool):
            raise TypeError("automount can only be an instance of type bool")
        self._call("createSharedFolder",
                     in_p=[name, host_path, writable, automount])

    def remove_shared_folder(self, name):
        """Removes the global shared folder with the given name previously
        created by <link to="#createSharedFolder"/> from the collection of
        shared folders and stops sharing it.
        
          In the current implementation, this operation is not
          implemented.

        in name of type str
            Logical name of the shared folder to remove.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("removeSharedFolder",
                     in_p=[name])

    def get_extra_data_keys(self):
        """Returns an array representing the global extra data keys which currently
        have values defined.

        return keys of type str
            Array of extra data keys.

        """
        keys = self._call("getExtraDataKeys")
        return keys

    def get_extra_data(self, key):
        """Returns associated global extra data.

        If the requested data @a key does not exist, this function will
        succeed and return an empty string in the @a value argument.

        in key of type str
            Name of the data key to get.

        return value of type str
            Value of the requested data key.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getExtraData",
                     in_p=[key])
        return value

    def set_extra_data(self, key, value):
        """Sets associated global extra data.

        If you pass @c null or empty string as a key @a value, the given @a key
        will be deleted.

        
          Before performing the actual data change, this method will ask all
          registered event listener using the
          <link to="IExtraDataCanChangeEvent"/>
          notification for a permission. If one of the listeners refuses the
          new value, the change will not be performed.
        
        
          On success, the
          <link to="IExtraDataChangedEvent"/> notification
          is called to inform all registered listeners about a successful data
          change.

        in key of type str
            Name of the data key to set.

        in value of type str
            Value to assign to the key.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        raises E_ACCESSDENIED
            Modification request refused.
        
        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setExtraData",
                     in_p=[key, value])

    def set_settings_secret(self, password):
        """Unlocks the secret data by passing the unlock password to the
        server. The server will cache the password for that machine.

        in password of type str
            The cipher key.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is not mutable.
        
        """
        if type(password) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setSettingsSecret",
                     in_p=[password])

    def create_dhcp_server(self, name):
        """Creates a DHCP server settings to be used for the given internal network name

        in name of type str
            server name

        return server of type IDHCPServer
            DHCP server settings

        raises E_INVALIDARG
            Host network interface @a name already exists.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        server = self._call("createDHCPServer",
                     in_p=[name])
        server = IDHCPServer(server)
        return server

    def find_dhcp_server_by_network_name(self, name):
        """Searches a DHCP server settings to be used for the given internal network name

        in name of type str
            server name

        return server of type IDHCPServer
            DHCP server settings

        raises E_INVALIDARG
            Host network interface @a name already exists.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        server = self._call("findDHCPServerByNetworkName",
                     in_p=[name])
        server = IDHCPServer(server)
        return server

    def remove_dhcp_server(self, server):
        """Removes the DHCP server settings

        in server of type IDHCPServer
            DHCP server settings to be removed

        raises E_INVALIDARG
            Host network interface @a name already exists.
        
        """
        if not isinstance(server, IDHCPServer):
            raise TypeError("server can only be an instance of type IDHCPServer")
        self._call("removeDHCPServer",
                     in_p=[server])

    def create_nat_network(self, network_name):
        """

        in network_name of type str

        return network of type INATNetwork

        """
        if type(network_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        network = self._call("createNATNetwork",
                     in_p=[network_name])
        network = INATNetwork(network)
        return network

    def find_nat_network_by_name(self, network_name):
        """

        in network_name of type str

        return network of type INATNetwork

        """
        if type(network_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        network = self._call("findNATNetworkByName",
                     in_p=[network_name])
        network = INATNetwork(network)
        return network

    def remove_nat_network(self, network):
        """

        in network of type INATNetwork

        """
        if not isinstance(network, INATNetwork):
            raise TypeError("network can only be an instance of type INATNetwork")
        self._call("removeNATNetwork",
                     in_p=[network])

    def check_firmware_present(self, firmware_type, version):
        """Check if this VirtualBox installation has a firmware
        of the given type available, either system-wide or per-user.
        Optionally, this may return a hint where this firmware can be
        downloaded from.

        in firmware_type of type FirmwareType
            Type of firmware to check.

        in version of type str
            Expected version number, usually empty string (presently ignored).

        out url of type str
            Suggested URL to download this firmware from.

        out file_p of type str
            Filename of firmware, only valid if result == TRUE.

        return result of type bool
            If firmware of this type and version is available.

        """
        if not isinstance(firmware_type, FirmwareType):
            raise TypeError("firmware_type can only be an instance of type FirmwareType")
        if type(version) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        (url, file_p, result) = self._call("checkFirmwarePresent",
                     in_p=[firmware_type, version])
        return (url, file_p, result)


class IVFSExplorer(Interface):
    """
    The VFSExplorer interface unifies access to different file system
      types. This includes local file systems as well remote file systems like
      S3. For a list of supported types see <link to="VFSType"/>.
      An instance of this is returned by <link to="IAppliance::createVFSExplorer"/>.
    """
    __uuid__ = '003d7f92-d38e-487f-b790-8c5e8631cb2f'
    __wsmap__ = 'managed'
    
    @property
    def path(self):
        """Get str value for 'path'
        Returns the current path in the virtual file system.
        """
        ret = self._get_attr("path")
        return ret

    @property
    def type_p(self):
        """Get VFSType value for 'type'
        Returns the file system type which is currently in use.
        """
        ret = self._get_attr("type")
        return VFSType(ret)

    def update(self):
        """Updates the internal list of files/directories from the
      current directory level. Use <link to="#entryList"/> to get the full list
      after a call to this method.

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        progress = self._call("update")
        progress = IProgress(progress)
        return progress

    def cd(self, dir_p):
        """Change the current directory level.

        in dir_p of type str
            The name of the directory to go in.

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        if type(dir_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("cd",
                     in_p=[dir_p])
        progress = IProgress(progress)
        return progress

    def cd_up(self):
        """Go one directory upwards from the current directory level.

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        progress = self._call("cdUp")
        progress = IProgress(progress)
        return progress

    def entry_list(self):
        """Returns a list of files/directories after a call to <link to="#update"/>. The user is responsible for keeping this internal
      list up do date.

        out names of type str
            The list of names for the entries.

        out types of type int
            The list of types for the entries.

        out sizes of type int
            The list of sizes (in bytes) for the entries.

        out modes of type int
            The list of file modes (in octal form) for the entries.

        """
        (names, types, sizes, modes) = self._call("entryList")
        return (names, types, sizes, modes)

    def exists(self, names):
        """Checks if the given file list exists in the current directory
      level.

        in names of type str
            The names to check.

        return exists of type str
            The names which exist.

        """
        if not isinstance(names, list):
            raise TypeError("names can only be an instance of type list")
        for a in names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        exists = self._call("exists",
                     in_p=[names])
        return exists

    def remove(self, names):
        """Deletes the given files in the current directory level.

        in names of type str
            The names to remove.

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        if not isinstance(names, list):
            raise TypeError("names can only be an instance of type list")
        for a in names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        progress = self._call("remove",
                     in_p=[names])
        progress = IProgress(progress)
        return progress


class IAppliance(Interface):
    """
    Represents a platform-independent appliance in OVF format. An instance of this is returned
        by <link to="IVirtualBox::createAppliance"/>, which can then be used to import and export
        virtual machines within an appliance with VirtualBox.

        The OVF standard suggests two different physical file formats:

        
            If the appliance is distributed as a set of files, there must be at least one XML descriptor
                file that conforms to the OVF standard and carries an .ovf file extension. If
                this descriptor file references other files such as disk images, as OVF appliances typically
                do, those additional files must be in the same directory as the descriptor file.

              If the appliance is distributed as a single file, it must be in TAR format and have the
                .ova file extension. This TAR file must then contain at least the OVF descriptor
                files and optionally other files.

                At this time, VirtualBox does not not yet support the packed (TAR) variant; support will
                be added with a later version.
        

        Importing an OVF appliance into VirtualBox as instances of
        <link to="IMachine"/> involves the following sequence of API calls:

        
          Call <link to="IVirtualBox::createAppliance"/>. This will create an empty IAppliance object.
          

          On the new object, call <link to="#read"/> with the full path of the OVF file you
              would like to import. So long as this file is syntactically valid, this will succeed
              and fill the appliance object with the parsed data from the OVF file.
          

          Next, call <link to="#interpret"/>, which analyzes the OVF data and sets up the
              contents of the IAppliance attributes accordingly. These can be inspected by a
              VirtualBox front-end such as the GUI, and the suggestions can be displayed to the
              user. In particular, the <link to="#virtualSystemDescriptions"/> array contains
              instances of <link to="IVirtualSystemDescription"/> which represent the virtual
              systems (machines) in the OVF, which in turn describe the virtual hardware prescribed
              by the OVF (network and hardware adapters, virtual disk images, memory size and so on).
              The GUI can then give the user the option to confirm and/or change these suggestions.
          

          If desired, call <link to="IVirtualSystemDescription::setFinalValues"/> for each
              virtual system (machine) to override the suggestions made by the <link to="#interpret"/> routine.
          

          Finally, call <link to="#importMachines"/> to create virtual machines in
              VirtualBox as instances of <link to="IMachine"/> that match the information in the
              virtual system descriptions. After this call succeeded, the UUIDs of the machines created
              can be found in the <link to="#machines"/> array attribute.
          
        

        Exporting VirtualBox machines into an OVF appliance involves the following steps:

        
            As with importing, first call <link to="IVirtualBox::createAppliance"/> to create
                an empty IAppliance object.
            

            For each machine you would like to export, call <link to="IMachine::exportTo"/>
                with the IAppliance object you just created. Each such call creates one instance of
                <link to="IVirtualSystemDescription"/> inside the appliance.
            

            If desired, call <link to="IVirtualSystemDescription::setFinalValues"/> for each
                virtual system (machine) to override the suggestions made by the <link to="IMachine::exportTo"/> routine.
            

            Finally, call <link to="#write"/> with a path specification to have the OVF
                file written.
    """
    __uuid__ = '3059cf9e-25c7-4f0b-9fa5-3c42e441670b'
    __wsmap__ = 'managed'
    
    @property
    def path(self):
        """Get str value for 'path'
        Path to the main file of the OVF appliance, which is either the .ovf or
          the .ova file passed to <link to="#read"/> (for import) or
          <link to="#write"/> (for export).
          This attribute is empty until one of these methods has been called.
        """
        ret = self._get_attr("path")
        return ret

    @property
    def disks(self):
        """Get str value for 'disks'
        Array of virtual disk definitions. One such description exists for each
        disk definition in the OVF; each string array item represents one such piece of
        disk information, with the information fields separated by tab (\\t) characters.

        The caller should be prepared for additional fields being appended to
        this string in future versions of VirtualBox and therefore check for
        the number of tabs in the strings returned.

        In the current version, the following eight fields are returned per string
        in the array:

        
            Disk ID (unique string identifier given to disk)

            Capacity (unsigned integer indicating the maximum capacity of the disk)

            Populated size (optional unsigned integer indicating the current size of the
            disk; can be approximate; -1 if unspecified)

            Format (string identifying the disk format, typically
            "http://www.vmware.com/specifications/vmdk.html#sparse")

            Reference (where to find the disk image, typically a file name; if empty,
            then the disk should be created on import)

            Image size (optional unsigned integer indicating the size of the image,
            which need not necessarily be the same as the values specified above, since
            the image may be compressed or sparse; -1 if not specified)

            Chunk size (optional unsigned integer if the image is split into chunks;
            presently unsupported and always -1)

            Compression (optional string equalling "gzip" if the image is gzip-compressed)
        """
        ret = self._get_attr("disks")
        return ret

    @property
    def virtual_system_descriptions(self):
        """Get IVirtualSystemDescription value for 'virtualSystemDescriptions'
        Array of virtual system descriptions. One such description is created
      for each virtual system (machine) found in the OVF.
      This array is empty until either <link to="#interpret"/> (for import) or <link to="IMachine::exportTo"/>
      (for export) has been called.
        """
        ret = self._get_attr("virtualSystemDescriptions")
        return [IVirtualSystemDescription(a) for a in ret]

    @property
    def machines(self):
        """Get str value for 'machines'
        Contains the UUIDs of the machines created from the information in this appliances. This is only
        relevant for the import case, and will only contain data after a call to <link to="#importMachines"/>
        succeeded.
        """
        ret = self._get_attr("machines")
        return ret

    def read(self, file_p):
        """Reads an OVF file into the appliance object.

        This method succeeds if the OVF is syntactically valid and, by itself, without errors. The
        mere fact that this method returns successfully does not mean that VirtualBox supports all
        features requested by the appliance; this can only be examined after a call to <link to="#interpret"/>.

        in file_p of type str
            Name of appliance file to open (either with an .ovf or .ova extension, depending
          on whether the appliance is distributed as a set of files or as a single file, respectively).

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        if type(file_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("read",
                     in_p=[file_p])
        progress = IProgress(progress)
        return progress

    def interpret(self):
        """Interprets the OVF data that was read when the appliance was constructed. After
        calling this method, one can inspect the
        <link to="#virtualSystemDescriptions"/> array attribute, which will then contain
        one <link to="IVirtualSystemDescription"/> for each virtual machine found in
        the appliance.

        Calling this method is the second step of importing an appliance into VirtualBox;
        see <link to="IAppliance"/> for an overview.

        After calling this method, one should call <link to="#getWarnings"/> to find out
        if problems were encountered during the processing which might later lead to
        errors.

        """
        self._call("interpret")

    def import_machines(self, options):
        """Imports the appliance into VirtualBox by creating instances of <link to="IMachine"/>
        and other interfaces that match the information contained in the appliance as
        closely as possible, as represented by the import instructions in the
        <link to="#virtualSystemDescriptions"/> array.

        Calling this method is the final step of importing an appliance into VirtualBox;
        see <link to="IAppliance"/> for an overview.

        Since importing the appliance will most probably involve copying and converting
        disk images, which can take a long time, this method operates asynchronously and
        returns an IProgress object to allow the caller to monitor the progress.

        After the import succeeded, the UUIDs of the IMachine instances created can be
        retrieved from the <link to="#machines"/> array attribute.

        in options of type ImportOptions
            Options for the importing operation.

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        if not isinstance(options, list):
            raise TypeError("options can only be an instance of type list")
        for a in options[:10]:
            if not isinstance(a, ImportOptions):
                raise TypeError(\
                        "array can only contain objects of type ImportOptions")
        progress = self._call("importMachines",
                     in_p=[options])
        progress = IProgress(progress)
        return progress

    def create_vfs_explorer(self, uri):
        """Returns a <link to="IVFSExplorer"/> object for the given URI.

        in uri of type str
            The URI describing the file system to use.

        return explorer of type IVFSExplorer
            <desc/>

        """
        if type(uri) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        explorer = self._call("createVFSExplorer",
                     in_p=[uri])
        explorer = IVFSExplorer(explorer)
        return explorer

    def write(self, format_p, manifest, path):
        """Writes the contents of the appliance exports into a new OVF file.

          Calling this method is the final step of exporting an appliance from VirtualBox;
          see <link to="IAppliance"/> for an overview.

          Since exporting the appliance will most probably involve copying and converting
          disk images, which can take a long time, this method operates asynchronously and
          returns an IProgress object to allow the caller to monitor the progress.

        in format_p of type str
            Output format, as a string. Currently supported formats are "ovf-0.9", "ovf-1.0"
            and "ovf-2.0"; future versions of VirtualBox may support additional formats.

        in manifest of type bool
            Indicate if the optional manifest file (.mf) should be written. The manifest file
            is used for integrity checks prior import.

        in path of type str
            Name of appliance file to open (either with an .ovf or .ova extension, depending
              on whether the appliance is distributed as a set of files or as a single file, respectively).

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        if type(format_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(manifest, bool):
            raise TypeError("manifest can only be an instance of type bool")
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("write",
                     in_p=[format_p, manifest, path])
        progress = IProgress(progress)
        return progress

    def get_warnings(self):
        """Returns textual warnings which occurred during execution of <link to="#interpret"/>.

        return warnings of type str
            <desc/>

        """
        warnings = self._call("getWarnings")
        return warnings


class IVirtualSystemDescription(Interface):
    """
    Represents one virtual system (machine) in an appliance. This interface is used in
      the <link to="IAppliance::virtualSystemDescriptions"/> array. After
      <link to="IAppliance::interpret"/> has been called, that array contains information
      about how the virtual systems described in the OVF should best be imported into
      VirtualBox virtual machines. See <link to="IAppliance"/> for the steps required to
      import an OVF into VirtualBox.
    """
    __uuid__ = 'd7525e6c-531a-4c51-8e04-41235083a3d8'
    __wsmap__ = 'managed'
    
    @property
    def count(self):
        """Get int value for 'count'
        Return the number of virtual system description entries.
        """
        ret = self._get_attr("count")
        return ret

    def get_description(self):
        """Returns information about the virtual system as arrays of instruction items. In each array, the
      items with the same indices correspond and jointly represent an import instruction for VirtualBox.

      The list below identifies the value sets that are possible depending on the
      <link to="VirtualSystemDescriptionType"/> enum value in the array item in @a aTypes[]. In each case,
      the array item with the same index in @a OVFValues[] will contain the original value as contained
      in the OVF file (just for informational purposes), and the corresponding item in @a aVBoxValues[]
      will contain a suggested value to be used for VirtualBox. Depending on the description type,
      the @a aExtraConfigValues[] array item may also be used.

      
      
        "OS": the guest operating system type. There must be exactly one such array item on import. The
        corresponding item in @a aVBoxValues[] contains the suggested guest operating system for VirtualBox.
        This will be one of the values listed in <link to="IVirtualBox::guestOSTypes"/>. The corresponding
        item in @a OVFValues[] will contain a numerical value that described the operating system in the OVF.
      
      
        "Name": the name to give to the new virtual machine. There can be at most one such array item;
        if none is present on import, then an automatic name will be created from the operating system
        type. The corresponding item im @a OVFValues[] will contain the suggested virtual machine name
        from the OVF file, and @a aVBoxValues[] will contain a suggestion for a unique VirtualBox
        <link to="IMachine"/> name that does not exist yet.
      
      
          "Description": an arbitrary description.
      
      
          "License": the EULA section from the OVF, if present. It is the responsibility of the calling
          code to display such a license for agreement; the Main API does not enforce any such policy.
      
      
          Miscellaneous: reserved for future use.
      
      
        "CPU": the number of CPUs. There can be at most one such item, which will presently be ignored.
      
      
        "Memory": the amount of guest RAM, in bytes. There can be at most one such array item; if none
        is present on import, then VirtualBox will set a meaningful default based on the operating system
        type.
      
      
        "HardDiskControllerIDE": an IDE hard disk controller. There can be at most two such items.
        An optional value in @a OVFValues[] and @a aVBoxValues[] can be "PIIX3" or "PIIX4" to specify
        the type of IDE controller; this corresponds to the ResourceSubType element which VirtualBox
        writes into the OVF.
        The matching item in the @a aRefs[] array will contain an integer that items of the "Harddisk"
        type can use to specify which hard disk controller a virtual disk should be connected to.
        Note that in OVF, an IDE controller has two channels, corresponding to "master" and "slave"
        in traditional terminology, whereas the IDE storage controller that VirtualBox supports in
        its virtual machines supports four channels (primary master, primary slave, secondary master,
        secondary slave) and thus maps to two IDE controllers in the OVF sense.
      
      
        "HardDiskControllerSATA": an SATA hard disk controller. There can be at most one such item. This
        has no value in @a OVFValues[] or @a aVBoxValues[].
        The matching item in the @a aRefs[] array will be used as with IDE controllers (see above).
      
      
        "HardDiskControllerSCSI": a SCSI hard disk controller. There can be at most one such item.
        The items in @a OVFValues[] and @a aVBoxValues[] will either be "LsiLogic", "BusLogic" or
        "LsiLogicSas". (Note that in OVF, the LsiLogicSas controller is treated as a SCSI controller
        whereas VirtualBox considers it a class of storage controllers of its own; see
        <link to="StorageControllerType"/>).
        The matching item in the @a aRefs[] array will be used as with IDE controllers (see above).
      
      
        "HardDiskImage": a virtual hard disk, most probably as a reference to an image file. There can be an
        arbitrary number of these items, one for each virtual disk image that accompanies the OVF.

        The array item in @a OVFValues[] will contain the file specification from the OVF file (without
        a path since the image file should be in the same location as the OVF file itself), whereas the
        item in @a aVBoxValues[] will contain a qualified path specification to where VirtualBox uses the
        hard disk image. This means that on import the image will be copied and converted from the
        "ovf" location to the "vbox" location; on export, this will be handled the other way round.

        The matching item in the @a aExtraConfigValues[] array must contain a string of the following
        format: "controller=<index>;channel=<c>"
        In this string, <index> must be an integer specifying the hard disk controller to connect
        the image to. That number must be the index of an array item with one of the hard disk controller
        types (HardDiskControllerSCSI, HardDiskControllerSATA, HardDiskControllerIDE).
        In addition, <c> must specify the channel to use on that controller. For IDE controllers,
        this can be 0 or 1 for master or slave, respectively. For compatibility with VirtualBox versions
        before 3.2, the values 2 and 3 (for secondary master and secondary slave) are also supported, but
        no longer exported. For SATA and SCSI controllers, the channel can range from 0-29.
      
      
        "CDROM": a virtual CD-ROM drive. The matching item in @a aExtraConfigValue[] contains the same
        attachment information as with "HardDiskImage" items.
      
      
        "CDROM": a virtual floppy drive. The matching item in @a aExtraConfigValue[] contains the same
        attachment information as with "HardDiskImage" items.
      
      
        "NetworkAdapter": a network adapter. The array item in @a aVBoxValues[] will specify the hardware
        for the network adapter, whereas the array item in @a aExtraConfigValues[] will have a string
        of the "type=<X>" format, where <X> must be either "NAT" or "Bridged".
      
      
          "USBController": a USB controller. There can be at most one such item. If and only if such an
          item ispresent, USB support will be enabled for the new virtual machine.
      
      
          "SoundCard": a sound card. There can be at most one such item. If and only if such an item is
          present, sound support will be enabled for the new virtual machine. Note that the virtual
          machine in VirtualBox will always be presented with the standard VirtualBox soundcard, which
          may be different from the virtual soundcard expected by the appliance.

        out types of type VirtualSystemDescriptionType
            <desc/>

        out refs of type str
            <desc/>

        out ovf_values of type str
            <desc/>

        out v_box_values of type str
            <desc/>

        out extra_config_values of type str
            <desc/>

        """
        (types, refs, ovf_values, v_box_values, extra_config_values) = self._call("getDescription")
        types = [VirtualSystemDescriptionType(a) for a in types]
        return (types, refs, ovf_values, v_box_values, extra_config_values)

    def get_description_by_type(self, type_p):
        """This is the same as <link to="#getDescription"/> except that you can specify which types
      should be returned.

        in type_p of type VirtualSystemDescriptionType
            <desc/>

        out types of type VirtualSystemDescriptionType
            <desc/>

        out refs of type str
            <desc/>

        out ovf_values of type str
            <desc/>

        out v_box_values of type str
            <desc/>

        out extra_config_values of type str
            <desc/>

        """
        if not isinstance(type_p, VirtualSystemDescriptionType):
            raise TypeError("type_p can only be an instance of type VirtualSystemDescriptionType")
        (types, refs, ovf_values, v_box_values, extra_config_values) = self._call("getDescriptionByType",
                     in_p=[type_p])
        types = [VirtualSystemDescriptionType(a) for a in types]
        return (types, refs, ovf_values, v_box_values, extra_config_values)

    def get_values_by_type(self, type_p, which):
        """This is the same as <link to="#getDescriptionByType"/> except that you can specify which
      value types should be returned. See <link to="VirtualSystemDescriptionValueType"/> for possible
      values.

        in type_p of type VirtualSystemDescriptionType
            <desc/>

        in which of type VirtualSystemDescriptionValueType
            <desc/>

        return values of type str
            <desc/>

        """
        if not isinstance(type_p, VirtualSystemDescriptionType):
            raise TypeError("type_p can only be an instance of type VirtualSystemDescriptionType")
        if not isinstance(which, VirtualSystemDescriptionValueType):
            raise TypeError("which can only be an instance of type VirtualSystemDescriptionValueType")
        values = self._call("getValuesByType",
                     in_p=[type_p, which])
        return values

    def set_final_values(self, enabled, v_box_values, extra_config_values):
        """This method allows the appliance's user to change the configuration for the virtual
        system descriptions. For each array item returned from <link to="#getDescription"/>,
        you must pass in one boolean value and one configuration value.

        Each item in the boolean array determines whether the particular configuration item
        should be enabled.
        You can only disable items of the types HardDiskControllerIDE, HardDiskControllerSATA,
        HardDiskControllerSCSI, HardDiskImage, CDROM, Floppy, NetworkAdapter, USBController
        and SoundCard.

        For the "vbox" and "extra configuration" values, if you pass in the same arrays
        as returned in the aVBoxValues and aExtraConfigValues arrays from <link to="#getDescription"/>,
        the configuration remains unchanged. Please see the documentation for <link to="#getDescription"/>
        for valid configuration values for the individual array item types. If the
        corresponding item in the aEnabled array is @c false, the configuration value is ignored.

        in enabled of type bool
            <desc/>

        in v_box_values of type str
            <desc/>

        in extra_config_values of type str
            <desc/>

        """
        if not isinstance(enabled, list):
            raise TypeError("enabled can only be an instance of type list")
        for a in enabled[:10]:
            if not isinstance(a, bool):
                raise TypeError(\
                        "array can only contain objects of type bool")
        if not isinstance(v_box_values, list):
            raise TypeError("v_box_values can only be an instance of type list")
        for a in v_box_values[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(extra_config_values, list):
            raise TypeError("extra_config_values can only be an instance of type list")
        for a in extra_config_values[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        self._call("setFinalValues",
                     in_p=[enabled, v_box_values, extra_config_values])

    def add_description(self, type_p, v_box_value, extra_config_value):
        """This method adds an additional description entry to the stack of already
      available descriptions for this virtual system. This is handy for writing
      values which aren't directly supported by VirtualBox. One example would
      be the License type of <link to="VirtualSystemDescriptionType"/>.

        in type_p of type VirtualSystemDescriptionType
            <desc/>

        in v_box_value of type str
            <desc/>

        in extra_config_value of type str
            <desc/>

        """
        if not isinstance(type_p, VirtualSystemDescriptionType):
            raise TypeError("type_p can only be an instance of type VirtualSystemDescriptionType")
        if type(v_box_value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(extra_config_value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("addDescription",
                     in_p=[type_p, v_box_value, extra_config_value])


class IInternalMachineControl(Interface):
    """
    Updates the flag whether the saved state file is removed on a
        machine state change from Saved to PoweredOff.
    """
    __uuid__ = 'dca36a92-703c-4649-98a4-f40c1ef0c336'
    __wsmap__ = 'suppress'
    
    def set_remove_saved_state_file(self, remove):
        """Updates the flag whether the saved state file is removed on a
        machine state change from Saved to PoweredOff.

        in remove of type bool

        """
        if not isinstance(remove, bool):
            raise TypeError("remove can only be an instance of type bool")
        self._call("setRemoveSavedStateFile",
                     in_p=[remove])

    def update_state(self, state):
        """Updates the VM state.
        
          This operation will also update the settings file with the correct
          information about the saved state file and delete this file from disk
          when appropriate.

        in state of type MachineState

        """
        if not isinstance(state, MachineState):
            raise TypeError("state can only be an instance of type MachineState")
        self._call("updateState",
                     in_p=[state])

    def get_ipc_id(self):
        """

        return id_p of type str

        """
        id_p = self._call("getIPCId")
        return id_p

    def begin_power_up(self, progress):
        """Tells VBoxSVC that <link to="IConsole::powerUp"/> is under ways and
        gives it the progress object that should be part of any pending
        <link to="IMachine::launchVMProcess"/> operations. The progress
        object may be called back to reflect an early cancelation, so some care
        have to be taken with respect to any cancelation callbacks. The console
        object will call <link to="IInternalMachineControl::endPowerUp"/>
        to signal the completion of the progress object.

        in progress of type IProgress

        """
        if not isinstance(progress, IProgress):
            raise TypeError("progress can only be an instance of type IProgress")
        self._call("beginPowerUp",
                     in_p=[progress])

    def end_power_up(self, result):
        """Tells VBoxSVC that <link to="IConsole::powerUp"/> has completed.
        This method may query status information from the progress object it
        received in <link to="IInternalMachineControl::beginPowerUp"/> and copy
        it over to any in-progress <link to="IMachine::launchVMProcess"/>
        call in order to complete that progress object.

        in result of type int

        """
        if not isinstance(result, int):
            raise TypeError("result can only be an instance of type int")
        self._call("endPowerUp",
                     in_p=[result])

    def begin_powering_down(self):
        """Called by the VM process to inform the server it wants to
        stop the VM execution and power down.

        out progress of type IProgress
            Progress object created by VBoxSVC to wait until
          the VM is powered down.

        """
        progress = self._call("beginPoweringDown")
        progress = IProgress(progress)
        return progress

    def end_powering_down(self, result, err_msg):
        """Called by the VM process to inform the server that powering
        down previously requested by #beginPoweringDown is either
        successfully finished or there was a failure.

        in result of type int
            @c S_OK to indicate success.

        in err_msg of type str
            @c human readable error message in case of failure.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        """
        if not isinstance(result, int):
            raise TypeError("result can only be an instance of type int")
        if type(err_msg) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("endPoweringDown",
                     in_p=[result, err_msg])

    def run_usb_device_filters(self, device):
        """Asks the server to run USB devices filters of the associated
        machine against the given USB device and tell if there is
        a match.
        
          Intended to be used only for remote USB devices. Local
          ones don't require to call this method (this is done
          implicitly by the Host and USBProxyService).

        in device of type IUSBDevice

        out matched of type bool

        out masked_interfaces of type int

        """
        if not isinstance(device, IUSBDevice):
            raise TypeError("device can only be an instance of type IUSBDevice")
        (matched, masked_interfaces) = self._call("runUSBDeviceFilters",
                     in_p=[device])
        return (matched, masked_interfaces)

    def capture_usb_device(self, id_p):
        """Requests a capture of the given host USB device.
        When the request is completed, the VM process will
        get a <link to="IInternalSessionControl::onUSBDeviceAttach"/>
        notification.

        in id_p of type str

        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("captureUSBDevice",
                     in_p=[id_p])

    def detach_usb_device(self, id_p, done):
        """Notification that a VM is going to detach (@a done = @c false) or has
        already detached (@a done = @c true) the given USB device.
        When the @a done = @c true request is completed, the VM process will
        get a <link to="IInternalSessionControl::onUSBDeviceDetach"/>
        notification.
        
          In the @a done = @c true case, the server must run its own filters
          and filters of all VMs but this one on the detached device
          as if it were just attached to the host computer.

        in id_p of type str

        in done of type bool

        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(done, bool):
            raise TypeError("done can only be an instance of type bool")
        self._call("detachUSBDevice",
                     in_p=[id_p, done])

    def auto_capture_usb_devices(self):
        """Requests a capture all matching USB devices attached to the host.
        When the request is completed, the VM process will
        get a <link to="IInternalSessionControl::onUSBDeviceAttach"/>
        notification per every captured device.

        """
        self._call("autoCaptureUSBDevices")

    def detach_all_usb_devices(self, done):
        """Notification that a VM that is being powered down. The done
        parameter indicates whether which stage of the power down
        we're at. When @a done = @c false the VM is announcing its
        intentions, while when @a done = @c true the VM is reporting
        what it has done.
        
          In the @a done = @c true case, the server must run its own filters
          and filters of all VMs but this one on all detach devices as
          if they were just attached to the host computer.

        in done of type bool

        """
        if not isinstance(done, bool):
            raise TypeError("done can only be an instance of type bool")
        self._call("detachAllUSBDevices",
                     in_p=[done])

    def on_session_end(self, session):
        """Triggered by the given session object when the session is about
        to close normally.

        in session of type ISession
            Session that is being closed

        return progress of type IProgress
            Used to wait until the corresponding machine is actually
          dissociated from the given session on the server.
          Returned only when this session is a direct one.

        """
        if not isinstance(session, ISession):
            raise TypeError("session can only be an instance of type ISession")
        progress = self._call("onSessionEnd",
                     in_p=[session])
        progress = IProgress(progress)
        return progress

    def begin_saving_state(self):
        """Called by the VM process to inform the server it wants to
        save the current state and stop the VM execution.

        out progress of type IProgress
            Progress object created by VBoxSVC to wait until
          the state is saved.

        out state_file_path of type str
            File path the VM process must save the execution state to.

        """
        (progress, state_file_path) = self._call("beginSavingState")
        progress = IProgress(progress)
        return (progress, state_file_path)

    def end_saving_state(self, result, err_msg):
        """Called by the VM process to inform the server that saving
        the state previously requested by #beginSavingState is either
        successfully finished or there was a failure.

        in result of type int
            @c S_OK to indicate success.

        in err_msg of type str
            @c human readable error message in case of failure.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        """
        if not isinstance(result, int):
            raise TypeError("result can only be an instance of type int")
        if type(err_msg) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("endSavingState",
                     in_p=[result, err_msg])

    def adopt_saved_state(self, saved_state_file):
        """Gets called by <link to="IConsole::adoptSavedState"/>.

        in saved_state_file of type str
            Path to the saved state file to adopt.

        raises VBOX_E_FILE_ERROR
            Invalid saved state file path.
        
        """
        if type(saved_state_file) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("adoptSavedState",
                     in_p=[saved_state_file])

    def begin_taking_snapshot(self, initiator, name, description, console_progress, f_taking_snapshot_online):
        """Called from the VM process to request from the server to perform the
        server-side actions of creating a snapshot (creating differencing images
        and the snapshot object).

        in initiator of type IConsole
            The console object that initiated this call.

        in name of type str
            Snapshot name.

        in description of type str
            Snapshot description.

        in console_progress of type IProgress
            Progress object created by the VM process tracking the
          snapshot's progress. This has the following sub-operations:
          
            setting up (weight 1);
            one for each medium attachment that needs a differencing image (weight 1 each);
            another one to copy the VM state (if offline with saved state, weight is VM memory size in MB);
            another one to save the VM state (if online, weight is VM memory size in MB);
            finishing up (weight 1)

        in f_taking_snapshot_online of type bool
            Whether this is an online snapshot (i.e. the machine is running).

        out state_file_path of type str
            File path the VM process must save the execution state to.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        """
        if not isinstance(initiator, IConsole):
            raise TypeError("initiator can only be an instance of type IConsole")
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(description) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(console_progress, IProgress):
            raise TypeError("console_progress can only be an instance of type IProgress")
        if not isinstance(f_taking_snapshot_online, bool):
            raise TypeError("f_taking_snapshot_online can only be an instance of type bool")
        state_file_path = self._call("beginTakingSnapshot",
                     in_p=[initiator, name, description, console_progress, f_taking_snapshot_online])
        return state_file_path

    def end_taking_snapshot(self, success):
        """Called by the VM process to inform the server that the snapshot
        previously requested by #beginTakingSnapshot is either
        successfully taken or there was a failure.

        in success of type bool
            @c true to indicate success and @c false otherwise

        """
        if not isinstance(success, bool):
            raise TypeError("success can only be an instance of type bool")
        self._call("endTakingSnapshot",
                     in_p=[success])

    def delete_snapshot(self, initiator, start_id, end_id, delete_all_children):
        """Gets called by <link to="IConsole::deleteSnapshot"/>,
        <link to="IConsole::deleteSnapshotAndAllChildren"/> and
        <link to="IConsole::deleteSnapshotRange"/>.

        in initiator of type IConsole
            The console object that initiated this call.

        in start_id of type str
            UUID of the first snapshot to delete.

        in end_id of type str
            UUID of the last snapshot to delete.

        in delete_all_children of type bool
            Whether all children should be deleted.

        out machine_state of type MachineState
            New machine state after this operation is started.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_OBJECT_STATE
            Snapshot has more than one child snapshot. Only possible if the
          delete operation does not delete all children or the range does
          not meet the linearity condition.
        
        """
        if not isinstance(initiator, IConsole):
            raise TypeError("initiator can only be an instance of type IConsole")
        if type(start_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(end_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(delete_all_children, bool):
            raise TypeError("delete_all_children can only be an instance of type bool")
        (machine_state, progress) = self._call("deleteSnapshot",
                     in_p=[initiator, start_id, end_id, delete_all_children])
        machine_state = MachineState(machine_state)
        progress = IProgress(progress)
        return (machine_state, progress)

    def finish_online_merge_medium(self, medium_attachment, source, target, merge_forward, parent_for_target, children_to_reparent):
        """Gets called by <link to="IInternalSessionControl::onlineMergeMedium"/>.

        in medium_attachment of type IMediumAttachment
            The medium attachment which needs to be cleaned up.

        in source of type IMedium
            Merge source medium.

        in target of type IMedium
            Merge target medium.

        in merge_forward of type bool
            Merge direction.

        in parent_for_target of type IMedium
            For forward merges: new parent for target medium.

        in children_to_reparent of type IMedium
            For backward merges: list of media which need their parent UUID
        updated.

        """
        if not isinstance(medium_attachment, IMediumAttachment):
            raise TypeError("medium_attachment can only be an instance of type IMediumAttachment")
        if not isinstance(source, IMedium):
            raise TypeError("source can only be an instance of type IMedium")
        if not isinstance(target, IMedium):
            raise TypeError("target can only be an instance of type IMedium")
        if not isinstance(merge_forward, bool):
            raise TypeError("merge_forward can only be an instance of type bool")
        if not isinstance(parent_for_target, IMedium):
            raise TypeError("parent_for_target can only be an instance of type IMedium")
        if not isinstance(children_to_reparent, list):
            raise TypeError("children_to_reparent can only be an instance of type list")
        for a in children_to_reparent[:10]:
            if not isinstance(a, IMedium):
                raise TypeError(\
                        "array can only contain objects of type IMedium")
        self._call("finishOnlineMergeMedium",
                     in_p=[medium_attachment, source, target, merge_forward, parent_for_target, children_to_reparent])

    def restore_snapshot(self, initiator, snapshot):
        """Gets called by <link to="IConsole::restoreSnapshot"/>.

        in initiator of type IConsole
            The console object that initiated this call.

        in snapshot of type ISnapshot
            The snapshot to restore the VM state from.

        out machine_state of type MachineState
            New machine state after this operation is started.

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        if not isinstance(initiator, IConsole):
            raise TypeError("initiator can only be an instance of type IConsole")
        if not isinstance(snapshot, ISnapshot):
            raise TypeError("snapshot can only be an instance of type ISnapshot")
        (machine_state, progress) = self._call("restoreSnapshot",
                     in_p=[initiator, snapshot])
        machine_state = MachineState(machine_state)
        progress = IProgress(progress)
        return (machine_state, progress)

    def pull_guest_properties(self):
        """Get the list of the guest properties matching a set of patterns along
        with their values, time stamps and flags and give responsibility for
        managing properties to the console.

        out names of type str
            The names of the properties returned.

        out values of type str
            The values of the properties returned. The array entries match the
          corresponding entries in the @a name array.

        out timestamps of type int
            The time stamps of the properties returned. The array entries match
          the corresponding entries in the @a name array.

        out flags of type str
            The flags of the properties returned. The array entries match the
          corresponding entries in the @a name array.

        """
        (names, values, timestamps, flags) = self._call("pullGuestProperties")
        return (names, values, timestamps, flags)

    def push_guest_property(self, name, value, timestamp, flags):
        """Update a single guest property in IMachine.

        in name of type str
            The name of the property to be updated.

        in value of type str
            The value of the property.

        in timestamp of type int
            The timestamp of the property.

        in flags of type str
            The flags of the property.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(timestamp, int):
            raise TypeError("timestamp can only be an instance of type int")
        if type(flags) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("pushGuestProperty",
                     in_p=[name, value, timestamp, flags])

    def lock_media(self):
        """Locks all media attached to the machine for writing and parents of
        attached differencing media (if any) for reading. This operation is
        atomic so that if it fails no media is actually locked.

        This method is intended to be called when the machine is in Starting or
        Restoring state. The locked media will be automatically unlocked when
        the machine is powered off or crashed.

        """
        self._call("lockMedia")

    def unlock_media(self):
        """Unlocks all media previously locked using
        <link to="IInternalMachineControl::lockMedia"/>.

        This method is intended to be used with teleportation so that it is
        possible to teleport between processes on the same machine.

        """
        self._call("unlockMedia")

    def eject_medium(self, attachment):
        """Tells VBoxSVC that the guest has ejected the medium associated with
        the medium attachment.

        in attachment of type IMediumAttachment
            The medium attachment where the eject happened.

        return new_attachment of type IMediumAttachment
            A new reference to the medium attachment, as the config change can
          result in the creation of a new instance.

        """
        if not isinstance(attachment, IMediumAttachment):
            raise TypeError("attachment can only be an instance of type IMediumAttachment")
        new_attachment = self._call("ejectMedium",
                     in_p=[attachment])
        new_attachment = IMediumAttachment(new_attachment)
        return new_attachment

    def report_vm_statistics(self, valid_stats, cpu_user, cpu_kernel, cpu_idle, mem_total, mem_free, mem_balloon, mem_shared, mem_cache, paged_total, mem_alloc_total, mem_free_total, mem_balloon_total, mem_shared_total, vm_net_rx, vm_net_tx):
        """Passes statistics collected by VM (including guest statistics) to VBoxSVC.

        in valid_stats of type int
            Mask defining which parameters are valid. For example: 0x11 means
          that cpuIdle and XXX are valid. Other parameters should be ignored.

        in cpu_user of type int
            Percentage of processor time spent in user mode as seen by the guest.

        in cpu_kernel of type int
            Percentage of processor time spent in kernel mode as seen by the guest.

        in cpu_idle of type int
            Percentage of processor time spent idling as seen by the guest.

        in mem_total of type int
            Total amount of physical guest RAM.

        in mem_free of type int
            Free amount of physical guest RAM.

        in mem_balloon of type int
            Amount of ballooned physical guest RAM.

        in mem_shared of type int
            Amount of shared physical guest RAM.

        in mem_cache of type int
            Total amount of guest (disk) cache memory.

        in paged_total of type int
            Total amount of space in the page file.

        in mem_alloc_total of type int
            Total amount of memory allocated by the hypervisor.

        in mem_free_total of type int
            Total amount of free memory available in the hypervisor.

        in mem_balloon_total of type int
            Total amount of memory ballooned by the hypervisor.

        in mem_shared_total of type int
            Total amount of shared memory in the hypervisor.

        in vm_net_rx of type int
            Network receive rate for VM.

        in vm_net_tx of type int
            Network transmit rate for VM.

        """
        if not isinstance(valid_stats, int):
            raise TypeError("valid_stats can only be an instance of type int")
        if not isinstance(cpu_user, int):
            raise TypeError("cpu_user can only be an instance of type int")
        if not isinstance(cpu_kernel, int):
            raise TypeError("cpu_kernel can only be an instance of type int")
        if not isinstance(cpu_idle, int):
            raise TypeError("cpu_idle can only be an instance of type int")
        if not isinstance(mem_total, int):
            raise TypeError("mem_total can only be an instance of type int")
        if not isinstance(mem_free, int):
            raise TypeError("mem_free can only be an instance of type int")
        if not isinstance(mem_balloon, int):
            raise TypeError("mem_balloon can only be an instance of type int")
        if not isinstance(mem_shared, int):
            raise TypeError("mem_shared can only be an instance of type int")
        if not isinstance(mem_cache, int):
            raise TypeError("mem_cache can only be an instance of type int")
        if not isinstance(paged_total, int):
            raise TypeError("paged_total can only be an instance of type int")
        if not isinstance(mem_alloc_total, int):
            raise TypeError("mem_alloc_total can only be an instance of type int")
        if not isinstance(mem_free_total, int):
            raise TypeError("mem_free_total can only be an instance of type int")
        if not isinstance(mem_balloon_total, int):
            raise TypeError("mem_balloon_total can only be an instance of type int")
        if not isinstance(mem_shared_total, int):
            raise TypeError("mem_shared_total can only be an instance of type int")
        if not isinstance(vm_net_rx, int):
            raise TypeError("vm_net_rx can only be an instance of type int")
        if not isinstance(vm_net_tx, int):
            raise TypeError("vm_net_tx can only be an instance of type int")
        self._call("reportVmStatistics",
                     in_p=[valid_stats, cpu_user, cpu_kernel, cpu_idle, mem_total, mem_free, mem_balloon, mem_shared, mem_cache, paged_total, mem_alloc_total, mem_free_total, mem_balloon_total, mem_shared_total, vm_net_rx, vm_net_tx])


class IBIOSSettings(Interface):
    """
    The IBIOSSettings interface represents BIOS settings of the virtual
        machine. This is used only in the <link to="IMachine::BIOSSettings"/> attribute.
    """
    __uuid__ = '38b54279-dc35-4f5e-a431-835b867c6b5e'
    __wsmap__ = 'managed'
    
    @property
    def logo_fade_in(self):
        """Get or set bool value for 'logoFadeIn'
        Fade in flag for BIOS logo animation.
        """
        ret = self._get_attr("logoFadeIn")
        return ret

    @logo_fade_in.setter
    def logo_fade_in(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("logoFadeIn", value)

    @property
    def logo_fade_out(self):
        """Get or set bool value for 'logoFadeOut'
        Fade out flag for BIOS logo animation.
        """
        ret = self._get_attr("logoFadeOut")
        return ret

    @logo_fade_out.setter
    def logo_fade_out(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("logoFadeOut", value)

    @property
    def logo_display_time(self):
        """Get or set int value for 'logoDisplayTime'
        BIOS logo display time in milliseconds (0 = default).
        """
        ret = self._get_attr("logoDisplayTime")
        return ret

    @logo_display_time.setter
    def logo_display_time(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("logoDisplayTime", value)

    @property
    def logo_image_path(self):
        """Get or set str value for 'logoImagePath'
        Local file system path for external BIOS splash image. Empty string
        means the default image is shown on boot.
        """
        ret = self._get_attr("logoImagePath")
        return ret

    @logo_image_path.setter
    def logo_image_path(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("logoImagePath", value)

    @property
    def boot_menu_mode(self):
        """Get or set BIOSBootMenuMode value for 'bootMenuMode'
        Mode of the BIOS boot device menu.
        """
        ret = self._get_attr("bootMenuMode")
        return BIOSBootMenuMode(ret)

    @boot_menu_mode.setter
    def boot_menu_mode(self, value):
        if not isinstance(value, BIOSBootMenuMode):
            raise TypeError("value is not an instance of BIOSBootMenuMode")
        return self._set_attr("bootMenuMode", value)

    @property
    def acpi_enabled(self):
        """Get or set bool value for 'ACPIEnabled'
        ACPI support flag.
        """
        ret = self._get_attr("ACPIEnabled")
        return ret

    @acpi_enabled.setter
    def acpi_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("ACPIEnabled", value)

    @property
    def ioapic_enabled(self):
        """Get or set bool value for 'IOAPICEnabled'
        IO APIC support flag. If set, VirtualBox will provide an IO APIC
        and support IRQs above 15.
        """
        ret = self._get_attr("IOAPICEnabled")
        return ret

    @ioapic_enabled.setter
    def ioapic_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("IOAPICEnabled", value)

    @property
    def time_offset(self):
        """Get or set int value for 'timeOffset'
        Offset in milliseconds from the host system time. This allows for
        guests running with a different system date/time than the host.
        It is equivalent to setting the system date/time in the BIOS except
        it is not an absolute value but a relative one. Guest Additions
        time synchronization honors this offset.
        """
        ret = self._get_attr("timeOffset")
        return ret

    @time_offset.setter
    def time_offset(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("timeOffset", value)

    @property
    def pxe_debug_enabled(self):
        """Get or set bool value for 'PXEDebugEnabled'
        PXE debug logging flag. If set, VirtualBox will write extensive
        PXE trace information to the release log.
        """
        ret = self._get_attr("PXEDebugEnabled")
        return ret

    @pxe_debug_enabled.setter
    def pxe_debug_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("PXEDebugEnabled", value)


class IPCIAddress(Interface):
    """
    Address on the PCI bus.
    """
    __uuid__ = 'c984d15f-e191-400b-840e-970f3dad7296'
    __wsmap__ = 'managed'
    
    @property
    def bus(self):
        """Get or set int value for 'bus'
        Bus number.
        """
        ret = self._get_attr("bus")
        return ret

    @bus.setter
    def bus(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("bus", value)

    @property
    def device(self):
        """Get or set int value for 'device'
        Device number.
        """
        ret = self._get_attr("device")
        return ret

    @device.setter
    def device(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("device", value)

    @property
    def dev_function(self):
        """Get or set int value for 'devFunction'
        Device function number.
        """
        ret = self._get_attr("devFunction")
        return ret

    @dev_function.setter
    def dev_function(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("devFunction", value)

    def as_long(self):
        """Convert PCI address into long.

        return result of type int

        """
        result = self._call("asLong")
        return result

    def from_long(self, number):
        """Make PCI address from long.

        in number of type int

        """
        if not isinstance(number, int):
            raise TypeError("number can only be an instance of type int")
        self._call("fromLong",
                     in_p=[number])


class IPCIDeviceAttachment(Interface):
    """
    Information about PCI attachments.
    """
    __uuid__ = '91f33d6f-e621-4f70-a77e-15f0e3c714d5'
    __wsmap__ = 'struct'
    
    @property
    def name(self):
        """Get str value for 'name'
        Device name.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def is_physical_device(self):
        """Get bool value for 'isPhysicalDevice'
        If this is physical or virtual device.
        """
        ret = self._get_attr("isPhysicalDevice")
        return ret

    @property
    def host_address(self):
        """Get int value for 'hostAddress'
        Address of device on the host, applicable only to host devices.
        """
        ret = self._get_attr("hostAddress")
        return ret

    @property
    def guest_address(self):
        """Get int value for 'guestAddress'
        Address of device on the guest.
        """
        ret = self._get_attr("guestAddress")
        return ret


class IMachine(Interface):
    """
    The IMachine interface represents a virtual machine, or guest, created
      in VirtualBox.

      This interface is used in two contexts. First of all, a collection of
      objects implementing this interface is stored in the
      <link to="IVirtualBox::machines"/> attribute which lists all the virtual
      machines that are currently registered with this VirtualBox
      installation. Also, once a session has been opened for the given virtual
      machine (e.g. the virtual machine is running), the machine object
      associated with the open session can be queried from the session object;
      see <link to="ISession"/> for details.

      The main role of this interface is to expose the settings of the virtual
      machine and provide methods to change various aspects of the virtual
      machine's configuration. For machine objects stored in the
      <link to="IVirtualBox::machines"/> collection, all attributes are
      read-only unless explicitly stated otherwise in individual attribute
      and method descriptions.

      In order to change a machine setting, a session for this machine must be
      opened using one of the <link to="IMachine::lockMachine"/> or
      <link to="IMachine::launchVMProcess"/> methods. After the
      machine has been successfully locked for a session, a mutable machine object
      needs to be queried from the session object and then the desired settings
      changes can be applied to the returned object using IMachine attributes and
      methods. See the <link to="ISession"/> interface description for more
      information about sessions.

      Note that IMachine does not provide methods to control virtual machine
      execution (such as start the machine, or power it down) -- these methods
      are grouped in a separate interface called <link to="IConsole"/>.

      <link to="ISession"/>, <link to="IConsole"/>
    """
    __uuid__ = 'f6258810-a760-11e2-9e96-0800200c9a66'
    __wsmap__ = 'managed'
    
    @property
    def parent(self):
        """Get IVirtualBox value for 'parent'
        Associated parent object.
        """
        ret = self._get_attr("parent")
        return IVirtualBox(ret)

    @property
    def icon(self):
        """Get or set str value for 'icon'
        Overriden VM Icon details.
        """
        ret = self._get_attr("icon")
        return ret

    @icon.setter
    def icon(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("icon", value)

    @property
    def accessible(self):
        """Get bool value for 'accessible'
        Whether this virtual machine is currently accessible or not.

        A machine is always deemed accessible unless it is registered and
        its settings file cannot be read or parsed (either because the file itself
        is unavailable or has invalid XML contents).

        Every time this property is read, the accessibility state of
        this machine is re-evaluated. If the returned value is @c false,
        the <link to="#accessError"/> property may be used to get the
        detailed error information describing the reason of
        inaccessibility, including XML error messages.

        When the machine is inaccessible, only the following properties
        can be used on it:
        
          <link to="#parent"/>
          <link to="#id"/>
          <link to="#settingsFilePath"/>
          <link to="#accessible"/>
          <link to="#accessError"/>
        

        An attempt to access any other property or method will return
        an error.

        The only possible action you can perform on an inaccessible
        machine is to unregister it using the
        <link to="IMachine::unregister"/> call (or, to check
        for the accessibility state once more by querying this
        property).

        
          In the current implementation, once this property returns
          @c true, the machine will never become inaccessible
          later, even if its settings file cannot be successfully
          read/written any more (at least, until the VirtualBox
          server is restarted). This limitation may be removed in
          future releases.
        """
        ret = self._get_attr("accessible")
        return ret

    @property
    def access_error(self):
        """Get IVirtualBoxErrorInfo value for 'accessError'
        Error information describing the reason of machine
        inaccessibility.

        Reading this property is only valid after the last call to
        <link to="#accessible"/> returned @c false (i.e. the
        machine is currently inaccessible). Otherwise, a @c null
        IVirtualBoxErrorInfo object will be returned.
        """
        ret = self._get_attr("accessError")
        return IVirtualBoxErrorInfo(ret)

    @property
    def name(self):
        """Get or set str value for 'name'
        Name of the virtual machine.

        Besides being used for human-readable identification purposes
        everywhere in VirtualBox, the virtual machine name is also used
        as a name of the machine's settings file and as a name of the
        subdirectory this settings file resides in. Thus, every time you
        change the value of this property, the settings file will be
        renamed once you call <link to="#saveSettings"/> to confirm the
        change. The containing subdirectory will be also renamed, but
        only if it has exactly the same name as the settings file
        itself prior to changing this property (for backward compatibility
        with previous API releases). The above implies the following
        limitations:
        
          The machine name cannot be empty.
          The machine name can contain only characters that are valid
            file name characters according to the rules of the file
            system used to store VirtualBox configuration.
          You cannot have two or more machines with the same name
            if they use the same subdirectory for storing the machine
            settings files.
          You cannot change the name of the machine if it is running,
            or if any file in the directory containing the settings file
            is being used by another running machine or by any other
            process in the host operating system at a time when
            <link to="#saveSettings"/> is called.
          
        
        If any of the above limitations are hit, <link to="#saveSettings"/>
        will return an appropriate error message explaining the exact
        reason and the changes you made to this machine will not be saved.

        Starting with VirtualBox 4.0, a ".vbox" extension of the settings
        file is recommended, but not enforced. (Previous versions always
        used a generic ".xml" extension.)
        """
        ret = self._get_attr("name")
        return ret

    @name.setter
    def name(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("name", value)

    @property
    def description(self):
        """Get or set str value for 'description'
        Description of the virtual machine.

        The description attribute can contain any text and is
        typically used to describe the hardware and software
        configuration of the virtual machine in detail (i.e. network
        settings, versions of the installed software and so on).
        """
        ret = self._get_attr("description")
        return ret

    @description.setter
    def description(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("description", value)

    @property
    def id_p(self):
        """Get str value for 'id'
        UUID of the virtual machine.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def groups(self):
        """Get or set str value for 'groups'
        Array of machine group names of which this machine is a member.
        "" and "/" are synonyms for the toplevel group. Each
        group is only listed once, however they are listed in no particular
        order and there is no guarantee that there are no gaps in the group
        hierarchy (i.e. "/group",
        "/group/subgroup/subsubgroup" is a valid result).
        """
        ret = self._get_attr("groups")
        return ret

    @groups.setter
    def groups(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("groups", value)

    @property
    def os_type_id(self):
        """Get or set str value for 'OSTypeId'
        User-defined identifier of the Guest OS type.
        You may use <link to="IVirtualBox::getGuestOSType"/> to obtain
        an IGuestOSType object representing details about the given
        Guest OS type.
        
          This value may differ from the value returned by
          <link to="IGuest::OSTypeId"/> if Guest Additions are
          installed to the guest OS.
        """
        ret = self._get_attr("OSTypeId")
        return ret

    @os_type_id.setter
    def os_type_id(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("OSTypeId", value)

    @property
    def hardware_version(self):
        """Get or set str value for 'hardwareVersion'
        Hardware version identifier. Internal use only for now.
        """
        ret = self._get_attr("hardwareVersion")
        return ret

    @hardware_version.setter
    def hardware_version(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("hardwareVersion", value)

    @property
    def hardware_uuid(self):
        """Get or set str value for 'hardwareUUID'
        The UUID presented to the guest via memory tables, hardware and guest
        properties. For most VMs this is the same as the @a id, but for VMs
        which have been cloned or teleported it may be the same as the source
        VM. The latter is because the guest shouldn't notice that it was
        cloned or teleported.
        """
        ret = self._get_attr("hardwareUUID")
        return ret

    @hardware_uuid.setter
    def hardware_uuid(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("hardwareUUID", value)

    @property
    def cpu_count(self):
        """Get or set int value for 'CPUCount'
        Number of virtual CPUs in the VM.
        """
        ret = self._get_attr("CPUCount")
        return ret

    @cpu_count.setter
    def cpu_count(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("CPUCount", value)

    @property
    def cpu_hot_plug_enabled(self):
        """Get or set bool value for 'CPUHotPlugEnabled'
        This setting determines whether VirtualBox allows CPU
        hotplugging for this machine.
        """
        ret = self._get_attr("CPUHotPlugEnabled")
        return ret

    @cpu_hot_plug_enabled.setter
    def cpu_hot_plug_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("CPUHotPlugEnabled", value)

    @property
    def cpu_execution_cap(self):
        """Get or set int value for 'CPUExecutionCap'
        Means to limit the number of CPU cycles a guest can use. The unit
        is percentage of host CPU cycles per second. The valid range
        is 1 - 100. 100 (the default) implies no limit.
        """
        ret = self._get_attr("CPUExecutionCap")
        return ret

    @cpu_execution_cap.setter
    def cpu_execution_cap(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("CPUExecutionCap", value)

    @property
    def memory_size(self):
        """Get or set int value for 'memorySize'
        System memory size in megabytes.
        """
        ret = self._get_attr("memorySize")
        return ret

    @memory_size.setter
    def memory_size(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("memorySize", value)

    @property
    def memory_balloon_size(self):
        """Get or set int value for 'memoryBalloonSize'
        Memory balloon size in megabytes.
        """
        ret = self._get_attr("memoryBalloonSize")
        return ret

    @memory_balloon_size.setter
    def memory_balloon_size(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("memoryBalloonSize", value)

    @property
    def page_fusion_enabled(self):
        """Get or set bool value for 'pageFusionEnabled'
        This setting determines whether VirtualBox allows page
        fusion for this machine (64-bit hosts only).
        """
        ret = self._get_attr("pageFusionEnabled")
        return ret

    @page_fusion_enabled.setter
    def page_fusion_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("pageFusionEnabled", value)

    @property
    def graphics_controller_type(self):
        """Get or set GraphicsControllerType value for 'graphicsControllerType'
        Graphics controller type.
        """
        ret = self._get_attr("graphicsControllerType")
        return GraphicsControllerType(ret)

    @graphics_controller_type.setter
    def graphics_controller_type(self, value):
        if not isinstance(value, GraphicsControllerType):
            raise TypeError("value is not an instance of GraphicsControllerType")
        return self._set_attr("graphicsControllerType", value)

    @property
    def vram_size(self):
        """Get or set int value for 'VRAMSize'
        Video memory size in megabytes.
        """
        ret = self._get_attr("VRAMSize")
        return ret

    @vram_size.setter
    def vram_size(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("VRAMSize", value)

    @property
    def accelerate3_d_enabled(self):
        """Get or set bool value for 'accelerate3DEnabled'
        This setting determines whether VirtualBox allows this machine to make
        use of the 3D graphics support available on the host.
        """
        ret = self._get_attr("accelerate3DEnabled")
        return ret

    @accelerate3_d_enabled.setter
    def accelerate3_d_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("accelerate3DEnabled", value)

    @property
    def accelerate2_d_video_enabled(self):
        """Get or set bool value for 'accelerate2DVideoEnabled'
        This setting determines whether VirtualBox allows this machine to make
        use of the 2D video acceleration support available on the host.
        """
        ret = self._get_attr("accelerate2DVideoEnabled")
        return ret

    @accelerate2_d_video_enabled.setter
    def accelerate2_d_video_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("accelerate2DVideoEnabled", value)

    @property
    def monitor_count(self):
        """Get or set int value for 'monitorCount'
        Number of virtual monitors.
        
          Only effective on Windows XP and later guests with
          Guest Additions installed.
        """
        ret = self._get_attr("monitorCount")
        return ret

    @monitor_count.setter
    def monitor_count(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("monitorCount", value)

    @property
    def video_capture_enabled(self):
        """Get or set bool value for 'videoCaptureEnabled'
        This setting determines whether VirtualBox uses video recording to
        record VM session.
        """
        ret = self._get_attr("videoCaptureEnabled")
        return ret

    @video_capture_enabled.setter
    def video_capture_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("videoCaptureEnabled", value)

    @property
    def video_capture_screens(self):
        """Get or set bool value for 'videoCaptureScreens'
        This setting determines for which screens video recording is
        enabled.
        """
        ret = self._get_attr("videoCaptureScreens")
        return ret

    @video_capture_screens.setter
    def video_capture_screens(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("videoCaptureScreens", value)

    @property
    def video_capture_file(self):
        """Get or set str value for 'videoCaptureFile'
        This setting determines the filename VirtualBox uses to save
        the recorded content. This setting cannot be changed while video
        capturing is enabled.
        
          When setting this attribute, the specified path has to be
          absolute (full path). When reading this attribute, a full path is
          always returned.
        """
        ret = self._get_attr("videoCaptureFile")
        return ret

    @video_capture_file.setter
    def video_capture_file(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("videoCaptureFile", value)

    @property
    def video_capture_width(self):
        """Get or set int value for 'videoCaptureWidth'
        This setting determines the horizontal resolution of the recorded
        video. This setting cannot be changed while video capturing is
        enabled.
        """
        ret = self._get_attr("videoCaptureWidth")
        return ret

    @video_capture_width.setter
    def video_capture_width(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("videoCaptureWidth", value)

    @property
    def video_capture_height(self):
        """Get or set int value for 'videoCaptureHeight'
        This setting determines the vertical resolution of the recorded
        video. This setting cannot be changed while video capturing is
        enabled.
        """
        ret = self._get_attr("videoCaptureHeight")
        return ret

    @video_capture_height.setter
    def video_capture_height(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("videoCaptureHeight", value)

    @property
    def video_capture_rate(self):
        """Get or set int value for 'videoCaptureRate'
        This setting determines the bitrate in kilobits per second.
        Increasing this value makes the video look better for the
        cost of an increased file size. This setting cannot be changed
        while video capturing is enabled.
        """
        ret = self._get_attr("videoCaptureRate")
        return ret

    @video_capture_rate.setter
    def video_capture_rate(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("videoCaptureRate", value)

    @property
    def video_capture_fps(self):
        """Get or set int value for 'videoCaptureFPS'
        This setting determines the maximum number of frames per second.
        Frames with a higher frequency will be skipped. Reducing this
        value increases the number of skipped frames and reduces the
        file size. This setting cannot be changed while video capturing
        is enabled.
        """
        ret = self._get_attr("videoCaptureFPS")
        return ret

    @video_capture_fps.setter
    def video_capture_fps(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("videoCaptureFPS", value)

    @property
    def bios_settings(self):
        """Get IBIOSSettings value for 'BIOSSettings'
        Object containing all BIOS settings.
        """
        ret = self._get_attr("BIOSSettings")
        return IBIOSSettings(ret)

    @property
    def firmware_type(self):
        """Get or set FirmwareType value for 'firmwareType'
        Type of firmware (such as legacy BIOS or EFI), used for initial
        bootstrap in this VM.
        """
        ret = self._get_attr("firmwareType")
        return FirmwareType(ret)

    @firmware_type.setter
    def firmware_type(self, value):
        if not isinstance(value, FirmwareType):
            raise TypeError("value is not an instance of FirmwareType")
        return self._set_attr("firmwareType", value)

    @property
    def pointing_hid_type(self):
        """Get or set PointingHIDType value for 'pointingHIDType'
        Type of pointing HID (such as mouse or tablet) used in this VM.
        The default is typically "PS2Mouse" but can vary depending on the
        requirements of the guest operating system.
        """
        ret = self._get_attr("pointingHIDType")
        return PointingHIDType(ret)

    @pointing_hid_type.setter
    def pointing_hid_type(self, value):
        if not isinstance(value, PointingHIDType):
            raise TypeError("value is not an instance of PointingHIDType")
        return self._set_attr("pointingHIDType", value)

    @property
    def keyboard_hid_type(self):
        """Get or set KeyboardHIDType value for 'keyboardHIDType'
        Type of keyboard HID used in this VM.
        The default is typically "PS2Keyboard" but can vary depending on the
        requirements of the guest operating system.
        """
        ret = self._get_attr("keyboardHIDType")
        return KeyboardHIDType(ret)

    @keyboard_hid_type.setter
    def keyboard_hid_type(self, value):
        if not isinstance(value, KeyboardHIDType):
            raise TypeError("value is not an instance of KeyboardHIDType")
        return self._set_attr("keyboardHIDType", value)

    @property
    def hpet_enabled(self):
        """Get or set bool value for 'HPETEnabled'
        This attribute controls if High Precision Event Timer (HPET) is
        enabled in this VM. Use this property if you want to provide guests
        with additional time source, or if guest requires HPET to function correctly.
        Default is false.
        """
        ret = self._get_attr("HPETEnabled")
        return ret

    @hpet_enabled.setter
    def hpet_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("HPETEnabled", value)

    @property
    def chipset_type(self):
        """Get or set ChipsetType value for 'chipsetType'
        Chipset type used in this VM.
        """
        ret = self._get_attr("chipsetType")
        return ChipsetType(ret)

    @chipset_type.setter
    def chipset_type(self, value):
        if not isinstance(value, ChipsetType):
            raise TypeError("value is not an instance of ChipsetType")
        return self._set_attr("chipsetType", value)

    @property
    def snapshot_folder(self):
        """Get or set str value for 'snapshotFolder'
        Full path to the directory used to store snapshot data
        (differencing media and saved state files) of this machine.

        The initial value of this property is
        <<link to="#settingsFilePath">
          path_to_settings_file</link>>/<
        <link to="#id">machine_uuid</link>
        >.

        Currently, it is an error to try to change this property on
        a machine that has snapshots (because this would require to
        move possibly large files to a different location).
        A separate method will be available for this purpose later.

        
          Setting this property to @c null or to an empty string will restore
          the initial value.
        
        
          When setting this property, the specified path can be
          absolute (full path) or relative to the directory where the
          <link to="#settingsFilePath">machine settings file</link>
          is located. When reading this property, a full path is
          always returned.
        
        
          The specified path may not exist, it will be created
          when necessary.
        """
        ret = self._get_attr("snapshotFolder")
        return ret

    @snapshot_folder.setter
    def snapshot_folder(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("snapshotFolder", value)

    @property
    def vrde_server(self):
        """Get IVRDEServer value for 'VRDEServer'
        VirtualBox Remote Desktop Extension (VRDE) server object.
        """
        ret = self._get_attr("VRDEServer")
        return IVRDEServer(ret)

    @property
    def emulated_usb_webcamera_enabled(self):
        """Get or set bool value for 'emulatedUSBWebcameraEnabled'"""
        ret = self._get_attr("emulatedUSBWebcameraEnabled")
        return ret

    @emulated_usb_webcamera_enabled.setter
    def emulated_usb_webcamera_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("emulatedUSBWebcameraEnabled", value)

    @property
    def emulated_usb_card_reader_enabled(self):
        """Get or set bool value for 'emulatedUSBCardReaderEnabled'"""
        ret = self._get_attr("emulatedUSBCardReaderEnabled")
        return ret

    @emulated_usb_card_reader_enabled.setter
    def emulated_usb_card_reader_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("emulatedUSBCardReaderEnabled", value)

    @property
    def medium_attachments(self):
        """Get IMediumAttachment value for 'mediumAttachments'
        Array of media attached to this machine.
        """
        ret = self._get_attr("mediumAttachments")
        return [IMediumAttachment(a) for a in ret]

    @property
    def usb_controller(self):
        """Get IUSBController value for 'USBController'
        Associated USB controller object.

        
          If USB functionality is not available in the given edition of
          VirtualBox, this method will set the result code to @c E_NOTIMPL.
        """
        ret = self._get_attr("USBController")
        return IUSBController(ret)

    @property
    def audio_adapter(self):
        """Get IAudioAdapter value for 'audioAdapter'
        Associated audio adapter, always present.
        """
        ret = self._get_attr("audioAdapter")
        return IAudioAdapter(ret)

    @property
    def storage_controllers(self):
        """Get IStorageController value for 'storageControllers'
        Array of storage controllers attached to this machine.
        """
        ret = self._get_attr("storageControllers")
        return [IStorageController(a) for a in ret]

    @property
    def settings_file_path(self):
        """Get str value for 'settingsFilePath'
        Full name of the file containing machine settings data.
        """
        ret = self._get_attr("settingsFilePath")
        return ret

    @property
    def settings_modified(self):
        """Get bool value for 'settingsModified'
        Whether the settings of this machine have been modified
        (but neither yet saved nor discarded).
        
          Reading this property is only valid on instances returned
          by <link to="ISession::machine"/> and on new machines
          created by <link to="IVirtualBox::createMachine"/> or opened
          by <link to="IVirtualBox::openMachine"/> but not
          yet registered, or on unregistered machines after calling
          <link to="IMachine::unregister"/>. For all other
          cases, the settings can never be modified.
        
        
          For newly created unregistered machines, the value of this
          property is always @c true until <link to="#saveSettings"/>
          is called (no matter if any machine settings have been
          changed after the creation or not). For opened machines
          the value is set to @c false (and then follows to normal rules).
        """
        ret = self._get_attr("settingsModified")
        return ret

    @property
    def session_state(self):
        """Get SessionState value for 'sessionState'
        Current session state for this machine.
        """
        ret = self._get_attr("sessionState")
        return SessionState(ret)

    @property
    def session_type(self):
        """Get str value for 'sessionType'
        Type of the session. If <link to="#sessionState"/> is
        Spawning or Locked, this attribute contains the
        same value as passed to the
        <link to="IMachine::launchVMProcess"/> method in the
        @a type parameter. If the session was used with
        <link to="IMachine::lockMachine"/>, or if
        <link to="#sessionState"/> is SessionClosed, the value of this
        attribute is an empty string.
        """
        ret = self._get_attr("sessionType")
        return ret

    @property
    def session_pid(self):
        """Get int value for 'sessionPID'
        Identifier of the session process. This attribute contains the
        platform-dependent identifier of the process whose session was
        used with <link to="IMachine::lockMachine"/> call. The returned
        value is only valid if <link to="#sessionState"/> is Locked or
        Unlocking by the time this property is read.
        """
        ret = self._get_attr("sessionPID")
        return ret

    @property
    def state(self):
        """Get MachineState value for 'state'
        Current execution state of this machine.
        """
        ret = self._get_attr("state")
        return MachineState(ret)

    @property
    def last_state_change(self):
        """Get int value for 'lastStateChange'
        Time stamp of the last execution state change,
        in milliseconds since 1970-01-01 UTC.
        """
        ret = self._get_attr("lastStateChange")
        return ret

    @property
    def state_file_path(self):
        """Get str value for 'stateFilePath'
        Full path to the file that stores the execution state of
        the machine when it is in the <link to="MachineState_Saved"/> state.
        
          When the machine is not in the Saved state, this attribute is
          an empty string.
        """
        ret = self._get_attr("stateFilePath")
        return ret

    @property
    def log_folder(self):
        """Get str value for 'logFolder'
        Full path to the folder that stores a set of rotated log files
        recorded during machine execution. The most recent log file is
        named VBox.log, the previous log file is
        named VBox.log.1 and so on (up to VBox.log.3
        in the current version).
        """
        ret = self._get_attr("logFolder")
        return ret

    @property
    def current_snapshot(self):
        """Get ISnapshot value for 'currentSnapshot'
        Current snapshot of this machine. This is @c null if the machine
        currently has no snapshots. If it is not @c null, then it was
        set by one of <link to="IConsole::takeSnapshot"/>,
        <link to="IConsole::deleteSnapshot"/>
        or <link to="IConsole::restoreSnapshot"/>, depending on which
        was called last. See <link to="ISnapshot"/> for details.
        """
        ret = self._get_attr("currentSnapshot")
        return ISnapshot(ret)

    @property
    def snapshot_count(self):
        """Get int value for 'snapshotCount'
        Number of snapshots taken on this machine. Zero means the
        machine doesn't have any snapshots.
        """
        ret = self._get_attr("snapshotCount")
        return ret

    @property
    def current_state_modified(self):
        """Get bool value for 'currentStateModified'
        Returns @c true if the current state of the machine is not
        identical to the state stored in the current snapshot.

        The current state is identical to the current snapshot only
        directly after one of the following calls are made:

        
          <link to="IConsole::restoreSnapshot"/>
          
          <link to="IConsole::takeSnapshot"/> (issued on a
            "powered off" or "saved" machine, for which
            <link to="#settingsModified"/> returns @c false)
          
        

        The current state remains identical until one of the following
        happens:
        
          settings of the machine are changed
          the saved state is deleted
          the current snapshot is deleted
          an attempt to execute the machine is made
        

        
          For machines that don't have snapshots, this property is
          always @c false.
        """
        ret = self._get_attr("currentStateModified")
        return ret

    @property
    def shared_folders(self):
        """Get ISharedFolder value for 'sharedFolders'
        Collection of shared folders for this machine (permanent shared
        folders). These folders are shared automatically at machine startup
        and available only to the guest OS installed within this machine.

        New shared folders are added to the collection using
        <link to="#createSharedFolder"/>. Existing shared folders can be
        removed using <link to="#removeSharedFolder"/>.
        """
        ret = self._get_attr("sharedFolders")
        return [ISharedFolder(a) for a in ret]

    @property
    def clipboard_mode(self):
        """Get or set ClipboardMode value for 'clipboardMode'
        Synchronization mode between the host OS clipboard
        and the guest OS clipboard.
        """
        ret = self._get_attr("clipboardMode")
        return ClipboardMode(ret)

    @clipboard_mode.setter
    def clipboard_mode(self, value):
        if not isinstance(value, ClipboardMode):
            raise TypeError("value is not an instance of ClipboardMode")
        return self._set_attr("clipboardMode", value)

    @property
    def drag_and_drop_mode(self):
        """Get or set DragAndDropMode value for 'dragAndDropMode'
        Which mode is allowed for drag'n'drop.
        """
        ret = self._get_attr("dragAndDropMode")
        return DragAndDropMode(ret)

    @drag_and_drop_mode.setter
    def drag_and_drop_mode(self, value):
        if not isinstance(value, DragAndDropMode):
            raise TypeError("value is not an instance of DragAndDropMode")
        return self._set_attr("dragAndDropMode", value)

    @property
    def guest_property_notification_patterns(self):
        """Get or set str value for 'guestPropertyNotificationPatterns'
        A comma-separated list of simple glob patterns. Changes to guest
        properties whose name matches one of the patterns will generate an
        <link to="IGuestPropertyChangedEvent"/> signal.
        """
        ret = self._get_attr("guestPropertyNotificationPatterns")
        return ret

    @guest_property_notification_patterns.setter
    def guest_property_notification_patterns(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("guestPropertyNotificationPatterns", value)

    @property
    def teleporter_enabled(self):
        """Get or set bool value for 'teleporterEnabled'
        When set to @a true, the virtual machine becomes a target teleporter
        the next time it is powered on. This can only set to @a true when the
        VM is in the @a PoweredOff or @a Aborted state.

        <!-- This property is automatically set to @a false when the VM is powered
        on. (bird: This doesn't work yet ) -->
        """
        ret = self._get_attr("teleporterEnabled")
        return ret

    @teleporter_enabled.setter
    def teleporter_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("teleporterEnabled", value)

    @property
    def teleporter_port(self):
        """Get or set int value for 'teleporterPort'
        The TCP port the target teleporter will listen for incoming
        teleportations on.

        0 means the port is automatically selected upon power on. The actual
        value can be read from this property while the machine is waiting for
        incoming teleportations.
        """
        ret = self._get_attr("teleporterPort")
        return ret

    @teleporter_port.setter
    def teleporter_port(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("teleporterPort", value)

    @property
    def teleporter_address(self):
        """Get or set str value for 'teleporterAddress'
        The address the target teleporter will listen on. If set to an empty
        string, it will listen on all addresses.
        """
        ret = self._get_attr("teleporterAddress")
        return ret

    @teleporter_address.setter
    def teleporter_address(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("teleporterAddress", value)

    @property
    def teleporter_password(self):
        """Get or set str value for 'teleporterPassword'
        The password to check for on the target teleporter. This is just a
        very basic measure to prevent simple hacks and operators accidentally
        beaming a virtual machine to the wrong place.

        Note that you SET a plain text password while reading back a HASHED
        password. Setting a hashed password is currently not supported.
        """
        ret = self._get_attr("teleporterPassword")
        return ret

    @teleporter_password.setter
    def teleporter_password(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("teleporterPassword", value)

    @property
    def fault_tolerance_state(self):
        """Get or set FaultToleranceState value for 'faultToleranceState'
        Fault tolerance state; disabled, source or target.
        This property can be changed at any time. If you change it for a running
        VM, then the fault tolerance address and port must be set beforehand.
        """
        ret = self._get_attr("faultToleranceState")
        return FaultToleranceState(ret)

    @fault_tolerance_state.setter
    def fault_tolerance_state(self, value):
        if not isinstance(value, FaultToleranceState):
            raise TypeError("value is not an instance of FaultToleranceState")
        return self._set_attr("faultToleranceState", value)

    @property
    def fault_tolerance_port(self):
        """Get or set int value for 'faultTolerancePort'
        The TCP port the fault tolerance source or target will use for
        communication.
        """
        ret = self._get_attr("faultTolerancePort")
        return ret

    @fault_tolerance_port.setter
    def fault_tolerance_port(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("faultTolerancePort", value)

    @property
    def fault_tolerance_address(self):
        """Get or set str value for 'faultToleranceAddress'
        The address the fault tolerance source or target.
        """
        ret = self._get_attr("faultToleranceAddress")
        return ret

    @fault_tolerance_address.setter
    def fault_tolerance_address(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("faultToleranceAddress", value)

    @property
    def fault_tolerance_password(self):
        """Get or set str value for 'faultTolerancePassword'
        The password to check for on the standby VM. This is just a
        very basic measure to prevent simple hacks and operators accidentally
        choosing the wrong standby VM.
        """
        ret = self._get_attr("faultTolerancePassword")
        return ret

    @fault_tolerance_password.setter
    def fault_tolerance_password(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("faultTolerancePassword", value)

    @property
    def fault_tolerance_sync_interval(self):
        """Get or set int value for 'faultToleranceSyncInterval'
        The interval in ms used for syncing the state between source and target.
        """
        ret = self._get_attr("faultToleranceSyncInterval")
        return ret

    @fault_tolerance_sync_interval.setter
    def fault_tolerance_sync_interval(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("faultToleranceSyncInterval", value)

    @property
    def rtc_use_utc(self):
        """Get or set bool value for 'RTCUseUTC'
        When set to @a true, the RTC device of the virtual machine will run
        in UTC time, otherwise in local time. Especially Unix guests prefer
        the time in UTC.
        """
        ret = self._get_attr("RTCUseUTC")
        return ret

    @rtc_use_utc.setter
    def rtc_use_utc(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("RTCUseUTC", value)

    @property
    def io_cache_enabled(self):
        """Get or set bool value for 'IOCacheEnabled'
        When set to @a true, the builtin I/O cache of the virtual machine
        will be enabled.
        """
        ret = self._get_attr("IOCacheEnabled")
        return ret

    @io_cache_enabled.setter
    def io_cache_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("IOCacheEnabled", value)

    @property
    def io_cache_size(self):
        """Get or set int value for 'IOCacheSize'
        Maximum size of the I/O cache in MB.
        """
        ret = self._get_attr("IOCacheSize")
        return ret

    @io_cache_size.setter
    def io_cache_size(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("IOCacheSize", value)

    @property
    def pci_device_assignments(self):
        """Get IPCIDeviceAttachment value for 'PCIDeviceAssignments'
        Array of PCI devices assigned to this machine, to get list of all
        PCI devices attached to the machine use
        <link to="IConsole::attachedPCIDevices"/> attribute, as this attribute
        is intended to list only devices additional to what described in
        virtual hardware config. Usually, this list keeps host's physical
        devices assigned to the particular machine.
        """
        ret = self._get_attr("PCIDeviceAssignments")
        return [IPCIDeviceAttachment(a) for a in ret]

    @property
    def bandwidth_control(self):
        """Get IBandwidthControl value for 'bandwidthControl'
        Bandwidth control manager.
        """
        ret = self._get_attr("bandwidthControl")
        return IBandwidthControl(ret)

    @property
    def tracing_enabled(self):
        """Get or set bool value for 'tracingEnabled'
        Enables the tracing facility in the VMM (including PDM devices +
        drivers). The VMM will consume about 0.5MB of more memory when
        enabled and there may be some extra overhead from tracepoints that are
        always enabled.
        """
        ret = self._get_attr("tracingEnabled")
        return ret

    @tracing_enabled.setter
    def tracing_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("tracingEnabled", value)

    @property
    def tracing_config(self):
        """Get or set str value for 'tracingConfig'
        Tracepoint configuration to apply at startup when
        <link to="IMachine::tracingEnabled"/> is true. The string specifies
        a space separated of tracepoint group names to enable. The special
        group 'all' enables all tracepoints. Check DBGFR3TracingConfig for
        more details on available tracepoint groups and such.

        Note that on hosts supporting DTrace (or similar), a lot of the
        tracepoints may be implemented exclusivly as DTrace probes. So, the
        effect of the same config may differ between Solaris and Windows for
        example.
        """
        ret = self._get_attr("tracingConfig")
        return ret

    @tracing_config.setter
    def tracing_config(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("tracingConfig", value)

    @property
    def allow_tracing_to_access_vm(self):
        """Get or set bool value for 'allowTracingToAccessVM'
        Enables tracepoints in PDM devices and drivers to use the VMCPU or VM
        structures when firing off trace points. This is especially useful
        with DTrace tracepoints, as it allows you to use the VMCPU or VM
        pointer to obtain useful information such as guest register state.

        This is disabled by default because devices and drivers normally has no
        business accessing the VMCPU or VM structures, and are therefore unable
        to get any pointers to these.
        """
        ret = self._get_attr("allowTracingToAccessVM")
        return ret

    @allow_tracing_to_access_vm.setter
    def allow_tracing_to_access_vm(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("allowTracingToAccessVM", value)

    @property
    def autostart_enabled(self):
        """Get or set bool value for 'autostartEnabled'
        Enables autostart of the VM during system boot.
        """
        ret = self._get_attr("autostartEnabled")
        return ret

    @autostart_enabled.setter
    def autostart_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("autostartEnabled", value)

    @property
    def autostart_delay(self):
        """Get or set int value for 'autostartDelay'
        Number of seconds to wait until the VM should be started during system boot.
        """
        ret = self._get_attr("autostartDelay")
        return ret

    @autostart_delay.setter
    def autostart_delay(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("autostartDelay", value)

    @property
    def autostop_type(self):
        """Get or set AutostopType value for 'autostopType'
        Action type to do when the system is shutting down.
        """
        ret = self._get_attr("autostopType")
        return AutostopType(ret)

    @autostop_type.setter
    def autostop_type(self, value):
        if not isinstance(value, AutostopType):
            raise TypeError("value is not an instance of AutostopType")
        return self._set_attr("autostopType", value)

    @property
    def default_frontend(self):
        """Get or set str value for 'defaultFrontend'
        Selects which VM frontend should be used by default when launching
        this VM through the <link to="IMachine::launchVMProcess"/> method.
        Empty or @c null strings do not define a particular default, it is up
        to <link to="IMachine::launchVMProcess"/> to select one. See the
        description of <link to="IMachine::launchVMProcess"/> for the valid
        frontend types.

        This per-VM setting overrides the default defined by
        <link to="ISystemProperties::defaultFrontend"/> attribute, and is
        overridden by a frontend type passed to
        <link to="IMachine::launchVMProcess"/>.
        """
        ret = self._get_attr("defaultFrontend")
        return ret

    @default_frontend.setter
    def default_frontend(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("defaultFrontend", value)

    def lock_machine(self, session, lock_type):
        """Locks the machine for the given session to enable the caller
        to make changes to the machine or start the VM or control
        VM execution.

        There are two ways to lock a machine for such uses:

        
          If you want to make changes to the machine settings,
            you must obtain an exclusive write lock on the machine
            by setting @a lockType to @c Write.

            This will only succeed if no other process has locked
            the machine to prevent conflicting changes. Only after
            an exclusive write lock has been obtained using this method, one
            can change all VM settings or execute the VM in the process
            space of the session object. (Note that the latter is only of
            interest if you actually want to write a new front-end for
            virtual machines; but this API gets called internally by
            the existing front-ends such as VBoxHeadless and the VirtualBox
            GUI to acquire a write lock on the machine that they are running.)

            On success, write-locking the machine for a session creates
            a second copy of the IMachine object. It is this second object
            upon which changes can be made; in VirtualBox terminology, the
            second copy is "mutable". It is only this second, mutable machine
            object upon which you can call methods that change the
            machine state. After having called this method, you can
            obtain this second, mutable machine object using the
            <link to="ISession::machine"/> attribute.
          
          If you only want to check the machine state or control
            machine execution without actually changing machine
            settings (e.g. to get access to VM statistics or take
            a snapshot or save the machine state), then set the
            @a lockType argument to @c Shared.

            If no other session has obtained a lock, you will obtain an
            exclusive write lock as described above. However, if another
            session has already obtained such a lock, then a link to that
            existing session will be established which allows you
            to control that existing session.

            To find out which type of lock was obtained, you can
            inspect <link to="ISession::type"/>, which will have been
            set to either @c WriteLock or @c Shared.
          
        

        In either case, you can get access to the <link to="IConsole"/>
        object which controls VM execution.

        Also in all of the above cases, one must always call
        <link to="ISession::unlockMachine"/> to release the lock on the machine, or
        the machine's state will eventually be set to "Aborted".

        To change settings on a machine, the following sequence is typically
        performed:

        
          Call this method to obtain an exclusive write lock for the current session.

          Obtain a mutable IMachine object from <link to="ISession::machine"/>.

          Change the settings of the machine by invoking IMachine methods.

          Call <link to="IMachine::saveSettings"/>.

          Release the write lock by calling <link to="ISession::unlockMachine"/>.

        in session of type ISession
            Session object for which the machine will be locked.

        in lock_type of type LockType
            If set to @c Write, then attempt to acquire an exclusive write lock or fail.
          If set to @c Shared, then either acquire an exclusive write lock or establish
          a link to an existing session.

        raises E_UNEXPECTED
            Virtual machine not registered.
        
        raises E_ACCESSDENIED
            Process not started by OpenRemoteSession.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session already open or being opened.
        
        raises VBOX_E_VM_ERROR
            Failed to assign machine to session.
        
        """
        if not isinstance(session, ISession):
            raise TypeError("session can only be an instance of type ISession")
        if not isinstance(lock_type, LockType):
            raise TypeError("lock_type can only be an instance of type LockType")
        self._call("lockMachine",
                     in_p=[session, lock_type])

    def launch_vm_process(self, session, type_p, environment):
        """Spawns a new process that will execute the virtual machine and obtains a shared
        lock on the machine for the calling session.

        If launching the VM succeeds, the new VM process will create its own session
        and write-lock the machine for it, preventing conflicting changes from other
        processes. If the machine is already locked (because it is already running or
        because another session has a write lock), launching the VM process will therefore
        fail. Reversely, future attempts to obtain a write lock will also fail while the
        machine is running.

        The caller's session object remains separate from the session opened by the new
        VM process. It receives its own <link to="IConsole"/> object which can be used
        to control machine execution, but it cannot be used to change all VM settings
        which would be available after a <link to="#lockMachine"/> call.

        The caller must eventually release the session's shared lock by calling
        <link to="ISession::unlockMachine"/> on the local session object once this call
        has returned. However, the session's state (see <link to="ISession::state"/>)
        will not return to "Unlocked" until the remote session has also unlocked
        the machine (i.e. the machine has stopped running).

        Launching a VM process can take some time (a new VM is started in a new process,
        for which memory and other resources need to be set up). Because of this,
        an <link to="IProgress"/> object is returned to allow the caller to wait
        for this asynchronous operation to be completed. Until then, the caller's
        session object remains in the "Unlocked" state, and its <link to="ISession::machine"/>
        and <link to="ISession::console"/> attributes cannot be accessed.
        It is recommended to use <link to="IProgress::waitForCompletion"/> or
        similar calls to wait for completion. Completion is signalled when the VM
        is powered on. If launching the VM fails, error messages can be queried
        via the progress object, if available.

        The progress object will have at least 2 sub-operations. The first
        operation covers the period up to the new VM process calls powerUp.
        The subsequent operations mirror the <link to="IConsole::powerUp"/>
        progress object. Because <link to="IConsole::powerUp"/> may require
        some extra sub-operations, the <link to="IProgress::operationCount"/>
        may change at the completion of operation.

        For details on the teleportation progress operation, see
        <link to="IConsole::powerUp"/>.

        The @a environment argument is a string containing definitions of
        environment variables in the following format:
        
        NAME[=VALUE]\n
        NAME[=VALUE]\n
        ...
        
        where \\n is the new line character. These environment
        variables will be appended to the environment of the VirtualBox server
        process. If an environment variable exists both in the server process
        and in this list, the value from this list takes precedence over the
        server's variable. If the value of the environment variable is
        omitted, this variable will be removed from the resulting environment.
        If the environment string is @c null or empty, the server environment
        is inherited by the started process as is.

        in session of type ISession
            Client session object to which the VM process will be connected (this
          must be in "Unlocked" state).

        in type_p of type str
            Front-end to use for the new VM process. The following are currently supported:
          
            "gui": VirtualBox Qt GUI front-end
            "headless": VBoxHeadless (VRDE Server) front-end
            "sdl": VirtualBox SDL front-end
            "emergencystop": reserved value, used for aborting
              the currently running VM or session owner. In this case the
              @a session parameter may be @c null (if it is non-null it isn't
              used in any way), and the @a progress return value will be always
              @c null. The operation completes immediately.
            "": use the per-VM default frontend if set, otherwise
              the global default defined in the system properties. If neither
              are set, the API will launch a "gui" session, which may
              fail if there is no windowing environment available. See
              <link to="IMachine::defaultFrontend"/> and
              <link to="ISystemProperties::defaultFrontend"/>.

        in environment of type str
            Environment to pass to the VM process.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises E_UNEXPECTED
            Virtual machine not registered.
        
        raises E_INVALIDARG
            Invalid session type @a type.
        
        raises VBOX_E_OBJECT_NOT_FOUND
            No machine matching @a machineId found.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session already open or being opened.
        
        raises VBOX_E_IPRT_ERROR
            Launching process for machine failed.
        
        raises VBOX_E_VM_ERROR
            Failed to assign machine to session.
        
        """
        if not isinstance(session, ISession):
            raise TypeError("session can only be an instance of type ISession")
        if type(type_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(environment) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("launchVMProcess",
                     in_p=[session, type_p, environment])
        progress = IProgress(progress)
        return progress

    def set_boot_order(self, position, device):
        """Puts the given device to the specified position in
        the boot order.

        To indicate that no device is associated with the given position,
        <link to="DeviceType_Null"/> should be used.

        @todo setHardDiskBootOrder(), setNetworkBootOrder()

        in position of type int
            Position in the boot order (@c 1 to the total number of
          devices the machine can boot from, as returned by
          <link to="ISystemProperties::maxBootPosition"/>).

        in device of type DeviceType
            The type of the device used to boot at the given position.

        raises E_INVALIDARG
            Boot @a position out of range.
        
        raises E_NOTIMPL
            Booting from USB @a device currently not supported.
        
        """
        if not isinstance(position, int):
            raise TypeError("position can only be an instance of type int")
        if not isinstance(device, DeviceType):
            raise TypeError("device can only be an instance of type DeviceType")
        self._call("setBootOrder",
                     in_p=[position, device])

    def get_boot_order(self, position):
        """Returns the device type that occupies the specified
        position in the boot order.

        @todo [remove?]
        If the machine can have more than one device of the returned type
        (such as hard disks), then a separate method should be used to
        retrieve the individual device that occupies the given position.

        If here are no devices at the given position, then
        <link to="DeviceType_Null"/> is returned.

        @todo getHardDiskBootOrder(), getNetworkBootOrder()

        in position of type int
            Position in the boot order (@c 1 to the total number of
          devices the machine can boot from, as returned by
          <link to="ISystemProperties::maxBootPosition"/>).

        return device of type DeviceType
            Device at the given position.

        raises E_INVALIDARG
            Boot @a position out of range.
        
        """
        if not isinstance(position, int):
            raise TypeError("position can only be an instance of type int")
        device = self._call("getBootOrder",
                     in_p=[position])
        device = DeviceType(device)
        return device

    def attach_device(self, name, controller_port, device, type_p, medium):
        """Attaches a device and optionally mounts a medium to the given storage
        controller (<link to="IStorageController"/>, identified by @a name),
        at the indicated port and device.

        This method is intended for managing storage devices in general while a
        machine is powered off. It can be used to attach and detach fixed
        and removable media. The following kind of media can be attached
        to a machine:

        
          For fixed and removable media, you can pass in a medium that was
            previously opened using <link to="IVirtualBox::openMedium"/>.
          

          Only for storage devices supporting removable media (such as
            DVDs and floppies), you can also specify a null pointer to
            indicate an empty drive or one of the medium objects listed
            in the <link to="IHost::DVDDrives"/> and <link to="IHost::floppyDrives"/>
            arrays to indicate a host drive.
            For removable devices, you can also use <link to="IMachine::mountMedium"/>
            to change the media while the machine is running.
          
        

        In a VM's default configuration of virtual machines, the secondary
        master of the IDE controller is used for a CD/DVD drive.

        After calling this returns successfully, a new instance of
        <link to="IMediumAttachment"/> will appear in the machine's list of medium
        attachments (see <link to="IMachine::mediumAttachments"/>).

        See <link to="IMedium"/> and <link to="IMediumAttachment"/> for more
        information about attaching media.

        The specified device slot must not have a device attached to it,
        or this method will fail.

        
          You cannot attach a device to a newly created machine until
          this machine's settings are saved to disk using
          <link to="#saveSettings"/>.
        
        
          If the medium is being attached indirectly, a new differencing medium
          will implicitly be created for it and attached instead. If the
          changes made to the machine settings (including this indirect
          attachment) are later cancelled using <link to="#discardSettings"/>,
          this implicitly created differencing medium will implicitly
          be deleted.

        in name of type str
            Name of the storage controller to attach the device to.

        in controller_port of type int
            Port to attach the device to. For an IDE controller, 0 specifies
        the primary controller and 1 specifies the secondary controller.
        For a SCSI controller, this must range from 0 to 15; for a SATA controller,
        from 0 to 29; for an SAS controller, from 0 to 7.

        in device of type int
            Device slot in the given port to attach the device to. This is only
        relevant for IDE controllers, for which 0 specifies the master device and
        1 specifies the slave device. For all other controller types, this must
        be 0.

        in type_p of type DeviceType
            Device type of the attached device. For media opened by
        <link to="IVirtualBox::openMedium"/>, this must match the device type
        specified there.

        in medium of type IMedium
            Medium to mount or @c null for an empty drive.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range, or
          file or UUID not found.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Machine must be registered before media can be attached.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        raises VBOX_E_OBJECT_IN_USE
            A medium is already attached to this or another virtual machine.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(type_p, DeviceType):
            raise TypeError("type_p can only be an instance of type DeviceType")
        if not isinstance(medium, IMedium):
            raise TypeError("medium can only be an instance of type IMedium")
        self._call("attachDevice",
                     in_p=[name, controller_port, device, type_p, medium])

    def attach_device_without_medium(self, name, controller_port, device, type_p):
        """Attaches a device and optionally mounts a medium to the given storage
      controller (<link to="IStorageController"/>, identified by @a name),
      at the indicated port and device.

      This method is intended for managing storage devices in general while a
      machine is powered off. It can be used to attach and detach fixed
      and removable media. The following kind of media can be attached
      to a machine:
      
      
      For fixed and removable media, you can pass in a medium that was
      previously opened using <link to="IVirtualBox::openMedium"/>.
      

      Only for storage devices supporting removable media (such as
      DVDs and floppies) with an empty drive or one of the medium objects listed
      in the <link to="IHost::DVDDrives"/> and <link to="IHost::floppyDrives"/>
      arrays to indicate a host drive.
      For removable devices, you can also use <link to="IMachine::mountMedium"/>
      to change the media while the machine is running.
      
      

      In a VM's default configuration of virtual machines, the secondary
      master of the IDE controller is used for a CD/DVD drive.
      <link to="IMediumAttachment"/> will appear in the machine's list of medium
      attachments (see <link to="IMachine::mediumAttachments"/>).

      See <link to="IMedium"/> and <link to="IMediumAttachment"/> for more
      information about attaching media.

      The specified device slot must not have a device attached to it,
      or this method will fail.
      
      You cannot attach a device to a newly created machine until
      this machine's settings are saved to disk using
      <link to="#saveSettings"/>.
      
      
      If the medium is being attached indirectly, a new differencing medium
      will implicitly be created for it and attached instead. If the
      changes made to the machine settings (including this indirect
      attachment) are later cancelled using <link to="#discardSettings"/>,
      this implicitly created differencing medium will implicitly
      be deleted.

        in name of type str
            Name of the storage controller to attach the device to.

        in controller_port of type int
            Port to attach the device to. For an IDE controller, 0 specifies
      the primary controller and 1 specifies the secondary controller.
      For a SCSI controller, this must range from 0 to 15; for a SATA controller,
      from 0 to 29; for an SAS controller, from 0 to 7.

        in device of type int
            Device slot in the given port to attach the device to. This is only
      relevant for IDE controllers, for which 0 specifies the master device and
      1 specifies the slave device. For all other controller types, this must
      be 0.

        in type_p of type DeviceType
            Device type of the attached device. For media opened by
      <link to="IVirtualBox::openMedium"/>, this must match the device type
      specified there.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range, or
            file or UUID not found.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Machine must be registered before media can be attached.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        raises VBOX_E_OBJECT_IN_USE
            A medium is already attached to this or another virtual machine.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(type_p, DeviceType):
            raise TypeError("type_p can only be an instance of type DeviceType")
        self._call("attachDeviceWithoutMedium",
                     in_p=[name, controller_port, device, type_p])

    def detach_device(self, name, controller_port, device):
        """Detaches the device attached to a device slot of the specified bus.

        Detaching the device from the virtual machine is deferred. This means
        that the medium remains associated with the machine when this method
        returns and gets actually de-associated only after a successful
        <link to="#saveSettings"/> call. See <link to="IMedium"/>
        for more detailed information about attaching media.

        
          You cannot detach a device from a running machine.
        
        
          Detaching differencing media implicitly created by <link to="#attachDevice"/> for the indirect attachment using this
          method will not implicitly delete them. The
          <link to="IMedium::deleteStorage"/> operation should be
          explicitly performed by the caller after the medium is successfully
          detached and the settings are saved with
          <link to="#saveSettings"/>, if it is the desired action.

        in name of type str
            Name of the storage controller to detach the medium from.

        in controller_port of type int
            Port number to detach the medium from.

        in device of type int
            Device slot number to detach the medium from.

        raises VBOX_E_INVALID_VM_STATE
            Attempt to detach medium from a running virtual machine.
        
        raises VBOX_E_OBJECT_NOT_FOUND
            No medium attached to given slot/bus.
        
        raises VBOX_E_NOT_SUPPORTED
            Medium format does not support storage deletion (only for implicitly
          created differencing media, should not happen).
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        self._call("detachDevice",
                     in_p=[name, controller_port, device])

    def passthrough_device(self, name, controller_port, device, passthrough):
        """Sets the passthrough mode of an existing DVD device. Changing the
        setting while the VM is running is forbidden. The setting is only used
        if at VM start the device is configured as a host DVD drive, in all
        other cases it is ignored. The device must already exist; see
        <link to="IMachine::attachDevice"/> for how to attach a new device.

        The @a controllerPort and @a device parameters specify the device slot and
        have have the same meaning as with <link to="IMachine::attachDevice"/>.

        in name of type str
            Name of the storage controller.

        in controller_port of type int
            Storage controller port.

        in device of type int
            Device slot in the given port.

        in passthrough of type bool
            New value for the passthrough setting.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to modify an unregistered virtual machine.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(passthrough, bool):
            raise TypeError("passthrough can only be an instance of type bool")
        self._call("passthroughDevice",
                     in_p=[name, controller_port, device, passthrough])

    def temporary_eject_device(self, name, controller_port, device, temporary_eject):
        """Sets the behavior for guest-triggered medium eject. In some situations
        it is desirable that such ejects update the VM configuration, and in
        others the eject should keep the VM configuration. The device must
        already exist; see <link to="IMachine::attachDevice"/> for how to
        attach a new device.

        The @a controllerPort and @a device parameters specify the device slot and
        have have the same meaning as with <link to="IMachine::attachDevice"/>.

        in name of type str
            Name of the storage controller.

        in controller_port of type int
            Storage controller port.

        in device of type int
            Device slot in the given port.

        in temporary_eject of type bool
            New value for the eject behavior.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to modify an unregistered virtual machine.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(temporary_eject, bool):
            raise TypeError("temporary_eject can only be an instance of type bool")
        self._call("temporaryEjectDevice",
                     in_p=[name, controller_port, device, temporary_eject])

    def non_rotational_device(self, name, controller_port, device, non_rotational):
        """Sets a flag in the device information which indicates that the medium
        is not based on rotational technology, i.e. that the access times are
        more or less independent of the position on the medium. This may or may
        not be supported by a particular drive, and is silently ignored in the
        latter case. At the moment only hard disks (which is a misnomer in this
        context) accept this setting. Changing the setting while the VM is
        running is forbidden. The device must already exist; see
        <link to="IMachine::attachDevice"/> for how to attach a new device.

        The @a controllerPort and @a device parameters specify the device slot and
        have have the same meaning as with <link to="IMachine::attachDevice"/>.

        in name of type str
            Name of the storage controller.

        in controller_port of type int
            Storage controller port.

        in device of type int
            Device slot in the given port.

        in non_rotational of type bool
            New value for the non-rotational device flag.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to modify an unregistered virtual machine.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(non_rotational, bool):
            raise TypeError("non_rotational can only be an instance of type bool")
        self._call("nonRotationalDevice",
                     in_p=[name, controller_port, device, non_rotational])

    def set_auto_discard_for_device(self, name, controller_port, device, discard):
        """Sets a flag in the device information which indicates that the medium
        supports discarding unsused blocks (called trimming for SATA or unmap
        for SCSI devices) .This may or may not be supported by a particular drive,
        and is silently ignored in the latter case. At the moment only hard disks
        (which is a misnomer in this context) accept this setting. Changing the
        setting while the VM is running is forbidden. The device must already
        exist; see <link to="IMachine::attachDevice"/> for how to attach a new
        device.

        The @a controllerPort and @a device parameters specify the device slot and
        have have the same meaning as with <link to="IMachine::attachDevice"/>.

        in name of type str
            Name of the storage controller.

        in controller_port of type int
            Storage controller port.

        in device of type int
            Device slot in the given port.

        in discard of type bool
            New value for the discard device flag.

        raises E_INVALIDARG
            SATA device, SATA port, SCSI port out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to modify an unregistered virtual machine.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(discard, bool):
            raise TypeError("discard can only be an instance of type bool")
        self._call("setAutoDiscardForDevice",
                     in_p=[name, controller_port, device, discard])

    def set_bandwidth_group_for_device(self, name, controller_port, device, bandwidth_group):
        """Sets the bandwidth group of an existing storage device.
        The device must already exist; see <link to="IMachine::attachDevice"/>
        for how to attach a new device.

        The @a controllerPort and @a device parameters specify the device slot and
        have have the same meaning as with <link to="IMachine::attachDevice"/>.

        in name of type str
            Name of the storage controller.

        in controller_port of type int
            Storage controller port.

        in device of type int
            Device slot in the given port.

        in bandwidth_group of type IBandwidthGroup
            New value for the bandwidth group or @c null for no group.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to modify an unregistered virtual machine.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(bandwidth_group, IBandwidthGroup):
            raise TypeError("bandwidth_group can only be an instance of type IBandwidthGroup")
        self._call("setBandwidthGroupForDevice",
                     in_p=[name, controller_port, device, bandwidth_group])

    def set_no_bandwidth_group_for_device(self, name, controller_port, device):
        """Sets no bandwidth group for an existing storage device.
      The device must already exist; see <link to="IMachine::attachDevice"/>
      for how to attach a new device.
      The @a controllerPort and @a device parameters specify the device slot and
      have have the same meaning as with <link to="IMachine::attachDevice"/>.

        in name of type str
            Name of the storage controller.

        in controller_port of type int
            Storage controller port.

        in device of type int
            Device slot in the given port.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to modify an unregistered virtual machine.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        self._call("setNoBandwidthGroupForDevice",
                     in_p=[name, controller_port, device])

    def unmount_medium(self, name, controller_port, device, force):
        """Unmounts any currently mounted medium (<link to="IMedium"/>,
            identified by the given UUID @a id) to the given storage controller
            (<link to="IStorageController"/>, identified by @a name),
            at the indicated port and device. The device must already exist;

            This method is intended only for managing removable media, where the
            device is fixed but media is changeable at runtime (such as DVDs
            and floppies). It cannot be used for fixed media such as hard disks.

            The @a controllerPort and @a device parameters specify the device slot
            and have have the same meaning as with
            <link to="IMachine::attachDevice"/>.

            The specified device slot must have a medium mounted, which will be
            unmounted. If there is no mounted medium it will do nothing.
            See <link to="IMedium"/> for more detailed information about
            attaching/unmounting media.

        in name of type str
            Name of the storage controller to unmount the medium from.

        in controller_port of type int
            Port to unmount the medium from.

        in device of type int
            Device slot in the given port to unmount the medium from.

        in force of type bool
            Allows to force unmount of a medium which is locked by
              the device slot in the given port medium is attached to.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to unmount medium that is not removeable - not dvd or floppy.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        raises VBOX_E_OBJECT_IN_USE
            Medium already attached to this or another virtual machine.
        
        raises VBOX_E_OBJECT_NOT_FOUND
            Medium not attached to specified port, device, controller.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(force, bool):
            raise TypeError("force can only be an instance of type bool")
        self._call("unmountMedium",
                     in_p=[name, controller_port, device, force])

    def mount_medium(self, name, controller_port, device, medium, force):
        """Mounts a medium (<link to="IMedium"/>, identified
        by the given UUID @a id) to the given storage controller
        (<link to="IStorageController"/>, identified by @a name),
        at the indicated port and device. The device must already exist;
        see <link to="IMachine::attachDevice"/> for how to attach a new device.

        This method is intended only for managing removable media, where the
        device is fixed but media is changeable at runtime (such as DVDs
        and floppies). It cannot be used for fixed media such as hard disks.

        The @a controllerPort and @a device parameters specify the device slot and
        have have the same meaning as with <link to="IMachine::attachDevice"/>.

        The specified device slot can have a medium mounted, which will be
        unmounted first. Specifying a zero UUID (or an empty string) for
        @a medium does just an unmount.

        See <link to="IMedium"/> for more detailed information about
        attaching media.

        in name of type str
            Name of the storage controller to attach the medium to.

        in controller_port of type int
            Port to attach the medium to.

        in device of type int
            Device slot in the given port to attach the medium to.

        in medium of type IMedium
            Medium to mount or @c null for an empty drive.

        in force of type bool
            Allows to force unmount/mount of a medium which is locked by
          the device slot in the given port to attach the medium to.

        raises E_INVALIDARG
            SATA device, SATA port, IDE port or IDE slot out of range.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Attempt to attach medium to an unregistered virtual machine.
        
        raises VBOX_E_INVALID_VM_STATE
            Invalid machine state.
        
        raises VBOX_E_OBJECT_IN_USE
            Medium already attached to this or another virtual machine.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        if not isinstance(medium, IMedium):
            raise TypeError("medium can only be an instance of type IMedium")
        if not isinstance(force, bool):
            raise TypeError("force can only be an instance of type bool")
        self._call("mountMedium",
                     in_p=[name, controller_port, device, medium, force])

    def get_medium(self, name, controller_port, device):
        """Returns the virtual medium attached to a device slot of the specified
        bus.

        Note that if the medium was indirectly attached by
        <link to="#mountMedium"/> to the given device slot then this
        method will return not the same object as passed to the
        <link to="#mountMedium"/> call. See <link to="IMedium"/> for
        more detailed information about mounting a medium.

        in name of type str
            Name of the storage controller the medium is attached to.

        in controller_port of type int
            Port to query.

        in device of type int
            Device slot in the given port to query.

        return medium of type IMedium
            Attached medium object.

        raises VBOX_E_OBJECT_NOT_FOUND
            No medium attached to given slot/bus.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        medium = self._call("getMedium",
                     in_p=[name, controller_port, device])
        medium = IMedium(medium)
        return medium

    def get_medium_attachments_of_controller(self, name):
        """Returns an array of medium attachments which are attached to the
        the controller with the given name.

        in name of type str

        return medium_attachments of type IMediumAttachment

        raises VBOX_E_OBJECT_NOT_FOUND
            A storage controller with given name doesn't exist.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        medium_attachments = self._call("getMediumAttachmentsOfController",
                     in_p=[name])
        medium_attachments = [IMediumAttachment(a) for a in medium_attachments]
        return medium_attachments

    def get_medium_attachment(self, name, controller_port, device):
        """Returns a medium attachment which corresponds to the controller with
        the given name, on the given port and device slot.

        in name of type str

        in controller_port of type int

        in device of type int

        return attachment of type IMediumAttachment

        raises VBOX_E_OBJECT_NOT_FOUND
            No attachment exists for the given controller/port/device combination.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(controller_port, int):
            raise TypeError("controller_port can only be an instance of type int")
        if not isinstance(device, int):
            raise TypeError("device can only be an instance of type int")
        attachment = self._call("getMediumAttachment",
                     in_p=[name, controller_port, device])
        attachment = IMediumAttachment(attachment)
        return attachment

    def attach_host_pci_device(self, host_address, desired_guest_address, try_to_unbind):
        """Attaches host PCI device with the given (host) PCI address to the
        PCI bus of the virtual machine. Please note, that this operation
        is two phase, as real attachment will happen when VM will start,
        and most information will be delivered as IHostPCIDevicePlugEvent
        on IVirtualBox event source.

        <link to="IHostPCIDevicePlugEvent"/>

        in host_address of type int
            Address of the host PCI device.

        in desired_guest_address of type int
            Desired position of this device on guest PCI bus.

        in try_to_unbind of type bool
            If VMM shall try to unbind existing drivers from the
        device before attaching it to the guest.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine state is not stopped (PCI hotplug not yet implemented).
        
        raises VBOX_E_PDM_ERROR
            Virtual machine does not have a PCI controller allowing attachment of physical devices.
        
        raises VBOX_E_NOT_SUPPORTED
            Hardware or host OS doesn't allow PCI device passthrought.
        
        """
        if not isinstance(host_address, int):
            raise TypeError("host_address can only be an instance of type int")
        if not isinstance(desired_guest_address, int):
            raise TypeError("desired_guest_address can only be an instance of type int")
        if not isinstance(try_to_unbind, bool):
            raise TypeError("try_to_unbind can only be an instance of type bool")
        self._call("attachHostPCIDevice",
                     in_p=[host_address, desired_guest_address, try_to_unbind])

    def detach_host_pci_device(self, host_address):
        """Detach host PCI device from the virtual machine.
        Also HostPCIDevicePlugEvent on IVirtualBox event source
        will be delivered. As currently we don't support hot device
        unplug, IHostPCIDevicePlugEvent event is delivered immediately.

        <link to="IHostPCIDevicePlugEvent"/>

        in host_address of type int
            Address of the host PCI device.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine state is not stopped (PCI hotplug not yet implemented).
        
        raises VBOX_E_OBJECT_NOT_FOUND
            This host device is not attached to this machine.
        
        raises VBOX_E_PDM_ERROR
            Virtual machine does not have a PCI controller allowing attachment of physical devices.
        
        raises VBOX_E_NOT_SUPPORTED
            Hardware or host OS doesn't allow PCI device passthrought.
        
        """
        if not isinstance(host_address, int):
            raise TypeError("host_address can only be an instance of type int")
        self._call("detachHostPCIDevice",
                     in_p=[host_address])

    def get_network_adapter(self, slot):
        """Returns the network adapter associated with the given slot.
        Slots are numbered sequentially, starting with zero. The total
        number of adapters per machine is defined by the
        <link to="ISystemProperties::getMaxNetworkAdapters"/> property,
        so the maximum slot number is one less than that property's value.

        in slot of type int

        return adapter of type INetworkAdapter

        raises E_INVALIDARG
            Invalid @a slot number.
        
        """
        if not isinstance(slot, int):
            raise TypeError("slot can only be an instance of type int")
        adapter = self._call("getNetworkAdapter",
                     in_p=[slot])
        adapter = INetworkAdapter(adapter)
        return adapter

    def add_storage_controller(self, name, connection_type):
        """Adds a new storage controller (SCSI, SAS or SATA controller) to the
        machine and returns it as an instance of
        <link to="IStorageController"/>.

        @a name identifies the controller for subsequent calls such as
        <link to="#getStorageControllerByName"/>,
        <link to="#getStorageControllerByInstance"/>,
        <link to="#removeStorageController"/>,
        <link to="#attachDevice"/> or <link to="#mountMedium"/>.

        After the controller has been added, you can set its exact
        type by setting the <link to="IStorageController::controllerType"/>.

        in name of type str

        in connection_type of type StorageBus

        return controller of type IStorageController

        raises VBOX_E_OBJECT_IN_USE
            A storage controller with given name exists already.
        
        raises E_INVALIDARG
            Invalid @a controllerType.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(connection_type, StorageBus):
            raise TypeError("connection_type can only be an instance of type StorageBus")
        controller = self._call("addStorageController",
                     in_p=[name, connection_type])
        controller = IStorageController(controller)
        return controller

    def get_storage_controller_by_name(self, name):
        """Returns a storage controller with the given name.

        in name of type str

        return storage_controller of type IStorageController

        raises VBOX_E_OBJECT_NOT_FOUND
            A storage controller with given name doesn't exist.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        storage_controller = self._call("getStorageControllerByName",
                     in_p=[name])
        storage_controller = IStorageController(storage_controller)
        return storage_controller

    def get_storage_controller_by_instance(self, instance):
        """Returns a storage controller with the given instance number.

        in instance of type int

        return storage_controller of type IStorageController

        raises VBOX_E_OBJECT_NOT_FOUND
            A storage controller with given instance number doesn't exist.
        
        """
        if not isinstance(instance, int):
            raise TypeError("instance can only be an instance of type int")
        storage_controller = self._call("getStorageControllerByInstance",
                     in_p=[instance])
        storage_controller = IStorageController(storage_controller)
        return storage_controller

    def remove_storage_controller(self, name):
        """Removes a storage controller from the machine with all devices attached to it.

        in name of type str

        raises VBOX_E_OBJECT_NOT_FOUND
            A storage controller with given name doesn't exist.
        
        raises VBOX_E_NOT_SUPPORTED
            Medium format does not support storage deletion (only for implicitly
          created differencing media, should not happen).
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("removeStorageController",
                     in_p=[name])

    def set_storage_controller_bootable(self, name, bootable):
        """Sets the bootable flag of the storage controller with the given name.

        in name of type str

        in bootable of type bool

        raises VBOX_E_OBJECT_NOT_FOUND
            A storage controller with given name doesn't exist.
        
        raises VBOX_E_OBJECT_IN_USE
            Another storage controller is marked as bootable already.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(bootable, bool):
            raise TypeError("bootable can only be an instance of type bool")
        self._call("setStorageControllerBootable",
                     in_p=[name, bootable])

    def get_serial_port(self, slot):
        """Returns the serial port associated with the given slot.
        Slots are numbered sequentially, starting with zero. The total
        number of serial ports per machine is defined by the
        <link to="ISystemProperties::serialPortCount"/> property,
        so the maximum slot number is one less than that property's value.

        in slot of type int

        return port of type ISerialPort

        raises E_INVALIDARG
            Invalid @a slot number.
        
        """
        if not isinstance(slot, int):
            raise TypeError("slot can only be an instance of type int")
        port = self._call("getSerialPort",
                     in_p=[slot])
        port = ISerialPort(port)
        return port

    def get_parallel_port(self, slot):
        """Returns the parallel port associated with the given slot.
        Slots are numbered sequentially, starting with zero. The total
        number of parallel ports per machine is defined by the
        <link to="ISystemProperties::parallelPortCount"/> property,
        so the maximum slot number is one less than that property's value.

        in slot of type int

        return port of type IParallelPort

        raises E_INVALIDARG
            Invalid @a slot number.
        
        """
        if not isinstance(slot, int):
            raise TypeError("slot can only be an instance of type int")
        port = self._call("getParallelPort",
                     in_p=[slot])
        port = IParallelPort(port)
        return port

    def get_extra_data_keys(self):
        """Returns an array representing the machine-specific extra data keys
            which currently have values defined.

        return keys of type str
            Array of extra data keys.

        """
        keys = self._call("getExtraDataKeys")
        return keys

    def get_extra_data(self, key):
        """Returns associated machine-specific extra data.

        If the requested data @a key does not exist, this function will
        succeed and return an empty string in the @a value argument.

        in key of type str
            Name of the data key to get.

        return value of type str
            Value of the requested data key.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getExtraData",
                     in_p=[key])
        return value

    def set_extra_data(self, key, value):
        """Sets associated machine-specific extra data.

        If you pass @c null or an empty string as a key @a value, the given
        @a key will be deleted.

        
          Before performing the actual data change, this method will ask all
          registered listeners using the
          <link to="IExtraDataCanChangeEvent"/>
          notification for a permission. If one of the listeners refuses the
          new value, the change will not be performed.
        
        
          On success, the
          <link to="IExtraDataChangedEvent"/> notification
          is called to inform all registered listeners about a successful data
          change.
        
        
          This method can be called outside the machine session and therefore
          it's a caller's responsibility to handle possible race conditions
          when several clients change the same key at the same time.

        in key of type str
            Name of the data key to set.

        in value of type str
            Value to assign to the key.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setExtraData",
                     in_p=[key, value])

    def get_cpu_property(self, property_p):
        """Returns the virtual CPU boolean value of the specified property.

        in property_p of type CPUPropertyType
            Property type to query.

        return value of type bool
            Property value.

        raises E_INVALIDARG
            Invalid property.
        
        """
        if not isinstance(property_p, CPUPropertyType):
            raise TypeError("property_p can only be an instance of type CPUPropertyType")
        value = self._call("getCPUProperty",
                     in_p=[property_p])
        return value

    def set_cpu_property(self, property_p, value):
        """Sets the virtual CPU boolean value of the specified property.

        in property_p of type CPUPropertyType
            Property type to query.

        in value of type bool
            Property value.

        raises E_INVALIDARG
            Invalid property.
        
        """
        if not isinstance(property_p, CPUPropertyType):
            raise TypeError("property_p can only be an instance of type CPUPropertyType")
        if not isinstance(value, bool):
            raise TypeError("value can only be an instance of type bool")
        self._call("setCPUProperty",
                     in_p=[property_p, value])

    def get_cpuid_leaf(self, id_p):
        """Returns the virtual CPU cpuid information for the specified leaf.

        Currently supported index values for cpuid:
        Standard CPUID leafs: 0 - 0xA
        Extended CPUID leafs: 0x80000000 - 0x8000000A

        See the Intel and AMD programmer's manuals for detailed information
        about the cpuid instruction and its leafs.

        in id_p of type int
            CPUID leaf index.

        out val_eax of type int
            CPUID leaf value for register eax.

        out val_ebx of type int
            CPUID leaf value for register ebx.

        out val_ecx of type int
            CPUID leaf value for register ecx.

        out val_edx of type int
            CPUID leaf value for register edx.

        raises E_INVALIDARG
            Invalid id.
        
        """
        if not isinstance(id_p, int):
            raise TypeError("id_p can only be an instance of type int")
        (val_eax, val_ebx, val_ecx, val_edx) = self._call("getCPUIDLeaf",
                     in_p=[id_p])
        return (val_eax, val_ebx, val_ecx, val_edx)

    def set_cpuid_leaf(self, id_p, val_eax, val_ebx, val_ecx, val_edx):
        """Sets the virtual CPU cpuid information for the specified leaf. Note that these values
        are not passed unmodified. VirtualBox clears features that it doesn't support.

        Currently supported index values for cpuid:
        Standard CPUID leafs: 0 - 0xA
        Extended CPUID leafs: 0x80000000 - 0x8000000A

        See the Intel and AMD programmer's manuals for detailed information
        about the cpuid instruction and its leafs.

        Do not use this method unless you know exactly what you're doing. Misuse can lead to
        random crashes inside VMs.

        in id_p of type int
            CPUID leaf index.

        in val_eax of type int
            CPUID leaf value for register eax.

        in val_ebx of type int
            CPUID leaf value for register ebx.

        in val_ecx of type int
            CPUID leaf value for register ecx.

        in val_edx of type int
            CPUID leaf value for register edx.

        raises E_INVALIDARG
            Invalid id.
        
        """
        if not isinstance(id_p, int):
            raise TypeError("id_p can only be an instance of type int")
        if not isinstance(val_eax, int):
            raise TypeError("val_eax can only be an instance of type int")
        if not isinstance(val_ebx, int):
            raise TypeError("val_ebx can only be an instance of type int")
        if not isinstance(val_ecx, int):
            raise TypeError("val_ecx can only be an instance of type int")
        if not isinstance(val_edx, int):
            raise TypeError("val_edx can only be an instance of type int")
        self._call("setCPUIDLeaf",
                     in_p=[id_p, val_eax, val_ebx, val_ecx, val_edx])

    def remove_cpuid_leaf(self, id_p):
        """Removes the virtual CPU cpuid leaf for the specified index

        in id_p of type int
            CPUID leaf index.

        raises E_INVALIDARG
            Invalid id.
        
        """
        if not isinstance(id_p, int):
            raise TypeError("id_p can only be an instance of type int")
        self._call("removeCPUIDLeaf",
                     in_p=[id_p])

    def remove_all_cpuid_leaves(self):
        """Removes all the virtual CPU cpuid leaves

        """
        self._call("removeAllCPUIDLeaves")

    def get_hw_virt_ex_property(self, property_p):
        """Returns the value of the specified hardware virtualization boolean property.

        in property_p of type HWVirtExPropertyType
            Property type to query.

        return value of type bool
            Property value.

        raises E_INVALIDARG
            Invalid property.
        
        """
        if not isinstance(property_p, HWVirtExPropertyType):
            raise TypeError("property_p can only be an instance of type HWVirtExPropertyType")
        value = self._call("getHWVirtExProperty",
                     in_p=[property_p])
        return value

    def set_hw_virt_ex_property(self, property_p, value):
        """Sets a new value for the specified hardware virtualization boolean property.

        in property_p of type HWVirtExPropertyType
            Property type to set.

        in value of type bool
            New property value.

        raises E_INVALIDARG
            Invalid property.
        
        """
        if not isinstance(property_p, HWVirtExPropertyType):
            raise TypeError("property_p can only be an instance of type HWVirtExPropertyType")
        if not isinstance(value, bool):
            raise TypeError("value can only be an instance of type bool")
        self._call("setHWVirtExProperty",
                     in_p=[property_p, value])

    def save_settings(self):
        """Saves any changes to machine settings made since the session
        has been opened or a new machine has been created, or since the
        last call to <link to="#saveSettings"/> or <link to="#discardSettings"/>.
        For registered machines, new settings become visible to all
        other VirtualBox clients after successful invocation of this
        method.
        
          The method sends <link to="IMachineDataChangedEvent"/>
          notification event after the configuration has been successfully
          saved (only for registered machines).
        
        
          Calling this method is only valid on instances returned
          by <link to="ISession::machine"/> and on new machines
          created by <link to="IVirtualBox::createMachine"/> but not
          yet registered, or on unregistered machines after calling
          <link to="IMachine::unregister"/>.

        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        raises E_ACCESSDENIED
            Modification request refused.
        
        """
        self._call("saveSettings")

    def discard_settings(self):
        """Discards any changes to the machine settings made since the session
        has been opened or since the last call to <link to="#saveSettings"/>
        or <link to="#discardSettings"/>.
        
          Calling this method is only valid on instances returned
          by <link to="ISession::machine"/> and on new machines
          created by <link to="IVirtualBox::createMachine"/> or
          opened by <link to="IVirtualBox::openMachine"/> but not
          yet registered, or on unregistered machines after calling
          <link to="IMachine::unregister"/>.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is not mutable.
        
        """
        self._call("discardSettings")

    def unregister(self, cleanup_mode):
        """Unregisters a machine previously registered with
        <link to="IVirtualBox::registerMachine"/> and optionally do additional
        cleanup before the machine is unregistered.

        This method does not delete any files. It only changes the machine configuration and
        the list of registered machines in the VirtualBox object. To delete the files which
        belonged to the machine, including the XML file of the machine itself, call
        <link to="#deleteConfig"/>, optionally with the array of IMedium objects which was returned
        from this method.

        How thoroughly this method cleans up the machine configuration before unregistering
        the machine depends on the @a cleanupMode argument.

        
          With "UnregisterOnly", the machine will only be unregistered, but no additional
            cleanup will be performed. The call will fail if the machine is in "Saved" state
            or has any snapshots or any media attached (see <link to="IMediumAttachment"/>).
            It is the responsibility of the caller to delete all such configuration in this mode.
            In this mode, the API behaves like the former @c IVirtualBox::unregisterMachine() API
            which it replaces.
          With "DetachAllReturnNone", the call will succeed even if the machine is in "Saved"
            state or if it has snapshots or media attached. All media attached to the current machine
            state or in snapshots will be detached. No medium objects will be returned;
            all of the machine's media will remain open.
          With "DetachAllReturnHardDisksOnly", the call will behave like with "DetachAllReturnNone",
            except that all the hard disk medium objects which were detached from the machine will
            be returned as an array. This allows for quickly passing them to the <link to="#deleteConfig"/>
            API for closing and deletion.
          With "Full", the call will behave like with "DetachAllReturnHardDisksOnly", except
            that all media will be returned in the array, including removable media like DVDs and
            floppies. This might be useful if the user wants to inspect in detail which media were
            attached to the machine. Be careful when passing the media array to <link to="#deleteConfig"/>
            in that case because users will typically want to preserve ISO and RAW image files.
        

        A typical implementation will use "DetachAllReturnHardDisksOnly" and then pass the
        resulting IMedium array to <link to="#deleteConfig"/>. This way, the machine is completely
        deleted with all its saved states and hard disk images, but images for removable
        drives (such as ISO and RAW files) will remain on disk.

        This API does not verify whether the media files returned in the array are still
        attached to other machines (i.e. shared between several machines). If such a shared
        image is passed to <link to="#deleteConfig"/> however, closing the image will fail there
        and the image will be silently skipped.

        This API may, however, move media from this machine's media registry to other media
        registries (see <link to="IMedium"/> for details on media registries). For machines
        created with VirtualBox 4.0 or later, if media from this machine's media registry
        are also attached to another machine (shared attachments), each such medium will be
        moved to another machine's registry. This is because without this machine's media
        registry, the other machine cannot find its media any more and would become inaccessible.

        This API implicitly calls <link to="#saveSettings"/> to save all current machine settings
        before unregistering it. It may also silently call <link to="#saveSettings"/> on other machines
        if media are moved to other machines' media registries.

        After successful method invocation, the <link to="IMachineRegisteredEvent"/> event
        is fired.

        The call will fail if the machine is currently locked (see <link to="ISession"/>).

        
          If the given machine is inaccessible (see <link to="#accessible"/>), it
          will be unregistered and fully uninitialized right afterwards. As a result,
          the returned machine object will be unusable and an attempt to call
          any method will return the "Object not ready" error.

        in cleanup_mode of type CleanupMode
            How to clean up after the machine has been unregistered.

        return media of type IMedium
            List of media detached from the machine, depending on the @a cleanupMode parameter.

        raises VBOX_E_INVALID_OBJECT_STATE
            Machine is currently locked for a session.
        
        """
        if not isinstance(cleanup_mode, CleanupMode):
            raise TypeError("cleanup_mode can only be an instance of type CleanupMode")
        media = self._call("unregister",
                     in_p=[cleanup_mode])
        media = [IMedium(a) for a in media]
        return media

    def delete_config(self, media):
        """Deletes the files associated with this machine from disk. If medium objects are passed
        in with the @a aMedia argument, they are closed and, if closing was successful, their
        storage files are deleted as well. For convenience, this array of media files can be
        the same as the one returned from a previous <link to="#unregister"/> call.

        This method must only be called on machines which are either write-locked (i.e. on instances
        returned by <link to="ISession::machine"/>) or on unregistered machines (i.e. not yet
        registered machines created by <link to="IVirtualBox::createMachine"/> or opened by
        <link to="IVirtualBox::openMachine"/>, or after having called <link to="#unregister"/>).

        The following files will be deleted by this method:
        
          If <link to="#unregister"/> had been previously called with a @a cleanupMode
            argument other than "UnregisterOnly", this will delete all saved state files that
            the machine had in use; possibly one if the machine was in "Saved" state and one
            for each online snapshot that the machine had.
          On each medium object passed in the @a aMedia array, this will call
            <link to="IMedium::close"/>. If that succeeds, this will attempt to delete the
            medium's storage on disk. Since the <link to="IMedium::close"/> call will fail if the medium is still
            in use, e.g. because it is still attached to a second machine; in that case the
            storage will not be deleted.
          Finally, the machine's own XML file will be deleted.
        

        Since deleting large disk image files can be a time-consuming I/O operation, this
        method operates asynchronously and returns an IProgress object to allow the caller
        to monitor the progress. There will be one sub-operation for each file that is
        being deleted (saved state or medium storage file).

        
          <link to="#settingsModified"/> will return @c true after this
          method successfully returns.

        in media of type IMedium
            List of media to be closed and whose storage files will be deleted.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Machine is registered but not write-locked.
        
        raises VBOX_E_IPRT_ERROR
            Could not delete the settings file.
        
        """
        if not isinstance(media, list):
            raise TypeError("media can only be an instance of type list")
        for a in media[:10]:
            if not isinstance(a, IMedium):
                raise TypeError(\
                        "array can only contain objects of type IMedium")
        progress = self._call("deleteConfig",
                     in_p=[media])
        progress = IProgress(progress)
        return progress

    def export_to(self, appliance, location):
        """Exports the machine to an OVF appliance. See <link to="IAppliance"/> for the
            steps required to export VirtualBox machines to OVF.

        in appliance of type IAppliance
            Appliance to export this machine to.

        in location of type str
            The target location.

        return description of type IVirtualSystemDescription
            VirtualSystemDescription object which is created for this machine.

        """
        if not isinstance(appliance, IAppliance):
            raise TypeError("appliance can only be an instance of type IAppliance")
        if type(location) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        description = self._call("exportTo",
                     in_p=[appliance, location])
        description = IVirtualSystemDescription(description)
        return description

    def find_snapshot(self, name_or_id):
        """Returns a snapshot of this machine with the given name or UUID.

        Returns a snapshot of this machine with the given UUID.
        A @c null argument can be used to obtain the first snapshot
        taken on this machine. To traverse the whole tree of snapshots
        starting from the root, inspect the root snapshot's
        <link to="ISnapshot::children"/> attribute and recurse over those children.

        in name_or_id of type str
            What to search for. Name or UUID of the snapshot to find

        return snapshot of type ISnapshot
            Snapshot object with the given name.

        raises VBOX_E_OBJECT_NOT_FOUND
            Virtual machine has no snapshots or snapshot not found.
        
        """
        if type(name_or_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        snapshot = self._call("findSnapshot",
                     in_p=[name_or_id])
        snapshot = ISnapshot(snapshot)
        return snapshot

    def create_shared_folder(self, name, host_path, writable, automount):
        """Creates a new permanent shared folder by associating the given logical
        name with the given host path, adds it to the collection of shared
        folders and starts sharing it. Refer to the description of
        <link to="ISharedFolder"/> to read more about logical names.

        in name of type str
            Unique logical name of the shared folder.

        in host_path of type str
            Full path to the shared folder in the host file system.

        in writable of type bool
            Whether the share is writable or readonly.

        in automount of type bool
            Whether the share gets automatically mounted by the guest
          or not.

        raises VBOX_E_OBJECT_IN_USE
            Shared folder already exists.
        
        raises VBOX_E_FILE_ERROR
            Shared folder @a hostPath not accessible.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(host_path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(writable, bool):
            raise TypeError("writable can only be an instance of type bool")
        if not isinstance(automount, bool):
            raise TypeError("automount can only be an instance of type bool")
        self._call("createSharedFolder",
                     in_p=[name, host_path, writable, automount])

    def remove_shared_folder(self, name):
        """Removes the permanent shared folder with the given name previously
        created by <link to="#createSharedFolder"/> from the collection of
        shared folders and stops sharing it.

        in name of type str
            Logical name of the shared folder to remove.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is not mutable.
        
        raises VBOX_E_OBJECT_NOT_FOUND
            Shared folder @a name does not exist.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("removeSharedFolder",
                     in_p=[name])

    def can_show_console_window(self):
        """Returns @c true if the VM console process can activate the
        console window and bring it to foreground on the desktop of
        the host PC.
        
          This method will fail if a session for this machine is not
          currently open.

        return can_show of type bool
            @c true if the console window can be shown and @c false otherwise.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        """
        can_show = self._call("canShowConsoleWindow")
        return can_show

    def show_console_window(self):
        """Activates the console window and brings it to foreground on
        the desktop of the host PC. Many modern window managers on
        many platforms implement some sort of focus stealing
        prevention logic, so that it may be impossible to activate
        a window without the help of the currently active
        application. In this case, this method will return a non-zero
        identifier that represents the top-level window of the VM
        console process. The caller, if it represents a currently
        active process, is responsible to use this identifier (in a
        platform-dependent manner) to perform actual window
        activation.
        
          This method will fail if a session for this machine is not
          currently open.

        return win_id of type int
            Platform-dependent identifier of the top-level VM console
          window, or zero if this method has performed all actions
          necessary to implement the show window semantics for
          the given platform and/or VirtualBox front-end.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        """
        win_id = self._call("showConsoleWindow")
        return win_id

    def get_guest_property(self, name):
        """Reads an entry from the machine's guest property store.

        in name of type str
            The name of the property to read.

        out value of type str
            The value of the property. If the property does not exist then this
          will be empty.

        out timestamp of type int
            The time at which the property was last modified, as seen by the
          server process.

        out flags of type str
            Additional property parameters, passed as a comma-separated list of
          "name=value" type entries.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        (value, timestamp, flags) = self._call("getGuestProperty",
                     in_p=[name])
        return (value, timestamp, flags)

    def get_guest_property_value(self, property_p):
        """Reads a value from the machine's guest property store.

        in property_p of type str
            The name of the property to read.

        return value of type str
            The value of the property. If the property does not exist then this
          will be empty.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        """
        if type(property_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getGuestPropertyValue",
                     in_p=[property_p])
        return value

    def get_guest_property_timestamp(self, property_p):
        """Reads a property timestamp from the machine's guest property store.

        in property_p of type str
            The name of the property to read.

        return value of type int
            The timestamp. If the property does not exist then this will be
          empty.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        """
        if type(property_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getGuestPropertyTimestamp",
                     in_p=[property_p])
        return value

    def set_guest_property(self, property_p, value, flags):
        """Sets, changes or deletes an entry in the machine's guest property
        store.

        in property_p of type str
            The name of the property to set, change or delete.

        in value of type str
            The new value of the property to set, change or delete. If the
          property does not yet exist and value is non-empty, it will be
          created. If the value is @c null or empty, the property will be
          deleted if it exists.

        in flags of type str
            Additional property parameters, passed as a comma-separated list of
          "name=value" type entries.

        raises E_ACCESSDENIED
            Property cannot be changed.
        
        raises E_INVALIDARG
            Invalid @a flags.
        
        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is not mutable or session not open.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Cannot set transient property when machine not running.
        
        """
        if type(property_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(flags) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setGuestProperty",
                     in_p=[property_p, value, flags])

    def set_guest_property_value(self, property_p, value):
        """Sets or changes a value in the machine's guest property
        store. The flags field will be left unchanged or created empty for a
        new property.

        in property_p of type str
            The name of the property to set or change.

        in value of type str
            The new value of the property to set or change. If the
          property does not yet exist and value is non-empty, it will be
          created.

        raises E_ACCESSDENIED
            Property cannot be changed.
        
        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is not mutable or session not open.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Cannot set transient property when machine not running.
        
        """
        if type(property_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setGuestPropertyValue",
                     in_p=[property_p, value])

    def delete_guest_property(self, name):
        """Deletes an entry from the machine's guest property store.

        in name of type str
            The name of the property to delete.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("deleteGuestProperty",
                     in_p=[name])

    def enumerate_guest_properties(self, patterns):
        """Return a list of the guest properties matching a set of patterns along
        with their values, time stamps and flags.

        in patterns of type str
            The patterns to match the properties against, separated by '|'
          characters. If this is empty or @c null, all properties will match.

        out names of type str
            The names of the properties returned.

        out values of type str
            The values of the properties returned. The array entries match the
          corresponding entries in the @a name array.

        out timestamps of type int
            The time stamps of the properties returned. The array entries match
          the corresponding entries in the @a name array.

        out flags of type str
            The flags of the properties returned. The array entries match the
          corresponding entries in the @a name array.

        """
        if type(patterns) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        (names, values, timestamps, flags) = self._call("enumerateGuestProperties",
                     in_p=[patterns])
        return (names, values, timestamps, flags)

    def query_saved_guest_screen_info(self, screen_id):
        """Returns the guest dimensions from the saved state.

        in screen_id of type int
            Saved guest screen to query info from.

        out origin_x of type int
            The X position of the guest monitor top left corner.

        out origin_y of type int
            The Y position of the guest monitor top left corner.

        out width of type int
            Guest width at the time of the saved state was taken.

        out height of type int
            Guest height at the time of the saved state was taken.

        out enabled of type bool
            Whether the monitor is enabled in the guest.

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (origin_x, origin_y, width, height, enabled) = self._call("querySavedGuestScreenInfo",
                     in_p=[screen_id])
        return (origin_x, origin_y, width, height, enabled)

    def query_saved_thumbnail_size(self, screen_id):
        """Returns size in bytes and dimensions in pixels of a saved thumbnail bitmap from saved state.

        in screen_id of type int
            Saved guest screen to query info from.

        out size of type int
            Size of buffer required to store the bitmap.

        out width of type int
            Bitmap width.

        out height of type int
            Bitmap height.

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (size, width, height) = self._call("querySavedThumbnailSize",
                     in_p=[screen_id])
        return (size, width, height)

    def read_saved_thumbnail_to_array(self, screen_id, bgr):
        """Thumbnail is retrieved to an array of bytes in uncompressed 32-bit BGRA or RGBA format.

        in screen_id of type int
            Saved guest screen to read from.

        in bgr of type bool
            How to order bytes in the pixel. A pixel consists of 4 bytes. If this parameter is true, then
          bytes order is: B, G, R, 0xFF. If this parameter is false, then bytes order is: R, G, B, 0xFF.

        out width of type int
            Bitmap width.

        out height of type int
            Bitmap height.

        return data of type str
            Array with resulting bitmap data.

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(bgr, bool):
            raise TypeError("bgr can only be an instance of type bool")
        (width, height, data) = self._call("readSavedThumbnailToArray",
                     in_p=[screen_id, bgr])
        return (width, height, data)

    def read_saved_thumbnail_png_to_array(self, screen_id):
        """Thumbnail in PNG format is retrieved to an array of bytes.

        in screen_id of type int
            Saved guest screen to read from.

        out width of type int
            Image width.

        out height of type int
            Image height.

        return data of type str
            Array with resulting PNG data.

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (width, height, data) = self._call("readSavedThumbnailPNGToArray",
                     in_p=[screen_id])
        return (width, height, data)

    def query_saved_screenshot_png_size(self, screen_id):
        """Returns size in bytes and dimensions of a saved PNG image of screenshot from saved state.

        in screen_id of type int
            Saved guest screen to query info from.

        out size of type int
            Size of buffer required to store the PNG binary data.

        out width of type int
            Image width.

        out height of type int
            Image height.

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (size, width, height) = self._call("querySavedScreenshotPNGSize",
                     in_p=[screen_id])
        return (size, width, height)

    def read_saved_screenshot_png_to_array(self, screen_id):
        """Screenshot in PNG format is retrieved to an array of bytes.

        in screen_id of type int
            Saved guest screen to read from.

        out width of type int
            Image width.

        out height of type int
            Image height.

        return data of type str
            Array with resulting PNG data.

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (width, height, data) = self._call("readSavedScreenshotPNGToArray",
                     in_p=[screen_id])
        return (width, height, data)

    def hot_plug_cpu(self, cpu):
        """Plugs a CPU into the machine.

        in cpu of type int
            The CPU id to insert.

        """
        if not isinstance(cpu, int):
            raise TypeError("cpu can only be an instance of type int")
        self._call("hotPlugCPU",
                     in_p=[cpu])

    def hot_unplug_cpu(self, cpu):
        """Removes a CPU from the machine.

        in cpu of type int
            The CPU id to remove.

        """
        if not isinstance(cpu, int):
            raise TypeError("cpu can only be an instance of type int")
        self._call("hotUnplugCPU",
                     in_p=[cpu])

    def get_cpu_status(self, cpu):
        """Returns the current status of the given CPU.

        in cpu of type int
            The CPU id to check for.

        return attached of type bool
            Status of the CPU.

        """
        if not isinstance(cpu, int):
            raise TypeError("cpu can only be an instance of type int")
        attached = self._call("getCPUStatus",
                     in_p=[cpu])
        return attached

    def query_log_filename(self, idx):
        """Queries for the VM log file name of an given index. Returns an empty
        string if a log file with that index doesn't exists.

        in idx of type int
            Which log file name to query. 0=current log file.

        return filename of type str
            On return the full path to the log file or an empty string on error.

        """
        if not isinstance(idx, int):
            raise TypeError("idx can only be an instance of type int")
        filename = self._call("queryLogFilename",
                     in_p=[idx])
        return filename

    def read_log(self, idx, offset, size):
        """Reads the VM log file. The chunk size is limited, so even if you
        ask for a big piece there might be less data returned.

        in idx of type int
            Which log file to read. 0=current log file.

        in offset of type int
            Offset in the log file.

        in size of type int
            Chunk size to read in the log file.

        return data of type str
            Data read from the log file. A data size of 0 means end of file
          if the requested chunk size was not 0. This is the unprocessed
          file data, i.e. the line ending style depends on the platform of
          the system the server is running on.

        """
        if not isinstance(idx, int):
            raise TypeError("idx can only be an instance of type int")
        if not isinstance(offset, int):
            raise TypeError("offset can only be an instance of type int")
        if not isinstance(size, int):
            raise TypeError("size can only be an instance of type int")
        data = self._call("readLog",
                     in_p=[idx, offset, size])
        return data

    def clone_to(self, target, mode, options):
        """Creates a clone of this machine, either as a full clone (which means
        creating independent copies of the hard disk media, save states and so
        on), or as a linked clone (which uses its own differencing media,
        sharing the parent media with the source machine).

        The target machine object must have been created previously with <link to="IVirtualBox::createMachine"/>, and all the settings will be
        transferred except the VM name and the hardware UUID. You can set the
        VM name and the new hardware UUID when creating the target machine. The
        network MAC addresses are newly created for all newtwork adapters. You
        can change that behaviour with the options parameter. The operation is
        performed asynchronously, so the machine object will be not be usable
        until the @a progress object signals completion.

        in target of type IMachine
            Target machine object.

        in mode of type CloneMode
            Which states should be cloned.

        in options of type CloneOptions
            Options for the cloning operation.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises E_INVALIDARG
            @a target is @c null.
        
        """
        if not isinstance(target, IMachine):
            raise TypeError("target can only be an instance of type IMachine")
        if not isinstance(mode, CloneMode):
            raise TypeError("mode can only be an instance of type CloneMode")
        if not isinstance(options, list):
            raise TypeError("options can only be an instance of type list")
        for a in options[:10]:
            if not isinstance(a, CloneOptions):
                raise TypeError(\
                        "array can only contain objects of type CloneOptions")
        progress = self._call("cloneTo",
                     in_p=[target, mode, options])
        progress = IProgress(progress)
        return progress


class IVRDEServerInfo(Interface):
    """
    Contains information about the remote desktop (VRDE) server capabilities and status.
      This is used in the <link to="IConsole::VRDEServerInfo"/> attribute.
    """
    __uuid__ = '714434a1-58c3-4aab-9049-7652c5df113b'
    __wsmap__ = 'struct'
    
    @property
    def active(self):
        """Get bool value for 'active'
        Whether the remote desktop connection is active.
        """
        ret = self._get_attr("active")
        return ret

    @property
    def port(self):
        """Get int value for 'port'
        VRDE server port number. If this property is equal to 0, then
        the VRDE server failed to start, usually because there are no free IP
        ports to bind to. If this property is equal to -1, then the VRDE
        server has not yet been started.
        """
        ret = self._get_attr("port")
        return ret

    @property
    def number_of_clients(self):
        """Get int value for 'numberOfClients'
        How many times a client connected.
        """
        ret = self._get_attr("numberOfClients")
        return ret

    @property
    def begin_time(self):
        """Get int value for 'beginTime'
        When the last connection was established, in milliseconds since 1970-01-01 UTC.
        """
        ret = self._get_attr("beginTime")
        return ret

    @property
    def end_time(self):
        """Get int value for 'endTime'
        When the last connection was terminated or the current time, if
        connection is still active, in milliseconds since 1970-01-01 UTC.
        """
        ret = self._get_attr("endTime")
        return ret

    @property
    def bytes_sent(self):
        """Get int value for 'bytesSent'
        How many bytes were sent in last or current, if still active, connection.
        """
        ret = self._get_attr("bytesSent")
        return ret

    @property
    def bytes_sent_total(self):
        """Get int value for 'bytesSentTotal'
        How many bytes were sent in all connections.
        """
        ret = self._get_attr("bytesSentTotal")
        return ret

    @property
    def bytes_received(self):
        """Get int value for 'bytesReceived'
        How many bytes were received in last or current, if still active, connection.
        """
        ret = self._get_attr("bytesReceived")
        return ret

    @property
    def bytes_received_total(self):
        """Get int value for 'bytesReceivedTotal'
        How many bytes were received in all connections.
        """
        ret = self._get_attr("bytesReceivedTotal")
        return ret

    @property
    def user(self):
        """Get str value for 'user'
        Login user name supplied by the client.
        """
        ret = self._get_attr("user")
        return ret

    @property
    def domain(self):
        """Get str value for 'domain'
        Login domain name supplied by the client.
        """
        ret = self._get_attr("domain")
        return ret

    @property
    def client_name(self):
        """Get str value for 'clientName'
        The client name supplied by the client.
        """
        ret = self._get_attr("clientName")
        return ret

    @property
    def client_ip(self):
        """Get str value for 'clientIP'
        The IP address of the client.
        """
        ret = self._get_attr("clientIP")
        return ret

    @property
    def client_version(self):
        """Get int value for 'clientVersion'
        The client software version number.
        """
        ret = self._get_attr("clientVersion")
        return ret

    @property
    def encryption_style(self):
        """Get int value for 'encryptionStyle'
        Public key exchange method used when connection was established.
        Values: 0 - RDP4 public key exchange scheme.
        1 - X509 certificates were sent to client.
        """
        ret = self._get_attr("encryptionStyle")
        return ret


class IConsole(Interface):
    """
    The IConsole interface represents an interface to control virtual
      machine execution.

      A console object gets created when a machine has been locked for a
      particular session (client process) using <link to="IMachine::lockMachine"/>
      or <link to="IMachine::launchVMProcess"/>. The console object can
      then be found in the session's <link to="ISession::console"/> attribute.

      Methods of the IConsole interface allow the caller to query the current
      virtual machine execution state, pause the machine or power it down, save
      the machine state or take a snapshot, attach and detach removable media
      and so on.

      <link to="ISession"/>
    """
    __uuid__ = 'db7ab4ca-2a3f-4183-9243-c1208da92392'
    __wsmap__ = 'managed'
    
    @property
    def machine(self):
        """Get IMachine value for 'machine'
        Machine object for this console session.
        
          This is a convenience property, it has the same value as
          <link to="ISession::machine"/> of the corresponding session
          object.
        """
        ret = self._get_attr("machine")
        return IMachine(ret)

    @property
    def state(self):
        """Get MachineState value for 'state'
        Current execution state of the machine.
        
          This property always returns the same value as the corresponding
          property of the IMachine object for this console session.
          For the process that owns (executes) the VM, this is the
          preferable way of querying the VM state, because no IPC
          calls are made.
        """
        ret = self._get_attr("state")
        return MachineState(ret)

    @property
    def guest(self):
        """Get IGuest value for 'guest'
        Guest object.
        """
        ret = self._get_attr("guest")
        return IGuest(ret)

    @property
    def keyboard(self):
        """Get IKeyboard value for 'keyboard'
        Virtual keyboard object.
        
          If the machine is not running, any attempt to use
          the returned object will result in an error.
        """
        ret = self._get_attr("keyboard")
        return IKeyboard(ret)

    @property
    def mouse(self):
        """Get IMouse value for 'mouse'
        Virtual mouse object.
        
          If the machine is not running, any attempt to use
          the returned object will result in an error.
        """
        ret = self._get_attr("mouse")
        return IMouse(ret)

    @property
    def display(self):
        """Get IDisplay value for 'display'
        Virtual display object.
        
          If the machine is not running, any attempt to use
          the returned object will result in an error.
        """
        ret = self._get_attr("display")
        return IDisplay(ret)

    @property
    def debugger(self):
        """Get IMachineDebugger value for 'debugger'
        Debugging interface.
        """
        ret = self._get_attr("debugger")
        return IMachineDebugger(ret)

    @property
    def usb_devices(self):
        """Get IUSBDevice value for 'USBDevices'
        Collection of USB devices currently attached to the virtual
        USB controller.
        
          The collection is empty if the machine is not running.
        """
        ret = self._get_attr("USBDevices")
        return [IUSBDevice(a) for a in ret]

    @property
    def remote_usb_devices(self):
        """Get IHostUSBDevice value for 'remoteUSBDevices'
        List of USB devices currently attached to the remote VRDE client.
        Once a new device is physically attached to the remote host computer,
        it appears in this list and remains there until detached.
        """
        ret = self._get_attr("remoteUSBDevices")
        return [IHostUSBDevice(a) for a in ret]

    @property
    def shared_folders(self):
        """Get ISharedFolder value for 'sharedFolders'
        Collection of shared folders for the current session. These folders
        are called transient shared folders because they are available to the
        guest OS running inside the associated virtual machine only for the
        duration of the session (as opposed to
        <link to="IMachine::sharedFolders"/> which represent permanent shared
        folders). When the session is closed (e.g. the machine is powered down),
        these folders are automatically discarded.

        New shared folders are added to the collection using
        <link to="#createSharedFolder"/>. Existing shared folders can be
        removed using <link to="#removeSharedFolder"/>.
        """
        ret = self._get_attr("sharedFolders")
        return [ISharedFolder(a) for a in ret]

    @property
    def vrde_server_info(self):
        """Get IVRDEServerInfo value for 'VRDEServerInfo'
        Interface that provides information on Remote Desktop Extension (VRDE) connection.
        """
        ret = self._get_attr("VRDEServerInfo")
        return IVRDEServerInfo(ret)

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for console events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    @property
    def attached_pci_devices(self):
        """Get IPCIDeviceAttachment value for 'attachedPCIDevices'
        Array of PCI devices attached to this machine.
        """
        ret = self._get_attr("attachedPCIDevices")
        return [IPCIDeviceAttachment(a) for a in ret]

    @property
    def use_host_clipboard(self):
        """Get or set bool value for 'useHostClipboard'
        Whether the guest clipboard should be connected to the host one or
        whether it should only be allowed access to the VRDE clipboard. This
        setting may not affect existing guest clipboard connections which
        are already connected to the host clipboard.
        """
        ret = self._get_attr("useHostClipboard")
        return ret

    @use_host_clipboard.setter
    def use_host_clipboard(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("useHostClipboard", value)

    def power_up(self):
        """Starts the virtual machine execution using the current machine
        state (that is, its current execution state, current settings and
        current storage devices).

        
          This method is only useful for front-ends that want to actually
          execute virtual machines in their own process (like the VirtualBox
          or VBoxSDL front-ends). Unless you are intending to write such a
          front-end, do not call this method. If you simply want to
          start virtual machine execution using one of the existing front-ends
          (for example the VirtualBox GUI or headless server), use
          <link to="IMachine::launchVMProcess"/> instead; these
          front-ends will power up the machine automatically for you.
        

        If the machine is powered off or aborted, the execution will
        start from the beginning (as if the real hardware were just
        powered on).

        If the machine is in the <link to="MachineState_Saved"/> state,
        it will continue its execution the point where the state has
        been saved.

        If the machine <link to="IMachine::teleporterEnabled"/> property is
        enabled on the machine being powered up, the machine will wait for an
        incoming teleportation in the <link to="MachineState_TeleportingIn"/>
        state. The returned progress object will have at least three
        operations where the last three are defined as: (1) powering up and
        starting TCP server, (2) waiting for incoming teleportations, and
        (3) perform teleportation. These operations will be reflected as the
        last three operations of the progress objected returned by
        <link to="IMachine::launchVMProcess"/> as well.

        <link to="#saveState"/>

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine already running.
        
        raises VBOX_E_HOST_ERROR
            Host interface does not exist or name not set.
        
        raises VBOX_E_FILE_ERROR
            Invalid saved state file.
        
        """
        progress = self._call("powerUp")
        progress = IProgress(progress)
        return progress

    def power_up_paused(self):
        """Identical to powerUp except that the VM will enter the
        <link to="MachineState_Paused"/> state, instead of
        <link to="MachineState_Running"/>.

        <link to="#powerUp"/>

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine already running.
        
        raises VBOX_E_HOST_ERROR
            Host interface does not exist or name not set.
        
        raises VBOX_E_FILE_ERROR
            Invalid saved state file.
        
        """
        progress = self._call("powerUpPaused")
        progress = IProgress(progress)
        return progress

    def power_down(self):
        """Initiates the power down procedure to stop the virtual machine
        execution.

        The completion of the power down procedure is tracked using the returned
        IProgress object. After the operation is complete, the machine will go
        to the PoweredOff state.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine must be Running, Paused or Stuck to be powered down.
        
        """
        progress = self._call("powerDown")
        progress = IProgress(progress)
        return progress

    def reset(self):
        """Resets the virtual machine.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Running state.
        
        raises VBOX_E_VM_ERROR
            Virtual machine error in reset operation.
        
        """
        self._call("reset")

    def pause(self):
        """Pauses the virtual machine execution.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Running state.
        
        raises VBOX_E_VM_ERROR
            Virtual machine error in suspend operation.
        
        """
        self._call("pause")

    def resume(self):
        """Resumes the virtual machine execution.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Paused state.
        
        raises VBOX_E_VM_ERROR
            Virtual machine error in resume operation.
        
        """
        self._call("resume")

    def power_button(self):
        """Sends the ACPI power button event to the guest.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Running state.
        
        raises VBOX_E_PDM_ERROR
            Controlled power off failed.
        
        """
        self._call("powerButton")

    def sleep_button(self):
        """Sends the ACPI sleep button event to the guest.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Running state.
        
        raises VBOX_E_PDM_ERROR
            Sending sleep button event failed.
        
        """
        self._call("sleepButton")

    def get_power_button_handled(self):
        """Checks if the last power button event was handled by guest.

        return handled of type bool

        raises VBOX_E_PDM_ERROR
            Checking if the event was handled by the guest OS failed.
        
        """
        handled = self._call("getPowerButtonHandled")
        return handled

    def get_guest_entered_acpi_mode(self):
        """Checks if the guest entered the ACPI mode G0 (working) or
        G1 (sleeping). If this method returns @c false, the guest will
        most likely not respond to external ACPI events.

        return entered of type bool

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Running state.
        
        """
        entered = self._call("getGuestEnteredACPIMode")
        return entered

    def save_state(self):
        """Saves the current execution state of a running virtual machine
        and stops its execution.

        After this operation completes, the machine will go to the
        Saved state. Next time it is powered up, this state will
        be restored and the machine will continue its execution from
        the place where it was saved.

        This operation differs from taking a snapshot to the effect
        that it doesn't create new differencing media. Also, once
        the machine is powered up from the state saved using this method,
        the saved state is deleted, so it will be impossible to return
        to this state later.

        
          On success, this method implicitly calls
          <link to="IMachine::saveSettings"/> to save all current machine
          settings (including runtime changes to the DVD medium, etc.).
          Together with the impossibility to change any VM settings when it is
          in the Saved state, this guarantees adequate hardware
          configuration of the machine when it is restored from the saved
          state file.
        

        
          The machine must be in the Running or Paused state, otherwise
          the operation will fail.
        
        

        <link to="#takeSnapshot"/>

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine state neither Running nor Paused.
        
        raises VBOX_E_FILE_ERROR
            Failed to create directory for saved state file.
        
        """
        progress = self._call("saveState")
        progress = IProgress(progress)
        return progress

    def adopt_saved_state(self, saved_state_file):
        """Associates the given saved state file to the virtual machine.

        On success, the machine will go to the Saved state. Next time it is
        powered up, it will be restored from the adopted saved state and
        continue execution from the place where the saved state file was
        created.

        The specified saved state file path may be absolute or relative to the
        folder the VM normally saves the state to (usually,
        <link to="IMachine::snapshotFolder"/>).

        
          It's a caller's responsibility to make sure the given saved state
          file is compatible with the settings of this virtual machine that
          represent its virtual hardware (memory size, storage disk configuration
          etc.). If there is a mismatch, the behavior of the virtual machine
          is undefined.

        in saved_state_file of type str
            Path to the saved state file to adopt.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine state neither PoweredOff nor Aborted.
        
        """
        if type(saved_state_file) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("adoptSavedState",
                     in_p=[saved_state_file])

    def discard_saved_state(self, f_remove_file):
        """Forcibly resets the machine to "Powered Off" state if it is
        currently in the "Saved" state (previously created by <link to="#saveState"/>).
        Next time the machine is powered up, a clean boot will occur.
        
          This operation is equivalent to resetting or powering off
          the machine without doing a proper shutdown of the guest
          operating system; as with resetting a running phyiscal
          computer, it can can lead to data loss.
        
        If @a fRemoveFile is @c true, the file in the machine directory
        into which the machine state was saved is also deleted. If
        this is @c false, then the state can be recovered and later
        re-inserted into a machine using <link to="#adoptSavedState"/>.
        The location of the file can be found in the
        <link to="IMachine::stateFilePath"/> attribute.

        in f_remove_file of type bool
            Whether to also remove the saved state file.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in state Saved.
        
        """
        if not isinstance(f_remove_file, bool):
            raise TypeError("f_remove_file can only be an instance of type bool")
        self._call("discardSavedState",
                     in_p=[f_remove_file])

    def get_device_activity(self, type_p):
        """Gets the current activity type of a given device or device group.

        in type_p of type DeviceType

        return activity of type DeviceActivity

        raises E_INVALIDARG
            Invalid device type.
        
        """
        if not isinstance(type_p, DeviceType):
            raise TypeError("type_p can only be an instance of type DeviceType")
        activity = self._call("getDeviceActivity",
                     in_p=[type_p])
        activity = DeviceActivity(activity)
        return activity

    def attach_usb_device(self, id_p):
        """Attaches a host USB device with the given UUID to the
        USB controller of the virtual machine.

        The device needs to be in one of the following states:
        <link to="USBDeviceState_Busy"/>,
        <link to="USBDeviceState_Available"/> or
        <link to="USBDeviceState_Held"/>,
        otherwise an error is immediately returned.

        When the device state is
        <link to="USBDeviceState_Busy">Busy</link>, an error may also
        be returned if the host computer refuses to release it for some reason.

        <link to="IUSBController::deviceFilters"/>,
          <link to="USBDeviceState"/>

        in id_p of type str
            UUID of the host USB device to attach.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine state neither Running nor Paused.
        
        raises VBOX_E_PDM_ERROR
            Virtual machine does not have a USB controller.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("attachUSBDevice",
                     in_p=[id_p])

    def detach_usb_device(self, id_p):
        """Detaches an USB device with the given UUID from the USB controller
        of the virtual machine.

        After this method succeeds, the VirtualBox server re-initiates
        all USB filters as if the device were just physically attached
        to the host, but filters of this machine are ignored to avoid
        a possible automatic re-attachment.

        <link to="IUSBController::deviceFilters"/>,
          <link to="USBDeviceState"/>

        in id_p of type str
            UUID of the USB device to detach.

        return device of type IUSBDevice
            Detached USB device.

        raises VBOX_E_PDM_ERROR
            Virtual machine does not have a USB controller.
        
        raises E_INVALIDARG
            USB device not attached to this virtual machine.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        device = self._call("detachUSBDevice",
                     in_p=[id_p])
        device = IUSBDevice(device)
        return device

    def find_usb_device_by_address(self, name):
        """Searches for a USB device with the given host address.

        

        <link to="IUSBDevice::address"/>

        in name of type str
            Address of the USB device (as assigned by the host) to
          search for.

        return device of type IUSBDevice
            Found USB device object.

        raises VBOX_E_OBJECT_NOT_FOUND
            Given @c name does not correspond to any USB device.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        device = self._call("findUSBDeviceByAddress",
                     in_p=[name])
        device = IUSBDevice(device)
        return device

    def find_usb_device_by_id(self, id_p):
        """Searches for a USB device with the given UUID.

        

        <link to="IUSBDevice::id"/>

        in id_p of type str
            UUID of the USB device to search for.

        return device of type IUSBDevice
            Found USB device object.

        raises VBOX_E_OBJECT_NOT_FOUND
            Given @c id does not correspond to any USB device.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        device = self._call("findUSBDeviceById",
                     in_p=[id_p])
        device = IUSBDevice(device)
        return device

    def create_shared_folder(self, name, host_path, writable, automount):
        """Creates a transient new shared folder by associating the given logical
        name with the given host path, adds it to the collection of shared
        folders and starts sharing it. Refer to the description of
        <link to="ISharedFolder"/> to read more about logical names.

        in name of type str
            Unique logical name of the shared folder.

        in host_path of type str
            Full path to the shared folder in the host file system.

        in writable of type bool
            Whether the share is writable or readonly

        in automount of type bool
            Whether the share gets automatically mounted by the guest
          or not.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine in Saved state or currently changing state.
        
        raises VBOX_E_FILE_ERROR
            Shared folder already exists or not accessible.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(host_path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(writable, bool):
            raise TypeError("writable can only be an instance of type bool")
        if not isinstance(automount, bool):
            raise TypeError("automount can only be an instance of type bool")
        self._call("createSharedFolder",
                     in_p=[name, host_path, writable, automount])

    def remove_shared_folder(self, name):
        """Removes a transient shared folder with the given name previously
        created by <link to="#createSharedFolder"/> from the collection of
        shared folders and stops sharing it.

        in name of type str
            Logical name of the shared folder to remove.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine in Saved state or currently changing state.
        
        raises VBOX_E_FILE_ERROR
            Shared folder does not exists.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("removeSharedFolder",
                     in_p=[name])

    def take_snapshot(self, name, description):
        """Saves the current execution state
        and all settings of the machine and creates differencing images
        for all normal (non-independent) media.
        See <link to="ISnapshot"/> for an introduction to snapshots.

        This method can be called for a PoweredOff, Saved (see
        <link to="#saveState"/>), Running or
        Paused virtual machine. When the machine is PoweredOff, an
        offline snapshot is created. When the machine is Running a live
        snapshot is created, and an online snapshot is created when Paused.

        The taken snapshot is always based on the
        <link to="IMachine::currentSnapshot">current snapshot</link>
        of the associated virtual machine and becomes a new current snapshot.

        
          This method implicitly calls <link to="IMachine::saveSettings"/> to
          save all current machine settings before taking an offline snapshot.

        in name of type str
            Short name for the snapshot.

        in description of type str
            Optional description of the snapshot.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine currently changing state.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(description) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("takeSnapshot",
                     in_p=[name, description])
        progress = IProgress(progress)
        return progress

    def delete_snapshot(self, id_p):
        """Starts deleting the specified snapshot asynchronously.
        See <link to="ISnapshot"/> for an introduction to snapshots.

        The execution state and settings of the associated machine stored in
        the snapshot will be deleted. The contents of all differencing media of
        this snapshot will be merged with the contents of their dependent child
        media to keep the medium chain valid (in other words, all changes
        represented by media being deleted will be propagated to their child
        medium). After that, this snapshot's differencing medium will be
        deleted. The parent of this snapshot will become a new parent for all
        its child snapshots.

        If the deleted snapshot is the current one, its parent snapshot will
        become a new current snapshot. The current machine state is not directly
        affected in this case, except that currently attached differencing
        media based on media of the deleted snapshot will be also merged as
        described above.

        If the deleted snapshot is the first or current snapshot, then the
        respective IMachine attributes will be adjusted. Deleting the current
        snapshot will also implicitly call <link to="IMachine::saveSettings"/>
        to make all current machine settings permanent.

        Deleting a snapshot has the following preconditions:

        
          Child media of all normal media of the deleted snapshot
          must be accessible (see <link to="IMedium::state"/>) for this
          operation to succeed. If only one running VM refers to all images
          which participates in merging the operation can be performed while
          the VM is running. Otherwise all virtual machines whose media are
          directly or indirectly based on the media of deleted snapshot must
          be powered off. In any case, online snapshot deleting usually is
          slower than the same operation without any running VM.

          You cannot delete the snapshot if a medium attached to it has
          more than one child medium (differencing images) because otherwise
          merging would be impossible. This might be the case if there is
          more than one child snapshot or differencing images were created
          for other reason (e.g. implicitly because of multiple machine
          attachments).
        

        The virtual machine's <link to="IMachine::state">state</link> is
        changed to "DeletingSnapshot", "DeletingSnapshotOnline" or
        "DeletingSnapshotPaused" while this operation is in progress.

        
          Merging medium contents can be very time and disk space
          consuming, if these media are big in size and have many
          children. However, if the snapshot being deleted is the last
          (head) snapshot on the branch, the operation will be rather
          quick.

        in id_p of type str
            UUID of the snapshot to delete.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            The running virtual machine prevents deleting this snapshot. This
          happens only in very specific situations, usually snapshots can be
          deleted without trouble while a VM is running. The error message
          text explains the reason for the failure.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("deleteSnapshot",
                     in_p=[id_p])
        progress = IProgress(progress)
        return progress

    def delete_snapshot_and_all_children(self, id_p):
        """Starts deleting the specified snapshot and all its children
        asynchronously. See <link to="ISnapshot"/> for an introduction to
        snapshots. The conditions and many details are the same as with
        <link to="#deleteSnapshot"/>.

        This operation is very fast if the snapshot subtree does not include
        the current state. It is still significantly faster than deleting the
        snapshots one by one if the current state is in the subtree and there
        are more than one snapshots from current state to the snapshot which
        marks the subtree, since it eliminates the incremental image merging.

        This API method is right now not implemented!

        in id_p of type str
            UUID of the snapshot to delete, including all its children.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            The running virtual machine prevents deleting this snapshot. This
          happens only in very specific situations, usually snapshots can be
          deleted without trouble while a VM is running. The error message
          text explains the reason for the failure.
        
        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("deleteSnapshotAndAllChildren",
                     in_p=[id_p])
        progress = IProgress(progress)
        return progress

    def delete_snapshot_range(self, start_id, end_id):
        """Starts deleting the specified snapshot range. This is limited to
        linear snapshot lists, which means there may not be any other child
        snapshots other than the direct sequence between the start and end
        snapshot. If the start and end snapshot point to the same snapshot this
        method is completely equivalent to <link to="#deleteSnapshot"/>. See
        <link to="ISnapshot"/> for an introduction to snapshots. The
        conditions and many details are the same as with
        <link to="#deleteSnapshot"/>.

        This operation is generally faster than deleting snapshots one by one
        and often also needs less extra disk space before freeing up disk space
        by deleting the removed disk images corresponding to the snapshot.

        This API method is right now not implemented!

        in start_id of type str
            UUID of the first snapshot to delete.

        in end_id of type str
            UUID of the last snapshot to delete.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            The running virtual machine prevents deleting this snapshot. This
          happens only in very specific situations, usually snapshots can be
          deleted without trouble while a VM is running. The error message
          text explains the reason for the failure.
        
        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(start_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(end_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("deleteSnapshotRange",
                     in_p=[start_id, end_id])
        progress = IProgress(progress)
        return progress

    def restore_snapshot(self, snapshot):
        """Starts resetting the machine's current state to the state contained
        in the given snapshot, asynchronously. All current settings of the
        machine will be reset and changes stored in differencing media
        will be lost.
        See <link to="ISnapshot"/> for an introduction to snapshots.

        After this operation is successfully completed, new empty differencing
        media are created for all normal media of the machine.

        If the given snapshot is an online snapshot, the machine will go to
        the <link to="MachineState_Saved"> saved state</link>, so that the
        next time it is powered on, the execution state will be restored
        from the state of the snapshot.

        
          The machine must not be running, otherwise the operation will fail.
        

        
          If the machine state is <link to="MachineState_Saved">Saved</link>
          prior to this operation, the saved state file will be implicitly
          deleted (as if <link to="IConsole::discardSavedState"/> were
          called).

        in snapshot of type ISnapshot
            The snapshot to restore the VM state from.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is running.
        
        """
        if not isinstance(snapshot, ISnapshot):
            raise TypeError("snapshot can only be an instance of type ISnapshot")
        progress = self._call("restoreSnapshot",
                     in_p=[snapshot])
        progress = IProgress(progress)
        return progress

    def teleport(self, hostname, tcpport, password, max_downtime):
        """Teleport the VM to a different host machine or process.

        TODO explain the details.

        in hostname of type str
            The name or IP of the host to teleport to.

        in tcpport of type int
            The TCP port to connect to (1..65535).

        in password of type str
            The password.

        in max_downtime of type int
            The maximum allowed downtime given as milliseconds. 0 is not a valid
          value. Recommended value: 250 ms.

          The higher the value is, the greater the chance for a successful
          teleportation. A small value may easily result in the teleportation
          process taking hours and eventually fail.

          
            The current implementation treats this a guideline, not as an
            absolute rule.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not running or paused.
        
        """
        if type(hostname) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(tcpport, int):
            raise TypeError("tcpport can only be an instance of type int")
        if type(password) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(max_downtime, int):
            raise TypeError("max_downtime can only be an instance of type int")
        progress = self._call("teleport",
                     in_p=[hostname, tcpport, password, max_downtime])
        progress = IProgress(progress)
        return progress


class IHostNetworkInterface(Interface):
    """
    Represents one of host's network interfaces. IP V6 address and network
      mask are strings of 32 hexdecimal digits grouped by four. Groups are
      separated by colons.
      For example, fe80:0000:0000:0000:021e:c2ff:fed2:b030.
    """
    __uuid__ = '87a4153d-6889-4dd6-9654-2e9ff0ae8dec'
    __wsmap__ = 'managed'
    
    @property
    def name(self):
        """Get str value for 'name'
        Returns the host network interface name.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def id_p(self):
        """Get str value for 'id'
        Returns the interface UUID.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def network_name(self):
        """Get str value for 'networkName'
        Returns the name of a virtual network the interface gets attached to.
        """
        ret = self._get_attr("networkName")
        return ret

    @property
    def dhcp_enabled(self):
        """Get bool value for 'DHCPEnabled'
        Specifies whether the DHCP is enabled for the interface.
        """
        ret = self._get_attr("DHCPEnabled")
        return ret

    @property
    def ip_address(self):
        """Get str value for 'IPAddress'
        Returns the IP V4 address of the interface.
        """
        ret = self._get_attr("IPAddress")
        return ret

    @property
    def network_mask(self):
        """Get str value for 'networkMask'
        Returns the network mask of the interface.
        """
        ret = self._get_attr("networkMask")
        return ret

    @property
    def ipv6_supported(self):
        """Get bool value for 'IPV6Supported'
        Specifies whether the IP V6 is supported/enabled for the interface.
        """
        ret = self._get_attr("IPV6Supported")
        return ret

    @property
    def ipv6_address(self):
        """Get str value for 'IPV6Address'
        Returns the IP V6 address of the interface.
        """
        ret = self._get_attr("IPV6Address")
        return ret

    @property
    def ipv6_network_mask_prefix_length(self):
        """Get int value for 'IPV6NetworkMaskPrefixLength'
        Returns the length IP V6 network mask prefix of the interface.
        """
        ret = self._get_attr("IPV6NetworkMaskPrefixLength")
        return ret

    @property
    def hardware_address(self):
        """Get str value for 'hardwareAddress'
        Returns the hardware address. For Ethernet it is MAC address.
        """
        ret = self._get_attr("hardwareAddress")
        return ret

    @property
    def medium_type(self):
        """Get HostNetworkInterfaceMediumType value for 'mediumType'
        Type of protocol encapsulation used.
        """
        ret = self._get_attr("mediumType")
        return HostNetworkInterfaceMediumType(ret)

    @property
    def status(self):
        """Get HostNetworkInterfaceStatus value for 'status'
        Status of the interface.
        """
        ret = self._get_attr("status")
        return HostNetworkInterfaceStatus(ret)

    @property
    def interface_type(self):
        """Get HostNetworkInterfaceType value for 'interfaceType'
        specifies the host interface type.
        """
        ret = self._get_attr("interfaceType")
        return HostNetworkInterfaceType(ret)

    def enable_static_ip_config(self, ip_address, network_mask):
        """sets and enables the static IP V4 configuration for the given interface.

        in ip_address of type str
            IP address.

        in network_mask of type str
            network mask.

        """
        if type(ip_address) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(network_mask) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("enableStaticIPConfig",
                     in_p=[ip_address, network_mask])

    def enable_static_ip_config_v6(self, ipv6_address, ipv6_network_mask_prefix_length):
        """sets and enables the static IP V6 configuration for the given interface.

        in ipv6_address of type str
            IP address.

        in ipv6_network_mask_prefix_length of type int
            network mask.

        """
        if type(ipv6_address) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(ipv6_network_mask_prefix_length, int):
            raise TypeError("ipv6_network_mask_prefix_length can only be an instance of type int")
        self._call("enableStaticIPConfigV6",
                     in_p=[ipv6_address, ipv6_network_mask_prefix_length])

    def enable_dynamic_ip_config(self):
        """enables the dynamic IP configuration.

        """
        self._call("enableDynamicIPConfig")

    def dhcp_rediscover(self):
        """refreshes the IP configuration for DHCP-enabled interface.

        """
        self._call("DHCPRediscover")


class IHost(Interface):
    """
    The IHost interface represents the physical machine that this VirtualBox
      installation runs on.

      An object implementing this interface is returned by the
      <link to="IVirtualBox::host"/> attribute. This interface contains
      read-only information about the host's physical hardware (such as what
      processors and disks are available, what the host operating system is,
      and so on) and also allows for manipulating some of the host's hardware,
      such as global USB device filters and host interface networking.
    """
    __uuid__ = 'a6107246-f939-42c4-82b6-8aca40327b6d'
    __wsmap__ = 'managed'
    
    @property
    def dvd_drives(self):
        """Get IMedium value for 'DVDDrives'
        List of DVD drives available on the host.
        """
        ret = self._get_attr("DVDDrives")
        return [IMedium(a) for a in ret]

    @property
    def floppy_drives(self):
        """Get IMedium value for 'floppyDrives'
        List of floppy drives available on the host.
        """
        ret = self._get_attr("floppyDrives")
        return [IMedium(a) for a in ret]

    @property
    def usb_devices(self):
        """Get IHostUSBDevice value for 'USBDevices'
        List of USB devices currently attached to the host.
        Once a new device is physically attached to the host computer,
        it appears in this list and remains there until detached.

        
          If USB functionality is not available in the given edition of
          VirtualBox, this method will set the result code to @c E_NOTIMPL.
        """
        ret = self._get_attr("USBDevices")
        return [IHostUSBDevice(a) for a in ret]

    @property
    def usb_device_filters(self):
        """Get IHostUSBDeviceFilter value for 'USBDeviceFilters'
        List of USB device filters in action.
        When a new device is physically attached to the host computer,
        filters from this list are applied to it (in order they are stored
        in the list). The first matched filter will determine the
        <link to="IHostUSBDeviceFilter::action">action</link>
        performed on the device.

        Unless the device is ignored by these filters, filters of all
        currently running virtual machines
        (<link to="IUSBController::deviceFilters"/>) are applied to it.

        
          If USB functionality is not available in the given edition of
          VirtualBox, this method will set the result code to @c E_NOTIMPL.
        

        <link to="IHostUSBDeviceFilter"/>,
          <link to="USBDeviceState"/>
        """
        ret = self._get_attr("USBDeviceFilters")
        return [IHostUSBDeviceFilter(a) for a in ret]

    @property
    def network_interfaces(self):
        """Get IHostNetworkInterface value for 'networkInterfaces'
        List of host network interfaces currently defined on the host.
        """
        ret = self._get_attr("networkInterfaces")
        return [IHostNetworkInterface(a) for a in ret]

    @property
    def name_servers(self):
        """Get str value for 'nameServers'
        The list of nameservers registered in host's name resolving system.
        """
        ret = self._get_attr("nameServers")
        return ret

    @property
    def domain_name(self):
        """Get str value for 'domainName'
        Domain name used for name resoving.
        """
        ret = self._get_attr("domainName")
        return ret

    @property
    def search_strings(self):
        """Get str value for 'searchStrings'
        Search string registered for name resoving.
        """
        ret = self._get_attr("searchStrings")
        return ret

    @property
    def processor_count(self):
        """Get int value for 'processorCount'
        Number of (logical) CPUs installed in the host system.
        """
        ret = self._get_attr("processorCount")
        return ret

    @property
    def processor_online_count(self):
        """Get int value for 'processorOnlineCount'
        Number of (logical) CPUs online in the host system.
        """
        ret = self._get_attr("processorOnlineCount")
        return ret

    @property
    def processor_core_count(self):
        """Get int value for 'processorCoreCount'
        Number of physical processor cores installed in the host system.
        """
        ret = self._get_attr("processorCoreCount")
        return ret

    def get_processor_speed(self, cpu_id):
        """Query the (approximate) maximum speed of a specified host CPU in
        Megahertz.

        in cpu_id of type int
            Identifier of the CPU.

        return speed of type int
            Speed value. 0 is returned if value is not known or @a cpuId is
          invalid.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        speed = self._call("getProcessorSpeed",
                     in_p=[cpu_id])
        return speed

    def get_processor_feature(self, feature):
        """Query whether a CPU feature is supported or not.

        in feature of type ProcessorFeature
            CPU Feature identifier.

        return supported of type bool
            Feature is supported or not.

        """
        if not isinstance(feature, ProcessorFeature):
            raise TypeError("feature can only be an instance of type ProcessorFeature")
        supported = self._call("getProcessorFeature",
                     in_p=[feature])
        return supported

    def get_processor_description(self, cpu_id):
        """Query the model string of a specified host CPU.

        in cpu_id of type int
            Identifier of the CPU.
          
            The current implementation might not necessarily return the
            description for this exact CPU.

        return description of type str
            Model string. An empty string is returned if value is not known or
          @a cpuId is invalid.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        description = self._call("getProcessorDescription",
                     in_p=[cpu_id])
        return description

    def get_processor_cpuid_leaf(self, cpu_id, leaf, sub_leaf):
        """Returns the CPU cpuid information for the specified leaf.

        in cpu_id of type int
            Identifier of the CPU. The CPU most be online.
          
            The current implementation might not necessarily return the
            description for this exact CPU.

        in leaf of type int
            CPUID leaf index (eax).

        in sub_leaf of type int
            CPUID leaf sub index (ecx). This currently only applies to cache
          information on Intel CPUs. Use 0 if retrieving values for
          <link to="IMachine::setCPUIDLeaf"/>.

        out val_eax of type int
            CPUID leaf value for register eax.

        out val_ebx of type int
            CPUID leaf value for register ebx.

        out val_ecx of type int
            CPUID leaf value for register ecx.

        out val_edx of type int
            CPUID leaf value for register edx.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        if not isinstance(leaf, int):
            raise TypeError("leaf can only be an instance of type int")
        if not isinstance(sub_leaf, int):
            raise TypeError("sub_leaf can only be an instance of type int")
        (val_eax, val_ebx, val_ecx, val_edx) = self._call("getProcessorCPUIDLeaf",
                     in_p=[cpu_id, leaf, sub_leaf])
        return (val_eax, val_ebx, val_ecx, val_edx)

    @property
    def memory_size(self):
        """Get int value for 'memorySize'
        Amount of system memory in megabytes installed in the host system.
        """
        ret = self._get_attr("memorySize")
        return ret

    @property
    def memory_available(self):
        """Get int value for 'memoryAvailable'
        Available system memory in the host system.
        """
        ret = self._get_attr("memoryAvailable")
        return ret

    @property
    def operating_system(self):
        """Get str value for 'operatingSystem'
        Name of the host system's operating system.
        """
        ret = self._get_attr("operatingSystem")
        return ret

    @property
    def os_version(self):
        """Get str value for 'OSVersion'
        Host operating system's version string.
        """
        ret = self._get_attr("OSVersion")
        return ret

    @property
    def utc_time(self):
        """Get int value for 'UTCTime'
        Returns the current host time in milliseconds since 1970-01-01 UTC.
        """
        ret = self._get_attr("UTCTime")
        return ret

    @property
    def acceleration3_d_available(self):
        """Get bool value for 'acceleration3DAvailable'
        Returns @c true when the host supports 3D hardware acceleration.
        """
        ret = self._get_attr("acceleration3DAvailable")
        return ret

    def create_host_only_network_interface(self):
        """Creates a new adapter for Host Only Networking.

        out host_interface of type IHostNetworkInterface
            Created host interface object.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises E_INVALIDARG
            Host network interface @a name already exists.
        
        """
        (host_interface, progress) = self._call("createHostOnlyNetworkInterface")
        host_interface = IHostNetworkInterface(host_interface)
        progress = IProgress(progress)
        return (host_interface, progress)

    def remove_host_only_network_interface(self, id_p):
        """Removes the given Host Only Networking interface.

        in id_p of type str
            Adapter GUID.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_OBJECT_NOT_FOUND
            No host network interface matching @a id found.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progress = self._call("removeHostOnlyNetworkInterface",
                     in_p=[id_p])
        progress = IProgress(progress)
        return progress

    def create_usb_device_filter(self, name):
        """Creates a new USB device filter. All attributes except
        the filter name are set to empty (any match),
        active is @c false (the filter is not active).

        The created filter can be added to the list of filters using
        <link to="#insertUSBDeviceFilter"/>.

        <link to="#USBDeviceFilters"/>

        in name of type str
            Filter name. See <link to="IUSBDeviceFilter::name"/> for more information.

        return filter_p of type IHostUSBDeviceFilter
            Created filter object.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        filter_p = self._call("createUSBDeviceFilter",
                     in_p=[name])
        filter_p = IHostUSBDeviceFilter(filter_p)
        return filter_p

    def insert_usb_device_filter(self, position, filter_p):
        """Inserts the given USB device to the specified position
        in the list of filters.

        Positions are numbered starting from @c 0. If the specified
        position is equal to or greater than the number of elements in
        the list, the filter is added at the end of the collection.

        
          Duplicates are not allowed, so an attempt to insert a
          filter already in the list is an error.
        
        
          If USB functionality is not available in the given edition of
          VirtualBox, this method will set the result code to @c E_NOTIMPL.
        

        <link to="#USBDeviceFilters"/>

        in position of type int
            Position to insert the filter to.

        in filter_p of type IHostUSBDeviceFilter
            USB device filter to insert.

        raises VBOX_E_INVALID_OBJECT_STATE
            USB device filter is not created within this VirtualBox instance.
        
        raises E_INVALIDARG
            USB device filter already in list.
        
        """
        if not isinstance(position, int):
            raise TypeError("position can only be an instance of type int")
        if not isinstance(filter_p, IHostUSBDeviceFilter):
            raise TypeError("filter_p can only be an instance of type IHostUSBDeviceFilter")
        self._call("insertUSBDeviceFilter",
                     in_p=[position, filter_p])

    def remove_usb_device_filter(self, position):
        """Removes a USB device filter from the specified position in the
        list of filters.

        Positions are numbered starting from @c 0. Specifying a
        position equal to or greater than the number of elements in
        the list will produce an error.

        
          If USB functionality is not available in the given edition of
          VirtualBox, this method will set the result code to @c E_NOTIMPL.
        

        <link to="#USBDeviceFilters"/>

        in position of type int
            Position to remove the filter from.

        raises E_INVALIDARG
            USB device filter list empty or invalid @a position.
        
        """
        if not isinstance(position, int):
            raise TypeError("position can only be an instance of type int")
        self._call("removeUSBDeviceFilter",
                     in_p=[position])

    def find_host_dvd_drive(self, name):
        """Searches for a host DVD drive with the given @c name.

        in name of type str
            Name of the host drive to search for

        return drive of type IMedium
            Found host drive object

        raises VBOX_E_OBJECT_NOT_FOUND
            Given @c name does not correspond to any host drive.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        drive = self._call("findHostDVDDrive",
                     in_p=[name])
        drive = IMedium(drive)
        return drive

    def find_host_floppy_drive(self, name):
        """Searches for a host floppy drive with the given @c name.

        in name of type str
            Name of the host floppy drive to search for

        return drive of type IMedium
            Found host floppy drive object

        raises VBOX_E_OBJECT_NOT_FOUND
            Given @c name does not correspond to any host floppy drive.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        drive = self._call("findHostFloppyDrive",
                     in_p=[name])
        drive = IMedium(drive)
        return drive

    def find_host_network_interface_by_name(self, name):
        """Searches through all host network interfaces for an interface with
        the given @c name.
        
          The method returns an error if the given @c name does not
          correspond to any host network interface.

        in name of type str
            Name of the host network interface to search for.

        return network_interface of type IHostNetworkInterface
            Found host network interface object.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        network_interface = self._call("findHostNetworkInterfaceByName",
                     in_p=[name])
        network_interface = IHostNetworkInterface(network_interface)
        return network_interface

    def find_host_network_interface_by_id(self, id_p):
        """Searches through all host network interfaces for an interface with
        the given GUID.
        
          The method returns an error if the given GUID does not
          correspond to any host network interface.

        in id_p of type str
            GUID of the host network interface to search for.

        return network_interface of type IHostNetworkInterface
            Found host network interface object.

        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        network_interface = self._call("findHostNetworkInterfaceById",
                     in_p=[id_p])
        network_interface = IHostNetworkInterface(network_interface)
        return network_interface

    def find_host_network_interfaces_of_type(self, type_p):
        """Searches through all host network interfaces and returns a list of interfaces of the specified type

        in type_p of type HostNetworkInterfaceType
            type of the host network interfaces to search for.

        return network_interfaces of type IHostNetworkInterface
            Found host network interface objects.

        """
        if not isinstance(type_p, HostNetworkInterfaceType):
            raise TypeError("type_p can only be an instance of type HostNetworkInterfaceType")
        network_interfaces = self._call("findHostNetworkInterfacesOfType",
                     in_p=[type_p])
        network_interfaces = [IHostNetworkInterface(a) for a in network_interfaces]
        return network_interfaces

    def find_usb_device_by_id(self, id_p):
        """Searches for a USB device with the given UUID.

        

        <link to="IUSBDevice::id"/>

        in id_p of type str
            UUID of the USB device to search for.

        return device of type IHostUSBDevice
            Found USB device object.

        raises VBOX_E_OBJECT_NOT_FOUND
            Given @c id does not correspond to any USB device.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        device = self._call("findUSBDeviceById",
                     in_p=[id_p])
        device = IHostUSBDevice(device)
        return device

    def find_usb_device_by_address(self, name):
        """Searches for a USB device with the given host address.

        

        <link to="IUSBDevice::address"/>

        in name of type str
            Address of the USB device (as assigned by the host) to
          search for.

        return device of type IHostUSBDevice
            Found USB device object.

        raises VBOX_E_OBJECT_NOT_FOUND
            Given @c name does not correspond to any USB device.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        device = self._call("findUSBDeviceByAddress",
                     in_p=[name])
        device = IHostUSBDevice(device)
        return device

    def generate_mac_address(self):
        """Generates a valid Ethernet MAC address, 12 hexadecimal characters.

        return address of type str
            New Ethernet MAC address.

        """
        address = self._call("generateMACAddress")
        return address


class ISystemProperties(Interface):
    """
    The ISystemProperties interface represents global properties of the given
      VirtualBox installation.

      These properties define limits and default values for various attributes
      and parameters. Most of the properties are read-only, but some can be
      changed by a user.
    """
    __uuid__ = '55699910-cc50-11e2-8b8b-0800200c9a66'
    __wsmap__ = 'managed'
    
    @property
    def min_guest_ram(self):
        """Get int value for 'minGuestRAM'
        Minimum guest system memory in Megabytes.
        """
        ret = self._get_attr("minGuestRAM")
        return ret

    @property
    def max_guest_ram(self):
        """Get int value for 'maxGuestRAM'
        Maximum guest system memory in Megabytes.
        """
        ret = self._get_attr("maxGuestRAM")
        return ret

    @property
    def min_guest_vram(self):
        """Get int value for 'minGuestVRAM'
        Minimum guest video memory in Megabytes.
        """
        ret = self._get_attr("minGuestVRAM")
        return ret

    @property
    def max_guest_vram(self):
        """Get int value for 'maxGuestVRAM'
        Maximum guest video memory in Megabytes.
        """
        ret = self._get_attr("maxGuestVRAM")
        return ret

    @property
    def min_guest_cpu_count(self):
        """Get int value for 'minGuestCPUCount'
        Minimum CPU count.
        """
        ret = self._get_attr("minGuestCPUCount")
        return ret

    @property
    def max_guest_cpu_count(self):
        """Get int value for 'maxGuestCPUCount'
        Maximum CPU count.
        """
        ret = self._get_attr("maxGuestCPUCount")
        return ret

    @property
    def max_guest_monitors(self):
        """Get int value for 'maxGuestMonitors'
        Maximum of monitors which could be connected.
        """
        ret = self._get_attr("maxGuestMonitors")
        return ret

    @property
    def info_vd_size(self):
        """Get int value for 'infoVDSize'
        Maximum size of a virtual disk image in bytes. Informational value,
      does not reflect the limits of any virtual disk image format.
        """
        ret = self._get_attr("infoVDSize")
        return ret

    @property
    def serial_port_count(self):
        """Get int value for 'serialPortCount'
        Maximum number of serial ports associated with every
        <link to="IMachine"/> instance.
        """
        ret = self._get_attr("serialPortCount")
        return ret

    @property
    def parallel_port_count(self):
        """Get int value for 'parallelPortCount'
        Maximum number of parallel ports associated with every
        <link to="IMachine"/> instance.
        """
        ret = self._get_attr("parallelPortCount")
        return ret

    @property
    def max_boot_position(self):
        """Get int value for 'maxBootPosition'
        Maximum device position in the boot order. This value corresponds
        to the total number of devices a machine can boot from, to make it
        possible to include all possible devices to the boot list.
        <link to="IMachine::setBootOrder"/>
        """
        ret = self._get_attr("maxBootPosition")
        return ret

    @property
    def default_machine_folder(self):
        """Get or set str value for 'defaultMachineFolder'
        Full path to the default directory used to create new or open
        existing machines when a machine settings file name contains no
        path.

        Starting with VirtualBox 4.0, by default, this attribute contains
        the full path of folder named "VirtualBox VMs" in the user's
        home directory, which depends on the host platform.

        When setting this attribute, a full path must be specified.
        Setting this property to @c null or an empty string or the
        special value "Machines" (for compatibility reasons) will restore
        that default value.

        If the folder specified herein does not exist, it will be created
        automatically as needed.

        
          <link to="IVirtualBox::createMachine"/>,
          <link to="IVirtualBox::openMachine"/>
        """
        ret = self._get_attr("defaultMachineFolder")
        return ret

    @default_machine_folder.setter
    def default_machine_folder(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("defaultMachineFolder", value)

    @property
    def logging_level(self):
        """Get or set str value for 'loggingLevel'
        Specifies the logging level in current use by VirtualBox.
        """
        ret = self._get_attr("loggingLevel")
        return ret

    @logging_level.setter
    def logging_level(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("loggingLevel", value)

    @property
    def medium_formats(self):
        """Get IMediumFormat value for 'mediumFormats'
        List of all medium storage formats supported by this VirtualBox
        installation.

        Keep in mind that the medium format identifier
        (<link to="IMediumFormat::id"/>) used in other API calls like
        <link to="IVirtualBox::createHardDisk"/> to refer to a particular
        medium format is a case-insensitive string. This means that, for
        example, all of the following strings:
        
          "VDI"
          "vdi"
          "VdI"
        refer to the same medium format.

        Note that the virtual medium framework is backend-based, therefore
        the list of supported formats depends on what backends are currently
        installed.

        <link to="IMediumFormat"/>
        """
        ret = self._get_attr("mediumFormats")
        return [IMediumFormat(a) for a in ret]

    @property
    def default_hard_disk_format(self):
        """Get or set str value for 'defaultHardDiskFormat'
        Identifier of the default medium format used by VirtualBox.

        The medium format set by this attribute is used by VirtualBox
        when the medium format was not specified explicitly. One example is
        <link to="IVirtualBox::createHardDisk"/> with the empty
        format argument. A more complex example is implicit creation of
        differencing media when taking a snapshot of a virtual machine:
        this operation will try to use a format of the parent medium first
        and if this format does not support differencing media the default
        format specified by this argument will be used.

        The list of supported medium formats may be obtained by the
        <link to="#mediumFormats"/> call. Note that the default medium
        format must have a capability to create differencing media;
        otherwise operations that create media implicitly may fail
        unexpectedly.

        The initial value of this property is "VDI" in the current
        version of the VirtualBox product, but may change in the future.

        
          Setting this property to @c null or empty string will restore the
          initial value.
        

        
          <link to="#mediumFormats"/>,
          <link to="IMediumFormat::id"/>,
          <link to="IVirtualBox::createHardDisk"/>
        """
        ret = self._get_attr("defaultHardDiskFormat")
        return ret

    @default_hard_disk_format.setter
    def default_hard_disk_format(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("defaultHardDiskFormat", value)

    @property
    def free_disk_space_warning(self):
        """Get or set int value for 'freeDiskSpaceWarning'
        Issue a warning if the free disk space is below (or in some disk
      intensive operation is expected to go below) the given size in
      bytes.
        """
        ret = self._get_attr("freeDiskSpaceWarning")
        return ret

    @free_disk_space_warning.setter
    def free_disk_space_warning(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("freeDiskSpaceWarning", value)

    @property
    def free_disk_space_percent_warning(self):
        """Get or set int value for 'freeDiskSpacePercentWarning'
        Issue a warning if the free disk space is below (or in some disk
      intensive operation is expected to go below) the given percentage.
        """
        ret = self._get_attr("freeDiskSpacePercentWarning")
        return ret

    @free_disk_space_percent_warning.setter
    def free_disk_space_percent_warning(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("freeDiskSpacePercentWarning", value)

    @property
    def free_disk_space_error(self):
        """Get or set int value for 'freeDiskSpaceError'
        Issue an error if the free disk space is below (or in some disk
      intensive operation is expected to go below) the given size in
      bytes.
        """
        ret = self._get_attr("freeDiskSpaceError")
        return ret

    @free_disk_space_error.setter
    def free_disk_space_error(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("freeDiskSpaceError", value)

    @property
    def free_disk_space_percent_error(self):
        """Get or set int value for 'freeDiskSpacePercentError'
        Issue an error if the free disk space is below (or in some disk
      intensive operation is expected to go below) the given percentage.
        """
        ret = self._get_attr("freeDiskSpacePercentError")
        return ret

    @free_disk_space_percent_error.setter
    def free_disk_space_percent_error(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("freeDiskSpacePercentError", value)

    @property
    def vrde_auth_library(self):
        """Get or set str value for 'VRDEAuthLibrary'
        Library that provides authentication for Remote Desktop clients. The library
        is used if a virtual machine's authentication type is set to "external"
        in the VM RemoteDisplay configuration.

        The system library extension (".DLL" or ".so") must be omitted.
        A full path can be specified; if not, then the library must reside on the
        system's default library path.

        The default value of this property is "VBoxAuth". There is a library
        of that name in one of the default VirtualBox library directories.

        For details about VirtualBox authentication libraries and how to implement
        them, please refer to the VirtualBox manual.

        
          Setting this property to @c null or empty string will restore the
          initial value.
        """
        ret = self._get_attr("VRDEAuthLibrary")
        return ret

    @vrde_auth_library.setter
    def vrde_auth_library(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("VRDEAuthLibrary", value)

    @property
    def web_service_auth_library(self):
        """Get or set str value for 'webServiceAuthLibrary'
        Library that provides authentication for webservice clients. The library
        is used if a virtual machine's authentication type is set to "external"
        in the VM RemoteDisplay configuration and will be called from
        within the <link to="IWebsessionManager::logon"/> implementation.

        As opposed to <link to="ISystemProperties::VRDEAuthLibrary"/>,
        there is no per-VM setting for this, as the webservice is a global
        resource (if it is running). Only for this setting (for the webservice),
        setting this value to a literal "null" string disables authentication,
        meaning that <link to="IWebsessionManager::logon"/> will always succeed,
        no matter what user name and password are supplied.

        The initial value of this property is "VBoxAuth",
        meaning that the webservice will use the same authentication
        library that is used by default for VRDE (again, see
        <link to="ISystemProperties::VRDEAuthLibrary"/>).
        The format and calling convention of authentication libraries
        is the same for the webservice as it is for VRDE.

        
          Setting this property to @c null or empty string will restore the
          initial value.
        """
        ret = self._get_attr("webServiceAuthLibrary")
        return ret

    @web_service_auth_library.setter
    def web_service_auth_library(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("webServiceAuthLibrary", value)

    @property
    def default_vrde_ext_pack(self):
        """Get or set str value for 'defaultVRDEExtPack'
        The name of the extension pack providing the default VRDE.

        This attribute is for choosing between multiple extension packs
        providing VRDE. If only one is installed, it will automatically be the
        default one. The attribute value can be empty if no VRDE extension
        pack is installed.

        For details about VirtualBox Remote Desktop Extension and how to
        implement one, please refer to the VirtualBox SDK.
        """
        ret = self._get_attr("defaultVRDEExtPack")
        return ret

    @default_vrde_ext_pack.setter
    def default_vrde_ext_pack(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("defaultVRDEExtPack", value)

    @property
    def log_history_count(self):
        """Get or set int value for 'logHistoryCount'
        This value specifies how many old release log files are kept.
        """
        ret = self._get_attr("logHistoryCount")
        return ret

    @log_history_count.setter
    def log_history_count(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("logHistoryCount", value)

    @property
    def default_audio_driver(self):
        """Get AudioDriverType value for 'defaultAudioDriver'
        This value hold the default audio driver for the current
      system.
        """
        ret = self._get_attr("defaultAudioDriver")
        return AudioDriverType(ret)

    @property
    def autostart_database_path(self):
        """Get or set str value for 'autostartDatabasePath'
        The path to the autostart database. Depending on the host this might
        be a filesystem path or something else.
        """
        ret = self._get_attr("autostartDatabasePath")
        return ret

    @autostart_database_path.setter
    def autostart_database_path(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("autostartDatabasePath", value)

    @property
    def default_additions_iso(self):
        """Get or set str value for 'defaultAdditionsISO'
        The path to the default Guest Additions ISO image. Can be empty if
        the location is not known in this installation.
        """
        ret = self._get_attr("defaultAdditionsISO")
        return ret

    @default_additions_iso.setter
    def default_additions_iso(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("defaultAdditionsISO", value)

    @property
    def default_frontend(self):
        """Get or set str value for 'defaultFrontend'
        Selects which VM frontend should be used by default when launching
        a VM through the <link to="IMachine::launchVMProcess"/> method.
        Empty or @c null strings do not define a particular default, it is up
        to <link to="IMachine::launchVMProcess"/> to select one. See the
        description of <link to="IMachine::launchVMProcess"/> for the valid
        frontend types.

        This global setting is overridden by the per-VM attribute
        <link to="IMachine::defaultFrontend"/> or a frontend type
        passed to <link to="IMachine::launchVMProcess"/>.
        """
        ret = self._get_attr("defaultFrontend")
        return ret

    @default_frontend.setter
    def default_frontend(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("defaultFrontend", value)

    def get_max_network_adapters(self, chipset):
        """Maximum total number of network adapters associated with every
        <link to="IMachine"/> instance.

        in chipset of type ChipsetType
            The chipset type to get the value for.

        return max_network_adapters of type int
            The maximum total number of network adapters allowed.

        """
        if not isinstance(chipset, ChipsetType):
            raise TypeError("chipset can only be an instance of type ChipsetType")
        max_network_adapters = self._call("getMaxNetworkAdapters",
                     in_p=[chipset])
        return max_network_adapters

    def get_max_network_adapters_of_type(self, chipset, type_p):
        """Maximum number of network adapters of a given attachment type,
        associated with every <link to="IMachine"/> instance.

        in chipset of type ChipsetType
            The chipset type to get the value for.

        in type_p of type NetworkAttachmentType
            Type of attachment.

        return max_network_adapters of type int
            The maximum number of network adapters allowed for
          particular chipset and attachment type.

        """
        if not isinstance(chipset, ChipsetType):
            raise TypeError("chipset can only be an instance of type ChipsetType")
        if not isinstance(type_p, NetworkAttachmentType):
            raise TypeError("type_p can only be an instance of type NetworkAttachmentType")
        max_network_adapters = self._call("getMaxNetworkAdaptersOfType",
                     in_p=[chipset, type_p])
        return max_network_adapters

    def get_max_devices_per_port_for_storage_bus(self, bus):
        """Returns the maximum number of devices which can be attached to a port
      for the given storage bus.

        in bus of type StorageBus
            The storage bus type to get the value for.

        return max_devices_per_port of type int
            The maximum number of devices which can be attached to the port for the given
        storage bus.

        """
        if not isinstance(bus, StorageBus):
            raise TypeError("bus can only be an instance of type StorageBus")
        max_devices_per_port = self._call("getMaxDevicesPerPortForStorageBus",
                     in_p=[bus])
        return max_devices_per_port

    def get_min_port_count_for_storage_bus(self, bus):
        """Returns the minimum number of ports the given storage bus supports.

        in bus of type StorageBus
            The storage bus type to get the value for.

        return min_port_count of type int
            The minimum number of ports for the given storage bus.

        """
        if not isinstance(bus, StorageBus):
            raise TypeError("bus can only be an instance of type StorageBus")
        min_port_count = self._call("getMinPortCountForStorageBus",
                     in_p=[bus])
        return min_port_count

    def get_max_port_count_for_storage_bus(self, bus):
        """Returns the maximum number of ports the given storage bus supports.

        in bus of type StorageBus
            The storage bus type to get the value for.

        return max_port_count of type int
            The maximum number of ports for the given storage bus.

        """
        if not isinstance(bus, StorageBus):
            raise TypeError("bus can only be an instance of type StorageBus")
        max_port_count = self._call("getMaxPortCountForStorageBus",
                     in_p=[bus])
        return max_port_count

    def get_max_instances_of_storage_bus(self, chipset, bus):
        """Returns the maximum number of storage bus instances which
        can be configured for each VM. This corresponds to the number of
        storage controllers one can have. Value may depend on chipset type
        used.

        in chipset of type ChipsetType
            The chipset type to get the value for.

        in bus of type StorageBus
            The storage bus type to get the value for.

        return max_instances of type int
            The maximum number of instances for the given storage bus.

        """
        if not isinstance(chipset, ChipsetType):
            raise TypeError("chipset can only be an instance of type ChipsetType")
        if not isinstance(bus, StorageBus):
            raise TypeError("bus can only be an instance of type StorageBus")
        max_instances = self._call("getMaxInstancesOfStorageBus",
                     in_p=[chipset, bus])
        return max_instances

    def get_device_types_for_storage_bus(self, bus):
        """Returns list of all the supported device types
        (<link to="DeviceType"/>) for the given type of storage
        bus.

        in bus of type StorageBus
            The storage bus type to get the value for.

        return device_types of type DeviceType
            The list of all supported device types for the given storage bus.

        """
        if not isinstance(bus, StorageBus):
            raise TypeError("bus can only be an instance of type StorageBus")
        device_types = self._call("getDeviceTypesForStorageBus",
                     in_p=[bus])
        device_types = [DeviceType(a) for a in device_types]
        return device_types

    def get_default_io_cache_setting_for_storage_controller(self, controller_type):
        """Returns the default I/O cache setting for the
        given storage controller

        in controller_type of type StorageControllerType
            The storage controller to the setting for.

        return enabled of type bool
            Returned flag indicating the default value

        """
        if not isinstance(controller_type, StorageControllerType):
            raise TypeError("controller_type can only be an instance of type StorageControllerType")
        enabled = self._call("getDefaultIoCacheSettingForStorageController",
                     in_p=[controller_type])
        return enabled


class IGuestOSType(Interface):
    """"""
    __uuid__ = '6d968f9a-858b-4c50-bf17-241f069e94c2'
    __wsmap__ = 'struct'
    
    @property
    def family_id(self):
        """Get str value for 'familyId'
        Guest OS family identifier string.
        """
        ret = self._get_attr("familyId")
        return ret

    @property
    def family_description(self):
        """Get str value for 'familyDescription'
        Human readable description of the guest OS family.
        """
        ret = self._get_attr("familyDescription")
        return ret

    @property
    def id_p(self):
        """Get str value for 'id'
        Guest OS identifier string.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def description(self):
        """Get str value for 'description'
        Human readable description of the guest OS.
        """
        ret = self._get_attr("description")
        return ret

    @property
    def is64_bit(self):
        """Get bool value for 'is64Bit'
        Returns @c true if the given OS is 64-bit
        """
        ret = self._get_attr("is64Bit")
        return ret

    @property
    def recommended_ioapic(self):
        """Get bool value for 'recommendedIOAPIC'
        Returns @c true if IO APIC recommended for this OS type.
        """
        ret = self._get_attr("recommendedIOAPIC")
        return ret

    @property
    def recommended_virt_ex(self):
        """Get bool value for 'recommendedVirtEx'
        Returns @c true if VT-x or AMD-V recommended for this OS type.
        """
        ret = self._get_attr("recommendedVirtEx")
        return ret

    @property
    def recommended_ram(self):
        """Get int value for 'recommendedRAM'
        Recommended RAM size in Megabytes.
        """
        ret = self._get_attr("recommendedRAM")
        return ret

    @property
    def recommended_vram(self):
        """Get int value for 'recommendedVRAM'
        Recommended video RAM size in Megabytes.
        """
        ret = self._get_attr("recommendedVRAM")
        return ret

    @property
    def recommended2_d_video_acceleration(self):
        """Get bool value for 'recommended2DVideoAcceleration'
        Returns @c true if 2D video acceleration is recommended for this OS type.
        """
        ret = self._get_attr("recommended2DVideoAcceleration")
        return ret

    @property
    def recommended3_d_acceleration(self):
        """Get bool value for 'recommended3DAcceleration'
        Returns @c true if 3D acceleration is recommended for this OS type.
        """
        ret = self._get_attr("recommended3DAcceleration")
        return ret

    @property
    def recommended_hdd(self):
        """Get int value for 'recommendedHDD'
        Recommended hard disk size in bytes.
        """
        ret = self._get_attr("recommendedHDD")
        return ret

    @property
    def adapter_type(self):
        """Get NetworkAdapterType value for 'adapterType'
        Returns recommended network adapter for this OS type.
        """
        ret = self._get_attr("adapterType")
        return NetworkAdapterType(ret)

    @property
    def recommended_pae(self):
        """Get bool value for 'recommendedPAE'
        Returns @c true if using PAE is recommended for this OS type.
        """
        ret = self._get_attr("recommendedPAE")
        return ret

    @property
    def recommended_dvd_storage_controller(self):
        """Get StorageControllerType value for 'recommendedDVDStorageController'
        Recommended storage controller type for DVD/CD drives.
        """
        ret = self._get_attr("recommendedDVDStorageController")
        return StorageControllerType(ret)

    @property
    def recommended_dvd_storage_bus(self):
        """Get StorageBus value for 'recommendedDVDStorageBus'
        Recommended storage bus type for DVD/CD drives.
        """
        ret = self._get_attr("recommendedDVDStorageBus")
        return StorageBus(ret)

    @property
    def recommended_hd_storage_controller(self):
        """Get StorageControllerType value for 'recommendedHDStorageController'
        Recommended storage controller type for HD drives.
        """
        ret = self._get_attr("recommendedHDStorageController")
        return StorageControllerType(ret)

    @property
    def recommended_hd_storage_bus(self):
        """Get StorageBus value for 'recommendedHDStorageBus'
        Recommended storage bus type for HD drives.
        """
        ret = self._get_attr("recommendedHDStorageBus")
        return StorageBus(ret)

    @property
    def recommended_firmware(self):
        """Get FirmwareType value for 'recommendedFirmware'
        Recommended firmware type.
        """
        ret = self._get_attr("recommendedFirmware")
        return FirmwareType(ret)

    @property
    def recommended_usbhid(self):
        """Get bool value for 'recommendedUSBHID'
        Returns @c true if using USB Human Interface Devices, such as keyboard and mouse recommended.
        """
        ret = self._get_attr("recommendedUSBHID")
        return ret

    @property
    def recommended_hpet(self):
        """Get bool value for 'recommendedHPET'
        Returns @c true if using HPET is recommended for this OS type.
        """
        ret = self._get_attr("recommendedHPET")
        return ret

    @property
    def recommended_usb_tablet(self):
        """Get bool value for 'recommendedUSBTablet'
        Returns @c true if using a USB Tablet is recommended.
        """
        ret = self._get_attr("recommendedUSBTablet")
        return ret

    @property
    def recommended_rtc_use_utc(self):
        """Get bool value for 'recommendedRTCUseUTC'
        Returns @c true if the RTC of this VM should be set to UTC
        """
        ret = self._get_attr("recommendedRTCUseUTC")
        return ret

    @property
    def recommended_chipset(self):
        """Get ChipsetType value for 'recommendedChipset'
        Recommended chipset type.
        """
        ret = self._get_attr("recommendedChipset")
        return ChipsetType(ret)

    @property
    def recommended_audio_controller(self):
        """Get AudioControllerType value for 'recommendedAudioController'
        Recommended audio type.
        """
        ret = self._get_attr("recommendedAudioController")
        return AudioControllerType(ret)

    @property
    def recommended_floppy(self):
        """Get bool value for 'recommendedFloppy'
        Returns @c true a floppy drive is recommended for this OS type.
        """
        ret = self._get_attr("recommendedFloppy")
        return ret

    @property
    def recommended_usb(self):
        """Get bool value for 'recommendedUSB'
        Returns @c true a USB controller is recommended for this OS type.
        """
        ret = self._get_attr("recommendedUSB")
        return ret


class IAdditionsFacility(Interface):
    """
    Structure representing a Guest Additions facility.
    """
    __uuid__ = '54992946-6af1-4e49-98ec-58b558b7291e'
    __wsmap__ = 'struct'
    
    @property
    def class_type(self):
        """Get AdditionsFacilityClass value for 'classType'
        The class this facility is part of.
        """
        ret = self._get_attr("classType")
        return AdditionsFacilityClass(ret)

    @property
    def last_updated(self):
        """Get int value for 'lastUpdated'
        Time stamp of the last status update,
        in milliseconds since 1970-01-01 UTC.
        """
        ret = self._get_attr("lastUpdated")
        return ret

    @property
    def name(self):
        """Get str value for 'name'
        The facility's friendly name.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def status(self):
        """Get AdditionsFacilityStatus value for 'status'
        The current status.
        """
        ret = self._get_attr("status")
        return AdditionsFacilityStatus(ret)

    @property
    def type_p(self):
        """Get AdditionsFacilityType value for 'type'
        The facility's type ID.
        """
        ret = self._get_attr("type")
        return AdditionsFacilityType(ret)


class IGuestSession(Interface):
    """
    A guest session represents one impersonated user account on the guest, so
      every operation will use the same credentials specified when creating
      the session object via <link to="IGuest::createSession"/>.

      There can be a maximum of 32 sessions at once per VM. Each session keeps
      track of its started guest processes, opened guest files or guest directories.
      To work on guest files or directories a guest session offers methods to open
      or create such objects (see <link to="IGuestSession::fileOpen"/> or
      <link to="IGuestSession::directoryOpen"/> for example).

      When done with either of these objects, including the guest session itself,
      use the appropriate close() method to let the object do its cleanup work.

      Every guest session has its own environment variable block which gets
      automatically applied when starting a new guest process via
      <link to="IGuestSession::processCreate"/> or <link to="IGuestSession::processCreateEx"/>.
      To override (or unset) certain environment variables already set by the
      guest session, one can specify a per-process environment block when using
      one of the both above mentioned process creation calls.
    """
    __uuid__ = 'c8e8607b-5e67-4073-8f14-146515d0c1ff'
    __wsmap__ = 'managed'
    
    @property
    def user(self):
        """Get str value for 'user'
        Returns the user name used by this session to impersonate
        users on the guest.
        """
        ret = self._get_attr("user")
        return ret

    @property
    def domain(self):
        """Get str value for 'domain'
        Returns the domain name used by this session to impersonate
        users on the guest.
        """
        ret = self._get_attr("domain")
        return ret

    @property
    def name(self):
        """Get str value for 'name'
        Returns the session's friendly name.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def id_p(self):
        """Get int value for 'id'
        Returns the internal session ID.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def timeout(self):
        """Get or set int value for 'timeout'
        Returns the session timeout (in ms).
        """
        ret = self._get_attr("timeout")
        return ret

    @timeout.setter
    def timeout(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("timeout", value)

    @property
    def status(self):
        """Get GuestSessionStatus value for 'status'
        Returns the current session status.
        """
        ret = self._get_attr("status")
        return GuestSessionStatus(ret)

    @property
    def environment(self):
        """Get or set str value for 'environment'
        Returns the current session environment.
        """
        ret = self._get_attr("environment")
        return ret

    @environment.setter
    def environment(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("environment", value)

    @property
    def processes(self):
        """Get IGuestProcess value for 'processes'
        Returns all current guest processes.
        """
        ret = self._get_attr("processes")
        return [IGuestProcess(a) for a in ret]

    @property
    def directories(self):
        """Get IGuestDirectory value for 'directories'
        Returns all currently opened guest directories.
        """
        ret = self._get_attr("directories")
        return [IGuestDirectory(a) for a in ret]

    @property
    def files(self):
        """Get IGuestFile value for 'files'
        Returns all currently opened guest files.
        """
        ret = self._get_attr("files")
        return [IGuestFile(a) for a in ret]

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for guest session events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    def close(self):
        """Closes this session. All opened guest directories, files and
        processes which are not referenced by clients anymore will be
        uninitialized.

        """
        self._call("close")

    def copy_from(self, source, dest, flags):
        """Copies a file from guest to the host.

        in source of type str
            Source file on the guest to copy to the host.

        in dest of type str
            Destination file name on the host.

        in flags of type CopyFileFlag
            Copy flags; see <link to="CopyFileFlag"/> for more information.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_IPRT_ERROR
            Error starting the copy operation.
        
        """
        if type(source) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(dest) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, CopyFileFlag):
                raise TypeError(\
                        "array can only contain objects of type CopyFileFlag")
        progress = self._call("copyFrom",
                     in_p=[source, dest, flags])
        progress = IProgress(progress)
        return progress

    def copy_to(self, source, dest, flags):
        """Copies a file from host to the guest.

        in source of type str
            Source file on the host to copy to the guest.

        in dest of type str
            Destination file name on the guest.

        in flags of type CopyFileFlag
            Copy flags; see <link to="CopyFileFlag"/> for more information.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_IPRT_ERROR
            Error starting the copy operation.
        
        """
        if type(source) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(dest) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, CopyFileFlag):
                raise TypeError(\
                        "array can only contain objects of type CopyFileFlag")
        progress = self._call("copyTo",
                     in_p=[source, dest, flags])
        progress = IProgress(progress)
        return progress

    def directory_create(self, path, mode, flags):
        """Create a directory on the guest.

        in path of type str
            Full path of directory to create.

        in mode of type int
            File creation mode.

        in flags of type DirectoryCreateFlag
            Creation flags; see <link to="DirectoryCreateFlag"/> for more information.

        raises VBOX_E_IPRT_ERROR
            Error while creating the directory.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(mode, int):
            raise TypeError("mode can only be an instance of type int")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, DirectoryCreateFlag):
                raise TypeError(\
                        "array can only contain objects of type DirectoryCreateFlag")
        self._call("directoryCreate",
                     in_p=[path, mode, flags])

    def directory_create_temp(self, template_name, mode, path, secure):
        """Create a temporary directory on the guest.

        in template_name of type str
            Template for the name of the directory to create. This must
          contain at least one 'X' character. The first group of consecutive
          'X' characters in the template will be replaced by a random
          alphanumeric string to produce a unique name.

        in mode of type int
            The mode of the directory to create. Use 0700 unless there are
          reasons not to. This parameter is ignored if "secure" is specified.

        in path of type str
            The absolute path to create the temporary directory in.

        in secure of type bool
            Whether to fail if the directory can not be securely created.
          Currently this means that another unprivileged user cannot
          manipulate the path specified or remove the temporary directory
          after it has been created. Also causes the mode specified to be
          ignored. May not be supported on all guest types.

        return directory of type str
            On success this will contain the name of the directory created
          with full path.

        raises VBOX_E_NOT_SUPPORTED
            The operation is not possible as requested on this particular
          guest type.
        
        raises E_INVALIDARG
            Invalid argument. This includes an incorrectly formatted template,
          or a non-absolute path.
        
        raises VBOX_E_IPRT_ERROR
            The temporary directory could not be created. Possible reasons
          include a non-existing path or an insecure path when the secure
          option was requested.
        
        """
        if type(template_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(mode, int):
            raise TypeError("mode can only be an instance of type int")
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(secure, bool):
            raise TypeError("secure can only be an instance of type bool")
        directory = self._call("directoryCreateTemp",
                     in_p=[template_name, mode, path, secure])
        return directory

    def directory_exists(self, path):
        """Checks whether a directory exists on the guest or not.

        in path of type str
            Directory to check existence for.

        return exists of type bool
            Returns @c true if the directory exists, @c false if not.

        raises VBOX_E_IPRT_ERROR
            Error while checking existence of the directory specified.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        exists = self._call("directoryExists",
                     in_p=[path])
        return exists

    def directory_open(self, path, filter_p, flags):
        """Opens a directory and creates a <link to="IGuestDirectory"/> object that
        can be used for further operations.

        in path of type str
            Full path to file to open.

        in filter_p of type str
            Open filter to apply. This can include wildcards like ? and *.

        in flags of type DirectoryOpenFlag
            Open flags; see <link to="DirectoryOpenFlag"/> for more information.

        return directory of type IGuestDirectory
            <link to="IGuestDirectory"/> object containing the opened directory.

        raises VBOX_E_OBJECT_NOT_FOUND
            Directory to open was not found.
        
        raises VBOX_E_IPRT_ERROR
            Error while opening the directory.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(filter_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, DirectoryOpenFlag):
                raise TypeError(\
                        "array can only contain objects of type DirectoryOpenFlag")
        directory = self._call("directoryOpen",
                     in_p=[path, filter_p, flags])
        directory = IGuestDirectory(directory)
        return directory

    def directory_query_info(self, path):
        """Queries information of a directory on the guest.

        in path of type str
            Directory to query information for.

        return info of type IGuestFsObjInfo
            <link to="IGuestFsObjInfo"/> object containing the queried information.

        raises VBOX_E_OBJECT_NOT_FOUND
            Directory to query information for was not found.
        
        raises VBOX_E_IPRT_ERROR
            Error querying information.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        info = self._call("directoryQueryInfo",
                     in_p=[path])
        info = IGuestFsObjInfo(info)
        return info

    def directory_remove(self, path):
        """Removes a guest directory if not empty.

        in path of type str
            Full path of directory to remove.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("directoryRemove",
                     in_p=[path])

    def directory_remove_recursive(self, path, flags):
        """Removes a guest directory recursively.

        in path of type str
            Full path of directory to remove recursively.

        in flags of type DirectoryRemoveRecFlag
            Remove flags; see <link to="DirectoryRemoveRecFlag"/> for more information.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, DirectoryRemoveRecFlag):
                raise TypeError(\
                        "array can only contain objects of type DirectoryRemoveRecFlag")
        progress = self._call("directoryRemoveRecursive",
                     in_p=[path, flags])
        progress = IProgress(progress)
        return progress

    def directory_rename(self, source, dest, flags):
        """Renames a directory on the guest.

        in source of type str
            Source directory to rename.

        in dest of type str
            Destination directory to rename the source to.

        in flags of type PathRenameFlag
            Rename flags; see <link to="PathRenameFlag"/> for more information.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(source) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(dest) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, PathRenameFlag):
                raise TypeError(\
                        "array can only contain objects of type PathRenameFlag")
        self._call("directoryRename",
                     in_p=[source, dest, flags])

    def directory_set_acl(self, path, acl):
        """Sets the ACL (Access Control List) of a guest directory.

        in path of type str
            Full path of directory to set the ACL for.

        in acl of type str
            Actual ACL string to set. Must comply with the guest OS.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(acl) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("directorySetACL",
                     in_p=[path, acl])

    def environment_clear(self):
        """Clears (deletes) all session environment variables.

        raises VBOX_E_IPRT_ERROR
            Error while clearing the session environment variables.
        
        """
        self._call("environmentClear")

    def environment_get(self, name):
        """Gets the value of a session environment variable.

        in name of type str
            Name of session environment variable to get the value for.

        return value of type str
            Value of the session environment variable specified. If this variable
          does not exist and empty value will be returned.

        raises VBOX_E_IPRT_ERROR
            Error while getting the value of the session environment variable.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("environmentGet",
                     in_p=[name])
        return value

    def environment_set(self, name, value):
        """Sets a session environment variable.

        in name of type str
            Name of session environment variable to set.

        in value of type str
            Value to set the session environment variable to.

        raises VBOX_E_IPRT_ERROR
            Error while setting the session environment variable.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("environmentSet",
                     in_p=[name, value])

    def environment_unset(self, name):
        """Unsets session environment variable.

        in name of type str
            Name of session environment variable to unset (clear).

        raises VBOX_E_IPRT_ERROR
            Error while unsetting the session environment variable.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("environmentUnset",
                     in_p=[name])

    def file_create_temp(self, template_name, mode, path, secure):
        """Creates a temporary file on the guest.

        in template_name of type str
            Template for the name of the file to create. This must contain
          at least one 'X' character. The first group of consecutive 'X'
          characters in the template will be replaced by a random
          alphanumeric string to produce a unique name.

        in mode of type int
            The mode of the file to create. Use 0700 unless there are
          reasons not to. This parameter is ignored if "secure" is specified.

        in path of type str
            The absolute path to create the temporary file in.

        in secure of type bool
            Whether to fail if the file can not be securely created.
          Currently this means that another unprivileged user cannot
          manipulate the path specified or remove the temporary file after
          it has been created. Also causes the mode specified to be ignored.
          May not be supported on all guest types.

        return file_p of type IGuestFile
            On success this will contain an open file object for the new
          temporary file.

        raises VBOX_E_NOT_SUPPORTED
            The operation is not possible as requested on this particular
          guest type.
        
        raises E_INVALIDARG
            Invalid argument. This includes an incorrectly formatted template,
          or a non-absolute path.
        
        raises VBOX_E_IPRT_ERROR
            The temporary file could not be created. Possible reasons include
          a non-existing path or an insecure path when the secure
          option was requested.
        
        """
        if type(template_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(mode, int):
            raise TypeError("mode can only be an instance of type int")
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(secure, bool):
            raise TypeError("secure can only be an instance of type bool")
        file_p = self._call("fileCreateTemp",
                     in_p=[template_name, mode, path, secure])
        file_p = IGuestFile(file_p)
        return file_p

    def file_exists(self, path):
        """Checks whether a file exists on the guest or not.

        in path of type str
            File to check existence for.

        return exists of type bool
            Returns @c true if the file exists, @c false if not.

        raises VBOX_E_IPRT_ERROR
            Error while checking existence of the file specified.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        exists = self._call("fileExists",
                     in_p=[path])
        return exists

    def file_remove(self, path):
        """Removes a single file on the guest.

        in path of type str
            Path to the file to remove.

        raises VBOX_E_OBJECT_NOT_FOUND
            File to remove was not found.
        
        raises VBOX_E_IPRT_ERROR
            Error while removing the file.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("fileRemove",
                     in_p=[path])

    def file_open(self, path, open_mode, disposition, creation_mode, offset):
        """Opens a file and creates a <link to="IGuestFile"/> object that
        can be used for further operations.

        in path of type str
            Full path to file to open.

        in open_mode of type str
            The file open mode.

        in disposition of type str
            The file disposition.

        in creation_mode of type int
            The file creation mode.

        in offset of type int
            The initial read/write offset.

        return file_p of type IGuestFile
            <link to="IGuestFile"/> object representing the opened file.

        raises VBOX_E_OBJECT_NOT_FOUND
            File to open was not found.
        
        raises VBOX_E_IPRT_ERROR
            Error while opening the file.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(open_mode) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(disposition) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(creation_mode, int):
            raise TypeError("creation_mode can only be an instance of type int")
        if not isinstance(offset, int):
            raise TypeError("offset can only be an instance of type int")
        file_p = self._call("fileOpen",
                     in_p=[path, open_mode, disposition, creation_mode, offset])
        file_p = IGuestFile(file_p)
        return file_p

    def file_query_info(self, path):
        """Queries information of a file on the guest.

        in path of type str
            File to query information for.

        return info of type IGuestFsObjInfo
            <link to="IGuestFsObjInfo"/> object containing the queried information.

        raises VBOX_E_OBJECT_NOT_FOUND
            File to query information for was not found.
        
        raises VBOX_E_IPRT_ERROR
            Error querying information.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        info = self._call("fileQueryInfo",
                     in_p=[path])
        info = IGuestFsObjInfo(info)
        return info

    def file_query_size(self, path):
        """Queries the size of a file on the guest.

        in path of type str
            File to query the size for.

        return size of type int
            Queried file size.

        raises VBOX_E_OBJECT_NOT_FOUND
            File to rename was not found.
        
        raises VBOX_E_IPRT_ERROR
            Error querying file size.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        size = self._call("fileQuerySize",
                     in_p=[path])
        return size

    def file_rename(self, source, dest, flags):
        """Renames a file on the guest.

        in source of type str
            Source file to rename.

        in dest of type str
            Destination file to rename the source to.

        in flags of type PathRenameFlag
            Rename flags; see <link to="PathRenameFlag"/> for more information.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(source) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(dest) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, PathRenameFlag):
                raise TypeError(\
                        "array can only contain objects of type PathRenameFlag")
        self._call("fileRename",
                     in_p=[source, dest, flags])

    def file_set_acl(self, file_p, acl):
        """Sets the ACL (Access Control List) of a file on the guest.

        in file_p of type str
            Full path of file to set the ACL for.

        in acl of type str
            Actual ACL string to set. Must comply with the guest OS.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(file_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(acl) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("fileSetACL",
                     in_p=[file_p, acl])

    def process_create(self, command, arguments, environment, flags, timeout_ms):
        """Creates a new process running on the guest. The new process will be
        started asynchronously, meaning on return of this function it is not
        guaranteed that the guest process is in a started state. To wait for
        successful startup, use the <link to="IProcess::waitFor"/> call.

        
          Starting at VirtualBox 4.2 guest process execution by default is limited
          to serve up to 255 guest processes at a time. If all 255 guest processes
          are still active and running, creating a new guest process will result in an
          appropriate error message.

          If ProcessCreateFlag_WaitForStdOut and / or respectively ProcessCreateFlag_WaitForStdErr
          is / are set, the guest process will not exit until all data from the specified
          stream(s) is / are read out.

          To raise or lower the guest process execution limit, either the guest property
          "/VirtualBox/GuestAdd/VBoxService/--control-procs-max-kept" or VBoxService'
          command line by specifying "--control-procs-max-kept" needs to be modified.
          A restart of the guest OS is required afterwards. To serve unlimited guest
          processes, a value of "0" needs to be set (not recommended).

        in command of type str
            Full path name of the command to execute on the guest; the
          commands has to exists in the guest VM in order to be executed.

        in arguments of type str
            Array of arguments passed to the execution command.

        in environment of type str
            <para>Environment variables that can be set while the command is being
          executed, in form of "NAME=VALUE"; one pair per entry. To unset a
          variable just set its name ("NAME") without a value.</para>
          <para>This parameter can be used to override environment variables set by
          the guest session, which will be applied to the newly started process
          in any case.</para>

        in flags of type ProcessCreateFlag
            Process creation flags;
          see <link to="ProcessCreateFlag"/> for more information.

        in timeout_ms of type int
            Timeout (in ms) for limiting the guest process' running time.
          Pass 0 for an infinite timeout. On timeout the guest process will be
          killed and its status will be put to an appropriate value. See
          <link to="ProcessStatus"/> for more information.

        return guest_process of type IGuestProcess
            Guest process object of the newly created process.

        raises VBOX_E_IPRT_ERROR
            Error creating guest process.
        
        """
        if type(command) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(arguments, list):
            raise TypeError("arguments can only be an instance of type list")
        for a in arguments[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(environment, list):
            raise TypeError("environment can only be an instance of type list")
        for a in environment[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, ProcessCreateFlag):
                raise TypeError(\
                        "array can only contain objects of type ProcessCreateFlag")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        guest_process = self._call("processCreate",
                     in_p=[command, arguments, environment, flags, timeout_ms])
        guest_process = IGuestProcess(guest_process)
        return guest_process

    def process_create_ex(self, command, arguments, environment, flags, timeout_ms, priority, affinity):
        """<para>Creates a new process running on the guest. Extended version for
          also setting the process priority and affinity.</para>

        <para>See <link to="IGuestSession::processCreate"/> for more
          information.</para>

        in command of type str
            Full path name of the command to execute on the guest; the
          commands has to exists in the guest VM in order to be executed.

        in arguments of type str
            Array of arguments passed to the execution command.

        in environment of type str
            <para>Environment variables that can be set while the command is being
          executed, in form of "NAME=VALUE"; one pair per entry. To unset a
          variable just set its name ("NAME") without a value.</para>
          <para>This parameter can be used to override environment variables set by
          the guest session, which will be applied to the newly started process
          in any case.</para>

        in flags of type ProcessCreateFlag
            Process creation flags;
          see <link to="ProcessCreateFlag"/> for more information.

        in timeout_ms of type int
            Timeout (in ms) for limiting the guest process' running time.
          Pass 0 for an infinite timeout. On timeout the guest process will be
          killed and its status will be put to an appropriate value. See
          <link to="ProcessStatus"/> for more information.

        in priority of type ProcessPriority
            Process priority to use for execution;
          see see <link to="ProcessPriority"/> for more information.

        in affinity of type int
            Process affinity to use for execution. This parameter
          is not implemented yet.

        return guest_process of type IGuestProcess
            Guest process object of the newly created process.

        """
        if type(command) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(arguments, list):
            raise TypeError("arguments can only be an instance of type list")
        for a in arguments[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(environment, list):
            raise TypeError("environment can only be an instance of type list")
        for a in environment[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, ProcessCreateFlag):
                raise TypeError(\
                        "array can only contain objects of type ProcessCreateFlag")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        if not isinstance(priority, ProcessPriority):
            raise TypeError("priority can only be an instance of type ProcessPriority")
        if not isinstance(affinity, list):
            raise TypeError("affinity can only be an instance of type list")
        for a in affinity[:10]:
            if not isinstance(a, int):
                raise TypeError(\
                        "array can only contain objects of type int")
        guest_process = self._call("processCreateEx",
                     in_p=[command, arguments, environment, flags, timeout_ms, priority, affinity])
        guest_process = IGuestProcess(guest_process)
        return guest_process

    def process_get(self, pid):
        """Gets a certain guest process by its process ID (PID).

        in pid of type int
            Process ID (PID) to get guest process for.

        return guest_process of type IGuestProcess
            Guest process of specified process ID (PID).

        """
        if not isinstance(pid, int):
            raise TypeError("pid can only be an instance of type int")
        guest_process = self._call("processGet",
                     in_p=[pid])
        guest_process = IGuestProcess(guest_process)
        return guest_process

    def symlink_create(self, source, target, type_p):
        """Creates a symbolic link on the guest.

        in source of type str
            The name of the symbolic link.

        in target of type str
            The path to the symbolic link target.

        in type_p of type SymlinkType
            The symbolic link type;
          see <link to="SymlinkReadFlag"/> for more information.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(source) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(target) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(type_p, SymlinkType):
            raise TypeError("type_p can only be an instance of type SymlinkType")
        self._call("symlinkCreate",
                     in_p=[source, target, type_p])

    def symlink_exists(self, symlink):
        """Checks whether a symbolic link exists on the guest or not.

        in symlink of type str
            Symbolic link to check existence for.

        return exists of type bool
            Returns @c true if the symbolic link exists, @c false if not.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(symlink) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        exists = self._call("symlinkExists",
                     in_p=[symlink])
        return exists

    def symlink_read(self, symlink, flags):
        """Reads a symbolic link on the guest.

        in symlink of type str
            Full path to symbolic link to read.

        in flags of type SymlinkReadFlag
            Read flags; see <link to="SymlinkReadFlag"/> for more information.

        return target of type str
            Target of the symbolic link pointing to, if found.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(symlink) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, SymlinkReadFlag):
                raise TypeError(\
                        "array can only contain objects of type SymlinkReadFlag")
        target = self._call("symlinkRead",
                     in_p=[symlink, flags])
        return target

    def symlink_remove_directory(self, path):
        """Removes a symbolic link on the guest if it's a directory.

        in path of type str
            Symbolic link to remove.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("symlinkRemoveDirectory",
                     in_p=[path])

    def symlink_remove_file(self, file_p):
        """Removes a symbolic link on the guest if it's a file.

        in file_p of type str
            Symbolic link to remove.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(file_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("symlinkRemoveFile",
                     in_p=[file_p])

    def wait_for(self, wait_for, timeout_ms):
        """Waits for one more events to happen.

        in wait_for of type int
            Specifies what to wait for;
          see <link to="GuestSessionWaitForFlag"/> for more information.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return reason of type GuestSessionWaitResult
            The overall wait result;
          see <link to="GuestSessionWaitResult"/> for more information.

        """
        if not isinstance(wait_for, int):
            raise TypeError("wait_for can only be an instance of type int")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        reason = self._call("waitFor",
                     in_p=[wait_for, timeout_ms])
        reason = GuestSessionWaitResult(reason)
        return reason

    def wait_for_array(self, wait_for, timeout_ms):
        """Waits for one more events to happen.
        Scriptable version of <link to="#waitFor"/>.

        in wait_for of type GuestSessionWaitForFlag
            Specifies what to wait for;
          see <link to="GuestSessionWaitForFlag"/> for more information.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return reason of type GuestSessionWaitResult
            The overall wait result;
          see <link to="GuestSessionWaitResult"/> for more information.

        """
        if not isinstance(wait_for, list):
            raise TypeError("wait_for can only be an instance of type list")
        for a in wait_for[:10]:
            if not isinstance(a, GuestSessionWaitForFlag):
                raise TypeError(\
                        "array can only contain objects of type GuestSessionWaitForFlag")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        reason = self._call("waitForArray",
                     in_p=[wait_for, timeout_ms])
        reason = GuestSessionWaitResult(reason)
        return reason


class IProcess(Interface):
    """
    Abstract parent interface for processes handled by VirtualBox.
    """
    __uuid__ = '5a4fe06d-8cb1-40ff-ac9e-9676e32f706e'
    __wsmap__ = 'managed'
    
    @property
    def arguments(self):
        """Get str value for 'arguments'
        The arguments this process is using for execution.
        """
        ret = self._get_attr("arguments")
        return ret

    @property
    def environment(self):
        """Get str value for 'environment'
        The environment block this process is using during execution.
        """
        ret = self._get_attr("environment")
        return ret

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for VirtualBox events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    @property
    def executable_path(self):
        """Get str value for 'executablePath'
        Full path of the actual executable image.
        """
        ret = self._get_attr("executablePath")
        return ret

    @property
    def exit_code(self):
        """Get int value for 'exitCode'
        The exit code. Only available when the process has been
        terminated normally.
        """
        ret = self._get_attr("exitCode")
        return ret

    @property
    def name(self):
        """Get str value for 'name'
        The friendly name of this process.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def pid(self):
        """Get int value for 'PID'
        The process ID (PID).
        """
        ret = self._get_attr("PID")
        return ret

    @property
    def status(self):
        """Get ProcessStatus value for 'status'
        The current process status; see <link to="ProcessStatus"/>
        for more information.
        """
        ret = self._get_attr("status")
        return ProcessStatus(ret)

    def wait_for(self, wait_for, timeout_ms):
        """Waits for one more events to happen.

        in wait_for of type int
            Specifies what to wait for;
          see <link to="ProcessWaitForFlag"/> for more information.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return reason of type ProcessWaitResult
            The overall wait result;
          see <link to="ProcessWaitResult"/> for more information.

        """
        if not isinstance(wait_for, int):
            raise TypeError("wait_for can only be an instance of type int")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        reason = self._call("waitFor",
                     in_p=[wait_for, timeout_ms])
        reason = ProcessWaitResult(reason)
        return reason

    def wait_for_array(self, wait_for, timeout_ms):
        """Waits for one more events to happen.
        Scriptable version of <link to="#waitFor"/>.

        in wait_for of type ProcessWaitForFlag
            Specifies what to wait for;
          see <link to="ProcessWaitForFlag"/> for more information.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return reason of type ProcessWaitResult
            The overall wait result;
          see <link to="ProcessWaitResult"/> for more information.

        """
        if not isinstance(wait_for, list):
            raise TypeError("wait_for can only be an instance of type list")
        for a in wait_for[:10]:
            if not isinstance(a, ProcessWaitForFlag):
                raise TypeError(\
                        "array can only contain objects of type ProcessWaitForFlag")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        reason = self._call("waitForArray",
                     in_p=[wait_for, timeout_ms])
        reason = ProcessWaitResult(reason)
        return reason

    def read(self, handle, to_read, timeout_ms):
        """Reads data from a running process.

        in handle of type int
            Handle to read from. Usually 0 is stdin.

        in to_read of type int
            Number of bytes to read.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return data of type str
            Array of data read.

        """
        if not isinstance(handle, int):
            raise TypeError("handle can only be an instance of type int")
        if not isinstance(to_read, int):
            raise TypeError("to_read can only be an instance of type int")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        data = self._call("read",
                     in_p=[handle, to_read, timeout_ms])
        return data

    def write(self, handle, flags, data, timeout_ms):
        """Writes data to a running process.

        in handle of type int
            Handle to write to. Usually 0 is stdin, 1 is stdout and 2 is stderr.

        in flags of type int
            A combination of <link to="ProcessInputFlag"/> flags.

        in data of type str
            Array of bytes to write. The size of the array also specifies
          how much to write.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return written of type int
            How much bytes were written.

        """
        if not isinstance(handle, int):
            raise TypeError("handle can only be an instance of type int")
        if not isinstance(flags, int):
            raise TypeError("flags can only be an instance of type int")
        if not isinstance(data, list):
            raise TypeError("data can only be an instance of type list")
        for a in data[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        written = self._call("write",
                     in_p=[handle, flags, data, timeout_ms])
        return written

    def write_array(self, handle, flags, data, timeout_ms):
        """Writes data to a running process.
        Scriptable version of <link to="#write"/>.

        in handle of type int
            Handle to write to. Usually 0 is stdin, 1 is stdout and 2 is stderr.

        in flags of type ProcessInputFlag
            A combination of <link to="ProcessInputFlag"/> flags.

        in data of type str
            Array of bytes to write. The size of the array also specifies
          how much to write.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return written of type int
            How much bytes were written.

        """
        if not isinstance(handle, int):
            raise TypeError("handle can only be an instance of type int")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, ProcessInputFlag):
                raise TypeError(\
                        "array can only contain objects of type ProcessInputFlag")
        if not isinstance(data, list):
            raise TypeError("data can only be an instance of type list")
        for a in data[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        written = self._call("writeArray",
                     in_p=[handle, flags, data, timeout_ms])
        return written

    def terminate(self):
        """Terminates (kills) a running process.

        """
        self._call("terminate")


class IGuestProcess(IProcess):
    """
    Implementation of the <link to="IProcess"/> object
      for processes on the guest.
    """
    __uuid__ = 'dfa39a36-5d43-4840-a025-67ea956b3111'
    __wsmap__ = 'managed'
    

class IDirectory(Interface):
    """
    Abstract parent interface for directories handled by VirtualBox.
    """
    __uuid__ = '1b70dd03-26d7-483a-8877-89bbb0f87b70'
    __wsmap__ = 'managed'
    
    @property
    def directory_name(self):
        """Get str value for 'directoryName'
        Full path of directory.
        """
        ret = self._get_attr("directoryName")
        return ret

    @property
    def filter_p(self):
        """Get str value for 'filter'
        The open filter.
        """
        ret = self._get_attr("filter")
        return ret

    def close(self):
        """Closes this directory. After closing operations like reading the next
        directory entry will not be possible anymore.

        """
        self._call("close")

    def read(self):
        """Reads the next directory entry of this directory.

        return obj_info of type IFsObjInfo
            Object information of the current directory entry read. Also see
          <link to="IFsObjInfo"/>.

        raises VBOX_E_OBJECT_NOT_FOUND
            No more directory entries to read.
        
        """
        obj_info = self._call("read")
        obj_info = IFsObjInfo(obj_info)
        return obj_info


class IGuestDirectory(IDirectory):
    """
    Implementation of the <link to="IDirectory"/> object
      for directories on the guest.
    """
    __uuid__ = 'af4a8ce0-0725-42b7-8826-46e3c7ba7357'
    __wsmap__ = 'managed'
    

class IFile(Interface):
    """
    Abstract parent interface for files handled by VirtualBox.
    """
    __uuid__ = 'ceb895d7-8b2d-4a39-8f7c-7d2270f341d5'
    __wsmap__ = 'managed'
    
    @property
    def creation_mode(self):
        """Get int value for 'creationMode'
        The creation mode.
        """
        ret = self._get_attr("creationMode")
        return ret

    @property
    def disposition(self):
        """Get int value for 'disposition'
        The disposition mode.
        """
        ret = self._get_attr("disposition")
        return ret

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for guest session events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    @property
    def file_name(self):
        """Get str value for 'fileName'
        Full path of the actual file name of this file.
        """
        ret = self._get_attr("fileName")
        return ret

    @property
    def initial_size(self):
        """Get int value for 'initialSize'
        The initial size in bytes when opened.
        """
        ret = self._get_attr("initialSize")
        return ret

    @property
    def open_mode(self):
        """Get int value for 'openMode'
        The open mode.
        """
        ret = self._get_attr("openMode")
        return ret

    @property
    def offset(self):
        """Get int value for 'offset'
        Current read/write offset in bytes.
        """
        ret = self._get_attr("offset")
        return ret

    @property
    def status(self):
        """Get FileStatus value for 'status'
        Current file status.
        """
        ret = self._get_attr("status")
        return FileStatus(ret)

    def close(self):
        """Closes this file. After closing operations like reading data,
        writing data or querying information will not be possible anymore.

        """
        self._call("close")

    def query_info(self):
        """Queries information about this file.

        return obj_info of type IFsObjInfo
            Object information of this file. Also see
          <link to="IFsObjInfo"/>.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        obj_info = self._call("queryInfo")
        obj_info = IFsObjInfo(obj_info)
        return obj_info

    def read(self, to_read, timeout_ms):
        """Reads data from this file.

        in to_read of type int
            Number of bytes to read.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return data of type str
            Array of data read.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if not isinstance(to_read, int):
            raise TypeError("to_read can only be an instance of type int")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        data = self._call("read",
                     in_p=[to_read, timeout_ms])
        return data

    def read_at(self, offset, to_read, timeout_ms):
        """Reads data from an offset of this file.

        in offset of type int
            Offset in bytes to start reading.

        in to_read of type int
            Number of bytes to read.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return data of type str
            Array of data read.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if not isinstance(offset, int):
            raise TypeError("offset can only be an instance of type int")
        if not isinstance(to_read, int):
            raise TypeError("to_read can only be an instance of type int")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        data = self._call("readAt",
                     in_p=[offset, to_read, timeout_ms])
        return data

    def seek(self, offset, whence):
        """Changes the read and write position of this file.

        in offset of type int
            Offset to seek.

        in whence of type FileSeekType
            Seek mode; see <link to="FileSeekType"/> for more information.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if not isinstance(offset, int):
            raise TypeError("offset can only be an instance of type int")
        if not isinstance(whence, FileSeekType):
            raise TypeError("whence can only be an instance of type FileSeekType")
        self._call("seek",
                     in_p=[offset, whence])

    def set_acl(self, acl):
        """Sets the ACL of this file.

        in acl of type str
            ACL string to set.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if type(acl) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setACL",
                     in_p=[acl])

    def write(self, data, timeout_ms):
        """Writes bytes to this file.

        in data of type str
            Array of bytes to write. The size of the array also specifies
          how much to write.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return written of type int
            How much bytes were written.

        """
        if not isinstance(data, list):
            raise TypeError("data can only be an instance of type list")
        for a in data[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        written = self._call("write",
                     in_p=[data, timeout_ms])
        return written

    def write_at(self, offset, data, timeout_ms):
        """Writes bytes at a certain offset to this file.

        in offset of type int
            Offset in bytes to start writing.

        in data of type str
            Array of bytes to write. The size of the array also specifies
          how much to write.

        in timeout_ms of type int
            Timeout (in ms) to wait for the operation to complete.
          Pass 0 for an infinite timeout.

        return written of type int
            How much bytes were written.

        raises E_NOTIMPL
            The method is not implemented yet.
        
        """
        if not isinstance(offset, int):
            raise TypeError("offset can only be an instance of type int")
        if not isinstance(data, list):
            raise TypeError("data can only be an instance of type list")
        for a in data[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(timeout_ms, int):
            raise TypeError("timeout_ms can only be an instance of type int")
        written = self._call("writeAt",
                     in_p=[offset, data, timeout_ms])
        return written


class IGuestFile(IFile):
    """
    Implementation of the <link to="IFile"/> object
      for files on the guest.
    """
    __uuid__ = '60661aec-145f-4d11-b80e-8ea151598093'
    __wsmap__ = 'managed'
    

class IFsObjInfo(Interface):
    """
    Abstract parent interface for VirtualBox file system object information.
      This can be information about a file or a directory, for example.
    """
    __uuid__ = '4047ba30-7006-4966-ae86-94164e5e20eb'
    __wsmap__ = 'managed'
    
    @property
    def access_time(self):
        """Get int value for 'accessTime'
        Time of last access (st_atime).
        """
        ret = self._get_attr("accessTime")
        return ret

    @property
    def allocated_size(self):
        """Get int value for 'allocatedSize'
        Disk allocation size (st_blocks * DEV_BSIZE).
        """
        ret = self._get_attr("allocatedSize")
        return ret

    @property
    def birth_time(self):
        """Get int value for 'birthTime'
        Time of file birth (st_birthtime).
        """
        ret = self._get_attr("birthTime")
        return ret

    @property
    def change_time(self):
        """Get int value for 'changeTime'
        Time of last status change (st_ctime).
        """
        ret = self._get_attr("changeTime")
        return ret

    @property
    def device_number(self):
        """Get int value for 'deviceNumber'
        The device number of a character or block device type object (st_rdev).
        """
        ret = self._get_attr("deviceNumber")
        return ret

    @property
    def file_attributes(self):
        """Get str value for 'fileAttributes'
        File attributes. Not implemented yet.
        """
        ret = self._get_attr("fileAttributes")
        return ret

    @property
    def generation_id(self):
        """Get int value for 'generationId'
        The current generation number (st_gen).
        """
        ret = self._get_attr("generationId")
        return ret

    @property
    def gid(self):
        """Get int value for 'GID'
        The group the filesystem object is assigned (st_gid).
        """
        ret = self._get_attr("GID")
        return ret

    @property
    def group_name(self):
        """Get str value for 'groupName'
        The group name.
        """
        ret = self._get_attr("groupName")
        return ret

    @property
    def hard_links(self):
        """Get int value for 'hardLinks'
        Number of hard links to this filesystem object (st_nlink).
        """
        ret = self._get_attr("hardLinks")
        return ret

    @property
    def modification_time(self):
        """Get int value for 'modificationTime'
        Time of last data modification (st_mtime).
        """
        ret = self._get_attr("modificationTime")
        return ret

    @property
    def name(self):
        """Get str value for 'name'
        The object's name.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def node_id(self):
        """Get int value for 'nodeId'
        The unique identifier (within the filesystem) of this filesystem object (st_ino).
        """
        ret = self._get_attr("nodeId")
        return ret

    @property
    def node_id_device(self):
        """Get int value for 'nodeIdDevice'
        The device number of the device which this filesystem object resides on (st_dev).
        """
        ret = self._get_attr("nodeIdDevice")
        return ret

    @property
    def object_size(self):
        """Get int value for 'objectSize'
        The logical size (st_size). For normal files this is the size of the file.
        For symbolic links, this is the length of the path name contained in the
        symbolic link. For other objects this fields needs to be specified.
        """
        ret = self._get_attr("objectSize")
        return ret

    @property
    def type_p(self):
        """Get FsObjType value for 'type'
        The object type. See <link to="FsObjType"/> for more.
        """
        ret = self._get_attr("type")
        return FsObjType(ret)

    @property
    def uid(self):
        """Get int value for 'UID'
        The user owning the filesystem object (st_uid).
        """
        ret = self._get_attr("UID")
        return ret

    @property
    def user_flags(self):
        """Get int value for 'userFlags'
        User flags (st_flags).
        """
        ret = self._get_attr("userFlags")
        return ret

    @property
    def user_name(self):
        """Get str value for 'userName'
        The user name.
        """
        ret = self._get_attr("userName")
        return ret


class IGuestFsObjInfo(IFsObjInfo):
    """
    Represents the guest implementation of the
      <link to="IFsObjInfo"/> object.
    """
    __uuid__ = 'd5cf678e-3484-4e4a-ac55-329e15462e18'
    __wsmap__ = 'managed'
    

class IGuest(Interface):
    """
    The IGuest interface represents information about the operating system
      running inside the virtual machine. Used in
      <link to="IConsole::guest"/>.

      IGuest provides information about the guest operating system, whether
      Guest Additions are installed and other OS-specific virtual machine
      properties.
    """
    __uuid__ = '1a1969c1-a583-4975-9810-1dd0f0e3a8ae'
    __wsmap__ = 'managed'
    
    @property
    def os_type_id(self):
        """Get str value for 'OSTypeId'
        Identifier of the Guest OS type as reported by the Guest
        Additions.
        You may use <link to="IVirtualBox::getGuestOSType"/> to obtain
        an IGuestOSType object representing details about the given
        Guest OS type.
        
          If Guest Additions are not installed, this value will be
          the same as <link to="IMachine::OSTypeId"/>.
        """
        ret = self._get_attr("OSTypeId")
        return ret

    @property
    def additions_run_level(self):
        """Get AdditionsRunLevelType value for 'additionsRunLevel'
        Current run level of the Guest Additions.
        """
        ret = self._get_attr("additionsRunLevel")
        return AdditionsRunLevelType(ret)

    @property
    def additions_version(self):
        """Get str value for 'additionsVersion'
        Version of the Guest Additions in the same format as
        <link to="IVirtualBox::version"/>.
        """
        ret = self._get_attr("additionsVersion")
        return ret

    @property
    def additions_revision(self):
        """Get int value for 'additionsRevision'
        The internal build revision number of the additions.

        See also <link to="IVirtualBox::revision"/>.
        """
        ret = self._get_attr("additionsRevision")
        return ret

    @property
    def facilities(self):
        """Get IAdditionsFacility value for 'facilities'
        Array of current known facilities. Only returns facilities where a status is known,
        e.g. facilities with an unknown status will not be returned.
        """
        ret = self._get_attr("facilities")
        return [IAdditionsFacility(a) for a in ret]

    @property
    def sessions(self):
        """Get IGuestSession value for 'sessions'
        Returns a collection of all opened guest sessions.
        """
        ret = self._get_attr("sessions")
        return [IGuestSession(a) for a in ret]

    @property
    def memory_balloon_size(self):
        """Get or set int value for 'memoryBalloonSize'
        Guest system memory balloon size in megabytes (transient property).
        """
        ret = self._get_attr("memoryBalloonSize")
        return ret

    @memory_balloon_size.setter
    def memory_balloon_size(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("memoryBalloonSize", value)

    @property
    def statistics_update_interval(self):
        """Get or set int value for 'statisticsUpdateInterval'
        Interval to update guest statistics in seconds.
        """
        ret = self._get_attr("statisticsUpdateInterval")
        return ret

    @statistics_update_interval.setter
    def statistics_update_interval(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("statisticsUpdateInterval", value)

    def internal_get_statistics(self):
        """Internal method; do not use as it might change at any time.

        out cpu_user of type int
            Percentage of processor time spent in user mode as seen by the guest.

        out cpu_kernel of type int
            Percentage of processor time spent in kernel mode as seen by the guest.

        out cpu_idle of type int
            Percentage of processor time spent idling as seen by the guest.

        out mem_total of type int
            Total amount of physical guest RAM.

        out mem_free of type int
            Free amount of physical guest RAM.

        out mem_balloon of type int
            Amount of ballooned physical guest RAM.

        out mem_shared of type int
            Amount of shared physical guest RAM.

        out mem_cache of type int
            Total amount of guest (disk) cache memory.

        out paged_total of type int
            Total amount of space in the page file.

        out mem_alloc_total of type int
            Total amount of memory allocated by the hypervisor.

        out mem_free_total of type int
            Total amount of free memory available in the hypervisor.

        out mem_balloon_total of type int
            Total amount of memory ballooned by the hypervisor.

        out mem_shared_total of type int
            Total amount of shared memory in the hypervisor.

        """
        (cpu_user, cpu_kernel, cpu_idle, mem_total, mem_free, mem_balloon, mem_shared, mem_cache, paged_total, mem_alloc_total, mem_free_total, mem_balloon_total, mem_shared_total) = self._call("internalGetStatistics")
        return (cpu_user, cpu_kernel, cpu_idle, mem_total, mem_free, mem_balloon, mem_shared, mem_cache, paged_total, mem_alloc_total, mem_free_total, mem_balloon_total, mem_shared_total)

    def get_facility_status(self, facility):
        """Get the current status of a Guest Additions facility.

        in facility of type AdditionsFacilityType
            Facility to check status for.

        out timestamp of type int
            Timestamp (in ms) of last status update seen by the host.

        return status of type AdditionsFacilityStatus
            The current (latest) facility status.

        """
        if not isinstance(facility, AdditionsFacilityType):
            raise TypeError("facility can only be an instance of type AdditionsFacilityType")
        (timestamp, status) = self._call("getFacilityStatus",
                     in_p=[facility])
        status = AdditionsFacilityStatus(status)
        return (timestamp, status)

    def get_additions_status(self, level):
        """Retrieve the current status of a certain Guest Additions run level.

        in level of type AdditionsRunLevelType
            Status level to check

        return active of type bool
            Flag whether the status level has been reached or not

        raises VBOX_E_NOT_SUPPORTED
            Wrong status level specified.
        
        """
        if not isinstance(level, AdditionsRunLevelType):
            raise TypeError("level can only be an instance of type AdditionsRunLevelType")
        active = self._call("getAdditionsStatus",
                     in_p=[level])
        return active

    def set_credentials(self, user_name, password, domain, allow_interactive_logon):
        """Store login credentials that can be queried by guest operating
        systems with Additions installed. The credentials are transient
        to the session and the guest may also choose to erase them. Note
        that the caller cannot determine whether the guest operating system
        has queried or made use of the credentials.

        in user_name of type str
            User name string, can be empty

        in password of type str
            Password string, can be empty

        in domain of type str
            Domain name (guest logon scheme specific), can be empty

        in allow_interactive_logon of type bool
            Flag whether the guest should alternatively allow the user to
          interactively specify different credentials. This flag might
          not be supported by all versions of the Additions.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if type(user_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(password) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(domain) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(allow_interactive_logon, bool):
            raise TypeError("allow_interactive_logon can only be an instance of type bool")
        self._call("setCredentials",
                     in_p=[user_name, password, domain, allow_interactive_logon])

    def drag_hg_enter(self, screen_id, y, x, default_action, allowed_actions, formats):
        """Informs the guest about a Drag and Drop enter event.

        This is used in Host - Guest direction.

        in screen_id of type int
            The screen id where the Drag and Drop event occured.

        in y of type int
            y-position of the event.

        in x of type int
            x-position of the event.

        in default_action of type DragAndDropAction
            The default action to use.

        in allowed_actions of type DragAndDropAction
            The actions which are allowed.

        in formats of type str
            The supported mime types.

        return result_action of type DragAndDropAction
            The resulting action of this event.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(default_action, DragAndDropAction):
            raise TypeError("default_action can only be an instance of type DragAndDropAction")
        if not isinstance(allowed_actions, list):
            raise TypeError("allowed_actions can only be an instance of type list")
        for a in allowed_actions[:10]:
            if not isinstance(a, DragAndDropAction):
                raise TypeError(\
                        "array can only contain objects of type DragAndDropAction")
        if not isinstance(formats, list):
            raise TypeError("formats can only be an instance of type list")
        for a in formats[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        result_action = self._call("dragHGEnter",
                     in_p=[screen_id, y, x, default_action, allowed_actions, formats])
        result_action = DragAndDropAction(result_action)
        return result_action

    def drag_hg_move(self, screen_id, x, y, default_action, allowed_actions, formats):
        """Informs the guest about a Drag and Drop move event.

        This is used in Host - Guest direction.

        in screen_id of type int
            The screen id where the Drag and Drop event occured.

        in x of type int
            x-position of the event.

        in y of type int
            y-position of the event.

        in default_action of type DragAndDropAction
            The default action to use.

        in allowed_actions of type DragAndDropAction
            The actions which are allowed.

        in formats of type str
            The supported mime types.

        return result_action of type DragAndDropAction
            The resulting action of this event.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        if not isinstance(default_action, DragAndDropAction):
            raise TypeError("default_action can only be an instance of type DragAndDropAction")
        if not isinstance(allowed_actions, list):
            raise TypeError("allowed_actions can only be an instance of type list")
        for a in allowed_actions[:10]:
            if not isinstance(a, DragAndDropAction):
                raise TypeError(\
                        "array can only contain objects of type DragAndDropAction")
        if not isinstance(formats, list):
            raise TypeError("formats can only be an instance of type list")
        for a in formats[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        result_action = self._call("dragHGMove",
                     in_p=[screen_id, x, y, default_action, allowed_actions, formats])
        result_action = DragAndDropAction(result_action)
        return result_action

    def drag_hg_leave(self, screen_id):
        """Informs the guest about a Drag and Drop leave event.

        This is used in Host - Guest direction.

        in screen_id of type int
            The screen id where the Drag and Drop event occured.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        self._call("dragHGLeave",
                     in_p=[screen_id])

    def drag_hg_drop(self, screen_id, x, y, default_action, allowed_actions, formats):
        """Informs the guest about a drop event.

        This is used in Host - Guest direction.

        in screen_id of type int
            The screen id where the Drag and Drop event occured.

        in x of type int
            x-position of the event.

        in y of type int
            y-position of the event.

        in default_action of type DragAndDropAction
            The default action to use.

        in allowed_actions of type DragAndDropAction
            The actions which are allowed.

        in formats of type str
            The supported mime types.

        out format_p of type str
            The resulting format of this event.

        return result_action of type DragAndDropAction
            The resulting action of this event.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        if not isinstance(default_action, DragAndDropAction):
            raise TypeError("default_action can only be an instance of type DragAndDropAction")
        if not isinstance(allowed_actions, list):
            raise TypeError("allowed_actions can only be an instance of type list")
        for a in allowed_actions[:10]:
            if not isinstance(a, DragAndDropAction):
                raise TypeError(\
                        "array can only contain objects of type DragAndDropAction")
        if not isinstance(formats, list):
            raise TypeError("formats can only be an instance of type list")
        for a in formats[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        (format_p, result_action) = self._call("dragHGDrop",
                     in_p=[screen_id, x, y, default_action, allowed_actions, formats])
        result_action = DragAndDropAction(result_action)
        return (format_p, result_action)

    def drag_hg_put_data(self, screen_id, format_p, data):
        """Informs the guest about a drop data event.

        This is used in Host - Guest direction.

        in screen_id of type int
            The screen id where the Drag and Drop event occured.

        in format_p of type str
            The mime type the data is in.

        in data of type str
            The actual data.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if type(format_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(data, list):
            raise TypeError("data can only be an instance of type list")
        for a in data[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        progress = self._call("dragHGPutData",
                     in_p=[screen_id, format_p, data])
        progress = IProgress(progress)
        return progress

    def drag_gh_pending(self, screen_id):
        """Ask the guest if there is any Drag and Drop operation pending in the guest.

        If no Drag and Drop operation is pending currently, Ignore is returned.

        This is used in Guest - Host direction.

        in screen_id of type int
            The screen id where the Drag and Drop event occured.

        out formats of type str
            On return the supported mime types.

        out allowed_actions of type DragAndDropAction
            On return the actions which are allowed.

        return default_action of type DragAndDropAction
            On return the default action to use.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (formats, allowed_actions, default_action) = self._call("dragGHPending",
                     in_p=[screen_id])
        allowed_actions = [DragAndDropAction(a) for a in allowed_actions]
        default_action = DragAndDropAction(default_action)
        return (formats, allowed_actions, default_action)

    def drag_gh_dropped(self, format_p, action):
        """Informs the guest that a drop event occured for a pending Drag and Drop event.

        This is used in Guest - Host direction.

        in format_p of type str
            The mime type the data must be in.

        in action of type DragAndDropAction
            The action to use.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        if type(format_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(action, DragAndDropAction):
            raise TypeError("action can only be an instance of type DragAndDropAction")
        progress = self._call("dragGHDropped",
                     in_p=[format_p, action])
        progress = IProgress(progress)
        return progress

    def drag_gh_get_data(self):
        """Fetch the data of a previously Drag and Drop event from the guest.

        This is used in Guest - Host direction.

        return data of type str
            The actual data.

        raises VBOX_E_VM_ERROR
            VMM device is not available.
        
        """
        data = self._call("dragGHGetData")
        return data

    def create_session(self, user, password, domain, session_name):
        """Creates a new guest session for controlling the guest.

        A guest session represents one impersonated user account on the guest, so
        every operation will use the same credentials specified when creating
        the session object via <link to="IGuest::createSession"/>. Anonymous
        sessions, that is, sessions without specifying a valid
        user account on the guest are not allowed due to security reasons.

        There can be a maximum of 32 sessions at once per VM. Each session keeps
        track of its started guest processes, opened guest files or guest directories.
        To work on guest files or directories a guest session offers methods to open
        or create such objects (see <link to="IGuestSession::fileOpen"/> or
        <link to="IGuestSession::directoryOpen"/> for example).

        When done with either of these objects, including the guest session itself,
        use the appropriate close() method to let the object do its cleanup work.

        Every guest session has its own environment variable block which gets
        automatically applied when starting a new guest process via
        <link to="IGuestSession::processCreate"/> or <link to="IGuestSession::processCreateEx"/>.
        To override (or unset) certain environment variables already set by the
        guest session, one can specify a per-process environment block when using
        one of the both above mentioned process creation calls.

        Closing a session via <link to="IGuestSession::close"/> will try to close
        all the mentioned objects above unless these objects are still used by
        a client.

        in user of type str
            User name this session will be using to control the guest; has to exist
          and have the appropriate rights to execute programs in the VM. Must not
          be empty.

        in password of type str
            Password of the user account to be used. Empty passwords are allowed.

        in domain of type str
            Domain name of the user account to be used if the guest is part of
          a domain. Optional. This feature is not implemented yet.

        in session_name of type str
            The session's friendly name. Optional, can be empty.

        return guest_session of type IGuestSession
            The newly created session object.

        """
        if type(user) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(password) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(domain) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(session_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        guest_session = self._call("createSession",
                     in_p=[user, password, domain, session_name])
        guest_session = IGuestSession(guest_session)
        return guest_session

    def find_session(self, session_name):
        """Finds guest sessions by their friendly name and returns an interface
        array with all found guest sessions.

        in session_name of type str
            The session's friendly name to find. Wildcards like ? and * are allowed.

        return sessions of type IGuestSession
            Array with all guest sessions found matching the name specified.

        """
        if type(session_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        sessions = self._call("findSession",
                     in_p=[session_name])
        sessions = [IGuestSession(a) for a in sessions]
        return sessions

    def update_guest_additions(self, source, arguments, flags):
        """Automatically updates already installed Guest Additions in a VM.

        At the moment only Windows guests are supported.

        Because the VirtualBox Guest Additions drivers are not WHQL-certified
        yet there might be warning dialogs during the actual Guest Additions
        update. These need to be confirmed manually in order to continue the
        installation process. This applies to Windows 2000 and Windows XP guests
        and therefore these guests can't be updated in a fully automated fashion
        without user interaction. However, to start a Guest Additions update for
        the mentioned Windows versions anyway, the flag
        AdditionsUpdateFlag_WaitForUpdateStartOnly can be specified. See
        <link to="AdditionsUpdateFlag"/> for more information.

        in source of type str
            Path to the Guest Additions .ISO file to use for the update.

        in arguments of type str
            Optional command line arguments to use for the Guest Additions
          installer. Useful for retrofitting features which weren't installed
          before on the guest.

        in flags of type AdditionsUpdateFlag
            <link to="AdditionsUpdateFlag"/> flags.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_NOT_SUPPORTED
            Guest OS is not supported for automated Guest Additions updates or the
          already installed Guest Additions are not ready yet.
        
        raises VBOX_E_IPRT_ERROR
            Error while updating.
        
        """
        if type(source) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(arguments, list):
            raise TypeError("arguments can only be an instance of type list")
        for a in arguments[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(flags, list):
            raise TypeError("flags can only be an instance of type list")
        for a in flags[:10]:
            if not isinstance(a, AdditionsUpdateFlag):
                raise TypeError(\
                        "array can only contain objects of type AdditionsUpdateFlag")
        progress = self._call("updateGuestAdditions",
                     in_p=[source, arguments, flags])
        progress = IProgress(progress)
        return progress


class IProgress(Interface):
    """
    The IProgress interface is used to track and control
        asynchronous tasks within VirtualBox.

        An instance of this is returned every time VirtualBox starts
        an asynchronous task (in other words, a separate thread) which
        continues to run after a method call returns. For example,
        <link to="IConsole::saveState"/>, which saves the state of
        a running virtual machine, can take a long time to complete.
        To be able to display a progress bar, a user interface such as
        the VirtualBox graphical user interface can use the IProgress
        object returned by that method.

        Note that IProgress is a "read-only" interface in the sense
        that only the VirtualBox internals behind the Main API can
        create and manipulate progress objects, whereas client code
        can only use the IProgress object to monitor a task's
        progress and, if <link to="#cancelable"/> is @c true,
        cancel the task by calling <link to="#cancel"/>.

        A task represented by IProgress consists of either one or
        several sub-operations that run sequentially, one by one (see
        <link to="#operation"/> and <link to="#operationCount"/>).
        Every operation is identified by a number (starting from 0)
        and has a separate description.

        You can find the individual percentage of completion of the current
        operation in <link to="#operationPercent"/> and the
        percentage of completion of the task as a whole
        in <link to="#percent"/>.

        Similarly, you can wait for the completion of a particular
        operation via <link to="#waitForOperationCompletion"/> or
        for the completion of the whole task via
        <link to="#waitForCompletion"/>.
    """
    __uuid__ = 'c20238e4-3221-4d3f-8891-81ce92d9f913'
    __wsmap__ = 'managed'
    
    @property
    def id_p(self):
        """Get str value for 'id'
        ID of the task.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def description(self):
        """Get str value for 'description'
        Description of the task.
        """
        ret = self._get_attr("description")
        return ret

    @property
    def initiator(self):
        """Get Interface value for 'initiator'
        Initiator of the task.
        """
        ret = self._get_attr("initiator")
        return Interface(ret)

    @property
    def cancelable(self):
        """Get bool value for 'cancelable'
        Whether the task can be interrupted.
        """
        ret = self._get_attr("cancelable")
        return ret

    @property
    def percent(self):
        """Get int value for 'percent'
        Current progress value of the task as a whole, in percent.
        This value depends on how many operations are already complete.
        Returns 100 if <link to="#completed"/> is @c true.
        """
        ret = self._get_attr("percent")
        return ret

    @property
    def time_remaining(self):
        """Get int value for 'timeRemaining'
        Estimated remaining time until the task completes, in
            seconds. Returns 0 once the task has completed; returns -1
            if the remaining time cannot be computed, in particular if
            the current progress is 0.

            Even if a value is returned, the estimate will be unreliable
            for low progress values. It will become more reliable as the
            task progresses; it is not recommended to display an ETA
            before at least 20% of a task have completed.
        """
        ret = self._get_attr("timeRemaining")
        return ret

    @property
    def completed(self):
        """Get bool value for 'completed'
        Whether the task has been completed.
        """
        ret = self._get_attr("completed")
        return ret

    @property
    def canceled(self):
        """Get bool value for 'canceled'
        Whether the task has been canceled.
        """
        ret = self._get_attr("canceled")
        return ret

    @property
    def result_code(self):
        """Get int value for 'resultCode'
        Result code of the progress task.
        Valid only if <link to="#completed"/> is @c true.
        """
        ret = self._get_attr("resultCode")
        return ret

    @property
    def error_info(self):
        """Get IVirtualBoxErrorInfo value for 'errorInfo'
        Extended information about the unsuccessful result of the
        progress operation. May be @c null if no extended information
        is available.
        Valid only if <link to="#completed"/> is @c true and
        <link to="#resultCode"/> indicates a failure.
        """
        ret = self._get_attr("errorInfo")
        return IVirtualBoxErrorInfo(ret)

    @property
    def operation_count(self):
        """Get int value for 'operationCount'
        Number of sub-operations this task is divided into.
          Every task consists of at least one suboperation.
        """
        ret = self._get_attr("operationCount")
        return ret

    @property
    def operation(self):
        """Get int value for 'operation'
        Number of the sub-operation being currently executed.
        """
        ret = self._get_attr("operation")
        return ret

    @property
    def operation_description(self):
        """Get str value for 'operationDescription'
        Description of the sub-operation being currently executed.
        """
        ret = self._get_attr("operationDescription")
        return ret

    @property
    def operation_percent(self):
        """Get int value for 'operationPercent'
        Progress value of the current sub-operation only, in percent.
        """
        ret = self._get_attr("operationPercent")
        return ret

    @property
    def operation_weight(self):
        """Get int value for 'operationWeight'
        Weight value of the current sub-operation only.
        """
        ret = self._get_attr("operationWeight")
        return ret

    @property
    def timeout(self):
        """Get or set int value for 'timeout'
        When non-zero, this specifies the number of milliseconds after which
          the operation will automatically be canceled. This can only be set on
          cancelable objects.
        """
        ret = self._get_attr("timeout")
        return ret

    @timeout.setter
    def timeout(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("timeout", value)

    def set_current_operation_progress(self, percent):
        """Internal method, not to be called externally.

        in percent of type int

        """
        if not isinstance(percent, int):
            raise TypeError("percent can only be an instance of type int")
        self._call("setCurrentOperationProgress",
                     in_p=[percent])

    def set_next_operation(self, next_operation_description, next_operations_weight):
        """Internal method, not to be called externally.

        in next_operation_description of type str

        in next_operations_weight of type int

        """
        if type(next_operation_description) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(next_operations_weight, int):
            raise TypeError("next_operations_weight can only be an instance of type int")
        self._call("setNextOperation",
                     in_p=[next_operation_description, next_operations_weight])

    def wait_for_completion(self, timeout):
        """Waits until the task is done (including all sub-operations)
          with a given timeout in milliseconds; specify -1 for an indefinite wait.

          Note that the VirtualBox/XPCOM/COM/native event queues of the calling
          thread are not processed while waiting. Neglecting event queues may
          have dire consequences (degrade performance, resource hogs,
          deadlocks, etc.), this is specially so for the main thread on
          platforms using XPCOM. Callers are adviced wait for short periods
          and service their event queues between calls, or to create a worker
          thread to do the waiting.

        in timeout of type int
            Maximum time in milliseconds to wait or -1 to wait indefinitely.

        raises VBOX_E_IPRT_ERROR
            Failed to wait for task completion.
        
        """
        if not isinstance(timeout, int):
            raise TypeError("timeout can only be an instance of type int")
        self._call("waitForCompletion",
                     in_p=[timeout])

    def wait_for_operation_completion(self, operation, timeout):
        """Waits until the given operation is done with a given timeout in
          milliseconds; specify -1 for an indefinite wait.

          See <link to="#waitForCompletion"> for event queue considerations.</link>

        in operation of type int
            Number of the operation to wait for.
          Must be less than <link to="#operationCount"/>.

        in timeout of type int
            Maximum time in milliseconds to wait or -1 to wait indefinitely.

        raises VBOX_E_IPRT_ERROR
            Failed to wait for operation completion.
        
        """
        if not isinstance(operation, int):
            raise TypeError("operation can only be an instance of type int")
        if not isinstance(timeout, int):
            raise TypeError("timeout can only be an instance of type int")
        self._call("waitForOperationCompletion",
                     in_p=[operation, timeout])

    def wait_for_async_progress_completion(self, p_progress_async):
        """Waits until the other task is completed (including all
          sub-operations) and forward all changes from the other progress to
          this progress. This means sub-operation number, description, percent
          and so on.

          You have to take care on setting up at least the same count on
          sub-operations in this progress object like there are in the other
          progress object.

          If the other progress object supports cancel and this object gets any
          cancel request (when here enabled as well), it will be forwarded to
          the other progress object.

          If there is an error in the other progress, this error isn't
          automatically transfered to this progress object. So you have to
          check any operation error within the other progress object, after
          this method returns.

        in p_progress_async of type IProgress
            The progress object of the asynchrony process.

        """
        if not isinstance(p_progress_async, IProgress):
            raise TypeError("p_progress_async can only be an instance of type IProgress")
        self._call("waitForAsyncProgressCompletion",
                     in_p=[p_progress_async])

    def cancel(self):
        """Cancels the task.
        
          If <link to="#cancelable"/> is @c false, then this method will fail.

        raises VBOX_E_INVALID_OBJECT_STATE
            Operation cannot be canceled.
        
        """
        self._call("cancel")


class ISnapshot(Interface):
    """
    The ISnapshot interface represents a snapshot of the virtual
      machine.

      Together with the differencing media that are created
      when a snapshot is taken, a machine can be brought back to
      the exact state it was in when the snapshot was taken.

      The ISnapshot interface has no methods, only attributes; snapshots
      are controlled through methods of the <link to="IConsole"/> interface
      which also manage the media associated with the snapshot.
      The following operations exist:

      
          <link to="IConsole::takeSnapshot"/> creates a new snapshot
              by creating new, empty differencing images for the machine's
              media and saving the VM settings and (if the VM is running)
              the current VM state in the snapshot.

              The differencing images will then receive all data written to
              the machine's media, while their parent (base) images
              remain unmodified after the snapshot has been taken (see
              <link to="IMedium"/> for details about differencing images).
              This simplifies restoring a machine to the state of a snapshot:
              only the differencing images need to be deleted.

              The current machine state is not changed by taking a snapshot
              except that <link to="IMachine::currentSnapshot"/> is set to
              the newly created snapshot, which is also added to the machine's
              snapshots tree.
          

          <link to="IConsole::restoreSnapshot"/> resets a machine to
              the state of a previous snapshot by deleting the differencing
              image of each of the machine's media and setting the machine's
              settings and state to the state that was saved in the snapshot (if any).

              This destroys the machine's current state. After calling this,
              <link to="IMachine::currentSnapshot"/> points to the snapshot
              that was restored.
          

          <link to="IConsole::deleteSnapshot"/> deletes a snapshot
              without affecting the current machine state.

              This does not change the current machine state, but instead frees the
              resources allocated when the snapshot was taken: the settings and machine
              state file are deleted (if any), and the snapshot's differencing image for
              each of the machine's media gets merged with its parent image.

              Neither the current machine state nor other snapshots are affected
              by this operation, except that parent media will be modified
              to contain the disk data associated with the snapshot being deleted.

              When deleting the current snapshot, the <link to="IMachine::currentSnapshot"/>
              attribute is set to the current snapshot's parent or @c null if it
              has no parent. Otherwise the attribute is unchanged.
          
      

      Each snapshot contains a copy of virtual machine's settings (hardware
      configuration etc.). This copy is contained in an immutable (read-only)
      instance of <link to="IMachine"/> which is available from the snapshot's
      <link to="#machine"/> attribute. When restoring the snapshot, these
      settings are copied back to the original machine.

      In addition, if the machine was running when the
      snapshot was taken (<link to="IMachine::state"/> is <link to="MachineState_Running"/>),
      the current VM state is saved in the snapshot (similarly to what happens
      when a VM's state is saved). The snapshot is then said to be online
      because when restoring it, the VM will be running.

      If the machine was in <link to="MachineState_Saved">saved</link> saved,
      the snapshot receives a copy of the execution state file
      (<link to="IMachine::stateFilePath"/>).

      Otherwise, if the machine was not running (<link to="MachineState_PoweredOff"/>
      or <link to="MachineState_Aborted"/>), the snapshot is offline;
      it then contains a so-called "zero execution state", representing a
      machine that is powered off.
    """
    __uuid__ = '0472823b-c6e7-472a-8e9f-d732e86b8463'
    __wsmap__ = 'managed'
    
    @property
    def id_p(self):
        """Get str value for 'id'
        UUID of the snapshot.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def name(self):
        """Get or set str value for 'name'
        Short name of the snapshot.
      Setting this attribute causes <link to="IMachine::saveSettings"/> to
      be called implicitly.
        """
        ret = self._get_attr("name")
        return ret

    @name.setter
    def name(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("name", value)

    @property
    def description(self):
        """Get or set str value for 'description'
        Optional description of the snapshot.
      Setting this attribute causes <link to="IMachine::saveSettings"/> to
      be called implicitly.
        """
        ret = self._get_attr("description")
        return ret

    @description.setter
    def description(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("description", value)

    @property
    def time_stamp(self):
        """Get int value for 'timeStamp'
        Time stamp of the snapshot, in milliseconds since 1970-01-01 UTC.
        """
        ret = self._get_attr("timeStamp")
        return ret

    @property
    def online(self):
        """Get bool value for 'online'
        @c true if this snapshot is an online snapshot and @c false otherwise.

          When this attribute is @c true, the
          <link to="IMachine::stateFilePath"/> attribute of the
          <link to="#machine"/> object associated with this snapshot
          will point to the saved state file. Otherwise, it will be
          an empty string.
        """
        ret = self._get_attr("online")
        return ret

    @property
    def machine(self):
        """Get IMachine value for 'machine'
        Virtual machine this snapshot is taken on. This object
        stores all settings the machine had when taking this snapshot.
        
          The returned machine object is immutable, i.e. no
          any settings can be changed.
        """
        ret = self._get_attr("machine")
        return IMachine(ret)

    @property
    def parent(self):
        """Get ISnapshot value for 'parent'
        Parent snapshot (a snapshot this one is based on), or
        @c null if the snapshot has no parent (i.e. is the first snapshot).
        """
        ret = self._get_attr("parent")
        return ISnapshot(ret)

    @property
    def children(self):
        """Get ISnapshot value for 'children'
        Child snapshots (all snapshots having this one as a parent).
        By inspecting this attribute starting with a machine's root snapshot
        (which can be obtained by calling <link to="IMachine::findSnapshot"/>
        with a @c null UUID), a machine's snapshots tree can be iterated over.
        """
        ret = self._get_attr("children")
        return [ISnapshot(a) for a in ret]

    def get_children_count(self):
        """Returns the number of direct childrens of this snapshot.

        return children_count of type int

        """
        children_count = self._call("getChildrenCount")
        return children_count


class IMediumAttachment(Interface):
    """
    The IMediumAttachment interface links storage media to virtual machines.
      For each medium (<link to="IMedium"/>) which has been attached to a
      storage controller (<link to="IStorageController"/>) of a machine
      (<link to="IMachine"/>) via the <link to="IMachine::attachDevice"/>
      method, one instance of IMediumAttachment is added to the machine's
      <link to="IMachine::mediumAttachments"/> array attribute.

      Each medium attachment specifies the storage controller as well as a
      port and device number and the IMedium instance representing a virtual
      hard disk or floppy or DVD image.

      For removable media (DVDs or floppies), there are two additional
      options. For one, the IMedium instance can be @c null to represent
      an empty drive with no media inserted (see <link to="IMachine::mountMedium"/>);
      secondly, the medium can be one of the pseudo-media for host drives
      listed in <link to="IHost::DVDDrives"/> or <link to="IHost::floppyDrives"/>.

      Attaching Hard Disks

      Hard disks are attached to virtual machines using the
      <link to="IMachine::attachDevice"/> method and detached using the
      <link to="IMachine::detachDevice"/> method. Depending on a medium's
      type (see <link to="IMedium::type"/>), hard disks are attached either
      directly or indirectly.

      When a hard disk is being attached directly, it is associated with the
      virtual machine and used for hard disk operations when the machine is
      running. When a hard disk is being attached indirectly, a new differencing
      hard disk linked to it is implicitly created and this differencing hard
      disk is associated with the machine and used for hard disk operations.
      This also means that if <link to="IMachine::attachDevice"/> performs
      a direct attachment then the same hard disk will be returned in response
      to the subsequent <link to="IMachine::getMedium"/> call; however if
      an indirect attachment is performed then
      <link to="IMachine::getMedium"/> will return the implicitly created
      differencing hard disk, not the original one passed to <link to="IMachine::attachDevice"/>. In detail:

      
        Normal base hard disks that do not have children (i.e.
            differencing hard disks linked to them) and that are not already
            attached to virtual machines in snapshots are attached directly.
            Otherwise, they are attached indirectly because having
            dependent children or being part of the snapshot makes it impossible
            to modify hard disk contents without breaking the integrity of the
            dependent party. The <link to="IMedium::readOnly"/> attribute allows to
            quickly determine the kind of the attachment for the given hard
            disk. Note that if a normal base hard disk is to be indirectly
            attached to a virtual machine with snapshots then a special
            procedure called smart attachment is performed (see below).
        Normal differencing hard disks are like normal base hard disks:
            they are attached directly if they do not have children and are
            not attached to virtual machines in snapshots, and indirectly
            otherwise. Note that the smart attachment procedure is never performed
            for differencing hard disks.
        Immutable hard disks are always attached indirectly because
            they are designed to be non-writable. If an immutable hard disk is
            attached to a virtual machine with snapshots then a special
            procedure called smart attachment is performed (see below).
        Writethrough hard disks are always attached directly,
            also as designed. This also means that writethrough hard disks cannot
            have other hard disks linked to them at all.
        Shareable hard disks are always attached directly,
            also as designed. This also means that shareable hard disks cannot
            have other hard disks linked to them at all. They behave almost
            like writethrough hard disks, except that shareable hard disks can
            be attached to several virtual machines which are running, allowing
            concurrent accesses. You need special cluster software running in
            the virtual machines to make use of such disks.
      

      Note that the same hard disk, regardless of its type, may be attached to
      more than one virtual machine at a time. In this case, the machine that is
      started first gains exclusive access to the hard disk and attempts to
      start other machines having this hard disk attached will fail until the
      first machine is powered down.

      Detaching hard disks is performed in a deferred fashion. This means
      that the given hard disk remains associated with the given machine after a
      successful <link to="IMachine::detachDevice"/> call until
      <link to="IMachine::saveSettings"/> is called to save all changes to
      machine settings to disk. This deferring is necessary to guarantee that
      the hard disk configuration may be restored at any time by a call to
      <link to="IMachine::discardSettings"/> before the settings
      are saved (committed).

      Note that if <link to="IMachine::discardSettings"/> is called after
      indirectly attaching some hard disks to the machine but before a call to
      <link to="IMachine::saveSettings"/> is made, it will implicitly delete
      all differencing hard disks implicitly created by
      <link to="IMachine::attachDevice"/> for these indirect attachments.
      Such implicitly created hard disks will also be immediately deleted when
      detached explicitly using the <link to="IMachine::detachDevice"/>
      call if it is made before <link to="IMachine::saveSettings"/>. This
      implicit deletion is safe because newly created differencing hard
      disks do not contain any user data.

      However, keep in mind that detaching differencing hard disks that were
      implicitly created by <link to="IMachine::attachDevice"/>
      before the last <link to="IMachine::saveSettings"/> call will
      not implicitly delete them as they may already contain some data
      (for example, as a result of virtual machine execution). If these hard
      disks are no more necessary, the caller can always delete them explicitly
      using <link to="IMedium::deleteStorage"/> after they are actually de-associated
      from this machine by the <link to="IMachine::saveSettings"/> call.

      Smart Attachment

      When normal base or immutable hard disks are indirectly attached to a
      virtual machine then some additional steps are performed to make sure the
      virtual machine will have the most recent "view" of the hard disk being
      attached. These steps include walking through the machine's snapshots
      starting from the current one and going through ancestors up to the first
      snapshot. Hard disks attached to the virtual machine in all
      of the encountered snapshots are checked whether they are descendants of
      the given normal base or immutable hard disk. The first found child (which
      is the differencing hard disk) will be used instead of the normal base or
      immutable hard disk as a parent for creating a new differencing hard disk
      that will be actually attached to the machine. And only if no descendants
      are found or if the virtual machine does not have any snapshots then the
      normal base or immutable hard disk will be used itself as a parent for
      this differencing hard disk.

      It is easier to explain what smart attachment does using the
      following example:
      
BEFORE attaching B.vdi:       AFTER attaching B.vdi:

Snapshot 1 (B.vdi)            Snapshot 1 (B.vdi)
 Snapshot 2 (D1->B.vdi)        Snapshot 2 (D1->B.vdi)
  Snapshot 3 (D2->D1.vdi)       Snapshot 3 (D2->D1.vdi)
   Snapshot 4 (none)             Snapshot 4 (none)
    CurState   (none)             CurState   (D3->D2.vdi)

                              NOT
                                 ...
                                  CurState   (D3->B.vdi)
      
      The first column is the virtual machine configuration before the base hard
      disk B.vdi is attached, the second column shows the machine after
      this hard disk is attached. Constructs like D1->B.vdi and similar
      mean that the hard disk that is actually attached to the machine is a
      differencing hard disk, D1.vdi, which is linked to (based on)
      another hard disk, B.vdi.

      As we can see from the example, the hard disk B.vdi was detached
      from the machine before taking Snapshot 4. Later, after Snapshot 4 was
      taken, the user decides to attach B.vdi again. B.vdi has
      dependent child hard disks (D1.vdi, D2.vdi), therefore
      it cannot be attached directly and needs an indirect attachment (i.e.
      implicit creation of a new differencing hard disk). Due to the smart
      attachment procedure, the new differencing hard disk
      (D3.vdi) will be based on D2.vdi, not on
      B.vdi itself, since D2.vdi is the most recent view of
      B.vdi existing for this snapshot branch of the given virtual
      machine.

      Note that if there is more than one descendant hard disk of the given base
      hard disk found in a snapshot, and there is an exact device, channel and
      bus match, then this exact match will be used. Otherwise, the youngest
      descendant will be picked up.

      There is one more important aspect of the smart attachment procedure which
      is not related to snapshots at all. Before walking through the snapshots
      as described above, the backup copy of the current list of hard disk
      attachment is searched for descendants. This backup copy is created when
      the hard disk configuration is changed for the first time after the last
      <link to="IMachine::saveSettings"/> call and used by
      <link to="IMachine::discardSettings"/> to undo the recent hard disk
      changes. When such a descendant is found in this backup copy, it will be
      simply re-attached back, without creating a new differencing hard disk for
      it. This optimization is necessary to make it possible to re-attach the
      base or immutable hard disk to a different bus, channel or device slot
      without losing the contents of the differencing hard disk actually
      attached to the machine in place of it.
    """
    __uuid__ = '5ee464d6-0613-4331-b154-7ce12170ef9f'
    __wsmap__ = 'struct'
    
    @property
    def medium(self):
        """Get IMedium value for 'medium'
        Medium object associated with this attachment; it
        can be @c null for removable devices.
        """
        ret = self._get_attr("medium")
        return IMedium(ret)

    @property
    def controller(self):
        """Get str value for 'controller'
        Name of the storage controller of this attachment; this
        refers to one of the controllers in <link to="IMachine::storageControllers"/>
        by name.
        """
        ret = self._get_attr("controller")
        return ret

    @property
    def port(self):
        """Get int value for 'port'
        Port number of this attachment.
        See <link to="IMachine::attachDevice"/> for the meaning of this value for the different controller types.
        """
        ret = self._get_attr("port")
        return ret

    @property
    def device(self):
        """Get int value for 'device'
        Device slot number of this attachment.
        See <link to="IMachine::attachDevice"/> for the meaning of this value for the different controller types.
        """
        ret = self._get_attr("device")
        return ret

    @property
    def type_p(self):
        """Get DeviceType value for 'type'
        Device type of this attachment.
        """
        ret = self._get_attr("type")
        return DeviceType(ret)

    @property
    def passthrough(self):
        """Get bool value for 'passthrough'
        Pass I/O requests through to a device on the host.
        """
        ret = self._get_attr("passthrough")
        return ret

    @property
    def temporary_eject(self):
        """Get bool value for 'temporaryEject'
        Whether guest-triggered eject results in unmounting the medium.
        """
        ret = self._get_attr("temporaryEject")
        return ret

    @property
    def is_ejected(self):
        """Get bool value for 'isEjected'
        Signals that the removable medium has been ejected. This is not
        necessarily equivalent to having a @c null medium association.
        """
        ret = self._get_attr("isEjected")
        return ret

    @property
    def non_rotational(self):
        """Get bool value for 'nonRotational'
        Whether the associated medium is non-rotational.
        """
        ret = self._get_attr("nonRotational")
        return ret

    @property
    def discard(self):
        """Get bool value for 'discard'
        Whether the associated medium supports discarding unused blocks.
        """
        ret = self._get_attr("discard")
        return ret

    @property
    def bandwidth_group(self):
        """Get IBandwidthGroup value for 'bandwidthGroup'
        The bandwidth group this medium attachment is assigned to.
        """
        ret = self._get_attr("bandwidthGroup")
        return IBandwidthGroup(ret)


class IMedium(Interface):
    """
    The IMedium interface represents virtual storage for a machine's
      hard disks, CD/DVD or floppy drives. It will typically represent
      a disk image on the host, for example a VDI or VMDK file representing
      a virtual hard disk, or an ISO or RAW file representing virtual
      removable media, but can also point to a network location (e.g.
      for iSCSI targets).

      Instances of IMedium are connected to virtual machines by way of medium
      attachments, which link the storage medium to a particular device slot
      of a storage controller of the virtual machine.
      In the VirtualBox API, virtual storage is therefore always represented
      by the following chain of object links:

      
        <link to="IMachine::storageControllers"/> contains an array of
          storage controllers (IDE, SATA, SCSI, SAS or a floppy controller;
          these are instances of <link to="IStorageController"/>).
        <link to="IMachine::mediumAttachments"/> contains an array of
          medium attachments (instances of <link to="IMediumAttachment"/>
          created by <link to="IMachine::attachDevice"/>),
          each containing a storage controller from the above array, a
          port/device specification, and an instance of IMedium representing
          the medium storage (image file).

          For removable media, the storage medium is optional; a medium
          attachment with no medium represents a CD/DVD or floppy drive
          with no medium inserted. By contrast, hard disk attachments
          will always have an IMedium object attached.
        Each IMedium in turn points to a storage unit (such as a file
          on the host computer or a network resource) that holds actual
          data. This location is represented by the <link to="#location"/>
          attribute.
      

      Existing media are opened using <link to="IVirtualBox::openMedium"/>;
      new hard disk media can be created with the VirtualBox API using the
      <link to="IVirtualBox::createHardDisk"/> method. Differencing hard
      disks (see below) are usually implicitly created by VirtualBox as
      needed, but may also be created explicitly using <link to="#createDiffStorage"/>.
      VirtualBox cannot create CD/DVD or floppy images (ISO and RAW files); these
      should be created with external tools and then opened from within VirtualBox.

      Only for CD/DVDs and floppies, an IMedium instance can also represent a host
      drive. In that case the <link to="#id"/> attribute contains the UUID of
      one of the drives in <link to="IHost::DVDDrives"/> or <link to="IHost::floppyDrives"/>.

      Media registries

      When a medium has been opened or created using one of the aforementioned
      APIs, it becomes "known" to VirtualBox. Known media can be attached
      to virtual machines and re-found through <link to="IVirtualBox::openMedium"/>.
      They also appear in the global
      <link to="IVirtualBox::hardDisks"/>,
      <link to="IVirtualBox::DVDImages"/> and
      <link to="IVirtualBox::floppyImages"/> arrays.

      Prior to VirtualBox 4.0, opening a medium added it to a global media registry
      in the VirtualBox.xml file, which was shared between all machines and made
      transporting machines and their media from one host to another difficult.

      Starting with VirtualBox 4.0, media are only added to a registry when they are
      attached to a machine using <link to="IMachine::attachDevice"/>. For
      backwards compatibility, which registry a medium is added to depends on which
      VirtualBox version created a machine:

      
        If the medium has first been attached to a machine which was created by
          VirtualBox 4.0 or later, it is added to that machine's media registry in
          the machine XML settings file. This way all information about a machine's
          media attachments is contained in a single file and can be transported
          easily.
        For older media attachments (i.e. if the medium was first attached to a
          machine which was created with a VirtualBox version before 4.0), media
          continue to be registered in the global VirtualBox settings file, for
          backwards compatibility.
      

      See <link to="IVirtualBox::openMedium"/> for more information.

      Media are removed from media registries by the <link to="IMedium::close"/>,
      <link to="#deleteStorage"/> and <link to="#mergeTo"/> methods.

      Accessibility checks

      VirtualBox defers media accessibility checks until the <link to="#refreshState"/>
      method is called explicitly on a medium. This is done to make the VirtualBox object
      ready for serving requests as fast as possible and let the end-user
      application decide if it needs to check media accessibility right away or not.

      As a result, when VirtualBox starts up (e.g. the VirtualBox
      object gets created for the first time), all known media are in the
      "Inaccessible" state, but the value of the <link to="#lastAccessError"/>
      attribute is an empty string because no actual accessibility check has
      been made yet.

      After calling <link to="#refreshState"/>, a medium is considered
      accessible if its storage unit can be read. In that case, the
      <link to="#state"/> attribute has a value of "Created". If the storage
      unit cannot be read (for example, because it is located on a disconnected
      network resource, or was accidentally deleted outside VirtualBox),
      the medium is considered inaccessible, which is indicated by the
      "Inaccessible" state. The exact reason why the medium is inaccessible can be
      obtained by reading the <link to="#lastAccessError"/> attribute.

      Medium types

      There are five types of medium behavior which are stored in the
      <link to="#type"/> attribute (see <link to="MediumType"/>) and
      which define the medium's behavior with attachments and snapshots.

      All media can be also divided in two groups: base media and
      differencing media. A base medium contains all sectors of the
      medium data in its own storage and therefore can be used independently.
      In contrast, a differencing medium is a "delta" to some other medium and
      contains only those sectors which differ from that other medium, which is
      then called a parent. The differencing medium is said to be
      linked to that parent. The parent may be itself a differencing
      medium, thus forming a chain of linked media. The last element in that
      chain must always be a base medium. Note that several differencing
      media may be linked to the same parent medium.

      Differencing media can be distinguished from base media by querying the
      <link to="#parent"/> attribute: base media do not have parents they would
      depend on, so the value of this attribute is always @c null for them.
      Using this attribute, it is possible to walk up the medium tree (from the
      child medium to its parent). It is also possible to walk down the tree
      using the <link to="#children"/> attribute.

      Note that the type of all differencing media is "normal"; all other
      values are meaningless for them. Base media may be of any type.

      Automatic composition of the file name part

      Another extension to the <link to="IMedium::location"/> attribute is that
      there is a possibility to cause VirtualBox to compose a unique value for
      the file name part of the location using the UUID of the hard disk. This
      applies only to hard disks in <link to="MediumState_NotCreated"/> state,
      e.g. before the storage unit is created, and works as follows. You set the
      value of the <link to="IMedium::location"/> attribute to a location
      specification which only contains the path specification but not the file
      name part and ends with either a forward slash or a backslash character.
      In response, VirtualBox will generate a new UUID for the hard disk and
      compose the file name using the following pattern:
      
        <path>/{<uuid>}.<ext>
      
      where <path> is the supplied path specification,
      <uuid> is the newly generated UUID and <ext>
      is the default extension for the storage format of this hard disk. After
      that, you may call any of the methods that create a new hard disk storage
      unit and they will use the generated UUID and file name.
    """
    __uuid__ = '86fd6208-4c8c-40c2-a4e3-f6b47ac6ef07'
    __wsmap__ = 'managed'
    
    @property
    def id_p(self):
        """Get str value for 'id'
        UUID of the medium. For a newly created medium, this value is a randomly
        generated UUID.

        
          For media in one of MediumState_NotCreated, MediumState_Creating or
          MediumState_Deleting states, the value of this property is undefined
          and will most likely be an empty UUID.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def description(self):
        """Get or set str value for 'description'
        Optional description of the medium. For a newly created medium the value
        of this attribute is an empty string.

        Medium types that don't support this attribute will return E_NOTIMPL in
        attempt to get or set this attribute's value.

        
          For some storage types, reading this attribute may return an outdated
          (last known) value when <link to="#state"/> is <link to="MediumState_Inaccessible"/> or <link to="MediumState_LockedWrite"/> because the value of this attribute is
          stored within the storage unit itself. Also note that changing the
          attribute value is not possible in such case, as well as when the
          medium is the <link to="MediumState_LockedRead"/> state.
        """
        ret = self._get_attr("description")
        return ret

    @description.setter
    def description(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("description", value)

    @property
    def state(self):
        """Get MediumState value for 'state'
        Returns the current medium state, which is the last state set by
        the accessibility check performed by <link to="#refreshState"/>.
        If that method has not yet been called on the medium, the state
        is "Inaccessible"; as opposed to truly inaccessible media, the
        value of <link to="#lastAccessError"/> will be an empty string in
        that case.

        As of version 3.1, this no longer performs an accessibility check
          automatically; call <link to="#refreshState"/> for that.
        """
        ret = self._get_attr("state")
        return MediumState(ret)

    @property
    def variant(self):
        """Get MediumVariant value for 'variant'
        Returns the storage format variant information for this medium
        as an array of the flags described at <link to="MediumVariant"/>.
        Before <link to="#refreshState"/> is called this method returns
        an undefined value.
        """
        ret = self._get_attr("variant")
        return [MediumVariant(a) for a in ret]

    @property
    def location(self):
        """Get or set str value for 'location'
        Location of the storage unit holding medium data.

        The format of the location string is medium type specific. For medium
        types using regular files in a host's file system, the location
        string is the full file name.

        Some medium types may support changing the storage unit location by
        simply changing the value of this property. If this operation is not
        supported, the implementation will return E_NOTIMPL in attempt to set
        this attribute's value.

        When setting a value of the location attribute which is a regular file
        in the host's file system, the given file name may be either relative to
        the <link to="IVirtualBox::homeFolder">VirtualBox home folder</link> or
        absolute. Note that if the given location specification does not contain
        the file extension part then a proper default extension will be
        automatically appended by the implementation depending on the medium type.
        """
        ret = self._get_attr("location")
        return ret

    @location.setter
    def location(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("location", value)

    @property
    def name(self):
        """Get str value for 'name'
        Name of the storage unit holding medium data.

        The returned string is a short version of the <link to="#location"/>
        attribute that is suitable for representing the medium in situations
        where the full location specification is too long (such as lists
        and comboboxes in GUI frontends). This string is also used by frontends
        to sort the media list alphabetically when needed.

        For example, for locations that are regular files in the host's file
        system, the value of this attribute is just the file name (+ extension),
        without the path specification.

        Note that as opposed to the <link to="#location"/> attribute, the name
        attribute will not necessary be unique for a list of media of the
        given type and format.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def device_type(self):
        """Get DeviceType value for 'deviceType'
        Kind of device (DVD/Floppy/HardDisk) which is applicable to this
        medium.
        """
        ret = self._get_attr("deviceType")
        return DeviceType(ret)

    @property
    def host_drive(self):
        """Get bool value for 'hostDrive'
        True if this corresponds to a drive on the host.
        """
        ret = self._get_attr("hostDrive")
        return ret

    @property
    def size(self):
        """Get int value for 'size'
        Physical size of the storage unit used to hold medium data (in bytes).

        
          For media whose <link to="#state"/> is <link to="MediumState_Inaccessible"/>, the value of this property is the
          last known size. For <link to="MediumState_NotCreated"/> media,
          the returned value is zero.
        """
        ret = self._get_attr("size")
        return ret

    @property
    def format_p(self):
        """Get str value for 'format'
        Storage format of this medium.

        The value of this attribute is a string that specifies a backend used
        to store medium data. The storage format is defined when you create a
        new medium or automatically detected when you open an existing medium,
        and cannot be changed later.

        The list of all storage formats supported by this VirtualBox
        installation can be obtained using
        <link to="ISystemProperties::mediumFormats"/>.
        """
        ret = self._get_attr("format")
        return ret

    @property
    def medium_format(self):
        """Get IMediumFormat value for 'mediumFormat'
        Storage medium format object corresponding to this medium.

        The value of this attribute is a reference to the medium format object
        that specifies the backend properties used to store medium data. The
        storage format is defined when you create a new medium or automatically
        detected when you open an existing medium, and cannot be changed later.

        @c null is returned if there is no associated medium format
        object. This can e.g. happen for medium objects representing host
        drives and other special medium objects.
        """
        ret = self._get_attr("mediumFormat")
        return IMediumFormat(ret)

    @property
    def type_p(self):
        """Get or set MediumType value for 'type'
        Type (role) of this medium.

        The following constraints apply when changing the value of this
        attribute:
        
          If a medium is attached to a virtual machine (either in the
              current state or in one of the snapshots), its type cannot be
              changed.
          
          As long as the medium has children, its type cannot be set
              to <link to="MediumType_Writethrough"/>.
          
          The type of all differencing media is
              <link to="MediumType_Normal"/> and cannot be changed.
          
        

        The type of a newly created or opened medium is set to
        <link to="MediumType_Normal"/>, except for DVD and floppy media,
        which have a type of <link to="MediumType_Writethrough"/>.
        """
        ret = self._get_attr("type")
        return MediumType(ret)

    @type_p.setter
    def type_p(self, value):
        if not isinstance(value, MediumType):
            raise TypeError("value is not an instance of MediumType")
        return self._set_attr("type", value)

    @property
    def allowed_types(self):
        """Get MediumType value for 'allowedTypes'
        Returns which medium types can selected for this medium.
        """
        ret = self._get_attr("allowedTypes")
        return [MediumType(a) for a in ret]

    @property
    def parent(self):
        """Get IMedium value for 'parent'
        Parent of this medium (the medium this medium is directly based
        on).

        Only differencing media have parents. For base (non-differencing)
        media, @c null is returned.
        """
        ret = self._get_attr("parent")
        return IMedium(ret)

    @property
    def children(self):
        """Get IMedium value for 'children'
        Children of this medium (all differencing media directly based
        on this medium). A @c null array is returned if this medium
        does not have any children.
        """
        ret = self._get_attr("children")
        return [IMedium(a) for a in ret]

    @property
    def base(self):
        """Get IMedium value for 'base'
        Base medium of this medium.

        If this is a differencing medium, its base medium is the medium
        the given medium branch starts from. For all other types of media, this
        property returns the medium object itself (i.e. the same object this
        property is read on).
        """
        ret = self._get_attr("base")
        return IMedium(ret)

    @property
    def read_only(self):
        """Get bool value for 'readOnly'
        Returns @c true if this medium is read-only and @c false otherwise.

        A medium is considered to be read-only when its contents cannot be
        modified without breaking the integrity of other parties that depend on
        this medium such as its child media or snapshots of virtual machines
        where this medium is attached to these machines. If there are no
        children and no such snapshots then there is no dependency and the
        medium is not read-only.

        The value of this attribute can be used to determine the kind of the
        attachment that will take place when attaching this medium to a
        virtual machine. If the value is @c false then the medium will
        be attached directly. If the value is @c true then the medium
        will be attached indirectly by creating a new differencing child
        medium for that. See the interface description for more information.

        Note that all <link to="MediumType_Immutable">Immutable</link> media
        are always read-only while all
        <link to="MediumType_Writethrough">Writethrough</link> media are
        always not.

        
          The read-only condition represented by this attribute is related to
          the medium type and usage, not to the current
          <link to="IMedium::state">medium state</link> and not to the read-only
          state of the storage unit.
        """
        ret = self._get_attr("readOnly")
        return ret

    @property
    def logical_size(self):
        """Get int value for 'logicalSize'
        Logical size of this medium (in bytes), as reported to the
        guest OS running inside the virtual machine this medium is
        attached to. The logical size is defined when the medium is created
        and cannot be changed later.

        
          For media whose state is <link to="#state"/> is <link to="MediumState_Inaccessible"/>, the value of this property is the
          last known logical size. For <link to="MediumState_NotCreated"/>
          media, the returned value is zero.
        """
        ret = self._get_attr("logicalSize")
        return ret

    @property
    def auto_reset(self):
        """Get or set bool value for 'autoReset'
        Whether this differencing medium will be automatically reset each
        time a virtual machine it is attached to is powered up. This
        attribute is automatically set to @c true for the last
        differencing image of an "immutable" medium (see
        <link to="MediumType"/>).

        See <link to="#reset"/> for more information about resetting
        differencing media.

        
          Reading this property on a base (non-differencing) medium will
          always @c false. Changing the value of this property in this
          case is not supported.
        """
        ret = self._get_attr("autoReset")
        return ret

    @auto_reset.setter
    def auto_reset(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("autoReset", value)

    @property
    def last_access_error(self):
        """Get str value for 'lastAccessError'
        Text message that represents the result of the last accessibility
        check performed by <link to="#refreshState"/>.

        An empty string is returned if the last accessibility check
        was successful or has not yet been called. As a result, if
        <link to="#state"/> is "Inaccessible" and this attribute is empty,
        then <link to="#refreshState"/> has yet to be called; this is the
        default value of media after VirtualBox initialization.
        A non-empty string indicates a failure and should normally describe
        a reason of the failure (for example, a file read error).
        """
        ret = self._get_attr("lastAccessError")
        return ret

    @property
    def machine_ids(self):
        """Get str value for 'machineIds'
        Array of UUIDs of all machines this medium is attached to.

        A @c null array is returned if this medium is not attached to any
        machine or to any machine's snapshot.

        
          The returned array will include a machine even if this medium is not
          attached to that machine in the current state but attached to it in
          one of the machine's snapshots. See <link to="#getSnapshotIds"/> for
          details.
        """
        ret = self._get_attr("machineIds")
        return ret

    def set_ids(self, set_image_id, image_id, set_parent_id, parent_id):
        """Changes the UUID and parent UUID for a hard disk medium.

        in set_image_id of type bool
            Select whether a new image UUID is set or not.

        in image_id of type str
            New UUID for the image. If an empty string is passed, then a new
          UUID is automatically created, provided that @a setImageId is @c true.
          Specifying a zero UUID is not allowed.

        in set_parent_id of type bool
            Select whether a new parent UUID is set or not.

        in parent_id of type str
            New parent UUID for the image. If an empty string is passed, then a
          new UUID is automatically created, provided @a setParentId is
          @c true. A zero UUID is valid.

        raises E_INVALIDARG
            Invalid parameter combination.
        
        raises VBOX_E_NOT_SUPPORTED
            Medium is not a hard disk medium.
        
        """
        if not isinstance(set_image_id, bool):
            raise TypeError("set_image_id can only be an instance of type bool")
        if type(image_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(set_parent_id, bool):
            raise TypeError("set_parent_id can only be an instance of type bool")
        if type(parent_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setIds",
                     in_p=[set_image_id, image_id, set_parent_id, parent_id])

    def refresh_state(self):
        """If the current medium state (see <link to="MediumState"/>) is one of
        "Created", "Inaccessible" or "LockedRead", then this performs an
        accessibility check on the medium and sets the value of the <link to="#state"/>
        attribute accordingly; that value is also returned for convenience.

        For all other state values, this does not perform a refresh but returns
        the state only.

        The refresh, if performed, may take a long time (several seconds or even
        minutes, depending on the storage unit location and format) because it performs an
        accessibility check of the storage unit. This check may cause a significant
        delay if the storage unit of the given medium is, for example, a file located
        on a network share which is not currently accessible due to connectivity
        problems. In that case, the call will not return until a timeout
        interval defined by the host OS for this operation expires. For this reason,
        it is recommended to never read this attribute on the main UI thread to avoid
        making the UI unresponsive.

        If the last known state of the medium is "Created" and the accessibility
        check fails, then the state would be set to "Inaccessible", and
        <link to="#lastAccessError"/> may be used to get more details about the
        failure. If the state of the medium is "LockedRead", then it remains the
        same, and a non-empty value of <link to="#lastAccessError"/> will
        indicate a failed accessibility check in this case.

        Note that not all medium states are applicable to all medium types.

        return state of type MediumState
            New medium state.

        """
        state = self._call("refreshState")
        state = MediumState(state)
        return state

    def get_snapshot_ids(self, machine_id):
        """Returns an array of UUIDs of all snapshots of the given machine where
        this medium is attached to.

        If the medium is attached to the machine in the current state, then the
        first element in the array will always be the ID of the queried machine
        (i.e. the value equal to the @c machineId argument), followed by
        snapshot IDs (if any).

        If the medium is not attached to the machine in the current state, then
        the array will contain only snapshot IDs.

        The returned array may be @c null if this medium is not attached
        to the given machine at all, neither in the current state nor in one of
        the snapshots.

        in machine_id of type str
            UUID of the machine to query.

        return snapshot_ids of type str
            Array of snapshot UUIDs of the given machine using this medium.

        """
        if type(machine_id) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        snapshot_ids = self._call("getSnapshotIds",
                     in_p=[machine_id])
        return snapshot_ids

    def lock_read(self):
        """Locks this medium for reading.

        A read lock is shared: many clients can simultaneously lock the
        same medium for reading unless it is already locked for writing (see
        <link to="#lockWrite"/>) in which case an error is returned.

        When the medium is locked for reading, it cannot be modified
        from within VirtualBox. This means that any method that changes
        the properties of this medium or contents of the storage unit
        will return an error (unless explicitly stated otherwise). That
        includes an attempt to start a virtual machine that wants to
        write to the the medium.

        When the virtual machine is started up, it locks for reading all
        media it uses in read-only mode. If some medium cannot be locked
        for reading, the startup procedure will fail.
        A medium is typically locked for reading while it is used by a running
        virtual machine but has a depending differencing image that receives
        the actual write operations. This way one base medium can have
        multiple child differencing images which can be written to
        simultaneously. Read-only media such as DVD and floppy images are
        also locked for reading only (so they can be in use by multiple
        machines simultaneously).

        A medium is also locked for reading when it is the source of a
        write operation such as <link to="#cloneTo"/> or <link to="#mergeTo"/>.

        The medium locked for reading must be unlocked using the <link to="#unlockRead"/> method. Calls to <link to="#lockRead"/>
        can be nested and must be followed by the same number of paired
        <link to="#unlockRead"/> calls.

        This method sets the medium state (see <link to="#state"/>) to
        "LockedRead" on success. The medium's previous state must be
        one of "Created", "Inaccessible" or "LockedRead".

        Locking an inaccessible medium is not an error; this method performs
        a logical lock that prevents modifications of this medium through
        the VirtualBox API, not a physical file-system lock of the underlying
        storage unit.

        This method returns the current state of the medium
        before the operation.

        return state of type MediumState
            State of the medium after the operation.

        raises VBOX_E_INVALID_OBJECT_STATE
            Invalid medium state (e.g. not created, locked, inaccessible,
          creating, deleting).
        
        """
        state = self._call("lockRead")
        state = MediumState(state)
        return state

    def unlock_read(self):
        """Cancels the read lock previously set by <link to="#lockRead"/>.

        For both success and failure, this method returns the current state
        of the medium after the operation.

        See <link to="#lockRead"/> for more details.

        return state of type MediumState
            State of the medium after the operation.

        raises VBOX_E_INVALID_OBJECT_STATE
            Medium not locked for reading.
        
        """
        state = self._call("unlockRead")
        state = MediumState(state)
        return state

    def lock_write(self):
        """Locks this medium for writing.

        A write lock, as opposed to <link to="#lockRead"/>, is
        exclusive: there may be only one client holding a write lock,
        and there may be no read locks while the write lock is held.
        As a result, read-locking fails if a write lock is held, and
        write-locking fails if either a read or another write lock is held.

        When a medium is locked for writing, it cannot be modified
        from within VirtualBox, and it is not guaranteed that the values
        of its properties are up-to-date. Any method that changes the
        properties of this medium or contents of the storage unit will
        return an error (unless explicitly stated otherwise).

        When a virtual machine is started up, it locks for writing all
        media it uses to write data to. If any medium could not be locked
        for writing, the startup procedure will fail. If a medium has
        differencing images, then while the machine is running, only
        the last ("leaf") differencing image is locked for writing,
        whereas its parents are locked for reading only.

        A medium is also locked for writing when it is the target of a
        write operation such as <link to="#cloneTo"/> or <link to="#mergeTo"/>.

        The medium locked for writing must be unlocked using the <link to="#unlockWrite"/> method. Write locks cannot be nested.

        This method sets the medium state (see <link to="#state"/>) to
        "LockedWrite" on success. The medium's previous state must be
        either "Created" or "Inaccessible".

        Locking an inaccessible medium is not an error; this method performs
        a logical lock that prevents modifications of this medium through
        the VirtualBox API, not a physical file-system lock of the underlying
        storage unit.

        For both, success and failure, this method returns the current
        state of the medium before the operation.

        return state of type MediumState
            State of the medium after the operation.

        raises VBOX_E_INVALID_OBJECT_STATE
            Invalid medium state (e.g. not created, locked, inaccessible,
          creating, deleting).
        
        """
        state = self._call("lockWrite")
        state = MediumState(state)
        return state

    def unlock_write(self):
        """Cancels the write lock previously set by <link to="#lockWrite"/>.

        For both success and failure, this method returns the current
        state of the medium after the operation.

        See <link to="#lockWrite"/> for more details.

        return state of type MediumState
            State of the medium after the operation.

        raises VBOX_E_INVALID_OBJECT_STATE
            Medium not locked for writing.
        
        """
        state = self._call("unlockWrite")
        state = MediumState(state)
        return state

    def close(self):
        """Closes this medium.

        The medium must not be attached to any known virtual machine
        and must not have any known child media, otherwise the
        operation will fail.

        When the medium is successfully closed, it is removed from
        the list of registered media, but its storage unit is not
        deleted. In particular, this means that this medium can
        later be opened again using the <link to="IVirtualBox::openMedium"/>
        call.

        Note that after this method successfully returns, the given medium
        object becomes uninitialized. This means that any attempt
        to call any of its methods or attributes will fail with the
        "Object not ready" (E_ACCESSDENIED) error.

        raises VBOX_E_INVALID_OBJECT_STATE
            Invalid medium state (other than not created, created or
          inaccessible).
        
        raises VBOX_E_OBJECT_IN_USE
            Medium attached to virtual machine.
        
        raises VBOX_E_FILE_ERROR
            Settings file not accessible.
        
        raises VBOX_E_XML_ERROR
            Could not parse the settings file.
        
        """
        self._call("close")

    def get_property(self, name):
        """Returns the value of the custom medium property with the given name.

        The list of all properties supported by the given medium format can
        be obtained with <link to="IMediumFormat::describeProperties"/>.

        If this method returns an empty string in @a value, the requested
        property is supported but currently not assigned any value.

        in name of type str
            Name of the property to get.

        return value of type str
            Current property value.

        raises VBOX_E_OBJECT_NOT_FOUND
            Requested property does not exist (not supported by the format).
        
        raises E_INVALIDARG
            @a name is @c null or empty.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getProperty",
                     in_p=[name])
        return value

    def set_property(self, name, value):
        """Sets the value of the custom medium property with the given name.

        The list of all properties supported by the given medium format can
        be obtained with <link to="IMediumFormat::describeProperties"/>.

        Setting the property value to @c null or an empty string is
        equivalent to deleting the existing value. A default value (if it is
        defined for this property) will be used by the format backend in this
        case.

        in name of type str
            Name of the property to set.

        in value of type str
            Property value to set.

        raises VBOX_E_OBJECT_NOT_FOUND
            Requested property does not exist (not supported by the format).
        
        raises E_INVALIDARG
            @a name is @c null or empty.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setProperty",
                     in_p=[name, value])

    def get_properties(self, names):
        """Returns values for a group of properties in one call.

        The names of the properties to get are specified using the @a names
        argument which is a list of comma-separated property names or
        an empty string if all properties are to be returned.
        Currently the value of this argument is ignored and the method
        always returns all existing properties.

        The list of all properties supported by the given medium format can
        be obtained with <link to="IMediumFormat::describeProperties"/>.

        The method returns two arrays, the array of property names corresponding
        to the @a names argument and the current values of these properties.
        Both arrays have the same number of elements with each element at the
        given index in the first array corresponds to an element at the same
        index in the second array.

        For properties that do not have assigned values, an empty string is
        returned at the appropriate index in the @a returnValues array.

        in names of type str
            Names of properties to get.

        out return_names of type str
            Names of returned properties.

        return return_values of type str
            Values of returned properties.

        """
        if type(names) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        (return_names, return_values) = self._call("getProperties",
                     in_p=[names])
        return (return_names, return_values)

    def set_properties(self, names, values):
        """Sets values for a group of properties in one call.

        The names of the properties to set are passed in the @a names
        array along with the new values for them in the @a values array. Both
        arrays have the same number of elements with each element at the given
        index in the first array corresponding to an element at the same index
        in the second array.

        If there is at least one property name in @a names that is not valid,
        the method will fail before changing the values of any other properties
        from the @a names array.

        Using this method over <link to="#setProperty"/> is preferred if you
        need to set several properties at once since it is more efficient.

        The list of all properties supported by the given medium format can
        be obtained with <link to="IMediumFormat::describeProperties"/>.

        Setting the property value to @c null or an empty string is equivalent
        to deleting the existing value. A default value (if it is defined for
        this property) will be used by the format backend in this case.

        in names of type str
            Names of properties to set.

        in values of type str
            Values of properties to set.

        """
        if not isinstance(names, list):
            raise TypeError("names can only be an instance of type list")
        for a in names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(values, list):
            raise TypeError("values can only be an instance of type list")
        for a in values[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        self._call("setProperties",
                     in_p=[names, values])

    def create_base_storage(self, logical_size, variant):
        """Starts creating a hard disk storage unit (fixed/dynamic, according
        to the variant flags) in in the background. The previous storage unit
        created for this object, if any, must first be deleted using
        <link to="#deleteStorage"/>, otherwise the operation will fail.

        Before the operation starts, the medium is placed in
        <link to="MediumState_Creating"/> state. If the create operation
        fails, the medium will be placed back in <link to="MediumState_NotCreated"/>
        state.

        After the returned progress object reports that the operation has
        successfully completed, the medium state will be set to <link to="MediumState_Created"/>, the medium will be remembered by this
        VirtualBox installation and may be attached to virtual machines.

        in logical_size of type int
            Maximum logical size of the medium in bytes.

        in variant of type MediumVariant
            Exact image variant which should be created (as a combination of
          <link to="MediumVariant"/> flags).

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_NOT_SUPPORTED
            The variant of storage creation operation is not supported. See
        
        """
        if not isinstance(logical_size, int):
            raise TypeError("logical_size can only be an instance of type int")
        if not isinstance(variant, list):
            raise TypeError("variant can only be an instance of type list")
        for a in variant[:10]:
            if not isinstance(a, MediumVariant):
                raise TypeError(\
                        "array can only contain objects of type MediumVariant")
        progress = self._call("createBaseStorage",
                     in_p=[logical_size, variant])
        progress = IProgress(progress)
        return progress

    def delete_storage(self):
        """Starts deleting the storage unit of this medium.

        The medium must not be attached to any known virtual machine and must
        not have any known child media, otherwise the operation will fail.
        It will also fail if there is no storage unit to delete or if deletion
        is already in progress, or if the medium is being in use (locked for
        read or for write) or inaccessible. Therefore, the only valid state for
        this operation to succeed is <link to="MediumState_Created"/>.

        Before the operation starts, the medium is placed in
        <link to="MediumState_Deleting"/> state and gets removed from the list
        of remembered hard disks (media registry). If the delete operation
        fails, the medium will be remembered again and placed back to
        <link to="MediumState_Created"/> state.

        After the returned progress object reports that the operation is
        complete, the medium state will be set to
        <link to="MediumState_NotCreated"/> and you will be able to use one of
        the storage creation methods to create it again.

        <link to="#close"/>

        

        
          If the deletion operation fails, it is not guaranteed that the storage
          unit still exists. You may check the <link to="IMedium::state"/> value
          to answer this question.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_OBJECT_IN_USE
            Medium is attached to a virtual machine.
        
        raises VBOX_E_NOT_SUPPORTED
            Storage deletion is not allowed because neither of storage creation
          operations are supported. See
        
        """
        progress = self._call("deleteStorage")
        progress = IProgress(progress)
        return progress

    def create_diff_storage(self, target, variant):
        """Starts creating an empty differencing storage unit based on this
        medium in the format and at the location defined by the @a target
        argument.

        The target medium must be in <link to="MediumState_NotCreated"/>
        state (i.e. must not have an existing storage unit). Upon successful
        completion, this operation will set the type of the target medium to
        <link to="MediumType_Normal"/> and create a storage unit necessary to
        represent the differencing medium data in the given format (according
        to the storage format of the target object).

        After the returned progress object reports that the operation is
        successfully complete, the target medium gets remembered by this
        VirtualBox installation and may be attached to virtual machines.

        
          The medium will be set to <link to="MediumState_LockedRead"/>
          state for the duration of this operation.

        in target of type IMedium
            Target medium.

        in variant of type MediumVariant
            Exact image variant which should be created (as a combination of
          <link to="MediumVariant"/> flags).

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_OBJECT_IN_USE
            Medium not in @c NotCreated state.
        
        """
        if not isinstance(target, IMedium):
            raise TypeError("target can only be an instance of type IMedium")
        if not isinstance(variant, list):
            raise TypeError("variant can only be an instance of type list")
        for a in variant[:10]:
            if not isinstance(a, MediumVariant):
                raise TypeError(\
                        "array can only contain objects of type MediumVariant")
        progress = self._call("createDiffStorage",
                     in_p=[target, variant])
        progress = IProgress(progress)
        return progress

    def merge_to(self, target):
        """Starts merging the contents of this medium and all intermediate
        differencing media in the chain to the given target medium.

        The target medium must be either a descendant of this medium or
        its ancestor (otherwise this method will immediately return a failure).
        It follows that there are two logical directions of the merge operation:
        from ancestor to descendant (forward merge) and from descendant to
        ancestor (backward merge). Let us consider the following medium
        chain:

        Base <- Diff_1 <- Diff_2

        Here, calling this method on the Base medium object with
        Diff_2 as an argument will be a forward merge; calling it on
        Diff_2 with Base as an argument will be a backward
        merge. Note that in both cases the contents of the resulting medium
        will be the same, the only difference is the medium object that takes
        the result of the merge operation. In case of the forward merge in the
        above example, the result will be written to Diff_2; in case of
        the backward merge, the result will be written to Base. In
        other words, the result of the operation is always stored in the target
        medium.

        Upon successful operation completion, the storage units of all media in
        the chain between this (source) medium and the target medium, including
        the source medium itself, will be automatically deleted and the
        relevant medium objects (including this medium) will become
        uninitialized. This means that any attempt to call any of
        their methods or attributes will fail with the
        "Object not ready" (E_ACCESSDENIED) error. Applied to the above
        example, the forward merge of Base to Diff_2 will
        delete and uninitialize both Base and Diff_1 media.
        Note that Diff_2 in this case will become a base medium
        itself since it will no longer be based on any other medium.

        Considering the above, all of the following conditions must be met in
        order for the merge operation to succeed:
        
          
            Neither this (source) medium nor any intermediate
            differencing medium in the chain between it and the target
            medium is attached to any virtual machine.
          
          
            Neither the source medium nor the target medium is an
            <link to="MediumType_Immutable"/> medium.
          
          
            The part of the medium tree from the source medium to the
            target medium is a linear chain, i.e. all medium in this
            chain have exactly one child which is the next medium in this
            chain. The only exception from this rule is the target medium in
            the forward merge operation; it is allowed to have any number of
            child media because the merge operation will not change its
            logical contents (as it is seen by the guest OS or by children).
          
          
            None of the involved media are in
            <link to="MediumState_LockedRead"/> or
            <link to="MediumState_LockedWrite"/> state.
          
        

        
          This (source) medium and all intermediates will be placed to <link to="MediumState_Deleting"/> state and the target medium will be
          placed to <link to="MediumState_LockedWrite"/> state and for the
          duration of this operation.

        in target of type IMedium
            Target medium.

        return progress of type IProgress
            Progress object to track the operation completion.

        """
        if not isinstance(target, IMedium):
            raise TypeError("target can only be an instance of type IMedium")
        progress = self._call("mergeTo",
                     in_p=[target])
        progress = IProgress(progress)
        return progress

    def clone_to(self, target, variant, parent):
        """Starts creating a clone of this medium in the format and at the
        location defined by the @a target argument.

        The target medium must be either in <link to="MediumState_NotCreated"/>
        state (i.e. must not have an existing storage unit) or in
        <link to="MediumState_Created"/> state (i.e. created and not locked, and
        big enough to hold the data or else the copy will be partial). Upon
        successful completion, the cloned medium will contain exactly the
        same sector data as the medium being cloned, except that in the
        first case a new UUID for the clone will be randomly generated, and in
        the second case the UUID will remain unchanged.

        The @a parent argument defines which medium will be the parent
        of the clone. Passing a @c null reference indicates that the clone will
        be a base image, i.e. completely independent. It is possible to specify
        an arbitrary medium for this parameter, including the parent of the
        medium which is being cloned. Even cloning to a child of the source
        medium is possible. Note that when cloning to an existing image, the
        @a parent argument is ignored.

        After the returned progress object reports that the operation is
        successfully complete, the target medium gets remembered by this
        VirtualBox installation and may be attached to virtual machines.

        
          This medium will be placed to <link to="MediumState_LockedRead"/>
          state for the duration of this operation.

        in target of type IMedium
            Target medium.

        in variant of type MediumVariant
            Exact image variant which should be created (as a combination of
          <link to="MediumVariant"/> flags).

        in parent of type IMedium
            Parent of the cloned medium.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises E_NOTIMPL
            The specified cloning variant is not supported at the moment.
        
        """
        if not isinstance(target, IMedium):
            raise TypeError("target can only be an instance of type IMedium")
        if not isinstance(variant, list):
            raise TypeError("variant can only be an instance of type list")
        for a in variant[:10]:
            if not isinstance(a, MediumVariant):
                raise TypeError(\
                        "array can only contain objects of type MediumVariant")
        if not isinstance(parent, IMedium):
            raise TypeError("parent can only be an instance of type IMedium")
        progress = self._call("cloneTo",
                     in_p=[target, variant, parent])
        progress = IProgress(progress)
        return progress

    def clone_to_base(self, target, variant):
        """Starts creating a clone of this medium in the format and at the
    location defined by the @a target argument.

    The target medium must be either in <link to="MediumState_NotCreated"/>
    state (i.e. must not have an existing storage unit) or in
    <link to="MediumState_Created"/> state (i.e. created and not locked, and
    big enough to hold the data or else the copy will be partial). Upon
    successful completion, the cloned medium will contain exactly the
    same sector data as the medium being cloned, except that in the
    first case a new UUID for the clone will be randomly generated, and in
    the second case the UUID will remain unchanged.

    The @a parent argument defines which medium will be the parent
    of the clone. In this case the clone will be a base image, i.e.
    completely independent. It is possible to specify an arbitrary
    medium for this parameter, including the parent of the
    medium which is being cloned. Even cloning to a child of the source
    medium is possible. Note that when cloning to an existing image, the
    @a parent argument is ignored.

    After the returned progress object reports that the operation is
    successfully complete, the target medium gets remembered by this
    VirtualBox installation and may be attached to virtual machines.

    
    This medium will be placed to <link to="MediumState_LockedRead"/>
    state for the duration of this operation.

        in target of type IMedium
            Target medium.

        in variant of type MediumVariant
            <link to="MediumVariant"/> flags).

        return progress of type IProgress
            Progress object to track the operation completion.

        raises E_NOTIMPL
            The specified cloning variant is not supported at the moment.
        
        """
        if not isinstance(target, IMedium):
            raise TypeError("target can only be an instance of type IMedium")
        if not isinstance(variant, list):
            raise TypeError("variant can only be an instance of type list")
        for a in variant[:10]:
            if not isinstance(a, MediumVariant):
                raise TypeError(\
                        "array can only contain objects of type MediumVariant")
        progress = self._call("cloneToBase",
                     in_p=[target, variant])
        progress = IProgress(progress)
        return progress

    def compact(self):
        """Starts compacting of this medium. This means that the medium is
        transformed into a possibly more compact storage representation.
        This potentially creates temporary images, which can require a
        substantial amount of additional disk space.

        This medium will be placed to <link to="MediumState_LockedWrite"/>
        state and all its parent media (if any) will be placed to
        <link to="MediumState_LockedRead"/> state for the duration of this
        operation.

        Please note that the results can be either returned straight away,
        or later as the result of the background operation via the object
        returned via the @a progress parameter.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_NOT_SUPPORTED
            Medium format does not support compacting (but potentially
          needs it).
        
        """
        progress = self._call("compact")
        progress = IProgress(progress)
        return progress

    def resize(self, logical_size):
        """Starts resizing this medium. This means that the nominal size of the
        medium is set to the new value. Both increasing and decreasing the
        size is possible, and there are no safety checks, since VirtualBox
        does not make any assumptions about the medium contents.

        Resizing usually needs additional disk space, and possibly also
        some temporary disk space. Note that resize does not create a full
        temporary copy of the medium, so the additional disk space requirement
        is usually much lower than using the clone operation.

        This medium will be placed to <link to="MediumState_LockedWrite"/>
        state for the duration of this operation.

        Please note that the results can be either returned straight away,
        or later as the result of the background operation via the object
        returned via the @a progress parameter.

        in logical_size of type int
            New nominal capacity of the medium in bytes.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_NOT_SUPPORTED
            Medium format does not support resizing.
        
        """
        if not isinstance(logical_size, int):
            raise TypeError("logical_size can only be an instance of type int")
        progress = self._call("resize",
                     in_p=[logical_size])
        progress = IProgress(progress)
        return progress

    def reset(self):
        """Starts erasing the contents of this differencing medium.

        This operation will reset the differencing medium to its initial
        state when it does not contain any sector data and any read operation is
        redirected to its parent medium. This automatically gets called
        during VM power-up for every medium whose <link to="#autoReset"/>
        attribute is @c true.

        The medium will be write-locked for the duration of this operation (see
        <link to="#lockWrite"/>).

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_NOT_SUPPORTED
            This is not a differencing medium.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Medium is not in
        
        """
        progress = self._call("reset")
        progress = IProgress(progress)
        return progress


class IMediumFormat(Interface):
    """
    The IMediumFormat interface represents a medium format.

        Each medium format has an associated backend which is used to handle
        media stored in this format. This interface provides information
        about the properties of the associated backend.

        Each medium format is identified by a string represented by the
        <link to="#id"/> attribute. This string is used in calls like
        <link to="IVirtualBox::createHardDisk"/> to specify the desired
        format.

        The list of all supported medium formats can be obtained using
        <link to="ISystemProperties::mediumFormats"/>.

        <link to="IMedium"/>
    """
    __uuid__ = '6238e1cf-a17d-4ec1-8172-418bfb22b93a'
    __wsmap__ = 'managed'
    
    @property
    def id_p(self):
        """Get str value for 'id'
        Identifier of this format.

        The format identifier is a non-@c null non-empty ASCII string. Note that
        this string is case-insensitive. This means that, for example, all of
        the following strings:
        
          "VDI"
          "vdi"
          "VdI"
        refer to the same medium format.

        This string is used in methods of other interfaces where it is necessary
        to specify a medium format, such as
        <link to="IVirtualBox::createHardDisk"/>.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def name(self):
        """Get str value for 'name'
        Human readable description of this format.

        Mainly for use in file open dialogs.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def capabilities(self):
        """Get MediumFormatCapabilities value for 'capabilities'
        Capabilities of the format as an array of the flags.

        For the meaning of individual capability flags see
        <link to="MediumFormatCapabilities"/>.
        """
        ret = self._get_attr("capabilities")
        return [MediumFormatCapabilities(a) for a in ret]

    def describe_file_extensions(self):
        """Returns two arrays describing the supported file extensions.

        The first array contains the supported extensions and the seconds one
        the type each extension supports. Both have the same size.

        Note that some backends do not work on files, so this array may be
        empty.

        <link to="IMediumFormat::capabilities"/>

        out extensions of type str
            The array of supported extensions.

        out types of type DeviceType
            The array which indicates the device type for every given extension.

        """
        (extensions, types) = self._call("describeFileExtensions")
        types = [DeviceType(a) for a in types]
        return (extensions, types)

    def describe_properties(self):
        """Returns several arrays describing the properties supported by this
        format.

        An element with the given index in each array describes one
        property. Thus, the number of elements in each returned array is the
        same and corresponds to the number of supported properties.

        The returned arrays are filled in only if the
        <link to="MediumFormatCapabilities_Properties"/> flag is set.
        All arguments must be non-@c null.

        <link to="DataType"/>, <link to="DataFlags"/>

        out names of type str
            Array of property names.

        out descriptions of type str
            Array of property descriptions.

        out types of type DataType
            Array of property types.

        out flags of type int
            Array of property flags.

        out defaults of type str
            Array of default property values.

        """
        (names, descriptions, types, flags, defaults) = self._call("describeProperties")
        types = [DataType(a) for a in types]
        return (names, descriptions, types, flags, defaults)


class IKeyboard(Interface):
    """
    The IKeyboard interface represents the virtual machine's keyboard. Used
      in <link to="IConsole::keyboard"/>.

      Use this interface to send keystrokes or the Ctrl-Alt-Del sequence
      to the virtual machine.
    """
    __uuid__ = 'f6916ec5-a881-4237-898f-7de58cf88672'
    __wsmap__ = 'managed'
    
    def put_scancode(self, scancode):
        """Sends a scancode to the keyboard.

        in scancode of type int

        raises VBOX_E_IPRT_ERROR
            Could not send scan code to virtual keyboard.
        
        """
        if not isinstance(scancode, int):
            raise TypeError("scancode can only be an instance of type int")
        self._call("putScancode",
                     in_p=[scancode])

    def put_scancodes(self, scancodes):
        """Sends an array of scancodes to the keyboard.

        in scancodes of type int

        return codes_stored of type int

        raises VBOX_E_IPRT_ERROR
            Could not send all scan codes to virtual keyboard.
        
        """
        if not isinstance(scancodes, list):
            raise TypeError("scancodes can only be an instance of type list")
        for a in scancodes[:10]:
            if not isinstance(a, int):
                raise TypeError(\
                        "array can only contain objects of type int")
        codes_stored = self._call("putScancodes",
                     in_p=[scancodes])
        return codes_stored

    def put_cad(self):
        """Sends the Ctrl-Alt-Del sequence to the keyboard. This
      function is nothing special, it is just a convenience function
      calling <link to="IKeyboard::putScancodes"/> with the proper scancodes.

        raises VBOX_E_IPRT_ERROR
            Could not send all scan codes to virtual keyboard.
        
        """
        self._call("putCAD")

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for keyboard events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)


class IMouse(Interface):
    """
    The IMouse interface represents the virtual machine's mouse. Used in
      <link to="IConsole::mouse"/>.

      Through this interface, the virtual machine's virtual mouse can be
      controlled.
    """
    __uuid__ = '05044a52-7811-4f00-ae3a-0ab7ff707b10'
    __wsmap__ = 'managed'
    
    @property
    def absolute_supported(self):
        """Get bool value for 'absoluteSupported'
        Whether the guest OS supports absolute mouse pointer positioning
        or not.
        
          You can use the <link to="IMouseCapabilityChangedEvent"/>
          event to be instantly informed about changes of this attribute
          during virtual machine execution.
        
        <link to="#putMouseEventAbsolute"/>
        """
        ret = self._get_attr("absoluteSupported")
        return ret

    @property
    def relative_supported(self):
        """Get bool value for 'relativeSupported'
        Whether the guest OS supports relative mouse pointer positioning
        or not.
        
          You can use the <link to="IMouseCapabilityChangedEvent"/>
          event to be instantly informed about changes of this attribute
          during virtual machine execution.
        
        <link to="#putMouseEvent"/>
        """
        ret = self._get_attr("relativeSupported")
        return ret

    @property
    def needs_host_cursor(self):
        """Get bool value for 'needsHostCursor'
        Whether the guest OS can currently switch to drawing it's own mouse
        cursor on demand.
        
          You can use the <link to="IMouseCapabilityChangedEvent"/>
          event to be instantly informed about changes of this attribute
          during virtual machine execution.
        
        <link to="#putMouseEvent"/>
        """
        ret = self._get_attr("needsHostCursor")
        return ret

    def put_mouse_event(self, dx, dy, dz, dw, button_state):
        """Initiates a mouse event using relative pointer movements
        along x and y axis.

        in dx of type int
            Amount of pixels the mouse should move to the right.
          Negative values move the mouse to the left.

        in dy of type int
            Amount of pixels the mouse should move downwards.
          Negative values move the mouse upwards.

        in dz of type int
            Amount of mouse wheel moves.
          Positive values describe clockwise wheel rotations,
          negative values describe counterclockwise rotations.

        in dw of type int
            Amount of horizontal mouse wheel moves.
          Positive values describe a movement to the left,
          negative values describe a movement to the right.

        in button_state of type int
            The current state of mouse buttons. Every bit represents
          a mouse button as follows:
          
            Bit 0 (0x01)left mouse button
            Bit 1 (0x02)right mouse button
            Bit 2 (0x04)middle mouse button
          
          A value of 1 means the corresponding button is pressed.
          otherwise it is released.

        raises E_ACCESSDENIED
            Console not powered up.
        
        raises VBOX_E_IPRT_ERROR
            Could not send mouse event to virtual mouse.
        
        """
        if not isinstance(dx, int):
            raise TypeError("dx can only be an instance of type int")
        if not isinstance(dy, int):
            raise TypeError("dy can only be an instance of type int")
        if not isinstance(dz, int):
            raise TypeError("dz can only be an instance of type int")
        if not isinstance(dw, int):
            raise TypeError("dw can only be an instance of type int")
        if not isinstance(button_state, int):
            raise TypeError("button_state can only be an instance of type int")
        self._call("putMouseEvent",
                     in_p=[dx, dy, dz, dw, button_state])

    def put_mouse_event_absolute(self, x, y, dz, dw, button_state):
        """Positions the mouse pointer using absolute x and y coordinates.
        These coordinates are expressed in pixels and
        start from [1,1] which corresponds to the top left
        corner of the virtual display.

        

        
          This method will have effect only if absolute mouse
          positioning is supported by the guest OS.
        

        <link to="#absoluteSupported"/>

        in x of type int
            X coordinate of the pointer in pixels, starting from @c 1.

        in y of type int
            Y coordinate of the pointer in pixels, starting from @c 1.

        in dz of type int
            Amount of mouse wheel moves.
          Positive values describe clockwise wheel rotations,
          negative values describe counterclockwise rotations.

        in dw of type int
            Amount of horizontal mouse wheel moves.
          Positive values describe a movement to the left,
          negative values describe a movement to the right.

        in button_state of type int
            The current state of mouse buttons. Every bit represents
          a mouse button as follows:
          
            Bit 0 (0x01)left mouse button
            Bit 1 (0x02)right mouse button
            Bit 2 (0x04)middle mouse button
          
          A value of @c 1 means the corresponding button is pressed.
          otherwise it is released.

        raises E_ACCESSDENIED
            Console not powered up.
        
        raises VBOX_E_IPRT_ERROR
            Could not send mouse event to virtual mouse.
        
        """
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        if not isinstance(dz, int):
            raise TypeError("dz can only be an instance of type int")
        if not isinstance(dw, int):
            raise TypeError("dw can only be an instance of type int")
        if not isinstance(button_state, int):
            raise TypeError("button_state can only be an instance of type int")
        self._call("putMouseEventAbsolute",
                     in_p=[x, y, dz, dw, button_state])

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for mouse events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)


class IFramebuffer(Interface):
    """
    Address of the start byte of the frame buffer.
    """
    __uuid__ = 'e3f122c0-adab-4fc9-a8dc-da112fb48428'
    __wsmap__ = 'managed'
    
    @property
    def address(self):
        """Get str value for 'address'
        Address of the start byte of the frame buffer.
        """
        ret = self._get_attr("address")
        return ret

    @property
    def width(self):
        """Get int value for 'width'
        Frame buffer width, in pixels.
        """
        ret = self._get_attr("width")
        return ret

    @property
    def height(self):
        """Get int value for 'height'
        Frame buffer height, in pixels.
        """
        ret = self._get_attr("height")
        return ret

    @property
    def bits_per_pixel(self):
        """Get int value for 'bitsPerPixel'
        Color depth, in bits per pixel. When <link to="#pixelFormat"/> is <link to="FramebufferPixelFormat_FOURCC_RGB">FOURCC_RGB</link>, valid values
        are: 8, 15, 16, 24 and 32.
        """
        ret = self._get_attr("bitsPerPixel")
        return ret

    @property
    def bytes_per_line(self):
        """Get int value for 'bytesPerLine'
        Scan line size, in bytes. When <link to="#pixelFormat"/> is <link to="FramebufferPixelFormat_FOURCC_RGB">FOURCC_RGB</link>, the
        size of the scan line must be aligned to 32 bits.
        """
        ret = self._get_attr("bytesPerLine")
        return ret

    @property
    def pixel_format(self):
        """Get int value for 'pixelFormat'
        Frame buffer pixel format. It's either one of the values defined by <link to="FramebufferPixelFormat"/> or a raw FOURCC code.
        
          This attribute must never (and will never) return <link to="FramebufferPixelFormat_Opaque"/> -- the format of the frame
          buffer must be always known.
        """
        ret = self._get_attr("pixelFormat")
        return ret

    @property
    def uses_guest_vram(self):
        """Get bool value for 'usesGuestVRAM'
        Defines whether this frame buffer uses the virtual video card's memory
        buffer (guest VRAM) directly or not.
        """
        ret = self._get_attr("usesGuestVRAM")
        return ret

    @property
    def height_reduction(self):
        """Get int value for 'heightReduction'
        Hint from the frame buffer about how much of the standard
        screen height it wants to use for itself. This information is
        exposed to the guest through the VESA BIOS and VMMDev interface
        so that it can use it for determining its video mode table. It
        is not guaranteed that the guest respects the value.
        """
        ret = self._get_attr("heightReduction")
        return ret

    @property
    def overlay(self):
        """Get IFramebufferOverlay value for 'overlay'
        An alpha-blended overlay which is superposed over the frame buffer.
        The initial purpose is to allow the display of icons providing
        information about the VM state, including disk activity, in front
        ends which do not have other means of doing that. The overlay is
        designed to controlled exclusively by IDisplay. It has no locking
        of its own, and any changes made to it are not guaranteed to be
        visible until the affected portion of IFramebuffer is updated. The
        overlay can be created lazily the first time it is requested. This
        attribute can also return @c null to signal that the overlay is not
        implemented.
        """
        ret = self._get_attr("overlay")
        return IFramebufferOverlay(ret)

    @property
    def win_id(self):
        """Get int value for 'winId'
        Platform-dependent identifier of the window where context of this
        frame buffer is drawn, or zero if there's no such window.
        """
        ret = self._get_attr("winId")
        return ret

    def lock(self):
        """Locks the frame buffer.
        Gets called by the IDisplay object where this frame buffer is
        bound to.

        """
        self._call("lock")

    def unlock(self):
        """Unlocks the frame buffer.
        Gets called by the IDisplay object where this frame buffer is
        bound to.

        """
        self._call("unlock")

    def notify_update(self, x, y, width, height):
        """Informs about an update.
        Gets called by the display object where this buffer is
        registered.

        in x of type int

        in y of type int

        in width of type int

        in height of type int

        """
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        self._call("notifyUpdate",
                     in_p=[x, y, width, height])

    def request_resize(self, screen_id, pixel_format, vram, bits_per_pixel, bytes_per_line, width, height):
        """Requests a size and pixel format change.

        There are two modes of working with the video buffer of the virtual
        machine. The indirect mode implies that the IFramebuffer
        implementation allocates a memory buffer for the requested display mode
        and provides it to the virtual machine. In direct mode, the
        IFramebuffer implementation uses the memory buffer allocated and owned
        by the virtual machine. This buffer represents the video memory of the
        emulated video adapter (so called guest VRAM). The direct mode is
        usually faster because the implementation gets a raw pointer to the
        guest VRAM buffer which it can directly use for visualizing the contents
        of the virtual display, as opposed to the indirect mode where the
        contents of guest VRAM are copied to the memory buffer provided by
        the implementation every time a display update occurs.

        It is important to note that the direct mode is really fast only when
        the implementation uses the given guest VRAM buffer directly, for
        example, by blitting it to the window representing the virtual machine's
        display, which saves at least one copy operation comparing to the
        indirect mode. However, using the guest VRAM buffer directly is not
        always possible: the format and the color depth of this buffer may be
        not supported by the target window, or it may be unknown (opaque) as in
        case of text or non-linear multi-plane VGA video modes. In this case,
        the indirect mode (that is always available) should be used as a
        fallback: when the guest VRAM contents are copied to the
        implementation-provided memory buffer, color and format conversion is
        done automatically by the underlying code.

        The @a pixelFormat parameter defines whether the direct mode is
        available or not. If @a pixelFormat is <link to="FramebufferPixelFormat_Opaque"/> then direct access to the guest
        VRAM buffer is not available -- the @a VRAM, @a bitsPerPixel and
        @a bytesPerLine parameters must be ignored and the implementation must use
        the indirect mode (where it provides its own buffer in one of the
        supported formats). In all other cases, @a pixelFormat together with
        @a bitsPerPixel and @a bytesPerLine define the format of the video memory
        buffer pointed to by the @a VRAM parameter and the implementation is
        free to choose which mode to use. To indicate that this frame buffer uses
        the direct mode, the implementation of the <link to="#usesGuestVRAM"/>
        attribute must return @c true and <link to="#address"/> must
        return exactly the same address that is passed in the @a VRAM parameter
        of this method; otherwise it is assumed that the indirect strategy is
        chosen.

        The @a width and @a height parameters represent the size of the
        requested display mode in both modes. In case of indirect mode, the
        provided memory buffer should be big enough to store data of the given
        display mode. In case of direct mode, it is guaranteed that the given
        @a VRAM buffer contains enough space to represent the display mode of the
        given size. Note that this frame buffer's <link to="#width"/> and <link to="#height"/> attributes must return exactly the same values as
        passed to this method after the resize is completed (see below).

        The @a finished output parameter determines if the implementation has
        finished resizing the frame buffer or not. If, for some reason, the
        resize cannot be finished immediately during this call, @a finished
        must be set to @c false, and the implementation must call
        <link to="IDisplay::resizeCompleted"/> after it has returned from
        this method as soon as possible. If @a finished is @c false, the
        machine will not call any frame buffer methods until
        <link to="IDisplay::resizeCompleted"/> is called.

        Note that if the direct mode is chosen, the <link to="#bitsPerPixel"/>,
        <link to="#bytesPerLine"/> and <link to="#pixelFormat"/> attributes of
        this frame buffer must return exactly the same values as specified in the
        parameters of this method, after the resize is completed. If the
        indirect mode is chosen, these attributes must return values describing
        the format of the implementation's own memory buffer <link to="#address"/> points to. Note also that the <link to="#bitsPerPixel"/>
        value must always correlate with <link to="#pixelFormat"/>. Note that
        the <link to="#pixelFormat"/> attribute must never return <link to="FramebufferPixelFormat_Opaque"/> regardless of the selected mode.

        
          This method is called by the IDisplay object under the
          <link to="#lock"/> provided by this IFramebuffer
          implementation. If this method returns @c false in @a finished, then
          this lock is not released until
          <link to="IDisplay::resizeCompleted"/> is called.

        in screen_id of type int
            Logical screen number. Must be used in the corresponding call to
          <link to="IDisplay::resizeCompleted"/> if this call is made.

        in pixel_format of type int
            Pixel format of the memory buffer pointed to by @a VRAM.
          See also <link to="FramebufferPixelFormat"/>.

        in vram of type str
            Pointer to the virtual video card's VRAM (may be @c null).

        in bits_per_pixel of type int
            Color depth, bits per pixel.

        in bytes_per_line of type int
            Size of one scan line, in bytes.

        in width of type int
            Width of the guest display, in pixels.

        in height of type int
            Height of the guest display, in pixels.

        return finished of type bool
            Can the VM start using the new frame buffer immediately
          after this method returns or it should wait for
          <link to="IDisplay::resizeCompleted"/>.

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(pixel_format, int):
            raise TypeError("pixel_format can only be an instance of type int")
        if type(vram) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(bits_per_pixel, int):
            raise TypeError("bits_per_pixel can only be an instance of type int")
        if not isinstance(bytes_per_line, int):
            raise TypeError("bytes_per_line can only be an instance of type int")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        finished = self._call("requestResize",
                     in_p=[screen_id, pixel_format, vram, bits_per_pixel, bytes_per_line, width, height])
        return finished

    def video_mode_supported(self, width, height, bpp):
        """Returns whether the frame buffer implementation is willing to
        support a given video mode. In case it is not able to render
        the video mode (or for some reason not willing), it should
        return @c false. Usually this method is called when the guest
        asks the VMM device whether a given video mode is supported
        so the information returned is directly exposed to the guest.
        It is important that this method returns very quickly.

        in width of type int

        in height of type int

        in bpp of type int

        return supported of type bool

        """
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        if not isinstance(bpp, int):
            raise TypeError("bpp can only be an instance of type int")
        supported = self._call("videoModeSupported",
                     in_p=[width, height, bpp])
        return supported

    def get_visible_region(self, rectangles, count):
        """Returns the visible region of this frame buffer.

        If the @a rectangles parameter is @c null then the value of the
        @a count parameter is ignored and the number of elements necessary to
        describe the current visible region is returned in @a countCopied.

        If @a rectangles is not @c null but @a count is less
        than the required number of elements to store region data, the method
        will report a failure. If @a count is equal or greater than the
        required number of elements, then the actual number of elements copied
        to the provided array will be returned in @a countCopied.

        
          The address of the provided array must be in the process space of
          this IFramebuffer object.
        
        
          Method not yet implemented.

        in rectangles of type str
            Pointer to the @c RTRECT array to receive region data.

        in count of type int
            Number of @c RTRECT elements in the @a rectangles array.

        return count_copied of type int
            Number of elements copied to the @a rectangles array.

        """
        if type(rectangles) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(count, int):
            raise TypeError("count can only be an instance of type int")
        count_copied = self._call("getVisibleRegion",
                     in_p=[rectangles, count])
        return count_copied

    def set_visible_region(self, rectangles, count):
        """Suggests a new visible region to this frame buffer. This region
        represents the area of the VM display which is a union of regions of
        all top-level windows of the guest operating system running inside the
        VM (if the Guest Additions for this system support this
        functionality). This information may be used by the frontends to
        implement the seamless desktop integration feature.

        
          The address of the provided array must be in the process space of
          this IFramebuffer object.
        
        
          The IFramebuffer implementation must make a copy of the provided
          array of rectangles.
        
        
          Method not yet implemented.

        in rectangles of type str
            Pointer to the @c RTRECT array.

        in count of type int
            Number of @c RTRECT elements in the @a rectangles array.

        """
        if type(rectangles) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(count, int):
            raise TypeError("count can only be an instance of type int")
        self._call("setVisibleRegion",
                     in_p=[rectangles, count])

    def process_vhwa_command(self, command):
        """Posts a Video HW Acceleration Command to the frame buffer for processing.
        The commands used for 2D video acceleration (DDraw surface creation/destroying, blitting, scaling, color conversion, overlaying, etc.)
        are posted from quest to the host to be processed by the host hardware.

        
          The address of the provided command must be in the process space of
          this IFramebuffer object.

        in command of type str
            Pointer to VBOXVHWACMD containing the command to execute.

        """
        if type(command) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("processVHWACommand",
                     in_p=[command])

    def notify3_d_event(self, type_p, reserved):
        """Notifies framebuffer about 3D backend event.

        in type_p of type int
            event type. Currently only VBOX3D_NOTIFY_EVENT_TYPE_VISIBLE_WINDOW is supported.

        in reserved of type str
            Reserved for future use, must be NULL.

        """
        if not isinstance(type_p, int):
            raise TypeError("type_p can only be an instance of type int")
        if type(reserved) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("notify3DEvent",
                     in_p=[type_p, reserved])


class IFramebufferOverlay(IFramebuffer):
    """
    The IFramebufferOverlay interface represents an alpha blended overlay
      for displaying status icons above an IFramebuffer. It is always created
      not visible, so that it must be explicitly shown. It only covers a
      portion of the IFramebuffer, determined by its width, height and
      co-ordinates. It is always in packed pixel little-endian 32bit ARGB (in
      that order) format, and may be written to directly. Do re-read the
      width though, after setting it, as it may be adjusted (increased) to
      make it more suitable for the front end.
    """
    __uuid__ = '0bcc1c7e-e415-47d2-bfdb-e4c705fb0f47'
    __wsmap__ = 'managed'
    
    @property
    def x(self):
        """Get int value for 'x'
        X position of the overlay, relative to the frame buffer.
        """
        ret = self._get_attr("x")
        return ret

    @property
    def y(self):
        """Get int value for 'y'
        Y position of the overlay, relative to the frame buffer.
        """
        ret = self._get_attr("y")
        return ret

    @property
    def visible(self):
        """Get or set bool value for 'visible'
        Whether the overlay is currently visible.
        """
        ret = self._get_attr("visible")
        return ret

    @visible.setter
    def visible(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("visible", value)

    @property
    def alpha(self):
        """Get or set int value for 'alpha'
        The global alpha value for the overlay. This may or may not be
        supported by a given front end.
        """
        ret = self._get_attr("alpha")
        return ret

    @alpha.setter
    def alpha(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("alpha", value)

    def move(self, x, y):
        """Changes the overlay's position relative to the IFramebuffer.

        in x of type int

        in y of type int

        """
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        self._call("move",
                     in_p=[x, y])


class IDisplay(Interface):
    """
    The IDisplay interface represents the virtual machine's display.

      The object implementing this interface is contained in each
      <link to="IConsole::display"/> attribute and represents the visual
      output of the virtual machine.

      The virtual display supports pluggable output targets represented by the
      IFramebuffer interface. Examples of the output target are a window on
      the host computer or an RDP session's display on a remote computer.
    """
    __uuid__ = '23efdcab-1ae5-47ee-951e-e0f9a3935f2a'
    __wsmap__ = 'managed'
    
    def get_screen_resolution(self, screen_id):
        """Queries display width, height and color depth for given screen.

        in screen_id of type int

        out width of type int

        out height of type int

        out bits_per_pixel of type int

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (width, height, bits_per_pixel) = self._call("getScreenResolution",
                     in_p=[screen_id])
        return (width, height, bits_per_pixel)

    def set_framebuffer(self, screen_id, framebuffer):
        """Sets the framebuffer for given screen.

        in screen_id of type int

        in framebuffer of type IFramebuffer

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(framebuffer, IFramebuffer):
            raise TypeError("framebuffer can only be an instance of type IFramebuffer")
        self._call("setFramebuffer",
                     in_p=[screen_id, framebuffer])

    def get_framebuffer(self, screen_id):
        """Queries the framebuffer for given screen.

        in screen_id of type int

        out framebuffer of type IFramebuffer

        out x_origin of type int

        out y_origin of type int

        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        (framebuffer, x_origin, y_origin) = self._call("getFramebuffer",
                     in_p=[screen_id])
        framebuffer = IFramebuffer(framebuffer)
        return (framebuffer, x_origin, y_origin)

    def set_video_mode_hint(self, display, enabled, change_origin, origin_x, origin_y, width, height, bits_per_pixel):
        """Asks VirtualBox to request the given video mode from
        the guest. This is just a hint and it cannot be guaranteed
        that the requested resolution will be used. Guest Additions
        are required for the request to be seen by guests. The caller
        should issue the request and wait for a resolution change and
        after a timeout retry.

        Specifying @c 0 for either @a width, @a height or @a bitsPerPixel
        parameters means that the corresponding values should be taken from the
        current video mode (i.e. left unchanged).

        If the guest OS supports multi-monitor configuration then the @a display
        parameter specifies the number of the guest display to send the hint to:
        @c 0 is the primary display, @c 1 is the first secondary and
        so on. If the multi-monitor configuration is not supported, @a display
        must be @c 0.

        in display of type int
            The number of the guest display to send the hint to.

        in enabled of type bool
            @c True, if this guest screen is enabled,
          @c False otherwise.

        in change_origin of type bool
            @c True, if the origin of the guest screen should be changed,
          @c False otherwise.

        in origin_x of type int
            The X origin of the guest screen.

        in origin_y of type int
            The Y origin of the guest screen.

        in width of type int

        in height of type int

        in bits_per_pixel of type int

        raises E_INVALIDARG
            The @a display is not associated with any monitor.
        
        """
        if not isinstance(display, int):
            raise TypeError("display can only be an instance of type int")
        if not isinstance(enabled, bool):
            raise TypeError("enabled can only be an instance of type bool")
        if not isinstance(change_origin, bool):
            raise TypeError("change_origin can only be an instance of type bool")
        if not isinstance(origin_x, int):
            raise TypeError("origin_x can only be an instance of type int")
        if not isinstance(origin_y, int):
            raise TypeError("origin_y can only be an instance of type int")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        if not isinstance(bits_per_pixel, int):
            raise TypeError("bits_per_pixel can only be an instance of type int")
        self._call("setVideoModeHint",
                     in_p=[display, enabled, change_origin, origin_x, origin_y, width, height, bits_per_pixel])

    def set_seamless_mode(self, enabled):
        """Enables or disables seamless guest display rendering (seamless desktop
        integration) mode.
        
          Calling this method has no effect if <link to="IGuest::getFacilityStatus"/> with facility @c Seamless
          does not return @c Active.

        in enabled of type bool

        """
        if not isinstance(enabled, bool):
            raise TypeError("enabled can only be an instance of type bool")
        self._call("setSeamlessMode",
                     in_p=[enabled])

    def take_screen_shot(self, screen_id, address, width, height):
        """Takes a screen shot of the requested size and copies it to the
        32-bpp buffer allocated by the caller and pointed to by @a address.
        A pixel consists of 4 bytes in order: B, G, R, 0.

        This API can be used only locally by a VM process through the
            COM/XPCOM C++ API as it requires pointer support. It is not
            available for scripting langages, Java or any webservice clients.
            Unless you are writing a new VM frontend use
            <link to="#takeScreenShotToArray"/>.

        in screen_id of type int

        in address of type str

        in width of type int

        in height of type int

        raises E_NOTIMPL
            Feature not implemented.
        
        raises VBOX_E_IPRT_ERROR
            Could not take a screenshot.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if type(address) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        self._call("takeScreenShot",
                     in_p=[screen_id, address, width, height])

    def take_screen_shot_to_array(self, screen_id, width, height):
        """Takes a guest screen shot of the requested size and returns it as
        an array of bytes in uncompressed 32-bpp RGBA format.
        A pixel consists of 4 bytes in order: R, G, B, 0xFF.

        This API is slow, but could be the only option to get guest screenshot
        for scriptable languages not allowed to manipulate with addresses
        directly.

        in screen_id of type int
            Monitor to take screenshot from.

        in width of type int
            Desired image width.

        in height of type int
            Desired image height.

        return screen_data of type str
            Array with resulting screen data.

        raises E_NOTIMPL
            Feature not implemented.
        
        raises VBOX_E_IPRT_ERROR
            Could not take a screenshot.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        screen_data = self._call("takeScreenShotToArray",
                     in_p=[screen_id, width, height])
        return screen_data

    def take_screen_shot_png_to_array(self, screen_id, width, height):
        """Takes a guest screen shot of the requested size and returns it as
        PNG image in array.

        in screen_id of type int
            Monitor to take the screenshot from.

        in width of type int
            Desired image width.

        in height of type int
            Desired image height.

        return screen_data of type str
            Array with resulting screen data.

        raises E_NOTIMPL
            Feature not implemented.
        
        raises VBOX_E_IPRT_ERROR
            Could not take a screenshot.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        screen_data = self._call("takeScreenShotPNGToArray",
                     in_p=[screen_id, width, height])
        return screen_data

    def draw_to_screen(self, screen_id, address, x, y, width, height):
        """Draws a 32-bpp image of the specified size from the given buffer
        to the given point on the VM display.

        in screen_id of type int
            Monitor to take the screenshot from.

        in address of type str
            Address to store the screenshot to

        in x of type int
            Relative to the screen top left corner.

        in y of type int
            Relative to the screen top left corner.

        in width of type int
            Desired image width.

        in height of type int
            Desired image height.

        raises E_NOTIMPL
            Feature not implemented.
        
        raises VBOX_E_IPRT_ERROR
            Could not draw to screen.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if type(address) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        self._call("drawToScreen",
                     in_p=[screen_id, address, x, y, width, height])

    def invalidate_and_update(self):
        """Does a full invalidation of the VM display and instructs the VM
        to update it.

        raises VBOX_E_IPRT_ERROR
            Could not invalidate and update screen.
        
        """
        self._call("invalidateAndUpdate")

    def resize_completed(self, screen_id):
        """Signals that a framebuffer has completed the resize operation.

        in screen_id of type int

        raises VBOX_E_NOT_SUPPORTED
            Operation only valid for external frame buffers.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        self._call("resizeCompleted",
                     in_p=[screen_id])

    def complete_vhwa_command(self, command):
        """Signals that the Video HW Acceleration command has completed.

        in command of type str
            Pointer to VBOXVHWACMD containing the completed command.

        """
        if type(command) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("completeVHWACommand",
                     in_p=[command])

    def viewport_changed(self, screen_id, x, y, width, height):
        """Signals that framebuffer window viewport has changed.

        in screen_id of type int
            Monitor to take the screenshot from.

        in x of type int
            Framebuffer x offset.

        in y of type int
            Framebuffer y offset.

        in width of type int
            Viewport width.

        in height of type int
            Viewport height.

        raises E_INVALIDARG
            The specified viewport data is invalid.
        
        """
        if not isinstance(screen_id, int):
            raise TypeError("screen_id can only be an instance of type int")
        if not isinstance(x, int):
            raise TypeError("x can only be an instance of type int")
        if not isinstance(y, int):
            raise TypeError("y can only be an instance of type int")
        if not isinstance(width, int):
            raise TypeError("width can only be an instance of type int")
        if not isinstance(height, int):
            raise TypeError("height can only be an instance of type int")
        self._call("viewportChanged",
                     in_p=[screen_id, x, y, width, height])


class INetworkAdapter(Interface):
    """
    Represents a virtual network adapter that is attached to a virtual machine.
        Each virtual machine has a fixed number of network adapter slots with one
        instance of this attached to each of them. Call
        <link to="IMachine::getNetworkAdapter"/> to get the network adapter that
        is attached to a given slot in a given machine.

        Each network adapter can be in one of five attachment modes, which are
        represented by the <link to="NetworkAttachmentType"/> enumeration;
        see the <link to="#attachmentType"/> attribute.
    """
    __uuid__ = 'efa0f965-63c7-4c60-afdf-b1cc9943b9c0'
    __wsmap__ = 'managed'
    
    @property
    def adapter_type(self):
        """Get or set NetworkAdapterType value for 'adapterType'
        Type of the virtual network adapter. Depending on this value,
        VirtualBox will provide a different virtual network hardware
        to the guest.
        """
        ret = self._get_attr("adapterType")
        return NetworkAdapterType(ret)

    @adapter_type.setter
    def adapter_type(self, value):
        if not isinstance(value, NetworkAdapterType):
            raise TypeError("value is not an instance of NetworkAdapterType")
        return self._set_attr("adapterType", value)

    @property
    def slot(self):
        """Get int value for 'slot'
        Slot number this adapter is plugged into. Corresponds to
        the value you pass to <link to="IMachine::getNetworkAdapter"/>
        to obtain this instance.
        """
        ret = self._get_attr("slot")
        return ret

    @property
    def enabled(self):
        """Get or set bool value for 'enabled'
        Flag whether the network adapter is present in the
        guest system. If disabled, the virtual guest hardware will
        not contain this network adapter. Can only be changed when
        the VM is not running.
        """
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def mac_address(self):
        """Get or set str value for 'MACAddress'
        Ethernet MAC address of the adapter, 12 hexadecimal characters. When setting
        it to @c null or an empty string, VirtualBox will generate a unique MAC address.
        """
        ret = self._get_attr("MACAddress")
        return ret

    @mac_address.setter
    def mac_address(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("MACAddress", value)

    @property
    def attachment_type(self):
        """Get or set NetworkAttachmentType value for 'attachmentType'
        Sets/Gets network attachment type of this network adapter.
        """
        ret = self._get_attr("attachmentType")
        return NetworkAttachmentType(ret)

    @attachment_type.setter
    def attachment_type(self, value):
        if not isinstance(value, NetworkAttachmentType):
            raise TypeError("value is not an instance of NetworkAttachmentType")
        return self._set_attr("attachmentType", value)

    @property
    def bridged_interface(self):
        """Get or set str value for 'bridgedInterface'
        Name of the network interface the VM should be bridged to.
        """
        ret = self._get_attr("bridgedInterface")
        return ret

    @bridged_interface.setter
    def bridged_interface(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("bridgedInterface", value)

    @property
    def host_only_interface(self):
        """Get or set str value for 'hostOnlyInterface'
        Name of the host only network interface the VM is attached to.
        """
        ret = self._get_attr("hostOnlyInterface")
        return ret

    @host_only_interface.setter
    def host_only_interface(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("hostOnlyInterface", value)

    @property
    def internal_network(self):
        """Get or set str value for 'internalNetwork'
        Name of the internal network the VM is attached to.
        """
        ret = self._get_attr("internalNetwork")
        return ret

    @internal_network.setter
    def internal_network(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("internalNetwork", value)

    @property
    def nat_network(self):
        """Get or set str value for 'NATNetwork'
        Name of the NAT network the VM is attached to.
        """
        ret = self._get_attr("NATNetwork")
        return ret

    @nat_network.setter
    def nat_network(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("NATNetwork", value)

    @property
    def generic_driver(self):
        """Get or set str value for 'genericDriver'
        Name of the driver to use for the "Generic" network attachment type.
        """
        ret = self._get_attr("genericDriver")
        return ret

    @generic_driver.setter
    def generic_driver(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("genericDriver", value)

    @property
    def cable_connected(self):
        """Get or set bool value for 'cableConnected'
        Flag whether the adapter reports the cable as connected or not.
        It can be used to report offline situations to a VM.
        """
        ret = self._get_attr("cableConnected")
        return ret

    @cable_connected.setter
    def cable_connected(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("cableConnected", value)

    @property
    def line_speed(self):
        """Get or set int value for 'lineSpeed'
        Line speed reported by custom drivers, in units of 1 kbps.
        """
        ret = self._get_attr("lineSpeed")
        return ret

    @line_speed.setter
    def line_speed(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("lineSpeed", value)

    @property
    def promisc_mode_policy(self):
        """Get or set NetworkAdapterPromiscModePolicy value for 'promiscModePolicy'
        The promiscuous mode policy of the network adapter when attached to an
        internal network, host only network or a bridge.
        """
        ret = self._get_attr("promiscModePolicy")
        return NetworkAdapterPromiscModePolicy(ret)

    @promisc_mode_policy.setter
    def promisc_mode_policy(self, value):
        if not isinstance(value, NetworkAdapterPromiscModePolicy):
            raise TypeError("value is not an instance of NetworkAdapterPromiscModePolicy")
        return self._set_attr("promiscModePolicy", value)

    @property
    def trace_enabled(self):
        """Get or set bool value for 'traceEnabled'
        Flag whether network traffic from/to the network card should be traced.
        Can only be toggled when the VM is turned off.
        """
        ret = self._get_attr("traceEnabled")
        return ret

    @trace_enabled.setter
    def trace_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("traceEnabled", value)

    @property
    def trace_file(self):
        """Get or set str value for 'traceFile'
        Filename where a network trace will be stored. If not set, VBox-pid.pcap
        will be used.
        """
        ret = self._get_attr("traceFile")
        return ret

    @trace_file.setter
    def trace_file(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("traceFile", value)

    @property
    def nat_engine(self):
        """Get INATEngine value for 'NATEngine'
        Points to the NAT engine which handles the network address translation
        for this interface. This is active only when the interface actually uses
        NAT.
        """
        ret = self._get_attr("NATEngine")
        return INATEngine(ret)

    @property
    def boot_priority(self):
        """Get or set int value for 'bootPriority'
        Network boot priority of the adapter. Priority 1 is highest. If not set,
        the priority is considered to be at the lowest possible setting.
        """
        ret = self._get_attr("bootPriority")
        return ret

    @boot_priority.setter
    def boot_priority(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("bootPriority", value)

    @property
    def bandwidth_group(self):
        """Get or set IBandwidthGroup value for 'bandwidthGroup'
        The bandwidth group this network adapter is assigned to.
        """
        ret = self._get_attr("bandwidthGroup")
        return IBandwidthGroup(ret)

    @bandwidth_group.setter
    def bandwidth_group(self, value):
        if not isinstance(value, IBandwidthGroup):
            raise TypeError("value is not an instance of IBandwidthGroup")
        return self._set_attr("bandwidthGroup", value)

    def get_property(self, key):
        """Returns the value of the network attachment property with the given name.

        If the requested data @a key does not exist, this function will
        succeed and return an empty string in the @a value argument.

        in key of type str
            Name of the property to get.

        return value of type str
            Current property value.

        raises E_INVALIDARG
            @a name is @c null or empty.
        
        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getProperty",
                     in_p=[key])
        return value

    def set_property(self, key, value):
        """Sets the value of the network attachment property with the given name.

        Setting the property value to @c null or an empty string is equivalent
        to deleting the existing value.

        in key of type str
            Name of the property to set.

        in value of type str
            Property value to set.

        raises E_INVALIDARG
            @a name is @c null or empty.
        
        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setProperty",
                     in_p=[key, value])

    def get_properties(self, names):
        """Returns values for a group of properties in one call.

        The names of the properties to get are specified using the @a names
        argument which is a list of comma-separated property names or
        an empty string if all properties are to be returned.
        Currently the value of this argument is ignored and the method
        always returns all existing properties.

        The method returns two arrays, the array of property names corresponding
        to the @a names argument and the current values of these properties.
        Both arrays have the same number of elements with each element at the
        given index in the first array corresponds to an element at the same
        index in the second array.

        in names of type str
            Names of properties to get.

        out return_names of type str
            Names of returned properties.

        return return_values of type str
            Values of returned properties.

        """
        if type(names) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        (return_names, return_values) = self._call("getProperties",
                     in_p=[names])
        return (return_names, return_values)


class ISerialPort(Interface):
    """
    The ISerialPort interface represents the virtual serial port device.

      The virtual serial port device acts like an ordinary serial port
      inside the virtual machine. This device communicates to the real
      serial port hardware in one of two modes: host pipe or host device.

      In host pipe mode, the #path attribute specifies the path to the pipe on
      the host computer that represents a serial port. The #server attribute
      determines if this pipe is created by the virtual machine process at
      machine startup or it must already exist before starting machine
      execution.

      In host device mode, the #path attribute specifies the name of the
      serial port device on the host computer.

      There is also a third communication mode: the disconnected mode. In this
      mode, the guest OS running inside the virtual machine will be able to
      detect the serial port, but all port write operations will be discarded
      and all port read operations will return no data.

      <link to="IMachine::getSerialPort"/>
    """
    __uuid__ = '937f6970-5103-4745-b78e-d28dcf1479a8'
    __wsmap__ = 'managed'
    
    @property
    def slot(self):
        """Get int value for 'slot'
        Slot number this serial port is plugged into. Corresponds to
        the value you pass to <link to="IMachine::getSerialPort"/>
        to obtain this instance.
        """
        ret = self._get_attr("slot")
        return ret

    @property
    def enabled(self):
        """Get or set bool value for 'enabled'
        Flag whether the serial port is enabled. If disabled,
        the serial port will not be reported to the guest OS.
        """
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def io_base(self):
        """Get or set int value for 'IOBase'
        Base I/O address of the serial port.
        """
        ret = self._get_attr("IOBase")
        return ret

    @io_base.setter
    def io_base(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("IOBase", value)

    @property
    def irq(self):
        """Get or set int value for 'IRQ'
        IRQ number of the serial port.
        """
        ret = self._get_attr("IRQ")
        return ret

    @irq.setter
    def irq(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("IRQ", value)

    @property
    def host_mode(self):
        """Get or set PortMode value for 'hostMode'
        How is this port connected to the host.
        
          Changing this attribute may fail if the conditions for
          <link to="#path"/> are not met.
        """
        ret = self._get_attr("hostMode")
        return PortMode(ret)

    @host_mode.setter
    def host_mode(self, value):
        if not isinstance(value, PortMode):
            raise TypeError("value is not an instance of PortMode")
        return self._set_attr("hostMode", value)

    @property
    def server(self):
        """Get or set bool value for 'server'
        Flag whether this serial port acts as a server (creates a new pipe on
        the host) or as a client (uses the existing pipe). This attribute is
        used only when <link to="#hostMode"/> is PortMode_HostPipe.
        """
        ret = self._get_attr("server")
        return ret

    @server.setter
    def server(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("server", value)

    @property
    def path(self):
        """Get or set str value for 'path'
        Path to the serial port's pipe on the host when <link to="ISerialPort::hostMode"/> is
        PortMode_HostPipe, or the host serial device name when
        <link to="ISerialPort::hostMode"/> is PortMode_HostDevice. For both
        cases, setting a @c null or empty string as the attribute's value
        is an error. Otherwise, the value of this property is ignored.
        """
        ret = self._get_attr("path")
        return ret

    @path.setter
    def path(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("path", value)


class IParallelPort(Interface):
    """
    The IParallelPort interface represents the virtual parallel port device.

      The virtual parallel port device acts like an ordinary parallel port
      inside the virtual machine. This device communicates to the real
      parallel port hardware using the name of the parallel device on the host
      computer specified in the #path attribute.

      Each virtual parallel port device is assigned a base I/O address and an
      IRQ number that will be reported to the guest operating system and used
      to operate the given parallel port from within the virtual machine.

      <link to="IMachine::getParallelPort"/>
    """
    __uuid__ = '0c925f06-dd10-4b77-8de8-294d738c3214'
    __wsmap__ = 'managed'
    
    @property
    def slot(self):
        """Get int value for 'slot'
        Slot number this parallel port is plugged into. Corresponds to
        the value you pass to <link to="IMachine::getParallelPort"/>
        to obtain this instance.
        """
        ret = self._get_attr("slot")
        return ret

    @property
    def enabled(self):
        """Get or set bool value for 'enabled'
        Flag whether the parallel port is enabled. If disabled,
        the parallel port will not be reported to the guest OS.
        """
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def io_base(self):
        """Get or set int value for 'IOBase'
        Base I/O address of the parallel port.
        """
        ret = self._get_attr("IOBase")
        return ret

    @io_base.setter
    def io_base(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("IOBase", value)

    @property
    def irq(self):
        """Get or set int value for 'IRQ'
        IRQ number of the parallel port.
        """
        ret = self._get_attr("IRQ")
        return ret

    @irq.setter
    def irq(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("IRQ", value)

    @property
    def path(self):
        """Get or set str value for 'path'
        Host parallel device name. If this parallel port is enabled, setting a
        @c null or an empty string as this attribute's value will result in
        an error.
        """
        ret = self._get_attr("path")
        return ret

    @path.setter
    def path(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("path", value)


class IMachineDebugger(Interface):
    """
    Takes a core dump of the guest.

        See include/VBox/dbgfcorefmt.h for details on the file format.
    """
    __uuid__ = '5e4534dc-21b8-4f6b-8a08-eef50e1a0aa1'
    __wsmap__ = 'managed'
    
    def dump_guest_core(self, filename, compression):
        """Takes a core dump of the guest.

        See include/VBox/dbgfcorefmt.h for details on the file format.

        in filename of type str
            The name of the output file. The file must not exist.

        in compression of type str
            Reserved for future compression method indicator.

        """
        if type(filename) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(compression) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("dumpGuestCore",
                     in_p=[filename, compression])

    def dump_host_process_core(self, filename, compression):
        """Takes a core dump of the VM process on the host.

        This feature is not implemented in the 4.0.0 release but it may show up
        in a dot release.

        in filename of type str
            The name of the output file. The file must not exist.

        in compression of type str
            Reserved for future compression method indicator.

        """
        if type(filename) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(compression) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("dumpHostProcessCore",
                     in_p=[filename, compression])

    def info(self, name, args):
        """Interfaces with the info dumpers (DBGFInfo).

        This feature is not implemented in the 4.0.0 release but it may show up
        in a dot release.

        in name of type str
            The name of the info item.

        in args of type str
            Arguments to the info dumper.

        return info of type str
            The into string.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(args) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        info = self._call("info",
                     in_p=[name, args])
        return info

    def inject_nmi(self):
        """Inject an NMI into a running VT-x/AMD-V VM.

        """
        self._call("injectNMI")

    def modify_log_groups(self, settings):
        """Modifies the group settings of the debug or release logger.

        in settings of type str
            The group settings string. See iprt/log.h for details. To target the
          release logger, prefix the string with "release:".

        """
        if type(settings) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("modifyLogGroups",
                     in_p=[settings])

    def modify_log_flags(self, settings):
        """Modifies the debug or release logger flags.

        in settings of type str
            The flags settings string. See iprt/log.h for details. To target the
          release logger, prefix the string with "release:".

        """
        if type(settings) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("modifyLogFlags",
                     in_p=[settings])

    def modify_log_destinations(self, settings):
        """Modifies the debug or release logger destinations.

        in settings of type str
            The destination settings string. See iprt/log.h for details. To target the
          release logger, prefix the string with "release:".

        """
        if type(settings) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("modifyLogDestinations",
                     in_p=[settings])

    def read_physical_memory(self, address, size):
        """Reads guest physical memory, no side effects (MMIO++).

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in address of type int
            The guest physical address.

        in size of type int
            The number of bytes to read.

        return bytes_p of type str
            The bytes read.

        """
        if not isinstance(address, int):
            raise TypeError("address can only be an instance of type int")
        if not isinstance(size, int):
            raise TypeError("size can only be an instance of type int")
        bytes_p = self._call("readPhysicalMemory",
                     in_p=[address, size])
        return bytes_p

    def write_physical_memory(self, address, size, bytes_p):
        """Writes guest physical memory, access handles (MMIO++) are ignored.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in address of type int
            The guest physical address.

        in size of type int
            The number of bytes to read.

        in bytes_p of type str
            The bytes to write.

        """
        if not isinstance(address, int):
            raise TypeError("address can only be an instance of type int")
        if not isinstance(size, int):
            raise TypeError("size can only be an instance of type int")
        if not isinstance(bytes_p, list):
            raise TypeError("bytes_p can only be an instance of type list")
        for a in bytes_p[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        self._call("writePhysicalMemory",
                     in_p=[address, size, bytes_p])

    def read_virtual_memory(self, cpu_id, address, size):
        """Reads guest virtual memory, no side effects (MMIO++).

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in cpu_id of type int
            The identifier of the Virtual CPU.

        in address of type int
            The guest virtual address.

        in size of type int
            The number of bytes to read.

        return bytes_p of type str
            The bytes read.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        if not isinstance(address, int):
            raise TypeError("address can only be an instance of type int")
        if not isinstance(size, int):
            raise TypeError("size can only be an instance of type int")
        bytes_p = self._call("readVirtualMemory",
                     in_p=[cpu_id, address, size])
        return bytes_p

    def write_virtual_memory(self, cpu_id, address, size, bytes_p):
        """Writes guest virtual memory, access handles (MMIO++) are ignored.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in cpu_id of type int
            The identifier of the Virtual CPU.

        in address of type int
            The guest virtual address.

        in size of type int
            The number of bytes to read.

        in bytes_p of type str
            The bytes to write.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        if not isinstance(address, int):
            raise TypeError("address can only be an instance of type int")
        if not isinstance(size, int):
            raise TypeError("size can only be an instance of type int")
        if not isinstance(bytes_p, list):
            raise TypeError("bytes_p can only be an instance of type list")
        for a in bytes_p[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        self._call("writeVirtualMemory",
                     in_p=[cpu_id, address, size, bytes_p])

    def detect_os(self):
        """Tries to (re-)detect the guest OS kernel.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        return os of type str
            The detected OS kernel on success.

        """
        os = self._call("detectOS")
        return os

    def get_register(self, cpu_id, name):
        """Gets one register.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in cpu_id of type int
            The identifier of the Virtual CPU.

        in name of type str
            The register name, case is ignored.

        return value of type str
            The register value. This is usually a hex value (always 0x prefixed)
          but other format may be used for floating point registers (TBD).

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getRegister",
                     in_p=[cpu_id, name])
        return value

    def get_registers(self, cpu_id):
        """Gets all the registers for the given CPU.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in cpu_id of type int
            The identifier of the Virtual CPU.

        out names of type str
            Array containing the lowercase register names.

        out values of type str
            Array paralell to the names holding the register values as if the
          register was returned by <link to="IMachineDebugger::getRegister"/>.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        (names, values) = self._call("getRegisters",
                     in_p=[cpu_id])
        return (names, values)

    def set_register(self, cpu_id, name, value):
        """Gets one register.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in cpu_id of type int
            The identifier of the Virtual CPU.

        in name of type str
            The register name, case is ignored.

        in value of type str
            The new register value. Hexadecimal, decimal and octal formattings
          are supported in addition to any special formattings returned by
          the getters.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setRegister",
                     in_p=[cpu_id, name, value])

    def set_registers(self, cpu_id, names, values):
        """Sets zero or more registers atomically.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in cpu_id of type int
            The identifier of the Virtual CPU.

        in names of type str
            Array containing the register names, case ignored.

        in values of type str
            Array paralell to the names holding the register values. See
          <link to="IMachineDebugger::setRegister"/> for formatting
          guidelines.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        if not isinstance(names, list):
            raise TypeError("names can only be an instance of type list")
        for a in names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(values, list):
            raise TypeError("values can only be an instance of type list")
        for a in values[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        self._call("setRegisters",
                     in_p=[cpu_id, names, values])

    def dump_guest_stack(self, cpu_id):
        """Produce a simple stack dump using the current guest state.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.

        in cpu_id of type int
            The identifier of the Virtual CPU.

        return stack of type str
            String containing the formatted stack dump.

        """
        if not isinstance(cpu_id, int):
            raise TypeError("cpu_id can only be an instance of type int")
        stack = self._call("dumpGuestStack",
                     in_p=[cpu_id])
        return stack

    def reset_stats(self, pattern):
        """Reset VM statistics.

        in pattern of type str
            The selection pattern. A bit similar to filename globbing.

        """
        if type(pattern) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("resetStats",
                     in_p=[pattern])

    def dump_stats(self, pattern):
        """Dumps VM statistics.

        in pattern of type str
            The selection pattern. A bit similar to filename globbing.

        """
        if type(pattern) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("dumpStats",
                     in_p=[pattern])

    def get_stats(self, pattern, with_descriptions):
        """Get the VM statistics in a XMLish format.

        in pattern of type str
            The selection pattern. A bit similar to filename globbing.

        in with_descriptions of type bool
            Whether to include the descriptions.

        return stats of type str
            The XML document containing the statistics.

        """
        if type(pattern) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(with_descriptions, bool):
            raise TypeError("with_descriptions can only be an instance of type bool")
        stats = self._call("getStats",
                     in_p=[pattern, with_descriptions])
        return stats

    @property
    def single_step(self):
        """Get or set bool value for 'singleStep'
        Switch for enabling single-stepping.
        """
        ret = self._get_attr("singleStep")
        return ret

    @single_step.setter
    def single_step(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("singleStep", value)

    @property
    def recompile_user(self):
        """Get or set bool value for 'recompileUser'
        Switch for forcing code recompilation for user mode code.
        """
        ret = self._get_attr("recompileUser")
        return ret

    @recompile_user.setter
    def recompile_user(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("recompileUser", value)

    @property
    def recompile_supervisor(self):
        """Get or set bool value for 'recompileSupervisor'
        Switch for forcing code recompilation for supervisor mode code.
        """
        ret = self._get_attr("recompileSupervisor")
        return ret

    @recompile_supervisor.setter
    def recompile_supervisor(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("recompileSupervisor", value)

    @property
    def execute_all_in_iem(self):
        """Get or set bool value for 'executeAllInIEM'
        Whether to execute all the code in the instruction interpreter. This
        is mainly for testing the interpreter and not an execution mode
        intended for general consumption.
        """
        ret = self._get_attr("executeAllInIEM")
        return ret

    @execute_all_in_iem.setter
    def execute_all_in_iem(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("executeAllInIEM", value)

    @property
    def patm_enabled(self):
        """Get or set bool value for 'PATMEnabled'
        Switch for enabling and disabling the PATM component.
        """
        ret = self._get_attr("PATMEnabled")
        return ret

    @patm_enabled.setter
    def patm_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("PATMEnabled", value)

    @property
    def csam_enabled(self):
        """Get or set bool value for 'CSAMEnabled'
        Switch for enabling and disabling the CSAM component.
        """
        ret = self._get_attr("CSAMEnabled")
        return ret

    @csam_enabled.setter
    def csam_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("CSAMEnabled", value)

    @property
    def log_enabled(self):
        """Get or set bool value for 'logEnabled'
        Switch for enabling and disabling the debug logger.
        """
        ret = self._get_attr("logEnabled")
        return ret

    @log_enabled.setter
    def log_enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("logEnabled", value)

    @property
    def log_dbg_flags(self):
        """Get str value for 'logDbgFlags'
        The debug logger flags.
        """
        ret = self._get_attr("logDbgFlags")
        return ret

    @property
    def log_dbg_groups(self):
        """Get str value for 'logDbgGroups'
        The debug logger's group settings.
        """
        ret = self._get_attr("logDbgGroups")
        return ret

    @property
    def log_dbg_destinations(self):
        """Get str value for 'logDbgDestinations'
        The debug logger's destination settings.
        """
        ret = self._get_attr("logDbgDestinations")
        return ret

    @property
    def log_rel_flags(self):
        """Get str value for 'logRelFlags'
        The release logger flags.
        """
        ret = self._get_attr("logRelFlags")
        return ret

    @property
    def log_rel_groups(self):
        """Get str value for 'logRelGroups'
        The release logger's group settings.
        """
        ret = self._get_attr("logRelGroups")
        return ret

    @property
    def log_rel_destinations(self):
        """Get str value for 'logRelDestinations'
        The relase logger's destination settings.
        """
        ret = self._get_attr("logRelDestinations")
        return ret

    @property
    def hw_virt_ex_enabled(self):
        """Get bool value for 'HWVirtExEnabled'
        Flag indicating whether the VM is currently making use of CPU hardware
        virtualization extensions.
        """
        ret = self._get_attr("HWVirtExEnabled")
        return ret

    @property
    def hw_virt_ex_nested_paging_enabled(self):
        """Get bool value for 'HWVirtExNestedPagingEnabled'
        Flag indicating whether the VM is currently making use of the nested paging
        CPU hardware virtualization extension.
        """
        ret = self._get_attr("HWVirtExNestedPagingEnabled")
        return ret

    @property
    def hw_virt_ex_vpid_enabled(self):
        """Get bool value for 'HWVirtExVPIDEnabled'
        Flag indicating whether the VM is currently making use of the VPID
        VT-x extension.
        """
        ret = self._get_attr("HWVirtExVPIDEnabled")
        return ret

    @property
    def hw_virt_ex_ux_enabled(self):
        """Get bool value for 'HWVirtExUXEnabled'
        Flag indicating whether the VM is currently making use of the
        unrestricted execution feature of VT-x.
        """
        ret = self._get_attr("HWVirtExUXEnabled")
        return ret

    @property
    def os_name(self):
        """Get str value for 'OSName'
        Query the guest OS kernel name as detected by the DBGF.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.
        """
        ret = self._get_attr("OSName")
        return ret

    @property
    def os_version(self):
        """Get str value for 'OSVersion'
        Query the guest OS kernel version string as detected by the DBGF.

        This feature is not implemented in the 4.0.0 release but may show up
        in a dot release.
        """
        ret = self._get_attr("OSVersion")
        return ret

    @property
    def pae_enabled(self):
        """Get bool value for 'PAEEnabled'
        Flag indicating whether the VM is currently making use of the Physical
        Address Extension CPU feature.
        """
        ret = self._get_attr("PAEEnabled")
        return ret

    @property
    def virtual_time_rate(self):
        """Get or set int value for 'virtualTimeRate'
        The rate at which the virtual time runs expressed as a percentage.
        The accepted range is 2% to 20000%.
        """
        ret = self._get_attr("virtualTimeRate")
        return ret

    @virtual_time_rate.setter
    def virtual_time_rate(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("virtualTimeRate", value)

    @property
    def vm(self):
        """Get int value for 'VM'
        Gets the user-mode VM handle, with a reference. Must be passed to
        VMR3ReleaseUVM when done. This is only for internal use while we carve
        the details of this interface.
        """
        ret = self._get_attr("VM")
        return ret


class IUSBController(Interface):
    """
    Flag whether the USB controller is present in the
        guest system. If disabled, the virtual guest hardware will
        not contain any USB controller. Can only be changed when
        the VM is powered off.
    """
    __uuid__ = '01e6f13a-0580-452f-a40f-74e32a5e4921'
    __wsmap__ = 'managed'
    
    @property
    def enabled(self):
        """Get or set bool value for 'enabled'
        Flag whether the USB controller is present in the
        guest system. If disabled, the virtual guest hardware will
        not contain any USB controller. Can only be changed when
        the VM is powered off.
        """
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def enabled_ehci(self):
        """Get or set bool value for 'enabledEHCI'
        Flag whether the USB EHCI controller is present in the
        guest system. If disabled, the virtual guest hardware will
        not contain a USB EHCI controller. Can only be changed when
        the VM is powered off.
        """
        ret = self._get_attr("enabledEHCI")
        return ret

    @enabled_ehci.setter
    def enabled_ehci(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabledEHCI", value)

    @property
    def proxy_available(self):
        """Get bool value for 'proxyAvailable'
        Flag whether there is an USB proxy available.
        """
        ret = self._get_attr("proxyAvailable")
        return ret

    @property
    def usb_standard(self):
        """Get int value for 'USBStandard'
        USB standard version which the controller implements.
        This is a BCD which means that the major version is in the
        high byte and minor version is in the low byte.
        """
        ret = self._get_attr("USBStandard")
        return ret

    @property
    def device_filters(self):
        """Get IUSBDeviceFilter value for 'deviceFilters'
        List of USB device filters associated with the machine.

        If the machine is currently running, these filters are activated
        every time a new (supported) USB device is attached to the host
        computer that was not ignored by global filters
        (<link to="IHost::USBDeviceFilters"/>).

        These filters are also activated when the machine is powered up.
        They are run against a list of all currently available USB
        devices (in states
        <link to="USBDeviceState_Available"/>,
        <link to="USBDeviceState_Busy"/>,
        <link to="USBDeviceState_Held"/>) that were not previously
        ignored by global filters.

        If at least one filter matches the USB device in question, this
        device is automatically captured (attached to) the virtual USB
        controller of this machine.

        <link to="IUSBDeviceFilter"/>, <link to="IUSBController"/>
        """
        ret = self._get_attr("deviceFilters")
        return [IUSBDeviceFilter(a) for a in ret]

    def create_device_filter(self, name):
        """Creates a new USB device filter. All attributes except
        the filter name are set to empty (any match),
        active is @c false (the filter is not active).

        The created filter can then be added to the list of filters using
        <link to="#insertDeviceFilter"/>.

        

        <link to="#deviceFilters"/>

        in name of type str
            Filter name. See <link to="IUSBDeviceFilter::name"/>
          for more info.

        return filter_p of type IUSBDeviceFilter
            Created filter object.

        raises VBOX_E_INVALID_VM_STATE
            The virtual machine is not mutable.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        filter_p = self._call("createDeviceFilter",
                     in_p=[name])
        filter_p = IUSBDeviceFilter(filter_p)
        return filter_p

    def insert_device_filter(self, position, filter_p):
        """Inserts the given USB device to the specified position
        in the list of filters.

        Positions are numbered starting from 0. If the specified
        position is equal to or greater than the number of elements in
        the list, the filter is added to the end of the collection.

        
          Duplicates are not allowed, so an attempt to insert a
          filter that is already in the collection, will return an
          error.
        

        

        <link to="#deviceFilters"/>

        in position of type int
            Position to insert the filter to.

        in filter_p of type IUSBDeviceFilter
            USB device filter to insert.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is not mutable.
        
        raises E_INVALIDARG
            USB device filter not created within this VirtualBox instance.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            USB device filter already in list.
        
        """
        if not isinstance(position, int):
            raise TypeError("position can only be an instance of type int")
        if not isinstance(filter_p, IUSBDeviceFilter):
            raise TypeError("filter_p can only be an instance of type IUSBDeviceFilter")
        self._call("insertDeviceFilter",
                     in_p=[position, filter_p])

    def remove_device_filter(self, position):
        """Removes a USB device filter from the specified position in the
        list of filters.

        Positions are numbered starting from 0. Specifying a
        position equal to or greater than the number of elements in
        the list will produce an error.

        <link to="#deviceFilters"/>

        in position of type int
            Position to remove the filter from.

        return filter_p of type IUSBDeviceFilter
            Removed USB device filter.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine is not mutable.
        
        raises E_INVALIDARG
            USB device filter list empty or invalid @a position.
        
        """
        if not isinstance(position, int):
            raise TypeError("position can only be an instance of type int")
        filter_p = self._call("removeDeviceFilter",
                     in_p=[position])
        filter_p = IUSBDeviceFilter(filter_p)
        return filter_p


class IUSBDevice(Interface):
    """
    The IUSBDevice interface represents a virtual USB device attached to the
      virtual machine.

      A collection of objects implementing this interface is stored in the
      <link to="IConsole::USBDevices"/> attribute which lists all USB devices
      attached to a running virtual machine's USB controller.
    """
    __uuid__ = 'f8967b0b-4483-400f-92b5-8b675d98a85b'
    __wsmap__ = 'managed'
    
    @property
    def id_p(self):
        """Get str value for 'id'
        Unique USB device ID. This ID is built from #vendorId,
        #productId, #revision and #serialNumber.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def vendor_id(self):
        """Get int value for 'vendorId'
        Vendor ID.
        """
        ret = self._get_attr("vendorId")
        return ret

    @property
    def product_id(self):
        """Get int value for 'productId'
        Product ID.
        """
        ret = self._get_attr("productId")
        return ret

    @property
    def revision(self):
        """Get int value for 'revision'
        Product revision number. This is a packed BCD represented as
        unsigned short. The high byte is the integer part and the low
        byte is the decimal.
        """
        ret = self._get_attr("revision")
        return ret

    @property
    def manufacturer(self):
        """Get str value for 'manufacturer'
        Manufacturer string.
        """
        ret = self._get_attr("manufacturer")
        return ret

    @property
    def product(self):
        """Get str value for 'product'
        Product string.
        """
        ret = self._get_attr("product")
        return ret

    @property
    def serial_number(self):
        """Get str value for 'serialNumber'
        Serial number string.
        """
        ret = self._get_attr("serialNumber")
        return ret

    @property
    def address(self):
        """Get str value for 'address'
        Host specific address of the device.
        """
        ret = self._get_attr("address")
        return ret

    @property
    def port(self):
        """Get int value for 'port'
        Host USB port number the device is physically
        connected to.
        """
        ret = self._get_attr("port")
        return ret

    @property
    def version(self):
        """Get int value for 'version'
        The major USB version of the device - 1 or 2.
        """
        ret = self._get_attr("version")
        return ret

    @property
    def port_version(self):
        """Get int value for 'portVersion'
        The major USB version of the host USB port the device is
        physically connected to - 1 or 2. For devices not connected to
        anything this will have the same value as the version attribute.
        """
        ret = self._get_attr("portVersion")
        return ret

    @property
    def remote(self):
        """Get bool value for 'remote'
        Whether the device is physically connected to a remote VRDE
        client or to a local host machine.
        """
        ret = self._get_attr("remote")
        return ret


class IUSBDeviceFilter(Interface):
    """
    The IUSBDeviceFilter interface represents an USB device filter used
      to perform actions on a group of USB devices.

      This type of filters is used by running virtual machines to
      automatically capture selected USB devices once they are physically
      attached to the host computer.

      A USB device is matched to the given device filter if and only if all
      attributes of the device match the corresponding attributes of the
      filter (that is, attributes are joined together using the logical AND
      operation). On the other hand, all together, filters in the list of
      filters carry the semantics of the logical OR operation. So if it is
      desirable to create a match like "this vendor id OR this product id",
      one needs to create two filters and specify "any match" (see below)
      for unused attributes.

      All filter attributes used for matching are strings. Each string
      is an expression representing a set of values of the corresponding
      device attribute, that will match the given filter. Currently, the
      following filtering expressions are supported:

      
        Interval filters. Used to specify valid intervals for
          integer device attributes (Vendor ID, Product ID and Revision).
          The format of the string is:

          int:((m)|([m]-[n]))(,(m)|([m]-[n]))*

          where m and n are integer numbers, either in octal
          (starting from 0), hexadecimal (starting from 0x)
          or decimal (otherwise) form, so that m < n. If m
          is omitted before a dash (-), the minimum possible integer
          is assumed; if n is omitted after a dash, the maximum
          possible integer is assumed.
        
        Boolean filters. Used to specify acceptable values for
          boolean device attributes. The format of the string is:

          true|false|yes|no|0|1

        
        Exact match. Used to specify a single value for the given
          device attribute. Any string that doesn't start with int:
          represents the exact match. String device attributes are compared to
          this string including case of symbols. Integer attributes are first
          converted to a string (see individual filter attributes) and then
          compared ignoring case.

        
        Any match. Any value of the corresponding device attribute
          will match the given filter. An empty or @c null string is
          used to construct this type of filtering expressions.

        
      

      
        On the Windows host platform, interval filters are not currently
        available. Also all string filter attributes
        (<link to="#manufacturer"/>, <link to="#product"/>,
        <link to="#serialNumber"/>) are ignored, so they behave as
        any match no matter what string expression is specified.
      

      <link to="IUSBController::deviceFilters"/>,
        <link to="IHostUSBDeviceFilter"/>
    """
    __uuid__ = 'd6831fb4-1a94-4c2c-96ef-8d0d6192066d'
    __wsmap__ = 'managed'
    
    @property
    def name(self):
        """Get or set str value for 'name'
        Visible name for this filter.
        This name is used to visually distinguish one filter from another,
        so it can neither be @c null nor an empty string.
        """
        ret = self._get_attr("name")
        return ret

    @name.setter
    def name(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("name", value)

    @property
    def active(self):
        """Get or set bool value for 'active'
        Whether this filter active or has been temporarily disabled.
        """
        ret = self._get_attr("active")
        return ret

    @active.setter
    def active(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("active", value)

    @property
    def vendor_id(self):
        """Get or set str value for 'vendorId'
        <link to="IUSBDevice::vendorId">Vendor ID</link> filter.
        The string representation for the exact matching
        has the form XXXX, where X is the hex digit
        (including leading zeroes).
        """
        ret = self._get_attr("vendorId")
        return ret

    @vendor_id.setter
    def vendor_id(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("vendorId", value)

    @property
    def product_id(self):
        """Get or set str value for 'productId'
        <link to="IUSBDevice::productId">Product ID</link> filter.
        The string representation for the exact matching
        has the form XXXX, where X is the hex digit
        (including leading zeroes).
        """
        ret = self._get_attr("productId")
        return ret

    @product_id.setter
    def product_id(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("productId", value)

    @property
    def revision(self):
        """Get or set str value for 'revision'
        <link to="IUSBDevice::productId">Product revision number</link>
        filter. The string representation for the exact matching
        has the form IIFF, where I is the decimal digit
        of the integer part of the revision, and F is the
        decimal digit of its fractional part (including leading and
        trailing zeros).
        Note that for interval filters, it's best to use the hexadecimal
        form, because the revision is stored as a 16 bit packed BCD value;
        so the expression int:0x0100-0x0199 will match any
        revision from 1.0 to 1.99.
        """
        ret = self._get_attr("revision")
        return ret

    @revision.setter
    def revision(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("revision", value)

    @property
    def manufacturer(self):
        """Get or set str value for 'manufacturer'
        <link to="IUSBDevice::manufacturer">Manufacturer</link> filter.
        """
        ret = self._get_attr("manufacturer")
        return ret

    @manufacturer.setter
    def manufacturer(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("manufacturer", value)

    @property
    def product(self):
        """Get or set str value for 'product'
        <link to="IUSBDevice::product">Product</link> filter.
        """
        ret = self._get_attr("product")
        return ret

    @product.setter
    def product(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("product", value)

    @property
    def serial_number(self):
        """Get or set str value for 'serialNumber'
        <link to="IUSBDevice::serialNumber">Serial number</link> filter.
        """
        ret = self._get_attr("serialNumber")
        return ret

    @serial_number.setter
    def serial_number(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("serialNumber", value)

    @property
    def port(self):
        """Get or set str value for 'port'
        <link to="IUSBDevice::port">Host USB port</link> filter.
        """
        ret = self._get_attr("port")
        return ret

    @port.setter
    def port(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("port", value)

    @property
    def remote(self):
        """Get or set str value for 'remote'
        <link to="IUSBDevice::remote">Remote state</link> filter.
        
          This filter makes sense only for machine USB filters,
          i.e. it is ignored by IHostUSBDeviceFilter objects.
        """
        ret = self._get_attr("remote")
        return ret

    @remote.setter
    def remote(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("remote", value)

    @property
    def masked_interfaces(self):
        """Get or set int value for 'maskedInterfaces'
        This is an advanced option for hiding one or more USB interfaces
        from the guest. The value is a bit mask where the bits that are set
        means the corresponding USB interface should be hidden, masked off
        if you like.
        This feature only works on Linux hosts.
        """
        ret = self._get_attr("maskedInterfaces")
        return ret

    @masked_interfaces.setter
    def masked_interfaces(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("maskedInterfaces", value)


class IHostUSBDevice(IUSBDevice):
    """
    The IHostUSBDevice interface represents a physical USB device attached
      to the host computer.

      Besides properties inherited from IUSBDevice, this interface adds the
      <link to="#state"/> property that holds the current state of the USB
      device.

      <link to="IHost::USBDevices"/>,
        <link to="IHost::USBDeviceFilters"/>
    """
    __uuid__ = '173b4b44-d268-4334-a00d-b6521c9a740a'
    __wsmap__ = 'managed'
    
    @property
    def state(self):
        """Get USBDeviceState value for 'state'
        Current state of the device.
        """
        ret = self._get_attr("state")
        return USBDeviceState(ret)


class IHostUSBDeviceFilter(IUSBDeviceFilter):
    """
    The IHostUSBDeviceFilter interface represents a global filter for a
      physical USB device used by the host computer. Used indirectly in
      <link to="IHost::USBDeviceFilters"/>.

      Using filters of this type, the host computer determines the initial
      state of the USB device after it is physically attached to the
      host's USB controller.

      
        The <link to="IUSBDeviceFilter::remote"/> attribute is ignored by this type of
        filters, because it makes sense only for
        <link to="IUSBController::deviceFilters">machine USB filters</link>.
      

      <link to="IHost::USBDeviceFilters"/>
    """
    __uuid__ = '4cc70246-d74a-400f-8222-3900489c0374'
    __wsmap__ = 'managed'
    
    @property
    def action(self):
        """Get or set USBDeviceFilterAction value for 'action'
        Action performed by the host when an attached USB device
        matches this filter.
        """
        ret = self._get_attr("action")
        return USBDeviceFilterAction(ret)

    @action.setter
    def action(self, value):
        if not isinstance(value, USBDeviceFilterAction):
            raise TypeError("value is not an instance of USBDeviceFilterAction")
        return self._set_attr("action", value)


class IAudioAdapter(Interface):
    """
    The IAudioAdapter interface represents the virtual audio adapter of
        the virtual machine. Used in <link to="IMachine::audioAdapter"/>.
    """
    __uuid__ = '921873db-5f3f-4b69-91f9-7be9e535a2cb'
    __wsmap__ = 'managed'
    
    @property
    def enabled(self):
        """Get or set bool value for 'enabled'
        Flag whether the audio adapter is present in the
        guest system. If disabled, the virtual guest hardware will
        not contain any audio adapter. Can only be changed when
        the VM is not running.
        """
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def audio_controller(self):
        """Get or set AudioControllerType value for 'audioController'
        The audio hardware we emulate.
        """
        ret = self._get_attr("audioController")
        return AudioControllerType(ret)

    @audio_controller.setter
    def audio_controller(self, value):
        if not isinstance(value, AudioControllerType):
            raise TypeError("value is not an instance of AudioControllerType")
        return self._set_attr("audioController", value)

    @property
    def audio_driver(self):
        """Get or set AudioDriverType value for 'audioDriver'
        Audio driver the adapter is connected to. This setting
        can only be changed when the VM is not running.
        """
        ret = self._get_attr("audioDriver")
        return AudioDriverType(ret)

    @audio_driver.setter
    def audio_driver(self, value):
        if not isinstance(value, AudioDriverType):
            raise TypeError("value is not an instance of AudioDriverType")
        return self._set_attr("audioDriver", value)


class IVRDEServer(Interface):
    """
    Flag if VRDE server is enabled.
    """
    __uuid__ = 'd38de40a-c2c1-4e95-b5a4-167b05f5694c'
    __wsmap__ = 'managed'
    
    @property
    def enabled(self):
        """Get or set bool value for 'enabled'
        Flag if VRDE server is enabled.
        """
        ret = self._get_attr("enabled")
        return ret

    @enabled.setter
    def enabled(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("enabled", value)

    @property
    def auth_type(self):
        """Get or set AuthType value for 'authType'
        VRDE authentication method.
        """
        ret = self._get_attr("authType")
        return AuthType(ret)

    @auth_type.setter
    def auth_type(self, value):
        if not isinstance(value, AuthType):
            raise TypeError("value is not an instance of AuthType")
        return self._set_attr("authType", value)

    @property
    def auth_timeout(self):
        """Get or set int value for 'authTimeout'
        Timeout for guest authentication. Milliseconds.
        """
        ret = self._get_attr("authTimeout")
        return ret

    @auth_timeout.setter
    def auth_timeout(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("authTimeout", value)

    @property
    def allow_multi_connection(self):
        """Get or set bool value for 'allowMultiConnection'
        Flag whether multiple simultaneous connections to the VM are permitted.
        Note that this will be replaced by a more powerful mechanism in the future.
        """
        ret = self._get_attr("allowMultiConnection")
        return ret

    @allow_multi_connection.setter
    def allow_multi_connection(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("allowMultiConnection", value)

    @property
    def reuse_single_connection(self):
        """Get or set bool value for 'reuseSingleConnection'
        Flag whether the existing connection must be dropped and a new connection
        must be established by the VRDE server, when a new client connects in single
        connection mode.
        """
        ret = self._get_attr("reuseSingleConnection")
        return ret

    @reuse_single_connection.setter
    def reuse_single_connection(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("reuseSingleConnection", value)

    @property
    def vrde_ext_pack(self):
        """Get or set str value for 'VRDEExtPack'
        The name of Extension Pack providing VRDE for this VM. Overrides
        <link to="ISystemProperties::defaultVRDEExtPack"/>.
        """
        ret = self._get_attr("VRDEExtPack")
        return ret

    @vrde_ext_pack.setter
    def vrde_ext_pack(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("VRDEExtPack", value)

    @property
    def auth_library(self):
        """Get or set str value for 'authLibrary'
        Library used for authentication of RDP clients by this VM. Overrides
        <link to="ISystemProperties::VRDEAuthLibrary"/>.
        """
        ret = self._get_attr("authLibrary")
        return ret

    @auth_library.setter
    def auth_library(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("authLibrary", value)

    @property
    def vrde_properties(self):
        """Get str value for 'VRDEProperties'
        Array of names of properties, which are supported by this VRDE server.
        """
        ret = self._get_attr("VRDEProperties")
        return ret

    def set_vrde_property(self, key, value):
        """Sets a VRDE specific property string.

        If you pass @c null or empty string as a key @a value, the given @a key
        will be deleted.

        in key of type str
            Name of the key to set.

        in value of type str
            Value to assign to the key.

        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("setVRDEProperty",
                     in_p=[key, value])

    def get_vrde_property(self, key):
        """Returns a VRDE specific property string.

        If the requested data @a key does not exist, this function will
        succeed and return an empty string in the @a value argument.

        in key of type str
            Name of the key to get.

        return value of type str
            Value of the requested key.

        """
        if type(key) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        value = self._call("getVRDEProperty",
                     in_p=[key])
        return value


class ISharedFolder(Interface):
    """
    The ISharedFolder interface represents a folder in the host computer's
      file system accessible from the guest OS running inside a virtual
      machine using an associated logical name.

      There are three types of shared folders:
      
        Global (<link to="IVirtualBox::sharedFolders"/>), shared
        folders available to all virtual machines.
        Permanent (<link to="IMachine::sharedFolders"/>),
        VM-specific shared folders available to the given virtual machine at
        startup.
        Transient (<link to="IConsole::sharedFolders"/>),
        VM-specific shared folders created in the session context (for
        example, when the virtual machine is running) and automatically
        discarded when the session is closed (the VM is powered off).
      

      Logical names of shared folders must be unique within the given scope
      (global, permanent or transient). However, they do not need to be unique
      across scopes. In this case, the definition of the shared folder in a
      more specific scope takes precedence over definitions in all other
      scopes. The order of precedence is (more specific to more general):
      
        Transient definitions
        Permanent definitions
        Global definitions
      

      For example, if MyMachine has a shared folder named
      C_DRIVE (that points to C:\\), then creating a
      transient shared folder named C_DRIVE (that points
      to C:\\\\WINDOWS) will change the definition
      of C_DRIVE in the guest OS so
      that \\\\VBOXSVR\\C_DRIVE will give access
      to C:\\WINDOWS instead of C:\\ on the host
      PC. Removing the transient shared folder C_DRIVE will restore
      the previous (permanent) definition of C_DRIVE that points
      to C:\\ if it still exists.

      Note that permanent and transient shared folders of different machines
      are in different name spaces, so they don't overlap and don't need to
      have unique logical names.

      
        Global shared folders are not implemented in the current version of the
        product.
    """
    __uuid__ = '8388da11-b559-4574-a5b7-2bd7acd5cef8'
    __wsmap__ = 'struct'
    
    @property
    def name(self):
        """Get str value for 'name'
        Logical name of the shared folder.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def host_path(self):
        """Get str value for 'hostPath'
        Full path to the shared folder in the host file system.
        """
        ret = self._get_attr("hostPath")
        return ret

    @property
    def accessible(self):
        """Get bool value for 'accessible'
        Whether the folder defined by the host path is currently
        accessible or not.
        For example, the folder can be inaccessible if it is placed
        on the network share that is not available by the time
        this property is read.
        """
        ret = self._get_attr("accessible")
        return ret

    @property
    def writable(self):
        """Get bool value for 'writable'
        Whether the folder defined by the host path is writable or
        not.
        """
        ret = self._get_attr("writable")
        return ret

    @property
    def auto_mount(self):
        """Get bool value for 'autoMount'
        Whether the folder gets automatically mounted by the guest or not.
        """
        ret = self._get_attr("autoMount")
        return ret

    @property
    def last_access_error(self):
        """Get str value for 'lastAccessError'
        Text message that represents the result of the last accessibility
        check.

        Accessibility checks are performed each time the <link to="#accessible"/>
        attribute is read. An empty string is returned if the last
        accessibility check was successful. A non-empty string indicates a
        failure and should normally describe a reason of the failure (for
        example, a file read error).
        """
        ret = self._get_attr("lastAccessError")
        return ret


class IInternalSessionControl(Interface):
    """
    PID of the process that has created this Session object.
    """
    __uuid__ = 'cddf451c-a006-4c33-8245-63b3c9ae6586'
    __wsmap__ = 'suppress'
    
    def get_pid(self):
        """PID of the process that has created this Session object.

        return pid of type int

        """
        pid = self._call("getPID")
        return pid

    def get_remote_console(self):
        """Returns the console object suitable for remote control.

        return console of type IConsole

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        console = self._call("getRemoteConsole")
        console = IConsole(console)
        return console

    def assign_machine(self, machine, lock_type):
        """Assigns the machine object associated with this direct-type
        session or informs the session that it will be a remote one
        (if @a machine == @c null).

        in machine of type IMachine

        in lock_type of type LockType

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(machine, IMachine):
            raise TypeError("machine can only be an instance of type IMachine")
        if not isinstance(lock_type, LockType):
            raise TypeError("lock_type can only be an instance of type LockType")
        self._call("assignMachine",
                     in_p=[machine, lock_type])

    def assign_remote_machine(self, machine, console):
        """Assigns the machine and the (remote) console object associated with
        this remote-type session.

        in machine of type IMachine

        in console of type IConsole

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        """
        if not isinstance(machine, IMachine):
            raise TypeError("machine can only be an instance of type IMachine")
        if not isinstance(console, IConsole):
            raise TypeError("console can only be an instance of type IConsole")
        self._call("assignRemoteMachine",
                     in_p=[machine, console])

    def update_machine_state(self, machine_state):
        """Updates the machine state in the VM process.
        Must be called only in certain cases
        (see the method implementation).

        in machine_state of type MachineState

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(machine_state, MachineState):
            raise TypeError("machine_state can only be an instance of type MachineState")
        self._call("updateMachineState",
                     in_p=[machine_state])

    def uninitialize(self):
        """Uninitializes (closes) this session. Used by VirtualBox to close
        the corresponding remote session when the direct session dies
        or gets closed.

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        """
        self._call("uninitialize")

    def on_network_adapter_change(self, network_adapter, change_adapter):
        """Triggered when settings of a network adapter of the
        associated virtual machine have changed.

        in network_adapter of type INetworkAdapter

        in change_adapter of type bool

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(network_adapter, INetworkAdapter):
            raise TypeError("network_adapter can only be an instance of type INetworkAdapter")
        if not isinstance(change_adapter, bool):
            raise TypeError("change_adapter can only be an instance of type bool")
        self._call("onNetworkAdapterChange",
                     in_p=[network_adapter, change_adapter])

    def on_serial_port_change(self, serial_port):
        """Triggered when settings of a serial port of the
        associated virtual machine have changed.

        in serial_port of type ISerialPort

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(serial_port, ISerialPort):
            raise TypeError("serial_port can only be an instance of type ISerialPort")
        self._call("onSerialPortChange",
                     in_p=[serial_port])

    def on_parallel_port_change(self, parallel_port):
        """Triggered when settings of a parallel port of the
        associated virtual machine have changed.

        in parallel_port of type IParallelPort

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(parallel_port, IParallelPort):
            raise TypeError("parallel_port can only be an instance of type IParallelPort")
        self._call("onParallelPortChange",
                     in_p=[parallel_port])

    def on_storage_controller_change(self):
        """Triggered when settings of a storage controller of the
        associated virtual machine have changed.

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        self._call("onStorageControllerChange")

    def on_medium_change(self, medium_attachment, force):
        """Triggered when attached media of the
        associated virtual machine have changed.

        in medium_attachment of type IMediumAttachment
            The medium attachment which changed.

        in force of type bool
            If the medium change was forced.

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(medium_attachment, IMediumAttachment):
            raise TypeError("medium_attachment can only be an instance of type IMediumAttachment")
        if not isinstance(force, bool):
            raise TypeError("force can only be an instance of type bool")
        self._call("onMediumChange",
                     in_p=[medium_attachment, force])

    def on_storage_device_change(self, medium_attachment, remove, silent):
        """Triggered when attached storage devices of the
        associated virtual machine have changed.

        in medium_attachment of type IMediumAttachment
            The medium attachment which changed.

        in remove of type bool
            TRUE if the device is removed, FALSE if it was added.

        in silent of type bool
            TRUE if the device is is silently reconfigured without
          notifying the guest about it.

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(medium_attachment, IMediumAttachment):
            raise TypeError("medium_attachment can only be an instance of type IMediumAttachment")
        if not isinstance(remove, bool):
            raise TypeError("remove can only be an instance of type bool")
        if not isinstance(silent, bool):
            raise TypeError("silent can only be an instance of type bool")
        self._call("onStorageDeviceChange",
                     in_p=[medium_attachment, remove, silent])

    def on_clipboard_mode_change(self, clipboard_mode):
        """Notification when the shared clipboard mode changes.

        in clipboard_mode of type ClipboardMode
            The new shared clipboard mode.

        """
        if not isinstance(clipboard_mode, ClipboardMode):
            raise TypeError("clipboard_mode can only be an instance of type ClipboardMode")
        self._call("onClipboardModeChange",
                     in_p=[clipboard_mode])

    def on_drag_and_drop_mode_change(self, drag_and_drop_mode):
        """Notification when the drag'n'drop mode changes.

        in drag_and_drop_mode of type DragAndDropMode
            The new mode for drag'n'drop.

        """
        if not isinstance(drag_and_drop_mode, DragAndDropMode):
            raise TypeError("drag_and_drop_mode can only be an instance of type DragAndDropMode")
        self._call("onDragAndDropModeChange",
                     in_p=[drag_and_drop_mode])

    def on_cpu_change(self, cpu, add):
        """Notification when a CPU changes.

        in cpu of type int
            The CPU which changed

        in add of type bool
            Flag whether the CPU was added or removed

        """
        if not isinstance(cpu, int):
            raise TypeError("cpu can only be an instance of type int")
        if not isinstance(add, bool):
            raise TypeError("add can only be an instance of type bool")
        self._call("onCPUChange",
                     in_p=[cpu, add])

    def on_cpu_execution_cap_change(self, execution_cap):
        """Notification when the CPU execution cap changes.

        in execution_cap of type int
            The new CPU execution cap value. (1-100)

        """
        if not isinstance(execution_cap, int):
            raise TypeError("execution_cap can only be an instance of type int")
        self._call("onCPUExecutionCapChange",
                     in_p=[execution_cap])

    def on_vrde_server_change(self, restart):
        """Triggered when settings of the VRDE server object of the
        associated virtual machine have changed.

        in restart of type bool
            Flag whether the server must be restarted

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(restart, bool):
            raise TypeError("restart can only be an instance of type bool")
        self._call("onVRDEServerChange",
                     in_p=[restart])

    def on_video_capture_change(self):
        """Triggered when video capture settings have changed.

        """
        self._call("onVideoCaptureChange")

    def on_usb_controller_change(self):
        """Triggered when settings of the USB controller object of the
        associated virtual machine have changed.

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        self._call("onUSBControllerChange")

    def on_shared_folder_change(self, global_p):
        """Triggered when a permanent (global or machine) shared folder has been
        created or removed.
        
          We don't pass shared folder parameters in this notification because
          the order in which parallel notifications are delivered is not defined,
          therefore it could happen that these parameters were outdated by the
          time of processing this notification.

        in global_p of type bool

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(global_p, bool):
            raise TypeError("global_p can only be an instance of type bool")
        self._call("onSharedFolderChange",
                     in_p=[global_p])

    def on_usb_device_attach(self, device, error, masked_interfaces):
        """Triggered when a request to capture a USB device (as a result
        of matched USB filters or direct call to
        <link to="IConsole::attachUSBDevice"/>) has completed.
        A @c null @a error object means success, otherwise it
        describes a failure.

        in device of type IUSBDevice

        in error of type IVirtualBoxErrorInfo

        in masked_interfaces of type int

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(device, IUSBDevice):
            raise TypeError("device can only be an instance of type IUSBDevice")
        if not isinstance(error, IVirtualBoxErrorInfo):
            raise TypeError("error can only be an instance of type IVirtualBoxErrorInfo")
        if not isinstance(masked_interfaces, int):
            raise TypeError("masked_interfaces can only be an instance of type int")
        self._call("onUSBDeviceAttach",
                     in_p=[device, error, masked_interfaces])

    def on_usb_device_detach(self, id_p, error):
        """Triggered when a request to release the USB device (as a result
        of machine termination or direct call to
        <link to="IConsole::detachUSBDevice"/>) has completed.
        A @c null @a error object means success, otherwise it
        describes a failure.

        in id_p of type str

        in error of type IVirtualBoxErrorInfo

        raises VBOX_E_INVALID_VM_STATE
            Session state prevents operation.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if type(id_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(error, IVirtualBoxErrorInfo):
            raise TypeError("error can only be an instance of type IVirtualBoxErrorInfo")
        self._call("onUSBDeviceDetach",
                     in_p=[id_p, error])

    def on_show_window(self, check):
        """Called by <link to="IMachine::canShowConsoleWindow"/> and by
        <link to="IMachine::showConsoleWindow"/> in order to notify
        console listeners
        <link to="ICanShowWindowEvent"/>
        and <link to="IShowWindowEvent"/>.

        in check of type bool

        out can_show of type bool

        out win_id of type int

        raises VBOX_E_INVALID_OBJECT_STATE
            Session type prevents operation.
        
        """
        if not isinstance(check, bool):
            raise TypeError("check can only be an instance of type bool")
        (can_show, win_id) = self._call("onShowWindow",
                     in_p=[check])
        return (can_show, win_id)

    def on_bandwidth_group_change(self, bandwidth_group):
        """Notification when one of the bandwidth groups change.

        in bandwidth_group of type IBandwidthGroup
            The bandwidth group which changed.

        """
        if not isinstance(bandwidth_group, IBandwidthGroup):
            raise TypeError("bandwidth_group can only be an instance of type IBandwidthGroup")
        self._call("onBandwidthGroupChange",
                     in_p=[bandwidth_group])

    def access_guest_property(self, name, value, flags, is_setter):
        """Called by <link to="IMachine::getGuestProperty"/> and by
        <link to="IMachine::setGuestProperty"/> in order to read and
        modify guest properties.

        in name of type str

        in value of type str

        in flags of type str

        in is_setter of type bool

        out ret_value of type str

        out ret_timestamp of type int

        out ret_flags of type str

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type is not direct.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(flags) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(is_setter, bool):
            raise TypeError("is_setter can only be an instance of type bool")
        (ret_value, ret_timestamp, ret_flags) = self._call("accessGuestProperty",
                     in_p=[name, value, flags, is_setter])
        return (ret_value, ret_timestamp, ret_flags)

    def enumerate_guest_properties(self, patterns):
        """Return a list of the guest properties matching a set of patterns along
        with their values, time stamps and flags.

        in patterns of type str
            The patterns to match the properties against as a comma-separated
          string. If this is empty, all properties currently set will be
          returned.

        out keys of type str
            The key names of the properties returned.

        out values of type str
            The values of the properties returned. The array entries match the
          corresponding entries in the @a key array.

        out timestamps of type int
            The time stamps of the properties returned. The array entries match
          the corresponding entries in the @a key array.

        out flags of type str
            The flags of the properties returned. The array entries match the
          corresponding entries in the @a key array.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type is not direct.
        
        """
        if type(patterns) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        (keys, values, timestamps, flags) = self._call("enumerateGuestProperties",
                     in_p=[patterns])
        return (keys, values, timestamps, flags)

    def online_merge_medium(self, medium_attachment, source_idx, target_idx, source, target, merge_forward, parent_for_target, children_to_reparent, progress):
        """Triggers online merging of a hard disk. Used internally when deleting
        a snapshot while a VM referring to the same hard disk chain is running.

        in medium_attachment of type IMediumAttachment
            The medium attachment to identify the medium chain.

        in source_idx of type int
            The index of the source image in the chain.
        Redundant, but drastically reduces IPC.

        in target_idx of type int
            The index of the target image in the chain.
        Redundant, but drastically reduces IPC.

        in source of type IMedium
            Merge source medium.

        in target of type IMedium
            Merge target medium.

        in merge_forward of type bool
            Merge direction.

        in parent_for_target of type IMedium
            For forward merges: new parent for target medium.

        in children_to_reparent of type IMedium
            For backward merges: list of media which need their parent UUID
        updated.

        in progress of type IProgress
            Progress object for this operation.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type is not direct.
        
        """
        if not isinstance(medium_attachment, IMediumAttachment):
            raise TypeError("medium_attachment can only be an instance of type IMediumAttachment")
        if not isinstance(source_idx, int):
            raise TypeError("source_idx can only be an instance of type int")
        if not isinstance(target_idx, int):
            raise TypeError("target_idx can only be an instance of type int")
        if not isinstance(source, IMedium):
            raise TypeError("source can only be an instance of type IMedium")
        if not isinstance(target, IMedium):
            raise TypeError("target can only be an instance of type IMedium")
        if not isinstance(merge_forward, bool):
            raise TypeError("merge_forward can only be an instance of type bool")
        if not isinstance(parent_for_target, IMedium):
            raise TypeError("parent_for_target can only be an instance of type IMedium")
        if not isinstance(children_to_reparent, list):
            raise TypeError("children_to_reparent can only be an instance of type list")
        for a in children_to_reparent[:10]:
            if not isinstance(a, IMedium):
                raise TypeError(\
                        "array can only contain objects of type IMedium")
        if not isinstance(progress, IProgress):
            raise TypeError("progress can only be an instance of type IProgress")
        self._call("onlineMergeMedium",
                     in_p=[medium_attachment, source_idx, target_idx, source, target, merge_forward, parent_for_target, children_to_reparent, progress])

    def enable_vmm_statistics(self, enable):
        """Enables or disables collection of VMM RAM statistics.

        in enable of type bool
            True enables statistics collection.

        raises VBOX_E_INVALID_VM_STATE
            Machine session is not open.
        
        raises VBOX_E_INVALID_OBJECT_STATE
            Session type is not direct.
        
        """
        if not isinstance(enable, bool):
            raise TypeError("enable can only be an instance of type bool")
        self._call("enableVMMStatistics",
                     in_p=[enable])

    def pause_with_reason(self, reason):
        """Internal method for triggering a VM pause with a specified reason code.
        The reason code can be interpreted by device/drivers and thus it might
        behave slightly differently than a normal VM pause.

        
        <link to="IConsole::pause"/>

        in reason of type Reason
            Specify the best matching reason code please.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Running state.
        
        raises VBOX_E_VM_ERROR
            Virtual machine error in suspend operation.
        
        """
        if not isinstance(reason, Reason):
            raise TypeError("reason can only be an instance of type Reason")
        self._call("pauseWithReason",
                     in_p=[reason])

    def resume_with_reason(self, reason):
        """Internal method for triggering a VM resume with a specified reason code.
        The reason code can be interpreted by device/drivers and thus it might
        behave slightly differently than a normal VM resume.

        
        <link to="IConsole::resume"/>

        in reason of type Reason
            Specify the best matching reason code please.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine not in Paused state.
        
        raises VBOX_E_VM_ERROR
            Virtual machine error in resume operation.
        
        """
        if not isinstance(reason, Reason):
            raise TypeError("reason can only be an instance of type Reason")
        self._call("resumeWithReason",
                     in_p=[reason])

    def save_state_with_reason(self, reason):
        """Internal method for triggering a VM save state with a specified reason
        code. The reason code can be interpreted by device/drivers and thus it
        might behave slightly differently than a normal VM save state.

        
        <link to="IConsole::saveState"/>

        in reason of type Reason
            Specify the best matching reason code please.

        return progress of type IProgress
            Progress object to track the operation completion.

        raises VBOX_E_INVALID_VM_STATE
            Virtual machine state neither Running nor Paused.
        
        raises VBOX_E_FILE_ERROR
            Failed to create directory for saved state file.
        
        """
        if not isinstance(reason, Reason):
            raise TypeError("reason can only be an instance of type Reason")
        progress = self._call("saveStateWithReason",
                     in_p=[reason])
        progress = IProgress(progress)
        return progress


class ISession(Interface):
    """
    The ISession interface represents a client process and allows for locking
      virtual machines (represented by IMachine objects) to prevent conflicting
      changes to the machine.

      Any caller wishing to manipulate a virtual machine needs to create a session
      object first, which lives in its own process space. Such session objects are
      then associated with <link to="IMachine"/> objects living in the VirtualBox
      server process to coordinate such changes.

      There are two typical scenarios in which sessions are used:

      
        To alter machine settings or control a running virtual machine, one
          needs to lock a machine for a given session (client process) by calling
          <link to="IMachine::lockMachine"/>.

          Whereas multiple sessions may control a running virtual machine, only
          one process can obtain a write lock on the machine to prevent conflicting
          changes. A write lock is also needed if a process wants to actually run a
          virtual machine in its own context, such as the VirtualBox GUI or
          VBoxHeadless front-ends. They must also lock a machine for their own
          sessions before they are allowed to power up the virtual machine.

          As a result, no machine settings can be altered while another process is
          already using it, either because that process is modifying machine settings
          or because the machine is running.
        
        
          To start a VM using one of the existing VirtualBox front-ends (e.g. the
          VirtualBox GUI or VBoxHeadless), one would use
          <link to="IMachine::launchVMProcess"/>, which also takes a session object
          as its first parameter. This session then identifies the caller and lets the
          caller control the started machine (for example, pause machine execution or
          power it down) as well as be notified about machine execution state changes.
        
      

      How sessions objects are created in a client process depends on whether you use
      the Main API via COM or via the webservice:

      
        When using the COM API directly, an object of the Session class from the
          VirtualBox type library needs to be created. In regular COM C++ client code,
          this can be done by calling createLocalObject(), a standard COM API.
          This object will then act as a local session object in further calls to open
          a session.
        

        In the webservice, the session manager (IWebsessionManager) instead creates
          a session object automatically whenever <link to="IWebsessionManager::logon"/>
          is called. A managed object reference to that session object can be retrieved by
          calling <link to="IWebsessionManager::getSessionObject"/>.
    """
    __uuid__ = '12F4DCDB-12B2-4EC1-B7CD-DDD9F6C5BF4D'
    __wsmap__ = 'managed'
    
    @property
    def state(self):
        """Get SessionState value for 'state'
        Current state of this session.
        """
        ret = self._get_attr("state")
        return SessionState(ret)

    @property
    def type_p(self):
        """Get SessionType value for 'type'
        Type of this session. The value of this attribute is valid only
        if the session currently has a machine locked (i.e. its
        <link to="#state"/> is Locked), otherwise an error will be returned.
        """
        ret = self._get_attr("type")
        return SessionType(ret)

    @property
    def machine(self):
        """Get IMachine value for 'machine'
        Machine object associated with this session.
        """
        ret = self._get_attr("machine")
        return IMachine(ret)

    @property
    def console(self):
        """Get IConsole value for 'console'
        Console object associated with this session.
        """
        ret = self._get_attr("console")
        return IConsole(ret)

    def unlock_machine(self):
        """Unlocks a machine that was previously locked for the current session.

        Calling this method is required every time a machine has been locked
        for a particular session using the <link to="IMachine::launchVMProcess"/>
        or <link to="IMachine::lockMachine"/> calls. Otherwise the state of
        the machine will be set to <link to="MachineState_Aborted"/> on the
        server, and changes made to the machine settings will be lost.

        Generally, it is recommended to unlock all machines explicitly
        before terminating the application (regardless of the reason for
        the termination).

        
          Do not expect the session state (<link to="ISession::state"/>
          to return to "Unlocked" immediately after you invoke this method,
          particularly if you have started a new VM process. The session
          state will automatically return to "Unlocked" once the VM is no
          longer executing, which can of course take a very long time.

        raises E_UNEXPECTED
            Session is not locked.
        
        """
        self._call("unlockMachine")


class IStorageController(Interface):
    """
    Represents a storage controller that is attached to a virtual machine
        (<link to="IMachine"/>). Just as drives (hard disks, DVDs, FDs) are
        attached to storage controllers in a real computer, virtual drives
        (represented by <link to="IMediumAttachment"/>) are attached to virtual
        storage controllers, represented by this interface.

        As opposed to physical hardware, VirtualBox has a very generic concept
        of a storage controller, and for purposes of the Main API, all virtual
        storage is attached to virtual machines via instances of this interface.
        There are five types of such virtual storage controllers: IDE, SCSI, SATA,
        SAS and Floppy (see <link to="#bus"/>). Depending on which of these four
        is used, certain sub-types may be available and can be selected in
        <link to="#controllerType"/>.

        Depending on these settings, the guest operating system might see
        significantly different virtual hardware.
    """
    __uuid__ = 'a1556333-09b6-46d9-bfb7-fc239b7fbe1e'
    __wsmap__ = 'managed'
    
    @property
    def name(self):
        """Get str value for 'name'
        Name of the storage controller, as originally specified with
        <link to="IMachine::addStorageController"/>. This then uniquely
        identifies this controller with other method calls such as
        <link to="IMachine::attachDevice"/> and <link to="IMachine::mountMedium"/>.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def max_devices_per_port_count(self):
        """Get int value for 'maxDevicesPerPortCount'
        Maximum number of devices which can be attached to one port.
        """
        ret = self._get_attr("maxDevicesPerPortCount")
        return ret

    @property
    def min_port_count(self):
        """Get int value for 'minPortCount'
        Minimum number of ports that <link to="IStorageController::portCount"/> can be set to.
        """
        ret = self._get_attr("minPortCount")
        return ret

    @property
    def max_port_count(self):
        """Get int value for 'maxPortCount'
        Maximum number of ports that <link to="IStorageController::portCount"/> can be set to.
        """
        ret = self._get_attr("maxPortCount")
        return ret

    @property
    def instance(self):
        """Get or set int value for 'instance'
        The instance number of the device in the running VM.
        """
        ret = self._get_attr("instance")
        return ret

    @instance.setter
    def instance(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("instance", value)

    @property
    def port_count(self):
        """Get or set int value for 'portCount'
        The number of currently usable ports on the controller.
        The minimum and maximum number of ports for one controller are
        stored in <link to="IStorageController::minPortCount"/>
        and <link to="IStorageController::maxPortCount"/>.
        """
        ret = self._get_attr("portCount")
        return ret

    @port_count.setter
    def port_count(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("portCount", value)

    @property
    def bus(self):
        """Get StorageBus value for 'bus'
        The bus type of the storage controller (IDE, SATA, SCSI, SAS or Floppy).
        """
        ret = self._get_attr("bus")
        return StorageBus(ret)

    @property
    def controller_type(self):
        """Get or set StorageControllerType value for 'controllerType'
        The exact variant of storage controller hardware presented
        to the guest.
        Depending on this value, VirtualBox will provide a different
        virtual storage controller hardware to the guest.
        For SATA, SAS and floppy controllers, only one variant is
        available, but for IDE and SCSI, there are several.

        For SCSI controllers, the default type is LsiLogic.
        """
        ret = self._get_attr("controllerType")
        return StorageControllerType(ret)

    @controller_type.setter
    def controller_type(self, value):
        if not isinstance(value, StorageControllerType):
            raise TypeError("value is not an instance of StorageControllerType")
        return self._set_attr("controllerType", value)

    @property
    def use_host_io_cache(self):
        """Get or set bool value for 'useHostIOCache'
        If true, the storage controller emulation will use a dedicated I/O thread, enable the host I/O
        caches and use synchronous file APIs on the host. This was the only option in the API before
        VirtualBox 3.2 and is still the default for IDE controllers.

        If false, the host I/O cache will be disabled for image files attached to this storage controller.
        Instead, the storage controller emulation will use asynchronous I/O APIs on the host. This makes
        it possible to turn off the host I/O caches because the emulation can handle unaligned access to
        the file. This should be used on OS X and Linux hosts if a high I/O load is expected or many
        virtual machines are running at the same time to prevent I/O cache related hangs.
        This option new with the API of VirtualBox 3.2 and is now the default for non-IDE storage controllers.
        """
        ret = self._get_attr("useHostIOCache")
        return ret

    @use_host_io_cache.setter
    def use_host_io_cache(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("useHostIOCache", value)

    @property
    def bootable(self):
        """Get bool value for 'bootable'
        Returns whether it is possible to boot from disks attached to this controller.
        """
        ret = self._get_attr("bootable")
        return ret


class IPerformanceMetric(Interface):
    """
    The IPerformanceMetric interface represents parameters of the given
      performance metric.
    """
    __uuid__ = '2a1a60ae-9345-4019-ad53-d34ba41cbfe9'
    __wsmap__ = 'managed'
    
    @property
    def metric_name(self):
        """Get str value for 'metricName'
        Name of the metric.
        """
        ret = self._get_attr("metricName")
        return ret

    @property
    def object_p(self):
        """Get Interface value for 'object'
        Object this metric belongs to.
        """
        ret = self._get_attr("object")
        return Interface(ret)

    @property
    def description(self):
        """Get str value for 'description'
        Textual description of the metric.
        """
        ret = self._get_attr("description")
        return ret

    @property
    def period(self):
        """Get int value for 'period'
        Time interval between samples, measured in seconds.
        """
        ret = self._get_attr("period")
        return ret

    @property
    def count(self):
        """Get int value for 'count'
        Number of recent samples retained by the performance collector for this
        metric.

        When the collected sample count exceeds this number, older samples
        are discarded.
        """
        ret = self._get_attr("count")
        return ret

    @property
    def unit(self):
        """Get str value for 'unit'
        Unit of measurement.
        """
        ret = self._get_attr("unit")
        return ret

    @property
    def minimum_value(self):
        """Get int value for 'minimumValue'
        Minimum possible value of this metric.
        """
        ret = self._get_attr("minimumValue")
        return ret

    @property
    def maximum_value(self):
        """Get int value for 'maximumValue'
        Maximum possible value of this metric.
        """
        ret = self._get_attr("maximumValue")
        return ret


class IPerformanceCollector(Interface):
    """
    The IPerformanceCollector interface represents a service that collects
      and stores performance metrics data.

      Performance metrics are associated with objects of interfaces like IHost
      and IMachine. Each object has a distinct set of performance metrics. The
      set can be obtained with <link to="IPerformanceCollector::getMetrics"/>.

      Metric data is collected at the specified intervals and is retained
      internally. The interval and the number of retained samples can be set
      with <link to="IPerformanceCollector::setupMetrics"/>. Both metric data
      and collection settings are not persistent, they are discarded as soon as
      VBoxSVC process terminates. Moreover, metric settings and data associated
      with a particular VM only exist while VM is running. They disappear as
      soon as VM shuts down. It is not possible to set up metrics for machines
      that are powered off. One needs to start VM first, then set up metric
      collection parameters.

      Metrics are organized hierarchically, with each level separated by a
      slash (/) character. Generally, the scheme for metric names is like this:

      Category/Metric[/SubMetric][:aggregation]

      "Category/Metric" together form the base metric name. A base metric is
      the smallest unit for which a sampling interval and the number of
      retained samples can be set. Only base metrics can be enabled and
      disabled. All sub-metrics are collected when their base metric is
      collected. Collected values for any set of sub-metrics can be queried
      with <link to="IPerformanceCollector::queryMetricsData"/>.

      For example "CPU/Load/User:avg" metric name stands for the "CPU"
      category, "Load" metric, "User" submetric, "average" aggregate. An
      aggregate function is computed over all retained data. Valid aggregate
      functions are:

      
          avg -- average
          min -- minimum
          max -- maximum
      

      When setting up metric parameters, querying metric data, enabling or
      disabling metrics wildcards can be used in metric names to specify a
      subset of metrics. For example, to select all CPU-related metrics
      use CPU/*, all averages can be queried using *:avg and
      so on. To query metric values without aggregates *: can be used.

      The valid names for base metrics are:

      
      CPU/Load
      CPU/MHz
      RAM/Usage
      RAM/VMM
      

      The general sequence for collecting and retrieving the metrics is:
      
        
          Obtain an instance of IPerformanceCollector with
          <link to="IVirtualBox::performanceCollector"/>
        
        
          Allocate and populate an array with references to objects the metrics
          will be collected for. Use references to IHost and IMachine objects.
        
        
          Allocate and populate an array with base metric names the data will
          be collected for.
        
        
          Call <link to="IPerformanceCollector::setupMetrics"/>. From now on
          the metric data will be collected and stored.
        
        
          Wait for the data to get collected.
        
        
          Allocate and populate an array with references to objects the metric
          values will be queried for. You can re-use the object array used for
          setting base metrics.
        
        
          Allocate and populate an array with metric names the data will be
          collected for. Note that metric names differ from base metric names.
        
        
          Call <link to="IPerformanceCollector::queryMetricsData"/>. The data
          that have been collected so far are returned. Note that the values
          are still retained internally and data collection continues.
        
      

      For an example of usage refer to the following files in VirtualBox SDK:
      
        
          Java: bindings/webservice/java/jax-ws/samples/metrictest.java
        
        
          Python: bindings/xpcom/python/sample/shellcommon.py
    """
    __uuid__ = 'e22e1acb-ac4a-43bb-a31c-17321659b0c6'
    __wsmap__ = 'managed'
    
    @property
    def metric_names(self):
        """Get str value for 'metricNames'
        Array of unique names of metrics.

        This array represents all metrics supported by the performance
        collector. Individual objects do not necessarily support all of them.
        <link to="IPerformanceCollector::getMetrics"/> can be used to get the
        list of supported metrics for a particular object.
        """
        ret = self._get_attr("metricNames")
        return ret

    def get_metrics(self, metric_names, objects):
        """Returns parameters of specified metrics for a set of objects.
        
          @c Null metrics array means all metrics. @c Null object array means
          all existing objects.

        in metric_names of type str
            Metric name filter. Currently, only a comma-separated list of metrics
          is supported.

        in objects of type Interface
            Set of objects to return metric parameters for.

        return metrics of type IPerformanceMetric
            Array of returned metric parameters.

        """
        if not isinstance(metric_names, list):
            raise TypeError("metric_names can only be an instance of type list")
        for a in metric_names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(objects, list):
            raise TypeError("objects can only be an instance of type list")
        for a in objects[:10]:
            if not isinstance(a, Interface):
                raise TypeError(\
                        "array can only contain objects of type Interface")
        metrics = self._call("getMetrics",
                     in_p=[metric_names, objects])
        metrics = [IPerformanceMetric(a) for a in metrics]
        return metrics

    def setup_metrics(self, metric_names, objects, period, count):
        """Sets parameters of specified base metrics for a set of objects. Returns
        an array of <link to="IPerformanceMetric"/> describing the metrics
        have been affected.
        
          @c Null or empty metric name array means all metrics. @c Null or
          empty object array means all existing objects. If metric name array
          contains a single element and object array contains many, the single
          metric name array element is applied to each object array element to
          form metric/object pairs.

        in metric_names of type str
            Metric name filter. Comma-separated list of metrics with wildcard
          support.

        in objects of type Interface
            Set of objects to setup metric parameters for.

        in period of type int
            Time interval in seconds between two consecutive samples of
          performance data.

        in count of type int
            Number of samples to retain in performance data history. Older
          samples get discarded.

        return affected_metrics of type IPerformanceMetric
            Array of metrics that have been modified by the call to this method.

        """
        if not isinstance(metric_names, list):
            raise TypeError("metric_names can only be an instance of type list")
        for a in metric_names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(objects, list):
            raise TypeError("objects can only be an instance of type list")
        for a in objects[:10]:
            if not isinstance(a, Interface):
                raise TypeError(\
                        "array can only contain objects of type Interface")
        if not isinstance(period, int):
            raise TypeError("period can only be an instance of type int")
        if not isinstance(count, int):
            raise TypeError("count can only be an instance of type int")
        affected_metrics = self._call("setupMetrics",
                     in_p=[metric_names, objects, period, count])
        affected_metrics = [IPerformanceMetric(a) for a in affected_metrics]
        return affected_metrics

    def enable_metrics(self, metric_names, objects):
        """Turns on collecting specified base metrics. Returns an array of
        <link to="IPerformanceMetric"/> describing the metrics have been
        affected.
        
          @c Null or empty metric name array means all metrics. @c Null or
          empty object array means all existing objects. If metric name array
          contains a single element and object array contains many, the single
          metric name array element is applied to each object array element to
          form metric/object pairs.

        in metric_names of type str
            Metric name filter. Comma-separated list of metrics with wildcard
          support.

        in objects of type Interface
            Set of objects to enable metrics for.

        return affected_metrics of type IPerformanceMetric
            Array of metrics that have been modified by the call to this method.

        """
        if not isinstance(metric_names, list):
            raise TypeError("metric_names can only be an instance of type list")
        for a in metric_names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(objects, list):
            raise TypeError("objects can only be an instance of type list")
        for a in objects[:10]:
            if not isinstance(a, Interface):
                raise TypeError(\
                        "array can only contain objects of type Interface")
        affected_metrics = self._call("enableMetrics",
                     in_p=[metric_names, objects])
        affected_metrics = [IPerformanceMetric(a) for a in affected_metrics]
        return affected_metrics

    def disable_metrics(self, metric_names, objects):
        """Turns off collecting specified base metrics. Returns an array of
        <link to="IPerformanceMetric"/> describing the metrics have been
        affected.
        
          @c Null or empty metric name array means all metrics. @c Null or
          empty object array means all existing objects. If metric name array
          contains a single element and object array contains many, the single
          metric name array element is applied to each object array element to
          form metric/object pairs.

        in metric_names of type str
            Metric name filter. Comma-separated list of metrics with wildcard
          support.

        in objects of type Interface
            Set of objects to disable metrics for.

        return affected_metrics of type IPerformanceMetric
            Array of metrics that have been modified by the call to this method.

        """
        if not isinstance(metric_names, list):
            raise TypeError("metric_names can only be an instance of type list")
        for a in metric_names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(objects, list):
            raise TypeError("objects can only be an instance of type list")
        for a in objects[:10]:
            if not isinstance(a, Interface):
                raise TypeError(\
                        "array can only contain objects of type Interface")
        affected_metrics = self._call("disableMetrics",
                     in_p=[metric_names, objects])
        affected_metrics = [IPerformanceMetric(a) for a in affected_metrics]
        return affected_metrics

    def query_metrics_data(self, metric_names, objects):
        """Queries collected metrics data for a set of objects.

        The data itself and related metric information are returned in seven
        parallel and one flattened array of arrays. Elements of
        returnMetricNames, returnObjects, returnUnits, returnScales,
        returnSequenceNumbers, returnDataIndices and returnDataLengths with
        the same index describe one set of values corresponding to a single
        metric.

        The returnData parameter is a flattened array of arrays. Each
        start and length of a sub-array is indicated by
        returnDataIndices and returnDataLengths. The first
        value for metric metricNames[i] is at
        returnData[returnIndices[i]].

        
          @c Null or empty metric name array means all metrics. @c Null or
          empty object array means all existing objects. If metric name array
          contains a single element and object array contains many, the single
          metric name array element is applied to each object array element to
          form metric/object pairs.
        
        
          Data collection continues behind the scenes after call to
          @c queryMetricsData. The return data can be seen as the snapshot of
          the current state at the time of @c queryMetricsData call. The
          internally kept metric values are not cleared by the call. This
          allows querying different subsets of metrics or aggregates with
          subsequent calls. If periodic querying is needed it is highly
          suggested to query the values with @c interval*count period to avoid
          confusion. This way a completely new set of data values will be
          provided by each query.

        in metric_names of type str
            Metric name filter. Comma-separated list of metrics with wildcard
          support.

        in objects of type Interface
            Set of objects to query metrics for.

        out return_metric_names of type str
            Names of metrics returned in @c returnData.

        out return_objects of type Interface
            Objects associated with metrics returned in @c returnData.

        out return_units of type str
            Units of measurement for each returned metric.

        out return_scales of type int
            Divisor that should be applied to return values in order to get
          floating point values. For example:
          (double)returnData[returnDataIndices[0]+i] / returnScales[0]
          will retrieve the floating point value of i-th sample of the first
          metric.

        out return_sequence_numbers of type int
            Sequence numbers of the first elements of value sequences of
          particular metrics returned in @c returnData. For aggregate metrics
          it is the sequence number of the sample the aggregate started
          calculation from.

        out return_data_indices of type int
            Indices of the first elements of value sequences of particular
          metrics returned in @c returnData.

        out return_data_lengths of type int
            Lengths of value sequences of particular metrics.

        return return_data of type int
            Flattened array of all metric data containing sequences of values for
          each metric.

        """
        if not isinstance(metric_names, list):
            raise TypeError("metric_names can only be an instance of type list")
        for a in metric_names[:10]:
            if type(a) not in [str, unicode]:
                raise TypeError("array can only contain str or unicode")
        if not isinstance(objects, list):
            raise TypeError("objects can only be an instance of type list")
        for a in objects[:10]:
            if not isinstance(a, Interface):
                raise TypeError(\
                        "array can only contain objects of type Interface")
        (return_metric_names, return_objects, return_units, return_scales, return_sequence_numbers, return_data_indices, return_data_lengths, return_data) = self._call("queryMetricsData",
                     in_p=[metric_names, objects])
        return_objects = [Interface(a) for a in return_objects]
        return (return_metric_names, return_objects, return_units, return_scales, return_sequence_numbers, return_data_indices, return_data_lengths, return_data)


class INATEngine(Interface):
    """
    Interface for managing a NAT engine which is used with a virtual machine. This
      allows for changing NAT behavior such as port-forwarding rules. This interface is
      used in the <link to="INetworkAdapter::NATEngine"/> attribute.
    """
    __uuid__ = '26451b99-3b2d-4dcb-8e4b-d63654218175'
    __wsmap__ = 'managed'
    
    @property
    def network(self):
        """Get or set str value for 'network'
        The network attribute of the NAT engine (the same value is used with built-in
        DHCP server to fill corresponding fields of DHCP leases).
        """
        ret = self._get_attr("network")
        return ret

    @network.setter
    def network(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("network", value)

    @property
    def host_ip(self):
        """Get or set str value for 'hostIP'
        IP of host interface to bind all opened sockets to.
          Changing this does not change binding of port forwarding.
        """
        ret = self._get_attr("hostIP")
        return ret

    @host_ip.setter
    def host_ip(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("hostIP", value)

    @property
    def tftp_prefix(self):
        """Get or set str value for 'TFTPPrefix'
        TFTP prefix attribute which is used with the built-in DHCP server to fill
        the corresponding fields of DHCP leases.
        """
        ret = self._get_attr("TFTPPrefix")
        return ret

    @tftp_prefix.setter
    def tftp_prefix(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("TFTPPrefix", value)

    @property
    def tftp_boot_file(self):
        """Get or set str value for 'TFTPBootFile'
        TFTP boot file attribute which is used with the built-in DHCP server to fill
        the corresponding fields of DHCP leases.
        """
        ret = self._get_attr("TFTPBootFile")
        return ret

    @tftp_boot_file.setter
    def tftp_boot_file(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("TFTPBootFile", value)

    @property
    def tftp_next_server(self):
        """Get or set str value for 'TFTPNextServer'
        TFTP server attribute which is used with the built-in DHCP server to fill
        the corresponding fields of DHCP leases.
        The preferred form is IPv4 addresses.
        """
        ret = self._get_attr("TFTPNextServer")
        return ret

    @tftp_next_server.setter
    def tftp_next_server(self, value):
        if type(value) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return self._set_attr("TFTPNextServer", value)

    @property
    def alias_mode(self):
        """Get or set int value for 'aliasMode'
        <desc/>
        """
        ret = self._get_attr("aliasMode")
        return ret

    @alias_mode.setter
    def alias_mode(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("aliasMode", value)

    @property
    def dns_pass_domain(self):
        """Get or set bool value for 'DNSPassDomain'
        Whether the DHCP server should pass the DNS domain used by the host.
        """
        ret = self._get_attr("DNSPassDomain")
        return ret

    @dns_pass_domain.setter
    def dns_pass_domain(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("DNSPassDomain", value)

    @property
    def dns_proxy(self):
        """Get or set bool value for 'DNSProxy'
        Whether the DHCP server (and the DNS traffic by NAT) should pass the address
        of the DNS proxy and process traffic using DNS servers registered on the host.
        """
        ret = self._get_attr("DNSProxy")
        return ret

    @dns_proxy.setter
    def dns_proxy(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("DNSProxy", value)

    @property
    def dns_use_host_resolver(self):
        """Get or set bool value for 'DNSUseHostResolver'
        Whether the DHCP server (and the DNS traffic by NAT) should pass the address
        of the DNS proxy and process traffic using the host resolver mechanism.
        """
        ret = self._get_attr("DNSUseHostResolver")
        return ret

    @dns_use_host_resolver.setter
    def dns_use_host_resolver(self, value):
        if not isinstance(value, bool):
            raise TypeError("value is not an instance of bool")
        return self._set_attr("DNSUseHostResolver", value)

    @property
    def redirects(self):
        """Get str value for 'redirects'
        Array of NAT port-forwarding rules in string representation, in the following
        format: "name,protocol id,host ip,host port,guest ip,guest port".
        """
        ret = self._get_attr("redirects")
        return ret

    def set_network_settings(self, mtu, sock_snd, sock_rcv, tcp_wnd_snd, tcp_wnd_rcv):
        """Sets network configuration of the NAT engine.

        in mtu of type int
            MTU (maximum transmission unit) of the NAT engine in bytes.

        in sock_snd of type int
            Capacity of the socket send buffer in bytes when creating a new socket.

        in sock_rcv of type int
            Capacity of the socket receive buffer in bytes when creating a new socket.

        in tcp_wnd_snd of type int
            Initial size of the NAT engine's sending TCP window in bytes when
          establishing a new TCP connection.

        in tcp_wnd_rcv of type int
            Initial size of the NAT engine's receiving TCP window in bytes when
          establishing a new TCP connection.

        """
        if not isinstance(mtu, int):
            raise TypeError("mtu can only be an instance of type int")
        if not isinstance(sock_snd, int):
            raise TypeError("sock_snd can only be an instance of type int")
        if not isinstance(sock_rcv, int):
            raise TypeError("sock_rcv can only be an instance of type int")
        if not isinstance(tcp_wnd_snd, int):
            raise TypeError("tcp_wnd_snd can only be an instance of type int")
        if not isinstance(tcp_wnd_rcv, int):
            raise TypeError("tcp_wnd_rcv can only be an instance of type int")
        self._call("setNetworkSettings",
                     in_p=[mtu, sock_snd, sock_rcv, tcp_wnd_snd, tcp_wnd_rcv])

    def get_network_settings(self):
        """Returns network configuration of NAT engine. See <link to="#setNetworkSettings"/>
        for parameter descriptions.

        out mtu of type int

        out sock_snd of type int

        out sock_rcv of type int

        out tcp_wnd_snd of type int

        out tcp_wnd_rcv of type int

        """
        (mtu, sock_snd, sock_rcv, tcp_wnd_snd, tcp_wnd_rcv) = self._call("getNetworkSettings")
        return (mtu, sock_snd, sock_rcv, tcp_wnd_snd, tcp_wnd_rcv)

    def add_redirect(self, name, proto, host_ip, host_port, guest_ip, guest_port):
        """Adds a new NAT port-forwarding rule.

        in name of type str
            The name of the rule. An empty name is acceptable, in which case the NAT engine
            auto-generates one using the other parameters.

        in proto of type NATProtocol
            Protocol handled with the rule.

        in host_ip of type str
            IP of the host interface to which the rule should apply. An empty ip address is
            acceptable, in which case the NAT engine binds the handling socket to any interface.

        in host_port of type int
            The port number to listen on.

        in guest_ip of type str
            The IP address of the guest which the NAT engine will forward matching packets
            to. An empty IP address is acceptable, in which case the NAT engine will forward
            packets to the first DHCP lease (x.x.x.15).

        in guest_port of type int
            The port number to forward.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(proto, NATProtocol):
            raise TypeError("proto can only be an instance of type NATProtocol")
        if type(host_ip) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(host_port, int):
            raise TypeError("host_port can only be an instance of type int")
        if type(guest_ip) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(guest_port, int):
            raise TypeError("guest_port can only be an instance of type int")
        self._call("addRedirect",
                     in_p=[name, proto, host_ip, host_port, guest_ip, guest_port])

    def remove_redirect(self, name):
        """Removes a port-forwarding rule that was previously registered.

        in name of type str
            The name of the rule to delete.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("removeRedirect",
                     in_p=[name])


class IExtPackPlugIn(Interface):
    """
    Interface for keeping information about a plug-in that ships with an
      extension pack.
    """
    __uuid__ = '58000040-e718-4746-bbce-4b86d96da461'
    __wsmap__ = 'suppress'
    
    @property
    def name(self):
        """Get str value for 'name'
        The plug-in name.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def description(self):
        """Get str value for 'description'
        The plug-in description.
        """
        ret = self._get_attr("description")
        return ret

    @property
    def frontend(self):
        """Get str value for 'frontend'
        The name of the frontend or component name this plug-in plugs into.
        """
        ret = self._get_attr("frontend")
        return ret

    @property
    def module_path(self):
        """Get str value for 'modulePath'
        The module path.
        """
        ret = self._get_attr("modulePath")
        return ret


class IExtPackBase(Interface):
    """
    Interface for querying information about an extension pack as well as
      accessing COM objects within it.
    """
    __uuid__ = 'f79b75d8-2890-4f34-ffff-ffffa144e82c'
    __wsmap__ = 'suppress'
    
    @property
    def name(self):
        """Get str value for 'name'
        The extension pack name. This is unique.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def description(self):
        """Get str value for 'description'
        The extension pack description.
        """
        ret = self._get_attr("description")
        return ret

    @property
    def version(self):
        """Get str value for 'version'
        The extension pack version string. This is restricted to the dotted
        version number and optionally a build indicator. No tree revision or
        tag will be included in the string as those things are available as
        separate properties. An optional publisher tag may be present like for
        <link to="IVirtualBox::version"/>.

        Examples: "1.2.3", "1.2.3_BETA1" and "1.2.3_RC2".
        """
        ret = self._get_attr("version")
        return ret

    @property
    def revision(self):
        """Get int value for 'revision'
        The extension pack internal revision number.
        """
        ret = self._get_attr("revision")
        return ret

    @property
    def edition(self):
        """Get str value for 'edition'
        Edition indicator. This is usually empty.

        Can for instance be used to help distinguishing between two editions
        of the same extension pack where only the license, service contract or
        something differs.
        """
        ret = self._get_attr("edition")
        return ret

    @property
    def vrde_module(self):
        """Get str value for 'VRDEModule'
        The name of the VRDE module if the extension pack sports one.
        """
        ret = self._get_attr("VRDEModule")
        return ret

    @property
    def plug_ins(self):
        """Get IExtPackPlugIn value for 'plugIns'
        Plug-ins provided by this extension pack.
        """
        ret = self._get_attr("plugIns")
        return [IExtPackPlugIn(a) for a in ret]

    @property
    def usable(self):
        """Get bool value for 'usable'
        Indicates whether the extension pack is usable or not.

        There are a number of reasons why an extension pack might be unusable,
        typical examples would be broken installation/file or that it is
        incompatible with the current VirtualBox version.
        """
        ret = self._get_attr("usable")
        return ret

    @property
    def why_unusable(self):
        """Get str value for 'whyUnusable'
        String indicating why the extension pack is not usable. This is an
        empty string if usable and always a non-empty string if not usable.
        """
        ret = self._get_attr("whyUnusable")
        return ret

    @property
    def show_license(self):
        """Get bool value for 'showLicense'
        Whether to show the license before installation
        """
        ret = self._get_attr("showLicense")
        return ret

    @property
    def license_p(self):
        """Get str value for 'license'
        The default HTML license text for the extension pack. Same as
        calling <link to="#queryLicense">queryLicense</link> with
        preferredLocale and preferredLanguage as empty strings and format set
        to html.
        """
        ret = self._get_attr("license")
        return ret

    def query_license(self, preferred_locale, preferred_language, format_p):
        """Full feature version of the license attribute.

        in preferred_locale of type str
            The preferred license locale. Pass an empty string to get the default
          license.

        in preferred_language of type str
            The preferred license language. Pass an empty string to get the
          default language for the locale.

        in format_p of type str
            The license format: html, rtf or txt. If a license is present there
          will always be an HTML of it, the rich text format (RTF) and plain
          text (txt) versions are optional. If

        return license_text of type str
            The license text.

        """
        if type(preferred_locale) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(preferred_language) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if type(format_p) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        license_text = self._call("queryLicense",
                     in_p=[preferred_locale, preferred_language, format_p])
        return license_text


class IExtPack(IExtPackBase):
    """
    Interface for querying information about an extension pack as well as
      accessing COM objects within it.
    """
    __uuid__ = '431685da-3618-4ebc-b038-833ba829b4b2'
    __wsmap__ = 'suppress'
    
    def query_object(self, obj_uuid):
        """Queries the IUnknown interface to an object in the extension pack
        main module. This allows plug-ins and others to talk directly to an
        extension pack.

        in obj_uuid of type str
            The object ID. What exactly this is

        return return_interface of type Interface
            The queried interface.

        """
        if type(obj_uuid) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return_interface = self._call("queryObject",
                     in_p=[obj_uuid])
        return_interface = Interface(return_interface)
        return return_interface


class IExtPackFile(IExtPackBase):
    """
    Extension pack file (aka tarball, .vbox-extpack) representation returned
      by <link to="IExtPackManager::openExtPackFile"/>. This provides the base
      extension pack information with the addition of the file name.
    """
    __uuid__ = 'b6b49f55-efcc-4f08-b486-56e8d8afb10b'
    __wsmap__ = 'suppress'
    
    @property
    def file_path(self):
        """Get str value for 'filePath'
        The path to the extension pack file.
        """
        ret = self._get_attr("filePath")
        return ret

    def install(self, replace, display_info):
        """Install the extension pack.

        in replace of type bool
            Set this to automatically uninstall any existing extension pack with
          the same name as the one being installed.

        in display_info of type str
            Platform specific display information. Reserved for future hacks.

        return progess of type IProgress
            Progress object for the operation.

        """
        if not isinstance(replace, bool):
            raise TypeError("replace can only be an instance of type bool")
        if type(display_info) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progess = self._call("install",
                     in_p=[replace, display_info])
        progess = IProgress(progess)
        return progess


class IExtPackManager(Interface):
    """
    Interface for managing VirtualBox Extension Packs.

      TODO: Describe extension packs, how they are managed and how to create
            one.
    """
    __uuid__ = '3295e6ce-b051-47b2-9514-2c588bfe7554'
    __wsmap__ = 'suppress'
    
    @property
    def installed_ext_packs(self):
        """Get IExtPack value for 'installedExtPacks'
        List of the installed extension packs.
        """
        ret = self._get_attr("installedExtPacks")
        return [IExtPack(a) for a in ret]

    def find(self, name):
        """Returns the extension pack with the specified name if found.

        in name of type str
            The name of the extension pack to locate.

        return return_data of type IExtPack
            The extension pack if found.

        raises VBOX_E_OBJECT_NOT_FOUND
            No extension pack matching @a name was found.
        
        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        return_data = self._call("find",
                     in_p=[name])
        return_data = IExtPack(return_data)
        return return_data

    def open_ext_pack_file(self, path):
        """Attempts to open an extension pack file in preparation for
        installation.

        in path of type str
            The path of the extension pack tarball. This can optionally be
        followed by a "::SHA-256=hex-digit" of the tarball.

        return file_p of type IExtPackFile
            The interface of the extension pack file object.

        """
        if type(path) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        file_p = self._call("openExtPackFile",
                     in_p=[path])
        file_p = IExtPackFile(file_p)
        return file_p

    def uninstall(self, name, forced_removal, display_info):
        """Uninstalls an extension pack, removing all related files.

        in name of type str
            The name of the extension pack to uninstall.

        in forced_removal of type bool
            Forced removal of the extension pack. This means that the uninstall
          hook will not be called.

        in display_info of type str
            Platform specific display information. Reserved for future hacks.

        return progess of type IProgress
            Progress object for the operation.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(forced_removal, bool):
            raise TypeError("forced_removal can only be an instance of type bool")
        if type(display_info) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        progess = self._call("uninstall",
                     in_p=[name, forced_removal, display_info])
        progess = IProgress(progess)
        return progess

    def cleanup(self):
        """Cleans up failed installs and uninstalls

        """
        self._call("cleanup")

    def query_all_plug_ins_for_frontend(self, frontend_name):
        """Gets the path to all the plug-in modules for a given frontend.

        This is a convenience method that is intended to simplify the plug-in
        loading process for a frontend.

        in frontend_name of type str
            The name of the frontend or component.

        return plug_in_modules of type str
            Array containing the plug-in modules (full paths).

        """
        if type(frontend_name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        plug_in_modules = self._call("queryAllPlugInsForFrontend",
                     in_p=[frontend_name])
        return plug_in_modules

    def is_ext_pack_usable(self, name):
        """Check if the given extension pack is loaded and usable.

        in name of type str
            The name of the extension pack to check for.

        return usable of type bool
            Is the given extension pack loaded and usable.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        usable = self._call("isExtPackUsable",
                     in_p=[name])
        return usable


class IBandwidthGroup(Interface):
    """
    Represents one bandwidth group.
    """
    __uuid__ = 'badea2d7-0261-4146-89f0-6a57cc34833d'
    __wsmap__ = 'managed'
    
    @property
    def name(self):
        """Get str value for 'name'
        Name of the group.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def type_p(self):
        """Get BandwidthGroupType value for 'type'
        Type of the group.
        """
        ret = self._get_attr("type")
        return BandwidthGroupType(ret)

    @property
    def reference(self):
        """Get int value for 'reference'
        How many devices/medium attachements use this group.
        """
        ret = self._get_attr("reference")
        return ret

    @property
    def max_bytes_per_sec(self):
        """Get or set int value for 'maxBytesPerSec'
        The maximum number of bytes which can be transfered by all
        entities attached to this group during one second.
        """
        ret = self._get_attr("maxBytesPerSec")
        return ret

    @max_bytes_per_sec.setter
    def max_bytes_per_sec(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("maxBytesPerSec", value)


class IBandwidthControl(Interface):
    """
    Controls the bandwidth groups of one machine used to cap I/O done by a VM.
      This includes network and disk I/O.
    """
    __uuid__ = 'e2eb3930-d2f4-4f87-be17-0707e30f019f'
    __wsmap__ = 'managed'
    
    @property
    def num_groups(self):
        """Get int value for 'numGroups'
        The current number of existing bandwidth groups managed.
        """
        ret = self._get_attr("numGroups")
        return ret

    def create_bandwidth_group(self, name, type_p, max_bytes_per_sec):
        """Creates a new bandwidth group.

        in name of type str
            Name of the bandwidth group.

        in type_p of type BandwidthGroupType
            The type of the bandwidth group (network or disk).

        in max_bytes_per_sec of type int
            The maximum number of bytes which can be transfered by all
          entities attached to this group during one second.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        if not isinstance(type_p, BandwidthGroupType):
            raise TypeError("type_p can only be an instance of type BandwidthGroupType")
        if not isinstance(max_bytes_per_sec, int):
            raise TypeError("max_bytes_per_sec can only be an instance of type int")
        self._call("createBandwidthGroup",
                     in_p=[name, type_p, max_bytes_per_sec])

    def delete_bandwidth_group(self, name):
        """Deletes a new bandwidth group.

        in name of type str
            Name of the bandwidth group to delete.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("deleteBandwidthGroup",
                     in_p=[name])

    def get_bandwidth_group(self, name):
        """Get a bandwidth group by name.

        in name of type str
            Name of the bandwidth group to get.

        return bandwidth_group of type IBandwidthGroup
            Where to store the bandwidth group on success.

        """
        if type(name) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        bandwidth_group = self._call("getBandwidthGroup",
                     in_p=[name])
        bandwidth_group = IBandwidthGroup(bandwidth_group)
        return bandwidth_group

    def get_all_bandwidth_groups(self):
        """Get all managed bandwidth groups.

        return bandwidth_groups of type IBandwidthGroup
            The array of managed bandwidth groups.

        """
        bandwidth_groups = self._call("getAllBandwidthGroups")
        bandwidth_groups = [IBandwidthGroup(a) for a in bandwidth_groups]
        return bandwidth_groups


class IVirtualBoxClient(Interface):
    """
    Convenience interface for client applications. Treat this as a
      singleton, i.e. never create more than one instance of this interface.

      At the moment only available for clients of the local API (not usable
      via the webservice). Once the session logic is redesigned this might
      change.
    """
    __uuid__ = 'd191281f-b0cb-4d83-a8fa-0d9fd6ba234c'
    __wsmap__ = 'suppress'
    
    @property
    def virtual_box(self):
        """Get IVirtualBox value for 'virtualBox'
        Reference to the server-side API root object.
        """
        ret = self._get_attr("virtualBox")
        return IVirtualBox(ret)

    @property
    def session(self):
        """Get ISession value for 'session'
        Create a new session object and return the reference to it.
        """
        ret = self._get_attr("session")
        return ISession(ret)

    @property
    def event_source(self):
        """Get IEventSource value for 'eventSource'
        Event source for VirtualBoxClient events.
        """
        ret = self._get_attr("eventSource")
        return IEventSource(ret)

    def check_machine_error(self, machine):
        """Perform error checking before using an <link to="IMachine"/> object.
        Generally useful before starting a VM and all other uses. If anything
        is not as it should be then this method will return an appropriate
        error.

        in machine of type IMachine
            The machine object to check.

        """
        if not isinstance(machine, IMachine):
            raise TypeError("machine can only be an instance of type IMachine")
        self._call("checkMachineError",
                     in_p=[machine])


class IEventSource(Interface):
    """
    Event source. Generally, any object which could generate events can be an event source,
      or aggregate one. To simplify using one-way protocols such as webservices running on top of HTTP(S),
      an event source can work with listeners in either active or passive mode. In active mode it is up to
      the IEventSource implementation to call <link to="IEventListener::handleEvent"/>, in passive mode the
      event source keeps track of pending events for each listener and returns available events on demand.

      See <link to="IEvent"/> for an introduction to VirtualBox event handling.
    """
    __uuid__ = '9b6e1aee-35f3-4f4d-b5bb-ed0ecefd8538'
    __wsmap__ = 'managed'
    
    def create_listener(self):
        """Creates a new listener object, useful for passive mode.

        return listener of type IEventListener

        """
        listener = self._call("createListener")
        listener = IEventListener(listener)
        return listener

    def create_aggregator(self, subordinates):
        """Creates an aggregator event source, collecting events from multiple sources.
        This way a single listener can listen for events coming from multiple sources,
        using a single blocking <link to="#getEvent"/> on the returned aggregator.

        in subordinates of type IEventSource
            Subordinate event source this one aggregatres.

        return result of type IEventSource
            Event source aggregating passed sources.

        """
        if not isinstance(subordinates, list):
            raise TypeError("subordinates can only be an instance of type list")
        for a in subordinates[:10]:
            if not isinstance(a, IEventSource):
                raise TypeError(\
                        "array can only contain objects of type IEventSource")
        result = self._call("createAggregator",
                     in_p=[subordinates])
        result = IEventSource(result)
        return result

    def register_listener(self, listener, interesting, active):
        """Register an event listener.

        
          To avoid system overload, the VirtualBox server process checks if passive event
          listeners call <link to="IEventSource::getEvent"/> frequently enough. In the
          current implementation, if more than 500 pending events are detected for a passive
          event listener, it is forcefully unregistered by the system, and further
          <link to="#getEvent"/> calls will return @c VBOX_E_OBJECT_NOT_FOUND.

        in listener of type IEventListener
            Listener to register.

        in interesting of type VBoxEventType
            Event types listener is interested in. One can use wildcards like -
          <link to="VBoxEventType_Any"/> to specify wildcards, matching more
          than one event.

        in active of type bool
            Which mode this listener is operating in.
          In active mode, <link to="IEventListener::handleEvent"/> is called directly.
          In passive mode, an internal event queue is created for this this IEventListener.
          For each event coming in, it is added to queues for all interested registered passive
          listeners. It is then up to the external code to call the listener's
          <link to="IEventListener::handleEvent"/> method. When done with an event, the
          external code must call <link to="#eventProcessed"/>.

        """
        if not isinstance(listener, IEventListener):
            raise TypeError("listener can only be an instance of type IEventListener")
        if not isinstance(interesting, list):
            raise TypeError("interesting can only be an instance of type list")
        for a in interesting[:10]:
            if not isinstance(a, VBoxEventType):
                raise TypeError(\
                        "array can only contain objects of type VBoxEventType")
        if not isinstance(active, bool):
            raise TypeError("active can only be an instance of type bool")
        self._call("registerListener",
                     in_p=[listener, interesting, active])

    def unregister_listener(self, listener):
        """Unregister an event listener. If listener is passive, and some waitable events are still
        in queue they are marked as processed automatically.

        in listener of type IEventListener
            Listener to unregister.

        """
        if not isinstance(listener, IEventListener):
            raise TypeError("listener can only be an instance of type IEventListener")
        self._call("unregisterListener",
                     in_p=[listener])

    def fire_event(self, event, timeout):
        """Fire an event for this source.

        in event of type IEvent
            Event to deliver.

        in timeout of type int
            Maximum time to wait for event processing (if event is waitable), in ms;
          0 = no wait, -1 = indefinite wait.

        return result of type bool
            true if an event was delivered to all targets, or is non-waitable.

        """
        if not isinstance(event, IEvent):
            raise TypeError("event can only be an instance of type IEvent")
        if not isinstance(timeout, int):
            raise TypeError("timeout can only be an instance of type int")
        result = self._call("fireEvent",
                     in_p=[event, timeout])
        return result

    def get_event(self, listener, timeout):
        """Get events from this peer's event queue (for passive mode). Calling this method
        regularly is required for passive event listeners to avoid system overload;
        see <link to="IEventSource::registerListener"/> for details.

        in listener of type IEventListener
            Which listener to get data for.

        in timeout of type int
            Maximum time to wait for events, in ms;
          0 = no wait, -1 = indefinite wait.

        return event of type IEvent
            Event retrieved, or null if none available.

        raises VBOX_E_OBJECT_NOT_FOUND
            Listener is not registered, or autounregistered.
        
        """
        if not isinstance(listener, IEventListener):
            raise TypeError("listener can only be an instance of type IEventListener")
        if not isinstance(timeout, int):
            raise TypeError("timeout can only be an instance of type int")
        event = self._call("getEvent",
                     in_p=[listener, timeout])
        event = IEvent(event)
        return event

    def event_processed(self, listener, event):
        """Must be called for waitable events after a particular listener finished its
        event processing. When all listeners of a particular event have called this
        method, the system will then call <link to="IEvent::setProcessed"/>.

        in listener of type IEventListener
            Which listener processed event.

        in event of type IEvent
            Which event.

        """
        if not isinstance(listener, IEventListener):
            raise TypeError("listener can only be an instance of type IEventListener")
        if not isinstance(event, IEvent):
            raise TypeError("event can only be an instance of type IEvent")
        self._call("eventProcessed",
                     in_p=[listener, event])


class IEventListener(Interface):
    """
    Event listener. An event listener can work in either active or passive mode, depending on the way
      it was registered.
      See <link to="IEvent"/> for an introduction to VirtualBox event handling.
    """
    __uuid__ = '67099191-32e7-4f6c-85ee-422304c71b90'
    __wsmap__ = 'managed'
    
    def handle_event(self, event):
        """Handle event callback for active listeners. It is not called for
        passive listeners. After calling <link to="#handleEvent"/> on all active listeners
        and having received acknowledgement from all passive listeners via
        <link to="IEventSource::eventProcessed"/>, the event is marked as
        processed and <link to="IEvent::waitProcessed"/> will return
        immediately.

        in event of type IEvent
            Event available.

        """
        if not isinstance(event, IEvent):
            raise TypeError("event can only be an instance of type IEvent")
        self._call("handleEvent",
                     in_p=[event])


class IEvent(Interface):
    """
    Abstract parent interface for VirtualBox events. Actual events will typically implement
      a more specific interface which derives from this (see below).

      Introduction to VirtualBox events

      Generally speaking, an event (represented by this interface) signals that something
      happened, while an event listener (see <link to="IEventListener"/>) represents an
      entity that is interested in certain events. In order for this to work with
      unidirectional protocols (i.e. web services), the concepts of passive and active
      listener are used.

      Event consumers can register themselves as listeners, providing an array of
      events they are interested in (see <link to="IEventSource::registerListener"/>).
      When an event triggers, the listener is notified about the event. The exact
      mechanism of the notification depends on whether the listener was registered as
      an active or passive listener:

      
        An active listener is very similar to a callback: it is a function invoked
          by the API. As opposed to the callbacks that were used in the API before
          VirtualBox 4.0 however, events are now objects with an interface hierarchy.
        

        Passive listeners are somewhat trickier to implement, but do not require
          a client function to be callable, which is not an option with scripting
          languages or web service clients. Internally the <link to="IEventSource"/>
          implementation maintains an event queue for each passive listener, and
          newly arrived events are put in this queue. When the listener calls
          <link to="IEventSource::getEvent"/>, first element from its internal event
          queue is returned. When the client completes processing of an event,
          the <link to="IEventSource::eventProcessed"/> function must be called,
          acknowledging that the event was processed. It supports implementing
          waitable events. On passive listener unregistration, all events from its
          queue are auto-acknowledged.
        
      

      Waitable events are useful in situations where the event generator wants to track
      delivery or a party wants to wait until all listeners have completed the event. A
      typical example would be a vetoable event (see <link to="IVetoEvent"/>) where a
      listeners might veto a certain action, and thus the event producer has to make
      sure that all listeners have processed the event and not vetoed before taking
      the action.

      A given event may have both passive and active listeners at the same time.

      Using events

      Any VirtualBox object capable of producing externally visible events provides an
      @c eventSource read-only attribute, which is of the type <link to="IEventSource"/>.
      This event source object is notified by VirtualBox once something has happened, so
      consumers may register event listeners with this event source. To register a listener,
      an object implementing the <link to="IEventListener"/> interface must be provided.
      For active listeners, such an object is typically created by the consumer, while for
      passive listeners <link to="IEventSource::createListener"/> should be used. Please
      note that a listener created with <link to="IEventSource::createListener"/> must not be used as an active listener.

      Once created, the listener must be registered to listen for the desired events
      (see <link to="IEventSource::registerListener"/>), providing an array of
      <link to="VBoxEventType"/> enums. Those elements can either be the individual
      event IDs or wildcards matching multiple event IDs.

      After registration, the callback's <link to="IEventListener::handleEvent"/> method is
      called automatically when the event is triggered, while passive listeners have to call
      <link to="IEventSource::getEvent"/> and <link to="IEventSource::eventProcessed"/> in
      an event processing loop.

      The IEvent interface is an abstract parent interface for all such VirtualBox events
      coming in. As a result, the standard use pattern inside <link to="IEventListener::handleEvent"/>
      or the event processing loop is to check the <link to="#type"/> attribute of the event and
      then cast to the appropriate specific interface using @c QueryInterface().
    """
    __uuid__ = '0ca2adba-8f30-401b-a8cd-fe31dbe839c0'
    __wsmap__ = 'managed'
    
    @property
    def type_p(self):
        """Get VBoxEventType value for 'type'
        Event type.
        """
        ret = self._get_attr("type")
        return VBoxEventType(ret)

    @property
    def source(self):
        """Get IEventSource value for 'source'
        Source of this event.
        """
        ret = self._get_attr("source")
        return IEventSource(ret)

    @property
    def waitable(self):
        """Get bool value for 'waitable'
        If we can wait for this event being processed. If false, <link to="#waitProcessed"/> returns immediately,
        and <link to="#setProcessed"/> doesn't make sense. Non-waitable events are generally better performing,
        as no additional overhead associated with waitability imposed.
        Waitable events are needed when one need to be able to wait for particular event processed,
        for example for vetoable changes, or if event refers to some resource which need to be kept immutable
        until all consumers confirmed events.
        """
        ret = self._get_attr("waitable")
        return ret

    def set_processed(self):
        """Internal method called by the system when all listeners of a particular event have called
        <link to="IEventSource::eventProcessed"/>. This should not be called by client code.

        """
        self._call("setProcessed")

    def wait_processed(self, timeout):
        """Wait until time outs, or this event is processed. Event must be waitable for this operation to have
        described semantics, for non-waitable returns true immediately.

        in timeout of type int
            Maximum time to wait for event processeing, in ms;
          0 = no wait, -1 = indefinite wait.

        return result of type bool
            If this event was processed before timeout.

        """
        if not isinstance(timeout, int):
            raise TypeError("timeout can only be an instance of type int")
        result = self._call("waitProcessed",
                     in_p=[timeout])
        return result


class IReusableEvent(IEvent):
    """
    Base abstract interface for all reusable events.
    """
    __uuid__ = '69bfb134-80f6-4266-8e20-16371f68fa25'
    __wsmap__ = 'managed'
    
    @property
    def generation(self):
        """Get int value for 'generation'
        Current generation of event, incremented on reuse.
        """
        ret = self._get_attr("generation")
        return ret

    def reuse(self):
        """Marks an event as reused, increments 'generation', fields shall no
        longer be considered valid.

        """
        self._call("reuse")


class IMachineEvent(IEvent):
    """
    Base abstract interface for all machine events.
    """
    __uuid__ = '92ed7b1a-0d96-40ed-ae46-a564d484325e'
    __wsmap__ = 'managed'
    id = VBoxEventType.machine_event
    @property
    def machine_id(self):
        """Get str value for 'machineId'
        ID of the machine this event relates to.
        """
        ret = self._get_attr("machineId")
        return ret


class IMachineStateChangedEvent(IMachineEvent):
    """
    Machine state change event.
    """
    __uuid__ = '5748F794-48DF-438D-85EB-98FFD70D18C9'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_machine_state_changed
    @property
    def state(self):
        """Get MachineState value for 'state'
        New execution state.
        """
        ret = self._get_attr("state")
        return MachineState(ret)


class IMachineDataChangedEvent(IMachineEvent):
    """
    Any of the settings of the given machine has changed.
    """
    __uuid__ = 'abe94809-2e88-4436-83d7-50f3e64d0503'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_machine_data_changed
    @property
    def temporary(self):
        """Get bool value for 'temporary'
        @c true if the settings change is temporary. All permanent
        settings changes will trigger an event, and only temporary settings
        changes for running VMs will trigger an event. Note: sending events
        for temporary changes is NOT IMPLEMENTED.
        """
        ret = self._get_attr("temporary")
        return ret


class IMediumRegisteredEvent(IEvent):
    """
    The given medium was registered or unregistered
      within this VirtualBox installation.
    """
    __uuid__ = '53fac49a-b7f1-4a5a-a4ef-a11dd9c2a458'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_medium_registered
    @property
    def medium_id(self):
        """Get str value for 'mediumId'
        ID of the medium this event relates to.
        """
        ret = self._get_attr("mediumId")
        return ret

    @property
    def medium_type(self):
        """Get DeviceType value for 'mediumType'
        Type of the medium this event relates to.
        """
        ret = self._get_attr("mediumType")
        return DeviceType(ret)

    @property
    def registered(self):
        """Get bool value for 'registered'
        If @c true, the medium was registered, otherwise it was
        unregistered.
        """
        ret = self._get_attr("registered")
        return ret


class IMachineRegisteredEvent(IMachineEvent):
    """
    The given machine was registered or unregistered
      within this VirtualBox installation.
    """
    __uuid__ = 'c354a762-3ff2-4f2e-8f09-07382ee25088'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_machine_registered
    @property
    def registered(self):
        """Get bool value for 'registered'
        If @c true, the machine was registered, otherwise it was
        unregistered.
        """
        ret = self._get_attr("registered")
        return ret


class ISessionStateChangedEvent(IMachineEvent):
    """
    The state of the session for the given machine was changed.
      <link to="IMachine::sessionState"/>
    """
    __uuid__ = '714a3eef-799a-4489-86cd-fe8e45b2ff8e'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_session_state_changed
    @property
    def state(self):
        """Get SessionState value for 'state'
        New session state.
        """
        ret = self._get_attr("state")
        return SessionState(ret)


class IGuestPropertyChangedEvent(IMachineEvent):
    """
    Notification when a guest property has changed.
    """
    __uuid__ = '3f63597a-26f1-4edb-8dd2-6bddd0912368'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_property_changed
    @property
    def name(self):
        """Get str value for 'name'
        The name of the property that has changed.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def value(self):
        """Get str value for 'value'
        The new property value.
        """
        ret = self._get_attr("value")
        return ret

    @property
    def flags(self):
        """Get str value for 'flags'
        The new property flags.
        """
        ret = self._get_attr("flags")
        return ret


class ISnapshotEvent(IMachineEvent):
    """
    Base interface for all snapshot events.
    """
    __uuid__ = '21637b0e-34b8-42d3-acfb-7e96daf77c22'
    __wsmap__ = 'managed'
    id = VBoxEventType.snapshot_event
    @property
    def snapshot_id(self):
        """Get str value for 'snapshotId'
        ID of the snapshot this event relates to.
        """
        ret = self._get_attr("snapshotId")
        return ret


class ISnapshotTakenEvent(ISnapshotEvent):
    """
    A new snapshot of the machine has been taken.
      <link to="ISnapshot"/>
    """
    __uuid__ = 'd27c0b3d-6038-422c-b45e-6d4a0503d9f1'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_snapshot_taken

class ISnapshotDeletedEvent(ISnapshotEvent):
    """
    Snapshot of the given machine has been deleted.

      
        This notification is delivered after the snapshot
        object has been uninitialized on the server (so that any
        attempt to call its methods will return an error).
      

      <link to="ISnapshot"/>
    """
    __uuid__ = 'c48f3401-4a9e-43f4-b7a7-54bd285e22f4'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_snapshot_deleted

class ISnapshotChangedEvent(ISnapshotEvent):
    """
    Snapshot properties (name and/or description) have been changed.
      <link to="ISnapshot"/>
    """
    __uuid__ = '07541941-8079-447a-a33e-47a69c7980db'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_snapshot_changed

class IMousePointerShapeChangedEvent(IEvent):
    """
    Notification when the guest mouse pointer shape has
      changed. The new shape data is given.
    """
    __uuid__ = 'a6dcf6e8-416b-4181-8c4a-45ec95177aef'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_mouse_pointer_shape_changed
    @property
    def visible(self):
        """Get bool value for 'visible'
        Flag whether the pointer is visible.
        """
        ret = self._get_attr("visible")
        return ret

    @property
    def alpha(self):
        """Get bool value for 'alpha'
        Flag whether the pointer has an alpha channel.
        """
        ret = self._get_attr("alpha")
        return ret

    @property
    def xhot(self):
        """Get int value for 'xhot'
        The pointer hot spot X coordinate.
        """
        ret = self._get_attr("xhot")
        return ret

    @property
    def yhot(self):
        """Get int value for 'yhot'
        The pointer hot spot Y coordinate.
        """
        ret = self._get_attr("yhot")
        return ret

    @property
    def width(self):
        """Get int value for 'width'
        Width of the pointer shape in pixels.
        """
        ret = self._get_attr("width")
        return ret

    @property
    def height(self):
        """Get int value for 'height'
        Height of the pointer shape in pixels.
        """
        ret = self._get_attr("height")
        return ret

    @property
    def shape(self):
        """Get str value for 'shape'
        Shape buffer arrays.

        The @a shape buffer contains a 1-bpp (bits per pixel) AND mask
        followed by a 32-bpp XOR (color) mask.

        For pointers without alpha channel the XOR mask pixels are
        32-bit values: (lsb)BGR0(msb). For pointers with alpha channel
        the XOR mask consists of (lsb)BGRA(msb) 32-bit values.

        An AND mask is used for pointers with alpha channel, so if the
        callback does not support alpha, the pointer could be
        displayed as a normal color pointer.

        The AND mask is a 1-bpp bitmap with byte aligned scanlines. The
        size of the AND mask therefore is cbAnd = (width + 7) / 8 *
          height. The padding bits at the end of each scanline are
        undefined.

        The XOR mask follows the AND mask on the next 4-byte aligned
        offset: uint8_t *pXor = pAnd + (cbAnd + 3) &amp; ~3.
        Bytes in the gap between the AND and the XOR mask are undefined.
        The XOR mask scanlines have no gap between them and the size of
        the XOR mask is: cXor = width * 4 * height.

        
          If @a shape is 0, only the pointer visibility is changed.
        """
        ret = self._get_attr("shape")
        return ret


class IMouseCapabilityChangedEvent(IEvent):
    """
    Notification when the mouse capabilities reported by the
      guest have changed. The new capabilities are passed.
    """
    __uuid__ = 'd633ad48-820c-4207-b46c-6bd3596640d5'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_mouse_capability_changed
    @property
    def supports_absolute(self):
        """Get bool value for 'supportsAbsolute'
        Supports absolute coordinates.
        """
        ret = self._get_attr("supportsAbsolute")
        return ret

    @property
    def supports_relative(self):
        """Get bool value for 'supportsRelative'
        Supports relative coordinates.
        """
        ret = self._get_attr("supportsRelative")
        return ret

    @property
    def needs_host_cursor(self):
        """Get bool value for 'needsHostCursor'
        If host cursor is needed.
        """
        ret = self._get_attr("needsHostCursor")
        return ret


class IKeyboardLedsChangedEvent(IEvent):
    """
    Notification when the guest OS executes the KBD_CMD_SET_LEDS command
      to alter the state of the keyboard LEDs.
    """
    __uuid__ = '6DDEF35E-4737-457B-99FC-BC52C851A44F'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_keyboard_leds_changed
    @property
    def num_lock(self):
        """Get bool value for 'numLock'
        NumLock status.
        """
        ret = self._get_attr("numLock")
        return ret

    @property
    def caps_lock(self):
        """Get bool value for 'capsLock'
        CapsLock status.
        """
        ret = self._get_attr("capsLock")
        return ret

    @property
    def scroll_lock(self):
        """Get bool value for 'scrollLock'
        ScrollLock status.
        """
        ret = self._get_attr("scrollLock")
        return ret


class IStateChangedEvent(IEvent):
    """
    Notification when the execution state of the machine has changed.
      The new state is given.
    """
    __uuid__ = '4376693C-CF37-453B-9289-3B0F521CAF27'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_state_changed
    @property
    def state(self):
        """Get MachineState value for 'state'
        New machine state.
        """
        ret = self._get_attr("state")
        return MachineState(ret)


class IAdditionsStateChangedEvent(IEvent):
    """
    Notification when a Guest Additions property changes.
      Interested callees should query IGuest attributes to
      find out what has changed.
    """
    __uuid__ = 'D70F7915-DA7C-44C8-A7AC-9F173490446A'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_additions_state_changed

class INetworkAdapterChangedEvent(IEvent):
    """
    Notification when a property of one of the
      virtual <link to="IMachine::getNetworkAdapter">network adapters</link>
      changes. Interested callees should use INetworkAdapter methods and
      attributes to find out what has changed.
    """
    __uuid__ = '08889892-1EC6-4883-801D-77F56CFD0103'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_network_adapter_changed
    @property
    def network_adapter(self):
        """Get INetworkAdapter value for 'networkAdapter'
        Network adapter that is subject to change.
        """
        ret = self._get_attr("networkAdapter")
        return INetworkAdapter(ret)


class ISerialPortChangedEvent(IEvent):
    """
    Notification when a property of one of the
      virtual <link to="IMachine::getSerialPort">serial ports</link> changes.
      Interested callees should use ISerialPort methods and attributes
      to find out what has changed.
    """
    __uuid__ = '3BA329DC-659C-488B-835C-4ECA7AE71C6C'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_serial_port_changed
    @property
    def serial_port(self):
        """Get ISerialPort value for 'serialPort'
        Serial port that is subject to change.
        """
        ret = self._get_attr("serialPort")
        return ISerialPort(ret)


class IParallelPortChangedEvent(IEvent):
    """
    Notification when a property of one of the
      virtual <link to="IMachine::getParallelPort">parallel ports</link>
      changes. Interested callees should use ISerialPort methods and
      attributes to find out what has changed.
    """
    __uuid__ = '813C99FC-9849-4F47-813E-24A75DC85615'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_parallel_port_changed
    @property
    def parallel_port(self):
        """Get IParallelPort value for 'parallelPort'
        Parallel port that is subject to change.
        """
        ret = self._get_attr("parallelPort")
        return IParallelPort(ret)


class IStorageControllerChangedEvent(IEvent):
    """
    Notification when a
      <link to="IMachine::mediumAttachments">medium attachment</link>
      changes.
    """
    __uuid__ = '715212BF-DA59-426E-8230-3831FAA52C56'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_storage_controller_changed

class IMediumChangedEvent(IEvent):
    """
    Notification when a
      <link to="IMachine::mediumAttachments">medium attachment</link>
      changes.
    """
    __uuid__ = '0FE2DA40-5637-472A-9736-72019EABD7DE'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_medium_changed
    @property
    def medium_attachment(self):
        """Get IMediumAttachment value for 'mediumAttachment'
        Medium attachment that is subject to change.
        """
        ret = self._get_attr("mediumAttachment")
        return IMediumAttachment(ret)


class IClipboardModeChangedEvent(IEvent):
    """
    Notification when the shared clipboard mode changes.
    """
    __uuid__ = 'cac21692-7997-4595-a731-3a509db604e5'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_clipboard_mode_changed
    @property
    def clipboard_mode(self):
        """Get ClipboardMode value for 'clipboardMode'
        The new clipboard mode.
        """
        ret = self._get_attr("clipboardMode")
        return ClipboardMode(ret)


class IDragAndDropModeChangedEvent(IEvent):
    """
    Notification when the drag'n'drop mode changes.
    """
    __uuid__ = 'e90b8850-ac8e-4dff-8059-4100ae2c3c3d'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_drag_and_drop_mode_changed
    @property
    def drag_and_drop_mode(self):
        """Get DragAndDropMode value for 'dragAndDropMode'
        The new drag'n'drop mode.
        """
        ret = self._get_attr("dragAndDropMode")
        return DragAndDropMode(ret)


class ICPUChangedEvent(IEvent):
    """
    Notification when a CPU changes.
    """
    __uuid__ = '4da2dec7-71b2-4817-9a64-4ed12c17388e'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_cpu_changed
    @property
    def cpu(self):
        """Get int value for 'CPU'
        The CPU which changed.
        """
        ret = self._get_attr("CPU")
        return ret

    @property
    def add(self):
        """Get bool value for 'add'
        Flag whether the CPU was added or removed.
        """
        ret = self._get_attr("add")
        return ret


class ICPUExecutionCapChangedEvent(IEvent):
    """
    Notification when the CPU execution cap changes.
    """
    __uuid__ = 'dfa7e4f5-b4a4-44ce-85a8-127ac5eb59dc'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_cpu_execution_cap_changed
    @property
    def execution_cap(self):
        """Get int value for 'executionCap'
        The new CPU execution cap value. (1-100)
        """
        ret = self._get_attr("executionCap")
        return ret


class IGuestKeyboardEvent(IEvent):
    """
    Notification when guest keyboard event happens.
    """
    __uuid__ = '88394258-7006-40d4-b339-472ee3801844'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_keyboard
    @property
    def scancodes(self):
        """Get int value for 'scancodes'
        Array of scancodes.
        """
        ret = self._get_attr("scancodes")
        return ret


class IGuestMouseEvent(IReusableEvent):
    """
    Notification when guest mouse event happens.
    """
    __uuid__ = '1f85d35c-c524-40ff-8e98-307000df0992'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_mouse
    @property
    def absolute(self):
        """Get bool value for 'absolute'
        If this event is relative or absolute.
        """
        ret = self._get_attr("absolute")
        return ret

    @property
    def x(self):
        """Get int value for 'x'
        New X position, or X delta.
        """
        ret = self._get_attr("x")
        return ret

    @property
    def y(self):
        """Get int value for 'y'
        New Y position, or Y delta.
        """
        ret = self._get_attr("y")
        return ret

    @property
    def z(self):
        """Get int value for 'z'
        Z delta.
        """
        ret = self._get_attr("z")
        return ret

    @property
    def w(self):
        """Get int value for 'w'
        W delta.
        """
        ret = self._get_attr("w")
        return ret

    @property
    def buttons(self):
        """Get int value for 'buttons'
        Button state bitmask.
        """
        ret = self._get_attr("buttons")
        return ret


class IGuestSessionEvent(IEvent):
    """
    Base abstract interface for all guest session events.
    """
    __uuid__ = 'b9acd33f-647d-45ac-8fe9-f49b3183ba37'
    __wsmap__ = 'managed'
    
    @property
    def session(self):
        """Get IGuestSession value for 'session'
        Guest session that is subject to change.
        """
        ret = self._get_attr("session")
        return IGuestSession(ret)


class IGuestSessionStateChangedEvent(IGuestSessionEvent):
    """
    Notification when a guest session changed its state.
    """
    __uuid__ = '327e3c00-ee61-462f-aed3-0dff6cbf9904'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_session_state_changed
    @property
    def id_p(self):
        """Get int value for 'id'
        Session ID of guest session which was changed.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def status(self):
        """Get GuestSessionStatus value for 'status'
        New session status.
        """
        ret = self._get_attr("status")
        return GuestSessionStatus(ret)

    @property
    def error(self):
        """Get IVirtualBoxErrorInfo value for 'error'
        Error information in case of new session status is indicating an error.

        The attribute <link to="IVirtualBoxErrorInfo::resultDetail"/> will contain
        the runtime (IPRT) error code from the guest. See include/iprt/err.h and
        include/VBox/err.h for details.
        """
        ret = self._get_attr("error")
        return IVirtualBoxErrorInfo(ret)


class IGuestSessionRegisteredEvent(IGuestSessionEvent):
    """
    Notification when a guest session was registered or unregistered.
    """
    __uuid__ = 'b79de686-eabd-4fa6-960a-f1756c99ea1c'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_session_registered
    @property
    def registered(self):
        """Get bool value for 'registered'
        If @c true, the guest session was registered, otherwise it was
        unregistered.
        """
        ret = self._get_attr("registered")
        return ret


class IGuestProcessEvent(IGuestSessionEvent):
    """
    Base abstract interface for all guest process events.
    """
    __uuid__ = '2405f0e5-6588-40a3-9b0a-68c05ba52c4b'
    __wsmap__ = 'managed'
    
    @property
    def process(self):
        """Get IGuestProcess value for 'process'
        Guest process object which is related to this event.
        """
        ret = self._get_attr("process")
        return IGuestProcess(ret)

    @property
    def pid(self):
        """Get int value for 'pid'
        Guest process ID (PID).
        """
        ret = self._get_attr("pid")
        return ret


class IGuestProcessRegisteredEvent(IGuestProcessEvent):
    """
    Notification when a guest process was registered or unregistered.
    """
    __uuid__ = '1d89e2b3-c6ea-45b6-9d43-dc6f70cc9f02'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_process_registered
    @property
    def registered(self):
        """Get bool value for 'registered'
        If @c true, the guest process was registered, otherwise it was
        unregistered.
        """
        ret = self._get_attr("registered")
        return ret


class IGuestProcessStateChangedEvent(IGuestProcessEvent):
    """
    Notification when a guest process changed its state.
    """
    __uuid__ = 'c365fb7b-4430-499f-92c8-8bed814a567a'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_process_state_changed
    @property
    def status(self):
        """Get ProcessStatus value for 'status'
        New guest process status.
        """
        ret = self._get_attr("status")
        return ProcessStatus(ret)

    @property
    def error(self):
        """Get IVirtualBoxErrorInfo value for 'error'
        Error information in case of new session status is indicating an error.

        The attribute <link to="IVirtualBoxErrorInfo::resultDetail"/> will contain
        the runtime (IPRT) error code from the guest. See include/iprt/err.h and
        include/VBox/err.h for details.
        """
        ret = self._get_attr("error")
        return IVirtualBoxErrorInfo(ret)


class IGuestProcessIOEvent(IGuestProcessEvent):
    """
    Base abstract interface for all guest process input/output (IO) events.
    """
    __uuid__ = '9ea9227c-e9bb-49b3-bfc7-c5171e93ef38'
    __wsmap__ = 'managed'
    
    @property
    def handle(self):
        """Get int value for 'handle'
        Input/output (IO) handle involved in this event. Usually 0 is stdin,
        1 is stdout and 2 is stderr.
        """
        ret = self._get_attr("handle")
        return ret

    @property
    def processed(self):
        """Get int value for 'processed'
        Processed input or output (in bytes).
        """
        ret = self._get_attr("processed")
        return ret


class IGuestProcessInputNotifyEvent(IGuestProcessIOEvent):
    """
    Notification when a guest process' stdin became available.
      This event is right now not implemented!
    """
    __uuid__ = '0de887f2-b7db-4616-aac6-cfb94d89ba78'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_process_input_notify
    @property
    def status(self):
        """Get ProcessInputStatus value for 'status'
        Current process input status.
        """
        ret = self._get_attr("status")
        return ProcessInputStatus(ret)


class IGuestProcessOutputEvent(IGuestProcessIOEvent):
    """
    Notification when there is guest process output available for reading.
    """
    __uuid__ = 'd3d5f1ee-bcb2-4905-a7ab-cc85448a742b'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_process_output
    @property
    def data(self):
        """Get str value for 'data'
        Actual output data.
        """
        ret = self._get_attr("data")
        return ret


class IGuestFileEvent(IGuestSessionEvent):
    """
    Base abstract interface for all guest file events.
    """
    __uuid__ = 'c8adb7b0-057d-4391-b928-f14b06b710c5'
    __wsmap__ = 'managed'
    
    @property
    def file_p(self):
        """Get IGuestFile value for 'file'
        Guest file object which is related to this event.
        """
        ret = self._get_attr("file")
        return IGuestFile(ret)


class IGuestFileRegisteredEvent(IGuestFileEvent):
    """
    Notification when a guest file was registered or unregistered.
    """
    __uuid__ = 'd0d93830-70a2-487e-895e-d3fc9679f7b3'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_file_registered
    @property
    def registered(self):
        """Get bool value for 'registered'
        If @c true, the guest file was registered, otherwise it was
        unregistered.
        """
        ret = self._get_attr("registered")
        return ret


class IGuestFileStateChangedEvent(IGuestFileEvent):
    """
    Notification when a guest file changed its state.
    """
    __uuid__ = 'd37fe88f-0979-486c-baa1-3abb144dc82d'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_file_state_changed
    @property
    def status(self):
        """Get FileStatus value for 'status'
        New guest file status.
        """
        ret = self._get_attr("status")
        return FileStatus(ret)

    @property
    def error(self):
        """Get IVirtualBoxErrorInfo value for 'error'
        Error information in case of new session status is indicating an error.

        The attribute <link to="IVirtualBoxErrorInfo::resultDetail"/> will contain
        the runtime (IPRT) error code from the guest. See include/iprt/err.h and
        include/VBox/err.h for details.
        """
        ret = self._get_attr("error")
        return IVirtualBoxErrorInfo(ret)


class IGuestFileIOEvent(IGuestFileEvent):
    """
    Base abstract interface for all guest file input/output (IO) events.
    """
    __uuid__ = 'b5191a7c-9536-4ef8-820e-3b0e17e5bbc8'
    __wsmap__ = 'managed'
    
    @property
    def offset(self):
        """Get int value for 'offset'
        Current offset (in bytes).
        """
        ret = self._get_attr("offset")
        return ret

    @property
    def processed(self):
        """Get int value for 'processed'
        Processed input or output (in bytes).
        """
        ret = self._get_attr("processed")
        return ret


class IGuestFileOffsetChangedEvent(IGuestFileIOEvent):
    """
    Notification when a guest file changed its current offset.
    """
    __uuid__ = 'e8f79a21-1207-4179-94cf-ca250036308f'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_file_offset_changed

class IGuestFileReadEvent(IGuestFileIOEvent):
    """
    Notification when data has been read from a guest file.
    """
    __uuid__ = '4ee3cbcb-486f-40db-9150-deee3fd24189'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_file_read
    @property
    def data(self):
        """Get str value for 'data'
        Actual data read.
        """
        ret = self._get_attr("data")
        return ret


class IGuestFileWriteEvent(IGuestFileIOEvent):
    """
    Notification when data has been written to a guest file.
    """
    __uuid__ = 'e062a915-3cf5-4c0a-bc90-9b8d4cc94d89'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_file_write

class IVRDEServerChangedEvent(IEvent):
    """
    Notification when a property of the
      <link to="IMachine::VRDEServer">VRDE server</link> changes.
      Interested callees should use IVRDEServer methods and attributes to
      find out what has changed.
    """
    __uuid__ = 'a06fd66a-3188-4c8c-8756-1395e8cb691c'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_vrde_server_changed

class IVRDEServerInfoChangedEvent(IEvent):
    """
    Notification when the status of the VRDE server changes. Interested callees
      should use <link to="IConsole::VRDEServerInfo">IVRDEServerInfo</link>
      attributes to find out what is the current status.
    """
    __uuid__ = 'dd6a1080-e1b7-4339-a549-f0878115596e'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_vrde_server_info_changed

class IVideoCaptureChangedEvent(IEvent):
    """
    Notification when video capture settings have changed.
    """
    __uuid__ = '6215d169-25dd-4719-ab34-c908701efb58'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_video_capture_changed

class IUSBControllerChangedEvent(IEvent):
    """
    Notification when a property of the virtual
      <link to="IMachine::USBController">USB controller</link> changes.
      Interested callees should use IUSBController methods and attributes to
      find out what has changed.
    """
    __uuid__ = '93BADC0C-61D9-4940-A084-E6BB29AF3D83'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_usb_controller_changed

class IUSBDeviceStateChangedEvent(IEvent):
    """
    Notification when a USB device is attached to or detached from
      the virtual USB controller.

      This notification is sent as a result of the indirect
      request to attach the device because it matches one of the
      machine USB filters, or as a result of the direct request
      issued by <link to="IConsole::attachUSBDevice"/> or
      <link to="IConsole::detachUSBDevice"/>.

      This notification is sent in case of both a succeeded and a
      failed request completion. When the request succeeds, the
      @a error parameter is @c null, and the given device has been
      already added to (when @a attached is @c true) or removed from
      (when @a attached is @c false) the collection represented by
      <link to="IConsole::USBDevices"/>. On failure, the collection
      doesn't change and the @a error parameter represents the error
      message describing the failure.
    """
    __uuid__ = '806da61b-6679-422a-b629-51b06b0c6d93'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_usb_device_state_changed
    @property
    def device(self):
        """Get IUSBDevice value for 'device'
        Device that is subject to state change.
        """
        ret = self._get_attr("device")
        return IUSBDevice(ret)

    @property
    def attached(self):
        """Get bool value for 'attached'
        @c true if the device was attached and @c false otherwise.
        """
        ret = self._get_attr("attached")
        return ret

    @property
    def error(self):
        """Get IVirtualBoxErrorInfo value for 'error'
        @c null on success or an error message object on failure.
        """
        ret = self._get_attr("error")
        return IVirtualBoxErrorInfo(ret)


class ISharedFolderChangedEvent(IEvent):
    """
    Notification when a shared folder is added or removed.
      The @a scope argument defines one of three scopes:
      <link to="IVirtualBox::sharedFolders">global shared folders</link>
      (<link to="Scope_Global">Global</link>),
      <link to="IMachine::sharedFolders">permanent shared folders</link> of
      the machine (<link to="Scope_Machine">Machine</link>) or <link to="IConsole::sharedFolders">transient shared folders</link> of the
      machine (<link to="Scope_Session">Session</link>). Interested callees
      should use query the corresponding collections to find out what has
      changed.
    """
    __uuid__ = 'B66349B5-3534-4239-B2DE-8E1535D94C0B'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_shared_folder_changed
    @property
    def scope(self):
        """Get Scope value for 'scope'
        Scope of the notification.
        """
        ret = self._get_attr("scope")
        return Scope(ret)


class IRuntimeErrorEvent(IEvent):
    """
    Notification when an error happens during the virtual
      machine execution.

      There are three kinds of runtime errors:
      
        fatal
        non-fatal with retry
        non-fatal warnings
      

      Fatal errors are indicated by the @a fatal parameter set
      to @c true. In case of fatal errors, the virtual machine
      execution is always paused before calling this notification, and
      the notification handler is supposed either to immediately save
      the virtual machine state using <link to="IConsole::saveState"/>
      or power it off using <link to="IConsole::powerDown"/>.
      Resuming the execution can lead to unpredictable results.

      Non-fatal errors and warnings are indicated by the
      @a fatal parameter set to @c false. If the virtual machine
      is in the Paused state by the time the error notification is
      received, it means that the user can try to resume the machine
      execution after attempting to solve the problem that caused the
      error. In this case, the notification handler is supposed
      to show an appropriate message to the user (depending on the
      value of the @a id parameter) that offers several actions such
      as Retry, Save or Power Off. If the user
      wants to retry, the notification handler should continue
      the machine execution using the <link to="IConsole::resume"/>
      call. If the machine execution is not Paused during this
      notification, then it means this notification is a warning
      (for example, about a fatal condition that can happen very soon);
      no immediate action is required from the user, the machine
      continues its normal execution.

      Note that in either case the notification handler
      must not perform any action directly on a thread
      where this notification is called. Everything it is allowed to
      do is to post a message to another thread that will then talk
      to the user and take the corresponding action.

      Currently, the following error identifiers are known:
      
        "HostMemoryLow"
        "HostAudioNotResponding"
        "VDIStorageFull"
        "3DSupportIncompatibleAdditions"
    """
    __uuid__ = '883DD18B-0721-4CDE-867C-1A82ABAF914C'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_runtime_error
    @property
    def fatal(self):
        """Get bool value for 'fatal'
        Whether the error is fatal or not.
        """
        ret = self._get_attr("fatal")
        return ret

    @property
    def id_p(self):
        """Get str value for 'id'
        Error identifier.
        """
        ret = self._get_attr("id")
        return ret

    @property
    def message(self):
        """Get str value for 'message'
        Optional error message.
        """
        ret = self._get_attr("message")
        return ret


class IEventSourceChangedEvent(IEvent):
    """
    Notification when an event source state changes (listener added or removed).
    """
    __uuid__ = 'e7932cb8-f6d4-4ab6-9cbf-558eb8959a6a'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_event_source_changed
    @property
    def listener(self):
        """Get IEventListener value for 'listener'
        Event listener which has changed.
        """
        ret = self._get_attr("listener")
        return IEventListener(ret)

    @property
    def add(self):
        """Get bool value for 'add'
        Flag whether listener was added or removed.
        """
        ret = self._get_attr("add")
        return ret


class IExtraDataChangedEvent(IEvent):
    """
    Notification when machine specific or global extra data
      has changed.
    """
    __uuid__ = '024F00CE-6E0B-492A-A8D0-968472A94DC7'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_extra_data_changed
    @property
    def machine_id(self):
        """Get str value for 'machineId'
        ID of the machine this event relates to.
        Null for global extra data changes.
        """
        ret = self._get_attr("machineId")
        return ret

    @property
    def key(self):
        """Get str value for 'key'
        Extra data key that has changed.
        """
        ret = self._get_attr("key")
        return ret

    @property
    def value(self):
        """Get str value for 'value'
        Extra data value for the given key.
        """
        ret = self._get_attr("value")
        return ret


class IVetoEvent(IEvent):
    """
    Base abstract interface for veto events.
    """
    __uuid__ = '9a1a4130-69fe-472f-ac10-c6fa25d75007'
    __wsmap__ = 'managed'
    
    def add_veto(self, reason):
        """Adds a veto on this event.

        in reason of type str
            Reason for veto, could be null or empty string.

        """
        if type(reason) not in [str, unicode]:
            raise TypeError("value is not a str or unicode")
        self._call("addVeto",
                     in_p=[reason])

    def is_vetoed(self):
        """If this event was vetoed.

        return result of type bool
            Reason for veto.

        """
        result = self._call("isVetoed")
        return result

    def get_vetos(self):
        """Current veto reason list, if size is 0 - no veto.

        return result of type str
            Array of reasons for veto provided by different event handlers.

        """
        result = self._call("getVetos")
        return result


class IExtraDataCanChangeEvent(IVetoEvent):
    """
    Notification when someone tries to change extra data for
      either the given machine or (if @c null) global extra data.
      This gives the chance to veto against changes.
    """
    __uuid__ = '245d88bd-800a-40f8-87a6-170d02249a55'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_extra_data_can_change
    @property
    def machine_id(self):
        """Get str value for 'machineId'
        ID of the machine this event relates to.
        Null for global extra data changes.
        """
        ret = self._get_attr("machineId")
        return ret

    @property
    def key(self):
        """Get str value for 'key'
        Extra data key that has changed.
        """
        ret = self._get_attr("key")
        return ret

    @property
    def value(self):
        """Get str value for 'value'
        Extra data value for the given key.
        """
        ret = self._get_attr("value")
        return ret


class ICanShowWindowEvent(IVetoEvent):
    """
    Notification when a call to
      <link to="IMachine::canShowConsoleWindow"/> is made by a
      front-end to check if a subsequent call to
      <link to="IMachine::showConsoleWindow"/> can succeed.

      The callee should give an answer appropriate to the current
      machine state using event veto. This answer must
      remain valid at least until the next
      <link to="IConsole::state">machine state</link> change.
    """
    __uuid__ = 'adf292b0-92c9-4a77-9d35-e058b39fe0b9'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_can_show_window

class IShowWindowEvent(IEvent):
    """
    Notification when a call to
      <link to="IMachine::showConsoleWindow"/>
      requests the console window to be activated and brought to
      foreground on the desktop of the host PC.

      This notification should cause the VM console process to
      perform the requested action as described above. If it is
      impossible to do it at a time of this notification, this
      method should return a failure.

      Note that many modern window managers on many platforms
      implement some sort of focus stealing prevention logic, so
      that it may be impossible to activate a window without the
      help of the currently active application (which is supposedly
      an initiator of this notification). In this case, this method
      must return a non-zero identifier that represents the
      top-level window of the VM console process. The caller, if it
      represents a currently active process, is responsible to use
      this identifier (in a platform-dependent manner) to perform
      actual window activation.

      This method must set @a winId to zero if it has performed all
      actions necessary to complete the request and the console
      window is now active and in foreground, to indicate that no
      further action is required on the caller's side.
    """
    __uuid__ = 'B0A0904D-2F05-4D28-855F-488F96BAD2B2'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_show_window
    @property
    def win_id(self):
        """Get or set int value for 'winId'
        Platform-dependent identifier of the top-level VM console
        window, or zero if this method has performed all actions
        necessary to implement the show window semantics for
        the given platform and/or this VirtualBox front-end.
        """
        ret = self._get_attr("winId")
        return ret

    @win_id.setter
    def win_id(self, value):
        if not isinstance(value, int):
            raise TypeError("value is not an instance of int")
        return self._set_attr("winId", value)


class INATRedirectEvent(IMachineEvent):
    """
    Notification when NAT redirect rule added or removed.
    """
    __uuid__ = '24eef068-c380-4510-bc7c-19314a7352f1'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_nat_redirect
    @property
    def slot(self):
        """Get int value for 'slot'
        Adapter which NAT attached to.
        """
        ret = self._get_attr("slot")
        return ret

    @property
    def remove(self):
        """Get bool value for 'remove'
        Whether rule remove or add.
        """
        ret = self._get_attr("remove")
        return ret

    @property
    def name(self):
        """Get str value for 'name'
        Name of the rule.
        """
        ret = self._get_attr("name")
        return ret

    @property
    def proto(self):
        """Get NATProtocol value for 'proto'
        Protocol (TCP or UDP) of the redirect rule.
        """
        ret = self._get_attr("proto")
        return NATProtocol(ret)

    @property
    def host_ip(self):
        """Get str value for 'hostIP'
        Host ip address to bind socket on.
        """
        ret = self._get_attr("hostIP")
        return ret

    @property
    def host_port(self):
        """Get int value for 'hostPort'
        Host port to bind socket on.
        """
        ret = self._get_attr("hostPort")
        return ret

    @property
    def guest_ip(self):
        """Get str value for 'guestIP'
        Guest ip address to redirect to.
        """
        ret = self._get_attr("guestIP")
        return ret

    @property
    def guest_port(self):
        """Get int value for 'guestPort'
        Guest port to redirect to.
        """
        ret = self._get_attr("guestPort")
        return ret


class IHostPCIDevicePlugEvent(IMachineEvent):
    """
    Notification when host PCI device is plugged/unplugged. Plugging
      usually takes place on VM startup, unplug - when
      <link to="IMachine::detachHostPCIDevice"/> is called.

      <link to="IMachine::detachHostPCIDevice"/>
    """
    __uuid__ = 'a0bad6df-d612-47d3-89d4-db3992533948'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_host_pci_device_plug
    @property
    def plugged(self):
        """Get bool value for 'plugged'
        If device successfully plugged or unplugged.
        """
        ret = self._get_attr("plugged")
        return ret

    @property
    def success(self):
        """Get bool value for 'success'
        If operation was successful, if false - 'message' attribute
        may be of interest.
        """
        ret = self._get_attr("success")
        return ret

    @property
    def attachment(self):
        """Get IPCIDeviceAttachment value for 'attachment'
        Attachment info for this device.
        """
        ret = self._get_attr("attachment")
        return IPCIDeviceAttachment(ret)

    @property
    def message(self):
        """Get str value for 'message'
        Optional error message.
        """
        ret = self._get_attr("message")
        return ret


class IVBoxSVCAvailabilityChangedEvent(IEvent):
    """
    Notification when VBoxSVC becomes unavailable (due to a crash or similar
      unexpected circumstances) or available again.
    """
    __uuid__ = '97c78fcd-d4fc-485f-8613-5af88bfcfcdc'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_v_box_svc_availability_changed
    @property
    def available(self):
        """Get bool value for 'available'
        Whether VBoxSVC is available now.
        """
        ret = self._get_attr("available")
        return ret


class IBandwidthGroupChangedEvent(IEvent):
    """
    Notification when one of the bandwidth groups changed
    """
    __uuid__ = '334df94a-7556-4cbc-8c04-043096b02d82'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_bandwidth_group_changed
    @property
    def bandwidth_group(self):
        """Get IBandwidthGroup value for 'bandwidthGroup'
        The changed bandwidth group.
        """
        ret = self._get_attr("bandwidthGroup")
        return IBandwidthGroup(ret)


class IGuestMonitorChangedEvent(IEvent):
    """
    Notification when the guest enables one of its monitors.
    """
    __uuid__ = '0f7b8a22-c71f-4a36-8e5f-a77d01d76090'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_guest_monitor_changed
    @property
    def change_type(self):
        """Get GuestMonitorChangedEventType value for 'changeType'
        What was changed for this guest monitor.
        """
        ret = self._get_attr("changeType")
        return GuestMonitorChangedEventType(ret)

    @property
    def screen_id(self):
        """Get int value for 'screenId'
        The monitor which was changed.
        """
        ret = self._get_attr("screenId")
        return ret

    @property
    def origin_x(self):
        """Get int value for 'originX'
        Physical X origin relative to the primary screen.
        Valid for Enabled and NewOrigin.
        """
        ret = self._get_attr("originX")
        return ret

    @property
    def origin_y(self):
        """Get int value for 'originY'
        Physical Y origin relative to the primary screen.
        Valid for Enabled and NewOrigin.
        """
        ret = self._get_attr("originY")
        return ret

    @property
    def width(self):
        """Get int value for 'width'
        Width of the screen.
        Valid for Enabled.
        """
        ret = self._get_attr("width")
        return ret

    @property
    def height(self):
        """Get int value for 'height'
        Height of the screen.
        Valid for Enabled.
        """
        ret = self._get_attr("height")
        return ret


class IStorageDeviceChangedEvent(IEvent):
    """
    Notification when a
      <link to="IMachine::mediumAttachments">storage device</link>
      is attached or removed.
    """
    __uuid__ = '232e9151-ae84-4b8e-b0f3-5c20c35caac9'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_storage_device_changed
    @property
    def storage_device(self):
        """Get IMediumAttachment value for 'storageDevice'
        Storage device that is subject to change.
        """
        ret = self._get_attr("storageDevice")
        return IMediumAttachment(ret)

    @property
    def removed(self):
        """Get bool value for 'removed'
        Flag whether the device was removed or added to the VM.
        """
        ret = self._get_attr("removed")
        return ret

    @property
    def silent(self):
        """Get bool value for 'silent'
        Flag whether the guest should be notified about the change.
        """
        ret = self._get_attr("silent")
        return ret


class INATNetworkChangedEvent(IEvent):
    """"""
    __uuid__ = '101ae042-1a29-4a19-92cf-02285773f3b5'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_nat_network_changed
    @property
    def network_name(self):
        """Get str value for 'networkName'"""
        ret = self._get_attr("networkName")
        return ret


class INATNetworkStartStopEvent(INATNetworkChangedEvent):
    """
    IsStartEvent is true when NAT network is started and false on stopping.
    """
    __uuid__ = '269d8f6b-fa1e-4cee-91c7-6d8496bea3c1'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_nat_network_start_stop
    @property
    def start_event(self):
        """Get bool value for 'startEvent'
        IsStartEvent is true when NAT network is started and false on stopping.
        """
        ret = self._get_attr("startEvent")
        return ret


class INATNetworkAlterEvent(INATNetworkChangedEvent):
    """"""
    __uuid__ = '3f5a0822-163a-43b1-ad16-8d58b0ef6e75'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_nat_network_alter

class INATNetworkCreationDeletionEvent(INATNetworkAlterEvent):
    """"""
    __uuid__ = '8d984a7e-b855-40b8-ab0c-44d3515b4528'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_nat_network_creation_deletion
    @property
    def creation_event(self):
        """Get bool value for 'creationEvent'"""
        ret = self._get_attr("creationEvent")
        return ret


class INATNetworkSettingEvent(INATNetworkAlterEvent):
    """"""
    __uuid__ = '9db3a9e6-7f29-4aae-a627-5a282c83092c'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_nat_network_setting
    @property
    def enabled(self):
        """Get bool value for 'enabled'"""
        ret = self._get_attr("enabled")
        return ret

    @property
    def network(self):
        """Get str value for 'network'"""
        ret = self._get_attr("network")
        return ret

    @property
    def gateway(self):
        """Get str value for 'gateway'"""
        ret = self._get_attr("gateway")
        return ret

    @property
    def advertise_default_i_pv6_route_enabled(self):
        """Get bool value for 'advertiseDefaultIPv6RouteEnabled'"""
        ret = self._get_attr("advertiseDefaultIPv6RouteEnabled")
        return ret

    @property
    def need_dhcp_server(self):
        """Get bool value for 'needDhcpServer'"""
        ret = self._get_attr("needDhcpServer")
        return ret


class INATNetworkPortForwardEvent(INATNetworkAlterEvent):
    """"""
    __uuid__ = '2514881b-23d0-430a-a7ff-7ed7f05534bc'
    __wsmap__ = 'managed'
    id = VBoxEventType.on_nat_network_port_forward
    @property
    def create(self):
        """Get bool value for 'create'"""
        ret = self._get_attr("create")
        return ret

    @property
    def ipv6(self):
        """Get bool value for 'ipv6'"""
        ret = self._get_attr("ipv6")
        return ret

    @property
    def name(self):
        """Get str value for 'name'"""
        ret = self._get_attr("name")
        return ret

    @property
    def proto(self):
        """Get NATProtocol value for 'proto'"""
        ret = self._get_attr("proto")
        return NATProtocol(ret)

    @property
    def host_ip(self):
        """Get str value for 'hostIp'"""
        ret = self._get_attr("hostIp")
        return ret

    @property
    def host_port(self):
        """Get int value for 'hostPort'"""
        ret = self._get_attr("hostPort")
        return ret

    @property
    def guest_ip(self):
        """Get str value for 'guestIp'"""
        ret = self._get_attr("guestIp")
        return ret

    @property
    def guest_port(self):
        """Get int value for 'guestPort'"""
        ret = self._get_attr("guestPort")
        return ret

