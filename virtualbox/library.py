#
#
#
#
#
 
V
i
r
t
a
l
B
o
x
 
a
p
i
 
#
#
#
#
 


#


#


#
 
 
 
 
B
y
 
M
i
c
h
a
e
l
 
D
o
r
m
a
n


#


i
m
p
o
r
t
 
s
y
s


i
m
p
o
r
t
 
r
e


t
r
y
:


 
 
 
 
i
m
p
o
r
t
 
_
_
b
u
i
l
t
i
n
_
_
 
a
s
 
b
u
i
l
t
i
n
 


e
x
c
e
p
t
:


 
 
 
 
i
m
p
o
r
t
 
b
u
i
l
t
i
n






l
i
b
_
v
e
r
s
i
o
n
 
=
 
1
.
3


l
i
b
_
a
p
p
_
u
u
i
d
 
=
 
'
8
1
9
B
4
D
8
5
-
9
C
E
E
-
4
9
3
C
-
B
6
F
C
-
6
4
F
F
E
7
5
9
B
3
C
9
'


l
i
b
_
u
u
i
d
 
=
 
'
d
7
5
6
9
3
5
1
-
1
7
5
0
-
4
6
f
0
-
9
3
6
e
-
b
d
1
2
7
d
5
b
c
2
6
4
'


x
i
d
l
_
h
a
s
h
 
=
 
'
7
0
f
8
7
5
3
a
7
1
1
4
e
2
9
2
a
8
9
e
e
3
0
9
f
d
2
a
4
f
7
7
'






d
e
f
 
p
y
t
h
o
n
i
c
_
n
a
m
e
(
n
a
m
e
)
:


 
 
 
 
s
1
 
=
 
r
e
.
s
u
b
(
'
(
.
)
(
[
A
-
Z
]
[
a
-
z
]
+
)
'
,
 
r
'
\
1
_
\
2
'
,
 
n
a
m
e
)


 
 
 
 
n
a
m
e
 
=
 
r
e
.
s
u
b
(
'
(
[
a
-
z
0
-
9
]
)
(
[
A
-
Z
]
)
'
,
 
r
'
\
1
_
\
2
'
,
 
s
1
)
.
l
o
w
e
r
(
)


 
 
 
 
i
f
 
h
a
s
a
t
t
r
(
b
u
i
l
t
i
n
,
 
n
a
m
e
)
 
i
s
 
T
r
u
e
 
o
r
 
n
a
m
e
 
i
n
 
[
'
g
l
o
b
a
l
'
]
:


 
 
 
 
 
 
 
 
n
a
m
e
 
+
=
 
"
_
p
"


 
 
 
 
r
e
t
u
r
n
 
n
a
m
e






c
l
a
s
s
 
E
n
u
m
T
y
p
e
(
t
y
p
e
)
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
c
l
s
,
 
n
a
m
e
,
 
b
a
s
e
s
,
 
d
c
t
)
:


 
 
 
 
 
 
 
 
c
l
s
.
v
a
l
u
e
 
=
 
N
o
n
e


 
 
 
 
 
 
 
 
c
l
s
.
l
o
o
k
u
p
_
l
a
b
e
l
 
=
 
{
v
:
k
 
f
o
r
 
k
,
 
v
 
i
n
 
c
l
s
.
l
o
o
k
u
p
_
v
a
l
u
e
.
i
t
e
m
s
(
)
}


 
 
 
 
 
 
 
 
f
o
r
 
n
a
m
e
,
 
v
 
i
n
 
c
l
s
.
l
o
o
k
u
p
_
v
a
l
u
e
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
 
 
 
 
s
e
t
a
t
t
r
(
c
l
s
,
 
p
y
t
h
o
n
i
c
_
n
a
m
e
(
n
a
m
e
)
,
 
c
l
s
(
v
)
)




 
 
 
 
d
e
f
 
_
_
g
e
t
i
t
e
m
_
_
(
c
l
s
,
 
k
)
:


 
 
 
 
 
 
 
 
i
f
 
n
o
t
 
h
a
s
a
t
t
r
(
c
l
s
,
 
k
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
K
e
y
E
r
r
o
r
(
"
%
s
 
h
a
s
 
n
o
 
k
e
y
 
%
s
"
 
%
 
c
l
s
.
_
_
n
a
m
e
_
_
,
 
k
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
g
e
t
a
t
t
r
(
c
l
s
,
 
k
)




 
 
 
 
d
e
f
 
_
_
g
e
t
a
t
t
r
i
b
u
t
e
_
_
(
c
l
s
,
 
k
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
t
y
p
e
.
_
_
g
e
t
a
t
t
r
i
b
u
t
e
_
_
(
c
l
s
,
 
k
)






c
l
a
s
s
 
E
n
u
m
(
o
b
j
e
c
t
)
:


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
}


 
 
 
 
_
_
m
e
t
a
c
l
a
s
s
_
_
 
=
 
E
n
u
m
T
y
p
e


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
v
a
l
u
e
=
N
o
n
e
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
v
a
l
u
e
 
=
 
v
a
l
u
e




 
 
 
 
d
e
f
 
_
_
s
t
r
_
_
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
l
o
o
k
u
p
_
l
a
b
e
l
[
s
e
l
f
.
v
a
l
u
e
]




 
 
 
 
d
e
f
 
_
_
i
n
t
_
_
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
v
a
l
u
e




 
 
 
 
d
e
f
 
_
_
r
e
p
r
_
_
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
%
s
(
%
s
)
"
 
%
 
(
s
e
l
f
.
_
_
c
l
a
s
s
_
_
.
_
_
n
a
m
e
_
_
,
 
s
e
l
f
.
v
a
l
u
e
)




 
 
 
 
d
e
f
 
_
_
e
q
_
_
(
s
e
l
f
,
 
k
)
:


 
 
 
 
 
 
 
 
i
f
 
i
s
i
n
s
t
a
n
c
e
(
k
,
 
s
e
l
f
.
_
_
c
l
a
s
s
_
_
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
k
.
v
a
l
u
e
 
=
=
 
s
e
l
f
.
v
a
l
u
e


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e




 
 
 
 
d
e
f
 
_
_
g
e
t
i
t
e
m
_
_
(
s
e
l
f
,
 
k
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
_
_
c
l
a
s
s
_
_
[
k
]






c
l
a
s
s
 
I
n
t
e
r
f
a
c
e
(
o
b
j
e
c
t
)
:




 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
i
n
t
e
r
f
a
c
e
=
N
o
n
e
)
:


 
 
 
 
 
 
 
 
i
f
 
i
n
t
e
r
f
a
c
e
 
i
s
 
N
o
n
e
:


 
 
 
 
 
 
 
 
 
 
 
 
#
T
O
D
O
 
:
 


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
_
i
 
=
 
i
n
t
e
r
f
a
c
e


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
s
e
l
f
.
_
i
 
=
 
i
n
t
e
r
f
a
c
e




 
 
 
 
d
e
f
 
_
c
h
a
n
g
e
_
t
o
_
r
e
a
l
t
y
p
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
i
f
 
i
s
i
n
s
t
a
n
c
e
(
v
a
l
u
e
,
 
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
.
_
i


 
 
 
 
 
 
 
 
e
l
i
f
 
i
s
i
n
s
t
a
n
c
e
(
v
a
l
u
e
,
 
E
n
u
m
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
v
a
l
u
e
)


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e




 
 
 
 
d
e
f
 
s
e
t
_
a
t
t
r
(
s
e
l
f
,
 
n
a
m
e
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
s
e
t
a
t
t
r
(
s
e
l
f
.
_
i
,
 
n
a
m
e
,
 
s
e
l
f
.
_
c
h
a
n
g
e
_
t
o
_
r
e
a
l
t
y
p
e
(
v
a
l
u
e
)
)




 
 
 
 
d
e
f
 
g
e
t
_
a
t
t
r
(
s
e
l
f
,
 
n
a
m
e
,
 
a
t
y
p
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
t
y
p
e
(
g
e
t
a
t
t
r
(
s
e
l
f
.
_
i
,
 
n
a
m
e
)
)




 
 
 
 
d
e
f
 
c
a
l
l
_
m
e
t
h
o
d
(
s
e
l
f
,
 
n
a
m
e
,
 
i
n
_
p
=
[
]
,
 
o
u
t
_
p
=
{
}
,
 
r
e
t
t
y
p
e
=
N
o
n
e
)
:


 
 
 
 
 
 
 
 
g
l
o
b
a
l
 
v
b
o
x
_
e
r
r
o
r


 
 
 
 
 
 
 
 
m
 
=
 
g
e
t
a
t
t
r
(
s
e
l
f
.
_
i
,
 
n
a
m
e
)


 
 
 
 
 
 
 
 
i
n
_
p
a
r
a
m
s
 
=
 
[
s
e
l
f
.
_
c
h
a
n
g
e
_
t
o
_
r
e
a
l
t
y
p
e
(
p
)
 
f
o
r
 
p
 
i
n
 
i
n
_
p
]


 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
 
=
 
m
(
*
i
n
_
p
a
r
a
m
s
)


 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
E
x
c
e
p
t
i
o
n
 
a
s
 
e
x
c
:


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
h
a
s
a
t
t
r
(
e
x
c
,
 
'
e
r
r
n
o
'
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
r
r
n
o
 
=
 
e
x
c
.
e
r
r
n
o
 
&
 
0
x
F
F
F
F
F
F
F
F


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
r
r
c
l
a
s
s
 
=
 
v
b
o
x
_
e
r
r
o
r
.
g
e
t
(
e
r
r
n
o
,
 
V
B
o
x
E
r
r
o
r
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
r
r
o
b
j
 
=
 
e
r
r
c
l
a
s
s
(
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
r
r
o
b
j
.
v
a
l
u
e
 
=
 
e
r
r
n
o


 
 
 
 
 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
r
r
o
b
j
 
=
 
V
B
o
x
E
r
r
o
r
(
)


 
 
 
 
 
 
 
 
 
 
 
 
e
r
r
o
b
j
.
m
s
g
 
=
 
g
e
t
a
t
t
r
(
e
x
c
,
 
'
m
s
g
'
,
 
e
x
c
.
m
e
s
s
a
g
e
)


 
 
 
 
 
 
 
 
 
 
 
 
r
a
i
s
e
 
e
r
r
o
b
j


 
 
 
 
 
 
 
 
i
f
 
r
e
t
t
y
p
e
 
i
s
 
n
o
t
 
N
o
n
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
t
t
y
p
e
(
r
e
t
)






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
(
E
x
c
e
p
t
i
o
n
)
:
 


 
 
 
 
"
"
"
G
e
n
e
r
i
c
 
V
B
o
x
E
r
r
o
r
"
"
"


 
 
 
 
n
a
m
e
 
=
 
"
u
n
d
e
f
"


 
 
 
 
v
a
l
u
e
 
=
 
-
1


 
 
 
 
m
s
g
 
=
 
"
"


 
 
 
 
d
e
f
 
_
_
s
t
r
_
_
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
0
x
%
x
 
(
%
s
)
"
 
%
 
(
s
e
l
f
.
v
a
l
u
e
,
 
s
e
l
f
.
m
s
g
)






#
c
o
n
t
a
i
n
e
r
 
l
o
o
k
u
p
 
f
o
r
 
t
h
e
 
d
i
f
f
e
r
e
n
t
 
e
r
r
o
r
 
t
y
p
e
s


v
b
o
x
_
e
r
r
o
r
 
=
 
{
}






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
O
b
j
e
c
t
N
o
t
F
o
u
n
d
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
O
b
j
e
c
t
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
s
u
p
p
l
i
e
d
 
a
r
g
u
m
e
n
t
s
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
1


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
1
]
 
=
 
V
B
o
x
E
r
r
o
r
O
b
j
e
c
t
N
o
t
F
o
u
n
d






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
I
n
v
a
l
i
d
V
m
S
t
a
t
e
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
C
u
r
r
e
n
t
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
p
r
e
v
e
n
t
s
 
t
h
e
 
o
p
e
r
a
t
i
o
n
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
2


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
2
]
 
=
 
V
B
o
x
E
r
r
o
r
I
n
v
a
l
i
d
V
m
S
t
a
t
e






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
V
m
E
r
r
o
r
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
r
r
o
r
 
o
c
c
u
r
r
e
d
 
a
t
t
e
m
p
t
i
n
g
 
t
h
e
 
o
p
e
r
a
t
i
o
n
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
V
M
_
E
R
R
O
R
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
3


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
3
]
 
=
 
V
B
o
x
E
r
r
o
r
V
m
E
r
r
o
r






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
F
i
l
e
E
r
r
o
r
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
F
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
 
o
r
 
e
r
r
o
n
e
o
u
s
 
f
i
l
e
 
c
o
n
t
e
n
t
s
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
4


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
4
]
 
=
 
V
B
o
x
E
r
r
o
r
F
i
l
e
E
r
r
o
r






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
I
p
r
t
E
r
r
o
r
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
R
u
n
t
i
m
e
 
s
u
b
s
y
s
t
e
m
 
e
r
r
o
r
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
I
P
R
T
_
E
R
R
O
R
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
5


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
5
]
 
=
 
V
B
o
x
E
r
r
o
r
I
p
r
t
E
r
r
o
r






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
P
d
m
E
r
r
o
r
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
P
l
u
g
g
a
b
l
e
 
D
e
v
i
c
e
 
M
a
n
a
g
e
r
 
e
r
r
o
r
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
6


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
6
]
 
=
 
V
B
o
x
E
r
r
o
r
P
d
m
E
r
r
o
r






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
I
n
v
a
l
i
d
O
b
j
e
c
t
S
t
a
t
e
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
C
u
r
r
e
n
t
 
o
b
j
e
c
t
 
s
t
a
t
e
 
p
r
o
h
i
b
i
t
s
 
o
p
e
r
a
t
i
o
n
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
7


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
7
]
 
=
 
V
B
o
x
E
r
r
o
r
I
n
v
a
l
i
d
O
b
j
e
c
t
S
t
a
t
e






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
H
o
s
t
E
r
r
o
r
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
H
o
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
 
r
e
l
a
t
e
d
 
e
r
r
o
r
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
H
O
S
T
_
E
R
R
O
R
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
8


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
8
]
 
=
 
V
B
o
x
E
r
r
o
r
H
o
s
t
E
r
r
o
r






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
N
o
t
S
u
p
p
o
r
t
e
d
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
R
e
q
u
e
s
t
e
d
 
o
p
e
r
a
t
i
o
n
 
i
s
 
n
o
t
 
s
u
p
p
o
r
t
e
d
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
N
O
T
_
S
U
P
P
O
R
T
E
D
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
9


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
9
]
 
=
 
V
B
o
x
E
r
r
o
r
N
o
t
S
u
p
p
o
r
t
e
d






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
X
m
l
E
r
r
o
r
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
I
n
v
a
l
i
d
 
X
M
L
 
f
o
u
n
d
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
A


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
A
]
 
=
 
V
B
o
x
E
r
r
o
r
X
m
l
E
r
r
o
r






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
I
n
v
a
l
i
d
S
e
s
s
i
o
n
S
t
a
t
e
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
C
u
r
r
e
n
t
 
s
e
s
s
i
o
n
 
s
t
a
t
e
 
p
r
o
h
i
b
i
t
s
 
o
p
e
r
a
t
i
o
n
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
S
E
S
S
I
O
N
_
S
T
A
T
E
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
B


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
B
]
 
=
 
V
B
o
x
E
r
r
o
r
I
n
v
a
l
i
d
S
e
s
s
i
o
n
S
t
a
t
e






c
l
a
s
s
 
V
B
o
x
E
r
r
o
r
O
b
j
e
c
t
I
n
U
s
e
(
V
B
o
x
E
r
r
o
r
)
:


 
 
 
 
r
"
"
"
O
b
j
e
c
t
 
b
e
i
n
g
 
i
n
 
u
s
e
 
p
r
o
h
i
b
i
t
s
 
o
p
e
r
a
t
i
o
n
.
"
"
"


 
 
 
 
n
a
m
e
 
=
 
'
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E
'


 
 
 
 
v
a
l
u
e
 
=
 
0
x
8
0
B
B
0
0
0
C


v
b
o
x
_
e
r
r
o
r
[
0
x
8
0
B
B
0
0
0
C
]
 
=
 
V
B
o
x
E
r
r
o
r
O
b
j
e
c
t
I
n
U
s
e






c
l
a
s
s
 
S
e
t
t
i
n
g
s
V
e
r
s
i
o
n
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
S
e
t
t
i
n
g
s
 
v
e
r
s
i
o
n
 
o
f
 
V
i
r
t
u
a
l
B
o
x
 
s
e
t
t
i
n
g
s
 
f
i
l
e
s
.
 
T
h
i
s
 
i
s
 
w
r
i
t
t
e
n
 
t
o


 
 
 
 
 
 
t
h
e
 
"
v
e
r
s
i
o
n
"
 
a
t
t
r
i
b
u
t
e
 
o
f
 
t
h
e
 
r
o
o
t
 
"
V
i
r
t
u
a
l
B
o
x
"
 
e
l
e
m
e
n
t
 
i
n
 
t
h
e
 
s
e
t
t
i
n
g
s


 
 
 
 
 
 
f
i
l
e
 
X
M
L
 
a
n
d
 
i
n
d
i
c
a
t
e
s
 
w
h
i
c
h
 
V
i
r
t
u
a
l
B
o
x
 
v
e
r
s
i
o
n
 
w
r
o
t
e
 
t
h
e
 
f
i
l
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
d
5
b
1
5
c
a
7
-
3
d
e
7
-
4
6
b
2
-
a
6
3
a
-
d
d
c
c
e
4
2
b
f
a
3
f
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
F
u
t
u
r
e
'
:
 
9
9
9
9
9
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
v
1
_
0
'
:
 
1
,


 
 
 
 
 
 
 
 
'
v
1
_
1
'
:
 
2
,


 
 
 
 
 
 
 
 
'
v
1
_
1
0
'
:
 
1
2
,


 
 
 
 
 
 
 
 
'
v
1
_
1
1
'
:
 
1
3
,


 
 
 
 
 
 
 
 
'
v
1
_
1
2
'
:
 
1
4
,


 
 
 
 
 
 
 
 
'
v
1
_
1
3
'
:
 
1
5
,


 
 
 
 
 
 
 
 
'
v
1
_
1
4
'
:
 
1
6
,


 
 
 
 
 
 
 
 
'
v
1
_
2
'
:
 
3
,


 
 
 
 
 
 
 
 
'
v
1
_
3
'
:
 
5
,


 
 
 
 
 
 
 
 
'
v
1
_
3
p
r
e
'
:
 
4
,


 
 
 
 
 
 
 
 
'
v
1
_
4
'
:
 
6
,


 
 
 
 
 
 
 
 
'
v
1
_
5
'
:
 
7
,


 
 
 
 
 
 
 
 
'
v
1
_
6
'
:
 
8
,


 
 
 
 
 
 
 
 
'
v
1
_
7
'
:
 
9
,


 
 
 
 
 
 
 
 
'
v
1
_
8
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
v
1
_
9
'
:
 
1
1
}
 






c
l
a
s
s
 
A
c
c
e
s
s
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
A
c
c
e
s
s
 
m
o
d
e
 
f
o
r
 
o
p
e
n
i
n
g
 
f
i
l
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
1
d
a
0
0
0
7
c
-
d
d
f
7
-
4
b
e
8
-
b
c
a
c
-
d
8
4
a
1
5
5
8
7
8
5
f
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
R
e
a
d
O
n
l
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
R
e
a
d
W
r
i
t
e
'
:
 
2
}
 






c
l
a
s
s
 
M
a
c
h
i
n
e
S
t
a
t
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
.




 
 
 
 
 
 
T
h
i
s
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
p
o
s
s
i
b
l
e
 
v
a
l
u
e
s
 
o
f
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
t
a
t
e
"
/
>
 
a
t
t
r
i
b
u
t
e
.




 
 
 
 
 
 
B
e
l
o
w
 
i
s
 
t
h
e
 
b
a
s
i
c
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
d
i
a
g
r
a
m
.
 
I
t
 
s
h
o
w
s
 
h
o
w
 
t
h
e
 
s
t
a
t
e


 
 
 
 
 
 
c
h
a
n
g
e
s
 
d
u
r
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
.
 
T
h
e
 
t
e
x
t
 
i
n
 
s
q
u
a
r
e
 
b
r
a
c
e
s
 
s
h
o
w
s


 
 
 
 
 
 
a
 
m
e
t
h
o
d
 
o
f
 
t
h
e
 
I
C
o
n
s
o
l
e
 
i
n
t
e
r
f
a
c
e
 
t
h
a
t
 
p
e
r
f
o
r
m
s
 
t
h
e
 
g
i
v
e
n
 
s
t
a
t
e


 
 
 
 
 
 
t
r
a
n
s
i
t
i
o
n
.




 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
+
-
-
-
-
-
-
-
-
-
[
p
o
w
e
r
D
o
w
n
(
)
]
 
<
-
 
S
t
u
c
k
 
<
-
-
[
f
a
i
l
u
r
e
]
-
+


 
 
 
 
 
 
 
 
 
 
 
 
V
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
+
-
>
 
P
o
w
e
r
e
d
O
f
f
 
-
-
+
-
-
>
[
p
o
w
e
r
U
p
(
)
]
-
-
>
 
S
t
a
r
t
i
n
g
 
-
-
+
 
 
 
 
 
 
|
 
+
-
-
-
-
-
[
r
e
s
u
m
e
(
)
]
-
-
-
-
-
+


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
 
 
 
|
 
V
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
 
 
 
A
b
o
r
t
e
d
 
-
-
-
-
-
+
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
+
-
-
>
 
R
u
n
n
i
n
g
 
-
-
[
p
a
u
s
e
(
)
]
-
-
>
 
P
a
u
s
e
d


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
 
 
 
^
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
^
 
|


 
 
 
 
|
 
 
 
S
a
v
e
d
 
-
-
-
-
-
-
-
-
-
-
-
[
p
o
w
e
r
U
p
(
)
]
-
-
>
 
R
e
s
t
o
r
i
n
g
 
-
+
 
 
 
 
 
 
|
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
|


 
 
 
 
|
 
 
 
 
 
^
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
|


 
 
 
 
|
 
 
 
 
 
|
 
 
 
 
 
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+
-
|
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+
 
+


 
 
 
 
|
 
 
 
 
 
|
 
 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
 
 
 
 
 
|
 
 
 
 
 
+
-
-
 
S
a
v
i
n
g
 
<
-
-
-
-
-
-
-
-
[
t
a
k
e
S
n
a
p
s
h
o
t
(
)
]
<
-
-
-
-
-
-
-
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+


 
 
 
 
|
 
 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
 
 
 
 
 
+
-
-
-
-
-
-
-
-
 
S
a
v
i
n
g
 
<
-
-
-
-
-
-
-
-
[
s
a
v
e
S
t
a
t
e
(
)
]
<
-
-
-
-
-
-
-
-
-
-
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
 
S
t
o
p
p
i
n
g
 
-
-
-
-
-
-
-
[
p
o
w
e
r
D
o
w
n
(
)
]
<
-
-
-
-
-
-
-
-
-
-
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
+


 
 
 
 
 
 




 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
s
t
a
t
e
s
 
t
o
 
t
h
e
 
r
i
g
h
t
 
f
r
o
m
 
P
o
w
e
r
e
d
O
f
f
,
 
A
b
o
r
t
e
d
 
a
n
d
 
S
a
v
e
d
 
i
n
 
t
h
e


 
 
 
 
 
 
a
b
o
v
e
 
d
i
a
g
r
a
m
 
a
r
e
 
c
a
l
l
e
d
 
o
n
l
i
n
e
 
V
M
 
s
t
a
t
e
s
.
 
T
h
e
s
e
 
s
t
a
t
e
s


 
 
 
 
 
 
r
e
p
r
e
s
e
n
t
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
w
h
i
c
h
 
i
s
 
b
e
i
n
g
 
e
x
e
c
u
t
e
d
 
i
n
 
a
 
d
e
d
i
c
a
t
e
d


 
 
 
 
 
 
p
r
o
c
e
s
s
 
(
u
s
u
a
l
l
y
 
w
i
t
h
 
a
 
G
U
I
 
w
i
n
d
o
w
 
a
t
t
a
c
h
e
d
 
t
o
 
i
t
 
w
h
e
r
e
 
y
o
u
 
c
a
n
 
s
e
e
 
t
h
e


 
 
 
 
 
 
a
c
t
i
v
i
t
y
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
a
n
d
 
i
n
t
e
r
a
c
t
 
w
i
t
h
 
i
t
)
.
 
T
h
e
r
e
 
a
r
e
 
t
w
o


 
 
 
 
 
 
s
p
e
c
i
a
l
 
p
s
e
u
d
o
-
s
t
a
t
e
s
,
 
F
i
r
s
t
O
n
l
i
n
e
 
a
n
d
 
L
a
s
t
O
n
l
i
n
e
,
 
t
h
a
t
 
c
a
n
 
b
e
 
u
s
e
d
 
i
n


 
 
 
 
 
 
r
e
l
a
t
i
o
n
a
l
 
e
x
p
r
e
s
s
i
o
n
s
 
t
o
 
d
e
t
e
c
t
 
i
f
 
t
h
e
 
g
i
v
e
n
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
i
s
 
o
n
l
i
n
e
 
o
r


 
 
 
 
 
 
n
o
t
:




 
 
 
 
 
 


 
 
 
 
 
 
 
 
i
f
 
(
m
a
c
h
i
n
e
.
G
e
t
S
t
a
t
e
(
)
 
>
=
 
M
a
c
h
i
n
e
S
t
a
t
e
_
F
i
r
s
t
O
n
l
i
n
e
 
&
a
m
p
;
&
a
m
p
;


 
 
 
 
 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
.
G
e
t
S
t
a
t
e
(
)
 
<
=
 
M
a
c
h
i
n
e
S
t
a
t
e
_
L
a
s
t
O
n
l
i
n
e
)


 
 
 
 
 
 
 
 
{


 
 
 
 
 
 
 
 
 
 
 
 
.
.
.
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
b
e
i
n
g
 
e
x
e
c
u
t
e
d
.
.
.


 
 
 
 
 
 
 
 
}


 
 
 
 
 
 




 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
i
n
 
o
n
e
 
o
f
 
t
h
e
 
o
n
l
i
n
e
 
V
M
 
s
t
a
t
e
s
 
(
t
h
a
t
 
i
s
,
 
b
e
i
n
g


 
 
 
 
 
 
e
x
e
c
u
t
e
d
)
,
 
o
n
l
y
 
a
 
f
e
w
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
c
a
n
 
b
e
 
m
o
d
i
f
i
e
d
.
 
M
e
t
h
o
d
s
 
w
o
r
k
i
n
g


 
 
 
 
 
 
w
i
t
h
 
s
u
c
h
 
s
e
t
t
i
n
g
s
 
c
o
n
t
a
i
n
 
a
n
 
e
x
p
l
i
c
i
t
 
n
o
t
e
 
a
b
o
u
t
 
t
h
a
t
.
 
A
n
 
a
t
t
e
m
p
t
 
t
o


 
 
 
 
 
 
c
h
a
n
g
e
 
a
n
y
 
o
t
h
e
r
 
s
e
t
t
i
n
g
 
o
r
 
p
e
r
f
o
r
m
 
a
 
m
o
d
i
f
y
i
n
g
 
o
p
e
r
a
t
i
o
n
 
d
u
r
i
n
g
 
t
h
i
s
 
t
i
m
e


 
 
 
 
 
 
w
i
l
l
 
r
e
s
u
l
t
 
i
n
 
t
h
e
 
@
c
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E
 
e
r
r
o
r
.




 
 
 
 
 
 
A
l
l
 
o
n
l
i
n
e
 
s
t
a
t
e
s
 
e
x
c
e
p
t
 
R
u
n
n
i
n
g
,
 
P
a
u
s
e
d
 
a
n
d
 
S
t
u
c
k
 
a
r
e
 
t
r
a
n
s
i
t
i
o
n
a
l
:
 
t
h
e
y


 
 
 
 
 
 
r
e
p
r
e
s
e
n
t
 
t
e
m
p
o
r
a
r
y
 
c
o
n
d
i
t
i
o
n
s
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
t
h
a
t
 
w
i
l
l
 
l
a
s
t
 
a
s


 
 
 
 
 
 
l
o
n
g
 
a
s
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
t
h
a
t
 
i
n
i
t
i
a
t
e
d
 
s
u
c
h
 
a
 
c
o
n
d
i
t
i
o
n
.




 
 
 
 
 
 
T
h
e
 
S
t
u
c
k
 
s
t
a
t
e
 
i
s
 
a
 
s
p
e
c
i
a
l
 
c
a
s
e
.
 
I
t
 
m
e
a
n
s
 
t
h
a
t
 
e
x
e
c
u
t
i
o
n
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e


 
 
 
 
 
 
h
a
s
 
r
e
a
c
h
e
d
 
t
h
e
 
"
G
u
r
u
 
M
e
d
i
t
a
t
i
o
n
"
 
c
o
n
d
i
t
i
o
n
.
 
T
h
i
s
 
c
o
n
d
i
t
i
o
n
 
i
n
d
i
c
a
t
e
s
 
a
n


 
 
 
 
 
 
i
n
t
e
r
n
a
l
 
V
M
M
 
(
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
m
a
n
a
g
e
r
)
 
f
a
i
l
u
r
e
 
w
h
i
c
h
 
m
a
y
 
h
a
p
p
e
n
 
a
s
 
a


 
 
 
 
 
 
r
e
s
u
l
t
 
o
f
 
e
i
t
h
e
r
 
a
n
 
u
n
h
a
n
d
l
e
d
 
l
o
w
-
l
e
v
e
l
 
v
i
r
t
u
a
l
 
h
a
r
d
w
a
r
e
 
e
x
c
e
p
t
i
o
n
 
o
r
 
o
n
e


 
 
 
 
 
 
o
f
 
t
h
e
 
r
e
c
o
m
p
i
l
e
r
 
e
x
c
e
p
t
i
o
n
s
 
(
s
u
c
h
 
a
s
 
t
h
e
 
t
o
o
-
m
a
n
y
-
t
r
a
p
s


 
 
 
 
 
 
c
o
n
d
i
t
i
o
n
)
.




 
 
 
 
 
 
N
o
t
e
 
a
l
s
o
 
t
h
a
t
 
a
n
y
 
o
n
l
i
n
e
 
V
M
 
s
t
a
t
e
 
m
a
y
 
t
r
a
n
s
i
t
 
t
o
 
t
h
e
 
A
b
o
r
t
e
d
 
s
t
a
t
e
.
 
T
h
i
s


 
 
 
 
 
 
h
a
p
p
e
n
s
 
i
f
 
t
h
e
 
p
r
o
c
e
s
s
 
t
h
a
t
 
i
s
 
e
x
e
c
u
t
i
n
g
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
t
e
r
m
i
n
a
t
e
s


 
 
 
 
 
 
u
n
e
x
p
e
c
t
e
d
l
y
 
(
f
o
r
 
e
x
a
m
p
l
e
,
 
c
r
a
s
h
e
s
)
.
 
O
t
h
e
r
 
t
h
a
n
 
t
h
a
t
,
 
t
h
e
 
A
b
o
r
t
e
d
 
s
t
a
t
e
 
i
s


 
 
 
 
 
 
e
q
u
i
v
a
l
e
n
t
 
t
o
 
P
o
w
e
r
e
d
O
f
f
.




 
 
 
 
 
 
T
h
e
r
e
 
a
r
e
 
a
l
s
o
 
a
 
f
e
w
 
a
d
d
i
t
i
o
n
a
l
 
s
t
a
t
e
 
d
i
a
g
r
a
m
s
 
t
h
a
t
 
d
o
 
n
o
t
 
d
e
a
l
 
w
i
t
h


 
 
 
 
 
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
 
a
n
d
 
t
h
e
r
e
f
o
r
e
 
a
r
e
 
s
h
o
w
n
 
s
e
p
a
r
a
t
e
l
y
.
 
T
h
e
 
s
t
a
t
e
s


 
 
 
 
 
 
s
h
o
w
n
 
o
n
 
t
h
e
s
e
 
d
i
a
g
r
a
m
s
 
a
r
e
 
c
a
l
l
e
d
 
o
f
f
l
i
n
e
 
V
M
 
s
t
a
t
e
s
 
(
t
h
i
s
 
i
n
c
l
u
d
e
s


 
 
 
 
 
 
P
o
w
e
r
e
d
O
f
f
,
 
A
b
o
r
t
e
d
 
a
n
d
 
S
a
v
e
d
 
t
o
o
)
.




 
 
 
 
 
 
T
h
e
 
f
i
r
s
t
 
d
i
a
g
r
a
m
 
s
h
o
w
s
 
w
h
a
t
 
h
a
p
p
e
n
s
 
w
h
e
n
 
a
 
l
e
n
g
t
h
y
 
s
e
t
u
p
 
o
p
e
r
a
t
i
o
n
 
i
s


 
 
 
 
 
 
b
e
i
n
g
 
e
x
e
c
u
t
e
d
 
(
s
u
c
h
 
a
s
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
)
.




 
 
 
 
 
 


 
 
 
 
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
(
s
a
m
e
 
s
t
a
t
e
 
a
s
 
b
e
f
o
r
e
 
t
h
e
 
c
a
l
l
)
-
-
-
-
-
-
+


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
+
-
>
 
P
o
w
e
r
e
d
O
f
f
 
-
-
+
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
-
>
 
A
b
o
r
t
e
d
 
-
-
-
-
-
+
-
-
>
[
l
e
n
g
t
h
y
 
V
M
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
c
a
l
l
]
 
-
-
>
 
S
e
t
t
i
n
g
U
p
 
-
-
-
-
-
+


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
+
-
>
 
S
a
v
e
d
 
-
-
-
-
-
-
-
+


 
 
 
 
 
 




 
 
 
 
 
 
T
h
e
 
n
e
x
t
 
t
w
o
 
d
i
a
g
r
a
m
s
 
d
e
m
o
n
s
t
r
a
t
e
 
t
h
e
 
p
r
o
c
e
s
s
 
o
f
 
t
a
k
i
n
g
 
a
 
s
n
a
p
s
h
o
t
 
o
f
 
a


 
 
 
 
 
 
p
o
w
e
r
e
d
 
o
f
f
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
,
 
r
e
s
t
o
r
i
n
g
 
t
h
e
 
s
t
a
t
e
 
t
o
 
t
h
a
t
 
a
s
 
o
f
 
a
 
s
n
a
p
s
h
o
t


 
 
 
 
 
 
o
r
 
d
e
l
e
t
i
n
g
 
a
 
s
n
a
p
s
h
o
t
,
 
r
e
s
p
e
c
t
i
v
e
l
y
.




 
 
 
 
 
 


 
 
 
 
+
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
(
s
a
m
e
 
s
t
a
t
e
 
a
s
 
b
e
f
o
r
e
 
t
h
e
 
c
a
l
l
)
-
-
-
-
-
-
+


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
+
-
>
 
P
o
w
e
r
e
d
O
f
f
 
-
-
+
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
+
-
-
>
[
t
a
k
e
S
n
a
p
s
h
o
t
(
)
]
 
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
>
 
S
a
v
i
n
g
 
-
-
-
-
-
-
+


 
 
 
 
+
-
>
 
A
b
o
r
t
e
d
 
-
-
-
-
-
+




 
 
 
 
+
-
>
 
P
o
w
e
r
e
d
O
f
f
 
-
-
+


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
 
 
 
A
b
o
r
t
e
d
 
-
-
-
-
-
+
-
-
>
[
r
e
s
t
o
r
e
S
n
a
p
s
h
o
t
(
)
 
 
 
 
]
-
-
-
-
-
-
-
>
 
R
e
s
t
o
r
i
n
g
S
n
a
p
s
h
o
t
 
-
+


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|
 
 
 
[
d
e
l
e
t
e
S
n
a
p
s
h
o
t
(
)
 
 
 
 
 
]
-
-
-
-
-
-
-
>
 
D
e
l
e
t
i
n
g
S
n
a
p
s
h
o
t
 
-
-
+


 
 
 
 
+
-
>
 
S
a
v
e
d
 
-
-
-
-
-
-
-
+
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
|
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
|


 
 
 
 
+
-
-
-
(
S
a
v
e
d
 
i
f
 
r
e
s
t
o
r
e
d
 
f
r
o
m
 
a
n
 
o
n
l
i
n
e
 
s
n
a
p
s
h
o
t
,
 
P
o
w
e
r
e
d
O
f
f
 
o
t
h
e
r
w
i
s
e
)
-
-
-
+


 
 
 
 
 
 




 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
S
a
v
i
n
g
 
s
t
a
t
e
 
i
s
 
p
r
e
s
e
n
t
 
i
n
 
b
o
t
h
 
t
h
e
 
o
f
f
l
i
n
e
 
s
t
a
t
e
 
g
r
o
u
p
 
a
n
d


 
 
 
 
 
 
o
n
l
i
n
e
 
s
t
a
t
e
 
g
r
o
u
p
.
 
C
u
r
r
e
n
t
l
y
,
 
t
h
e
 
o
n
l
y
 
w
a
y
 
t
o
 
d
e
t
e
r
m
i
n
e
 
w
h
a
t
 
g
r
o
u
p
 
i
s


 
 
 
 
 
 
a
s
s
u
m
e
d
 
i
n
 
a
 
p
a
r
t
i
c
u
l
a
r
 
c
a
s
e
 
i
s
 
t
o
 
r
e
m
e
m
b
e
r
 
t
h
e
 
p
r
e
v
i
o
u
s
 
m
a
c
h
i
n
e
 
s
t
a
t
e
:
 
i
f


 
 
 
 
 
 
i
t
 
w
a
s
 
R
u
n
n
i
n
g
 
o
r
 
P
a
u
s
e
d
,
 
t
h
e
n
 
S
a
v
i
n
g
 
i
s
 
a
n
 
o
n
l
i
n
e
 
s
t
a
t
e
,
 
o
t
h
e
r
w
i
s
e
 
i
t
 
i
s


 
 
 
 
 
 
a
n
 
o
f
f
l
i
n
e
 
s
t
a
t
e
.
 
T
h
i
s
 
i
n
c
o
n
s
i
s
t
e
n
c
y
 
m
a
y
 
b
e
 
r
e
m
o
v
e
d
 
i
n
 
o
n
e
 
o
f
 
t
h
e
 
f
u
t
u
r
e


 
 
 
 
 
 
v
e
r
s
i
o
n
s
 
o
f
 
V
i
r
t
u
a
l
B
o
x
 
b
y
 
a
d
d
i
n
g
 
a
 
n
e
w
 
s
t
a
t
e
.




 
 
 
 
 
 
<
n
o
t
e
 
i
n
t
e
r
n
a
l
=
"
y
e
s
"
>


 
 
 
 
 
 
 
 
F
o
r
 
w
h
o
e
v
e
r
 
d
e
c
i
d
e
s
 
t
o
 
t
o
u
c
h
 
t
h
i
s
 
e
n
u
m
:
 
I
n
 
o
r
d
e
r
 
t
o
 
k
e
e
p
 
t
h
e


 
 
 
 
 
 
 
 
c
o
m
p
a
r
i
s
o
n
s
 
i
n
v
o
l
v
i
n
g
 
F
i
r
s
t
O
n
l
i
n
e
 
a
n
d
 
L
a
s
t
O
n
l
i
n
e
 
p
s
e
u
d
o
-
s
t
a
t
e
s
 
v
a
l
i
d
,


 
 
 
 
 
 
 
 
t
h
e
 
n
u
m
e
r
i
c
 
v
a
l
u
e
s
 
o
f
 
t
h
e
s
e
 
s
t
a
t
e
s
 
m
u
s
t
 
b
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
l
y
 
u
p
d
a
t
e
d
 
i
f


 
 
 
 
 
 
 
 
n
e
e
d
e
d
:
 
f
o
r
 
a
n
y
 
o
n
l
i
n
e
 
V
M
 
s
t
a
t
e
,
 
t
h
e
 
c
o
n
d
i
t
i
o
n


 
 
 
 
 
 
 
 
F
i
r
s
t
O
n
l
i
n
e
 
<
=
 
s
t
a
t
e
 
<
=
 
L
a
s
t
O
n
l
i
n
e
 
m
u
s
t
 
b
e


 
 
 
 
 
 
 
 
@
c
 
t
r
u
e
.
 
T
h
e
 
s
a
m
e
 
r
e
l
a
t
e
s
 
t
o
 
t
r
a
n
s
i
e
n
t
 
s
t
a
t
e
s
 
f
o
r
 
w
h
i
c
h


 
 
 
 
 
 
 
 
t
h
e
 
c
o
n
d
i
t
i
o
n
 
F
i
r
s
t
O
n
l
i
n
e
 
<
=
 
s
t
a
t
e
 
<
=
 
L
a
s
t
O
n
l
i
n
e
 
m
u
s
t
 
b
e


 
 
 
 
 
 
 
 
@
c
 
t
r
u
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
e
c
6
c
6
a
9
e
-
1
1
3
d
-
4
f
f
4
-
b
4
4
f
-
0
b
6
9
f
2
1
c
9
7
f
e
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
b
o
r
t
e
d
'
:
 
4
,


 
 
 
 
 
 
 
 
'
D
e
l
e
t
i
n
g
S
n
a
p
s
h
o
t
'
:
 
2
0
,


 
 
 
 
 
 
 
 
'
D
e
l
e
t
i
n
g
S
n
a
p
s
h
o
t
O
n
l
i
n
e
'
:
 
1
7
,


 
 
 
 
 
 
 
 
'
D
e
l
e
t
i
n
g
S
n
a
p
s
h
o
t
P
a
u
s
e
d
'
:
 
1
8
,


 
 
 
 
 
 
 
 
'
F
a
u
l
t
T
o
l
e
r
a
n
t
S
y
n
c
i
n
g
'
:
 
1
6
,


 
 
 
 
 
 
 
 
'
F
i
r
s
t
O
n
l
i
n
e
'
:
 
5
,


 
 
 
 
 
 
 
 
'
F
i
r
s
t
T
r
a
n
s
i
e
n
t
'
:
 
8
,


 
 
 
 
 
 
 
 
'
L
a
s
t
O
n
l
i
n
e
'
:
 
1
8
,


 
 
 
 
 
 
 
 
'
L
a
s
t
T
r
a
n
s
i
e
n
t
'
:
 
2
1
,


 
 
 
 
 
 
 
 
'
L
i
v
e
S
n
a
p
s
h
o
t
t
i
n
g
'
:
 
9
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
P
a
u
s
e
d
'
:
 
6
,


 
 
 
 
 
 
 
 
'
P
o
w
e
r
e
d
O
f
f
'
:
 
1
,


 
 
 
 
 
 
 
 
'
R
e
s
t
o
r
i
n
g
'
:
 
1
3
,


 
 
 
 
 
 
 
 
'
R
e
s
t
o
r
i
n
g
S
n
a
p
s
h
o
t
'
:
 
1
9
,


 
 
 
 
 
 
 
 
'
R
u
n
n
i
n
g
'
:
 
5
,


 
 
 
 
 
 
 
 
'
S
a
v
e
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
S
a
v
i
n
g
'
:
 
1
2
,


 
 
 
 
 
 
 
 
'
S
e
t
t
i
n
g
U
p
'
:
 
2
1
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
i
n
g
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
S
t
o
p
p
i
n
g
'
:
 
1
1
,


 
 
 
 
 
 
 
 
'
S
t
u
c
k
'
:
 
7
,


 
 
 
 
 
 
 
 
'
T
e
l
e
p
o
r
t
e
d
'
:
 
3
,


 
 
 
 
 
 
 
 
'
T
e
l
e
p
o
r
t
i
n
g
'
:
 
8
,


 
 
 
 
 
 
 
 
'
T
e
l
e
p
o
r
t
i
n
g
I
n
'
:
 
1
5
,


 
 
 
 
 
 
 
 
'
T
e
l
e
p
o
r
t
i
n
g
P
a
u
s
e
d
V
M
'
:
 
1
4
}
 






c
l
a
s
s
 
S
e
s
s
i
o
n
S
t
a
t
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
S
e
s
s
i
o
n
 
s
t
a
t
e
.
 
T
h
i
s
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
p
o
s
s
i
b
l
e
 
v
a
l
u
e
s
 
o
f


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
e
s
s
i
o
n
S
t
a
t
e
"
/
>
 
a
n
d
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
s
t
a
t
e
"
/
>


 
 
 
 
 
 
a
t
t
r
i
b
u
t
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
c
f
2
7
0
0
c
0
-
e
a
4
b
-
4
7
a
e
-
9
7
2
5
-
7
8
1
0
1
1
4
b
9
4
d
8
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
L
o
c
k
e
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
p
a
w
n
i
n
g
'
:
 
3
,


 
 
 
 
 
 
 
 
'
U
n
l
o
c
k
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
U
n
l
o
c
k
i
n
g
'
:
 
4
}
 






c
l
a
s
s
 
C
P
U
P
r
o
p
e
r
t
y
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
 
C
P
U
 
p
r
o
p
e
r
t
y
 
t
y
p
e
.
 
T
h
i
s
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
p
o
s
s
i
b
l
e
 
v
a
l
u
e
s
 
o
f
 
t
h
e


 
 
 
 
 
 
I
M
a
c
h
i
n
e
 
g
e
t
-
 
a
n
d
 
s
e
t
C
P
U
P
r
o
p
e
r
t
y
 
m
e
t
h
o
d
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
2
4
d
3
5
6
a
6
-
2
f
4
5
-
4
a
b
d
-
b
9
7
7
-
1
c
b
e
9
c
4
7
0
1
f
5
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
L
o
n
g
M
o
d
e
'
:
 
3
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
P
A
E
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
y
n
t
h
e
t
i
c
'
:
 
2
}
 






c
l
a
s
s
 
H
W
V
i
r
t
E
x
P
r
o
p
e
r
t
y
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
H
a
r
d
w
a
r
e
 
v
i
r
t
u
a
l
i
z
a
t
i
o
n
 
p
r
o
p
e
r
t
y
 
t
y
p
e
.
 
T
h
i
s
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
p
o
s
s
i
b
l
e
 
v
a
l
u
e
s


 
 
 
 
 
 
f
o
r
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
g
e
t
H
W
V
i
r
t
E
x
P
r
o
p
e
r
t
y
"
/
>
 
a
n
d


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
e
t
H
W
V
i
r
t
E
x
P
r
o
p
e
r
t
y
"
/
>
 
m
e
t
h
o
d
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
9
4
6
3
e
c
d
-
b
4
b
8
-
4
0
1
f
-
b
1
6
8
-
7
6
c
f
a
8
7
e
1
1
f
0
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
E
n
a
b
l
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
E
x
c
l
u
s
i
v
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
F
o
r
c
e
'
:
 
7
,


 
 
 
 
 
 
 
 
'
L
a
r
g
e
P
a
g
e
s
'
:
 
6
,


 
 
 
 
 
 
 
 
'
N
e
s
t
e
d
P
a
g
i
n
g
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
U
n
r
e
s
t
r
i
c
t
e
d
E
x
e
c
u
t
i
o
n
'
:
 
5
,


 
 
 
 
 
 
 
 
'
V
P
I
D
'
:
 
3
}
 






c
l
a
s
s
 
F
a
u
l
t
T
o
l
e
r
a
n
c
e
S
t
a
t
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
U
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
f
a
u
l
t
T
o
l
e
r
a
n
c
e
S
t
a
t
e
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
5
1
2
4
f
7
e
c
-
6
b
6
7
-
4
9
3
c
-
9
d
e
e
-
e
e
4
5
a
4
4
1
1
4
e
1
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
I
n
a
c
t
i
v
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
M
a
s
t
e
r
'
:
 
2
,


 
 
 
 
 
 
 
 
'
S
t
a
n
d
b
y
'
:
 
3
}
 






c
l
a
s
s
 
L
o
c
k
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
U
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
o
c
k
M
a
c
h
i
n
e
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
1
6
8
a
6
a
8
e
-
1
2
f
d
-
4
8
7
8
-
a
1
f
9
-
3
8
a
7
5
0
a
5
6
0
8
9
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
S
h
a
r
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
V
M
'
:
 
3
,


 
 
 
 
 
 
 
 
'
W
r
i
t
e
'
:
 
2
}
 






c
l
a
s
s
 
S
e
s
s
i
o
n
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
S
e
s
s
i
o
n
 
t
y
p
e
.
 
T
h
i
s
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
p
o
s
s
i
b
l
e
 
v
a
l
u
e
s
 
o
f
 
t
h
e


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
t
y
p
e
"
/
>
 
a
t
t
r
i
b
u
t
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
A
1
3
C
0
2
C
B
-
0
C
2
C
-
4
2
1
E
-
8
3
1
7
-
A
C
0
E
8
A
A
A
1
5
3
A
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
R
e
m
o
t
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
S
h
a
r
e
d
'
:
 
3
,


 
 
 
 
 
 
 
 
'
W
r
i
t
e
L
o
c
k
'
:
 
1
}
 






c
l
a
s
s
 
D
e
v
i
c
e
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
D
e
v
i
c
e
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
d
9
4
2
0
f
7
-
0
b
5
6
-
4
6
3
6
-
9
9
f
9
-
7
3
4
6
f
1
b
0
1
e
5
7
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
V
D
'
:
 
2
,


 
 
 
 
 
 
 
 
'
F
l
o
p
p
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
H
a
r
d
D
i
s
k
'
:
 
3
,


 
 
 
 
 
 
 
 
'
N
e
t
w
o
r
k
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
h
a
r
e
d
F
o
l
d
e
r
'
:
 
6
,


 
 
 
 
 
 
 
 
'
U
S
B
'
:
 
5
}
 






c
l
a
s
s
 
D
e
v
i
c
e
A
c
t
i
v
i
t
y
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
D
e
v
i
c
e
 
a
c
t
i
v
i
t
y
 
f
o
r
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
g
e
t
D
e
v
i
c
e
A
c
t
i
v
i
t
y
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
F
C
8
A
E
A
A
-
1
3
0
A
-
4
e
b
5
-
8
9
5
4
-
3
F
9
2
1
4
2
2
D
7
0
7
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
I
d
l
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
R
e
a
d
i
n
g
'
:
 
2
,


 
 
 
 
 
 
 
 
'
W
r
i
t
i
n
g
'
:
 
3
}
 






c
l
a
s
s
 
C
l
i
p
b
o
a
r
d
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
H
o
s
t
-
G
u
e
s
t
 
c
l
i
p
b
o
a
r
d
 
i
n
t
e
r
c
h
a
n
g
e
 
m
o
d
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
3
3
6
4
7
1
6
-
4
0
0
8
-
4
7
0
1
-
8
f
1
4
-
b
e
0
f
a
3
d
6
2
9
5
0
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
B
i
d
i
r
e
c
t
i
o
n
a
l
'
:
 
3
,


 
 
 
 
 
 
 
 
'
D
i
s
a
b
l
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
G
u
e
s
t
T
o
H
o
s
t
'
:
 
2
,


 
 
 
 
 
 
 
 
'
H
o
s
t
T
o
G
u
e
s
t
'
:
 
1
}
 






c
l
a
s
s
 
D
r
a
g
A
n
d
D
r
o
p
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
D
r
a
g
'
n
'
D
r
o
p
 
i
n
t
e
r
c
h
a
n
g
e
 
m
o
d
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
b
6
1
8
e
a
0
e
-
b
6
f
b
-
4
f
8
d
-
9
7
f
7
-
5
e
2
3
7
e
4
9
b
5
4
7
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
B
i
d
i
r
e
c
t
i
o
n
a
l
'
:
 
3
,


 
 
 
 
 
 
 
 
'
D
i
s
a
b
l
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
G
u
e
s
t
T
o
H
o
s
t
'
:
 
2
,


 
 
 
 
 
 
 
 
'
H
o
s
t
T
o
G
u
e
s
t
'
:
 
1
}
 






c
l
a
s
s
 
S
c
o
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
S
c
o
p
e
 
o
f
 
t
h
e
 
o
p
e
r
a
t
i
o
n
.




 
 
 
 
 
 
A
 
g
e
n
e
r
i
c
 
e
n
u
m
e
r
a
t
i
o
n
 
u
s
e
d
 
i
n
 
v
a
r
i
o
u
s
 
m
e
t
h
o
d
s
 
t
o
 
d
e
f
i
n
e
 
t
h
e
 
a
c
t
i
o
n
 
o
r


 
 
 
 
 
 
a
r
g
u
m
e
n
t
 
s
c
o
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
c
9
1
0
9
6
e
-
4
9
9
e
-
4
e
c
a
-
9
f
9
b
-
9
0
0
1
4
3
8
d
7
8
5
5
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
G
l
o
b
a
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
M
a
c
h
i
n
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
e
s
s
i
o
n
'
:
 
2
}
 






c
l
a
s
s
 
B
I
O
S
B
o
o
t
M
e
n
u
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
B
I
O
S
 
b
o
o
t
 
m
e
n
u
 
m
o
d
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
a
e
4
f
b
9
f
7
-
2
9
d
2
-
4
5
b
4
-
b
2
c
7
-
d
5
7
9
6
0
3
1
3
5
d
5
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
i
s
a
b
l
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
M
e
n
u
O
n
l
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
M
e
s
s
a
g
e
A
n
d
M
e
n
u
'
:
 
2
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
o
r
F
e
a
t
u
r
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
C
P
U
 
f
e
a
t
u
r
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
4
c
3
8
e
6
b
-
8
b
c
f
-
4
5
a
d
-
a
c
0
3
-
9
b
4
0
6
2
8
7
c
5
b
f
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
H
W
V
i
r
t
E
x
'
:
 
0
,


 
 
 
 
 
 
 
 
'
L
o
n
g
M
o
d
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
N
e
s
t
e
d
P
a
g
i
n
g
'
:
 
3
,


 
 
 
 
 
 
 
 
'
P
A
E
'
:
 
1
}
 






c
l
a
s
s
 
F
i
r
m
w
a
r
e
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
F
i
r
m
w
a
r
e
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
b
9
0
3
f
2
6
4
-
c
2
3
0
-
4
8
3
e
-
a
c
7
4
-
2
b
3
7
c
e
6
0
d
3
7
1
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
B
I
O
S
'
:
 
1
,


 
 
 
 
 
 
 
 
'
E
F
I
'
:
 
2
,


 
 
 
 
 
 
 
 
'
E
F
I
3
2
'
:
 
3
,


 
 
 
 
 
 
 
 
'
E
F
I
6
4
'
:
 
4
,


 
 
 
 
 
 
 
 
'
E
F
I
D
U
A
L
'
:
 
5
}
 






c
l
a
s
s
 
P
o
i
n
t
i
n
g
H
I
D
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
y
p
e
 
o
f
 
p
o
i
n
t
i
n
g
 
d
e
v
i
c
e
 
u
s
e
d
 
i
n
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
e
4
4
b
2
f
7
b
-
7
2
b
a
-
4
4
f
b
-
9
e
5
3
-
2
1
8
6
0
1
4
f
0
d
1
7
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
o
m
b
o
M
o
u
s
e
'
:
 
5
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
P
S
2
M
o
u
s
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
U
S
B
M
o
u
s
e
'
:
 
3
,


 
 
 
 
 
 
 
 
'
U
S
B
T
a
b
l
e
t
'
:
 
4
}
 






c
l
a
s
s
 
K
e
y
b
o
a
r
d
H
I
D
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
y
p
e
 
o
f
 
k
e
y
b
o
a
r
d
 
d
e
v
i
c
e
 
u
s
e
d
 
i
n
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
8
3
e
4
3
d
7
-
5
c
7
c
-
4
e
c
8
-
9
c
b
8
-
e
d
a
1
b
c
c
d
6
6
9
9
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
o
m
b
o
K
e
y
b
o
a
r
d
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
P
S
2
K
e
y
b
o
a
r
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
U
S
B
K
e
y
b
o
a
r
d
'
:
 
3
}
 






c
l
a
s
s
 
V
F
S
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
 
f
i
l
e
 
s
y
s
t
e
m
s
 
s
u
p
p
o
r
t
e
d
 
b
y
 
V
F
S
E
x
p
l
o
r
e
r
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
8
1
3
9
9
9
b
a
-
b
9
4
9
-
4
8
a
8
-
9
2
3
0
-
a
a
d
c
6
2
8
5
e
2
f
2
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
l
o
u
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
F
i
l
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
3
'
:
 
3
,


 
 
 
 
 
 
 
 
'
W
e
b
D
a
v
'
:
 
4
}
 






c
l
a
s
s
 
V
F
S
F
i
l
e
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
F
i
l
e
 
t
y
p
e
s
 
k
n
o
w
n
 
b
y
 
V
F
S
E
x
p
l
o
r
e
r
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
1
4
3
3
3
c
d
-
4
4
e
2
-
4
1
5
f
-
a
2
4
5
-
d
3
7
8
f
a
9
b
1
2
4
2
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
e
v
B
l
o
c
k
'
:
 
5
,


 
 
 
 
 
 
 
 
'
D
e
v
C
h
a
r
'
:
 
3
,


 
 
 
 
 
 
 
 
'
D
i
r
e
c
t
o
r
y
'
:
 
4
,


 
 
 
 
 
 
 
 
'
F
i
f
o
'
:
 
2
,


 
 
 
 
 
 
 
 
'
F
i
l
e
'
:
 
6
,


 
 
 
 
 
 
 
 
'
S
o
c
k
e
t
'
:
 
8
,


 
 
 
 
 
 
 
 
'
S
y
m
L
i
n
k
'
:
 
7
,


 
 
 
 
 
 
 
 
'
U
n
k
n
o
w
n
'
:
 
1
,


 
 
 
 
 
 
 
 
'
W
h
i
t
e
O
u
t
'
:
 
9
}
 






c
l
a
s
s
 
I
m
p
o
r
t
O
p
t
i
o
n
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
I
m
p
o
r
t
 
o
p
t
i
o
n
s
,
 
u
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
:
:
i
m
p
o
r
t
M
a
c
h
i
n
e
s
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
0
a
9
8
1
5
2
3
-
3
b
2
0
-
4
0
0
4
-
8
e
e
3
-
d
f
d
3
2
2
2
0
2
a
c
e
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
K
e
e
p
A
l
l
M
A
C
s
'
:
 
1
,


 
 
 
 
 
 
 
 
'
K
e
e
p
N
A
T
M
A
C
s
'
:
 
2
}
 






c
l
a
s
s
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
U
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
"
/
>
 
t
o
 
d
e
s
c
r
i
b
e
 
t
h
e
 
t
y
p
e
 
o
f


 
 
 
 
a
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
v
a
l
u
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
0
3
c
0
9
0
0
-
a
7
4
6
-
4
6
1
2
-
8
c
6
7
-
7
9
0
0
3
e
9
1
f
4
5
9
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
D
R
O
M
'
:
 
2
0
,


 
 
 
 
 
 
 
 
'
C
P
U
'
:
 
1
2
,


 
 
 
 
 
 
 
 
'
D
e
s
c
r
i
p
t
i
o
n
'
:
 
9
,


 
 
 
 
 
 
 
 
'
F
l
o
p
p
y
'
:
 
1
9
,


 
 
 
 
 
 
 
 
'
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
I
D
E
'
:
 
1
4
,


 
 
 
 
 
 
 
 
'
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
A
S
'
:
 
1
7
,


 
 
 
 
 
 
 
 
'
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
A
T
A
'
:
 
1
5
,


 
 
 
 
 
 
 
 
'
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
C
S
I
'
:
 
1
6
,


 
 
 
 
 
 
 
 
'
H
a
r
d
D
i
s
k
I
m
a
g
e
'
:
 
1
8
,


 
 
 
 
 
 
 
 
'
I
g
n
o
r
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
L
i
c
e
n
s
e
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
M
e
m
o
r
y
'
:
 
1
3
,


 
 
 
 
 
 
 
 
'
M
i
s
c
e
l
l
a
n
e
o
u
s
'
:
 
1
1
,


 
 
 
 
 
 
 
 
'
N
a
m
e
'
:
 
3
,


 
 
 
 
 
 
 
 
'
N
e
t
w
o
r
k
A
d
a
p
t
e
r
'
:
 
2
1
,


 
 
 
 
 
 
 
 
'
O
S
'
:
 
2
,


 
 
 
 
 
 
 
 
'
P
r
o
d
u
c
t
'
:
 
4
,


 
 
 
 
 
 
 
 
'
P
r
o
d
u
c
t
U
r
l
'
:
 
7
,


 
 
 
 
 
 
 
 
'
S
e
t
t
i
n
g
s
F
i
l
e
'
:
 
2
4
,


 
 
 
 
 
 
 
 
'
S
o
u
n
d
C
a
r
d
'
:
 
2
3
,


 
 
 
 
 
 
 
 
'
U
S
B
C
o
n
t
r
o
l
l
e
r
'
:
 
2
2
,


 
 
 
 
 
 
 
 
'
V
e
n
d
o
r
'
:
 
5
,


 
 
 
 
 
 
 
 
'
V
e
n
d
o
r
U
r
l
'
:
 
8
,


 
 
 
 
 
 
 
 
'
V
e
r
s
i
o
n
'
:
 
6
}
 






c
l
a
s
s
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
V
a
l
u
e
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
U
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
:
:
g
e
t
V
a
l
u
e
s
B
y
T
y
p
e
"
/
>
 
t
o
 
d
e
s
c
r
i
b
e
 
t
h
e
 
v
a
l
u
e


 
 
 
 
t
y
p
e
 
t
o
 
f
e
t
c
h
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
5
6
d
9
4
0
3
f
-
3
4
2
5
-
4
1
1
8
-
9
9
1
9
-
3
6
f
2
a
9
b
8
c
7
7
c
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
u
t
o
'
:
 
3
,


 
 
 
 
 
 
 
 
'
E
x
t
r
a
C
o
n
f
i
g
'
:
 
4
,


 
 
 
 
 
 
 
 
'
O
r
i
g
i
n
a
l
'
:
 
2
,


 
 
 
 
 
 
 
 
'
R
e
f
e
r
e
n
c
e
'
:
 
1
}
 






c
l
a
s
s
 
G
r
a
p
h
i
c
s
C
o
n
t
r
o
l
l
e
r
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
r
a
p
h
i
c
s
 
c
o
n
t
r
o
l
l
e
r
 
t
y
p
e
,
 
u
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
u
n
r
e
g
i
s
t
e
r
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
9
c
9
6
c
a
0
-
9
f
3
9
-
4
9
0
0
-
9
4
8
e
-
6
8
c
4
1
c
b
e
1
2
7
a
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
V
B
o
x
V
G
A
'
:
 
1
}
 






c
l
a
s
s
 
C
l
e
a
n
u
p
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
C
l
e
a
n
u
p
 
m
o
d
e
,
 
u
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
u
n
r
e
g
i
s
t
e
r
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
7
8
9
7
c
5
0
-
7
c
c
a
-
4
7
a
9
-
8
3
f
6
-
c
e
8
f
d
8
e
b
5
4
4
1
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
e
t
a
c
h
A
l
l
R
e
t
u
r
n
H
a
r
d
D
i
s
k
s
O
n
l
y
'
:
 
3
,


 
 
 
 
 
 
 
 
'
D
e
t
a
c
h
A
l
l
R
e
t
u
r
n
N
o
n
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
F
u
l
l
'
:
 
4
,


 
 
 
 
 
 
 
 
'
U
n
r
e
g
i
s
t
e
r
O
n
l
y
'
:
 
1
}
 






c
l
a
s
s
 
C
l
o
n
e
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
C
l
o
n
e
 
m
o
d
e
,
 
u
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
c
l
o
n
e
T
o
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
A
7
A
1
5
9
F
E
-
5
0
9
6
-
4
B
8
D
-
8
C
3
C
-
D
0
3
3
C
B
0
B
3
5
A
8
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
l
l
S
t
a
t
e
s
'
:
 
3
,


 
 
 
 
 
 
 
 
'
M
a
c
h
i
n
e
A
n
d
C
h
i
l
d
S
t
a
t
e
s
'
:
 
2
,


 
 
 
 
 
 
 
 
'
M
a
c
h
i
n
e
S
t
a
t
e
'
:
 
1
}
 






c
l
a
s
s
 
C
l
o
n
e
O
p
t
i
o
n
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
C
l
o
n
e
 
o
p
t
i
o
n
s
,
 
u
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
c
l
o
n
e
T
o
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
2
2
2
4
3
f
8
e
-
9
6
a
b
-
4
9
7
c
-
8
c
f
0
-
f
4
0
a
5
6
6
c
6
3
0
b
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
K
e
e
p
A
l
l
M
A
C
s
'
:
 
2
,


 
 
 
 
 
 
 
 
'
K
e
e
p
D
i
s
k
N
a
m
e
s
'
:
 
4
,


 
 
 
 
 
 
 
 
'
K
e
e
p
N
A
T
M
A
C
s
'
:
 
3
,


 
 
 
 
 
 
 
 
'
L
i
n
k
'
:
 
1
}
 






c
l
a
s
s
 
A
u
t
o
s
t
o
p
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
A
u
t
o
s
t
o
p
 
t
y
p
e
s
,
 
u
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
u
t
o
s
t
o
p
T
y
p
e
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
b
b
9
6
7
4
0
-
c
f
3
4
-
4
7
0
d
-
a
a
b
2
-
2
c
d
4
8
e
a
2
e
1
0
e
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
c
p
i
S
h
u
t
d
o
w
n
'
:
 
4
,


 
 
 
 
 
 
 
 
'
D
i
s
a
b
l
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
P
o
w
e
r
O
f
f
'
:
 
3
,


 
 
 
 
 
 
 
 
'
S
a
v
e
S
t
a
t
e
'
:
 
2
}
 






c
l
a
s
s
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
M
e
d
i
u
m
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
y
p
e
 
o
f
 
e
n
c
a
p
s
u
l
a
t
i
o
n
.
 
E
t
h
e
r
n
e
t
 
e
n
c
a
p
s
u
l
a
t
i
o
n
 
i
n
c
l
u
d
e
s
 
b
o
t
h
 
w
i
r
e
d
 
a
n
d


 
 
 
 
 
 
w
i
r
e
l
e
s
s
 
E
t
h
e
r
n
e
t
 
c
o
n
n
e
c
t
i
o
n
s
.


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
"
/
>
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
1
a
a
5
4
a
a
f
-
2
4
9
7
-
4
5
a
2
-
b
f
b
1
-
8
e
b
2
2
5
e
9
3
d
5
b
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
E
t
h
e
r
n
e
t
'
:
 
1
,


 
 
 
 
 
 
 
 
'
P
P
P
'
:
 
2
,


 
 
 
 
 
 
 
 
'
S
L
I
P
'
:
 
3
,


 
 
 
 
 
 
 
 
'
U
n
k
n
o
w
n
'
:
 
0
}
 






c
l
a
s
s
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
S
t
a
t
u
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
C
u
r
r
e
n
t
 
s
t
a
t
u
s
 
o
f
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
"
/
>
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
C
C
4
7
4
A
6
9
-
2
7
1
0
-
4
3
4
B
-
8
D
9
9
-
C
3
8
E
5
D
5
A
6
F
4
1
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
o
w
n
'
:
 
2
,


 
 
 
 
 
 
 
 
'
U
n
k
n
o
w
n
'
:
 
0
,


 
 
 
 
 
 
 
 
'
U
p
'
:
 
1
}
 






c
l
a
s
s
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
N
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
7
4
3
1
b
0
0
-
9
9
4
6
-
4
8
a
2
-
b
c
0
2
-
b
2
5
c
5
9
1
9
f
4
f
3
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
B
r
i
d
g
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
H
o
s
t
O
n
l
y
'
:
 
2
}
 






c
l
a
s
s
 
A
d
d
i
t
i
o
n
s
F
a
c
i
l
i
t
y
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
f
a
c
i
l
i
t
y
 
I
D
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
9
8
f
7
f
9
5
7
-
8
9
f
b
-
4
9
b
6
-
a
3
b
1
-
3
1
e
3
2
8
5
e
b
1
d
8
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
l
l
'
:
 
2
1
4
7
4
8
3
6
4
6
,


 
 
 
 
 
 
 
 
'
A
u
t
o
L
o
g
o
n
'
:
 
9
0
,


 
 
 
 
 
 
 
 
'
G
r
a
p
h
i
c
s
'
:
 
1
1
0
0
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
e
a
m
l
e
s
s
'
:
 
1
0
0
0
,


 
 
 
 
 
 
 
 
'
V
B
o
x
G
u
e
s
t
D
r
i
v
e
r
'
:
 
2
0
,


 
 
 
 
 
 
 
 
'
V
B
o
x
S
e
r
v
i
c
e
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
V
B
o
x
T
r
a
y
C
l
i
e
n
t
'
:
 
1
0
1
}
 






c
l
a
s
s
 
A
d
d
i
t
i
o
n
s
F
a
c
i
l
i
t
y
C
l
a
s
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
f
a
c
i
l
i
t
y
 
c
l
a
s
s
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
4
4
6
4
5
1
b
2
-
c
8
8
d
-
4
e
5
d
-
8
4
c
9
-
9
1
b
c
7
f
5
3
3
f
5
f
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
l
l
'
:
 
2
1
4
7
4
8
3
6
4
6
,


 
 
 
 
 
 
 
 
'
D
r
i
v
e
r
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
F
e
a
t
u
r
e
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
P
r
o
g
r
a
m
'
:
 
5
0
,


 
 
 
 
 
 
 
 
'
S
e
r
v
i
c
e
'
:
 
3
0
,


 
 
 
 
 
 
 
 
'
T
h
i
r
d
P
a
r
t
y
'
:
 
9
9
9
}
 






c
l
a
s
s
 
A
d
d
i
t
i
o
n
s
F
a
c
i
l
i
t
y
S
t
a
t
u
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
f
a
c
i
l
i
t
y
 
s
t
a
t
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
c
e
0
6
f
9
e
1
-
3
9
4
e
-
4
f
e
9
-
9
3
6
8
-
5
a
8
8
c
5
6
7
d
b
d
e
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
c
t
i
v
e
'
:
 
5
0
,


 
 
 
 
 
 
 
 
'
F
a
i
l
e
d
'
:
 
8
0
0
,


 
 
 
 
 
 
 
 
'
I
n
a
c
t
i
v
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
I
n
i
t
'
:
 
3
0
,


 
 
 
 
 
 
 
 
'
P
a
u
s
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
P
r
e
I
n
i
t
'
:
 
2
0
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
d
'
:
 
1
0
1
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
i
n
g
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
U
n
k
n
o
w
n
'
:
 
9
9
9
}
 






c
l
a
s
s
 
A
d
d
i
t
i
o
n
s
R
u
n
L
e
v
e
l
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
r
u
n
 
l
e
v
e
l
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
a
2
5
4
1
7
e
e
-
a
9
d
d
-
4
f
5
b
-
b
0
d
c
-
3
7
7
8
6
0
0
8
7
7
5
4
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
e
s
k
t
o
p
'
:
 
3
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
y
s
t
e
m
'
:
 
1
,


 
 
 
 
 
 
 
 
'
U
s
e
r
l
a
n
d
'
:
 
2
}
 






c
l
a
s
s
 
A
d
d
i
t
i
o
n
s
U
p
d
a
t
e
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
u
p
d
a
t
e
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
2
6
a
8
1
8
d
-
1
8
d
6
-
4
3
8
9
-
9
4
e
8
-
3
e
9
e
6
8
2
6
1
7
1
a
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
W
a
i
t
F
o
r
U
p
d
a
t
e
S
t
a
r
t
O
n
l
y
'
:
 
1
}
 






c
l
a
s
s
 
G
u
e
s
t
S
e
s
s
i
o
n
S
t
a
t
u
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
s
e
s
s
i
o
n
 
s
t
a
t
u
s
.
 
T
h
i
s
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
p
o
s
s
i
b
l
e
 
v
a
l
u
e
s
 
o
f


 
 
 
 
 
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
G
u
e
s
t
S
e
s
s
i
o
n
:
:
s
t
a
t
u
s
"
/
>
 
a
t
t
r
i
b
u
t
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
a
c
2
6
6
9
d
a
-
4
6
2
4
-
4
4
f
2
-
8
5
b
5
-
0
b
0
b
f
b
8
d
8
6
7
3
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
o
w
n
'
:
 
6
0
0
,


 
 
 
 
 
 
 
 
'
E
r
r
o
r
'
:
 
8
0
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
e
d
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
i
n
g
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
d
'
:
 
5
0
0
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
i
n
g
'
:
 
4
8
0
,


 
 
 
 
 
 
 
 
'
T
i
m
e
d
O
u
t
A
b
n
o
r
m
a
l
l
y
'
:
 
5
1
3
,


 
 
 
 
 
 
 
 
'
T
i
m
e
d
O
u
t
K
i
l
l
e
d
'
:
 
5
1
2
,


 
 
 
 
 
 
 
 
'
U
n
d
e
f
i
n
e
d
'
:
 
0
}
 






c
l
a
s
s
 
G
u
e
s
t
S
e
s
s
i
o
n
W
a
i
t
F
o
r
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
s
e
s
s
i
o
n
 
w
a
i
t
i
n
g
 
f
l
a
g
s
.
 
M
u
l
t
i
p
l
e
 
f
l
a
g
s
 
c
a
n
 
b
e
 
c
o
m
b
i
n
e
d
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
b
b
7
a
3
7
2
a
-
f
6
3
5
-
4
e
1
1
-
a
8
1
a
-
e
7
0
7
f
3
a
5
2
e
f
5
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
t
a
t
u
s
'
:
 
4
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
'
:
 
2
}
 






c
l
a
s
s
 
G
u
e
s
t
S
e
s
s
i
o
n
W
a
i
t
R
e
s
u
l
t
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
s
e
s
s
i
o
n
 
w
a
i
t
i
n
g
 
r
e
s
u
l
t
s
.
 
D
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
s
e
s
s
i
o
n
 
w
a
i
t
i
n
g
 
f
l
a
g
s
 
(
f
o
r


 
 
 
 
 
 
m
o
r
e
 
i
n
f
o
r
m
a
t
i
o
n
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
G
u
e
s
t
S
e
s
s
i
o
n
W
a
i
t
F
o
r
F
l
a
g
"
/
>
)
 
t
h
e
 
w
a
i
t
i
n
g
 
r
e
s
u
l
t


 
 
 
 
 
 
c
a
n
 
v
a
r
y
 
b
a
s
e
d
 
o
n
 
t
h
e
 
s
e
s
s
i
o
n
'
s
 
c
u
r
r
e
n
t
 
s
t
a
t
u
s
.




 
 
 
 
 
 
T
o
 
w
a
i
t
 
f
o
r
 
a
 
g
u
e
s
t
 
s
e
s
s
i
o
n
 
t
o
 
t
e
r
m
i
n
a
t
e
 
a
f
t
e
r
 
i
t
 
h
a
s
 
b
e
e
n


 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
G
u
e
s
t
:
:
c
r
e
a
t
e
S
e
s
s
i
o
n
"
/
>
 
o
n
e
 
w
o
u
l
d
 
s
p
e
c
i
f
y


 
 
 
 
 
 
G
u
e
s
t
S
e
s
s
i
o
n
W
a
i
t
R
e
s
u
l
t
_
T
e
r
m
i
n
a
t
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
c
0
f
6
a
8
a
5
-
f
d
b
6
-
4
2
b
f
-
a
5
8
2
-
5
6
c
6
f
8
2
b
c
d
2
d
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
E
r
r
o
r
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
t
a
t
u
s
'
:
 
3
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
T
i
m
e
o
u
t
'
:
 
5
,


 
 
 
 
 
 
 
 
'
W
a
i
t
F
l
a
g
N
o
t
S
u
p
p
o
r
t
e
d
'
:
 
6
}
 






c
l
a
s
s
 
F
i
l
e
S
e
e
k
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
F
i
l
e
 
s
e
e
k
i
n
g
 
t
y
p
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
1
b
7
3
f
4
f
3
-
3
5
1
5
-
4
0
7
3
-
a
5
0
6
-
7
6
8
7
8
d
9
e
2
5
4
1
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
u
r
r
e
n
t
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
e
t
'
:
 
0
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
I
n
p
u
t
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
p
r
o
c
e
s
s
 
i
n
p
u
t
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
5
d
3
8
c
1
d
d
-
2
6
0
4
-
4
d
d
f
-
9
2
e
5
-
0
c
0
c
d
d
3
b
d
b
d
5
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
E
n
d
O
f
F
i
l
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
O
u
t
p
u
t
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
p
r
o
c
e
s
s
 
o
u
t
p
u
t
 
f
l
a
g
s
 
f
o
r
 
s
p
e
c
i
f
y
i
n
g
 
w
h
i
c
h


 
 
 
 
 
 
t
y
p
e
 
o
f
 
o
u
t
p
u
t
 
t
o
 
r
e
t
r
i
e
v
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
9
9
7
9
e
8
5
a
-
5
2
b
b
-
4
0
b
7
-
8
7
0
c
-
5
7
1
1
5
e
2
7
e
0
f
1
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
t
d
E
r
r
'
:
 
1
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
W
a
i
t
F
o
r
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
r
o
c
e
s
s
 
w
a
i
t
i
n
g
 
f
l
a
g
s
.
 
M
u
l
t
i
p
l
e
 
f
l
a
g
s
 
c
a
n
 
b
e
 
c
o
m
b
i
n
e
d
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
2
3
b
5
5
0
c
7
-
7
8
e
1
-
4
3
7
e
-
9
8
f
0
-
6
5
f
d
9
7
5
7
b
c
d
2
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
t
d
E
r
r
'
:
 
1
6
,


 
 
 
 
 
 
 
 
'
S
t
d
I
n
'
:
 
4
,


 
 
 
 
 
 
 
 
'
S
t
d
O
u
t
'
:
 
8
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
'
:
 
2
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
W
a
i
t
R
e
s
u
l
t
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
r
o
c
e
s
s
 
w
a
i
t
i
n
g
 
r
e
s
u
l
t
s
.
 
D
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
p
r
o
c
e
s
s
 
w
a
i
t
i
n
g
 
f
l
a
g
s
 
(
f
o
r


 
 
 
 
 
 
m
o
r
e
 
i
n
f
o
r
m
a
t
i
o
n
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
P
r
o
c
e
s
s
W
a
i
t
F
o
r
F
l
a
g
"
/
>
)
 
t
h
e
 
w
a
i
t
i
n
g
 
r
e
s
u
l
t


 
 
 
 
 
 
c
a
n
 
v
a
r
y
 
b
a
s
e
d
 
o
n
 
t
h
e
 
p
r
o
c
e
s
s
e
s
'
 
c
u
r
r
e
n
t
 
s
t
a
t
u
s
.




 
 
 
 
 
 
T
o
 
w
a
i
t
 
f
o
r
 
a
 
g
u
e
s
t
 
p
r
o
c
e
s
s
 
t
o
 
t
e
r
m
i
n
a
t
e
 
a
f
t
e
r
 
i
t
 
h
a
s
 
b
e
e
n


 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
G
u
e
s
t
S
e
s
s
i
o
n
:
:
p
r
o
c
e
s
s
C
r
e
a
t
e
"
/
>
 
o
r
 
<
l
i
n
k
 
t
o
=
"
I
G
u
e
s
t
S
e
s
s
i
o
n
:
:
p
r
o
c
e
s
s
C
r
e
a
t
e
E
x
"
/
>


 
 
 
 
 
 
o
n
e
 
w
o
u
l
d
 
s
p
e
c
i
f
y
 
P
r
o
c
e
s
s
W
a
i
t
R
e
s
u
l
t
_
T
e
r
m
i
n
a
t
e
.




 
 
 
 
 
 
I
f
 
a
 
g
u
e
s
t
 
p
r
o
c
e
s
s
 
h
a
s
 
b
e
e
n
 
s
t
a
r
t
e
d
 
w
i
t
h
 
P
r
o
c
e
s
s
C
r
e
a
t
e
F
l
a
g
_
W
a
i
t
F
o
r
S
t
d
O
u
t


 
 
 
 
 
 
a
 
c
l
i
e
n
t
 
c
a
n
 
w
a
i
t
 
w
i
t
h
 
P
r
o
c
e
s
s
W
a
i
t
R
e
s
u
l
t
_
S
t
d
O
u
t
 
f
o
r
 
n
e
w
 
d
a
t
a
 
t
o
 
a
r
r
i
v
e
 
o
n


 
 
 
 
 
 
s
t
d
o
u
t
;
 
s
a
m
e
 
a
p
p
l
i
e
s
 
f
o
r
 
P
r
o
c
e
s
s
C
r
e
a
t
e
F
l
a
g
_
W
a
i
t
F
o
r
S
t
d
E
r
r
 
a
n
d


 
 
 
 
 
 
P
r
o
c
e
s
s
W
a
i
t
R
e
s
u
l
t
_
S
t
d
E
r
r
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
4
0
7
1
9
c
b
e
-
f
1
9
2
-
4
f
e
9
-
a
2
3
1
-
6
6
9
7
b
3
c
8
e
2
b
4
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
E
r
r
o
r
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
t
a
t
u
s
'
:
 
3
,


 
 
 
 
 
 
 
 
'
S
t
d
E
r
r
'
:
 
8
,


 
 
 
 
 
 
 
 
'
S
t
d
I
n
'
:
 
6
,


 
 
 
 
 
 
 
 
'
S
t
d
O
u
t
'
:
 
7
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
T
i
m
e
o
u
t
'
:
 
5
,


 
 
 
 
 
 
 
 
'
W
a
i
t
F
l
a
g
N
o
t
S
u
p
p
o
r
t
e
d
'
:
 
9
}
 






c
l
a
s
s
 
C
o
p
y
F
i
l
e
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
F
i
l
e
 
c
o
p
y
i
n
g
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
2
3
f
7
9
f
d
f
-
7
3
8
a
-
4
9
3
d
-
b
8
0
b
-
4
2
d
6
0
7
c
9
b
9
1
6
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
F
o
l
l
o
w
L
i
n
k
s
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
R
e
c
u
r
s
i
v
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
U
p
d
a
t
e
'
:
 
2
}
 






c
l
a
s
s
 
D
i
r
e
c
t
o
r
y
C
r
e
a
t
e
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
D
i
r
e
c
t
o
r
y
 
c
r
e
a
t
i
o
n
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
b
d
7
2
1
b
0
e
-
c
e
d
5
-
4
f
7
9
-
b
3
6
8
-
2
4
9
8
9
7
c
3
2
a
3
6
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
P
a
r
e
n
t
s
'
:
 
1
}
 






c
l
a
s
s
 
D
i
r
e
c
t
o
r
y
R
e
m
o
v
e
R
e
c
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
D
i
r
e
c
t
o
r
y
 
r
e
c
u
r
s
i
v
e
 
r
e
m
o
v
e
m
e
n
t
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
4
5
5
a
a
b
f
0
-
7
6
9
2
-
4
8
f
6
-
9
0
6
1
-
f
2
1
5
7
9
b
6
5
7
6
9
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
o
n
t
e
n
t
A
n
d
D
i
r
'
:
 
1
,


 
 
 
 
 
 
 
 
'
C
o
n
t
e
n
t
O
n
l
y
'
:
 
2
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
}
 






c
l
a
s
s
 
P
a
t
h
R
e
n
a
m
e
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
a
t
h
 
r
e
n
a
m
i
n
g
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
f
3
b
a
a
0
9
f
-
c
7
5
8
-
4
5
3
d
-
b
9
1
c
-
c
7
7
8
7
d
7
6
3
5
1
d
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
R
e
p
l
a
c
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
o
S
y
m
l
i
n
k
s
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
R
e
p
l
a
c
e
'
:
 
2
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
C
r
e
a
t
e
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
G
u
e
s
t
 
p
r
o
c
e
s
s
 
e
x
e
c
u
t
i
o
n
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
5
1
9
2
7
9
9
-
b
f
d
e
-
4
0
5
d
-
9
b
e
a
-
c
7
3
5
a
b
9
9
9
8
e
4
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
E
x
p
a
n
d
A
r
g
u
m
e
n
t
s
'
:
 
6
4
,


 
 
 
 
 
 
 
 
'
H
i
d
d
e
n
'
:
 
4
,


 
 
 
 
 
 
 
 
'
I
g
n
o
r
e
O
r
p
h
a
n
e
d
P
r
o
c
e
s
s
e
s
'
:
 
2
,


 
 
 
 
 
 
 
 
'
N
o
P
r
o
f
i
l
e
'
:
 
8
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
W
a
i
t
F
o
r
P
r
o
c
e
s
s
S
t
a
r
t
O
n
l
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
W
a
i
t
F
o
r
S
t
d
E
r
r
'
:
 
3
2
,


 
 
 
 
 
 
 
 
'
W
a
i
t
F
o
r
S
t
d
O
u
t
'
:
 
1
6
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
P
r
i
o
r
i
t
y
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
r
o
c
e
s
s
 
p
r
i
o
r
i
t
i
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
e
e
8
c
a
c
5
0
-
e
2
3
2
-
4
9
f
e
-
8
0
6
b
-
d
1
2
1
4
d
9
c
2
e
4
9
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
e
f
a
u
l
t
'
:
 
1
,


 
 
 
 
 
 
 
 
'
I
n
v
a
l
i
d
'
:
 
0
}
 






c
l
a
s
s
 
S
y
m
l
i
n
k
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
S
y
m
b
o
l
i
c
 
l
i
n
k
 
t
y
p
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
7
7
9
4
6
6
8
-
f
8
f
1
-
4
7
1
4
-
9
8
a
5
-
6
f
8
f
a
2
e
d
0
1
1
8
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
i
r
e
c
t
o
r
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
F
i
l
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
U
n
k
n
o
w
n
'
:
 
0
}
 






c
l
a
s
s
 
S
y
m
l
i
n
k
R
e
a
d
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
S
y
m
b
o
l
i
c
 
l
i
n
k
 
r
e
a
d
i
n
g
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
b
7
f
e
2
b
9
d
-
7
9
0
e
-
4
b
2
5
-
8
a
d
f
-
1
c
a
3
3
0
2
6
9
3
1
f
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
S
y
m
l
i
n
k
s
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
S
t
a
t
u
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
r
o
c
e
s
s
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
u
s
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
4
d
5
2
3
6
8
f
-
5
b
4
8
-
4
b
f
e
-
b
4
8
6
-
a
c
f
8
9
1
3
9
b
5
2
f
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
o
w
n
'
:
 
6
0
0
,


 
 
 
 
 
 
 
 
'
E
r
r
o
r
'
:
 
8
0
0
,


 
 
 
 
 
 
 
 
'
P
a
u
s
e
d
'
:
 
1
1
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
e
d
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
S
t
a
r
t
i
n
g
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
d
A
b
n
o
r
m
a
l
l
y
'
:
 
5
1
1
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
d
N
o
r
m
a
l
l
y
'
:
 
5
0
0
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
e
d
S
i
g
n
a
l
'
:
 
5
1
0
,


 
 
 
 
 
 
 
 
'
T
e
r
m
i
n
a
t
i
n
g
'
:
 
4
8
0
,


 
 
 
 
 
 
 
 
'
T
i
m
e
d
O
u
t
A
b
n
o
r
m
a
l
l
y
'
:
 
5
1
3
,


 
 
 
 
 
 
 
 
'
T
i
m
e
d
O
u
t
K
i
l
l
e
d
'
:
 
5
1
2
,


 
 
 
 
 
 
 
 
'
U
n
d
e
f
i
n
e
d
'
:
 
0
}
 






c
l
a
s
s
 
P
r
o
c
e
s
s
I
n
p
u
t
S
t
a
t
u
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
r
o
c
e
s
s
 
i
n
p
u
t
 
s
t
a
t
u
s
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
a
4
a
0
e
f
9
c
-
2
9
c
c
-
4
8
0
5
-
9
8
0
3
-
c
8
2
1
5
a
e
9
d
a
6
c
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
v
a
i
l
a
b
l
e
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
B
r
o
k
e
n
'
:
 
1
,


 
 
 
 
 
 
 
 
'
O
v
e
r
f
l
o
w
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
U
n
d
e
f
i
n
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
W
r
i
t
t
e
n
'
:
 
5
0
}
 






c
l
a
s
s
 
F
i
l
e
S
t
a
t
u
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
F
i
l
e
 
s
t
a
t
u
s
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
8
c
8
6
4
6
8
b
-
b
9
7
b
-
4
0
8
0
-
8
9
1
4
-
e
2
9
f
5
b
0
a
b
d
2
c
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
l
o
s
e
d
'
:
 
2
0
0
,


 
 
 
 
 
 
 
 
'
C
l
o
s
i
n
g
'
:
 
1
5
0
,


 
 
 
 
 
 
 
 
'
D
o
w
n
'
:
 
6
0
0
,


 
 
 
 
 
 
 
 
'
E
r
r
o
r
'
:
 
8
0
0
,


 
 
 
 
 
 
 
 
'
O
p
e
n
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
O
p
e
n
i
n
g
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
U
n
d
e
f
i
n
e
d
'
:
 
0
}
 






c
l
a
s
s
 
F
s
O
b
j
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
F
i
l
e
 
s
y
s
t
e
m
 
o
b
j
e
c
t
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
a
1
e
d
4
3
7
c
-
b
3
c
3
-
4
c
a
2
-
b
1
9
c
-
4
2
3
9
d
6
5
8
d
5
e
8
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
e
v
B
l
o
c
k
'
:
 
1
1
,


 
 
 
 
 
 
 
 
'
D
e
v
C
h
a
r
'
:
 
1
0
,


 
 
 
 
 
 
 
 
'
D
i
r
e
c
t
o
r
y
'
:
 
5
0
,


 
 
 
 
 
 
 
 
'
F
I
F
O
'
:
 
1
,


 
 
 
 
 
 
 
 
'
F
i
l
e
'
:
 
8
0
,


 
 
 
 
 
 
 
 
'
S
o
c
k
e
t
'
:
 
2
0
0
,


 
 
 
 
 
 
 
 
'
S
y
m
l
i
n
k
'
:
 
1
0
0
,


 
 
 
 
 
 
 
 
'
U
n
d
e
f
i
n
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
W
h
i
t
e
o
u
t
'
:
 
4
0
0
}
 






c
l
a
s
s
 
D
r
a
g
A
n
d
D
r
o
p
A
c
t
i
o
n
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
o
s
s
i
b
l
e
 
a
c
t
i
o
n
s
 
w
i
t
h
i
n
 
a
n
 
D
r
a
g
 
a
n
d
 
D
r
o
p
 
o
p
e
r
a
t
i
o
n
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
4
7
f
3
b
1
6
2
-
c
1
0
7
-
4
f
c
d
-
b
f
a
7
-
5
4
b
8
1
3
5
c
4
4
1
e
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
o
p
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
I
g
n
o
r
e
'
:
 
0
,


 
 
 
 
 
 
 
 
'
L
i
n
k
'
:
 
3
,


 
 
 
 
 
 
 
 
'
M
o
v
e
'
:
 
2
}
 






c
l
a
s
s
 
D
i
r
e
c
t
o
r
y
O
p
e
n
F
l
a
g
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
D
i
r
e
c
t
o
r
y
 
o
p
e
n
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
5
1
3
8
8
3
7
a
-
8
f
d
2
-
4
1
9
4
-
a
1
b
0
-
0
8
f
7
b
c
3
9
4
9
d
0
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
N
o
S
y
m
l
i
n
k
s
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
}
 






c
l
a
s
s
 
M
e
d
i
u
m
S
t
a
t
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
 
m
e
d
i
u
m
 
s
t
a
t
e
.


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
e
f
4
1
e
9
8
0
-
e
0
1
2
-
4
3
c
d
-
9
d
e
a
-
4
7
9
d
4
e
f
1
4
d
1
3
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
C
r
e
a
t
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
C
r
e
a
t
i
n
g
'
:
 
5
,


 
 
 
 
 
 
 
 
'
D
e
l
e
t
i
n
g
'
:
 
6
,


 
 
 
 
 
 
 
 
'
I
n
a
c
c
e
s
s
i
b
l
e
'
:
 
4
,


 
 
 
 
 
 
 
 
'
L
o
c
k
e
d
R
e
a
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
L
o
c
k
e
d
W
r
i
t
e
'
:
 
3
,


 
 
 
 
 
 
 
 
'
N
o
t
C
r
e
a
t
e
d
'
:
 
0
}
 






c
l
a
s
s
 
M
e
d
i
u
m
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
 
m
e
d
i
u
m
 
t
y
p
e
.
 
F
o
r
 
e
a
c
h
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
,
 
t
h
i
s
 
d
e
f
i
n
e
s
 
h
o
w
 
t
h
e
 
m
e
d
i
u
m
 
i
s


 
 
 
 
 
 
a
t
t
a
c
h
e
d
 
t
o
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
"
/
>
)
 
a
n
d
 
w
h
a
t
 
h
a
p
p
e
n
s


 
 
 
 
 
 
w
h
e
n
 
a
 
s
n
a
p
s
h
o
t
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
"
/
>
)
 
i
s
 
t
a
k
e
n
 
o
f
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
w
h
i
c
h
 
h
a
s


 
 
 
 
 
 
t
h
e
 
m
e
d
i
u
m
 
a
t
t
a
c
h
e
d
.
 
A
t
 
t
h
e
 
m
o
m
e
n
t
 
D
V
D
 
a
n
d
 
f
l
o
p
p
y
 
m
e
d
i
a
 
a
r
e
 
a
l
w
a
y
s
 
o
f
 
t
y
p
e
 
"
w
r
i
t
e
t
h
r
o
u
g
h
"
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
f
e
6
6
3
f
b
5
-
c
2
4
4
-
4
e
1
b
-
9
d
8
1
-
c
6
2
8
b
4
1
7
d
d
0
4
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
I
m
m
u
t
a
b
l
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
M
u
l
t
i
A
t
t
a
c
h
'
:
 
5
,


 
 
 
 
 
 
 
 
'
N
o
r
m
a
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
R
e
a
d
o
n
l
y
'
:
 
4
,


 
 
 
 
 
 
 
 
'
S
h
a
r
e
a
b
l
e
'
:
 
3
,


 
 
 
 
 
 
 
 
'
W
r
i
t
e
t
h
r
o
u
g
h
'
:
 
2
}
 






c
l
a
s
s
 
M
e
d
i
u
m
V
a
r
i
a
n
t
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
 
m
e
d
i
u
m
 
i
m
a
g
e
 
v
a
r
i
a
n
t
.
 
M
o
r
e
 
t
h
a
n
 
o
n
e
 
f
l
a
g
 
m
a
y
 
b
e
 
s
e
t
.


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
8
0
6
8
5
b
6
b
-
e
4
2
f
-
4
9
7
d
-
8
2
7
1
-
e
7
7
b
f
3
c
6
1
a
d
a
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
i
f
f
'
:
 
1
3
1
0
7
2
,


 
 
 
 
 
 
 
 
'
F
i
x
e
d
'
:
 
6
5
5
3
6
,


 
 
 
 
 
 
 
 
'
N
o
C
r
e
a
t
e
D
i
r
'
:
 
1
0
7
3
7
4
1
8
2
4
,


 
 
 
 
 
 
 
 
'
S
t
a
n
d
a
r
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
V
m
d
k
E
S
X
'
:
 
8
,


 
 
 
 
 
 
 
 
'
V
m
d
k
R
a
w
D
i
s
k
'
:
 
2
,


 
 
 
 
 
 
 
 
'
V
m
d
k
S
p
l
i
t
2
G
'
:
 
1
,


 
 
 
 
 
 
 
 
'
V
m
d
k
S
t
r
e
a
m
O
p
t
i
m
i
z
e
d
'
:
 
4
}
 






c
l
a
s
s
 
D
a
t
a
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
d
9
0
e
a
5
1
e
-
a
3
f
1
-
4
a
0
1
-
b
e
b
1
-
c
1
7
2
3
c
0
d
3
b
a
7
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
I
n
t
3
2
'
:
 
0
,


 
 
 
 
 
 
 
 
'
I
n
t
8
'
:
 
1
,


 
 
 
 
 
 
 
 
'
S
t
r
i
n
g
'
:
 
2
}
 






c
l
a
s
s
 
D
a
t
a
F
l
a
g
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
8
6
8
8
4
d
c
f
-
1
d
6
b
-
4
f
1
b
-
b
4
b
f
-
f
5
a
a
4
4
9
5
9
d
6
0
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
r
r
a
y
'
:
 
4
,


 
 
 
 
 
 
 
 
'
E
x
p
e
r
t
'
:
 
2
,


 
 
 
 
 
 
 
 
'
F
l
a
g
M
a
s
k
'
:
 
7
,


 
 
 
 
 
 
 
 
'
M
a
n
d
a
t
o
r
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
o
n
e
'
:
 
0
}
 






c
l
a
s
s
 
M
e
d
i
u
m
F
o
r
m
a
t
C
a
p
a
b
i
l
i
t
i
e
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
M
e
d
i
u
m
 
f
o
r
m
a
t
 
c
a
p
a
b
i
l
i
t
y
 
f
l
a
g
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
3
4
2
b
a
7
9
-
7
c
e
0
-
4
d
9
4
-
8
f
8
6
-
5
e
d
5
a
1
8
5
d
9
b
d
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
s
y
n
c
h
r
o
n
o
u
s
'
:
 
3
2
,


 
 
 
 
 
 
 
 
'
C
a
p
a
b
i
l
i
t
y
M
a
s
k
'
:
 
1
0
2
3
,


 
 
 
 
 
 
 
 
'
C
r
e
a
t
e
D
y
n
a
m
i
c
'
:
 
4
,


 
 
 
 
 
 
 
 
'
C
r
e
a
t
e
F
i
x
e
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
C
r
e
a
t
e
S
p
l
i
t
2
G
'
:
 
8
,


 
 
 
 
 
 
 
 
'
D
i
f
f
e
r
e
n
c
i
n
g
'
:
 
1
6
,


 
 
 
 
 
 
 
 
'
F
i
l
e
'
:
 
6
4
,


 
 
 
 
 
 
 
 
'
P
r
o
p
e
r
t
i
e
s
'
:
 
1
2
8
,


 
 
 
 
 
 
 
 
'
T
c
p
N
e
t
w
o
r
k
i
n
g
'
:
 
2
5
6
,


 
 
 
 
 
 
 
 
'
U
u
i
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
V
F
S
'
:
 
5
1
2
}
 






c
l
a
s
s
 
M
o
u
s
e
B
u
t
t
o
n
S
t
a
t
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
M
o
u
s
e
 
b
u
t
t
o
n
 
s
t
a
t
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
9
e
e
0
9
4
b
8
-
b
2
8
a
-
4
d
5
6
-
a
1
6
6
-
9
7
3
c
b
5
8
8
d
7
f
8
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
L
e
f
t
B
u
t
t
o
n
'
:
 
1
,


 
 
 
 
 
 
 
 
'
M
i
d
d
l
e
B
u
t
t
o
n
'
:
 
4
,


 
 
 
 
 
 
 
 
'
M
o
u
s
e
S
t
a
t
e
M
a
s
k
'
:
 
1
2
7
,


 
 
 
 
 
 
 
 
'
R
i
g
h
t
B
u
t
t
o
n
'
:
 
2
,


 
 
 
 
 
 
 
 
'
W
h
e
e
l
D
o
w
n
'
:
 
1
6
,


 
 
 
 
 
 
 
 
'
W
h
e
e
l
U
p
'
:
 
8
,


 
 
 
 
 
 
 
 
'
X
B
u
t
t
o
n
1
'
:
 
3
2
,


 
 
 
 
 
 
 
 
'
X
B
u
t
t
o
n
2
'
:
 
6
4
}
 






c
l
a
s
s
 
F
r
a
m
e
b
u
f
f
e
r
P
i
x
e
l
F
o
r
m
a
t
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
F
o
r
m
a
t
 
o
f
 
t
h
e
 
v
i
d
e
o
 
m
e
m
o
r
y
 
b
u
f
f
e
r
.
 
C
o
n
s
t
a
n
t
s
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
t
h
i
s
 
e
n
u
m
 
c
a
n


 
 
 
 
 
 
b
e
 
u
s
e
d
 
t
o
 
t
e
s
t
 
f
o
r
 
p
a
r
t
i
c
u
l
a
r
 
v
a
l
u
e
s
 
o
f
 
<
l
i
n
k
 
t
o
=
"
I
F
r
a
m
e
b
u
f
f
e
r
:
:
p
i
x
e
l
F
o
r
m
a
t
"
/
>
.
 
S
e
e
 
a
l
s
o
 
<
l
i
n
k
 
t
o
=
"
I
F
r
a
m
e
b
u
f
f
e
r
:
:
r
e
q
u
e
s
t
R
e
s
i
z
e
"
/
>
.




 
 
 
 
 
 
S
e
e
 
a
l
s
o
 
w
w
w
.
f
o
u
r
c
c
.
o
r
g
 
f
o
r
 
m
o
r
e
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
F
O
U
R
C
C
 
p
i
x
e
l
 
f
o
r
m
a
t
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
a
c
f
d
5
e
d
-
2
9
e
3
-
4
5
e
3
-
8
1
3
6
-
7
3
c
9
2
2
4
f
3
d
2
d
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
F
O
U
R
C
C
_
R
G
B
'
:
 
8
4
3
2
0
4
4
3
4
,


 
 
 
 
 
 
 
 
'
O
p
a
q
u
e
'
:
 
0
}
 






c
l
a
s
s
 
N
e
t
w
o
r
k
A
t
t
a
c
h
m
e
n
t
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
N
e
t
w
o
r
k
 
a
t
t
a
c
h
m
e
n
t
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
2
a
c
4
b
c
7
1
-
6
b
8
2
-
4
1
7
a
-
a
c
d
1
-
f
7
4
2
6
d
2
5
7
0
d
6
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
B
r
i
d
g
e
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
G
e
n
e
r
i
c
'
:
 
5
,


 
 
 
 
 
 
 
 
'
H
o
s
t
O
n
l
y
'
:
 
4
,


 
 
 
 
 
 
 
 
'
I
n
t
e
r
n
a
l
'
:
 
3
,


 
 
 
 
 
 
 
 
'
N
A
T
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
}
 






c
l
a
s
s
 
N
e
t
w
o
r
k
A
d
a
p
t
e
r
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
N
e
t
w
o
r
k
 
a
d
a
p
t
e
r
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
c
2
2
8
1
e
4
-
d
9
5
2
-
4
e
8
7
-
8
c
7
d
-
2
4
3
7
9
c
b
6
a
8
1
c
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
m
7
9
C
9
7
0
A
'
:
 
1
,


 
 
 
 
 
 
 
 
'
A
m
7
9
C
9
7
3
'
:
 
2
,


 
 
 
 
 
 
 
 
'
I
8
2
5
4
0
E
M
'
:
 
3
,


 
 
 
 
 
 
 
 
'
I
8
2
5
4
3
G
C
'
:
 
4
,


 
 
 
 
 
 
 
 
'
I
8
2
5
4
5
E
M
'
:
 
5
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
V
i
r
t
i
o
'
:
 
6
}
 






c
l
a
s
s
 
N
e
t
w
o
r
k
A
d
a
p
t
e
r
P
r
o
m
i
s
c
M
o
d
e
P
o
l
i
c
y
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
h
e
 
p
r
o
m
i
s
c
u
o
u
s
 
m
o
d
e
 
p
o
l
i
c
y
 
o
f
 
a
n
 
i
n
t
e
r
f
a
c
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
c
9
6
3
7
6
8
a
-
3
7
6
f
-
4
c
8
5
-
8
d
8
4
-
d
8
c
e
d
4
b
7
2
6
9
e
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
l
l
o
w
A
l
l
'
:
 
3
,


 
 
 
 
 
 
 
 
'
A
l
l
o
w
N
e
t
w
o
r
k
'
:
 
2
,


 
 
 
 
 
 
 
 
'
D
e
n
y
'
:
 
1
}
 






c
l
a
s
s
 
P
o
r
t
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
h
e
 
P
o
r
t
M
o
d
e
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
p
o
s
s
i
b
l
e
 
c
o
m
m
u
n
i
c
a
t
i
o
n
 
m
o
d
e
s
 
f
o
r


 
 
 
 
 
 
t
h
e
 
v
i
r
t
u
a
l
 
s
e
r
i
a
l
 
p
o
r
t
 
d
e
v
i
c
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
5
3
3
b
5
f
e
3
-
0
1
8
5
-
4
1
9
7
-
8
6
a
7
-
1
7
e
3
7
d
d
3
9
d
7
6
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
i
s
c
o
n
n
e
c
t
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
H
o
s
t
D
e
v
i
c
e
'
:
 
2
,


 
 
 
 
 
 
 
 
'
H
o
s
t
P
i
p
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
R
a
w
F
i
l
e
'
:
 
3
}
 






c
l
a
s
s
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
U
S
B
 
d
e
v
i
c
e
 
s
t
a
t
e
.
 
T
h
i
s
 
e
n
u
m
e
r
a
t
i
o
n
 
r
e
p
r
e
s
e
n
t
s
 
a
l
l
 
p
o
s
s
i
b
l
e
 
s
t
a
t
e
s


 
 
 
 
 
 
o
f
 
t
h
e
 
U
S
B
 
d
e
v
i
c
e
 
p
h
y
s
i
c
a
l
l
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
 
r
e
g
a
r
d
i
n
g


 
 
 
 
 
 
i
t
s
 
s
t
a
t
e
 
o
n
 
t
h
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
 
a
n
d
 
a
v
a
i
l
a
b
i
l
i
t
y
 
t
o
 
g
u
e
s
t
 
c
o
m
p
u
t
e
r
s


 
 
 
 
 
 
(
a
l
l
 
c
u
r
r
e
n
t
l
y
 
r
u
n
n
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
)
.




 
 
 
 
 
 
O
n
c
e
 
a
 
s
u
p
p
o
r
t
e
d
 
U
S
B
 
d
e
v
i
c
e
 
i
s
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
,
 
g
l
o
b
a
l
 
U
S
B


 
 
 
 
 
 
f
i
l
t
e
r
s
 
(
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
:
:
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>
)
 
a
r
e
 
a
c
t
i
v
a
t
e
d
.
 
T
h
e
y
 
c
a
n


 
 
 
 
 
 
e
i
t
h
e
r
 
i
g
n
o
r
e
 
t
h
e
 
d
e
v
i
c
e
,
 
o
r
 
p
u
t
 
i
t
 
t
o
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
H
e
l
d
 
s
t
a
t
e
,
 
o
r
 
d
o


 
 
 
 
 
 
n
o
t
h
i
n
g
.
 
U
n
l
e
s
s
 
t
h
e
 
d
e
v
i
c
e
 
i
s
 
i
g
n
o
r
e
d
 
b
y
 
g
l
o
b
a
l
 
f
i
l
t
e
r
s
,
 
f
i
l
t
e
r
s
 
o
f
 
a
l
l


 
 
 
 
 
 
c
u
r
r
e
n
t
l
y
 
r
u
n
n
i
n
g
 
g
u
e
s
t
s
 
(
<
l
i
n
k
 
t
o
=
"
I
U
S
B
C
o
n
t
r
o
l
l
e
r
:
:
d
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>
)
 
a
r
e


 
 
 
 
 
 
a
c
t
i
v
a
t
e
d
 
t
h
a
t
 
c
a
n
 
p
u
t
 
i
t
 
t
o
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
C
a
p
t
u
r
e
d
 
s
t
a
t
e
.




 
 
 
 
 
 
I
f
 
t
h
e
 
d
e
v
i
c
e
 
w
a
s
 
i
g
n
o
r
e
d
 
b
y
 
g
l
o
b
a
l
 
f
i
l
t
e
r
s
,
 
o
r
 
d
i
d
n
'
t
 
m
a
t
c
h


 
 
 
 
 
 
a
n
y
 
f
i
l
t
e
r
s
 
a
t
 
a
l
l
 
(
i
n
c
l
u
d
i
n
g
 
g
u
e
s
t
 
o
n
e
s
)
,
 
i
t
 
i
s
 
h
a
n
d
l
e
d
 
b
y
 
t
h
e
 
h
o
s
t


 
 
 
 
 
 
i
n
 
a
 
n
o
r
m
a
l
 
w
a
y
.
 
I
n
 
t
h
i
s
 
c
a
s
e
,
 
t
h
e
 
d
e
v
i
c
e
 
s
t
a
t
e
 
i
s
 
d
e
t
e
r
m
i
n
e
d
 
b
y


 
 
 
 
 
 
t
h
e
 
h
o
s
t
 
a
n
d
 
c
a
n
 
b
e
 
o
n
e
 
o
f
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
U
n
a
v
a
i
l
a
b
l
e
,
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
B
u
s
y


 
 
 
 
 
 
o
r
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
A
v
a
i
l
a
b
l
e
,
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
c
u
r
r
e
n
t
 
d
e
v
i
c
e
 
u
s
a
g
e
.




 
 
 
 
 
 
B
e
s
i
d
e
s
 
a
u
t
o
-
c
a
p
t
u
r
i
n
g
 
b
a
s
e
d
 
o
n
 
f
i
l
t
e
r
s
,
 
t
h
e
 
d
e
v
i
c
e
 
c
a
n
 
b
e
 
m
a
n
u
a
l
l
y


 
 
 
 
 
 
c
a
p
t
u
r
e
d
 
b
y
 
g
u
e
s
t
s
 
(
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
a
t
t
a
c
h
U
S
B
D
e
v
i
c
e
"
/
>
)
 
i
f
 
i
t
s


 
 
 
 
 
 
s
t
a
t
e
 
i
s
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
B
u
s
y
,
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
A
v
a
i
l
a
b
l
e
 
o
r


 
 
 
 
 
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
H
e
l
d
.




 
 
 
 
 
 


 
 
 
 
 
 
 
 
D
u
e
 
t
o
 
d
i
f
f
e
r
e
n
c
e
s
 
i
n
 
U
S
B
 
s
t
a
c
k
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
s
 
i
n
 
L
i
n
u
x
 
a
n
d
 
W
i
n
3
2
,


 
 
 
 
 
 
 
 
s
t
a
t
e
s
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
B
u
s
y
 
a
n
d
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
U
n
a
v
a
i
l
a
b
l
e
 
a
r
e
 
a
p
p
l
i
c
a
b
l
e


 
 
 
 
 
 
 
 
o
n
l
y
 
t
o
 
t
h
e
 
L
i
n
u
x
 
v
e
r
s
i
o
n
 
o
f
 
t
h
e
 
p
r
o
d
u
c
t
.
 
T
h
i
s
 
a
l
s
o
 
m
e
a
n
s
 
t
h
a
t
 
(
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
a
t
t
a
c
h
U
S
B
D
e
v
i
c
e
"
/
>
)
 
c
a
n
 
o
n
l
y
 
s
u
c
c
e
e
d
 
o
n
 
W
i
n
3
2
 
i
f
 
t
h
e


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
s
t
a
t
e
 
i
s
 
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
H
e
l
d
.


 
 
 
 
 
 




 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
U
S
B
D
e
v
i
c
e
"
/
>
,
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
"
/
>
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
b
9
9
a
2
e
6
5
-
6
7
f
b
-
4
8
8
2
-
8
2
f
d
-
f
3
e
5
e
8
1
9
3
a
b
4
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
v
a
i
l
a
b
l
e
'
:
 
3
,


 
 
 
 
 
 
 
 
'
B
u
s
y
'
:
 
2
,


 
 
 
 
 
 
 
 
'
C
a
p
t
u
r
e
d
'
:
 
5
,


 
 
 
 
 
 
 
 
'
H
e
l
d
'
:
 
4
,


 
 
 
 
 
 
 
 
'
N
o
t
S
u
p
p
o
r
t
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
U
n
a
v
a
i
l
a
b
l
e
'
:
 
1
}
 






c
l
a
s
s
 
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
A
c
t
i
o
n
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
A
c
t
i
o
n
s
 
f
o
r
 
h
o
s
t
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
s
.


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
"
/
>
,
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
"
/
>
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
c
b
c
3
0
a
4
9
-
2
f
4
e
-
4
3
b
5
-
9
d
a
6
-
1
2
1
3
2
0
4
7
5
9
3
3
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
H
o
l
d
'
:
 
2
,


 
 
 
 
 
 
 
 
'
I
g
n
o
r
e
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
}
 






c
l
a
s
s
 
A
u
d
i
o
D
r
i
v
e
r
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
H
o
s
t
 
a
u
d
i
o
 
d
r
i
v
e
r
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
4
b
c
c
3
d
7
3
-
c
2
f
e
-
4
0
d
b
-
b
7
2
f
-
0
c
2
c
a
9
d
6
8
4
9
6
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
L
S
A
'
:
 
3
,


 
 
 
 
 
 
 
 
'
C
o
r
e
A
u
d
i
o
'
:
 
5
,


 
 
 
 
 
 
 
 
'
D
i
r
e
c
t
S
o
u
n
d
'
:
 
4
,


 
 
 
 
 
 
 
 
'
M
M
P
M
'
:
 
6
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
O
S
S
'
:
 
2
,


 
 
 
 
 
 
 
 
'
P
u
l
s
e
'
:
 
7
,


 
 
 
 
 
 
 
 
'
S
o
l
A
u
d
i
o
'
:
 
8
,


 
 
 
 
 
 
 
 
'
W
i
n
M
M
'
:
 
1
}
 






c
l
a
s
s
 
A
u
d
i
o
C
o
n
t
r
o
l
l
e
r
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
 
a
u
d
i
o
 
c
o
n
t
r
o
l
l
e
r
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
a
f
d
3
9
5
c
-
4
2
c
3
-
4
4
4
e
-
8
7
8
8
-
3
c
e
8
0
2
9
2
f
3
6
c
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
C
9
7
'
:
 
0
,


 
 
 
 
 
 
 
 
'
H
D
A
'
:
 
2
,


 
 
 
 
 
 
 
 
'
S
B
1
6
'
:
 
1
}
 






c
l
a
s
s
 
A
u
t
h
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
V
i
r
t
u
a
l
B
o
x
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
 
t
y
p
e
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
e
e
f
6
e
f
6
-
9
8
c
2
-
4
d
c
2
-
a
b
3
5
-
1
0
d
2
b
2
9
2
0
2
8
d
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
E
x
t
e
r
n
a
l
'
:
 
1
,


 
 
 
 
 
 
 
 
'
G
u
e
s
t
'
:
 
2
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
}
 






c
l
a
s
s
 
S
t
o
r
a
g
e
B
u
s
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
h
e
 
b
u
s
 
t
y
p
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
(
I
D
E
,
 
S
A
T
A
,
 
S
C
S
I
,
 
S
A
S
 
o
r
 
F
l
o
p
p
y
)
;


 
 
 
 
 
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
:
:
b
u
s
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
e
e
e
6
7
a
b
3
-
6
6
8
d
-
4
e
f
5
-
9
1
e
0
-
7
0
2
5
f
e
4
a
0
d
7
a
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
F
l
o
p
p
y
'
:
 
4
,


 
 
 
 
 
 
 
 
'
I
D
E
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
S
A
S
'
:
 
5
,


 
 
 
 
 
 
 
 
'
S
A
T
A
'
:
 
2
,


 
 
 
 
 
 
 
 
'
S
C
S
I
'
:
 
3
}
 






c
l
a
s
s
 
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
h
e
 
e
x
a
c
t
 
v
a
r
i
a
n
t
 
o
f
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
h
a
r
d
w
a
r
e
 
p
r
e
s
e
n
t
e
d


 
 
 
 
 
 
t
o
 
t
h
e
 
g
u
e
s
t
;
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
:
:
c
o
n
t
r
o
l
l
e
r
T
y
p
e
"
/
>
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
8
a
4
1
2
b
8
a
-
f
4
3
e
-
4
4
5
6
-
b
d
3
7
-
b
4
7
4
f
0
8
7
9
a
5
8
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
B
u
s
L
o
g
i
c
'
:
 
2
,


 
 
 
 
 
 
 
 
'
I
8
2
0
7
8
'
:
 
7
,


 
 
 
 
 
 
 
 
'
I
C
H
6
'
:
 
6
,


 
 
 
 
 
 
 
 
'
I
n
t
e
l
A
h
c
i
'
:
 
3
,


 
 
 
 
 
 
 
 
'
L
s
i
L
o
g
i
c
'
:
 
1
,


 
 
 
 
 
 
 
 
'
L
s
i
L
o
g
i
c
S
a
s
'
:
 
8
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
P
I
I
X
3
'
:
 
4
,


 
 
 
 
 
 
 
 
'
P
I
I
X
4
'
:
 
5
}
 






c
l
a
s
s
 
C
h
i
p
s
e
t
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
y
p
e
 
o
f
 
e
m
u
l
a
t
e
d
 
c
h
i
p
s
e
t
 
(
m
o
s
t
l
y
 
s
o
u
t
h
b
r
i
d
g
e
)
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
8
b
4
0
9
6
a
8
-
a
7
c
3
-
4
d
3
b
-
b
b
b
1
-
0
5
a
0
a
5
1
e
c
3
9
4
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
I
C
H
9
'
:
 
2
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
,


 
 
 
 
 
 
 
 
'
P
I
I
X
3
'
:
 
1
}
 






c
l
a
s
s
 
N
A
T
A
l
i
a
s
M
o
d
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
<
d
e
s
c
/
>
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
7
7
7
2
1
6
8
-
5
0
d
9
-
1
1
d
f
-
9
6
6
9
-
7
f
b
7
1
4
e
e
4
f
a
1
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
l
i
a
s
L
o
g
'
:
 
1
,


 
 
 
 
 
 
 
 
'
A
l
i
a
s
P
r
o
x
y
O
n
l
y
'
:
 
2
,


 
 
 
 
 
 
 
 
'
A
l
i
a
s
U
s
e
S
a
m
e
P
o
r
t
s
'
:
 
4
}
 






c
l
a
s
s
 
N
A
T
P
r
o
t
o
c
o
l
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
P
r
o
t
o
c
o
l
 
d
e
f
i
n
i
t
i
o
n
s
 
u
s
e
d
 
w
i
t
h
 
N
A
T
 
p
o
r
t
-
f
o
r
w
a
r
d
i
n
g
 
r
u
l
e
s
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
e
9
0
1
6
4
b
e
-
e
b
0
3
-
1
1
d
e
-
9
4
a
f
-
f
f
f
9
b
1
c
1
b
1
9
f
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
T
C
P
'
:
 
1
,


 
 
 
 
 
 
 
 
'
U
D
P
'
:
 
0
}
 






c
l
a
s
s
 
B
a
n
d
w
i
d
t
h
G
r
o
u
p
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
y
p
e
 
o
f
 
a
 
b
a
n
d
w
i
d
t
h
 
c
o
n
t
r
o
l
 
g
r
o
u
p
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
1
d
9
2
b
6
7
d
-
d
c
6
9
-
4
b
e
9
-
a
d
4
c
-
9
3
a
0
1
e
1
e
0
c
8
e
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
i
s
k
'
:
 
1
,


 
 
 
 
 
 
 
 
'
N
e
t
w
o
r
k
'
:
 
2
,


 
 
 
 
 
 
 
 
'
N
u
l
l
'
:
 
0
}
 






c
l
a
s
s
 
V
B
o
x
E
v
e
n
t
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
T
y
p
e
 
o
f
 
a
n
 
e
v
e
n
t
.


 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
E
v
e
n
t
"
/
>
 
f
o
r
 
a
n
 
i
n
t
r
o
d
u
c
t
i
o
n
 
t
o
 
V
i
r
t
u
a
l
B
o
x
 
e
v
e
n
t
 
h
a
n
d
l
i
n
g
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
c
5
1
6
4
5
b
3
-
7
1
0
8
-
4
d
c
e
-
b
5
a
3
-
b
b
f
5
e
4
f
6
9
e
d
2
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
A
n
y
'
:
 
1
,


 
 
 
 
 
 
 
 
'
I
n
p
u
t
E
v
e
n
t
'
:
 
5
,


 
 
 
 
 
 
 
 
'
I
n
v
a
l
i
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
L
a
s
t
'
:
 
9
1
,


 
 
 
 
 
 
 
 
'
L
a
s
t
W
i
l
d
c
a
r
d
'
:
 
3
1
,


 
 
 
 
 
 
 
 
'
M
a
c
h
i
n
e
E
v
e
n
t
'
:
 
3
,


 
 
 
 
 
 
 
 
'
O
n
A
d
d
i
t
i
o
n
s
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
4
7
,


 
 
 
 
 
 
 
 
'
O
n
B
a
n
d
w
i
d
t
h
G
r
o
u
p
C
h
a
n
g
e
d
'
:
 
6
9
,


 
 
 
 
 
 
 
 
'
O
n
C
P
U
C
h
a
n
g
e
d
'
:
 
6
0
,


 
 
 
 
 
 
 
 
'
O
n
C
P
U
E
x
e
c
u
t
i
o
n
C
a
p
C
h
a
n
g
e
d
'
:
 
6
3
,


 
 
 
 
 
 
 
 
'
O
n
C
a
n
S
h
o
w
W
i
n
d
o
w
'
:
 
5
8
,


 
 
 
 
 
 
 
 
'
O
n
C
l
i
p
b
o
a
r
d
M
o
d
e
C
h
a
n
g
e
d
'
:
 
7
2
,


 
 
 
 
 
 
 
 
'
O
n
D
r
a
g
A
n
d
D
r
o
p
M
o
d
e
C
h
a
n
g
e
d
'
:
 
7
3
,


 
 
 
 
 
 
 
 
'
O
n
E
v
e
n
t
S
o
u
r
c
e
C
h
a
n
g
e
d
'
:
 
6
2
,


 
 
 
 
 
 
 
 
'
O
n
E
x
t
r
a
D
a
t
a
C
a
n
C
h
a
n
g
e
'
:
 
3
5
,


 
 
 
 
 
 
 
 
'
O
n
E
x
t
r
a
D
a
t
a
C
h
a
n
g
e
d
'
:
 
3
4
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
F
i
l
e
O
f
f
s
e
t
C
h
a
n
g
e
d
'
:
 
8
8
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
F
i
l
e
R
e
a
d
'
:
 
8
9
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
F
i
l
e
R
e
g
i
s
t
e
r
e
d
'
:
 
8
6
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
F
i
l
e
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
8
7
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
F
i
l
e
W
r
i
t
e
'
:
 
9
0
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
K
e
y
b
o
a
r
d
'
:
 
6
4
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
M
o
n
i
t
o
r
C
h
a
n
g
e
d
'
:
 
7
0
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
M
o
u
s
e
'
:
 
6
5
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
P
r
o
c
e
s
s
I
n
p
u
t
N
o
t
i
f
y
'
:
 
8
4
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
P
r
o
c
e
s
s
O
u
t
p
u
t
'
:
 
8
5
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
P
r
o
c
e
s
s
R
e
g
i
s
t
e
r
e
d
'
:
 
8
2
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
P
r
o
c
e
s
s
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
8
3
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
P
r
o
p
e
r
t
y
C
h
a
n
g
e
d
'
:
 
4
2
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
S
e
s
s
i
o
n
R
e
g
i
s
t
e
r
e
d
'
:
 
8
1
,


 
 
 
 
 
 
 
 
'
O
n
G
u
e
s
t
S
e
s
s
i
o
n
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
8
0
,


 
 
 
 
 
 
 
 
'
O
n
H
o
s
t
P
C
I
D
e
v
i
c
e
P
l
u
g
'
:
 
6
7
,


 
 
 
 
 
 
 
 
'
O
n
K
e
y
b
o
a
r
d
L
e
d
s
C
h
a
n
g
e
d
'
:
 
4
5
,


 
 
 
 
 
 
 
 
'
O
n
M
a
c
h
i
n
e
D
a
t
a
C
h
a
n
g
e
d
'
:
 
3
3
,


 
 
 
 
 
 
 
 
'
O
n
M
a
c
h
i
n
e
R
e
g
i
s
t
e
r
e
d
'
:
 
3
7
,


 
 
 
 
 
 
 
 
'
O
n
M
a
c
h
i
n
e
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
3
2
,


 
 
 
 
 
 
 
 
'
O
n
M
e
d
i
u
m
C
h
a
n
g
e
d
'
:
 
5
2
,


 
 
 
 
 
 
 
 
'
O
n
M
e
d
i
u
m
R
e
g
i
s
t
e
r
e
d
'
:
 
3
6
,


 
 
 
 
 
 
 
 
'
O
n
M
o
u
s
e
C
a
p
a
b
i
l
i
t
y
C
h
a
n
g
e
d
'
:
 
4
4
,


 
 
 
 
 
 
 
 
'
O
n
M
o
u
s
e
P
o
i
n
t
e
r
S
h
a
p
e
C
h
a
n
g
e
d
'
:
 
4
3
,


 
 
 
 
 
 
 
 
'
O
n
N
A
T
N
e
t
w
o
r
k
A
l
t
e
r
'
:
 
7
6
,


 
 
 
 
 
 
 
 
'
O
n
N
A
T
N
e
t
w
o
r
k
C
h
a
n
g
e
d
'
:
 
7
4
,


 
 
 
 
 
 
 
 
'
O
n
N
A
T
N
e
t
w
o
r
k
C
r
e
a
t
i
o
n
D
e
l
e
t
i
o
n
'
:
 
7
7
,


 
 
 
 
 
 
 
 
'
O
n
N
A
T
N
e
t
w
o
r
k
P
o
r
t
F
o
r
w
a
r
d
'
:
 
7
9
,


 
 
 
 
 
 
 
 
'
O
n
N
A
T
N
e
t
w
o
r
k
S
e
t
t
i
n
g
'
:
 
7
8
,


 
 
 
 
 
 
 
 
'
O
n
N
A
T
N
e
t
w
o
r
k
S
t
a
r
t
S
t
o
p
'
:
 
7
5
,


 
 
 
 
 
 
 
 
'
O
n
N
A
T
R
e
d
i
r
e
c
t
'
:
 
6
6
,


 
 
 
 
 
 
 
 
'
O
n
N
e
t
w
o
r
k
A
d
a
p
t
e
r
C
h
a
n
g
e
d
'
:
 
4
8
,


 
 
 
 
 
 
 
 
'
O
n
P
a
r
a
l
l
e
l
P
o
r
t
C
h
a
n
g
e
d
'
:
 
5
0
,


 
 
 
 
 
 
 
 
'
O
n
R
u
n
t
i
m
e
E
r
r
o
r
'
:
 
5
7
,


 
 
 
 
 
 
 
 
'
O
n
S
e
r
i
a
l
P
o
r
t
C
h
a
n
g
e
d
'
:
 
4
9
,


 
 
 
 
 
 
 
 
'
O
n
S
e
s
s
i
o
n
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
3
8
,


 
 
 
 
 
 
 
 
'
O
n
S
h
a
r
e
d
F
o
l
d
e
r
C
h
a
n
g
e
d
'
:
 
5
6
,


 
 
 
 
 
 
 
 
'
O
n
S
h
o
w
W
i
n
d
o
w
'
:
 
5
9
,


 
 
 
 
 
 
 
 
'
O
n
S
n
a
p
s
h
o
t
C
h
a
n
g
e
d
'
:
 
4
1
,


 
 
 
 
 
 
 
 
'
O
n
S
n
a
p
s
h
o
t
D
e
l
e
t
e
d
'
:
 
4
0
,


 
 
 
 
 
 
 
 
'
O
n
S
n
a
p
s
h
o
t
T
a
k
e
n
'
:
 
3
9
,


 
 
 
 
 
 
 
 
'
O
n
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
4
6
,


 
 
 
 
 
 
 
 
'
O
n
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
C
h
a
n
g
e
d
'
:
 
5
1
,


 
 
 
 
 
 
 
 
'
O
n
S
t
o
r
a
g
e
D
e
v
i
c
e
C
h
a
n
g
e
d
'
:
 
7
1
,


 
 
 
 
 
 
 
 
'
O
n
U
S
B
C
o
n
t
r
o
l
l
e
r
C
h
a
n
g
e
d
'
:
 
5
4
,


 
 
 
 
 
 
 
 
'
O
n
U
S
B
D
e
v
i
c
e
S
t
a
t
e
C
h
a
n
g
e
d
'
:
 
5
5
,


 
 
 
 
 
 
 
 
'
O
n
V
B
o
x
S
V
C
A
v
a
i
l
a
b
i
l
i
t
y
C
h
a
n
g
e
d
'
:
 
6
8
,


 
 
 
 
 
 
 
 
'
O
n
V
R
D
E
S
e
r
v
e
r
C
h
a
n
g
e
d
'
:
 
5
3
,


 
 
 
 
 
 
 
 
'
O
n
V
R
D
E
S
e
r
v
e
r
I
n
f
o
C
h
a
n
g
e
d
'
:
 
6
1
,


 
 
 
 
 
 
 
 
'
S
n
a
p
s
h
o
t
E
v
e
n
t
'
:
 
4
,


 
 
 
 
 
 
 
 
'
V
e
t
o
a
b
l
e
'
:
 
2
}
 






c
l
a
s
s
 
G
u
e
s
t
M
o
n
i
t
o
r
C
h
a
n
g
e
d
E
v
e
n
t
T
y
p
e
(
E
n
u
m
)
:


 
 
 
 
"
"
"
(
H
o
w
 
t
h
e
 
g
u
e
s
t
 
m
o
n
i
t
o
r
 
h
a
s
 
b
e
e
n
 
c
h
a
n
g
e
d
.
)
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
e
f
1
7
2
9
8
5
-
7
e
3
6
-
4
2
9
7
-
9
5
b
e
-
e
4
6
3
9
6
9
6
8
d
6
6
'


 
 
 
 
l
o
o
k
u
p
_
v
a
l
u
e
 
=
 
{
 
 
 
 
 
 
 
'
D
i
s
a
b
l
e
d
'
:
 
1
,


 
 
 
 
 
 
 
 
'
E
n
a
b
l
e
d
'
:
 
0
,


 
 
 
 
 
 
 
 
'
N
e
w
O
r
i
g
i
n
'
:
 
2
}
 






c
l
a
s
s
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
e
x
t
e
n
d
e
d
 
e
r
r
o
r
 
i
n
f
o
r
m
a
t
i
o
n
.




 
 
 
 
 
 
E
x
t
e
n
d
e
d
 
e
r
r
o
r
 
i
n
f
o
r
m
a
t
i
o
n
 
c
a
n
 
b
e
 
s
e
t
 
b
y
 
V
i
r
t
u
a
l
B
o
x
 
c
o
m
p
o
n
e
n
t
s
 
a
f
t
e
r


 
 
 
 
 
 
u
n
s
u
c
c
e
s
s
f
u
l
 
o
r
 
p
a
r
t
i
a
l
l
y
 
s
u
c
c
e
s
s
f
u
l
 
m
e
t
h
o
d
 
i
n
v
o
c
a
t
i
o
n
.
 
T
h
i
s
 
i
n
f
o
r
m
a
t
i
o
n


 
 
 
 
 
 
c
a
n
 
b
e
 
r
e
t
r
i
e
v
e
d
 
b
y
 
t
h
e
 
c
a
l
l
i
n
g
 
p
a
r
t
y
 
a
s
 
a
n
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
 
o
b
j
e
c
t


 
 
 
 
 
 
a
n
d
 
t
h
e
n
 
s
h
o
w
n
 
t
o
 
t
h
e
 
c
l
i
e
n
t
 
i
n
 
a
d
d
i
t
i
o
n
 
t
o
 
t
h
e
 
p
l
a
i
n
 
3
2
-
b
i
t
 
r
e
s
u
l
t
 
c
o
d
e
.




 
 
 
 
 
 
I
n
 
M
S
 
C
O
M
,
 
t
h
i
s
 
i
n
t
e
r
f
a
c
e
 
e
x
t
e
n
d
s
 
t
h
e
 
I
E
r
r
o
r
I
n
f
o
 
i
n
t
e
r
f
a
c
e
,


 
 
 
 
 
 
i
n
 
X
P
C
O
M
,
 
i
t
 
e
x
t
e
n
d
s
 
t
h
e
 
n
s
I
E
x
c
e
p
t
i
o
n
 
i
n
t
e
r
f
a
c
e
.
 
I
n
 
b
o
t
h
 
c
a
s
e
s
,


 
 
 
 
 
 
i
t
 
p
r
o
v
i
d
e
s
 
a
 
s
e
t
 
o
f
 
c
o
m
m
o
n
 
a
t
t
r
i
b
u
t
e
s
 
t
o
 
r
e
t
r
i
e
v
e
 
e
r
r
o
r


 
 
 
 
 
 
i
n
f
o
r
m
a
t
i
o
n
.




 
 
 
 
 
 
S
o
m
e
t
i
m
e
s
 
i
n
v
o
c
a
t
i
o
n
 
o
f
 
s
o
m
e
 
c
o
m
p
o
n
e
n
t
'
s
 
m
e
t
h
o
d
 
m
a
y
 
i
n
v
o
l
v
e
 
m
e
t
h
o
d
s
 
o
f


 
 
 
 
 
 
o
t
h
e
r
 
c
o
m
p
o
n
e
n
t
s
 
t
h
a
t
 
m
a
y
 
a
l
s
o
 
f
a
i
l
 
(
i
n
d
e
p
e
n
d
e
n
t
l
y
 
o
f
 
t
h
i
s
 
m
e
t
h
o
d
'
s


 
 
 
 
 
 
f
a
i
l
u
r
e
)
,
 
o
r
 
a
 
s
e
r
i
e
s
 
o
f
 
n
o
n
-
f
a
t
a
l
 
e
r
r
o
r
s
 
m
a
y
 
p
r
e
c
e
d
e
 
a
 
f
a
t
a
l
 
e
r
r
o
r
 
t
h
a
t


 
 
 
 
 
 
c
a
u
s
e
s
 
m
e
t
h
o
d
 
f
a
i
l
u
r
e
.
 
I
n
 
c
a
s
e
s
 
l
i
k
e
 
t
h
a
t
,
 
i
t
 
m
a
y
 
b
e
 
d
e
s
i
r
a
b
l
e
 
t
o
 
p
r
e
s
e
r
v
e


 
 
 
 
 
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
a
l
l
 
e
r
r
o
r
s
 
h
a
p
p
e
n
e
d
 
d
u
r
i
n
g
 
m
e
t
h
o
d
 
i
n
v
o
c
a
t
i
o
n
 
a
n
d
 
d
e
l
i
v
e
r


 
 
 
 
 
 
i
t
 
t
o
 
t
h
e
 
c
a
l
l
e
r
.
 
T
h
e
 
<
l
i
n
k
 
t
o
=
"
#
n
e
x
t
"
/
>
 
a
t
t
r
i
b
u
t
e
 
i
s
 
i
n
t
e
n
d
e
d


 
 
 
 
 
 
s
p
e
c
i
f
i
c
a
l
l
y
 
f
o
r
 
t
h
i
s
 
p
u
r
p
o
s
e
 
a
n
d
 
a
l
l
o
w
s
 
t
o
 
r
e
p
r
e
s
e
n
t
 
a
 
c
h
a
i
n
 
o
f
 
e
r
r
o
r
s


 
 
 
 
 
 
t
h
r
o
u
g
h
 
a
 
s
i
n
g
l
e
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
 
o
b
j
e
c
t
 
s
e
t
 
a
f
t
e
r
 
m
e
t
h
o
d
 
i
n
v
o
c
a
t
i
o
n
.




 
 
 
 
 
 
e
r
r
o
r
s
 
a
r
e
 
s
t
o
r
e
d
 
t
o
 
a
 
c
h
a
i
n
 
i
n
 
t
h
e
 
r
e
v
e
r
s
e
 
o
r
d
e
r
,
 
i
.
e
.
 
t
h
e


 
 
 
 
 
 
i
n
i
t
i
a
l
 
e
r
r
o
r
 
o
b
j
e
c
t
 
y
o
u
 
q
u
e
r
y
 
r
i
g
h
t
 
a
f
t
e
r
 
m
e
t
h
o
d
 
i
n
v
o
c
a
t
i
o
n
 
i
s
 
t
h
e
 
l
a
s
t


 
 
 
 
 
 
e
r
r
o
r
 
s
e
t
 
b
y
 
t
h
e
 
c
a
l
l
e
e
,
 
t
h
e
 
o
b
j
e
c
t
 
i
t
 
p
o
i
n
t
s
 
t
o
 
i
n
 
t
h
e
 
@
a
 
n
e
x
t
 
a
t
t
r
i
b
u
t
e


 
 
 
 
 
 
i
s
 
t
h
e
 
p
r
e
v
i
o
u
s
 
e
r
r
o
r
 
a
n
d
 
s
o
 
o
n
,
 
u
p
 
t
o
 
t
h
e
 
f
i
r
s
t
 
e
r
r
o
r
 
(
w
h
i
c
h
 
i
s
 
t
h
e
 
l
a
s
t


 
 
 
 
 
 
i
n
 
t
h
e
 
c
h
a
i
n
)
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
c
1
b
c
c
6
d
5
-
7
9
6
6
-
4
8
1
d
-
a
b
0
b
-
d
0
e
d
7
3
e
2
8
1
3
5
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
s
u
l
t
_
c
o
d
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
r
e
s
u
l
t
C
o
d
e
'


 
 
 
 
 
 
 
 
R
e
s
u
l
t
 
c
o
d
e
 
o
f
 
t
h
e
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 
U
s
u
a
l
l
y
,
 
i
t
 
w
i
l
l
 
b
e
 
t
h
e
 
s
a
m
e
 
a
s
 
t
h
e
 
r
e
s
u
l
t
 
c
o
d
e
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
b
y
 
t
h
e
 
m
e
t
h
o
d
 
t
h
a
t
 
p
r
o
v
i
d
e
d
 
t
h
i
s
 
e
r
r
o
r
 
i
n
f
o
r
m
a
t
i
o
n
,
 
b
u
t
 
n
o
t


 
 
 
 
 
 
 
 
a
l
w
a
y
s
.
 
F
o
r
 
e
x
a
m
p
l
e
,
 
o
n
 
W
i
n
3
2
,
 
C
o
C
r
e
a
t
e
I
n
s
t
a
n
c
e
(
)
 
w
i
l
l
 
m
o
s
t


 
 
 
 
 
 
 
 
l
i
k
e
l
y
 
r
e
t
u
r
n
 
E
_
N
O
I
N
T
E
R
F
A
C
E
 
u
p
o
n
 
u
n
s
u
c
c
e
s
s
f
u
l
 
c
o
m
p
o
n
e
n
t


 
 
 
 
 
 
 
 
i
n
s
t
a
n
t
i
a
t
i
o
n
 
a
t
t
e
m
p
t
,
 
b
u
t
 
n
o
t
 
t
h
e
 
v
a
l
u
e
 
t
h
e
 
c
o
m
p
o
n
e
n
t
 
f
a
c
t
o
r
y


 
 
 
 
 
 
 
 
r
e
t
u
r
n
e
d
.
 
V
a
l
u
e
 
i
s
 
t
y
p
e
d
 
'
l
o
n
g
'
,
 
n
o
t
 
'
r
e
s
u
l
t
'
,


 
 
 
 
 
 
 
 
t
o
 
m
a
k
e
 
i
n
t
e
r
f
a
c
e
 
u
s
a
b
l
e
 
f
r
o
m
 
s
c
r
i
p
t
i
n
g
 
l
a
n
g
u
a
g
e
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
M
S
 
C
O
M
,
 
t
h
e
r
e
 
i
s
 
n
o
 
e
q
u
i
v
a
l
e
n
t
.


 
 
 
 
 
 
 
 
 
 
I
n
 
X
P
C
O
M
,
 
i
t
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
n
s
I
E
x
c
e
p
t
i
o
n
:
:
r
e
s
u
l
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
s
u
l
t
C
o
d
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
s
u
l
t
_
d
e
t
a
i
l
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
r
e
s
u
l
t
D
e
t
a
i
l
'


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
 
r
e
s
u
l
t
 
d
a
t
a
 
o
f
 
t
h
i
s
 
e
r
r
o
r
.
 
T
h
i
s
 
w
i
l
l
 
v
a
r
y
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e


 
 
 
 
 
 
 
 
a
c
t
u
a
l
 
e
r
r
o
r
 
u
s
a
g
e
.
 
B
y
 
d
e
f
a
u
l
t
 
t
h
i
s
 
a
t
t
r
i
b
u
t
e
 
i
s
 
n
o
t
 
b
e
i
n
g
 
u
s
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
s
u
l
t
D
e
t
a
i
l
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
n
t
e
r
f
a
c
e
_
i
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
i
n
t
e
r
f
a
c
e
I
D
'


 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
i
n
t
e
r
f
a
c
e
 
t
h
a
t
 
d
e
f
i
n
e
d
 
t
h
e
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
M
S
 
C
O
M
,
 
i
t
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
I
E
r
r
o
r
I
n
f
o
:
:
G
e
t
G
U
I
D
,
 
e
x
c
e
p
t
 
f
o
r
 
t
h
e


 
 
 
 
 
 
 
 
 
 
d
a
t
a
 
t
y
p
e
.


 
 
 
 
 
 
 
 
 
 
I
n
 
X
P
C
O
M
,
 
t
h
e
r
e
 
i
s
 
n
o
 
e
q
u
i
v
a
l
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
n
t
e
r
f
a
c
e
I
D
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
o
m
p
o
n
e
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
c
o
m
p
o
n
e
n
t
'


 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
c
o
m
p
o
n
e
n
t
 
t
h
a
t
 
g
e
n
e
r
a
t
e
d
 
t
h
e
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
M
S
 
C
O
M
,
 
i
t
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
I
E
r
r
o
r
I
n
f
o
:
:
G
e
t
S
o
u
r
c
e
.


 
 
 
 
 
 
 
 
 
 
I
n
 
X
P
C
O
M
,
 
t
h
e
r
e
 
i
s
 
n
o
 
e
q
u
i
v
a
l
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
o
m
p
o
n
e
n
t
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
e
x
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
t
e
x
t
'


 
 
 
 
 
 
 
 
T
e
x
t
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
h
e
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
M
S
 
C
O
M
,
 
i
t
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
I
E
r
r
o
r
I
n
f
o
:
:
G
e
t
D
e
s
c
r
i
p
t
i
o
n
.


 
 
 
 
 
 
 
 
 
 
I
n
 
X
P
C
O
M
,
 
i
t
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
n
s
I
E
x
c
e
p
t
i
o
n
:
:
m
e
s
s
a
g
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
e
x
t
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
x
t
_
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
 
v
a
l
u
e
 
f
o
r
 
'
n
e
x
t
'


 
 
 
 
 
 
 
 
N
e
x
t
 
e
r
r
o
r
 
o
b
j
e
c
t
 
i
f
 
t
h
e
r
e
 
i
s
 
a
n
y
,
 
o
r
 
@
c
 
n
u
l
l
 
o
t
h
e
r
w
i
s
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
M
S
 
C
O
M
,
 
t
h
e
r
e
 
i
s
 
n
o
 
e
q
u
i
v
a
l
e
n
t
.


 
 
 
 
 
 
 
 
 
 
I
n
 
X
P
C
O
M
,
 
i
t
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
n
s
I
E
x
c
e
p
t
i
o
n
:
:
i
n
n
e
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
x
t
'
,
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
)






c
l
a
s
s
 
I
N
A
T
N
e
t
w
o
r
k
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
B
D
:
 
t
h
e
 
i
d
e
a
,
 
t
e
c
h
n
i
c
a
l
l
y
 
w
e
 
c
a
n
 
s
t
a
r
t
 
a
n
y
 
n
u
m
b
e
r
 
o
f
 
t
h
e
 
N
A
T
 
n
e
t
w
o
r
k
s
,


 
 
 
 
 
 
 
 
b
u
t
 
w
e
 
s
h
o
u
l
d
 
e
x
p
e
c
t
 
t
h
a
t
 
a
t
 
s
o
m
e
 
p
o
i
n
t
 
w
e
 
w
i
l
l
 
g
e
t
 
c
o
l
l
i
s
i
o
n
s
 
b
e
c
a
u
s
e
 
o
f


 
 
 
 
 
 
 
 
p
o
r
t
-
f
o
r
w
a
n
d
i
n
g
 
r
u
l
e
s
.
 
s
o
 
p
e
r
h
a
p
s
 
w
e
 
s
h
o
u
l
d
 
s
u
p
p
o
r
t
 
o
n
l
y
 
s
i
n
g
l
e
 
i
n
s
t
a
n
c
e
 
o
f
 
N
A
T


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
0
3
D
F
D
6
F
7
-
1
B
7
8
-
4
8
A
3
-
8
3
4
5
-
C
7
8
5
2
8
1
E
9
5
2
3
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
_
n
a
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
N
e
t
w
o
r
k
N
a
m
e
'


 
 
 
 
 
 
 
 
T
B
D
:
 
t
h
e
 
i
d
e
a
,
 
t
e
c
h
n
i
c
a
l
l
y
 
w
e
 
c
a
n
 
s
t
a
r
t
 
a
n
y
 
n
u
m
b
e
r
 
o
f
 
t
h
e
 
N
A
T
 
n
e
t
w
o
r
k
s
,


 
 
 
 
 
 
 
 
b
u
t
 
w
e
 
s
h
o
u
l
d
 
e
x
p
e
c
t
 
t
h
a
t
 
a
t
 
s
o
m
e
 
p
o
i
n
t
 
w
e
 
w
i
l
l
 
g
e
t
 
c
o
l
l
i
s
i
o
n
s
 
b
e
c
a
u
s
e
 
o
f


 
 
 
 
 
 
 
 
p
o
r
t
-
f
o
r
w
a
n
d
i
n
g
 
r
u
l
e
s
.
 
s
o
 
p
e
r
h
a
p
s
 
w
e
 
s
h
o
u
l
d
 
s
u
p
p
o
r
t
 
o
n
l
y
 
s
i
n
g
l
e
 
i
n
s
t
a
n
c
e
 
o
f
 
N
A
T


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
N
e
t
w
o
r
k
N
a
m
e
'
,
 
s
t
r
)




 
 
 
 
@
n
e
t
w
o
r
k
_
n
a
m
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
_
n
a
m
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
N
e
t
w
o
r
k
N
a
m
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
e
n
a
b
l
e
d
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
e
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
e
t
w
o
r
k
'


 
 
 
 
 
 
 
 
T
h
i
s
 
i
s
 
C
I
D
R
 
I
P
v
4
 
s
t
r
i
n
g
.
 
S
p
e
c
i
f
i
y
i
n
g
 
i
t
 
u
s
e
r
 
d
e
f
i
n
e
s
 
I
P
v
4
 
a
d
d
r
e
s
s
e
s


 
 
 
 
 
 
 
 
o
f
 
g
a
t
e
w
a
y
 
(
l
o
w
 
a
d
d
r
e
s
s
 
+
 
1
)
 
a
n
d
 
d
h
c
p
 
s
e
r
v
e
r
 
(
=
 
l
o
w
 
a
d
d
r
e
s
s
 
+
 
2
)
.


 
 
 
 
 
 
 
 
N
o
t
e
:
 
i
f
 
t
h
e
r
e
'
r
e
 
d
e
f
i
n
e
d
 
I
P
v
4
 
p
o
r
t
-
f
o
r
w
a
r
d
 
r
u
l
e
s
 
u
p
d
a
t
e
 
o
f
 
n
e
t
w
o
r
k


 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
i
g
n
o
r
e
d
 
(
b
e
c
a
u
s
e
 
n
e
w
 
a
s
s
i
g
n
m
e
n
t
 
c
o
u
l
d
 
b
r
e
a
k
 
e
x
i
s
t
i
n
g
 
r
u
l
e
s
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
t
w
o
r
k
'
,
 
s
t
r
)




 
 
 
 
@
n
e
t
w
o
r
k
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
n
e
t
w
o
r
k
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
a
t
e
w
a
y
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
g
a
t
e
w
a
y
'


 
 
 
 
 
 
 
 
T
h
i
s
 
a
t
t
r
i
b
u
t
e
 
i
s
 
r
e
a
d
-
o
n
l
y
.
 
I
t
'
s
 
r
e
c
a
l
c
u
l
a
t
e
d
 
o
n
 
c
h
a
n
g
i
n
g


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
 
a
t
t
r
i
b
u
t
e
 
(
l
o
w
 
a
d
d
r
e
s
s
 
o
f
 
n
e
t
w
o
r
k
 
+
 
1
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
a
t
e
w
a
y
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
_
p
v
6
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
I
P
v
6
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
T
h
i
s
 
a
t
t
r
i
b
u
t
e
 
d
e
f
i
n
e
 
w
h
e
t
h
e
r
 
g
a
t
e
w
a
y
 
w
i
l
l
 
s
u
p
p
o
r
t
 
I
P
v
6
 
o
r
 
n
o
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
P
v
6
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
i
_
p
v
6
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
i
_
p
v
6
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
I
P
v
6
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
_
p
v
6
_
p
r
e
f
i
x
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
I
P
v
6
P
r
e
f
i
x
'


 
 
 
 
 
 
 
 
T
h
i
s
 
a
 
C
I
D
R
 
I
P
v
6
 
d
e
f
i
n
i
n
g
 
p
r
e
f
i
x
 
f
o
r
 
l
i
n
k
-
l
o
c
a
l
 
a
d
d
r
e
s
s
e
s
 
a
u
t
o
c
o
n
f
i
g
u
r
a
t
i
o
n
 
 
 
 
 
w
i
t
h
i
n
 
n
e
t
w
o
r
k
.
 
N
o
t
e
:
 
i
g
n
o
r
e
d
 
i
f
 
a
t
t
r
i
b
u
t
e
 
i
p
v
6
e
n
a
b
l
e
d
 
i
s
 
f
a
l
s
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
P
v
6
P
r
e
f
i
x
'
,
 
s
t
r
)




 
 
 
 
@
i
_
p
v
6
_
p
r
e
f
i
x
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
i
_
p
v
6
_
p
r
e
f
i
x
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
I
P
v
6
P
r
e
f
i
x
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
d
v
e
r
t
i
s
e
_
d
e
f
a
u
l
t
_
i
_
p
v
6
_
r
o
u
t
e
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
d
v
e
r
t
i
s
e
D
e
f
a
u
l
t
I
P
v
6
R
o
u
t
e
E
n
a
b
l
e
d
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
d
v
e
r
t
i
s
e
D
e
f
a
u
l
t
I
P
v
6
R
o
u
t
e
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
a
d
v
e
r
t
i
s
e
_
d
e
f
a
u
l
t
_
i
_
p
v
6
_
r
o
u
t
e
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
d
v
e
r
t
i
s
e
_
d
e
f
a
u
l
t
_
i
_
p
v
6
_
r
o
u
t
e
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
d
v
e
r
t
i
s
e
D
e
f
a
u
l
t
I
P
v
6
R
o
u
t
e
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
e
d
_
d
h
c
p
_
s
e
r
v
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
n
e
e
d
D
h
c
p
S
e
r
v
e
r
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
e
d
D
h
c
p
S
e
r
v
e
r
'
,
 
b
o
o
l
)




 
 
 
 
@
n
e
e
d
_
d
h
c
p
_
s
e
r
v
e
r
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
n
e
e
d
_
d
h
c
p
_
s
e
r
v
e
r
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
n
e
e
d
D
h
c
p
S
e
r
v
e
r
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
v
e
n
t
_
s
o
u
r
c
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
E
v
e
n
t
S
o
u
r
c
e
 
v
a
l
u
e
 
f
o
r
 
'
e
v
e
n
t
S
o
u
r
c
e
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
v
e
n
t
S
o
u
r
c
e
'
,
 
I
E
v
e
n
t
S
o
u
r
c
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
o
r
t
_
f
o
r
w
a
r
d
_
r
u
l
e
s
4
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
p
o
r
t
F
o
r
w
a
r
d
R
u
l
e
s
4
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
N
A
T
 
p
o
r
t
-
f
o
r
w
a
r
d
i
n
g
 
r
u
l
e
s
 
i
n
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
,


 
 
 
 
 
 
i
n
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
f
o
r
m
a
t
:


 
 
 
 
 
 
"
n
a
m
e
:
p
r
o
t
o
c
o
l
i
d
:
[
h
o
s
t
 
i
p
]
:
h
o
s
t
 
p
o
r
t
:
[
g
u
e
s
t
 
i
p
]
:
g
u
e
s
t
 
p
o
r
t
"
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
o
r
t
F
o
r
w
a
r
d
R
u
l
e
s
4
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
o
r
t
_
f
o
r
w
a
r
d
_
r
u
l
e
s
6
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
p
o
r
t
F
o
r
w
a
r
d
R
u
l
e
s
6
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
N
A
T
 
p
o
r
t
-
f
o
r
w
a
r
d
i
n
g
 
r
u
l
e
s
 
i
n
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
,
 
i
n
 
t
h
e


 
 
 
 
 
 
f
o
l
l
o
w
i
n
g
 
f
o
r
m
a
t
:
 
"
n
a
m
e
:
p
r
o
t
o
c
o
l
i
d
:
[
h
o
s
t
 
i
p
]
:
h
o
s
t
 
p
o
r
t
:
[
g
u
e
s
t
 
i
p
]
:
g
u
e
s
t
 
p
o
r
t
"
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
o
r
t
F
o
r
w
a
r
d
R
u
l
e
s
6
'
,
 
s
t
r
)




 
 
 
 
d
e
f
 
a
d
d
_
p
o
r
t
_
f
o
r
w
a
r
d
_
r
u
l
e
(
s
e
l
f
,
 
i
s
_
i
p
v
6
,
 
r
u
l
e
_
n
a
m
e
,
 
p
r
o
t
o
,
 
h
o
s
t
_
i
p
,
 
h
o
s
t
_
p
o
r
t
,
 
g
u
e
s
t
_
i
p
,
 
g
u
e
s
t
_
p
o
r
t
)
:


 
 
 
 
 
 
 
 
"
"
"
P
r
o
t
o
c
o
l
 
h
a
n
d
l
e
d
 
w
i
t
h
 
t
h
e
 
r
u
l
e
.




 
 
 
 
 
 
 
 
i
n
 
i
s
_
i
p
v
6
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
i
n
 
r
u
l
e
_
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
i
n
 
p
r
o
t
o
 
o
f
 
t
y
p
e
 
N
A
T
P
r
o
t
o
c
o
l


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
t
o
c
o
l
 
h
a
n
d
l
e
d
 
w
i
t
h
 
t
h
e
 
r
u
l
e
.




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
_
i
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
I
P
 
o
f
 
t
h
e
 
h
o
s
t
 
i
n
t
e
r
f
a
c
e
 
t
o
 
w
h
i
c
h
 
t
h
e
 
r
u
l
e
 
s
h
o
u
l
d
 
a
p
p
l
y
.


 
 
 
 
 
 
 
 
A
n
 
e
m
p
t
y
 
i
p
 
a
d
d
r
e
s
s
 
i
s
 
a
c
c
e
p
t
a
b
l
e
,
 
i
n
 
w
h
i
c
h
 
c
a
s
e
 
t
h
e
 
N
A
T
 
e
n
g
i
n
e


 
 
 
 
 
 
 
 
b
i
n
d
s
 
t
h
e
 
h
a
n
d
l
i
n
g
 
s
o
c
k
e
t
 
t
o
 
a
n
y
 
i
n
t
e
r
f
a
c
e
.




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
p
o
r
t
 
n
u
m
b
e
r
 
t
o
 
l
i
s
t
e
n
 
o
n
.




 
 
 
 
 
 
 
 
i
n
 
g
u
e
s
t
_
i
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
I
P
 
a
d
d
r
e
s
s
 
o
f
 
t
h
e
 
g
u
e
s
t
 
w
h
i
c
h
 
t
h
e
 
N
A
T
 
e
n
g
i
n
e
 
w
i
l
l
 
f
o
r
w
a
r
d


 
 
 
 
 
 
 
 
m
a
t
c
h
i
n
g
 
p
a
c
k
e
t
s
 
t
o
.
 
A
n
 
e
m
p
t
y
 
I
P
 
a
d
d
r
e
s
s
 
i
s
 
n
o
t
 
a
c
c
e
p
t
a
b
l
e
.




 
 
 
 
 
 
 
 
i
n
 
g
u
e
s
t
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
p
o
r
t
 
n
u
m
b
e
r
 
t
o
 
f
o
r
w
a
r
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
d
d
P
o
r
t
F
o
r
w
a
r
d
R
u
l
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
s
_
i
p
v
6
,
 
r
u
l
e
_
n
a
m
e
,
 
p
r
o
t
o
,
 
h
o
s
t
_
i
p
,
 
h
o
s
t
_
p
o
r
t
,
 
g
u
e
s
t
_
i
p
,
 
g
u
e
s
t
_
p
o
r
t
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
p
o
r
t
_
f
o
r
w
a
r
d
_
r
u
l
e
(
s
e
l
f
,
 
i
_
s
i
p
v
6
,
 
r
u
l
e
_
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
 
 
 
 
i
n
 
i
_
s
i
p
v
6
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
i
n
 
r
u
l
e
_
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
P
o
r
t
F
o
r
w
a
r
d
R
u
l
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
_
s
i
p
v
6
,
 
r
u
l
e
_
n
a
m
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
t
a
r
t
(
s
e
l
f
,
 
t
r
u
n
k
_
t
y
p
e
)
:


 
 
 
 
 
 
 
 
"
"
"
T
y
p
e
 
o
f
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
t
r
u
n
k
.




 
 
 
 
 
 
 
 
i
n
 
t
r
u
n
k
_
t
y
p
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
t
r
u
n
k
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
t
a
r
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
t
r
u
n
k
_
t
y
p
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
t
o
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
t
o
p
'
)


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
D
H
C
P
S
e
r
v
e
r
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
D
H
C
P
S
e
r
v
e
r
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
t
h
e
 
v
b
o
x
 
D
H
C
P
 
s
e
r
v
e
r
 
c
o
n
f
i
g
u
r
a
t
i
o
n
.




 
 
 
 
 
 
T
o
 
e
n
u
m
e
r
a
t
e
 
a
l
l
 
t
h
e
 
D
H
C
P
 
s
e
r
v
e
r
s
 
o
n
 
t
h
e
 
h
o
s
t
,
 
u
s
e
 
t
h
e


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
D
H
C
P
S
e
r
v
e
r
s
"
/
>
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
c
f
e
3
8
7
c
-
7
4
f
b
-
4
c
a
7
-
b
f
f
6
-
9
7
3
b
e
c
8
a
f
7
a
3
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
e
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
s
 
i
f
 
t
h
e
 
D
H
C
P
 
s
e
r
v
e
r
 
i
s
 
e
n
a
b
l
e
d


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
e
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
p
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
I
P
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
s
 
s
e
r
v
e
r
 
I
P


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
P
A
d
d
r
e
s
s
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
_
m
a
s
k
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
e
t
w
o
r
k
M
a
s
k
'


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
s
 
s
e
r
v
e
r
 
n
e
t
w
o
r
k
 
m
a
s
k


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
t
w
o
r
k
M
a
s
k
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
_
n
a
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
e
t
w
o
r
k
N
a
m
e
'


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
s
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
n
a
m
e
 
t
h
e
 
s
e
r
v
e
r
 
i
s
 
u
s
e
d
 
f
o
r


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
t
w
o
r
k
N
a
m
e
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
o
w
e
r
_
i
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
l
o
w
e
r
I
P
'


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
s
 
f
r
o
m
 
I
P
 
a
d
d
r
e
s
s
 
i
n
 
s
e
r
v
e
r
 
a
d
d
r
e
s
s
 
r
a
n
g
e


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
o
w
e
r
I
P
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
p
p
e
r
_
i
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
u
p
p
e
r
I
P
'


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
s
 
t
o
 
I
P
 
a
d
d
r
e
s
s
 
i
n
 
s
e
r
v
e
r
 
a
d
d
r
e
s
s
 
r
a
n
g
e


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
u
p
p
e
r
I
P
'
,
 
s
t
r
)




 
 
 
 
d
e
f
 
s
e
t
_
c
o
n
f
i
g
u
r
a
t
i
o
n
(
s
e
l
f
,
 
i
p
_
a
d
d
r
e
s
s
,
 
n
e
t
w
o
r
k
_
m
a
s
k
,
 
f
r
o
m
_
i
p
_
a
d
d
r
e
s
s
,
 
t
o
_
i
p
_
a
d
d
r
e
s
s
)
:


 
 
 
 
 
 
 
 
"
"
"
c
o
n
f
i
g
u
r
e
s
 
t
h
e
 
s
e
r
v
e
r




 
 
 
 
 
 
 
 
i
n
 
i
p
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
I
P
 
a
d
d
r
e
s
s




 
 
 
 
 
 
 
 
i
n
 
n
e
t
w
o
r
k
_
m
a
s
k
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
n
e
t
w
o
r
k
 
m
a
s
k




 
 
 
 
 
 
 
 
i
n
 
f
r
o
m
_
i
p
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
F
r
o
m
 
I
P
 
a
d
d
r
e
s
s
 
f
o
r
 
a
d
d
r
e
s
s
 
r
a
n
g
e




 
 
 
 
 
 
 
 
i
n
 
t
o
_
i
p
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
T
o
 
I
P
 
a
d
d
r
e
s
s
 
f
o
r
 
a
d
d
r
e
s
s
 
r
a
n
g
e




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
i
n
v
a
l
i
d
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
s
u
p
p
l
i
e
d


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
C
o
n
f
i
g
u
r
a
t
i
o
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
p
_
a
d
d
r
e
s
s
,
 
n
e
t
w
o
r
k
_
m
a
s
k
,
 
f
r
o
m
_
i
p
_
a
d
d
r
e
s
s
,
 
t
o
_
i
p
_
a
d
d
r
e
s
s
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
t
a
r
t
(
s
e
l
f
,
 
n
e
t
w
o
r
k
_
n
a
m
e
,
 
t
r
u
n
k
_
n
a
m
e
,
 
t
r
u
n
k
_
t
y
p
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
t
a
r
t
s
 
D
H
C
P
 
s
e
r
v
e
r
 
p
r
o
c
e
s
s
.




 
 
 
 
 
 
 
 
i
n
 
n
e
t
w
o
r
k
_
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
D
H
C
P
 
s
e
r
v
e
r
 
s
h
o
u
l
d
 
a
t
t
a
c
h
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
t
r
u
n
k
_
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
t
r
u
n
k
.




 
 
 
 
 
 
 
 
i
n
 
t
r
u
n
k
_
t
y
p
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
t
r
u
n
k
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
F
A
I
L


 
 
 
 
 
 
 
 
 
 
 
 
F
a
i
l
e
d
 
t
o
 
s
t
a
r
t
 
t
h
e
 
p
r
o
c
e
s
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
t
a
r
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
e
t
w
o
r
k
_
n
a
m
e
,
 
t
r
u
n
k
_
n
a
m
e
,
 
t
r
u
n
k
_
t
y
p
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
t
o
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
S
t
o
p
s
 
D
H
C
P
 
s
e
r
v
e
r
 
p
r
o
c
e
s
s
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
F
A
I
L


 
 
 
 
 
 
 
 
 
 
 
 
F
a
i
l
e
d
 
t
o
 
s
t
o
p
 
t
h
e
 
p
r
o
c
e
s
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
t
o
p
'
)


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
V
i
r
t
u
a
l
B
o
x
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
V
i
r
t
u
a
l
B
o
x
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
t
h
e
 
m
a
i
n
 
i
n
t
e
r
f
a
c
e
 
e
x
p
o
s
e
d
 
b
y
 
t
h
e


 
 
 
 
 
 
p
r
o
d
u
c
t
 
t
h
a
t
 
p
r
o
v
i
d
e
s
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
m
a
n
a
g
e
m
e
n
t
.




 
 
 
 
 
 
A
n
 
i
n
s
t
a
n
c
e
 
o
f
 
I
V
i
r
t
u
a
l
B
o
x
 
i
s
 
r
e
q
u
i
r
e
d
 
f
o
r
 
t
h
e
 
p
r
o
d
u
c
t
 
t
o
 
d
o
 
a
n
y
t
h
i
n
g


 
 
 
 
 
 
u
s
e
f
u
l
.
 
E
v
e
n
 
t
h
o
u
g
h
 
t
h
e
 
i
n
t
e
r
f
a
c
e
 
d
o
e
s
 
n
o
t
 
e
x
p
o
s
e
 
t
h
i
s
,
 
i
n
t
e
r
n
a
l
l
y
,


 
 
 
 
 
 
I
V
i
r
t
u
a
l
B
o
x
 
i
s
 
i
m
p
l
e
m
e
n
t
e
d
 
a
s
 
a
 
s
i
n
g
l
e
t
o
n
 
a
n
d
 
a
c
t
u
a
l
l
y
 
l
i
v
e
s
 
i
n
 
t
h
e


 
 
 
 
 
 
p
r
o
c
e
s
s
 
o
f
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
s
e
r
v
e
r
 
(
V
B
o
x
S
V
C
.
e
x
e
)
.
 
T
h
i
s
 
m
a
k
e
s
 
s
u
r
e
 
t
h
a
t


 
 
 
 
 
 
I
V
i
r
t
u
a
l
B
o
x
 
c
a
n
 
t
r
a
c
k
 
t
h
e
 
s
t
a
t
e
 
o
f
 
a
l
l
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
 
o
n
 
a
 
p
a
r
t
i
c
u
l
a
r


 
 
 
 
 
 
h
o
s
t
,
 
r
e
g
a
r
d
l
e
s
s
 
o
f
 
w
h
i
c
h
 
f
r
o
n
t
e
n
d
 
s
t
a
r
t
e
d
 
t
h
e
m
.




 
 
 
 
 
 
T
o
 
e
n
u
m
e
r
a
t
e
 
a
l
l
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
 
o
n
 
t
h
e
 
h
o
s
t
,
 
u
s
e
 
t
h
e


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
m
a
c
h
i
n
e
s
"
/
>
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
f
a
f
a
4
e
1
7
-
1
e
e
2
-
4
9
0
5
-
a
1
0
e
-
f
e
7
c
1
8
b
f
5
5
5
4
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
e
r
s
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
v
e
r
s
i
o
n
'


 
 
 
 
 
 
 
 
A
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
v
e
r
s
i
o
n
 
n
u
m
b
e
r
 
o
f
 
t
h
e
 
p
r
o
d
u
c
t
.
 
T
h
e


 
 
 
 
 
 
 
 
f
o
r
m
a
t
 
i
s
 
3
 
i
n
t
e
g
e
r
 
n
u
m
b
e
r
s
 
d
i
v
i
d
e
d
 
b
y
 
d
o
t
s
 
(
e
.
g
.
 
1
.
0
.
1
)
.
 
T
h
e


 
 
 
 
 
 
 
 
l
a
s
t
 
n
u
m
b
e
r
 
r
e
p
r
e
s
e
n
t
s
 
t
h
e
 
b
u
i
l
d
 
n
u
m
b
e
r
 
a
n
d
 
w
i
l
l
 
f
r
e
q
u
e
n
t
l
y
 
c
h
a
n
g
e
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
a
y
 
b
e
 
f
o
l
l
o
w
e
d
 
b
y
 
a
 
_
A
L
P
H
A
[
0
-
9
]
*
,
 
_
B
E
T
A
[
0
-
9
]
*
 
o
r
 
_
R
C
[
0
-
9
]
*
 
t
a
g


 
 
 
 
 
 
 
 
i
n
 
p
r
e
r
e
l
e
a
s
e
 
b
u
i
l
d
s
.
 
N
o
n
-
O
r
a
c
l
e
 
b
u
i
l
d
s
 
m
a
y
 
(
/
s
h
a
l
l
)
 
a
l
s
o
 
h
a
v
e
 
a


 
 
 
 
 
 
 
 
p
u
b
l
i
s
h
e
r
 
t
a
g
,
 
a
t
 
t
h
e
 
e
n
d
.
 
T
h
e
 
p
u
b
l
i
s
h
e
r
 
t
a
g
 
s
t
a
r
t
s
 
w
i
t
h
 
a
n
 
u
n
d
e
r
s
c
o
r
e


 
 
 
 
 
 
 
 
j
u
s
t
 
l
i
k
e
 
t
h
e
 
p
r
e
r
e
l
e
a
s
e
 
b
u
i
l
d
 
t
y
p
e
 
t
a
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
v
e
r
s
i
o
n
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
e
r
s
i
o
n
_
n
o
r
m
a
l
i
z
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
v
e
r
s
i
o
n
N
o
r
m
a
l
i
z
e
d
'


 
 
 
 
 
 
 
 
A
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
v
e
r
s
i
o
n
 
n
u
m
b
e
r
 
o
f
 
t
h
e
 
p
r
o
d
u
c
t
,


 
 
 
 
 
 
 
 
w
i
t
h
o
u
t
 
t
h
e
 
p
u
b
l
i
s
h
e
r
 
i
n
f
o
r
m
a
t
i
o
n
 
(
b
u
t
 
s
t
i
l
l
 
w
i
t
h
 
o
t
h
e
r
 
t
a
g
s
)
.


 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
#
v
e
r
s
i
o
n
"
/
>
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
v
e
r
s
i
o
n
N
o
r
m
a
l
i
z
e
d
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
v
i
s
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
r
e
v
i
s
i
o
n
'


 
 
 
 
 
 
 
 
T
h
e
 
i
n
t
e
r
n
a
l
 
b
u
i
l
d
 
r
e
v
i
s
i
o
n
 
n
u
m
b
e
r
 
o
f
 
t
h
e
 
p
r
o
d
u
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
v
i
s
i
o
n
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
a
c
k
a
g
e
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
p
a
c
k
a
g
e
T
y
p
e
'


 
 
 
 
 
 
 
 
A
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
p
a
c
k
a
g
e
 
t
y
p
e
 
o
f
 
t
h
i
s
 
p
r
o
d
u
c
t
.
 
T
h
e


 
 
 
 
 
 
 
 
f
o
r
m
a
t
 
i
s
 
O
S
_
A
R
C
H
_
D
I
S
T
 
w
h
e
r
e
 
O
S
 
i
s
 
e
i
t
h
e
r
 
W
I
N
D
O
W
S
,
 
L
I
N
U
X
,


 
 
 
 
 
 
 
 
S
O
L
A
R
I
S
,
 
D
A
R
W
I
N
.
 
A
R
C
H
 
i
s
 
e
i
t
h
e
r
 
3
2
B
I
T
S
 
o
r
 
6
4
B
I
T
S
.
 
D
I
S
T


 
 
 
 
 
 
 
 
i
s
 
e
i
t
h
e
r
 
G
E
N
E
R
I
C
,
 
U
B
U
N
T
U
_
6
0
6
,
 
U
B
U
N
T
U
_
7
1
0
,
 
o
r
 
s
o
m
e
t
h
i
n
g
 
l
i
k
e


 
 
 
 
 
 
 
 
t
h
i
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
a
c
k
a
g
e
T
y
p
e
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
p
i
_
v
e
r
s
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
A
P
I
V
e
r
s
i
o
n
'


 
 
 
 
 
 
 
 
A
 
s
t
r
i
n
g
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
A
P
I
 
v
e
r
s
i
o
n
 
n
u
m
b
e
r
.
 
T
h
e
 
f
o
r
m
a
t
 
i
s


 
 
 
 
 
 
 
 
2
 
i
n
t
e
g
e
r
 
n
u
m
b
e
r
s
 
d
i
v
i
d
e
d
 
b
y
 
a
n
 
u
n
d
e
r
s
c
o
r
e
 
(
e
.
g
.
 
1
_
0
)
.
 
A
f
t
e
r
 
t
h
e


 
 
 
 
 
 
 
 
f
i
r
s
t
 
p
u
b
l
i
c
 
r
e
l
e
a
s
e
 
o
f
 
p
a
c
k
a
g
e
s
 
w
i
t
h
 
a
 
p
a
r
t
i
c
u
l
a
r
 
A
P
I
 
v
e
r
s
i
o
n
 
t
h
e


 
 
 
 
 
 
 
 
A
P
I
 
w
i
l
l
 
n
o
t
 
b
e
 
c
h
a
n
g
e
d
 
i
n
 
a
n
 
i
n
c
o
m
p
a
t
i
b
l
e
 
w
a
y
.
 
N
o
t
e
 
t
h
a
t
 
t
h
i
s


 
 
 
 
 
 
 
 
g
u
a
r
a
n
t
e
e
 
d
o
e
s
 
n
o
t
 
a
p
p
l
y
 
t
o
 
d
e
v
e
l
o
p
m
e
n
t
 
b
u
i
l
d
s
,
 
a
n
d
 
a
l
s
o
 
t
h
e
r
e
 
i
s
 
n
o


 
 
 
 
 
 
 
 
g
u
a
r
a
n
t
e
e
 
t
h
a
t
 
t
h
i
s
 
v
e
r
s
i
o
n
 
i
s
 
i
d
e
n
t
i
c
a
l
 
t
o
 
t
h
e
 
f
i
r
s
t
 
t
w
o
 
i
n
t
e
g
e
r


 
 
 
 
 
 
 
 
n
u
m
b
e
r
s
 
o
f
 
t
h
e
 
p
a
c
k
a
g
e
 
v
e
r
s
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
A
P
I
V
e
r
s
i
o
n
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
o
m
e
_
f
o
l
d
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
h
o
m
e
F
o
l
d
e
r
'


 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
d
i
r
e
c
t
o
r
y
 
w
h
e
r
e
 
t
h
e
 
g
l
o
b
a
l
 
s
e
t
t
i
n
g
s
 
f
i
l
e
,


 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
.
x
m
l
,
 
i
s
 
s
t
o
r
e
d
.




 
 
 
 
 
 
 
 
I
n
 
t
h
i
s
 
v
e
r
s
i
o
n
 
o
f
 
V
i
r
t
u
a
l
B
o
x
,
 
t
h
e
 
v
a
l
u
e
 
o
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s


 
 
 
 
 
 
 
 
a
l
w
a
y
s
 
<
u
s
e
r
_
d
i
r
>
/
.
V
i
r
t
u
a
l
B
o
x
 
(
w
h
e
r
e


 
 
 
 
 
 
 
 
<
u
s
e
r
_
d
i
r
>
 
i
s
 
t
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
u
s
e
r
 
d
i
r
e
c
t
o
r
y
,


 
 
 
 
 
 
 
 
a
s
 
d
e
t
e
r
m
i
n
e
d
 
b
y
 
t
h
e
 
h
o
s
t
 
O
S
)
,
 
a
n
d
 
c
a
n
n
o
t
 
b
e
 
c
h
a
n
g
e
d
.




 
 
 
 
 
 
 
 
T
h
i
s
 
p
a
t
h
 
i
s
 
a
l
s
o
 
u
s
e
d
 
a
s
 
t
h
e
 
b
a
s
e
 
t
o
 
r
e
s
o
l
v
e
 
r
e
l
a
t
i
v
e
 
p
a
t
h
s
 
i
n


 
 
 
 
 
 
 
 
p
l
a
c
e
s
 
w
h
e
r
e
 
r
e
l
a
t
i
v
e
 
p
a
t
h
s
 
a
r
e
 
a
l
l
o
w
e
d
 
(
u
n
l
e
s
s
 
o
t
h
e
r
w
i
s
e


 
 
 
 
 
 
 
 
e
x
p
r
e
s
s
l
y
 
i
n
d
i
c
a
t
e
d
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
h
o
m
e
F
o
l
d
e
r
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
e
t
t
i
n
g
s
_
f
i
l
e
_
p
a
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
s
e
t
t
i
n
g
s
F
i
l
e
P
a
t
h
'


 
 
 
 
 
 
 
 
F
u
l
l
 
n
a
m
e
 
o
f
 
t
h
e
 
g
l
o
b
a
l
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 
T
h
e
 
v
a
l
u
e
 
o
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
c
o
r
r
e
s
p
o
n
d
s
 
t
o
 
t
h
e
 
v
a
l
u
e
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
h
o
m
e
F
o
l
d
e
r
"
/
>
 
p
l
u
s
 
/
V
i
r
t
u
a
l
B
o
x
.
x
m
l
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
e
t
t
i
n
g
s
F
i
l
e
P
a
t
h
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
o
s
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
H
o
s
t
 
v
a
l
u
e
 
f
o
r
 
'
h
o
s
t
'


 
 
 
 
 
 
 
 
A
s
s
o
c
i
a
t
e
d
 
h
o
s
t
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
h
o
s
t
'
,
 
I
H
o
s
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
y
s
t
e
m
_
p
r
o
p
e
r
t
i
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
 
v
a
l
u
e
 
f
o
r
 
'
s
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
'


 
 
 
 
 
 
 
 
A
s
s
o
c
i
a
t
e
d
 
s
y
s
t
e
m
 
i
n
f
o
r
m
a
t
i
o
n
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
'
,
 
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
c
h
i
n
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
a
c
h
i
n
e
 
v
a
l
u
e
 
f
o
r
 
'
m
a
c
h
i
n
e
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
s
 
r
e
g
i
s
t
e
r
e
d
 
w
i
t
h
i
n
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
n
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
c
h
i
n
e
s
'
,
 
I
M
a
c
h
i
n
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
c
h
i
n
e
_
g
r
o
u
p
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
m
a
c
h
i
n
e
G
r
o
u
p
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
a
l
l
 
m
a
c
h
i
n
e
 
g
r
o
u
p
 
n
a
m
e
s
 
w
h
i
c
h
 
a
r
e
 
u
s
e
d
 
b
y
 
t
h
e
 
m
a
c
h
i
n
e
s
 
w
h
i
c
h


 
 
 
 
 
 
 
 
a
r
e
 
a
c
c
e
s
s
i
b
l
e
.
 
E
a
c
h
 
g
r
o
u
p
 
i
s
 
o
n
l
y
 
l
i
s
t
e
d
 
o
n
c
e
,
 
h
o
w
e
v
e
r
 
t
h
e
y
 
a
r
e
 
l
i
s
t
e
d


 
 
 
 
 
 
 
 
i
n
 
n
o
 
p
a
r
t
i
c
u
l
a
r
 
o
r
d
e
r
 
a
n
d
 
t
h
e
r
e
 
i
s
 
n
o
 
g
u
a
r
a
n
t
e
e
 
t
h
a
t
 
t
h
e
r
e
 
a
r
e
 
n
o
 
g
a
p
s


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
g
r
o
u
p
 
h
i
e
r
a
r
c
h
y
 
(
i
.
e
.
 
"
/
"
,
 
"
/
g
r
o
u
p
/
s
u
b
g
r
o
u
p
"


 
 
 
 
 
 
 
 
i
s
 
a
 
v
a
l
i
d
 
r
e
s
u
l
t
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
c
h
i
n
e
G
r
o
u
p
s
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
a
r
d
_
d
i
s
k
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
e
d
i
u
m
 
v
a
l
u
e
 
f
o
r
 
'
h
a
r
d
D
i
s
k
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
m
e
d
i
u
m
 
o
b
j
e
c
t
s
 
k
n
o
w
n
 
t
o
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
l
l
a
t
i
o
n
.




 
 
 
 
 
 
 
 
T
h
i
s
 
a
r
r
a
y
 
c
o
n
t
a
i
n
s
 
o
n
l
y
 
b
a
s
e
 
m
e
d
i
a
.
 
A
l
l
 
d
i
f
f
e
r
e
n
c
i
n
g


 
 
 
 
 
 
 
 
m
e
d
i
a
 
o
f
 
t
h
e
 
g
i
v
e
n
 
b
a
s
e
 
m
e
d
i
u
m
 
c
a
n
 
b
e
 
e
n
u
m
e
r
a
t
e
d
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
c
h
i
l
d
r
e
n
"
/
>
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
h
a
r
d
D
i
s
k
s
'
,
 
I
M
e
d
i
u
m
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
v
d
_
i
m
a
g
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
e
d
i
u
m
 
v
a
l
u
e
 
f
o
r
 
'
D
V
D
I
m
a
g
e
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
C
D
/
D
V
D
 
i
m
a
g
e
 
o
b
j
e
c
t
s
 
c
u
r
r
e
n
t
l
y
 
i
n
 
u
s
e
 
b
y
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
n
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
D
V
D
I
m
a
g
e
s
'
,
 
I
M
e
d
i
u
m
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
l
o
p
p
y
_
i
m
a
g
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
e
d
i
u
m
 
v
a
l
u
e
 
f
o
r
 
'
f
l
o
p
p
y
I
m
a
g
e
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
f
l
o
p
p
y
 
i
m
a
g
e
 
o
b
j
e
c
t
s
 
c
u
r
r
e
n
t
l
y
 
i
n
 
u
s
e
 
b
y
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
n
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
l
o
p
p
y
I
m
a
g
e
s
'
,
 
I
M
e
d
i
u
m
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
r
o
g
r
e
s
s
_
o
p
e
r
a
t
i
o
n
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
P
r
o
g
r
e
s
s
 
v
a
l
u
e
 
f
o
r
 
'
p
r
o
g
r
e
s
s
O
p
e
r
a
t
i
o
n
s
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
r
o
g
r
e
s
s
O
p
e
r
a
t
i
o
n
s
'
,
 
I
P
r
o
g
r
e
s
s
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
u
e
s
t
_
o
s
_
t
y
p
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
G
u
e
s
t
O
S
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
g
u
e
s
t
O
S
T
y
p
e
s
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
u
e
s
t
O
S
T
y
p
e
s
'
,
 
I
G
u
e
s
t
O
S
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
h
a
r
e
d
_
f
o
l
d
e
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
S
h
a
r
e
d
F
o
l
d
e
r
 
v
a
l
u
e
 
f
o
r
 
'
s
h
a
r
e
d
F
o
l
d
e
r
s
'


 
 
 
 
 
 
 
 
C
o
l
l
e
c
t
i
o
n
 
o
f
 
g
l
o
b
a
l
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
.
 
G
l
o
b
a
l
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
r
e


 
 
 
 
 
 
 
 
a
v
a
i
l
a
b
l
e
 
t
o
 
a
l
l
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
.




 
 
 
 
 
 
 
 
N
e
w
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
r
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
.
 
E
x
i
s
t
i
n
g
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
r
e
m
o
v
e
d
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
#
r
e
m
o
v
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
t
h
e
 
c
u
r
r
e
n
t
 
v
e
r
s
i
o
n
 
o
f
 
t
h
e
 
p
r
o
d
u
c
t
,
 
g
l
o
b
a
l
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
r
e
 
n
o
t


 
 
 
 
 
 
 
 
 
 
i
m
p
l
e
m
e
n
t
e
d
 
a
n
d
 
t
h
e
r
e
f
o
r
e
 
t
h
i
s
 
c
o
l
l
e
c
t
i
o
n
 
i
s
 
a
l
w
a
y
s
 
e
m
p
t
y
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
h
a
r
e
d
F
o
l
d
e
r
s
'
,
 
I
S
h
a
r
e
d
F
o
l
d
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
e
r
f
o
r
m
a
n
c
e
_
c
o
l
l
e
c
t
o
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
P
e
r
f
o
r
m
a
n
c
e
C
o
l
l
e
c
t
o
r
 
v
a
l
u
e
 
f
o
r
 
'
p
e
r
f
o
r
m
a
n
c
e
C
o
l
l
e
c
t
o
r
'


 
 
 
 
 
 
 
 
A
s
s
o
c
i
a
t
e
d
 
p
e
r
f
o
r
m
a
n
c
e
 
c
o
l
l
e
c
t
o
r
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
e
r
f
o
r
m
a
n
c
e
C
o
l
l
e
c
t
o
r
'
,
 
I
P
e
r
f
o
r
m
a
n
c
e
C
o
l
l
e
c
t
o
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
h
c
p
_
s
e
r
v
e
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
D
H
C
P
S
e
r
v
e
r
 
v
a
l
u
e
 
f
o
r
 
'
D
H
C
P
S
e
r
v
e
r
s
'


 
 
 
 
 
 
 
 
D
H
C
P
 
s
e
r
v
e
r
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
D
H
C
P
S
e
r
v
e
r
s
'
,
 
I
D
H
C
P
S
e
r
v
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
a
t
_
n
e
t
w
o
r
k
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
N
A
T
N
e
t
w
o
r
k
 
v
a
l
u
e
 
f
o
r
 
'
N
A
T
N
e
t
w
o
r
k
s
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
N
A
T
N
e
t
w
o
r
k
s
'
,
 
I
N
A
T
N
e
t
w
o
r
k
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
v
e
n
t
_
s
o
u
r
c
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
E
v
e
n
t
S
o
u
r
c
e
 
v
a
l
u
e
 
f
o
r
 
'
e
v
e
n
t
S
o
u
r
c
e
'


 
 
 
 
 
 
 
 
E
v
e
n
t
 
s
o
u
r
c
e
 
f
o
r
 
V
i
r
t
u
a
l
B
o
x
 
e
v
e
n
t
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
v
e
n
t
S
o
u
r
c
e
'
,
 
I
E
v
e
n
t
S
o
u
r
c
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
x
t
e
n
s
i
o
n
_
p
a
c
k
_
m
a
n
a
g
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
E
x
t
P
a
c
k
M
a
n
a
g
e
r
 
v
a
l
u
e
 
f
o
r
 
'
e
x
t
e
n
s
i
o
n
P
a
c
k
M
a
n
a
g
e
r
'


 
 
 
 
 
 
 
 
T
h
e
 
e
x
t
e
n
s
i
o
n
 
p
a
c
k
 
m
a
n
a
g
e
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
x
t
e
n
s
i
o
n
P
a
c
k
M
a
n
a
g
e
r
'
,
 
I
E
x
t
P
a
c
k
M
a
n
a
g
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
n
t
e
r
n
a
l
_
n
e
t
w
o
r
k
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
i
n
t
e
r
n
a
l
N
e
t
w
o
r
k
s
'


 
 
 
 
 
 
 
 
N
a
m
e
s
 
o
f
 
a
l
l
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
n
t
e
r
n
a
l
N
e
t
w
o
r
k
s
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
e
n
e
r
i
c
_
n
e
t
w
o
r
k
_
d
r
i
v
e
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
g
e
n
e
r
i
c
N
e
t
w
o
r
k
D
r
i
v
e
r
s
'


 
 
 
 
 
 
 
 
N
a
m
e
s
 
o
f
 
a
l
l
 
g
e
n
e
r
i
c
 
n
e
t
w
o
r
k
 
d
r
i
v
e
r
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
e
n
e
r
i
c
N
e
t
w
o
r
k
D
r
i
v
e
r
s
'
,
 
s
t
r
)




 
 
 
 
d
e
f
 
c
o
m
p
o
s
e
_
m
a
c
h
i
n
e
_
f
i
l
e
n
a
m
e
(
s
e
l
f
,
 
n
a
m
e
,
 
g
r
o
u
p
,
 
c
r
e
a
t
e
_
f
l
a
g
s
,
 
b
a
s
e
_
f
o
l
d
e
r
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
r
e
c
o
m
m
e
n
d
e
d
 
f
u
l
l
 
p
a
t
h
 
o
f
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
n
a
m
e
 
f
o
r
 
a
 
n
e
w
 
v
i
r
t
u
a
l


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
T
h
i
s
 
A
P
I
 
s
e
r
v
e
s
 
t
w
o
 
p
u
r
p
o
s
e
s
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
t
 
g
e
t
s
 
c
a
l
l
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
i
f
 
@
c
 
n
u
l
l
 
o
r


 
 
 
 
 
 
 
 
 
 
 
 
e
m
p
t
y
 
s
t
r
i
n
g
 
(
w
h
i
c
h
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
)
 
i
s
 
s
p
e
c
i
f
i
e
d
 
f
o
r
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
s
e
t
t
i
n
g
s
F
i
l
e
 
a
r
g
u
m
e
n
t
 
t
h
e
r
e
,
 
w
h
i
c
h
 
m
e
a
n
s
 
t
h
a
t
 
A
P
I
 
s
h
o
u
l
d
 
u
s
e


 
 
 
 
 
 
 
 
 
 
 
 
a
 
r
e
c
o
m
m
e
n
d
e
d
 
d
e
f
a
u
l
t
 
f
i
l
e
 
n
a
m
e
.




 
 
 
 
 
 
 
 
 
 
I
t
 
c
a
n
 
b
e
 
c
a
l
l
e
d
 
m
a
n
u
a
l
l
y
 
b
y
 
a
 
c
l
i
e
n
t
 
s
o
f
t
w
a
r
e
 
b
e
f
o
r
e
 
c
r
e
a
t
i
n
g
 
a
 
m
a
c
h
i
n
e
,


 
 
 
 
 
 
 
 
 
 
 
 
e
.
g
.
 
i
f
 
t
h
a
t
 
c
l
i
e
n
t
 
w
a
n
t
s
 
t
o
 
p
r
e
-
c
r
e
a
t
e
 
t
h
e
 
m
a
c
h
i
n
e
 
d
i
r
e
c
t
o
r
y
 
t
o
 
c
r
e
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
h
a
r
d
 
d
i
s
k
s
 
i
n
 
t
h
a
t
 
d
i
r
e
c
t
o
r
y
 
t
o
g
e
t
h
e
r
 
w
i
t
h
 
t
h
e
 
n
e
w
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.
 
I
n
 
t
h
a
t
 
c
a
s
e
,
 
t
h
e
 
f
i
l
e
 
n
a
m
e
 
s
h
o
u
l
d
 
b
e
 
s
t
r
i
p
p
e
d
 
f
r
o
m
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
f
u
l
l
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
p
a
t
h
 
r
e
t
u
r
n
e
d
 
b
y
 
t
h
i
s
 
f
u
n
c
t
i
o
n
 
t
o
 
o
b
t
a
i
n
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
d
i
r
e
c
t
o
r
y
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
n
a
m
e
"
/
>
 
a
n
d
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
f
o
r
 
m
o
r
e


 
 
 
 
 
 
 
 
d
e
t
a
i
l
s
 
a
b
o
u
t
 
t
h
e
 
m
a
c
h
i
n
e
 
n
a
m
e
.




 
 
 
 
 
 
 
 
@
a
 
g
r
o
u
p
N
a
m
e
 
d
e
f
i
n
e
s
 
w
h
i
c
h
 
a
d
d
i
t
i
o
n
a
l
 
s
u
b
d
i
r
e
c
t
o
r
y
 
l
e
v
e
l
s
 
s
h
o
u
l
d
 
b
e


 
 
 
 
 
 
 
 
i
n
c
l
u
d
e
d
.
 
I
t
 
m
u
s
t
 
b
e
 
e
i
t
h
e
r
 
a
 
v
a
l
i
d
 
g
r
o
u
p
 
n
a
m
e
 
o
r
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
w
h
i
c
h
 
d
e
s
i
g
n
a
t
e
s
 
t
h
a
t
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
n
o
t
 
b
e
 
r
e
l
a
t
e
d
 
t
o
 
a


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
g
r
o
u
p
.




 
 
 
 
 
 
 
 
I
f
 
@
a
 
b
a
s
e
F
o
l
d
e
r
 
i
s
 
a
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
 
s
t
r
i
n
g
 
(
w
h
i
c
h
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
)
,
 
t
h
e


 
 
 
 
 
 
 
 
d
e
f
a
u
l
t
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
f
o
l
d
e
r


 
 
 
 
 
 
 
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
d
e
f
a
u
l
t
M
a
c
h
i
n
e
F
o
l
d
e
r
"
/
>
)
 
w
i
l
l
 
b
e
 
u
s
e
d
 
a
s


 
 
 
 
 
 
 
 
a
 
b
a
s
e
 
f
o
l
d
e
r
 
f
o
r
 
t
h
e
 
c
r
e
a
t
e
d
 
m
a
c
h
i
n
e
,
 
r
e
s
u
l
t
i
n
g
 
i
n
 
a
 
f
i
l
e
 
n
a
m
e
 
l
i
k
e


 
 
 
 
 
 
 
 
"
/
h
o
m
e
/
u
s
e
r
/
V
i
r
t
u
a
l
B
o
x
 
V
M
s
/
n
a
m
e
/
n
a
m
e
.
v
b
o
x
"
.
 
O
t
h
e
r
w
i
s
e
 
t
h
e
 
g
i
v
e
n
 
b
a
s
e
 
f
o
l
d
e
r


 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
u
s
e
d
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
d
o
e
s
 
n
o
t
 
a
c
c
e
s
s
 
t
h
e
 
h
o
s
t
 
d
i
s
k
s
.
 
I
n
 
p
a
r
t
i
c
u
l
a
r
,
 
i
t
 
d
o
e
s
 
n
o
t
 
c
h
e
c
k


 
 
 
 
 
 
 
 
f
o
r
 
w
h
e
t
h
e
r
 
a
 
m
a
c
h
i
n
e
 
w
i
t
h
 
t
h
i
s
 
n
a
m
e
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
S
u
g
g
e
s
t
e
d
 
m
a
c
h
i
n
e
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
g
r
o
u
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
g
r
o
u
p
 
n
a
m
e
 
f
o
r
 
t
h
e
 
n
e
w
 
m
a
c
h
i
n
e
 
o
r
 
m
a
c
h
i
n
e
 
g
r
o
u
p
.
 
I
t
 
i
s


 
 
 
 
 
 
 
 
u
s
e
d
 
t
o
 
d
e
t
e
r
m
i
n
e
 
t
h
e
 
r
i
g
h
t
 
s
u
b
d
i
r
e
c
t
o
r
y
.




 
 
 
 
 
 
 
 
i
n
 
c
r
e
a
t
e
_
f
l
a
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
c
r
e
a
t
i
o
n
 
f
l
a
g
s
,
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
(
o
p
t
i
o
n
a
l
)
.




 
 
 
 
 
 
 
 
i
n
 
b
a
s
e
_
f
o
l
d
e
r
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
B
a
s
e
 
m
a
c
h
i
n
e
 
f
o
l
d
e
r
 
(
o
p
t
i
o
n
a
l
)
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
e
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
u
l
l
y
 
q
u
a
l
i
f
i
e
d
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
m
a
c
h
i
n
e
 
w
o
u
l
d
 
b
e
 
c
r
e
a
t
e
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
f
i
l
e
_
p
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
o
m
p
o
s
e
M
a
c
h
i
n
e
F
i
l
e
n
a
m
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
g
r
o
u
p
,
 
c
r
e
a
t
e
_
f
l
a
g
s
,
 
b
a
s
e
_
f
o
l
d
e
r
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
e
_
p


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
m
a
c
h
i
n
e
(
s
e
l
f
,
 
s
e
t
t
i
n
g
s
_
f
i
l
e
,
 
n
a
m
e
,
 
g
r
o
u
p
s
,
 
o
s
_
t
y
p
e
_
i
d
,
 
f
l
a
g
s
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
n
e
w
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
b
y
 
c
r
e
a
t
i
n
g
 
a
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
a
t


 
 
 
 
 
 
 
 
t
h
e
 
g
i
v
e
n
 
l
o
c
a
t
i
o
n
.




 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
s
 
u
s
e
 
a
 
c
u
s
t
o
m
 
X
M
L
 
d
i
a
l
e
c
t
.
 
S
t
a
r
t
i
n
g


 
 
 
 
 
 
 
 
w
i
t
h
 
V
i
r
t
u
a
l
B
o
x
 
4
.
0
,
 
a
 
"
.
v
b
o
x
"
 
e
x
t
e
n
s
i
o
n
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
,
 
b
u
t
 
n
o
t
 
e
n
f
o
r
c
e
d
,


 
 
 
 
 
 
 
 
a
n
d
 
m
a
c
h
i
n
e
 
f
i
l
e
s
 
c
a
n
 
b
e
 
c
r
e
a
t
e
d
 
a
t
 
a
r
b
i
t
r
a
r
y
 
l
o
c
a
t
i
o
n
s
.




 
 
 
 
 
 
 
 
H
o
w
e
v
e
r
,
 
i
t
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
 
t
h
a
t
 
m
a
c
h
i
n
e
s
 
a
r
e
 
c
r
e
a
t
e
d
 
i
n
 
t
h
e
 
d
e
f
a
u
l
t


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
f
o
l
d
e
r
 
(
e
.
g
.
 
"
/
h
o
m
e
/
u
s
e
r
/
V
i
r
t
u
a
l
B
o
x
 
V
M
s
/
n
a
m
e
/
n
a
m
e
.
v
b
o
x
"
;
 
s
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
d
e
f
a
u
l
t
M
a
c
h
i
n
e
F
o
l
d
e
r
"
/
>
)
.
 
I
f
 
y
o
u
 
s
p
e
c
i
f
y


 
 
 
 
 
 
 
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
 
s
t
r
i
n
g
 
(
w
h
i
c
h
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
)
 
f
o
r
 
t
h
e
 
@
a
 
s
e
t
t
i
n
g
s
F
i
l
e


 
 
 
 
 
 
 
 
a
r
g
u
m
e
n
t
,
 
<
l
i
n
k
 
t
o
=
"
#
c
o
m
p
o
s
e
M
a
c
h
i
n
e
F
i
l
e
n
a
m
e
"
/
>
 
i
s
 
c
a
l
l
e
d
 
a
u
t
o
m
a
t
i
c
a
l
l
y


 
 
 
 
 
 
 
 
t
o
 
h
a
v
e
 
s
u
c
h
 
a
 
r
e
c
o
m
m
e
n
d
e
d
 
n
a
m
e
 
c
o
m
p
o
s
e
d
 
b
a
s
e
d
 
o
n
 
t
h
e
 
m
a
c
h
i
n
e
 
n
a
m
e


 
 
 
 
 
 
 
 
g
i
v
e
n
 
i
n
 
t
h
e
 
@
a
 
n
a
m
e
 
a
r
g
u
m
e
n
t
 
a
n
d
 
t
h
e
 
p
r
i
m
a
r
y
 
g
r
o
u
p
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
r
e
s
u
l
t
i
n
g
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
f
a
i
l
,


 
 
 
 
 
 
 
 
u
n
l
e
s
s
 
t
h
e
 
f
o
r
c
e
O
v
e
r
w
r
i
t
e
 
f
l
a
g
 
i
s
 
s
e
t
.




 
 
 
 
 
 
 
 
T
h
e
 
n
e
w
 
m
a
c
h
i
n
e
 
i
s
 
c
r
e
a
t
e
d
 
u
n
r
e
g
i
s
t
e
r
e
d
,
 
w
i
t
h
 
t
h
e
 
i
n
i
t
i
a
l
 
c
o
n
f
i
g
u
r
a
t
i
o
n


 
 
 
 
 
 
 
 
s
e
t
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
g
u
e
s
t
 
O
S
 
t
y
p
e
.
 
A
 
t
y
p
i
c
a
l
 
s
e
q
u
e
n
c
e
 
o
f


 
 
 
 
 
 
 
 
a
c
t
i
o
n
s
 
t
o
 
c
r
e
a
t
e
 
a
 
n
e
w
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
a
s
 
f
o
l
l
o
w
s
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
C
a
l
l
 
t
h
i
s
 
m
e
t
h
o
d
 
t
o
 
h
a
v
e
 
a
 
n
e
w
 
m
a
c
h
i
n
e
 
c
r
e
a
t
e
d
.
 
T
h
e
 
r
e
t
u
r
n
e
d
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
o
b
j
e
c
t
 
w
i
l
l
 
b
e
 
"
m
u
t
a
b
l
e
"
 
a
l
l
o
w
i
n
g
 
t
o
 
c
h
a
n
g
e
 
a
n
y
 
m
a
c
h
i
n
e
 
p
r
o
p
e
r
t
y
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
C
o
n
f
i
g
u
r
e
 
t
h
e
 
m
a
c
h
i
n
e
 
u
s
i
n
g
 
t
h
e
 
a
p
p
r
o
p
r
i
a
t
e
 
a
t
t
r
i
b
u
t
e
s
 
a
n
d
 
m
e
t
h
o
d
s
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
C
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
t
o
 
w
r
i
t
e
 
t
h
e
 
s
e
t
t
i
n
g
s


 
 
 
 
 
 
 
 
 
 
 
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
X
M
L
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.
 
T
h
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
o
f
 
t
h
e
 
n
e
w
l
y


 
 
 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
m
a
c
h
i
n
e
 
w
i
l
l
 
n
o
t
 
b
e
 
s
a
v
e
d
 
t
o
 
d
i
s
k
 
u
n
t
i
l
 
t
h
i
s
 
m
e
t
h
o
d
 
i
s


 
 
 
 
 
 
 
 
 
 
 
 
c
a
l
l
e
d
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
C
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
r
e
g
i
s
t
e
r
M
a
c
h
i
n
e
"
/
>
 
t
o
 
a
d
d
 
t
h
e
 
m
a
c
h
i
n
e
 
t
o
 
t
h
e
 
l
i
s
t


 
 
 
 
 
 
 
 
 
 
 
 
o
f
 
m
a
c
h
i
n
e
s
 
k
n
o
w
n
 
t
o
 
V
i
r
t
u
a
l
B
o
x
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
g
u
e
s
t
 
O
S
 
t
y
p
e
 
i
d
e
n
t
i
f
i
e
r
 
m
u
s
t
 
m
a
t
c
h
 
a
n
 
I
D
 
o
f
 
o
n
e
 
o
f
 
k
n
o
w
n


 
 
 
 
 
 
 
 
g
u
e
s
t
 
O
S
 
t
y
p
e
s
 
l
i
s
t
e
d
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
g
u
e
s
t
O
S
T
y
p
e
s
"
/
>


 
 
 
 
 
 
 
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
r
e
 
i
s
 
n
o
 
w
a
y
 
t
o
 
c
h
a
n
g
e
 
t
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
o
r


 
 
 
 
 
 
 
 
 
 
s
u
b
f
o
l
d
e
r
 
o
f
 
t
h
e
 
c
r
e
a
t
e
d
 
m
a
c
h
i
n
e
 
d
i
r
e
c
t
l
y
.




 
 
 
 
 
 
 
 
i
n
 
s
e
t
t
i
n
g
s
_
f
i
l
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
u
l
l
y
 
q
u
a
l
i
f
i
e
d
 
p
a
t
h
 
w
h
e
r
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
s
h
o
u
l
d
 
b
e
 
c
r
e
a
t
e
d
,


 
 
 
 
 
 
 
 
 
 
e
m
p
t
y
 
s
t
r
i
n
g
 
o
r
 
@
c
 
n
u
l
l
 
f
o
r
 
a
 
d
e
f
a
u
l
t
 
f
o
l
d
e
r
 
a
n
d
 
f
i
l
e
 
b
a
s
e
d
 
o
n
 
t
h
e


 
 
 
 
 
 
 
 
 
 
@
a
 
n
a
m
e
 
a
r
g
u
m
e
n
t
 
a
n
d
 
t
h
e
 
p
r
i
m
a
r
y
 
g
r
o
u
p
.


 
 
 
 
 
 
 
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
#
c
o
m
p
o
s
e
M
a
c
h
i
n
e
F
i
l
e
n
a
m
e
"
/
>
)
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
g
r
o
u
p
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
g
r
o
u
p
 
n
a
m
e
s
.
 
@
c
 
n
u
l
l
 
o
r
 
a
n
 
e
m
p
t
y
 
a
r
r
a
y
 
h
a
v
e
 
t
h
e
 
s
a
m
e


 
 
 
 
 
 
 
 
 
 
m
e
a
n
i
n
g
 
a
s
 
a
n
 
a
r
r
a
y
 
w
i
t
h
 
j
u
s
t
 
t
h
e
 
e
m
p
t
y
 
s
t
r
i
n
g
 
o
r
 
"
/
"
,
 
i
.
e
.


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
 
a
 
m
a
c
h
i
n
e
 
w
i
t
h
o
u
t
 
g
r
o
u
p
 
a
s
s
o
c
i
a
t
i
o
n
.




 
 
 
 
 
 
 
 
i
n
 
o
s
_
t
y
p
e
_
i
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
G
u
e
s
t
 
O
S
 
T
y
p
e
 
I
D
.




 
 
 
 
 
 
 
 
i
n
 
f
l
a
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
d
d
i
t
i
o
n
a
l
 
p
r
o
p
e
r
t
y
 
p
a
r
a
m
e
t
e
r
s
,
 
p
a
s
s
e
d
 
a
s
 
a
 
c
o
m
m
a
-
s
e
p
a
r
a
t
e
d
 
l
i
s
t
 
o
f


 
 
 
 
 
 
 
 
 
 
"
n
a
m
e
=
v
a
l
u
e
"
 
t
y
p
e
 
e
n
t
r
i
e
s
.
 
T
h
e
 
f
o
l
l
o
w
i
n
g
 
o
n
e
s
 
a
r
e
 
r
e
c
o
g
n
i
z
e
d
:


 
 
 
 
 
 
 
 
 
 
f
o
r
c
e
O
v
e
r
w
r
i
t
e
=
1
 
t
o
 
o
v
e
r
w
r
i
t
e
 
a
n
 
e
x
i
s
t
i
n
g
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s


 
 
 
 
 
 
 
 
 
 
f
i
l
e
,
 
U
U
I
D
=
<
u
u
i
d
>
 
t
o
 
s
p
e
c
i
f
y
 
a
 
m
a
c
h
i
n
e
 
U
U
I
D
 
a
n
d


 
 
 
 
 
 
 
 
 
 
d
i
r
e
c
t
o
r
y
I
n
c
l
u
d
e
s
U
U
I
D
=
1
 
t
o
 
s
w
i
t
c
h
 
t
o
 
a
 
s
p
e
c
i
a
l
 
V
M
 
d
i
r
e
c
t
o
r
y


 
 
 
 
 
 
 
 
 
 
n
a
m
i
n
g
 
s
c
h
e
m
e
 
w
h
i
c
h
 
s
h
o
u
l
d
 
n
o
t
 
b
e
 
u
s
e
d
 
u
n
l
e
s
s
 
n
e
c
e
s
s
a
r
y
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e
 
o
f
 
t
y
p
e
 
I
M
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
C
r
e
a
t
e
d
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
o
s
T
y
p
e
I
d
 
i
s
 
i
n
v
a
l
i
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
R
e
s
u
l
t
i
n
g
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
n
a
m
e
 
i
s
 
i
n
v
a
l
i
d
 
o
r
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
a
l
r
e
a
d
y


 
 
 
 
 
 
 
 
 
 
e
x
i
s
t
s
 
o
r
 
c
o
u
l
d
 
n
o
t
 
b
e
 
c
r
e
a
t
e
d
 
d
u
e
 
t
o
 
a
n
 
I
/
O
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
n
a
m
e
 
i
s
 
e
m
p
t
y
 
o
r
 
@
c
 
n
u
l
l
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
M
a
c
h
i
n
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
e
t
t
i
n
g
s
_
f
i
l
e
,
 
n
a
m
e
,
 
g
r
o
u
p
s
,
 
o
s
_
t
y
p
e
_
i
d
,
 
f
l
a
g
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
a
c
h
i
n
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
o
p
e
n
_
m
a
c
h
i
n
e
(
s
e
l
f
,
 
s
e
t
t
i
n
g
s
_
f
i
l
e
)
:


 
 
 
 
 
 
 
 
"
"
"
O
p
e
n
s
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
f
r
o
m
 
t
h
e
 
e
x
i
s
t
i
n
g
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 
T
h
e
 
o
p
e
n
e
d
 
m
a
c
h
i
n
e
 
r
e
m
a
i
n
s
 
u
n
r
e
g
i
s
t
e
r
e
d
 
u
n
t
i
l
 
y
o
u
 
c
a
l
l


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
r
e
g
i
s
t
e
r
M
a
c
h
i
n
e
"
/
>
.




 
 
 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
n
a
m
e
 
m
u
s
t
 
b
e
 
f
u
l
l
y
 
q
u
a
l
i
f
i
e
d
.


 
 
 
 
 
 
 
 
T
h
e
 
f
i
l
e
 
m
u
s
t
 
e
x
i
s
t
 
a
n
d
 
b
e
 
a
 
v
a
l
i
d
 
m
a
c
h
i
n
e
 
X
M
L
 
s
e
t
t
i
n
g
s
 
f
i
l
e


 
 
 
 
 
 
 
 
w
h
o
s
e
 
c
o
n
t
e
n
t
s
 
w
i
l
l
 
b
e
 
u
s
e
d
 
t
o
 
c
o
n
s
t
r
u
c
t
 
t
h
e
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
i
n
 
s
e
t
t
i
n
g
s
_
f
i
l
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e
 
o
f
 
t
y
p
e
 
I
M
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
O
p
e
n
e
d
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
a
m
e
 
i
n
v
a
l
i
d
,
 
n
o
t
 
f
o
u
n
d
 
o
r
 
s
h
a
r
i
n
g
 
v
i
o
l
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
o
p
e
n
M
a
c
h
i
n
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
e
t
t
i
n
g
s
_
f
i
l
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
a
c
h
i
n
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
g
i
s
t
e
r
_
m
a
c
h
i
n
e
(
s
e
l
f
,
 
m
a
c
h
i
n
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
g
i
s
t
e
r
s
 
t
h
e
 
m
a
c
h
i
n
e
 
p
r
e
v
i
o
u
s
l
y
 
c
r
e
a
t
e
d
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
o
r
 
o
p
e
n
e
d
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
o
p
e
n
M
a
c
h
i
n
e
"
/
>
 
w
i
t
h
i
n
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
l
l
a
t
i
o
n
.
 
A
f
t
e
r


 
 
 
 
 
 
 
 
s
u
c
c
e
s
s
f
u
l
 
m
e
t
h
o
d
 
i
n
v
o
c
a
t
i
o
n
,
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
R
e
g
i
s
t
e
r
e
d
E
v
e
n
t
"
/
>
 
e
v
e
n
t
 
i
s
 
f
i
r
e
d
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
m
p
l
i
c
i
t
l
y
 
c
a
l
l
s
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>


 
 
 
 
 
 
 
 
 
 
t
o
 
s
a
v
e
 
a
l
l
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
b
e
f
o
r
e
 
r
e
g
i
s
t
e
r
i
n
g
 
i
t
.




 
 
 
 
 
 
 
 
i
n
 
m
a
c
h
i
n
e
 
o
f
 
t
y
p
e
 
I
M
a
c
h
i
n
e




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
N
o
 
m
a
t
c
h
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
f
o
u
n
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
w
a
s
 
n
o
t
 
c
r
e
a
t
e
d
 
w
i
t
h
i
n
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
n
c
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
g
i
s
t
e
r
M
a
c
h
i
n
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
m
a
c
h
i
n
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
m
a
c
h
i
n
e
(
s
e
l
f
,
 
n
a
m
e
_
o
r
_
i
d
)
:


 
 
 
 
 
 
 
 
"
"
"
A
t
t
e
m
p
t
s
 
t
o
 
f
i
n
d
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
g
i
v
e
n
 
i
t
s
 
n
a
m
e
 
o
r
 
U
U
I
D
.




 
 
 
 
 
 
 
 
I
n
a
c
c
e
s
s
i
b
l
e
 
m
a
c
h
i
n
e
s
 
c
a
n
n
o
t
 
b
e
 
f
o
u
n
d
 
b
y
 
n
a
m
e
,
 
o
n
l
y
 
b
y
 
U
U
I
D
,
 
b
e
c
a
u
s
e
 
t
h
e
i
r
 
n
a
m
e


 
 
 
 
 
 
 
 
 
 
c
a
n
n
o
t
 
s
a
f
e
l
y
 
b
e
 
d
e
t
e
r
m
i
n
e
d
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
_
o
r
_
i
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
W
h
a
t
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.
 
T
h
i
s
 
c
a
n
 
e
i
t
h
e
r
 
b
e
 
t
h
e
 
U
U
I
D
 
o
r
 
t
h
e
 
n
a
m
e
 
o
f
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e
 
o
f
 
t
y
p
e
 
I
M
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
o
b
j
e
c
t
,
 
i
f
 
f
o
u
n
d
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
f
i
n
d
 
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
 
m
a
t
c
h
i
n
g
 
@
a
 
n
a
m
e
O
r
I
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
M
a
c
h
i
n
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
_
o
r
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
a
c
h
i
n
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
a
c
h
i
n
e
s
_
b
y
_
g
r
o
u
p
s
(
s
e
l
f
,
 
g
r
o
u
p
s
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
s
 
a
l
l
 
m
a
c
h
i
n
e
 
r
e
f
e
r
e
n
c
e
s
 
w
h
i
c
h
 
a
r
e
 
i
n
 
o
n
e
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
g
r
o
u
p
s
.




 
 
 
 
 
 
 
 
i
n
 
g
r
o
u
p
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
W
h
a
t
 
g
r
o
u
p
s
 
t
o
 
m
a
t
c
h
.
 
T
h
e
 
u
s
u
a
l
 
g
r
o
u
p
 
l
i
s
t
 
r
u
l
e
s
 
a
p
p
l
y
,
 
i
.
e
.


 
 
 
 
 
 
 
 
p
a
s
s
i
n
g
 
a
n
 
e
m
p
t
y
 
l
i
s
t
 
w
i
l
l
 
m
a
t
c
h
 
V
M
s
 
i
n
 
t
h
e
 
t
o
p
l
e
v
e
l
 
g
r
o
u
p
,
 
l
i
k
e
w
i
s
e


 
 
 
 
 
 
 
 
t
h
e
 
e
m
p
t
y
 
s
t
r
i
n
g
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e
s
 
o
f
 
t
y
p
e
 
I
M
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
A
l
l
 
m
a
c
h
i
n
e
s
 
w
h
i
c
h
 
m
a
t
c
h
e
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
a
c
h
i
n
e
s
B
y
G
r
o
u
p
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
g
r
o
u
p
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
a
c
h
i
n
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
a
c
h
i
n
e
_
s
t
a
t
e
s
(
s
e
l
f
,
 
m
a
c
h
i
n
e
s
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
s
 
t
h
e
 
s
t
a
t
e
 
o
f
 
s
e
v
e
r
a
l
 
m
a
c
h
i
n
e
s
 
i
n
 
a
 
s
i
n
g
l
e
 
o
p
e
r
a
t
i
o
n
.




 
 
 
 
 
 
 
 
i
n
 
m
a
c
h
i
n
e
s
 
o
f
 
t
y
p
e
 
I
M
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
A
r
r
a
y
 
w
i
t
h
 
t
h
e
 
m
a
c
h
i
n
e
 
r
e
f
e
r
e
n
c
e
s
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
a
t
e
s
 
o
f
 
t
y
p
e
 
M
a
c
h
i
n
e
S
t
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
s
t
a
t
e
s
,
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
t
a
t
e
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
a
c
h
i
n
e
S
t
a
t
e
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
m
a
c
h
i
n
e
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
M
a
c
h
i
n
e
S
t
a
t
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
a
t
e
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
a
p
p
l
i
a
n
c
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
n
e
w
 
a
p
p
l
i
a
n
c
e
 
o
b
j
e
c
t
,
 
w
h
i
c
h
 
r
e
p
r
e
s
e
n
t
s
 
a
n
 
a
p
p
l
i
a
n
c
e
 
i
n
 
t
h
e
 
O
p
e
n
 
V
i
r
t
u
a
l
 
M
a
c
h
i
n
e


 
 
 
 
 
 
 
 
F
o
r
m
a
t
 
(
O
V
F
)
.
 
T
h
i
s
 
c
a
n
 
t
h
e
n
 
b
e
 
u
s
e
d
 
t
o
 
i
m
p
o
r
t
 
a
n
 
O
V
F
 
a
p
p
l
i
a
n
c
e
 
i
n
t
o
 
V
i
r
t
u
a
l
B
o
x
 
o
r
 
t
o
 
e
x
p
o
r
t


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
s
 
a
s
 
a
n
 
O
V
F
 
a
p
p
l
i
a
n
c
e
;
 
s
e
e
 
t
h
e
 
d
o
c
u
m
e
n
t
a
t
i
o
n
 
f
o
r
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
"
/
>
 
f
o
r
 
d
e
t
a
i
l
s
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
p
p
l
i
a
n
c
e
 
o
f
 
t
y
p
e
 
I
A
p
p
l
i
a
n
c
e


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
a
p
p
l
i
a
n
c
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
a
p
p
l
i
a
n
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
A
p
p
l
i
a
n
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
A
p
p
l
i
a
n
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
p
p
l
i
a
n
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
h
a
r
d
_
d
i
s
k
(
s
e
l
f
,
 
f
o
r
m
a
t
_
p
,
 
l
o
c
a
t
i
o
n
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
n
e
w
 
b
a
s
e
 
m
e
d
i
u
m
 
o
b
j
e
c
t
 
t
h
a
t
 
w
i
l
l
 
u
s
e
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e


 
 
 
 
 
 
 
 
f
o
r
m
a
t
 
a
n
d
 
l
o
c
a
t
i
o
n
 
f
o
r
 
m
e
d
i
u
m
 
d
a
t
a
.




 
 
 
 
 
 
 
 
T
h
e
 
a
c
t
u
a
l
 
s
t
o
r
a
g
e
 
u
n
i
t
 
i
s
 
n
o
t
 
c
r
e
a
t
e
d
 
b
y
 
t
h
i
s
 
m
e
t
h
o
d
.
 
I
n
 
o
r
d
e
r
 
t
o


 
 
 
 
 
 
 
 
d
o
 
i
t
,
 
a
n
d
 
b
e
f
o
r
e
 
y
o
u
 
a
r
e
 
a
b
l
e
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
c
r
e
a
t
e
d
 
m
e
d
i
u
m
 
t
o


 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
,
 
y
o
u
 
m
u
s
t
 
c
a
l
l
 
o
n
e
 
o
f
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
m
e
t
h
o
d
s
 
t
o


 
 
 
 
 
 
 
 
a
l
l
o
c
a
t
e
 
a
 
f
o
r
m
a
t
-
s
p
e
c
i
f
i
c
 
s
t
o
r
a
g
e
 
u
n
i
t
 
a
t
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
o
c
a
t
i
o
n
:


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
c
r
e
a
t
e
B
a
s
e
S
t
o
r
a
g
e
"
/
>


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
c
r
e
a
t
e
D
i
f
f
S
t
o
r
a
g
e
"
/
>


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
S
o
m
e
 
m
e
d
i
u
m
 
a
t
t
r
i
b
u
t
e
s
,
 
s
u
c
h
 
a
s
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
i
d
"
/
>
,
 
m
a
y


 
 
 
 
 
 
 
 
r
e
m
a
i
n
 
u
n
i
n
i
t
i
a
l
i
z
e
d
 
u
n
t
i
l
 
t
h
e
 
m
e
d
i
u
m
 
s
t
o
r
a
g
e
 
u
n
i
t
 
i
s
 
s
u
c
c
e
s
s
f
u
l
l
y


 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
o
n
e
 
o
f
 
t
h
e
 
a
b
o
v
e
 
m
e
t
h
o
d
s
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
e
 
s
t
o
r
a
g
e
 
u
n
i
t
 
i
s
 
s
u
c
c
e
s
s
f
u
l
l
y
 
c
r
e
a
t
e
d
,
 
i
t
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
a
c
c
e
s
s
i
b
l
e
 
t
h
r
o
u
g
h
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
o
p
e
n
M
e
d
i
u
m
"
/
>
 
m
e
t
h
o
d
 
a
n
d
 
c
a
n


 
 
 
 
 
 
 
 
b
e
 
f
o
u
n
d
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
h
a
r
d
D
i
s
k
s
"
/
>
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
o
f
 
a
l
l
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
s
 
s
u
p
p
o
r
t
e
d
 
b
y
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
i
n
s
t
a
l
l
a
t
i
o
n
 
c
a
n
 
b
e
 
o
b
t
a
i
n
e
d
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
m
e
d
i
u
m
F
o
r
m
a
t
s
"
/
>
.
 
I
f
 
t
h
e
 
@
a
 
f
o
r
m
a
t


 
 
 
 
 
 
 
 
a
t
t
r
i
b
u
t
e
 
i
s
 
e
m
p
t
y
 
o
r
 
@
c
 
n
u
l
l
 
t
h
e
n
 
t
h
e
 
d
e
f
a
u
l
t
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
d
e
f
a
u
l
t
H
a
r
d
D
i
s
k
F
o
r
m
a
t
"
/
>
 
w
i
l
l


 
 
 
 
 
 
 
 
b
e
 
u
s
e
d
 
f
o
r
 
c
r
e
a
t
i
n
g
 
a
 
s
t
o
r
a
g
e
 
u
n
i
t
 
o
f
 
t
h
e
 
m
e
d
i
u
m
.




 
 
 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
f
o
r
m
a
t
 
o
f
 
t
h
e
 
l
o
c
a
t
i
o
n
 
s
t
r
i
n
g
 
i
s
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
 
s
p
e
c
i
f
i
c
.


 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
l
o
c
a
t
i
o
n
"
/
>
 
a
n
d
 
I
M
e
d
i
u
m
 
f
o
r
 
m
o
r
e
 
d
e
t
a
i
l
s
.




 
 
 
 
 
 
 
 
i
n
 
f
o
r
m
a
t
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
I
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
 
t
o
 
u
s
e
 
f
o
r
 
t
h
e
 
n
e
w
 
m
e
d
i
u
m
.




 
 
 
 
 
 
 
 
i
n
 
l
o
c
a
t
i
o
n
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
L
o
c
a
t
i
o
n
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
u
n
i
t
 
f
o
r
 
t
h
e
 
n
e
w
 
m
e
d
i
u
m
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
C
r
e
a
t
e
d
 
m
e
d
i
u
m
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
f
o
r
m
a
t
 
i
d
e
n
t
i
f
i
e
r
 
i
s
 
i
n
v
a
l
i
d
.
 
S
e
e


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
l
o
c
a
t
i
o
n
 
i
s
 
a
 
n
o
t
 
v
a
l
i
d
 
f
i
l
e
 
n
a
m
e
 
(
f
o
r
 
f
i
l
e
-
b
a
s
e
d
 
f
o
r
m
a
t
s
 
o
n
l
y
)
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
e
d
i
u
m
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
H
a
r
d
D
i
s
k
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
f
o
r
m
a
t
_
p
,
 
l
o
c
a
t
i
o
n
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
o
p
e
n
_
m
e
d
i
u
m
(
s
e
l
f
,
 
l
o
c
a
t
i
o
n
,
 
d
e
v
i
c
e
_
t
y
p
e
,
 
a
c
c
e
s
s
_
m
o
d
e
,
 
f
o
r
c
e
_
n
e
w
_
u
u
i
d
)
:


 
 
 
 
 
 
 
 
"
"
"
F
i
n
d
s
 
e
x
i
s
t
i
n
g
 
m
e
d
i
a
 
o
r
 
o
p
e
n
s
 
a
 
m
e
d
i
u
m
 
f
r
o
m
 
a
n
 
e
x
i
s
t
i
n
g
 
s
t
o
r
a
g
e
 
l
o
c
a
t
i
o
n
.




 
 
 
 
 
 
 
 
O
n
c
e
 
a
 
m
e
d
i
u
m
 
h
a
s
 
b
e
e
n
 
o
p
e
n
e
d
,
 
i
t
 
c
a
n
 
b
e
 
p
a
s
s
e
d
 
t
o
 
o
t
h
e
r
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
m
e
t
h
o
d
s
,
 
i
n
 
p
a
r
t
i
c
u
l
a
r
 
t
o
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
D
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
g
i
v
e
n
 
d
e
v
i
c
e
 
t
y
p
e
,
 
t
h
e
 
f
i
l
e
 
a
t
 
t
h
e
 
s
t
o
r
a
g
e
 
l
o
c
a
t
i
o
n


 
 
 
 
 
 
 
 
m
u
s
t
 
b
e
 
i
n
 
o
n
e
 
o
f
 
t
h
e
 
m
e
d
i
a
 
f
o
r
m
a
t
s
 
u
n
d
e
r
s
t
o
o
d
 
b
y
 
V
i
r
t
u
a
l
B
o
x
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
W
i
t
h
 
a
 
"
H
a
r
d
D
i
s
k
"
 
d
e
v
i
c
e
 
t
y
p
e
,
 
t
h
e
 
f
i
l
e
 
m
u
s
t
 
b
e
 
a
 
h
a
r
d
 
d
i
s
k
 
i
m
a
g
e


 
 
 
 
 
 
 
 
 
 
 
 
i
n
 
o
n
e
 
o
f
 
t
h
e
 
f
o
r
m
a
t
s
 
s
u
p
p
o
r
t
e
d
 
b
y
 
V
i
r
t
u
a
l
B
o
x
 
(
s
e
e


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
m
e
d
i
u
m
F
o
r
m
a
t
s
"
/
>
)
.


 
 
 
 
 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
i
s
 
m
e
t
h
o
d
 
s
u
c
c
e
e
d
s
,
 
i
f
 
t
h
e
 
m
e
d
i
u
m
 
i
s
 
a
 
b
a
s
e
 
m
e
d
i
u
m
,
 
i
t


 
 
 
 
 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
h
a
r
d
D
i
s
k
s
"
/
>
 
a
r
r
a
y
 
a
t
t
r
i
b
u
t
e
.
 


 
 
 
 
 
 
 
 
 
 
W
i
t
h
 
a
 
"
D
V
D
"
 
d
e
v
i
c
e
 
t
y
p
e
,
 
t
h
e
 
f
i
l
e
 
m
u
s
t
 
b
e
 
a
n
 
I
S
O
 
9
9
6
0
 
C
D
/
D
V
D
 
i
m
a
g
e
.


 
 
 
 
 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
i
s
 
m
e
t
h
o
d
 
s
u
c
c
e
e
d
s
,
 
t
h
e
 
m
e
d
i
u
m
 
w
i
l
l
 
b
e
 
a
d
d
e
d
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
D
V
D
I
m
a
g
e
s
"
/
>
 
a
r
r
a
y
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
 
 
 
 
 
 
W
i
t
h
 
a
 
"
F
l
o
p
p
y
"
 
d
e
v
i
c
e
 
t
y
p
e
,
 
t
h
e
 
f
i
l
e
 
m
u
s
t
 
b
e
 
a
n
 
R
A
W
 
f
l
o
p
p
y
 
i
m
a
g
e
.


 
 
 
 
 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
i
s
 
m
e
t
h
o
d
 
s
u
c
c
e
e
d
s
,
 
t
h
e
 
m
e
d
i
u
m
 
w
i
l
l
 
b
e
 
a
d
d
e
d
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
f
l
o
p
p
y
I
m
a
g
e
s
"
/
>
 
a
r
r
a
y
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
A
f
t
e
r
 
h
a
v
i
n
g
 
b
e
e
n
 
o
p
e
n
e
d
,
 
t
h
e
 
m
e
d
i
u
m
 
c
a
n
 
b
e
 
r
e
-
f
o
u
n
d
 
b
y
 
t
h
i
s
 
m
e
t
h
o
d


 
 
 
 
 
 
 
 
a
n
d
 
c
a
n
 
b
e
 
a
t
t
a
c
h
e
d
 
t
o
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
 
f
o
r


 
 
 
 
 
 
 
 
m
o
r
e
 
d
e
t
a
i
l
s
.




 
 
 
 
 
 
 
 
T
h
e
 
U
U
I
D
 
o
f
 
t
h
e
 
n
e
w
l
y
 
o
p
e
n
e
d
 
m
e
d
i
u
m
 
w
i
l
l
 
e
i
t
h
e
r
 
b
e
 
r
e
t
r
i
e
v
e
d
 
f
r
o
m
 
t
h
e


 
 
 
 
 
 
 
 
s
t
o
r
a
g
e
 
l
o
c
a
t
i
o
n
,
 
i
f
 
t
h
e
 
f
o
r
m
a
t
 
s
u
p
p
o
r
t
s
 
i
t
 
(
e
.
g
.
 
f
o
r
 
h
a
r
d
 
d
i
s
k
 
i
m
a
g
e
s
)
,


 
 
 
 
 
 
 
 
o
r
 
a
 
n
e
w
 
U
U
I
D
 
w
i
l
l
 
b
e
 
r
a
n
d
o
m
l
y
 
g
e
n
e
r
a
t
e
d
 
(
e
.
g
.
 
f
o
r
 
I
S
O
 
a
n
d
 
R
A
W
 
f
i
l
e
s
)
.


 
 
 
 
 
 
 
 
I
f
 
f
o
r
 
s
o
m
e
 
r
e
a
s
o
n
 
y
o
u
 
n
e
e
d
 
t
o
 
c
h
a
n
g
e
 
t
h
e
 
m
e
d
i
u
m
'
s
 
U
U
I
D
,
 
u
s
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
s
e
t
I
d
s
"
/
>
.




 
 
 
 
 
 
 
 
I
f
 
a
 
d
i
f
f
e
r
e
n
c
i
n
g
 
h
a
r
d
 
d
i
s
k
 
m
e
d
i
u
m
 
i
s
 
t
o
 
b
e
 
o
p
e
n
e
d
 
b
y
 
t
h
i
s
 
m
e
t
h
o
d
,
 
t
h
e


 
 
 
 
 
 
 
 
o
p
e
r
a
t
i
o
n
 
w
i
l
l
 
s
u
c
c
e
e
d
 
o
n
l
y
 
i
f
 
i
t
s
 
p
a
r
e
n
t
 
m
e
d
i
u
m
 
a
n
d
 
a
l
l
 
a
n
c
e
s
t
o
r
s
,


 
 
 
 
 
 
 
 
i
f
 
a
n
y
,
 
a
r
e
 
a
l
r
e
a
d
y
 
k
n
o
w
n
 
t
o
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
l
l
a
t
i
o
n
 
(
f
o
r
 
e
x
a
m
p
l
e
,


 
 
 
 
 
 
 
 
w
e
r
e
 
o
p
e
n
e
d
 
b
y
 
t
h
i
s
 
m
e
t
h
o
d
 
b
e
f
o
r
e
)
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
a
t
t
e
m
p
t
s
 
t
o
 
g
u
e
s
s
 
t
h
e
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 
b
y
 
r
e
a
d
i
n
g
 
m
e
d
i
u
m
 
d
a
t
a
 
a
t
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
o
c
a
t
i
o
n
.




 
 
 
 
 
 
 
 
I
f
 
@
a
 
a
c
c
e
s
s
M
o
d
e
 
i
s
 
R
e
a
d
W
r
i
t
e
 
(
w
h
i
c
h
 
i
t
 
s
h
o
u
l
d
 
b
e
 
f
o
r
 
h
a
r
d
 
d
i
s
k
s
 
a
n
d
 
f
l
o
p
p
i
e
s
)
,


 
 
 
 
 
 
 
 
t
h
e
 
i
m
a
g
e
 
i
s
 
o
p
e
n
e
d
 
f
o
r
 
r
e
a
d
/
w
r
i
t
e
 
a
c
c
e
s
s
 
a
n
d
 
m
u
s
t
 
h
a
v
e
 
a
c
c
o
r
d
i
n
g
 
p
e
r
m
i
s
s
i
o
n
s
,


 
 
 
 
 
 
 
 
a
s
 
V
i
r
t
u
a
l
B
o
x
 
m
a
y
 
a
c
t
u
a
l
l
y
 
w
r
i
t
e
 
s
t
a
t
u
s
 
i
n
f
o
r
m
a
t
i
o
n
 
i
n
t
o
 
t
h
e
 
d
i
s
k
'
s
 
m
e
t
a
d
a
t
a


 
 
 
 
 
 
 
 
s
e
c
t
i
o
n
s
.




 
 
 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
w
r
i
t
e
 
a
c
c
e
s
s
 
i
s
 
r
e
q
u
i
r
e
d
 
f
o
r
 
a
l
l
 
t
y
p
i
c
a
l
 
h
a
r
d
 
d
i
s
k
 
u
s
a
g
e
 
i
n
 
V
i
r
t
u
a
l
B
o
x
,


 
 
 
 
 
 
 
 
s
i
n
c
e
 
V
i
r
t
u
a
l
B
o
x
 
m
a
y
 
n
e
e
d
 
t
o
 
w
r
i
t
e
 
m
e
t
a
d
a
t
a
 
s
u
c
h
 
a
s
 
a
 
U
U
I
D
 
i
n
t
o
 
t
h
e
 
i
m
a
g
e
.


 
 
 
 
 
 
 
 
T
h
e
 
o
n
l
y
 
e
x
c
e
p
t
i
o
n
 
i
s
 
o
p
e
n
i
n
g
 
a
 
s
o
u
r
c
e
 
i
m
a
g
e
 
t
e
m
p
o
r
a
r
i
l
y
 
f
o
r
 
c
o
p
y
i
n
g
 
a
n
d


 
 
 
 
 
 
 
 
c
l
o
n
i
n
g
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
c
l
o
n
e
T
o
"
/
>
 
w
h
e
n
 
t
h
e
 
i
m
a
g
e
 
w
i
l
l
 
b
e
 
c
l
o
s
e
d


 
 
 
 
 
 
 
 
a
g
a
i
n
 
s
o
o
n
.




 
 
 
 
 
 
 
 
T
h
e
 
f
o
r
m
a
t
 
o
f
 
t
h
e
 
l
o
c
a
t
i
o
n
 
s
t
r
i
n
g
 
i
s
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
 
s
p
e
c
i
f
i
c
.
 
S
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
l
o
c
a
t
i
o
n
"
/
>
 
a
n
d
 
I
M
e
d
i
u
m
 
f
o
r
 
m
o
r
e
 
d
e
t
a
i
l
s
.




 
 
 
 
 
 
 
 
i
n
 
l
o
c
a
t
i
o
n
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
L
o
c
a
t
i
o
n
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
u
n
i
t
 
t
h
a
t
 
c
o
n
t
a
i
n
s
 
m
e
d
i
u
m
 
d
a
t
a
 
i
n
 
o
n
e
 
o
f


 
 
 
 
 
 
 
 
 
 
t
h
e
 
s
u
p
p
o
r
t
e
d
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
s
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
_
t
y
p
e
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
M
u
s
t
 
b
e
 
o
n
e
 
o
f
 
"
H
a
r
d
D
i
s
k
"
,
 
"
D
V
D
"
 
o
r
 
"
F
l
o
p
p
y
"
.




 
 
 
 
 
 
 
 
i
n
 
a
c
c
e
s
s
_
m
o
d
e
 
o
f
 
t
y
p
e
 
A
c
c
e
s
s
M
o
d
e


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
o
 
o
p
e
n
 
t
h
e
 
i
m
a
g
e
 
i
n
 
r
e
a
d
/
w
r
i
t
e
 
o
r
 
r
e
a
d
-
o
n
l
y
 
m
o
d
e
.
 
F
o
r


 
 
 
 
 
 
 
 
a
 
"
D
V
D
"
 
d
e
v
i
c
e
 
t
y
p
e
,
 
t
h
i
s
 
i
s
 
i
g
n
o
r
e
d
 
a
n
d
 
r
e
a
d
-
o
n
l
y
 
m
o
d
e
 
i
s
 
a
l
w
a
y
s
 
a
s
s
u
m
e
d
.




 
 
 
 
 
 
 
 
i
n
 
f
o
r
c
e
_
n
e
w
_
u
u
i
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
A
l
l
o
w
s
 
t
h
e
 
c
a
l
l
e
r
 
t
o
 
r
e
q
u
e
s
t
 
a
 
c
o
m
p
l
e
t
e
l
y
 
n
e
w
 
m
e
d
i
u
m
 
U
U
I
D
 
f
o
r


 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
i
m
a
g
e
 
w
h
i
c
h
 
i
s
 
t
o
 
b
e
 
o
p
e
n
e
d
.
 
U
s
e
f
u
l
 
i
f
 
o
n
e
 
i
n
t
e
n
d
s
 
t
o
 
o
p
e
n
 
a
n
 
e
x
a
c
t


 
 
 
 
 
 
 
 
 
 
 
c
o
p
y
 
o
f
 
a
 
p
r
e
v
i
o
u
s
l
y
 
o
p
e
n
e
d
 
i
m
a
g
e
,
 
a
s
 
t
h
i
s
 
w
o
u
l
d
 
n
o
r
m
a
l
l
y
 
f
a
i
l
 
d
u
e
 
t
o


 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
d
u
p
l
i
c
a
t
e
 
U
U
I
D
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
O
p
e
n
e
d
 
m
e
d
i
u
m
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
e
d
i
u
m
 
s
t
o
r
a
g
e
 
f
i
l
e
 
l
o
c
a
t
i
o
n
 
o
r
 
c
o
u
l
d
 
n
o
t
 
f
i
n
d
 
t
h
e
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
a
t
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
o
c
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
P
R
T
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
g
e
t
 
m
e
d
i
u
m
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
e
d
i
u
m
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
h
a
s
 
a
l
r
e
a
d
y
 
b
e
e
n
 
a
d
d
e
d
 
t
o
 
a
 
m
e
d
i
a
 
r
e
g
i
s
t
r
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
e
d
i
u
m
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
o
p
e
n
M
e
d
i
u
m
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
l
o
c
a
t
i
o
n
,
 
d
e
v
i
c
e
_
t
y
p
e
,
 
a
c
c
e
s
s
_
m
o
d
e
,
 
f
o
r
c
e
_
n
e
w
_
u
u
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
g
u
e
s
t
_
o
s
_
t
y
p
e
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
n
 
o
b
j
e
c
t
 
d
e
s
c
r
i
b
i
n
g
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
g
u
e
s
t
 
O
S
 
t
y
p
e
.




 
 
 
 
 
 
 
 
T
h
e
 
r
e
q
u
e
s
t
e
d
 
g
u
e
s
t
 
O
S
 
t
y
p
e
 
i
s
 
s
p
e
c
i
f
i
e
d
 
u
s
i
n
g
 
a
 
s
t
r
i
n
g
 
w
h
i
c
h
 
i
s
 
a


 
 
 
 
 
 
 
 
m
n
e
m
o
n
i
c
 
i
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
g
u
e
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
,
 
s
u
c
h
 
a
s


 
 
 
 
 
 
 
 
"
w
i
n
3
1
"
 
o
r
 
"
u
b
u
n
t
u
"
.
 
T
h
e
 
g
u
e
s
t
 
O
S
 
t
y
p
e
 
I
D
 
o
f
 
a


 
 
 
 
 
 
 
 
p
a
r
t
i
c
u
l
a
r
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
c
a
n
 
b
e
 
r
e
a
d
 
o
r
 
s
e
t
 
u
s
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
O
S
T
y
p
e
I
d
"
/
>
 
a
t
t
r
i
b
u
t
e
.




 
 
 
 
 
 
 
 
T
h
e
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
g
u
e
s
t
O
S
T
y
p
e
s
"
/
>
 
c
o
l
l
e
c
t
i
o
n
 
c
o
n
t
a
i
n
s
 
a
l
l


 
 
 
 
 
 
 
 
a
v
a
i
l
a
b
l
e
 
g
u
e
s
t
 
O
S
 
t
y
p
e
 
o
b
j
e
c
t
s
.
 
E
a
c
h
 
o
b
j
e
c
t
 
h
a
s
 
a
n


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
G
u
e
s
t
O
S
T
y
p
e
:
:
i
d
"
/
>
 
a
t
t
r
i
b
u
t
e
 
w
h
i
c
h
 
c
o
n
t
a
i
n
s
 
a
n
 
i
d
e
n
t
i
f
i
e
r
 
o
f


 
 
 
 
 
 
 
 
t
h
e
 
g
u
e
s
t
 
O
S
 
t
h
i
s
 
o
b
j
e
c
t
 
d
e
s
c
r
i
b
e
s
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
G
u
e
s
t
 
O
S
 
t
y
p
e
 
I
D
 
s
t
r
i
n
g
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
I
G
u
e
s
t
O
S
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
G
u
e
s
t
 
O
S
 
t
y
p
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
i
d
 
i
s
 
n
o
t
 
a
 
v
a
l
i
d
 
G
u
e
s
t
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
t
y
p
e
_
p
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
G
u
e
s
t
O
S
T
y
p
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
G
u
e
s
t
O
S
T
y
p
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
t
y
p
e
_
p


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
s
h
a
r
e
d
_
f
o
l
d
e
r
(
s
e
l
f
,
 
n
a
m
e
,
 
h
o
s
t
_
p
a
t
h
,
 
w
r
i
t
a
b
l
e
,
 
a
u
t
o
m
o
u
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
n
e
w
 
g
l
o
b
a
l
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
b
y
 
a
s
s
o
c
i
a
t
i
n
g
 
t
h
e
 
g
i
v
e
n
 
l
o
g
i
c
a
l


 
 
 
 
 
 
 
 
n
a
m
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
h
o
s
t
 
p
a
t
h
,
 
a
d
d
s
 
i
t
 
t
o
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
o
f
 
s
h
a
r
e
d


 
 
 
 
 
 
 
 
f
o
l
d
e
r
s
 
a
n
d
 
s
t
a
r
t
s
 
s
h
a
r
i
n
g
 
i
t
.
 
R
e
f
e
r
 
t
o
 
t
h
e
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
 
t
o
 
r
e
a
d
 
m
o
r
e
 
a
b
o
u
t
 
l
o
g
i
c
a
l
 
n
a
m
e
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
t
h
e
 
c
u
r
r
e
n
t
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
,
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
n
o
t


 
 
 
 
 
 
 
 
 
 
i
m
p
l
e
m
e
n
t
e
d
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
n
i
q
u
e
 
l
o
g
i
c
a
l
 
n
a
m
e
 
o
f
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
.




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
_
p
a
t
h
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
i
n
 
t
h
e
 
h
o
s
t
 
f
i
l
e
 
s
y
s
t
e
m
.




 
 
 
 
 
 
 
 
i
n
 
w
r
i
t
a
b
l
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
s
h
a
r
e
 
i
s
 
w
r
i
t
a
b
l
e
 
o
r
 
r
e
a
d
o
n
l
y




 
 
 
 
 
 
 
 
i
n
 
a
u
t
o
m
o
u
n
t
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
s
h
a
r
e
 
g
e
t
s
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
m
o
u
n
t
e
d
 
b
y
 
t
h
e
 
g
u
e
s
t


 
 
 
 
 
 
 
 
 
 
o
r
 
n
o
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
h
o
s
t
_
p
a
t
h
,
 
w
r
i
t
a
b
l
e
,
 
a
u
t
o
m
o
u
n
t
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
s
h
a
r
e
d
_
f
o
l
d
e
r
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
t
h
e
 
g
l
o
b
a
l
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
 
p
r
e
v
i
o
u
s
l
y


 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
 
f
r
o
m
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
n
d
 
s
t
o
p
s
 
s
h
a
r
i
n
g
 
i
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
t
h
e
 
c
u
r
r
e
n
t
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
,
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
n
o
t


 
 
 
 
 
 
 
 
 
 
i
m
p
l
e
m
e
n
t
e
d
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
L
o
g
i
c
a
l
 
n
a
m
e
 
o
f
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
t
o
 
r
e
m
o
v
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
S
h
a
r
e
d
F
o
l
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
e
x
t
r
a
_
d
a
t
a
_
k
e
y
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
n
 
a
r
r
a
y
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
g
l
o
b
a
l
 
e
x
t
r
a
 
d
a
t
a
 
k
e
y
s
 
w
h
i
c
h
 
c
u
r
r
e
n
t
l
y


 
 
 
 
 
 
 
 
h
a
v
e
 
v
a
l
u
e
s
 
d
e
f
i
n
e
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
k
e
y
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
e
x
t
r
a
 
d
a
t
a
 
k
e
y
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
k
e
y
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
E
x
t
r
a
D
a
t
a
K
e
y
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
k
e
y
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
e
x
t
r
a
_
d
a
t
a
(
s
e
l
f
,
 
k
e
y
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
s
s
o
c
i
a
t
e
d
 
g
l
o
b
a
l
 
e
x
t
r
a
 
d
a
t
a
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
r
e
q
u
e
s
t
e
d
 
d
a
t
a
 
@
a
 
k
e
y
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
,
 
t
h
i
s
 
f
u
n
c
t
i
o
n
 
w
i
l
l


 
 
 
 
 
 
 
 
s
u
c
c
e
e
d
 
a
n
d
 
r
e
t
u
r
n
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
n
 
t
h
e
 
@
a
 
v
a
l
u
e
 
a
r
g
u
m
e
n
t
.




 
 
 
 
 
 
 
 
i
n
 
k
e
y
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
d
a
t
a
 
k
e
y
 
t
o
 
g
e
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
V
a
l
u
e
 
o
f
 
t
h
e
 
r
e
q
u
e
s
t
e
d
 
d
a
t
a
 
k
e
y
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
E
x
t
r
a
D
a
t
a
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
k
e
y
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
e
x
t
r
a
_
d
a
t
a
(
s
e
l
f
,
 
k
e
y
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
a
s
s
o
c
i
a
t
e
d
 
g
l
o
b
a
l
 
e
x
t
r
a
 
d
a
t
a
.




 
 
 
 
 
 
 
 
I
f
 
y
o
u
 
p
a
s
s
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
 
s
t
r
i
n
g
 
a
s
 
a
 
k
e
y
 
@
a
 
v
a
l
u
e
,
 
t
h
e
 
g
i
v
e
n
 
@
a
 
k
e
y


 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
d
e
l
e
t
e
d
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
B
e
f
o
r
e
 
p
e
r
f
o
r
m
i
n
g
 
t
h
e
 
a
c
t
u
a
l
 
d
a
t
a
 
c
h
a
n
g
e
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
a
s
k
 
a
l
l


 
 
 
 
 
 
 
 
 
 
r
e
g
i
s
t
e
r
e
d
 
e
v
e
n
t
 
l
i
s
t
e
n
e
r
 
u
s
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
E
x
t
r
a
D
a
t
a
C
a
n
C
h
a
n
g
e
E
v
e
n
t
"
/
>


 
 
 
 
 
 
 
 
 
 
n
o
t
i
f
i
c
a
t
i
o
n
 
f
o
r
 
a
 
p
e
r
m
i
s
s
i
o
n
.
 
I
f
 
o
n
e
 
o
f
 
t
h
e
 
l
i
s
t
e
n
e
r
s
 
r
e
f
u
s
e
s
 
t
h
e


 
 
 
 
 
 
 
 
 
 
n
e
w
 
v
a
l
u
e
,
 
t
h
e
 
c
h
a
n
g
e
 
w
i
l
l
 
n
o
t
 
b
e
 
p
e
r
f
o
r
m
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
O
n
 
s
u
c
c
e
s
s
,
 
t
h
e


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
E
x
t
r
a
D
a
t
a
C
h
a
n
g
e
d
E
v
e
n
t
"
/
>
 
n
o
t
i
f
i
c
a
t
i
o
n


 
 
 
 
 
 
 
 
 
 
i
s
 
c
a
l
l
e
d
 
t
o
 
i
n
f
o
r
m
 
a
l
l
 
r
e
g
i
s
t
e
r
e
d
 
l
i
s
t
e
n
e
r
s
 
a
b
o
u
t
 
a
 
s
u
c
c
e
s
s
f
u
l
 
d
a
t
a


 
 
 
 
 
 
 
 
 
 
c
h
a
n
g
e
.




 
 
 
 
 
 
 
 
i
n
 
k
e
y
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
d
a
t
a
 
k
e
y
 
t
o
 
s
e
t
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
V
a
l
u
e
 
t
o
 
a
s
s
i
g
n
 
t
o
 
t
h
e
 
k
e
y
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
A
C
C
E
S
S
D
E
N
I
E
D


 
 
 
 
 
 
 
 
 
 
 
 
M
o
d
i
f
i
c
a
t
i
o
n
 
r
e
q
u
e
s
t
 
r
e
f
u
s
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
E
x
t
r
a
D
a
t
a
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
k
e
y
,
 
v
a
l
u
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
s
e
t
t
i
n
g
s
_
s
e
c
r
e
t
(
s
e
l
f
,
 
p
a
s
s
w
o
r
d
)
:


 
 
 
 
 
 
 
 
"
"
"
U
n
l
o
c
k
s
 
t
h
e
 
s
e
c
r
e
t
 
d
a
t
a
 
b
y
 
p
a
s
s
i
n
g
 
t
h
e
 
u
n
l
o
c
k
 
p
a
s
s
w
o
r
d
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
s
e
r
v
e
r
.
 
T
h
e
 
s
e
r
v
e
r
 
w
i
l
l
 
c
a
c
h
e
 
t
h
e
 
p
a
s
s
w
o
r
d
 
f
o
r
 
t
h
a
t
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
i
n
 
p
a
s
s
w
o
r
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
i
p
h
e
r
 
k
e
y
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
m
u
t
a
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
S
e
t
t
i
n
g
s
S
e
c
r
e
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
a
s
s
w
o
r
d
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
d
h
c
p
_
s
e
r
v
e
r
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
D
H
C
P
 
s
e
r
v
e
r
 
s
e
t
t
i
n
g
s
 
t
o
 
b
e
 
u
s
e
d
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
n
a
m
e




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
n
a
m
e




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
r
v
e
r
 
o
f
 
t
y
p
e
 
I
D
H
C
P
S
e
r
v
e
r


 
 
 
 
 
 
 
 
 
 
 
 
D
H
C
P
 
s
e
r
v
e
r
 
s
e
t
t
i
n
g
s




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
H
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
@
a
 
n
a
m
e
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
D
H
C
P
S
e
r
v
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
D
H
C
P
S
e
r
v
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
r
v
e
r


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
d
h
c
p
_
s
e
r
v
e
r
_
b
y
_
n
e
t
w
o
r
k
_
n
a
m
e
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
a
 
D
H
C
P
 
s
e
r
v
e
r
 
s
e
t
t
i
n
g
s
 
t
o
 
b
e
 
u
s
e
d
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
i
n
t
e
r
n
a
l
 
n
e
t
w
o
r
k
 
n
a
m
e




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
n
a
m
e




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
r
v
e
r
 
o
f
 
t
y
p
e
 
I
D
H
C
P
S
e
r
v
e
r


 
 
 
 
 
 
 
 
 
 
 
 
D
H
C
P
 
s
e
r
v
e
r
 
s
e
t
t
i
n
g
s




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
H
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
@
a
 
n
a
m
e
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
D
H
C
P
S
e
r
v
e
r
B
y
N
e
t
w
o
r
k
N
a
m
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
D
H
C
P
S
e
r
v
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
r
v
e
r


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
d
h
c
p
_
s
e
r
v
e
r
(
s
e
l
f
,
 
s
e
r
v
e
r
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
t
h
e
 
D
H
C
P
 
s
e
r
v
e
r
 
s
e
t
t
i
n
g
s




 
 
 
 
 
 
 
 
i
n
 
s
e
r
v
e
r
 
o
f
 
t
y
p
e
 
I
D
H
C
P
S
e
r
v
e
r


 
 
 
 
 
 
 
 
 
 
 
 
D
H
C
P
 
s
e
r
v
e
r
 
s
e
t
t
i
n
g
s
 
t
o
 
b
e
 
r
e
m
o
v
e
d




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
H
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
@
a
 
n
a
m
e
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
D
H
C
P
S
e
r
v
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
e
r
v
e
r
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
n
a
t
_
n
e
t
w
o
r
k
(
s
e
l
f
,
 
n
e
t
w
o
r
k
_
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
 
 
 
 
i
n
 
n
e
t
w
o
r
k
_
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
 
o
f
 
t
y
p
e
 
I
N
A
T
N
e
t
w
o
r
k




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
N
A
T
N
e
t
w
o
r
k
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
e
t
w
o
r
k
_
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
N
A
T
N
e
t
w
o
r
k
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
n
a
t
_
n
e
t
w
o
r
k
_
b
y
_
n
a
m
e
(
s
e
l
f
,
 
n
e
t
w
o
r
k
_
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
 
 
 
 
i
n
 
n
e
t
w
o
r
k
_
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
 
o
f
 
t
y
p
e
 
I
N
A
T
N
e
t
w
o
r
k




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
N
A
T
N
e
t
w
o
r
k
B
y
N
a
m
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
e
t
w
o
r
k
_
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
N
A
T
N
e
t
w
o
r
k
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
n
a
t
_
n
e
t
w
o
r
k
(
s
e
l
f
,
 
n
e
t
w
o
r
k
)
:


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
 
 
 
 
i
n
 
n
e
t
w
o
r
k
 
o
f
 
t
y
p
e
 
I
N
A
T
N
e
t
w
o
r
k




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
N
A
T
N
e
t
w
o
r
k
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
e
t
w
o
r
k
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
h
e
c
k
_
f
i
r
m
w
a
r
e
_
p
r
e
s
e
n
t
(
s
e
l
f
,
 
f
i
r
m
w
a
r
e
_
t
y
p
e
,
 
v
e
r
s
i
o
n
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
C
h
e
c
k
 
i
f
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
l
l
a
t
i
o
n
 
h
a
s
 
a
 
f
i
r
m
w
a
r
e


 
 
 
 
 
 
 
 
o
f
 
t
h
e
 
g
i
v
e
n
 
t
y
p
e
 
a
v
a
i
l
a
b
l
e
,
 
e
i
t
h
e
r
 
s
y
s
t
e
m
-
w
i
d
e
 
o
r
 
p
e
r
-
u
s
e
r
.


 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
l
y
,
 
t
h
i
s
 
m
a
y
 
r
e
t
u
r
n
 
a
 
h
i
n
t
 
w
h
e
r
e
 
t
h
i
s
 
f
i
r
m
w
a
r
e
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
d
o
w
n
l
o
a
d
e
d
 
f
r
o
m
.




 
 
 
 
 
 
 
 
i
n
 
f
i
r
m
w
a
r
e
_
t
y
p
e
 
o
f
 
t
y
p
e
 
F
i
r
m
w
a
r
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
f
i
r
m
w
a
r
e
 
t
o
 
c
h
e
c
k
.




 
 
 
 
 
 
 
 
i
n
 
v
e
r
s
i
o
n
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
E
x
p
e
c
t
e
d
 
v
e
r
s
i
o
n
 
n
u
m
b
e
r
,
 
u
s
u
a
l
l
y
 
e
m
p
t
y
 
s
t
r
i
n
g
 
(
p
r
e
s
e
n
t
l
y
 
i
g
n
o
r
e
d
)
.




 
 
 
 
 
 
 
 
o
u
t
 
u
r
l
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
S
u
g
g
e
s
t
e
d
 
U
R
L
 
t
o
 
d
o
w
n
l
o
a
d
 
t
h
i
s
 
f
i
r
m
w
a
r
e
 
f
r
o
m
.




 
 
 
 
 
 
 
 
o
u
t
 
f
i
l
e
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
i
l
e
n
a
m
e
 
o
f
 
f
i
r
m
w
a
r
e
,
 
o
n
l
y
 
v
a
l
i
d
 
i
f
 
r
e
s
u
l
t
 
=
=
 
T
R
U
E
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
f
i
r
m
w
a
r
e
 
o
f
 
t
h
i
s
 
t
y
p
e
 
a
n
d
 
v
e
r
s
i
o
n
 
i
s
 
a
v
a
i
l
a
b
l
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
h
e
c
k
F
i
r
m
w
a
r
e
P
r
e
s
e
n
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
f
i
r
m
w
a
r
e
_
t
y
p
e
,
 
v
e
r
s
i
o
n
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
V
F
S
E
x
p
l
o
r
e
r
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
V
F
S
E
x
p
l
o
r
e
r
 
i
n
t
e
r
f
a
c
e
 
u
n
i
f
i
e
s
 
a
c
c
e
s
s
 
t
o
 
d
i
f
f
e
r
e
n
t
 
f
i
l
e
 
s
y
s
t
e
m


 
 
 
 
 
 
t
y
p
e
s
.
 
T
h
i
s
 
i
n
c
l
u
d
e
s
 
l
o
c
a
l
 
f
i
l
e
 
s
y
s
t
e
m
s
 
a
s
 
w
e
l
l
 
r
e
m
o
t
e
 
f
i
l
e
 
s
y
s
t
e
m
s
 
l
i
k
e


 
 
 
 
 
 
S
3
.
 
F
o
r
 
a
 
l
i
s
t
 
o
f
 
s
u
p
p
o
r
t
e
d
 
t
y
p
e
s
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
V
F
S
T
y
p
e
"
/
>
.


 
 
 
 
 
 
A
n
 
i
n
s
t
a
n
c
e
 
o
f
 
t
h
i
s
 
i
s
 
r
e
t
u
r
n
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
:
:
c
r
e
a
t
e
V
F
S
E
x
p
l
o
r
e
r
"
/
>
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
0
0
3
d
7
f
9
2
-
d
3
8
e
-
4
8
7
f
-
b
7
9
0
-
8
c
5
e
8
6
3
1
c
b
2
f
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
a
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
p
a
t
h
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
c
u
r
r
e
n
t
 
p
a
t
h
 
i
n
 
t
h
e
 
v
i
r
t
u
a
l
 
f
i
l
e
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
a
t
h
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
y
p
e
_
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
V
F
S
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
t
y
p
e
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
f
i
l
e
 
s
y
s
t
e
m
 
t
y
p
e
 
w
h
i
c
h
 
i
s
 
c
u
r
r
e
n
t
l
y
 
i
n
 
u
s
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
y
p
e
'
,
 
V
F
S
T
y
p
e
)




 
 
 
 
d
e
f
 
u
p
d
a
t
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
U
p
d
a
t
e
s
 
t
h
e
 
i
n
t
e
r
n
a
l
 
l
i
s
t
 
o
f
 
f
i
l
e
s
/
d
i
r
e
c
t
o
r
i
e
s
 
f
r
o
m
 
t
h
e


 
 
 
 
 
 
c
u
r
r
e
n
t
 
d
i
r
e
c
t
o
r
y
 
l
e
v
e
l
.
 
U
s
e
 
<
l
i
n
k
 
t
o
=
"
#
e
n
t
r
y
L
i
s
t
"
/
>
 
t
o
 
g
e
t
 
t
h
e
 
f
u
l
l
 
l
i
s
t


 
 
 
 
 
 
a
f
t
e
r
 
a
 
c
a
l
l
 
t
o
 
t
h
i
s
 
m
e
t
h
o
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
u
p
d
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
d
(
s
e
l
f
,
 
d
i
r
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
C
h
a
n
g
e
 
t
h
e
 
c
u
r
r
e
n
t
 
d
i
r
e
c
t
o
r
y
 
l
e
v
e
l
.




 
 
 
 
 
 
 
 
i
n
 
d
i
r
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
d
i
r
e
c
t
o
r
y
 
t
o
 
g
o
 
i
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
d
i
r
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
d
_
u
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
o
 
o
n
e
 
d
i
r
e
c
t
o
r
y
 
u
p
w
a
r
d
s
 
f
r
o
m
 
t
h
e
 
c
u
r
r
e
n
t
 
d
i
r
e
c
t
o
r
y
 
l
e
v
e
l
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
d
U
p
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
t
r
y
_
l
i
s
t
(
s
e
l
f
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
l
i
s
t
 
o
f
 
f
i
l
e
s
/
d
i
r
e
c
t
o
r
i
e
s
 
a
f
t
e
r
 
a
 
c
a
l
l
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
u
p
d
a
t
e
"
/
>
.
 
T
h
e
 
u
s
e
r
 
i
s
 
r
e
s
p
o
n
s
i
b
l
e
 
f
o
r
 
k
e
e
p
i
n
g
 
t
h
i
s
 
i
n
t
e
r
n
a
l


 
 
 
 
 
 
l
i
s
t
 
u
p
 
d
o
 
d
a
t
e
.




 
 
 
 
 
 
 
 
o
u
t
 
n
a
m
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
o
f
 
n
a
m
e
s
 
f
o
r
 
t
h
e
 
e
n
t
r
i
e
s
.




 
 
 
 
 
 
 
 
o
u
t
 
t
y
p
e
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
o
f
 
t
y
p
e
s
 
f
o
r
 
t
h
e
 
e
n
t
r
i
e
s
.




 
 
 
 
 
 
 
 
o
u
t
 
s
i
z
e
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
o
f
 
s
i
z
e
s
 
(
i
n
 
b
y
t
e
s
)
 
f
o
r
 
t
h
e
 
e
n
t
r
i
e
s
.




 
 
 
 
 
 
 
 
o
u
t
 
m
o
d
e
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
o
f
 
f
i
l
e
 
m
o
d
e
s
 
(
i
n
 
o
c
t
a
l
 
f
o
r
m
)
 
f
o
r
 
t
h
e
 
e
n
t
r
i
e
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
t
r
y
L
i
s
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
x
i
s
t
s
(
s
e
l
f
,
 
n
a
m
e
s
)
:


 
 
 
 
 
 
 
 
"
"
"
C
h
e
c
k
s
 
i
f
 
t
h
e
 
g
i
v
e
n
 
f
i
l
e
 
l
i
s
t
 
e
x
i
s
t
s
 
i
n
 
t
h
e
 
c
u
r
r
e
n
t
 
d
i
r
e
c
t
o
r
y


 
 
 
 
 
 
l
e
v
e
l
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
s
 
t
o
 
c
h
e
c
k
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
x
i
s
t
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
s
 
w
h
i
c
h
 
e
x
i
s
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
e
x
i
s
t
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
x
i
s
t
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
x
i
s
t
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
(
s
e
l
f
,
 
n
a
m
e
s
)
:


 
 
 
 
 
 
 
 
"
"
"
D
e
l
e
t
e
s
 
t
h
e
 
g
i
v
e
n
 
f
i
l
e
s
 
i
n
 
t
h
e
 
c
u
r
r
e
n
t
 
d
i
r
e
c
t
o
r
y
 
l
e
v
e
l
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
s
 
t
o
 
r
e
m
o
v
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
A
p
p
l
i
a
n
c
e
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
R
e
p
r
e
s
e
n
t
s
 
a
 
p
l
a
t
f
o
r
m
-
i
n
d
e
p
e
n
d
e
n
t
 
a
p
p
l
i
a
n
c
e
 
i
n
 
O
V
F
 
f
o
r
m
a
t
.
 
A
n
 
i
n
s
t
a
n
c
e
 
o
f
 
t
h
i
s
 
i
s
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
A
p
p
l
i
a
n
c
e
"
/
>
,
 
w
h
i
c
h
 
c
a
n
 
t
h
e
n
 
b
e
 
u
s
e
d
 
t
o
 
i
m
p
o
r
t
 
a
n
d
 
e
x
p
o
r
t


 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
 
w
i
t
h
i
n
 
a
n
 
a
p
p
l
i
a
n
c
e
 
w
i
t
h
 
V
i
r
t
u
a
l
B
o
x
.




 
 
 
 
 
 
 
 
T
h
e
 
O
V
F
 
s
t
a
n
d
a
r
d
 
s
u
g
g
e
s
t
s
 
t
w
o
 
d
i
f
f
e
r
e
n
t
 
p
h
y
s
i
c
a
l
 
f
i
l
e
 
f
o
r
m
a
t
s
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
i
s
 
d
i
s
t
r
i
b
u
t
e
d
 
a
s
 
a
 
s
e
t
 
o
f
 
f
i
l
e
s
,
 
t
h
e
r
e
 
m
u
s
t
 
b
e
 
a
t
 
l
e
a
s
t
 
o
n
e
 
X
M
L
 
d
e
s
c
r
i
p
t
o
r


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
 
t
h
a
t
 
c
o
n
f
o
r
m
s
 
t
o
 
t
h
e
 
O
V
F
 
s
t
a
n
d
a
r
d
 
a
n
d
 
c
a
r
r
i
e
s
 
a
n
 
.
o
v
f
 
f
i
l
e
 
e
x
t
e
n
s
i
o
n
.
 
I
f


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
h
i
s
 
d
e
s
c
r
i
p
t
o
r
 
f
i
l
e
 
r
e
f
e
r
e
n
c
e
s
 
o
t
h
e
r
 
f
i
l
e
s
 
s
u
c
h
 
a
s
 
d
i
s
k
 
i
m
a
g
e
s
,
 
a
s
 
O
V
F
 
a
p
p
l
i
a
n
c
e
s
 
t
y
p
i
c
a
l
l
y


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
o
,
 
t
h
o
s
e
 
a
d
d
i
t
i
o
n
a
l
 
f
i
l
e
s
 
m
u
s
t
 
b
e
 
i
n
 
t
h
e
 
s
a
m
e
 
d
i
r
e
c
t
o
r
y
 
a
s
 
t
h
e
 
d
e
s
c
r
i
p
t
o
r
 
f
i
l
e
.




 
 
 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
i
s
 
d
i
s
t
r
i
b
u
t
e
d
 
a
s
 
a
 
s
i
n
g
l
e
 
f
i
l
e
,
 
i
t
 
m
u
s
t
 
b
e
 
i
n
 
T
A
R
 
f
o
r
m
a
t
 
a
n
d
 
h
a
v
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
o
v
a
 
f
i
l
e
 
e
x
t
e
n
s
i
o
n
.
 
T
h
i
s
 
T
A
R
 
f
i
l
e
 
m
u
s
t
 
t
h
e
n
 
c
o
n
t
a
i
n
 
a
t
 
l
e
a
s
t
 
t
h
e
 
O
V
F
 
d
e
s
c
r
i
p
t
o
r


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
s
 
a
n
d
 
o
p
t
i
o
n
a
l
l
y
 
o
t
h
e
r
 
f
i
l
e
s
.




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
A
t
 
t
h
i
s
 
t
i
m
e
,
 
V
i
r
t
u
a
l
B
o
x
 
d
o
e
s
 
n
o
t
 
n
o
t
 
y
e
t
 
s
u
p
p
o
r
t
 
t
h
e
 
p
a
c
k
e
d
 
(
T
A
R
)
 
v
a
r
i
a
n
t
;
 
s
u
p
p
o
r
t
 
w
i
l
l


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
e
 
a
d
d
e
d
 
w
i
t
h
 
a
 
l
a
t
e
r
 
v
e
r
s
i
o
n
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
I
m
p
o
r
t
i
n
g
 
a
n
 
O
V
F
 
a
p
p
l
i
a
n
c
e
 
i
n
t
o
 
V
i
r
t
u
a
l
B
o
x
 
a
s
 
i
n
s
t
a
n
c
e
s
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>
 
i
n
v
o
l
v
e
s
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
e
q
u
e
n
c
e
 
o
f
 
A
P
I
 
c
a
l
l
s
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
C
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
A
p
p
l
i
a
n
c
e
"
/
>
.
 
T
h
i
s
 
w
i
l
l
 
c
r
e
a
t
e
 
a
n
 
e
m
p
t
y
 
I
A
p
p
l
i
a
n
c
e
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
O
n
 
t
h
e
 
n
e
w
 
o
b
j
e
c
t
,
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
r
e
a
d
"
/
>
 
w
i
t
h
 
t
h
e
 
f
u
l
l
 
p
a
t
h
 
o
f
 
t
h
e
 
O
V
F
 
f
i
l
e
 
y
o
u


 
 
 
 
 
 
 
 
 
 
 
 
 
 
w
o
u
l
d
 
l
i
k
e
 
t
o
 
i
m
p
o
r
t
.
 
S
o
 
l
o
n
g
 
a
s
 
t
h
i
s
 
f
i
l
e
 
i
s
 
s
y
n
t
a
c
t
i
c
a
l
l
y
 
v
a
l
i
d
,
 
t
h
i
s
 
w
i
l
l
 
s
u
c
c
e
e
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
f
i
l
l
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
o
b
j
e
c
t
 
w
i
t
h
 
t
h
e
 
p
a
r
s
e
d
 
d
a
t
a
 
f
r
o
m
 
t
h
e
 
O
V
F
 
f
i
l
e
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
N
e
x
t
,
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
i
n
t
e
r
p
r
e
t
"
/
>
,
 
w
h
i
c
h
 
a
n
a
l
y
z
e
s
 
t
h
e
 
O
V
F
 
d
a
t
a
 
a
n
d
 
s
e
t
s
 
u
p
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
 
I
A
p
p
l
i
a
n
c
e
 
a
t
t
r
i
b
u
t
e
s
 
a
c
c
o
r
d
i
n
g
l
y
.
 
T
h
e
s
e
 
c
a
n
 
b
e
 
i
n
s
p
e
c
t
e
d
 
b
y
 
a


 
 
 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
 
f
r
o
n
t
-
e
n
d
 
s
u
c
h
 
a
s
 
t
h
e
 
G
U
I
,
 
a
n
d
 
t
h
e
 
s
u
g
g
e
s
t
i
o
n
s
 
c
a
n
 
b
e
 
d
i
s
p
l
a
y
e
d
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
u
s
e
r
.
 
I
n
 
p
a
r
t
i
c
u
l
a
r
,
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
v
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
s
"
/
>
 
a
r
r
a
y
 
c
o
n
t
a
i
n
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
s
t
a
n
c
e
s
 
o
f
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
"
/
>
 
w
h
i
c
h
 
r
e
p
r
e
s
e
n
t
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
 
 
 
 
 
 
 
 
s
y
s
t
e
m
s
 
(
m
a
c
h
i
n
e
s
)
 
i
n
 
t
h
e
 
O
V
F
,
 
w
h
i
c
h
 
i
n
 
t
u
r
n
 
d
e
s
c
r
i
b
e
 
t
h
e
 
v
i
r
t
u
a
l
 
h
a
r
d
w
a
r
e
 
p
r
e
s
c
r
i
b
e
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
y
 
t
h
e
 
O
V
F
 
(
n
e
t
w
o
r
k
 
a
n
d
 
h
a
r
d
w
a
r
e
 
a
d
a
p
t
e
r
s
,
 
v
i
r
t
u
a
l
 
d
i
s
k
 
i
m
a
g
e
s
,
 
m
e
m
o
r
y
 
s
i
z
e
 
a
n
d
 
s
o
 
o
n
)
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
G
U
I
 
c
a
n
 
t
h
e
n
 
g
i
v
e
 
t
h
e
 
u
s
e
r
 
t
h
e
 
o
p
t
i
o
n
 
t
o
 
c
o
n
f
i
r
m
 
a
n
d
/
o
r
 
c
h
a
n
g
e
 
t
h
e
s
e
 
s
u
g
g
e
s
t
i
o
n
s
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
I
f
 
d
e
s
i
r
e
d
,
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
:
:
s
e
t
F
i
n
a
l
V
a
l
u
e
s
"
/
>
 
f
o
r
 
e
a
c
h


 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
(
m
a
c
h
i
n
e
)
 
t
o
 
o
v
e
r
r
i
d
e
 
t
h
e
 
s
u
g
g
e
s
t
i
o
n
s
 
m
a
d
e
 
b
y
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
i
n
t
e
r
p
r
e
t
"
/
>
 
r
o
u
t
i
n
e
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
F
i
n
a
l
l
y
,
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
i
m
p
o
r
t
M
a
c
h
i
n
e
s
"
/
>
 
t
o
 
c
r
e
a
t
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
 
i
n


 
 
 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
 
a
s
 
i
n
s
t
a
n
c
e
s
 
o
f
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>
 
t
h
a
t
 
m
a
t
c
h
 
t
h
e
 
i
n
f
o
r
m
a
t
i
o
n
 
i
n
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
d
e
s
c
r
i
p
t
i
o
n
s
.
 
A
f
t
e
r
 
t
h
i
s
 
c
a
l
l
 
s
u
c
c
e
e
d
e
d
,
 
t
h
e
 
U
U
I
D
s
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
s
 
c
r
e
a
t
e
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
a
n
 
b
e
 
f
o
u
n
d
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
m
a
c
h
i
n
e
s
"
/
>
 
a
r
r
a
y
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
E
x
p
o
r
t
i
n
g
 
V
i
r
t
u
a
l
B
o
x
 
m
a
c
h
i
n
e
s
 
i
n
t
o
 
a
n
 
O
V
F
 
a
p
p
l
i
a
n
c
e
 
i
n
v
o
l
v
e
s
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
t
e
p
s
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
A
s
 
w
i
t
h
 
i
m
p
o
r
t
i
n
g
,
 
f
i
r
s
t
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
A
p
p
l
i
a
n
c
e
"
/
>
 
t
o
 
c
r
e
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
 
e
m
p
t
y
 
I
A
p
p
l
i
a
n
c
e
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
 
 
F
o
r
 
e
a
c
h
 
m
a
c
h
i
n
e
 
y
o
u
 
w
o
u
l
d
 
l
i
k
e
 
t
o
 
e
x
p
o
r
t
,
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
e
x
p
o
r
t
T
o
"
/
>


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
w
i
t
h
 
t
h
e
 
I
A
p
p
l
i
a
n
c
e
 
o
b
j
e
c
t
 
y
o
u
 
j
u
s
t
 
c
r
e
a
t
e
d
.
 
E
a
c
h
 
s
u
c
h
 
c
a
l
l
 
c
r
e
a
t
e
s
 
o
n
e
 
i
n
s
t
a
n
c
e
 
o
f


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
"
/
>
 
i
n
s
i
d
e
 
t
h
e
 
a
p
p
l
i
a
n
c
e
.


 
 
 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
d
e
s
i
r
e
d
,
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
:
:
s
e
t
F
i
n
a
l
V
a
l
u
e
s
"
/
>
 
f
o
r
 
e
a
c
h


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
(
m
a
c
h
i
n
e
)
 
t
o
 
o
v
e
r
r
i
d
e
 
t
h
e
 
s
u
g
g
e
s
t
i
o
n
s
 
m
a
d
e
 
b
y
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
e
x
p
o
r
t
T
o
"
/
>
 
r
o
u
t
i
n
e
.


 
 
 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
 
 
F
i
n
a
l
l
y
,
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
w
r
i
t
e
"
/
>
 
w
i
t
h
 
a
 
p
a
t
h
 
s
p
e
c
i
f
i
c
a
t
i
o
n
 
t
o
 
h
a
v
e
 
t
h
e
 
O
V
F


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
 
w
r
i
t
t
e
n
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
0
5
9
c
f
9
e
-
2
5
c
7
-
4
f
0
b
-
9
f
a
5
-
3
c
4
2
e
4
4
1
6
7
0
b
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
a
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
p
a
t
h
'


 
 
 
 
 
 
 
 
P
a
t
h
 
t
o
 
t
h
e
 
m
a
i
n
 
f
i
l
e
 
o
f
 
t
h
e
 
O
V
F
 
a
p
p
l
i
a
n
c
e
,
 
w
h
i
c
h
 
i
s
 
e
i
t
h
e
r
 
t
h
e
 
.
o
v
f
 
o
r


 
 
 
 
 
 
 
 
 
 
t
h
e
 
.
o
v
a
 
f
i
l
e
 
p
a
s
s
e
d
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
r
e
a
d
"
/
>
 
(
f
o
r
 
i
m
p
o
r
t
)
 
o
r


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
w
r
i
t
e
"
/
>
 
(
f
o
r
 
e
x
p
o
r
t
)
.


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
a
t
t
r
i
b
u
t
e
 
i
s
 
e
m
p
t
y
 
u
n
t
i
l
 
o
n
e
 
o
f
 
t
h
e
s
e
 
m
e
t
h
o
d
s
 
h
a
s
 
b
e
e
n
 
c
a
l
l
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
a
t
h
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
i
s
k
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
i
s
k
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
v
i
r
t
u
a
l
 
d
i
s
k
 
d
e
f
i
n
i
t
i
o
n
s
.
 
O
n
e
 
s
u
c
h
 
d
e
s
c
r
i
p
t
i
o
n
 
e
x
i
s
t
s
 
f
o
r
 
e
a
c
h


 
 
 
 
 
 
 
 
d
i
s
k
 
d
e
f
i
n
i
t
i
o
n
 
i
n
 
t
h
e
 
O
V
F
;
 
e
a
c
h
 
s
t
r
i
n
g
 
a
r
r
a
y
 
i
t
e
m
 
r
e
p
r
e
s
e
n
t
s
 
o
n
e
 
s
u
c
h
 
p
i
e
c
e
 
o
f


 
 
 
 
 
 
 
 
d
i
s
k
 
i
n
f
o
r
m
a
t
i
o
n
,
 
w
i
t
h
 
t
h
e
 
i
n
f
o
r
m
a
t
i
o
n
 
f
i
e
l
d
s
 
s
e
p
a
r
a
t
e
d
 
b
y
 
t
a
b
 
(
\
\
t
)
 
c
h
a
r
a
c
t
e
r
s
.




 
 
 
 
 
 
 
 
T
h
e
 
c
a
l
l
e
r
 
s
h
o
u
l
d
 
b
e
 
p
r
e
p
a
r
e
d
 
f
o
r
 
a
d
d
i
t
i
o
n
a
l
 
f
i
e
l
d
s
 
b
e
i
n
g
 
a
p
p
e
n
d
e
d
 
t
o


 
 
 
 
 
 
 
 
t
h
i
s
 
s
t
r
i
n
g
 
i
n
 
f
u
t
u
r
e
 
v
e
r
s
i
o
n
s
 
o
f
 
V
i
r
t
u
a
l
B
o
x
 
a
n
d
 
t
h
e
r
e
f
o
r
e
 
c
h
e
c
k
 
f
o
r


 
 
 
 
 
 
 
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
t
a
b
s
 
i
n
 
t
h
e
 
s
t
r
i
n
g
s
 
r
e
t
u
r
n
e
d
.




 
 
 
 
 
 
 
 
I
n
 
t
h
e
 
c
u
r
r
e
n
t
 
v
e
r
s
i
o
n
,
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
e
i
g
h
t
 
f
i
e
l
d
s
 
a
r
e
 
r
e
t
u
r
n
e
d
 
p
e
r
 
s
t
r
i
n
g


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
a
r
r
a
y
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
D
i
s
k
 
I
D
 
(
u
n
i
q
u
e
 
s
t
r
i
n
g
 
i
d
e
n
t
i
f
i
e
r
 
g
i
v
e
n
 
t
o
 
d
i
s
k
)




 
 
 
 
 
 
 
 
 
 
 
 
C
a
p
a
c
i
t
y
 
(
u
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
i
n
d
i
c
a
t
i
n
g
 
t
h
e
 
m
a
x
i
m
u
m
 
c
a
p
a
c
i
t
y
 
o
f
 
t
h
e
 
d
i
s
k
)




 
 
 
 
 
 
 
 
 
 
 
 
P
o
p
u
l
a
t
e
d
 
s
i
z
e
 
(
o
p
t
i
o
n
a
l
 
u
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
i
n
d
i
c
a
t
i
n
g
 
t
h
e
 
c
u
r
r
e
n
t
 
s
i
z
e
 
o
f
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
d
i
s
k
;
 
c
a
n
 
b
e
 
a
p
p
r
o
x
i
m
a
t
e
;
 
-
1
 
i
f
 
u
n
s
p
e
c
i
f
i
e
d
)




 
 
 
 
 
 
 
 
 
 
 
 
F
o
r
m
a
t
 
(
s
t
r
i
n
g
 
i
d
e
n
t
i
f
y
i
n
g
 
t
h
e
 
d
i
s
k
 
f
o
r
m
a
t
,
 
t
y
p
i
c
a
l
l
y


 
 
 
 
 
 
 
 
 
 
 
 
"
h
t
t
p
:
/
/
w
w
w
.
v
m
w
a
r
e
.
c
o
m
/
s
p
e
c
i
f
i
c
a
t
i
o
n
s
/
v
m
d
k
.
h
t
m
l
#
s
p
a
r
s
e
"
)




 
 
 
 
 
 
 
 
 
 
 
 
R
e
f
e
r
e
n
c
e
 
(
w
h
e
r
e
 
t
o
 
f
i
n
d
 
t
h
e
 
d
i
s
k
 
i
m
a
g
e
,
 
t
y
p
i
c
a
l
l
y
 
a
 
f
i
l
e
 
n
a
m
e
;
 
i
f
 
e
m
p
t
y
,


 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
n
 
t
h
e
 
d
i
s
k
 
s
h
o
u
l
d
 
b
e
 
c
r
e
a
t
e
d
 
o
n
 
i
m
p
o
r
t
)




 
 
 
 
 
 
 
 
 
 
 
 
I
m
a
g
e
 
s
i
z
e
 
(
o
p
t
i
o
n
a
l
 
u
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
i
n
d
i
c
a
t
i
n
g
 
t
h
e
 
s
i
z
e
 
o
f
 
t
h
e
 
i
m
a
g
e
,


 
 
 
 
 
 
 
 
 
 
 
 
w
h
i
c
h
 
n
e
e
d
 
n
o
t
 
n
e
c
e
s
s
a
r
i
l
y
 
b
e
 
t
h
e
 
s
a
m
e
 
a
s
 
t
h
e
 
v
a
l
u
e
s
 
s
p
e
c
i
f
i
e
d
 
a
b
o
v
e
,
 
s
i
n
c
e


 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
i
m
a
g
e
 
m
a
y
 
b
e
 
c
o
m
p
r
e
s
s
e
d
 
o
r
 
s
p
a
r
s
e
;
 
-
1
 
i
f
 
n
o
t
 
s
p
e
c
i
f
i
e
d
)




 
 
 
 
 
 
 
 
 
 
 
 
C
h
u
n
k
 
s
i
z
e
 
(
o
p
t
i
o
n
a
l
 
u
n
s
i
g
n
e
d
 
i
n
t
e
g
e
r
 
i
f
 
t
h
e
 
i
m
a
g
e
 
i
s
 
s
p
l
i
t
 
i
n
t
o
 
c
h
u
n
k
s
;


 
 
 
 
 
 
 
 
 
 
 
 
p
r
e
s
e
n
t
l
y
 
u
n
s
u
p
p
o
r
t
e
d
 
a
n
d
 
a
l
w
a
y
s
 
-
1
)




 
 
 
 
 
 
 
 
 
 
 
 
C
o
m
p
r
e
s
s
i
o
n
 
(
o
p
t
i
o
n
a
l
 
s
t
r
i
n
g
 
e
q
u
a
l
l
i
n
g
 
"
g
z
i
p
"
 
i
f
 
t
h
e
 
i
m
a
g
e
 
i
s
 
g
z
i
p
-
c
o
m
p
r
e
s
s
e
d
)


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
i
s
k
s
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
r
t
u
a
l
_
s
y
s
t
e
m
_
d
e
s
c
r
i
p
t
i
o
n
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
 
v
a
l
u
e
 
f
o
r
 
'
v
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
d
e
s
c
r
i
p
t
i
o
n
s
.
 
O
n
e
 
s
u
c
h
 
d
e
s
c
r
i
p
t
i
o
n
 
i
s
 
c
r
e
a
t
e
d


 
 
 
 
 
 
f
o
r
 
e
a
c
h
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
(
m
a
c
h
i
n
e
)
 
f
o
u
n
d
 
i
n
 
t
h
e
 
O
V
F
.


 
 
 
 
 
 
T
h
i
s
 
a
r
r
a
y
 
i
s
 
e
m
p
t
y
 
u
n
t
i
l
 
e
i
t
h
e
r
 
<
l
i
n
k
 
t
o
=
"
#
i
n
t
e
r
p
r
e
t
"
/
>
 
(
f
o
r
 
i
m
p
o
r
t
)
 
o
r
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
e
x
p
o
r
t
T
o
"
/
>


 
 
 
 
 
 
(
f
o
r
 
e
x
p
o
r
t
)
 
h
a
s
 
b
e
e
n
 
c
a
l
l
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
v
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
s
'
,
 
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
c
h
i
n
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
m
a
c
h
i
n
e
s
'


 
 
 
 
 
 
 
 
C
o
n
t
a
i
n
s
 
t
h
e
 
U
U
I
D
s
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
s
 
c
r
e
a
t
e
d
 
f
r
o
m
 
t
h
e
 
i
n
f
o
r
m
a
t
i
o
n
 
i
n
 
t
h
i
s
 
a
p
p
l
i
a
n
c
e
s
.
 
T
h
i
s
 
i
s
 
o
n
l
y


 
 
 
 
 
 
 
 
r
e
l
e
v
a
n
t
 
f
o
r
 
t
h
e
 
i
m
p
o
r
t
 
c
a
s
e
,
 
a
n
d
 
w
i
l
l
 
o
n
l
y
 
c
o
n
t
a
i
n
 
d
a
t
a
 
a
f
t
e
r
 
a
 
c
a
l
l
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
i
m
p
o
r
t
M
a
c
h
i
n
e
s
"
/
>


 
 
 
 
 
 
 
 
s
u
c
c
e
e
d
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
c
h
i
n
e
s
'
,
 
s
t
r
)




 
 
 
 
d
e
f
 
r
e
a
d
(
s
e
l
f
,
 
f
i
l
e
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
a
d
s
 
a
n
 
O
V
F
 
f
i
l
e
 
i
n
t
o
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
s
u
c
c
e
e
d
s
 
i
f
 
t
h
e
 
O
V
F
 
i
s
 
s
y
n
t
a
c
t
i
c
a
l
l
y
 
v
a
l
i
d
 
a
n
d
,
 
b
y
 
i
t
s
e
l
f
,
 
w
i
t
h
o
u
t
 
e
r
r
o
r
s
.
 
T
h
e


 
 
 
 
 
 
 
 
m
e
r
e
 
f
a
c
t
 
t
h
a
t
 
t
h
i
s
 
m
e
t
h
o
d
 
r
e
t
u
r
n
s
 
s
u
c
c
e
s
s
f
u
l
l
y
 
d
o
e
s
 
n
o
t
 
m
e
a
n
 
t
h
a
t
 
V
i
r
t
u
a
l
B
o
x
 
s
u
p
p
o
r
t
s
 
a
l
l


 
 
 
 
 
 
 
 
f
e
a
t
u
r
e
s
 
r
e
q
u
e
s
t
e
d
 
b
y
 
t
h
e
 
a
p
p
l
i
a
n
c
e
;
 
t
h
i
s
 
c
a
n
 
o
n
l
y
 
b
e
 
e
x
a
m
i
n
e
d
 
a
f
t
e
r
 
a
 
c
a
l
l
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
i
n
t
e
r
p
r
e
t
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
f
i
l
e
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
a
p
p
l
i
a
n
c
e
 
f
i
l
e
 
t
o
 
o
p
e
n
 
(
e
i
t
h
e
r
 
w
i
t
h
 
a
n
 
.
o
v
f
 
o
r
 
.
o
v
a
 
e
x
t
e
n
s
i
o
n
,
 
d
e
p
e
n
d
i
n
g


 
 
 
 
 
 
 
 
 
 
o
n
 
w
h
e
t
h
e
r
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
i
s
 
d
i
s
t
r
i
b
u
t
e
d
 
a
s
 
a
 
s
e
t
 
o
f
 
f
i
l
e
s
 
o
r
 
a
s
 
a
 
s
i
n
g
l
e
 
f
i
l
e
,
 
r
e
s
p
e
c
t
i
v
e
l
y
)
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
a
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
f
i
l
e
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
i
n
t
e
r
p
r
e
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
I
n
t
e
r
p
r
e
t
s
 
t
h
e
 
O
V
F
 
d
a
t
a
 
t
h
a
t
 
w
a
s
 
r
e
a
d
 
w
h
e
n
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
w
a
s
 
c
o
n
s
t
r
u
c
t
e
d
.
 
A
f
t
e
r


 
 
 
 
 
 
 
 
c
a
l
l
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
,
 
o
n
e
 
c
a
n
 
i
n
s
p
e
c
t
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
v
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
s
"
/
>
 
a
r
r
a
y
 
a
t
t
r
i
b
u
t
e
,
 
w
h
i
c
h
 
w
i
l
l
 
t
h
e
n
 
c
o
n
t
a
i
n


 
 
 
 
 
 
 
 
o
n
e
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
"
/
>
 
f
o
r
 
e
a
c
h
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
f
o
u
n
d
 
i
n


 
 
 
 
 
 
 
 
t
h
e
 
a
p
p
l
i
a
n
c
e
.




 
 
 
 
 
 
 
 
C
a
l
l
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
 
i
s
 
t
h
e
 
s
e
c
o
n
d
 
s
t
e
p
 
o
f
 
i
m
p
o
r
t
i
n
g
 
a
n
 
a
p
p
l
i
a
n
c
e
 
i
n
t
o
 
V
i
r
t
u
a
l
B
o
x
;


 
 
 
 
 
 
 
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
"
/
>
 
f
o
r
 
a
n
 
o
v
e
r
v
i
e
w
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
c
a
l
l
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
,
 
o
n
e
 
s
h
o
u
l
d
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
W
a
r
n
i
n
g
s
"
/
>
 
t
o
 
f
i
n
d
 
o
u
t


 
 
 
 
 
 
 
 
i
f
 
p
r
o
b
l
e
m
s
 
w
e
r
e
 
e
n
c
o
u
n
t
e
r
e
d
 
d
u
r
i
n
g
 
t
h
e
 
p
r
o
c
e
s
s
i
n
g
 
w
h
i
c
h
 
m
i
g
h
t
 
l
a
t
e
r
 
l
e
a
d
 
t
o


 
 
 
 
 
 
 
 
e
r
r
o
r
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
i
n
t
e
r
p
r
e
t
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
i
m
p
o
r
t
_
m
a
c
h
i
n
e
s
(
s
e
l
f
,
 
o
p
t
i
o
n
s
)
:


 
 
 
 
 
 
 
 
"
"
"
I
m
p
o
r
t
s
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
i
n
t
o
 
V
i
r
t
u
a
l
B
o
x
 
b
y
 
c
r
e
a
t
i
n
g
 
i
n
s
t
a
n
c
e
s
 
o
f
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>


 
 
 
 
 
 
 
 
a
n
d
 
o
t
h
e
r
 
i
n
t
e
r
f
a
c
e
s
 
t
h
a
t
 
m
a
t
c
h
 
t
h
e
 
i
n
f
o
r
m
a
t
i
o
n
 
c
o
n
t
a
i
n
e
d
 
i
n
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
a
s


 
 
 
 
 
 
 
 
c
l
o
s
e
l
y
 
a
s
 
p
o
s
s
i
b
l
e
,
 
a
s
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
t
h
e
 
i
m
p
o
r
t
 
i
n
s
t
r
u
c
t
i
o
n
s
 
i
n
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
v
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
s
"
/
>
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
C
a
l
l
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
 
i
s
 
t
h
e
 
f
i
n
a
l
 
s
t
e
p
 
o
f
 
i
m
p
o
r
t
i
n
g
 
a
n
 
a
p
p
l
i
a
n
c
e
 
i
n
t
o
 
V
i
r
t
u
a
l
B
o
x
;


 
 
 
 
 
 
 
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
"
/
>
 
f
o
r
 
a
n
 
o
v
e
r
v
i
e
w
.




 
 
 
 
 
 
 
 
S
i
n
c
e
 
i
m
p
o
r
t
i
n
g
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
w
i
l
l
 
m
o
s
t
 
p
r
o
b
a
b
l
y
 
i
n
v
o
l
v
e
 
c
o
p
y
i
n
g
 
a
n
d
 
c
o
n
v
e
r
t
i
n
g


 
 
 
 
 
 
 
 
d
i
s
k
 
i
m
a
g
e
s
,
 
w
h
i
c
h
 
c
a
n
 
t
a
k
e
 
a
 
l
o
n
g
 
t
i
m
e
,
 
t
h
i
s
 
m
e
t
h
o
d
 
o
p
e
r
a
t
e
s
 
a
s
y
n
c
h
r
o
n
o
u
s
l
y
 
a
n
d


 
 
 
 
 
 
 
 
r
e
t
u
r
n
s
 
a
n
 
I
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
a
l
l
o
w
 
t
h
e
 
c
a
l
l
e
r
 
t
o
 
m
o
n
i
t
o
r
 
t
h
e
 
p
r
o
g
r
e
s
s
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
e
 
i
m
p
o
r
t
 
s
u
c
c
e
e
d
e
d
,
 
t
h
e
 
U
U
I
D
s
 
o
f
 
t
h
e
 
I
M
a
c
h
i
n
e
 
i
n
s
t
a
n
c
e
s
 
c
r
e
a
t
e
d
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
r
e
t
r
i
e
v
e
d
 
f
r
o
m
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
m
a
c
h
i
n
e
s
"
/
>
 
a
r
r
a
y
 
a
t
t
r
i
b
u
t
e
.




 
 
 
 
 
 
 
 
i
n
 
o
p
t
i
o
n
s
 
o
f
 
t
y
p
e
 
I
m
p
o
r
t
O
p
t
i
o
n
s


 
 
 
 
 
 
 
 
 
 
 
 
O
p
t
i
o
n
s
 
f
o
r
 
t
h
e
 
i
m
p
o
r
t
i
n
g
 
o
p
e
r
a
t
i
o
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
i
m
p
o
r
t
M
a
c
h
i
n
e
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
o
p
t
i
o
n
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
v
f
s
_
e
x
p
l
o
r
e
r
(
s
e
l
f
,
 
u
r
i
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
<
l
i
n
k
 
t
o
=
"
I
V
F
S
E
x
p
l
o
r
e
r
"
/
>
 
o
b
j
e
c
t
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
U
R
I
.




 
 
 
 
 
 
 
 
i
n
 
u
r
i
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
U
R
I
 
d
e
s
c
r
i
b
i
n
g
 
t
h
e
 
f
i
l
e
 
s
y
s
t
e
m
 
t
o
 
u
s
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
x
p
l
o
r
e
r
 
o
f
 
t
y
p
e
 
I
V
F
S
E
x
p
l
o
r
e
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
e
x
p
l
o
r
e
r
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
V
F
S
E
x
p
l
o
r
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
u
r
i
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
V
F
S
E
x
p
l
o
r
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
x
p
l
o
r
e
r


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
w
r
i
t
e
(
s
e
l
f
,
 
f
o
r
m
a
t
_
p
,
 
m
a
n
i
f
e
s
t
,
 
p
a
t
h
)
:


 
 
 
 
 
 
 
 
"
"
"
W
r
i
t
e
s
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
e
x
p
o
r
t
s
 
i
n
t
o
 
a
 
n
e
w
 
O
V
F
 
f
i
l
e
.




 
 
 
 
 
 
 
 
 
 
C
a
l
l
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
 
i
s
 
t
h
e
 
f
i
n
a
l
 
s
t
e
p
 
o
f
 
e
x
p
o
r
t
i
n
g
 
a
n
 
a
p
p
l
i
a
n
c
e
 
f
r
o
m
 
V
i
r
t
u
a
l
B
o
x
;


 
 
 
 
 
 
 
 
 
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
"
/
>
 
f
o
r
 
a
n
 
o
v
e
r
v
i
e
w
.




 
 
 
 
 
 
 
 
 
 
S
i
n
c
e
 
e
x
p
o
r
t
i
n
g
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
w
i
l
l
 
m
o
s
t
 
p
r
o
b
a
b
l
y
 
i
n
v
o
l
v
e
 
c
o
p
y
i
n
g
 
a
n
d
 
c
o
n
v
e
r
t
i
n
g


 
 
 
 
 
 
 
 
 
 
d
i
s
k
 
i
m
a
g
e
s
,
 
w
h
i
c
h
 
c
a
n
 
t
a
k
e
 
a
 
l
o
n
g
 
t
i
m
e
,
 
t
h
i
s
 
m
e
t
h
o
d
 
o
p
e
r
a
t
e
s
 
a
s
y
n
c
h
r
o
n
o
u
s
l
y
 
a
n
d


 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
s
 
a
n
 
I
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
a
l
l
o
w
 
t
h
e
 
c
a
l
l
e
r
 
t
o
 
m
o
n
i
t
o
r
 
t
h
e
 
p
r
o
g
r
e
s
s
.




 
 
 
 
 
 
 
 
i
n
 
f
o
r
m
a
t
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
O
u
t
p
u
t
 
f
o
r
m
a
t
,
 
a
s
 
a
 
s
t
r
i
n
g
.
 
C
u
r
r
e
n
t
l
y
 
s
u
p
p
o
r
t
e
d
 
f
o
r
m
a
t
s
 
a
r
e
 
"
o
v
f
-
0
.
9
"
,
 
"
o
v
f
-
1
.
0
"


 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
"
o
v
f
-
2
.
0
"
;
 
f
u
t
u
r
e
 
v
e
r
s
i
o
n
s
 
o
f
 
V
i
r
t
u
a
l
B
o
x
 
m
a
y
 
s
u
p
p
o
r
t
 
a
d
d
i
t
i
o
n
a
l
 
f
o
r
m
a
t
s
.




 
 
 
 
 
 
 
 
i
n
 
m
a
n
i
f
e
s
t
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
I
n
d
i
c
a
t
e
 
i
f
 
t
h
e
 
o
p
t
i
o
n
a
l
 
m
a
n
i
f
e
s
t
 
f
i
l
e
 
(
.
m
f
)
 
s
h
o
u
l
d
 
b
e
 
w
r
i
t
t
e
n
.
 
T
h
e
 
m
a
n
i
f
e
s
t
 
f
i
l
e


 
 
 
 
 
 
 
 
 
 
 
 
i
s
 
u
s
e
d
 
f
o
r
 
i
n
t
e
g
r
i
t
y
 
c
h
e
c
k
s
 
p
r
i
o
r
 
i
m
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
p
a
t
h
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
a
p
p
l
i
a
n
c
e
 
f
i
l
e
 
t
o
 
o
p
e
n
 
(
e
i
t
h
e
r
 
w
i
t
h
 
a
n
 
.
o
v
f
 
o
r
 
.
o
v
a
 
e
x
t
e
n
s
i
o
n
,
 
d
e
p
e
n
d
i
n
g


 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
n
 
w
h
e
t
h
e
r
 
t
h
e
 
a
p
p
l
i
a
n
c
e
 
i
s
 
d
i
s
t
r
i
b
u
t
e
d
 
a
s
 
a
 
s
e
t
 
o
f
 
f
i
l
e
s
 
o
r
 
a
s
 
a
 
s
i
n
g
l
e
 
f
i
l
e
,
 
r
e
s
p
e
c
t
i
v
e
l
y
)
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
w
r
i
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
f
o
r
m
a
t
_
p
,
 
m
a
n
i
f
e
s
t
,
 
p
a
t
h
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
w
a
r
n
i
n
g
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
e
x
t
u
a
l
 
w
a
r
n
i
n
g
s
 
w
h
i
c
h
 
o
c
c
u
r
r
e
d
 
d
u
r
i
n
g
 
e
x
e
c
u
t
i
o
n
 
o
f
 
<
l
i
n
k
 
t
o
=
"
#
i
n
t
e
r
p
r
e
t
"
/
>
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
w
a
r
n
i
n
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
w
a
r
n
i
n
g
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
W
a
r
n
i
n
g
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
w
a
r
n
i
n
g
s


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
R
e
p
r
e
s
e
n
t
s
 
o
n
e
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
(
m
a
c
h
i
n
e
)
 
i
n
 
a
n
 
a
p
p
l
i
a
n
c
e
.
 
T
h
i
s
 
i
n
t
e
r
f
a
c
e
 
i
s
 
u
s
e
d
 
i
n


 
 
 
 
 
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
:
:
v
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
s
"
/
>
 
a
r
r
a
y
.
 
A
f
t
e
r


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
:
:
i
n
t
e
r
p
r
e
t
"
/
>
 
h
a
s
 
b
e
e
n
 
c
a
l
l
e
d
,
 
t
h
a
t
 
a
r
r
a
y
 
c
o
n
t
a
i
n
s
 
i
n
f
o
r
m
a
t
i
o
n


 
 
 
 
 
 
a
b
o
u
t
 
h
o
w
 
t
h
e
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
s
 
d
e
s
c
r
i
b
e
d
 
i
n
 
t
h
e
 
O
V
F
 
s
h
o
u
l
d
 
b
e
s
t
 
b
e
 
i
m
p
o
r
t
e
d
 
i
n
t
o


 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
"
/
>
 
f
o
r
 
t
h
e
 
s
t
e
p
s
 
r
e
q
u
i
r
e
d
 
t
o


 
 
 
 
 
 
i
m
p
o
r
t
 
a
n
 
O
V
F
 
i
n
t
o
 
V
i
r
t
u
a
l
B
o
x
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
d
7
5
2
5
e
6
c
-
5
3
1
a
-
4
c
5
1
-
8
e
0
4
-
4
1
2
3
5
0
8
3
a
3
d
8
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
c
o
u
n
t
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
d
e
s
c
r
i
p
t
i
o
n
 
e
n
t
r
i
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
d
e
f
 
g
e
t
_
d
e
s
c
r
i
p
t
i
o
n
(
s
e
l
f
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
t
h
e
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
 
a
s
 
a
r
r
a
y
s
 
o
f
 
i
n
s
t
r
u
c
t
i
o
n
 
i
t
e
m
s
.
 
I
n
 
e
a
c
h
 
a
r
r
a
y
,
 
t
h
e


 
 
 
 
 
 
i
t
e
m
s
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
i
n
d
i
c
e
s
 
c
o
r
r
e
s
p
o
n
d
 
a
n
d
 
j
o
i
n
t
l
y
 
r
e
p
r
e
s
e
n
t
 
a
n
 
i
m
p
o
r
t
 
i
n
s
t
r
u
c
t
i
o
n
 
f
o
r
 
V
i
r
t
u
a
l
B
o
x
.




 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
b
e
l
o
w
 
i
d
e
n
t
i
f
i
e
s
 
t
h
e
 
v
a
l
u
e
 
s
e
t
s
 
t
h
a
t
 
a
r
e
 
p
o
s
s
i
b
l
e
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e
"
/
>
 
e
n
u
m
 
v
a
l
u
e
 
i
n
 
t
h
e
 
a
r
r
a
y
 
i
t
e
m
 
i
n
 
@
a
 
a
T
y
p
e
s
[
]
.
 
I
n
 
e
a
c
h
 
c
a
s
e
,


 
 
 
 
 
 
t
h
e
 
a
r
r
a
y
 
i
t
e
m
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
i
n
d
e
x
 
i
n
 
@
a
 
O
V
F
V
a
l
u
e
s
[
]
 
w
i
l
l
 
c
o
n
t
a
i
n
 
t
h
e
 
o
r
i
g
i
n
a
l
 
v
a
l
u
e
 
a
s
 
c
o
n
t
a
i
n
e
d


 
 
 
 
 
 
i
n
 
t
h
e
 
O
V
F
 
f
i
l
e
 
(
j
u
s
t
 
f
o
r
 
i
n
f
o
r
m
a
t
i
o
n
a
l
 
p
u
r
p
o
s
e
s
)
,
 
a
n
d
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
i
t
e
m
 
i
n
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]


 
 
 
 
 
 
w
i
l
l
 
c
o
n
t
a
i
n
 
a
 
s
u
g
g
e
s
t
e
d
 
v
a
l
u
e
 
t
o
 
b
e
 
u
s
e
d
 
f
o
r
 
V
i
r
t
u
a
l
B
o
x
.
 
D
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
d
e
s
c
r
i
p
t
i
o
n
 
t
y
p
e
,


 
 
 
 
 
 
t
h
e
 
@
a
 
a
E
x
t
r
a
C
o
n
f
i
g
V
a
l
u
e
s
[
]
 
a
r
r
a
y
 
i
t
e
m
 
m
a
y
 
a
l
s
o
 
b
e
 
u
s
e
d
.




 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
O
S
"
:
 
t
h
e
 
g
u
e
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
 
t
y
p
e
.
 
T
h
e
r
e
 
m
u
s
t
 
b
e
 
e
x
a
c
t
l
y
 
o
n
e
 
s
u
c
h
 
a
r
r
a
y
 
i
t
e
m
 
o
n
 
i
m
p
o
r
t
.
 
T
h
e


 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
i
t
e
m
 
i
n
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]
 
c
o
n
t
a
i
n
s
 
t
h
e
 
s
u
g
g
e
s
t
e
d
 
g
u
e
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
 
f
o
r
 
V
i
r
t
u
a
l
B
o
x
.


 
 
 
 
 
 
 
 
T
h
i
s
 
w
i
l
l
 
b
e
 
o
n
e
 
o
f
 
t
h
e
 
v
a
l
u
e
s
 
l
i
s
t
e
d
 
i
n
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
g
u
e
s
t
O
S
T
y
p
e
s
"
/
>
.
 
T
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g


 
 
 
 
 
 
 
 
i
t
e
m
 
i
n
 
@
a
 
O
V
F
V
a
l
u
e
s
[
]
 
w
i
l
l
 
c
o
n
t
a
i
n
 
a
 
n
u
m
e
r
i
c
a
l
 
v
a
l
u
e
 
t
h
a
t
 
d
e
s
c
r
i
b
e
d
 
t
h
e
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
 
i
n
 
t
h
e
 
O
V
F
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
N
a
m
e
"
:
 
t
h
e
 
n
a
m
e
 
t
o
 
g
i
v
e
 
t
o
 
t
h
e
 
n
e
w
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
o
n
e
 
s
u
c
h
 
a
r
r
a
y
 
i
t
e
m
;


 
 
 
 
 
 
 
 
i
f
 
n
o
n
e
 
i
s
 
p
r
e
s
e
n
t
 
o
n
 
i
m
p
o
r
t
,
 
t
h
e
n
 
a
n
 
a
u
t
o
m
a
t
i
c
 
n
a
m
e
 
w
i
l
l
 
b
e
 
c
r
e
a
t
e
d
 
f
r
o
m
 
t
h
e
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m


 
 
 
 
 
 
 
 
t
y
p
e
.
 
T
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
i
t
e
m
 
i
m
 
@
a
 
O
V
F
V
a
l
u
e
s
[
]
 
w
i
l
l
 
c
o
n
t
a
i
n
 
t
h
e
 
s
u
g
g
e
s
t
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
a
m
e


 
 
 
 
 
 
 
 
f
r
o
m
 
t
h
e
 
O
V
F
 
f
i
l
e
,
 
a
n
d
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]
 
w
i
l
l
 
c
o
n
t
a
i
n
 
a
 
s
u
g
g
e
s
t
i
o
n
 
f
o
r
 
a
 
u
n
i
q
u
e
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>
 
n
a
m
e
 
t
h
a
t
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
 
y
e
t
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
"
D
e
s
c
r
i
p
t
i
o
n
"
:
 
a
n
 
a
r
b
i
t
r
a
r
y
 
d
e
s
c
r
i
p
t
i
o
n
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
"
L
i
c
e
n
s
e
"
:
 
t
h
e
 
E
U
L
A
 
s
e
c
t
i
o
n
 
f
r
o
m
 
t
h
e
 
O
V
F
,
 
i
f
 
p
r
e
s
e
n
t
.
 
I
t
 
i
s
 
t
h
e
 
r
e
s
p
o
n
s
i
b
i
l
i
t
y
 
o
f
 
t
h
e
 
c
a
l
l
i
n
g


 
 
 
 
 
 
 
 
 
 
c
o
d
e
 
t
o
 
d
i
s
p
l
a
y
 
s
u
c
h
 
a
 
l
i
c
e
n
s
e
 
f
o
r
 
a
g
r
e
e
m
e
n
t
;
 
t
h
e
 
M
a
i
n
 
A
P
I
 
d
o
e
s
 
n
o
t
 
e
n
f
o
r
c
e
 
a
n
y
 
s
u
c
h
 
p
o
l
i
c
y
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
M
i
s
c
e
l
l
a
n
e
o
u
s
:
 
r
e
s
e
r
v
e
d
 
f
o
r
 
f
u
t
u
r
e
 
u
s
e
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
C
P
U
"
:
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
C
P
U
s
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
o
n
e
 
s
u
c
h
 
i
t
e
m
,
 
w
h
i
c
h
 
w
i
l
l
 
p
r
e
s
e
n
t
l
y
 
b
e
 
i
g
n
o
r
e
d
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
M
e
m
o
r
y
"
:
 
t
h
e
 
a
m
o
u
n
t
 
o
f
 
g
u
e
s
t
 
R
A
M
,
 
i
n
 
b
y
t
e
s
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
o
n
e
 
s
u
c
h
 
a
r
r
a
y
 
i
t
e
m
;
 
i
f
 
n
o
n
e


 
 
 
 
 
 
 
 
i
s
 
p
r
e
s
e
n
t
 
o
n
 
i
m
p
o
r
t
,
 
t
h
e
n
 
V
i
r
t
u
a
l
B
o
x
 
w
i
l
l
 
s
e
t
 
a
 
m
e
a
n
i
n
g
f
u
l
 
d
e
f
a
u
l
t
 
b
a
s
e
d
 
o
n
 
t
h
e
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m


 
 
 
 
 
 
 
 
t
y
p
e
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
I
D
E
"
:
 
a
n
 
I
D
E
 
h
a
r
d
 
d
i
s
k
 
c
o
n
t
r
o
l
l
e
r
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
t
w
o
 
s
u
c
h
 
i
t
e
m
s
.


 
 
 
 
 
 
 
 
A
n
 
o
p
t
i
o
n
a
l
 
v
a
l
u
e
 
i
n
 
@
a
 
O
V
F
V
a
l
u
e
s
[
]
 
a
n
d
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]
 
c
a
n
 
b
e
 
"
P
I
I
X
3
"
 
o
r
 
"
P
I
I
X
4
"
 
t
o
 
s
p
e
c
i
f
y


 
 
 
 
 
 
 
 
t
h
e
 
t
y
p
e
 
o
f
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
;
 
t
h
i
s
 
c
o
r
r
e
s
p
o
n
d
s
 
t
o
 
t
h
e
 
R
e
s
o
u
r
c
e
S
u
b
T
y
p
e
 
e
l
e
m
e
n
t
 
w
h
i
c
h
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
w
r
i
t
e
s
 
i
n
t
o
 
t
h
e
 
O
V
F
.


 
 
 
 
 
 
 
 
T
h
e
 
m
a
t
c
h
i
n
g
 
i
t
e
m
 
i
n
 
t
h
e
 
@
a
 
a
R
e
f
s
[
]
 
a
r
r
a
y
 
w
i
l
l
 
c
o
n
t
a
i
n
 
a
n
 
i
n
t
e
g
e
r
 
t
h
a
t
 
i
t
e
m
s
 
o
f
 
t
h
e
 
"
H
a
r
d
d
i
s
k
"


 
 
 
 
 
 
 
 
t
y
p
e
 
c
a
n
 
u
s
e
 
t
o
 
s
p
e
c
i
f
y
 
w
h
i
c
h
 
h
a
r
d
 
d
i
s
k
 
c
o
n
t
r
o
l
l
e
r
 
a
 
v
i
r
t
u
a
l
 
d
i
s
k
 
s
h
o
u
l
d
 
b
e
 
c
o
n
n
e
c
t
e
d
 
t
o
.


 
 
 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
i
n
 
O
V
F
,
 
a
n
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
 
h
a
s
 
t
w
o
 
c
h
a
n
n
e
l
s
,
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
"
m
a
s
t
e
r
"
 
a
n
d
 
"
s
l
a
v
e
"


 
 
 
 
 
 
 
 
i
n
 
t
r
a
d
i
t
i
o
n
a
l
 
t
e
r
m
i
n
o
l
o
g
y
,
 
w
h
e
r
e
a
s
 
t
h
e
 
I
D
E
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
h
a
t
 
V
i
r
t
u
a
l
B
o
x
 
s
u
p
p
o
r
t
s
 
i
n


 
 
 
 
 
 
 
 
i
t
s
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
 
s
u
p
p
o
r
t
s
 
f
o
u
r
 
c
h
a
n
n
e
l
s
 
(
p
r
i
m
a
r
y
 
m
a
s
t
e
r
,
 
p
r
i
m
a
r
y
 
s
l
a
v
e
,
 
s
e
c
o
n
d
a
r
y
 
m
a
s
t
e
r
,


 
 
 
 
 
 
 
 
s
e
c
o
n
d
a
r
y
 
s
l
a
v
e
)
 
a
n
d
 
t
h
u
s
 
m
a
p
s
 
t
o
 
t
w
o
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
s
 
i
n
 
t
h
e
 
O
V
F
 
s
e
n
s
e
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
A
T
A
"
:
 
a
n
 
S
A
T
A
 
h
a
r
d
 
d
i
s
k
 
c
o
n
t
r
o
l
l
e
r
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
o
n
e
 
s
u
c
h
 
i
t
e
m
.
 
T
h
i
s


 
 
 
 
 
 
 
 
h
a
s
 
n
o
 
v
a
l
u
e
 
i
n
 
@
a
 
O
V
F
V
a
l
u
e
s
[
]
 
o
r
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]
.


 
 
 
 
 
 
 
 
T
h
e
 
m
a
t
c
h
i
n
g
 
i
t
e
m
 
i
n
 
t
h
e
 
@
a
 
a
R
e
f
s
[
]
 
a
r
r
a
y
 
w
i
l
l
 
b
e
 
u
s
e
d
 
a
s
 
w
i
t
h
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
s
 
(
s
e
e
 
a
b
o
v
e
)
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
C
S
I
"
:
 
a
 
S
C
S
I
 
h
a
r
d
 
d
i
s
k
 
c
o
n
t
r
o
l
l
e
r
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
o
n
e
 
s
u
c
h
 
i
t
e
m
.


 
 
 
 
 
 
 
 
T
h
e
 
i
t
e
m
s
 
i
n
 
@
a
 
O
V
F
V
a
l
u
e
s
[
]
 
a
n
d
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]
 
w
i
l
l
 
e
i
t
h
e
r
 
b
e
 
"
L
s
i
L
o
g
i
c
"
,
 
"
B
u
s
L
o
g
i
c
"
 
o
r


 
 
 
 
 
 
 
 
"
L
s
i
L
o
g
i
c
S
a
s
"
.
 
(
N
o
t
e
 
t
h
a
t
 
i
n
 
O
V
F
,
 
t
h
e
 
L
s
i
L
o
g
i
c
S
a
s
 
c
o
n
t
r
o
l
l
e
r
 
i
s
 
t
r
e
a
t
e
d
 
a
s
 
a
 
S
C
S
I
 
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 
w
h
e
r
e
a
s
 
V
i
r
t
u
a
l
B
o
x
 
c
o
n
s
i
d
e
r
s
 
i
t
 
a
 
c
l
a
s
s
 
o
f
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
s
 
o
f
 
i
t
s
 
o
w
n
;
 
s
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
T
y
p
e
"
/
>
)
.


 
 
 
 
 
 
 
 
T
h
e
 
m
a
t
c
h
i
n
g
 
i
t
e
m
 
i
n
 
t
h
e
 
@
a
 
a
R
e
f
s
[
]
 
a
r
r
a
y
 
w
i
l
l
 
b
e
 
u
s
e
d
 
a
s
 
w
i
t
h
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
s
 
(
s
e
e
 
a
b
o
v
e
)
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
H
a
r
d
D
i
s
k
I
m
a
g
e
"
:
 
a
 
v
i
r
t
u
a
l
 
h
a
r
d
 
d
i
s
k
,
 
m
o
s
t
 
p
r
o
b
a
b
l
y
 
a
s
 
a
 
r
e
f
e
r
e
n
c
e
 
t
o
 
a
n
 
i
m
a
g
e
 
f
i
l
e
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
n


 
 
 
 
 
 
 
 
a
r
b
i
t
r
a
r
y
 
n
u
m
b
e
r
 
o
f
 
t
h
e
s
e
 
i
t
e
m
s
,
 
o
n
e
 
f
o
r
 
e
a
c
h
 
v
i
r
t
u
a
l
 
d
i
s
k
 
i
m
a
g
e
 
t
h
a
t
 
a
c
c
o
m
p
a
n
i
e
s
 
t
h
e
 
O
V
F
.




 
 
 
 
 
 
 
 
T
h
e
 
a
r
r
a
y
 
i
t
e
m
 
i
n
 
@
a
 
O
V
F
V
a
l
u
e
s
[
]
 
w
i
l
l
 
c
o
n
t
a
i
n
 
t
h
e
 
f
i
l
e
 
s
p
e
c
i
f
i
c
a
t
i
o
n
 
f
r
o
m
 
t
h
e
 
O
V
F
 
f
i
l
e
 
(
w
i
t
h
o
u
t


 
 
 
 
 
 
 
 
a
 
p
a
t
h
 
s
i
n
c
e
 
t
h
e
 
i
m
a
g
e
 
f
i
l
e
 
s
h
o
u
l
d
 
b
e
 
i
n
 
t
h
e
 
s
a
m
e
 
l
o
c
a
t
i
o
n
 
a
s
 
t
h
e
 
O
V
F
 
f
i
l
e
 
i
t
s
e
l
f
)
,
 
w
h
e
r
e
a
s
 
t
h
e


 
 
 
 
 
 
 
 
i
t
e
m
 
i
n
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]
 
w
i
l
l
 
c
o
n
t
a
i
n
 
a
 
q
u
a
l
i
f
i
e
d
 
p
a
t
h
 
s
p
e
c
i
f
i
c
a
t
i
o
n
 
t
o
 
w
h
e
r
e
 
V
i
r
t
u
a
l
B
o
x
 
u
s
e
s
 
t
h
e


 
 
 
 
 
 
 
 
h
a
r
d
 
d
i
s
k
 
i
m
a
g
e
.
 
T
h
i
s
 
m
e
a
n
s
 
t
h
a
t
 
o
n
 
i
m
p
o
r
t
 
t
h
e
 
i
m
a
g
e
 
w
i
l
l
 
b
e
 
c
o
p
i
e
d
 
a
n
d
 
c
o
n
v
e
r
t
e
d
 
f
r
o
m
 
t
h
e


 
 
 
 
 
 
 
 
"
o
v
f
"
 
l
o
c
a
t
i
o
n
 
t
o
 
t
h
e
 
"
v
b
o
x
"
 
l
o
c
a
t
i
o
n
;
 
o
n
 
e
x
p
o
r
t
,
 
t
h
i
s
 
w
i
l
l
 
b
e
 
h
a
n
d
l
e
d
 
t
h
e
 
o
t
h
e
r
 
w
a
y
 
r
o
u
n
d
.




 
 
 
 
 
 
 
 
T
h
e
 
m
a
t
c
h
i
n
g
 
i
t
e
m
 
i
n
 
t
h
e
 
@
a
 
a
E
x
t
r
a
C
o
n
f
i
g
V
a
l
u
e
s
[
]
 
a
r
r
a
y
 
m
u
s
t
 
c
o
n
t
a
i
n
 
a
 
s
t
r
i
n
g
 
o
f
 
t
h
e
 
f
o
l
l
o
w
i
n
g


 
 
 
 
 
 
 
 
f
o
r
m
a
t
:
 
"
c
o
n
t
r
o
l
l
e
r
=
<
i
n
d
e
x
>
;
c
h
a
n
n
e
l
=
<
c
>
"


 
 
 
 
 
 
 
 
I
n
 
t
h
i
s
 
s
t
r
i
n
g
,
 
<
i
n
d
e
x
>
 
m
u
s
t
 
b
e
 
a
n
 
i
n
t
e
g
e
r
 
s
p
e
c
i
f
y
i
n
g
 
t
h
e
 
h
a
r
d
 
d
i
s
k
 
c
o
n
t
r
o
l
l
e
r
 
t
o
 
c
o
n
n
e
c
t


 
 
 
 
 
 
 
 
t
h
e
 
i
m
a
g
e
 
t
o
.
 
T
h
a
t
 
n
u
m
b
e
r
 
m
u
s
t
 
b
e
 
t
h
e
 
i
n
d
e
x
 
o
f
 
a
n
 
a
r
r
a
y
 
i
t
e
m
 
w
i
t
h
 
o
n
e
 
o
f
 
t
h
e
 
h
a
r
d
 
d
i
s
k
 
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 
t
y
p
e
s
 
(
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
C
S
I
,
 
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
A
T
A
,
 
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
I
D
E
)
.


 
 
 
 
 
 
 
 
I
n
 
a
d
d
i
t
i
o
n
,
 
<
c
>
 
m
u
s
t
 
s
p
e
c
i
f
y
 
t
h
e
 
c
h
a
n
n
e
l
 
t
o
 
u
s
e
 
o
n
 
t
h
a
t
 
c
o
n
t
r
o
l
l
e
r
.
 
F
o
r
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
s
,


 
 
 
 
 
 
 
 
t
h
i
s
 
c
a
n
 
b
e
 
0
 
o
r
 
1
 
f
o
r
 
m
a
s
t
e
r
 
o
r
 
s
l
a
v
e
,
 
r
e
s
p
e
c
t
i
v
e
l
y
.
 
F
o
r
 
c
o
m
p
a
t
i
b
i
l
i
t
y
 
w
i
t
h
 
V
i
r
t
u
a
l
B
o
x
 
v
e
r
s
i
o
n
s


 
 
 
 
 
 
 
 
b
e
f
o
r
e
 
3
.
2
,
 
t
h
e
 
v
a
l
u
e
s
 
2
 
a
n
d
 
3
 
(
f
o
r
 
s
e
c
o
n
d
a
r
y
 
m
a
s
t
e
r
 
a
n
d
 
s
e
c
o
n
d
a
r
y
 
s
l
a
v
e
)
 
a
r
e
 
a
l
s
o
 
s
u
p
p
o
r
t
e
d
,
 
b
u
t


 
 
 
 
 
 
 
 
n
o
 
l
o
n
g
e
r
 
e
x
p
o
r
t
e
d
.
 
F
o
r
 
S
A
T
A
 
a
n
d
 
S
C
S
I
 
c
o
n
t
r
o
l
l
e
r
s
,
 
t
h
e
 
c
h
a
n
n
e
l
 
c
a
n
 
r
a
n
g
e
 
f
r
o
m
 
0
-
2
9
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
C
D
R
O
M
"
:
 
a
 
v
i
r
t
u
a
l
 
C
D
-
R
O
M
 
d
r
i
v
e
.
 
T
h
e
 
m
a
t
c
h
i
n
g
 
i
t
e
m
 
i
n
 
@
a
 
a
E
x
t
r
a
C
o
n
f
i
g
V
a
l
u
e
[
]
 
c
o
n
t
a
i
n
s
 
t
h
e
 
s
a
m
e


 
 
 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
 
i
n
f
o
r
m
a
t
i
o
n
 
a
s
 
w
i
t
h
 
"
H
a
r
d
D
i
s
k
I
m
a
g
e
"
 
i
t
e
m
s
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
C
D
R
O
M
"
:
 
a
 
v
i
r
t
u
a
l
 
f
l
o
p
p
y
 
d
r
i
v
e
.
 
T
h
e
 
m
a
t
c
h
i
n
g
 
i
t
e
m
 
i
n
 
@
a
 
a
E
x
t
r
a
C
o
n
f
i
g
V
a
l
u
e
[
]
 
c
o
n
t
a
i
n
s
 
t
h
e
 
s
a
m
e


 
 
 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
 
i
n
f
o
r
m
a
t
i
o
n
 
a
s
 
w
i
t
h
 
"
H
a
r
d
D
i
s
k
I
m
a
g
e
"
 
i
t
e
m
s
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
N
e
t
w
o
r
k
A
d
a
p
t
e
r
"
:
 
a
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
.
 
T
h
e
 
a
r
r
a
y
 
i
t
e
m
 
i
n
 
@
a
 
a
V
B
o
x
V
a
l
u
e
s
[
]
 
w
i
l
l
 
s
p
e
c
i
f
y
 
t
h
e
 
h
a
r
d
w
a
r
e


 
 
 
 
 
 
 
 
f
o
r
 
t
h
e
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
,
 
w
h
e
r
e
a
s
 
t
h
e
 
a
r
r
a
y
 
i
t
e
m
 
i
n
 
@
a
 
a
E
x
t
r
a
C
o
n
f
i
g
V
a
l
u
e
s
[
]
 
w
i
l
l
 
h
a
v
e
 
a
 
s
t
r
i
n
g


 
 
 
 
 
 
 
 
o
f
 
t
h
e
 
"
t
y
p
e
=
<
X
>
"
 
f
o
r
m
a
t
,
 
w
h
e
r
e
 
<
X
>
 
m
u
s
t
 
b
e
 
e
i
t
h
e
r
 
"
N
A
T
"
 
o
r
 
"
B
r
i
d
g
e
d
"
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
"
U
S
B
C
o
n
t
r
o
l
l
e
r
"
:
 
a
 
U
S
B
 
c
o
n
t
r
o
l
l
e
r
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
o
n
e
 
s
u
c
h
 
i
t
e
m
.
 
I
f
 
a
n
d
 
o
n
l
y
 
i
f
 
s
u
c
h
 
a
n


 
 
 
 
 
 
 
 
 
 
i
t
e
m
 
i
s
p
r
e
s
e
n
t
,
 
U
S
B
 
s
u
p
p
o
r
t
 
w
i
l
l
 
b
e
 
e
n
a
b
l
e
d
 
f
o
r
 
t
h
e
 
n
e
w
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
"
S
o
u
n
d
C
a
r
d
"
:
 
a
 
s
o
u
n
d
 
c
a
r
d
.
 
T
h
e
r
e
 
c
a
n
 
b
e
 
a
t
 
m
o
s
t
 
o
n
e
 
s
u
c
h
 
i
t
e
m
.
 
I
f
 
a
n
d
 
o
n
l
y
 
i
f
 
s
u
c
h
 
a
n
 
i
t
e
m
 
i
s


 
 
 
 
 
 
 
 
 
 
p
r
e
s
e
n
t
,
 
s
o
u
n
d
 
s
u
p
p
o
r
t
 
w
i
l
l
 
b
e
 
e
n
a
b
l
e
d
 
f
o
r
 
t
h
e
 
n
e
w
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
i
n
 
V
i
r
t
u
a
l
B
o
x
 
w
i
l
l
 
a
l
w
a
y
s
 
b
e
 
p
r
e
s
e
n
t
e
d
 
w
i
t
h
 
t
h
e
 
s
t
a
n
d
a
r
d
 
V
i
r
t
u
a
l
B
o
x
 
s
o
u
n
d
c
a
r
d
,
 
w
h
i
c
h


 
 
 
 
 
 
 
 
 
 
m
a
y
 
b
e
 
d
i
f
f
e
r
e
n
t
 
f
r
o
m
 
t
h
e
 
v
i
r
t
u
a
l
 
s
o
u
n
d
c
a
r
d
 
e
x
p
e
c
t
e
d
 
b
y
 
t
h
e
 
a
p
p
l
i
a
n
c
e
.




 
 
 
 
 
 
 
 
o
u
t
 
t
y
p
e
s
 
o
f
 
t
y
p
e
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
r
e
f
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
o
v
f
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
v
_
b
o
x
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
D
e
s
c
r
i
p
t
i
o
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
d
e
s
c
r
i
p
t
i
o
n
_
b
y
_
t
y
p
e
(
s
e
l
f
,
 
t
y
p
e
_
p
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
T
h
i
s
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
D
e
s
c
r
i
p
t
i
o
n
"
/
>
 
e
x
c
e
p
t
 
t
h
a
t
 
y
o
u
 
c
a
n
 
s
p
e
c
i
f
y
 
w
h
i
c
h
 
t
y
p
e
s


 
 
 
 
 
 
s
h
o
u
l
d
 
b
e
 
r
e
t
u
r
n
e
d
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
t
y
p
e
s
 
o
f
 
t
y
p
e
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
r
e
f
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
o
v
f
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
v
_
b
o
x
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
o
u
t
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
D
e
s
c
r
i
p
t
i
o
n
B
y
T
y
p
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
t
y
p
e
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
v
a
l
u
e
s
_
b
y
_
t
y
p
e
(
s
e
l
f
,
 
t
y
p
e
_
p
,
 
w
h
i
c
h
)
:


 
 
 
 
 
 
 
 
"
"
"
T
h
i
s
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
D
e
s
c
r
i
p
t
i
o
n
B
y
T
y
p
e
"
/
>
 
e
x
c
e
p
t
 
t
h
a
t
 
y
o
u
 
c
a
n
 
s
p
e
c
i
f
y
 
w
h
i
c
h


 
 
 
 
 
 
v
a
l
u
e
 
t
y
p
e
s
 
s
h
o
u
l
d
 
b
e
 
r
e
t
u
r
n
e
d
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
V
a
l
u
e
T
y
p
e
"
/
>
 
f
o
r
 
p
o
s
s
i
b
l
e


 
 
 
 
 
 
v
a
l
u
e
s
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
i
n
 
w
h
i
c
h
 
o
f
 
t
y
p
e
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
V
a
l
u
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
v
a
l
u
e
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
V
a
l
u
e
s
B
y
T
y
p
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
t
y
p
e
_
p
,
 
w
h
i
c
h
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
f
i
n
a
l
_
v
a
l
u
e
s
(
s
e
l
f
,
 
e
n
a
b
l
e
d
,
 
v
_
b
o
x
_
v
a
l
u
e
s
,
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
s
)
:


 
 
 
 
 
 
 
 
"
"
"
T
h
i
s
 
m
e
t
h
o
d
 
a
l
l
o
w
s
 
t
h
e
 
a
p
p
l
i
a
n
c
e
'
s
 
u
s
e
r
 
t
o
 
c
h
a
n
g
e
 
t
h
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
f
o
r
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
 
 
s
y
s
t
e
m
 
d
e
s
c
r
i
p
t
i
o
n
s
.
 
F
o
r
 
e
a
c
h
 
a
r
r
a
y
 
i
t
e
m
 
r
e
t
u
r
n
e
d
 
f
r
o
m
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
D
e
s
c
r
i
p
t
i
o
n
"
/
>
,


 
 
 
 
 
 
 
 
y
o
u
 
m
u
s
t
 
p
a
s
s
 
i
n
 
o
n
e
 
b
o
o
l
e
a
n
 
v
a
l
u
e
 
a
n
d
 
o
n
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
E
a
c
h
 
i
t
e
m
 
i
n
 
t
h
e
 
b
o
o
l
e
a
n
 
a
r
r
a
y
 
d
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
t
h
e
 
p
a
r
t
i
c
u
l
a
r
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
i
t
e
m


 
 
 
 
 
 
 
 
s
h
o
u
l
d
 
b
e
 
e
n
a
b
l
e
d
.


 
 
 
 
 
 
 
 
Y
o
u
 
c
a
n
 
o
n
l
y
 
d
i
s
a
b
l
e
 
i
t
e
m
s
 
o
f
 
t
h
e
 
t
y
p
e
s
 
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
I
D
E
,
 
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
A
T
A
,


 
 
 
 
 
 
 
 
H
a
r
d
D
i
s
k
C
o
n
t
r
o
l
l
e
r
S
C
S
I
,
 
H
a
r
d
D
i
s
k
I
m
a
g
e
,
 
C
D
R
O
M
,
 
F
l
o
p
p
y
,
 
N
e
t
w
o
r
k
A
d
a
p
t
e
r
,
 
U
S
B
C
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 
a
n
d
 
S
o
u
n
d
C
a
r
d
.




 
 
 
 
 
 
 
 
F
o
r
 
t
h
e
 
"
v
b
o
x
"
 
a
n
d
 
"
e
x
t
r
a
 
c
o
n
f
i
g
u
r
a
t
i
o
n
"
 
v
a
l
u
e
s
,
 
i
f
 
y
o
u
 
p
a
s
s
 
i
n
 
t
h
e
 
s
a
m
e
 
a
r
r
a
y
s


 
 
 
 
 
 
 
 
a
s
 
r
e
t
u
r
n
e
d
 
i
n
 
t
h
e
 
a
V
B
o
x
V
a
l
u
e
s
 
a
n
d
 
a
E
x
t
r
a
C
o
n
f
i
g
V
a
l
u
e
s
 
a
r
r
a
y
s
 
f
r
o
m
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
D
e
s
c
r
i
p
t
i
o
n
"
/
>
,


 
 
 
 
 
 
 
 
t
h
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
r
e
m
a
i
n
s
 
u
n
c
h
a
n
g
e
d
.
 
P
l
e
a
s
e
 
s
e
e
 
t
h
e
 
d
o
c
u
m
e
n
t
a
t
i
o
n
 
f
o
r
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
D
e
s
c
r
i
p
t
i
o
n
"
/
>


 
 
 
 
 
 
 
 
f
o
r
 
v
a
l
i
d
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
v
a
l
u
e
s
 
f
o
r
 
t
h
e
 
i
n
d
i
v
i
d
u
a
l
 
a
r
r
a
y
 
i
t
e
m
 
t
y
p
e
s
.
 
I
f
 
t
h
e


 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
i
t
e
m
 
i
n
 
t
h
e
 
a
E
n
a
b
l
e
d
 
a
r
r
a
y
 
i
s
 
@
c
 
f
a
l
s
e
,
 
t
h
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
v
a
l
u
e
 
i
s
 
i
g
n
o
r
e
d
.




 
 
 
 
 
 
 
 
i
n
 
e
n
a
b
l
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
i
n
 
v
_
b
o
x
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
i
n
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
F
i
n
a
l
V
a
l
u
e
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
e
n
a
b
l
e
d
,
 
v
_
b
o
x
_
v
a
l
u
e
s
,
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
s
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
d
d
_
d
e
s
c
r
i
p
t
i
o
n
(
s
e
l
f
,
 
t
y
p
e
_
p
,
 
v
_
b
o
x
_
v
a
l
u
e
,
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
"
"
"
T
h
i
s
 
m
e
t
h
o
d
 
a
d
d
s
 
a
n
 
a
d
d
i
t
i
o
n
a
l
 
d
e
s
c
r
i
p
t
i
o
n
 
e
n
t
r
y
 
t
o
 
t
h
e
 
s
t
a
c
k
 
o
f
 
a
l
r
e
a
d
y


 
 
 
 
 
 
a
v
a
i
l
a
b
l
e
 
d
e
s
c
r
i
p
t
i
o
n
s
 
f
o
r
 
t
h
i
s
 
v
i
r
t
u
a
l
 
s
y
s
t
e
m
.
 
T
h
i
s
 
i
s
 
h
a
n
d
y
 
f
o
r
 
w
r
i
t
i
n
g


 
 
 
 
 
 
v
a
l
u
e
s
 
w
h
i
c
h
 
a
r
e
n
'
t
 
d
i
r
e
c
t
l
y
 
s
u
p
p
o
r
t
e
d
 
b
y
 
V
i
r
t
u
a
l
B
o
x
.
 
O
n
e
 
e
x
a
m
p
l
e
 
w
o
u
l
d


 
 
 
 
 
 
b
e
 
t
h
e
 
L
i
c
e
n
s
e
 
t
y
p
e
 
o
f
 
<
l
i
n
k
 
t
o
=
"
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
i
n
 
v
_
b
o
x
_
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
i
n
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
s
c
/
>




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
d
d
D
e
s
c
r
i
p
t
i
o
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
t
y
p
e
_
p
,
 
v
_
b
o
x
_
v
a
l
u
e
,
 
e
x
t
r
a
_
c
o
n
f
i
g
_
v
a
l
u
e
]
)


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
I
n
t
e
r
n
a
l
M
a
c
h
i
n
e
C
o
n
t
r
o
l
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
U
p
d
a
t
e
s
 
t
h
e
 
f
l
a
g
 
w
h
e
t
h
e
r
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
i
s
 
r
e
m
o
v
e
d
 
o
n
 
a


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
c
h
a
n
g
e
 
f
r
o
m
 
S
a
v
e
d
 
t
o
 
P
o
w
e
r
e
d
O
f
f
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
d
c
a
3
6
a
9
2
-
7
0
3
c
-
4
6
4
9
-
9
8
a
4
-
f
4
0
c
1
e
f
0
c
3
3
6
'


 
 
 
 
w
s
m
a
p
 
=
 
'
s
u
p
p
r
e
s
s
'


 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
r
e
m
o
v
e
_
s
a
v
e
d
_
s
t
a
t
e
_
f
i
l
e
(
s
e
l
f
,
 
r
e
m
o
v
e
)
:


 
 
 
 
 
 
 
 
"
"
"
U
p
d
a
t
e
s
 
t
h
e
 
f
l
a
g
 
w
h
e
t
h
e
r
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
i
s
 
r
e
m
o
v
e
d
 
o
n
 
a


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
c
h
a
n
g
e
 
f
r
o
m
 
S
a
v
e
d
 
t
o
 
P
o
w
e
r
e
d
O
f
f
.




 
 
 
 
 
 
 
 
i
n
 
r
e
m
o
v
e
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
R
e
m
o
v
e
S
a
v
e
d
S
t
a
t
e
F
i
l
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
r
e
m
o
v
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
u
p
d
a
t
e
_
s
t
a
t
e
(
s
e
l
f
,
 
s
t
a
t
e
)
:


 
 
 
 
 
 
 
 
"
"
"
U
p
d
a
t
e
s
 
t
h
e
 
V
M
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
o
p
e
r
a
t
i
o
n
 
w
i
l
l
 
a
l
s
o
 
u
p
d
a
t
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
w
i
t
h
 
t
h
e
 
c
o
r
r
e
c
t


 
 
 
 
 
 
 
 
 
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
a
n
d
 
d
e
l
e
t
e
 
t
h
i
s
 
f
i
l
e
 
f
r
o
m
 
d
i
s
k


 
 
 
 
 
 
 
 
 
 
w
h
e
n
 
a
p
p
r
o
p
r
i
a
t
e
.




 
 
 
 
 
 
 
 
i
n
 
s
t
a
t
e
 
o
f
 
t
y
p
e
 
M
a
c
h
i
n
e
S
t
a
t
e




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
u
p
d
a
t
e
S
t
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
t
a
t
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
i
p
c
_
i
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
i
d
_
p
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
I
P
C
I
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
d
_
p


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
b
e
g
i
n
_
p
o
w
e
r
_
u
p
(
s
e
l
f
,
 
p
r
o
g
r
e
s
s
)
:


 
 
 
 
 
 
 
 
"
"
"
T
e
l
l
s
 
V
B
o
x
S
V
C
 
t
h
a
t
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
p
o
w
e
r
U
p
"
/
>
 
i
s
 
u
n
d
e
r
 
w
a
y
s
 
a
n
d


 
 
 
 
 
 
 
 
g
i
v
e
s
 
i
t
 
t
h
e
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
h
a
t
 
s
h
o
u
l
d
 
b
e
 
p
a
r
t
 
o
f
 
a
n
y
 
p
e
n
d
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
o
p
e
r
a
t
i
o
n
s
.
 
T
h
e
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
o
b
j
e
c
t
 
m
a
y
 
b
e
 
c
a
l
l
e
d
 
b
a
c
k
 
t
o
 
r
e
f
l
e
c
t
 
a
n
 
e
a
r
l
y
 
c
a
n
c
e
l
a
t
i
o
n
,
 
s
o
 
s
o
m
e
 
c
a
r
e


 
 
 
 
 
 
 
 
h
a
v
e
 
t
o
 
b
e
 
t
a
k
e
n
 
w
i
t
h
 
r
e
s
p
e
c
t
 
t
o
 
a
n
y
 
c
a
n
c
e
l
a
t
i
o
n
 
c
a
l
l
b
a
c
k
s
.
 
T
h
e
 
c
o
n
s
o
l
e


 
 
 
 
 
 
 
 
o
b
j
e
c
t
 
w
i
l
l
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
I
n
t
e
r
n
a
l
M
a
c
h
i
n
e
C
o
n
t
r
o
l
:
:
e
n
d
P
o
w
e
r
U
p
"
/
>


 
 
 
 
 
 
 
 
t
o
 
s
i
g
n
a
l
 
t
h
e
 
c
o
m
p
l
e
t
i
o
n
 
o
f
 
t
h
e
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
b
e
g
i
n
P
o
w
e
r
U
p
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
g
r
e
s
s
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
d
_
p
o
w
e
r
_
u
p
(
s
e
l
f
,
 
r
e
s
u
l
t
)
:


 
 
 
 
 
 
 
 
"
"
"
T
e
l
l
s
 
V
B
o
x
S
V
C
 
t
h
a
t
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
p
o
w
e
r
U
p
"
/
>
 
h
a
s
 
c
o
m
p
l
e
t
e
d
.


 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
m
a
y
 
q
u
e
r
y
 
s
t
a
t
u
s
 
i
n
f
o
r
m
a
t
i
o
n
 
f
r
o
m
 
t
h
e
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
i
t


 
 
 
 
 
 
 
 
r
e
c
e
i
v
e
d
 
i
n
 
<
l
i
n
k
 
t
o
=
"
I
I
n
t
e
r
n
a
l
M
a
c
h
i
n
e
C
o
n
t
r
o
l
:
:
b
e
g
i
n
P
o
w
e
r
U
p
"
/
>
 
a
n
d
 
c
o
p
y


 
 
 
 
 
 
 
 
i
t
 
o
v
e
r
 
t
o
 
a
n
y
 
i
n
-
p
r
o
g
r
e
s
s
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>


 
 
 
 
 
 
 
 
c
a
l
l
 
i
n
 
o
r
d
e
r
 
t
o
 
c
o
m
p
l
e
t
e
 
t
h
a
t
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
i
n
 
r
e
s
u
l
t
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
d
P
o
w
e
r
U
p
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
r
e
s
u
l
t
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
b
e
g
i
n
_
p
o
w
e
r
i
n
g
_
d
o
w
n
(
s
e
l
f
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
C
a
l
l
e
d
 
b
y
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
t
o
 
i
n
f
o
r
m
 
t
h
e
 
s
e
r
v
e
r
 
i
t
 
w
a
n
t
s
 
t
o


 
 
 
 
 
 
 
 
s
t
o
p
 
t
h
e
 
V
M
 
e
x
e
c
u
t
i
o
n
 
a
n
d
 
p
o
w
e
r
 
d
o
w
n
.




 
 
 
 
 
 
 
 
o
u
t
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
c
r
e
a
t
e
d
 
b
y
 
V
B
o
x
S
V
C
 
t
o
 
w
a
i
t
 
u
n
t
i
l


 
 
 
 
 
 
 
 
 
 
t
h
e
 
V
M
 
i
s
 
p
o
w
e
r
e
d
 
d
o
w
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
b
e
g
i
n
P
o
w
e
r
i
n
g
D
o
w
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
d
_
p
o
w
e
r
i
n
g
_
d
o
w
n
(
s
e
l
f
,
 
r
e
s
u
l
t
,
 
e
r
r
_
m
s
g
)
:


 
 
 
 
 
 
 
 
"
"
"
C
a
l
l
e
d
 
b
y
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
t
o
 
i
n
f
o
r
m
 
t
h
e
 
s
e
r
v
e
r
 
t
h
a
t
 
p
o
w
e
r
i
n
g


 
 
 
 
 
 
 
 
d
o
w
n
 
p
r
e
v
i
o
u
s
l
y
 
r
e
q
u
e
s
t
e
d
 
b
y
 
#
b
e
g
i
n
P
o
w
e
r
i
n
g
D
o
w
n
 
i
s
 
e
i
t
h
e
r


 
 
 
 
 
 
 
 
s
u
c
c
e
s
s
f
u
l
l
y
 
f
i
n
i
s
h
e
d
 
o
r
 
t
h
e
r
e
 
w
a
s
 
a
 
f
a
i
l
u
r
e
.




 
 
 
 
 
 
 
 
i
n
 
r
e
s
u
l
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
@
c
 
S
_
O
K
 
t
o
 
i
n
d
i
c
a
t
e
 
s
u
c
c
e
s
s
.




 
 
 
 
 
 
 
 
i
n
 
e
r
r
_
m
s
g
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
@
c
 
h
u
m
a
n
 
r
e
a
d
a
b
l
e
 
e
r
r
o
r
 
m
e
s
s
a
g
e
 
i
n
 
c
a
s
e
 
o
f
 
f
a
i
l
u
r
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
d
P
o
w
e
r
i
n
g
D
o
w
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
r
e
s
u
l
t
,
 
e
r
r
_
m
s
g
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
u
n
_
u
s
b
_
d
e
v
i
c
e
_
f
i
l
t
e
r
s
(
s
e
l
f
,
 
d
e
v
i
c
e
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
A
s
k
s
 
t
h
e
 
s
e
r
v
e
r
 
t
o
 
r
u
n
 
U
S
B
 
d
e
v
i
c
e
s
 
f
i
l
t
e
r
s
 
o
f
 
t
h
e
 
a
s
s
o
c
i
a
t
e
d


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
a
g
a
i
n
s
t
 
t
h
e
 
g
i
v
e
n
 
U
S
B
 
d
e
v
i
c
e
 
a
n
d
 
t
e
l
l
 
i
f
 
t
h
e
r
e
 
i
s


 
 
 
 
 
 
 
 
a
 
m
a
t
c
h
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
t
e
n
d
e
d
 
t
o
 
b
e
 
u
s
e
d
 
o
n
l
y
 
f
o
r
 
r
e
m
o
t
e
 
U
S
B
 
d
e
v
i
c
e
s
.
 
L
o
c
a
l


 
 
 
 
 
 
 
 
 
 
o
n
e
s
 
d
o
n
'
t
 
r
e
q
u
i
r
e
 
t
o
 
c
a
l
l
 
t
h
i
s
 
m
e
t
h
o
d
 
(
t
h
i
s
 
i
s
 
d
o
n
e


 
 
 
 
 
 
 
 
 
 
i
m
p
l
i
c
i
t
l
y
 
b
y
 
t
h
e
 
H
o
s
t
 
a
n
d
 
U
S
B
P
r
o
x
y
S
e
r
v
i
c
e
)
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
I
U
S
B
D
e
v
i
c
e




 
 
 
 
 
 
 
 
o
u
t
 
m
a
t
c
h
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
o
u
t
 
m
a
s
k
e
d
_
i
n
t
e
r
f
a
c
e
s
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
u
n
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
d
e
v
i
c
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
a
p
t
u
r
e
_
u
s
b
_
d
e
v
i
c
e
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
q
u
e
s
t
s
 
a
 
c
a
p
t
u
r
e
 
o
f
 
t
h
e
 
g
i
v
e
n
 
h
o
s
t
 
U
S
B
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
r
e
q
u
e
s
t
 
i
s
 
c
o
m
p
l
e
t
e
d
,
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
w
i
l
l


 
 
 
 
 
 
 
 
g
e
t
 
a
 
<
l
i
n
k
 
t
o
=
"
I
I
n
t
e
r
n
a
l
S
e
s
s
i
o
n
C
o
n
t
r
o
l
:
:
o
n
U
S
B
D
e
v
i
c
e
A
t
t
a
c
h
"
/
>


 
 
 
 
 
 
 
 
n
o
t
i
f
i
c
a
t
i
o
n
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
a
p
t
u
r
e
U
S
B
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
t
a
c
h
_
u
s
b
_
d
e
v
i
c
e
(
s
e
l
f
,
 
i
d
_
p
,
 
d
o
n
e
)
:


 
 
 
 
 
 
 
 
"
"
"
N
o
t
i
f
i
c
a
t
i
o
n
 
t
h
a
t
 
a
 
V
M
 
i
s
 
g
o
i
n
g
 
t
o
 
d
e
t
a
c
h
 
(
@
a
 
d
o
n
e
 
=
 
@
c
 
f
a
l
s
e
)
 
o
r
 
h
a
s


 
 
 
 
 
 
 
 
a
l
r
e
a
d
y
 
d
e
t
a
c
h
e
d
 
(
@
a
 
d
o
n
e
 
=
 
@
c
 
t
r
u
e
)
 
t
h
e
 
g
i
v
e
n
 
U
S
B
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
@
a
 
d
o
n
e
 
=
 
@
c
 
t
r
u
e
 
r
e
q
u
e
s
t
 
i
s
 
c
o
m
p
l
e
t
e
d
,
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
w
i
l
l


 
 
 
 
 
 
 
 
g
e
t
 
a
 
<
l
i
n
k
 
t
o
=
"
I
I
n
t
e
r
n
a
l
S
e
s
s
i
o
n
C
o
n
t
r
o
l
:
:
o
n
U
S
B
D
e
v
i
c
e
D
e
t
a
c
h
"
/
>


 
 
 
 
 
 
 
 
n
o
t
i
f
i
c
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
t
h
e
 
@
a
 
d
o
n
e
 
=
 
@
c
 
t
r
u
e
 
c
a
s
e
,
 
t
h
e
 
s
e
r
v
e
r
 
m
u
s
t
 
r
u
n
 
i
t
s
 
o
w
n
 
f
i
l
t
e
r
s


 
 
 
 
 
 
 
 
 
 
a
n
d
 
f
i
l
t
e
r
s
 
o
f
 
a
l
l
 
V
M
s
 
b
u
t
 
t
h
i
s
 
o
n
e
 
o
n
 
t
h
e
 
d
e
t
a
c
h
e
d
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 
 
 
a
s
 
i
f
 
i
t
 
w
e
r
e
 
j
u
s
t
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
i
n
 
d
o
n
e
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
t
a
c
h
U
S
B
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
,
 
d
o
n
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
u
t
o
_
c
a
p
t
u
r
e
_
u
s
b
_
d
e
v
i
c
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
q
u
e
s
t
s
 
a
 
c
a
p
t
u
r
e
 
a
l
l
 
m
a
t
c
h
i
n
g
 
U
S
B
 
d
e
v
i
c
e
s
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
r
e
q
u
e
s
t
 
i
s
 
c
o
m
p
l
e
t
e
d
,
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
w
i
l
l


 
 
 
 
 
 
 
 
g
e
t
 
a
 
<
l
i
n
k
 
t
o
=
"
I
I
n
t
e
r
n
a
l
S
e
s
s
i
o
n
C
o
n
t
r
o
l
:
:
o
n
U
S
B
D
e
v
i
c
e
A
t
t
a
c
h
"
/
>


 
 
 
 
 
 
 
 
n
o
t
i
f
i
c
a
t
i
o
n
 
p
e
r
 
e
v
e
r
y
 
c
a
p
t
u
r
e
d
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
u
t
o
C
a
p
t
u
r
e
U
S
B
D
e
v
i
c
e
s
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
t
a
c
h
_
a
l
l
_
u
s
b
_
d
e
v
i
c
e
s
(
s
e
l
f
,
 
d
o
n
e
)
:


 
 
 
 
 
 
 
 
"
"
"
N
o
t
i
f
i
c
a
t
i
o
n
 
t
h
a
t
 
a
 
V
M
 
t
h
a
t
 
i
s
 
b
e
i
n
g
 
p
o
w
e
r
e
d
 
d
o
w
n
.
 
T
h
e
 
d
o
n
e


 
 
 
 
 
 
 
 
p
a
r
a
m
e
t
e
r
 
i
n
d
i
c
a
t
e
s
 
w
h
e
t
h
e
r
 
w
h
i
c
h
 
s
t
a
g
e
 
o
f
 
t
h
e
 
p
o
w
e
r
 
d
o
w
n


 
 
 
 
 
 
 
 
w
e
'
r
e
 
a
t
.
 
W
h
e
n
 
@
a
 
d
o
n
e
 
=
 
@
c
 
f
a
l
s
e
 
t
h
e
 
V
M
 
i
s
 
a
n
n
o
u
n
c
i
n
g
 
i
t
s


 
 
 
 
 
 
 
 
i
n
t
e
n
t
i
o
n
s
,
 
w
h
i
l
e
 
w
h
e
n
 
@
a
 
d
o
n
e
 
=
 
@
c
 
t
r
u
e
 
t
h
e
 
V
M
 
i
s
 
r
e
p
o
r
t
i
n
g


 
 
 
 
 
 
 
 
w
h
a
t
 
i
t
 
h
a
s
 
d
o
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
t
h
e
 
@
a
 
d
o
n
e
 
=
 
@
c
 
t
r
u
e
 
c
a
s
e
,
 
t
h
e
 
s
e
r
v
e
r
 
m
u
s
t
 
r
u
n
 
i
t
s
 
o
w
n
 
f
i
l
t
e
r
s


 
 
 
 
 
 
 
 
 
 
a
n
d
 
f
i
l
t
e
r
s
 
o
f
 
a
l
l
 
V
M
s
 
b
u
t
 
t
h
i
s
 
o
n
e
 
o
n
 
a
l
l
 
d
e
t
a
c
h
 
d
e
v
i
c
e
s
 
a
s


 
 
 
 
 
 
 
 
 
 
i
f
 
t
h
e
y
 
w
e
r
e
 
j
u
s
t
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
.




 
 
 
 
 
 
 
 
i
n
 
d
o
n
e
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
t
a
c
h
A
l
l
U
S
B
D
e
v
i
c
e
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
d
o
n
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
o
n
_
s
e
s
s
i
o
n
_
e
n
d
(
s
e
l
f
,
 
s
e
s
s
i
o
n
)
:


 
 
 
 
 
 
 
 
"
"
"
T
r
i
g
g
e
r
e
d
 
b
y
 
t
h
e
 
g
i
v
e
n
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
 
w
h
e
n
 
t
h
e
 
s
e
s
s
i
o
n
 
i
s
 
a
b
o
u
t


 
 
 
 
 
 
 
 
t
o
 
c
l
o
s
e
 
n
o
r
m
a
l
l
y
.




 
 
 
 
 
 
 
 
i
n
 
s
e
s
s
i
o
n
 
o
f
 
t
y
p
e
 
I
S
e
s
s
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
S
e
s
s
i
o
n
 
t
h
a
t
 
i
s
 
b
e
i
n
g
 
c
l
o
s
e
d




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
U
s
e
d
 
t
o
 
w
a
i
t
 
u
n
t
i
l
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
m
a
c
h
i
n
e
 
i
s
 
a
c
t
u
a
l
l
y


 
 
 
 
 
 
 
 
 
 
d
i
s
s
o
c
i
a
t
e
d
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
s
e
s
s
i
o
n
 
o
n
 
t
h
e
 
s
e
r
v
e
r
.


 
 
 
 
 
 
 
 
 
 
R
e
t
u
r
n
e
d
 
o
n
l
y
 
w
h
e
n
 
t
h
i
s
 
s
e
s
s
i
o
n
 
i
s
 
a
 
d
i
r
e
c
t
 
o
n
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
o
n
S
e
s
s
i
o
n
E
n
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
e
s
s
i
o
n
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
b
e
g
i
n
_
s
a
v
i
n
g
_
s
t
a
t
e
(
s
e
l
f
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
C
a
l
l
e
d
 
b
y
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
t
o
 
i
n
f
o
r
m
 
t
h
e
 
s
e
r
v
e
r
 
i
t
 
w
a
n
t
s
 
t
o


 
 
 
 
 
 
 
 
s
a
v
e
 
t
h
e
 
c
u
r
r
e
n
t
 
s
t
a
t
e
 
a
n
d
 
s
t
o
p
 
t
h
e
 
V
M
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
 
 
o
u
t
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
c
r
e
a
t
e
d
 
b
y
 
V
B
o
x
S
V
C
 
t
o
 
w
a
i
t
 
u
n
t
i
l


 
 
 
 
 
 
 
 
 
 
t
h
e
 
s
t
a
t
e
 
i
s
 
s
a
v
e
d
.




 
 
 
 
 
 
 
 
o
u
t
 
s
t
a
t
e
_
f
i
l
e
_
p
a
t
h
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
i
l
e
 
p
a
t
h
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
m
u
s
t
 
s
a
v
e
 
t
h
e
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
t
o
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
b
e
g
i
n
S
a
v
i
n
g
S
t
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
d
_
s
a
v
i
n
g
_
s
t
a
t
e
(
s
e
l
f
,
 
r
e
s
u
l
t
,
 
e
r
r
_
m
s
g
)
:


 
 
 
 
 
 
 
 
"
"
"
C
a
l
l
e
d
 
b
y
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
t
o
 
i
n
f
o
r
m
 
t
h
e
 
s
e
r
v
e
r
 
t
h
a
t
 
s
a
v
i
n
g


 
 
 
 
 
 
 
 
t
h
e
 
s
t
a
t
e
 
p
r
e
v
i
o
u
s
l
y
 
r
e
q
u
e
s
t
e
d
 
b
y
 
#
b
e
g
i
n
S
a
v
i
n
g
S
t
a
t
e
 
i
s
 
e
i
t
h
e
r


 
 
 
 
 
 
 
 
s
u
c
c
e
s
s
f
u
l
l
y
 
f
i
n
i
s
h
e
d
 
o
r
 
t
h
e
r
e
 
w
a
s
 
a
 
f
a
i
l
u
r
e
.




 
 
 
 
 
 
 
 
i
n
 
r
e
s
u
l
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
@
c
 
S
_
O
K
 
t
o
 
i
n
d
i
c
a
t
e
 
s
u
c
c
e
s
s
.




 
 
 
 
 
 
 
 
i
n
 
e
r
r
_
m
s
g
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
@
c
 
h
u
m
a
n
 
r
e
a
d
a
b
l
e
 
e
r
r
o
r
 
m
e
s
s
a
g
e
 
i
n
 
c
a
s
e
 
o
f
 
f
a
i
l
u
r
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
d
S
a
v
i
n
g
S
t
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
r
e
s
u
l
t
,
 
e
r
r
_
m
s
g
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
d
o
p
t
_
s
a
v
e
d
_
s
t
a
t
e
(
s
e
l
f
,
 
s
a
v
e
d
_
s
t
a
t
e
_
f
i
l
e
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
s
 
c
a
l
l
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
a
d
o
p
t
S
a
v
e
d
S
t
a
t
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
s
a
v
e
d
_
s
t
a
t
e
_
f
i
l
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
P
a
t
h
 
t
o
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
t
o
 
a
d
o
p
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
p
a
t
h
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
d
o
p
t
S
a
v
e
d
S
t
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
a
v
e
d
_
s
t
a
t
e
_
f
i
l
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
b
e
g
i
n
_
t
a
k
i
n
g
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
i
n
i
t
i
a
t
o
r
,
 
n
a
m
e
,
 
d
e
s
c
r
i
p
t
i
o
n
,
 
c
o
n
s
o
l
e
_
p
r
o
g
r
e
s
s
,
 
f
_
t
a
k
i
n
g
_
s
n
a
p
s
h
o
t
_
o
n
l
i
n
e
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
C
a
l
l
e
d
 
f
r
o
m
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
t
o
 
r
e
q
u
e
s
t
 
f
r
o
m
 
t
h
e
 
s
e
r
v
e
r
 
t
o
 
p
e
r
f
o
r
m
 
t
h
e


 
 
 
 
 
 
 
 
s
e
r
v
e
r
-
s
i
d
e
 
a
c
t
i
o
n
s
 
o
f
 
c
r
e
a
t
i
n
g
 
a
 
s
n
a
p
s
h
o
t
 
(
c
r
e
a
t
i
n
g
 
d
i
f
f
e
r
e
n
c
i
n
g
 
i
m
a
g
e
s


 
 
 
 
 
 
 
 
a
n
d
 
t
h
e
 
s
n
a
p
s
h
o
t
 
o
b
j
e
c
t
)
.




 
 
 
 
 
 
 
 
i
n
 
i
n
i
t
i
a
t
o
r
 
o
f
 
t
y
p
e
 
I
C
o
n
s
o
l
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
o
n
s
o
l
e
 
o
b
j
e
c
t
 
t
h
a
t
 
i
n
i
t
i
a
t
e
d
 
t
h
i
s
 
c
a
l
l
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
S
n
a
p
s
h
o
t
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
S
n
a
p
s
h
o
t
 
d
e
s
c
r
i
p
t
i
o
n
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
s
o
l
e
_
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
c
r
e
a
t
e
d
 
b
y
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
t
r
a
c
k
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
'
s
 
p
r
o
g
r
e
s
s
.
 
T
h
i
s
 
h
a
s
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
u
b
-
o
p
e
r
a
t
i
o
n
s
:


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
 
u
p
 
(
w
e
i
g
h
t
 
1
)
;


 
 
 
 
 
 
 
 
 
 
 
 
o
n
e
 
f
o
r
 
e
a
c
h
 
m
e
d
i
u
m
 
a
t
t
a
c
h
m
e
n
t
 
t
h
a
t
 
n
e
e
d
s
 
a
 
d
i
f
f
e
r
e
n
c
i
n
g
 
i
m
a
g
e
 
(
w
e
i
g
h
t
 
1
 
e
a
c
h
)
;


 
 
 
 
 
 
 
 
 
 
 
 
a
n
o
t
h
e
r
 
o
n
e
 
t
o
 
c
o
p
y
 
t
h
e
 
V
M
 
s
t
a
t
e
 
(
i
f
 
o
f
f
l
i
n
e
 
w
i
t
h
 
s
a
v
e
d
 
s
t
a
t
e
,
 
w
e
i
g
h
t
 
i
s
 
V
M
 
m
e
m
o
r
y
 
s
i
z
e
 
i
n
 
M
B
)
;


 
 
 
 
 
 
 
 
 
 
 
 
a
n
o
t
h
e
r
 
o
n
e
 
t
o
 
s
a
v
e
 
t
h
e
 
V
M
 
s
t
a
t
e
 
(
i
f
 
o
n
l
i
n
e
,
 
w
e
i
g
h
t
 
i
s
 
V
M
 
m
e
m
o
r
y
 
s
i
z
e
 
i
n
 
M
B
)
;


 
 
 
 
 
 
 
 
 
 
 
 
f
i
n
i
s
h
i
n
g
 
u
p
 
(
w
e
i
g
h
t
 
1
)




 
 
 
 
 
 
 
 
i
n
 
f
_
t
a
k
i
n
g
_
s
n
a
p
s
h
o
t
_
o
n
l
i
n
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
i
s
 
i
s
 
a
n
 
o
n
l
i
n
e
 
s
n
a
p
s
h
o
t
 
(
i
.
e
.
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
r
u
n
n
i
n
g
)
.




 
 
 
 
 
 
 
 
o
u
t
 
s
t
a
t
e
_
f
i
l
e
_
p
a
t
h
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
i
l
e
 
p
a
t
h
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
m
u
s
t
 
s
a
v
e
 
t
h
e
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
t
o
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
b
e
g
i
n
T
a
k
i
n
g
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
n
i
t
i
a
t
o
r
,
 
n
a
m
e
,
 
d
e
s
c
r
i
p
t
i
o
n
,
 
c
o
n
s
o
l
e
_
p
r
o
g
r
e
s
s
,
 
f
_
t
a
k
i
n
g
_
s
n
a
p
s
h
o
t
_
o
n
l
i
n
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
d
_
t
a
k
i
n
g
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
s
u
c
c
e
s
s
)
:


 
 
 
 
 
 
 
 
"
"
"
C
a
l
l
e
d
 
b
y
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
t
o
 
i
n
f
o
r
m
 
t
h
e
 
s
e
r
v
e
r
 
t
h
a
t
 
t
h
e
 
s
n
a
p
s
h
o
t


 
 
 
 
 
 
 
 
p
r
e
v
i
o
u
s
l
y
 
r
e
q
u
e
s
t
e
d
 
b
y
 
#
b
e
g
i
n
T
a
k
i
n
g
S
n
a
p
s
h
o
t
 
i
s
 
e
i
t
h
e
r


 
 
 
 
 
 
 
 
s
u
c
c
e
s
s
f
u
l
l
y
 
t
a
k
e
n
 
o
r
 
t
h
e
r
e
 
w
a
s
 
a
 
f
a
i
l
u
r
e
.




 
 
 
 
 
 
 
 
i
n
 
s
u
c
c
e
s
s
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
@
c
 
t
r
u
e
 
t
o
 
i
n
d
i
c
a
t
e
 
s
u
c
c
e
s
s
 
a
n
d
 
@
c
 
f
a
l
s
e
 
o
t
h
e
r
w
i
s
e




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
d
T
a
k
i
n
g
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
u
c
c
e
s
s
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
l
e
t
e
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
i
n
i
t
i
a
t
o
r
,
 
s
t
a
r
t
_
i
d
,
 
e
n
d
_
i
d
,
 
d
e
l
e
t
e
_
a
l
l
_
c
h
i
l
d
r
e
n
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
s
 
c
a
l
l
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
d
e
l
e
t
e
S
n
a
p
s
h
o
t
"
/
>
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
d
e
l
e
t
e
S
n
a
p
s
h
o
t
A
n
d
A
l
l
C
h
i
l
d
r
e
n
"
/
>
 
a
n
d


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
d
e
l
e
t
e
S
n
a
p
s
h
o
t
R
a
n
g
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
i
n
i
t
i
a
t
o
r
 
o
f
 
t
y
p
e
 
I
C
o
n
s
o
l
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
o
n
s
o
l
e
 
o
b
j
e
c
t
 
t
h
a
t
 
i
n
i
t
i
a
t
e
d
 
t
h
i
s
 
c
a
l
l
.




 
 
 
 
 
 
 
 
i
n
 
s
t
a
r
t
_
i
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
f
i
r
s
t
 
s
n
a
p
s
h
o
t
 
t
o
 
d
e
l
e
t
e
.




 
 
 
 
 
 
 
 
i
n
 
e
n
d
_
i
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
l
a
s
t
 
s
n
a
p
s
h
o
t
 
t
o
 
d
e
l
e
t
e
.




 
 
 
 
 
 
 
 
i
n
 
d
e
l
e
t
e
_
a
l
l
_
c
h
i
l
d
r
e
n
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
a
l
l
 
c
h
i
l
d
r
e
n
 
s
h
o
u
l
d
 
b
e
 
d
e
l
e
t
e
d
.




 
 
 
 
 
 
 
 
o
u
t
 
m
a
c
h
i
n
e
_
s
t
a
t
e
 
o
f
 
t
y
p
e
 
M
a
c
h
i
n
e
S
t
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
a
f
t
e
r
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
s
t
a
r
t
e
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
S
n
a
p
s
h
o
t
 
h
a
s
 
m
o
r
e
 
t
h
a
n
 
o
n
e
 
c
h
i
l
d
 
s
n
a
p
s
h
o
t
.
 
O
n
l
y
 
p
o
s
s
i
b
l
e
 
i
f
 
t
h
e


 
 
 
 
 
 
 
 
 
 
d
e
l
e
t
e
 
o
p
e
r
a
t
i
o
n
 
d
o
e
s
 
n
o
t
 
d
e
l
e
t
e
 
a
l
l
 
c
h
i
l
d
r
e
n
 
o
r
 
t
h
e
 
r
a
n
g
e
 
d
o
e
s


 
 
 
 
 
 
 
 
 
 
n
o
t
 
m
e
e
t
 
t
h
e
 
l
i
n
e
a
r
i
t
y
 
c
o
n
d
i
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
l
e
t
e
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
n
i
t
i
a
t
o
r
,
 
s
t
a
r
t
_
i
d
,
 
e
n
d
_
i
d
,
 
d
e
l
e
t
e
_
a
l
l
_
c
h
i
l
d
r
e
n
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
i
s
h
_
o
n
l
i
n
e
_
m
e
r
g
e
_
m
e
d
i
u
m
(
s
e
l
f
,
 
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
,
 
s
o
u
r
c
e
,
 
t
a
r
g
e
t
,
 
m
e
r
g
e
_
f
o
r
w
a
r
d
,
 
p
a
r
e
n
t
_
f
o
r
_
t
a
r
g
e
t
,
 
c
h
i
l
d
r
e
n
_
t
o
_
r
e
p
a
r
e
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
s
 
c
a
l
l
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
I
n
t
e
r
n
a
l
S
e
s
s
i
o
n
C
o
n
t
r
o
l
:
:
o
n
l
i
n
e
M
e
r
g
e
M
e
d
i
u
m
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
e
d
i
u
m
 
a
t
t
a
c
h
m
e
n
t
 
w
h
i
c
h
 
n
e
e
d
s
 
t
o
 
b
e
 
c
l
e
a
n
e
d
 
u
p
.




 
 
 
 
 
 
 
 
i
n
 
s
o
u
r
c
e
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
M
e
r
g
e
 
s
o
u
r
c
e
 
m
e
d
i
u
m
.




 
 
 
 
 
 
 
 
i
n
 
t
a
r
g
e
t
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
M
e
r
g
e
 
t
a
r
g
e
t
 
m
e
d
i
u
m
.




 
 
 
 
 
 
 
 
i
n
 
m
e
r
g
e
_
f
o
r
w
a
r
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
M
e
r
g
e
 
d
i
r
e
c
t
i
o
n
.




 
 
 
 
 
 
 
 
i
n
 
p
a
r
e
n
t
_
f
o
r
_
t
a
r
g
e
t
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
F
o
r
 
f
o
r
w
a
r
d
 
m
e
r
g
e
s
:
 
n
e
w
 
p
a
r
e
n
t
 
f
o
r
 
t
a
r
g
e
t
 
m
e
d
i
u
m
.




 
 
 
 
 
 
 
 
i
n
 
c
h
i
l
d
r
e
n
_
t
o
_
r
e
p
a
r
e
n
t
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
F
o
r
 
b
a
c
k
w
a
r
d
 
m
e
r
g
e
s
:
 
l
i
s
t
 
o
f
 
m
e
d
i
a
 
w
h
i
c
h
 
n
e
e
d
 
t
h
e
i
r
 
p
a
r
e
n
t
 
U
U
I
D


 
 
 
 
 
 
 
 
u
p
d
a
t
e
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
i
s
h
O
n
l
i
n
e
M
e
r
g
e
M
e
d
i
u
m
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
,
 
s
o
u
r
c
e
,
 
t
a
r
g
e
t
,
 
m
e
r
g
e
_
f
o
r
w
a
r
d
,
 
p
a
r
e
n
t
_
f
o
r
_
t
a
r
g
e
t
,
 
c
h
i
l
d
r
e
n
_
t
o
_
r
e
p
a
r
e
n
t
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
s
t
o
r
e
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
i
n
i
t
i
a
t
o
r
,
 
s
n
a
p
s
h
o
t
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
s
 
c
a
l
l
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
r
e
s
t
o
r
e
S
n
a
p
s
h
o
t
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
i
n
i
t
i
a
t
o
r
 
o
f
 
t
y
p
e
 
I
C
o
n
s
o
l
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
o
n
s
o
l
e
 
o
b
j
e
c
t
 
t
h
a
t
 
i
n
i
t
i
a
t
e
d
 
t
h
i
s
 
c
a
l
l
.




 
 
 
 
 
 
 
 
i
n
 
s
n
a
p
s
h
o
t
 
o
f
 
t
y
p
e
 
I
S
n
a
p
s
h
o
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
n
a
p
s
h
o
t
 
t
o
 
r
e
s
t
o
r
e
 
t
h
e
 
V
M
 
s
t
a
t
e
 
f
r
o
m
.




 
 
 
 
 
 
 
 
o
u
t
 
m
a
c
h
i
n
e
_
s
t
a
t
e
 
o
f
 
t
y
p
e
 
M
a
c
h
i
n
e
S
t
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
a
f
t
e
r
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
s
t
a
r
t
e
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
s
t
o
r
e
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
n
i
t
i
a
t
o
r
,
 
s
n
a
p
s
h
o
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
p
u
l
l
_
g
u
e
s
t
_
p
r
o
p
e
r
t
i
e
s
(
s
e
l
f
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
t
h
e
 
l
i
s
t
 
o
f
 
t
h
e
 
g
u
e
s
t
 
p
r
o
p
e
r
t
i
e
s
 
m
a
t
c
h
i
n
g
 
a
 
s
e
t
 
o
f
 
p
a
t
t
e
r
n
s
 
a
l
o
n
g


 
 
 
 
 
 
 
 
w
i
t
h
 
t
h
e
i
r
 
v
a
l
u
e
s
,
 
t
i
m
e
 
s
t
a
m
p
s
 
a
n
d
 
f
l
a
g
s
 
a
n
d
 
g
i
v
e
 
r
e
s
p
o
n
s
i
b
i
l
i
t
y
 
f
o
r


 
 
 
 
 
 
 
 
m
a
n
a
g
i
n
g
 
p
r
o
p
e
r
t
i
e
s
 
t
o
 
t
h
e
 
c
o
n
s
o
l
e
.




 
 
 
 
 
 
 
 
o
u
t
 
n
a
m
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
v
a
l
u
e
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.
 
T
h
e
 
a
r
r
a
y
 
e
n
t
r
i
e
s
 
m
a
t
c
h
 
t
h
e


 
 
 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
e
n
t
r
i
e
s
 
i
n
 
t
h
e
 
@
a
 
n
a
m
e
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
o
u
t
 
t
i
m
e
s
t
a
m
p
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
i
m
e
 
s
t
a
m
p
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.
 
T
h
e
 
a
r
r
a
y
 
e
n
t
r
i
e
s
 
m
a
t
c
h


 
 
 
 
 
 
 
 
 
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
e
n
t
r
i
e
s
 
i
n
 
t
h
e
 
@
a
 
n
a
m
e
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
o
u
t
 
f
l
a
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
f
l
a
g
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.
 
T
h
e
 
a
r
r
a
y
 
e
n
t
r
i
e
s
 
m
a
t
c
h
 
t
h
e


 
 
 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
e
n
t
r
i
e
s
 
i
n
 
t
h
e
 
@
a
 
n
a
m
e
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
u
l
l
G
u
e
s
t
P
r
o
p
e
r
t
i
e
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
p
u
s
h
_
g
u
e
s
t
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
n
a
m
e
,
 
v
a
l
u
e
,
 
t
i
m
e
s
t
a
m
p
,
 
f
l
a
g
s
)
:


 
 
 
 
 
 
 
 
"
"
"
U
p
d
a
t
e
 
a
 
s
i
n
g
l
e
 
g
u
e
s
t
 
p
r
o
p
e
r
t
y
 
i
n
 
I
M
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
b
e
 
u
p
d
a
t
e
d
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
v
a
l
u
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
i
n
 
t
i
m
e
s
t
a
m
p
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
i
m
e
s
t
a
m
p
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
i
n
 
f
l
a
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
f
l
a
g
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
u
s
h
G
u
e
s
t
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
v
a
l
u
e
,
 
t
i
m
e
s
t
a
m
p
,
 
f
l
a
g
s
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
l
o
c
k
_
m
e
d
i
a
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
L
o
c
k
s
 
a
l
l
 
m
e
d
i
a
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
 
f
o
r
 
w
r
i
t
i
n
g
 
a
n
d
 
p
a
r
e
n
t
s
 
o
f


 
 
 
 
 
 
 
 
a
t
t
a
c
h
e
d
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
 
(
i
f
 
a
n
y
)
 
f
o
r
 
r
e
a
d
i
n
g
.
 
T
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s


 
 
 
 
 
 
 
 
a
t
o
m
i
c
 
s
o
 
t
h
a
t
 
i
f
 
i
t
 
f
a
i
l
s
 
n
o
 
m
e
d
i
a
 
i
s
 
a
c
t
u
a
l
l
y
 
l
o
c
k
e
d
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
i
n
t
e
n
d
e
d
 
t
o
 
b
e
 
c
a
l
l
e
d
 
w
h
e
n
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
i
n
 
S
t
a
r
t
i
n
g
 
o
r


 
 
 
 
 
 
 
 
R
e
s
t
o
r
i
n
g
 
s
t
a
t
e
.
 
T
h
e
 
l
o
c
k
e
d
 
m
e
d
i
a
 
w
i
l
l
 
b
e
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
u
n
l
o
c
k
e
d
 
w
h
e
n


 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
p
o
w
e
r
e
d
 
o
f
f
 
o
r
 
c
r
a
s
h
e
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
l
o
c
k
M
e
d
i
a
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
u
n
l
o
c
k
_
m
e
d
i
a
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
U
n
l
o
c
k
s
 
a
l
l
 
m
e
d
i
a
 
p
r
e
v
i
o
u
s
l
y
 
l
o
c
k
e
d
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
I
n
t
e
r
n
a
l
M
a
c
h
i
n
e
C
o
n
t
r
o
l
:
:
l
o
c
k
M
e
d
i
a
"
/
>
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
i
n
t
e
n
d
e
d
 
t
o
 
b
e
 
u
s
e
d
 
w
i
t
h
 
t
e
l
e
p
o
r
t
a
t
i
o
n
 
s
o
 
t
h
a
t
 
i
t
 
i
s


 
 
 
 
 
 
 
 
p
o
s
s
i
b
l
e
 
t
o
 
t
e
l
e
p
o
r
t
 
b
e
t
w
e
e
n
 
p
r
o
c
e
s
s
e
s
 
o
n
 
t
h
e
 
s
a
m
e
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
u
n
l
o
c
k
M
e
d
i
a
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
j
e
c
t
_
m
e
d
i
u
m
(
s
e
l
f
,
 
a
t
t
a
c
h
m
e
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
T
e
l
l
s
 
V
B
o
x
S
V
C
 
t
h
a
t
 
t
h
e
 
g
u
e
s
t
 
h
a
s
 
e
j
e
c
t
e
d
 
t
h
e
 
m
e
d
i
u
m
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h


 
 
 
 
 
 
 
 
t
h
e
 
m
e
d
i
u
m
 
a
t
t
a
c
h
m
e
n
t
.




 
 
 
 
 
 
 
 
i
n
 
a
t
t
a
c
h
m
e
n
t
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
e
d
i
u
m
 
a
t
t
a
c
h
m
e
n
t
 
w
h
e
r
e
 
t
h
e
 
e
j
e
c
t
 
h
a
p
p
e
n
e
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
w
_
a
t
t
a
c
h
m
e
n
t
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t


 
 
 
 
 
 
 
 
 
 
 
 
A
 
n
e
w
 
r
e
f
e
r
e
n
c
e
 
t
o
 
t
h
e
 
m
e
d
i
u
m
 
a
t
t
a
c
h
m
e
n
t
,
 
a
s
 
t
h
e
 
c
o
n
f
i
g
 
c
h
a
n
g
e
 
c
a
n


 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
i
n
 
t
h
e
 
c
r
e
a
t
i
o
n
 
o
f
 
a
 
n
e
w
 
i
n
s
t
a
n
c
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
n
e
w
_
a
t
t
a
c
h
m
e
n
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
j
e
c
t
M
e
d
i
u
m
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
a
t
t
a
c
h
m
e
n
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
w
_
a
t
t
a
c
h
m
e
n
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
p
o
r
t
_
v
m
_
s
t
a
t
i
s
t
i
c
s
(
s
e
l
f
,
 
v
a
l
i
d
_
s
t
a
t
s
,
 
c
p
u
_
u
s
e
r
,
 
c
p
u
_
k
e
r
n
e
l
,
 
c
p
u
_
i
d
l
e
,
 
m
e
m
_
t
o
t
a
l
,
 
m
e
m
_
f
r
e
e
,
 
m
e
m
_
b
a
l
l
o
o
n
,
 
m
e
m
_
s
h
a
r
e
d
,
 
m
e
m
_
c
a
c
h
e
,
 
p
a
g
e
d
_
t
o
t
a
l
,
 
m
e
m
_
a
l
l
o
c
_
t
o
t
a
l
,
 
m
e
m
_
f
r
e
e
_
t
o
t
a
l
,
 
m
e
m
_
b
a
l
l
o
o
n
_
t
o
t
a
l
,
 
m
e
m
_
s
h
a
r
e
d
_
t
o
t
a
l
,
 
v
m
_
n
e
t
_
r
x
,
 
v
m
_
n
e
t
_
t
x
)
:


 
 
 
 
 
 
 
 
"
"
"
P
a
s
s
e
s
 
s
t
a
t
i
s
t
i
c
s
 
c
o
l
l
e
c
t
e
d
 
b
y
 
V
M
 
(
i
n
c
l
u
d
i
n
g
 
g
u
e
s
t
 
s
t
a
t
i
s
t
i
c
s
)
 
t
o
 
V
B
o
x
S
V
C
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
i
d
_
s
t
a
t
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
M
a
s
k
 
d
e
f
i
n
i
n
g
 
w
h
i
c
h
 
p
a
r
a
m
e
t
e
r
s
 
a
r
e
 
v
a
l
i
d
.
 
F
o
r
 
e
x
a
m
p
l
e
:
 
0
x
1
1
 
m
e
a
n
s


 
 
 
 
 
 
 
 
 
 
t
h
a
t
 
c
p
u
I
d
l
e
 
a
n
d
 
X
X
X
 
a
r
e
 
v
a
l
i
d
.
 
O
t
h
e
r
 
p
a
r
a
m
e
t
e
r
s
 
s
h
o
u
l
d
 
b
e
 
i
g
n
o
r
e
d
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
_
u
s
e
r
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
e
r
c
e
n
t
a
g
e
 
o
f
 
p
r
o
c
e
s
s
o
r
 
t
i
m
e
 
s
p
e
n
t
 
i
n
 
u
s
e
r
 
m
o
d
e
 
a
s
 
s
e
e
n
 
b
y
 
t
h
e
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
_
k
e
r
n
e
l
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
e
r
c
e
n
t
a
g
e
 
o
f
 
p
r
o
c
e
s
s
o
r
 
t
i
m
e
 
s
p
e
n
t
 
i
n
 
k
e
r
n
e
l
 
m
o
d
e
 
a
s
 
s
e
e
n
 
b
y
 
t
h
e
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
_
i
d
l
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
e
r
c
e
n
t
a
g
e
 
o
f
 
p
r
o
c
e
s
s
o
r
 
t
i
m
e
 
s
p
e
n
t
 
i
d
l
i
n
g
 
a
s
 
s
e
e
n
 
b
y
 
t
h
e
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
t
o
t
a
l
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
o
t
a
l
 
a
m
o
u
n
t
 
o
f
 
p
h
y
s
i
c
a
l
 
g
u
e
s
t
 
R
A
M
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
f
r
e
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
F
r
e
e
 
a
m
o
u
n
t
 
o
f
 
p
h
y
s
i
c
a
l
 
g
u
e
s
t
 
R
A
M
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
b
a
l
l
o
o
n
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
A
m
o
u
n
t
 
o
f
 
b
a
l
l
o
o
n
e
d
 
p
h
y
s
i
c
a
l
 
g
u
e
s
t
 
R
A
M
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
s
h
a
r
e
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
A
m
o
u
n
t
 
o
f
 
s
h
a
r
e
d
 
p
h
y
s
i
c
a
l
 
g
u
e
s
t
 
R
A
M
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
c
a
c
h
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
o
t
a
l
 
a
m
o
u
n
t
 
o
f
 
g
u
e
s
t
 
(
d
i
s
k
)
 
c
a
c
h
e
 
m
e
m
o
r
y
.




 
 
 
 
 
 
 
 
i
n
 
p
a
g
e
d
_
t
o
t
a
l
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
o
t
a
l
 
a
m
o
u
n
t
 
o
f
 
s
p
a
c
e
 
i
n
 
t
h
e
 
p
a
g
e
 
f
i
l
e
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
a
l
l
o
c
_
t
o
t
a
l
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
o
t
a
l
 
a
m
o
u
n
t
 
o
f
 
m
e
m
o
r
y
 
a
l
l
o
c
a
t
e
d
 
b
y
 
t
h
e
 
h
y
p
e
r
v
i
s
o
r
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
f
r
e
e
_
t
o
t
a
l
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
o
t
a
l
 
a
m
o
u
n
t
 
o
f
 
f
r
e
e
 
m
e
m
o
r
y
 
a
v
a
i
l
a
b
l
e
 
i
n
 
t
h
e
 
h
y
p
e
r
v
i
s
o
r
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
b
a
l
l
o
o
n
_
t
o
t
a
l
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
o
t
a
l
 
a
m
o
u
n
t
 
o
f
 
m
e
m
o
r
y
 
b
a
l
l
o
o
n
e
d
 
b
y
 
t
h
e
 
h
y
p
e
r
v
i
s
o
r
.




 
 
 
 
 
 
 
 
i
n
 
m
e
m
_
s
h
a
r
e
d
_
t
o
t
a
l
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
o
t
a
l
 
a
m
o
u
n
t
 
o
f
 
s
h
a
r
e
d
 
m
e
m
o
r
y
 
i
n
 
t
h
e
 
h
y
p
e
r
v
i
s
o
r
.




 
 
 
 
 
 
 
 
i
n
 
v
m
_
n
e
t
_
r
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
N
e
t
w
o
r
k
 
r
e
c
e
i
v
e
 
r
a
t
e
 
f
o
r
 
V
M
.




 
 
 
 
 
 
 
 
i
n
 
v
m
_
n
e
t
_
t
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
N
e
t
w
o
r
k
 
t
r
a
n
s
m
i
t
 
r
a
t
e
 
f
o
r
 
V
M
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
p
o
r
t
V
m
S
t
a
t
i
s
t
i
c
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
v
a
l
i
d
_
s
t
a
t
s
,
 
c
p
u
_
u
s
e
r
,
 
c
p
u
_
k
e
r
n
e
l
,
 
c
p
u
_
i
d
l
e
,
 
m
e
m
_
t
o
t
a
l
,
 
m
e
m
_
f
r
e
e
,
 
m
e
m
_
b
a
l
l
o
o
n
,
 
m
e
m
_
s
h
a
r
e
d
,
 
m
e
m
_
c
a
c
h
e
,
 
p
a
g
e
d
_
t
o
t
a
l
,
 
m
e
m
_
a
l
l
o
c
_
t
o
t
a
l
,
 
m
e
m
_
f
r
e
e
_
t
o
t
a
l
,
 
m
e
m
_
b
a
l
l
o
o
n
_
t
o
t
a
l
,
 
m
e
m
_
s
h
a
r
e
d
_
t
o
t
a
l
,
 
v
m
_
n
e
t
_
r
x
,
 
v
m
_
n
e
t
_
t
x
]
)


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
B
I
O
S
S
e
t
t
i
n
g
s
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
B
I
O
S
S
e
t
t
i
n
g
s
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
B
I
O
S
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
.
 
T
h
i
s
 
i
s
 
u
s
e
d
 
o
n
l
y
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
B
I
O
S
S
e
t
t
i
n
g
s
"
/
>
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
8
b
5
4
2
7
9
-
d
c
3
5
-
4
f
5
e
-
a
4
3
1
-
8
3
5
b
8
6
7
c
6
b
5
e
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
o
g
o
_
f
a
d
e
_
i
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
l
o
g
o
F
a
d
e
I
n
'


 
 
 
 
 
 
 
 
F
a
d
e
 
i
n
 
f
l
a
g
 
f
o
r
 
B
I
O
S
 
l
o
g
o
 
a
n
i
m
a
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
o
g
o
F
a
d
e
I
n
'
,
 
b
o
o
l
)




 
 
 
 
@
l
o
g
o
_
f
a
d
e
_
i
n
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
l
o
g
o
_
f
a
d
e
_
i
n
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
l
o
g
o
F
a
d
e
I
n
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
o
g
o
_
f
a
d
e
_
o
u
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
l
o
g
o
F
a
d
e
O
u
t
'


 
 
 
 
 
 
 
 
F
a
d
e
 
o
u
t
 
f
l
a
g
 
f
o
r
 
B
I
O
S
 
l
o
g
o
 
a
n
i
m
a
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
o
g
o
F
a
d
e
O
u
t
'
,
 
b
o
o
l
)




 
 
 
 
@
l
o
g
o
_
f
a
d
e
_
o
u
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
l
o
g
o
_
f
a
d
e
_
o
u
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
l
o
g
o
F
a
d
e
O
u
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
o
g
o
_
d
i
s
p
l
a
y
_
t
i
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
l
o
g
o
D
i
s
p
l
a
y
T
i
m
e
'


 
 
 
 
 
 
 
 
B
I
O
S
 
l
o
g
o
 
d
i
s
p
l
a
y
 
t
i
m
e
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
 
(
0
 
=
 
d
e
f
a
u
l
t
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
o
g
o
D
i
s
p
l
a
y
T
i
m
e
'
,
 
i
n
t
)




 
 
 
 
@
l
o
g
o
_
d
i
s
p
l
a
y
_
t
i
m
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
l
o
g
o
_
d
i
s
p
l
a
y
_
t
i
m
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
l
o
g
o
D
i
s
p
l
a
y
T
i
m
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
o
g
o
_
i
m
a
g
e
_
p
a
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
l
o
g
o
I
m
a
g
e
P
a
t
h
'


 
 
 
 
 
 
 
 
L
o
c
a
l
 
f
i
l
e
 
s
y
s
t
e
m
 
p
a
t
h
 
f
o
r
 
e
x
t
e
r
n
a
l
 
B
I
O
S
 
s
p
l
a
s
h
 
i
m
a
g
e
.
 
E
m
p
t
y
 
s
t
r
i
n
g


 
 
 
 
 
 
 
 
m
e
a
n
s
 
t
h
e
 
d
e
f
a
u
l
t
 
i
m
a
g
e
 
i
s
 
s
h
o
w
n
 
o
n
 
b
o
o
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
o
g
o
I
m
a
g
e
P
a
t
h
'
,
 
s
t
r
)




 
 
 
 
@
l
o
g
o
_
i
m
a
g
e
_
p
a
t
h
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
l
o
g
o
_
i
m
a
g
e
_
p
a
t
h
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
l
o
g
o
I
m
a
g
e
P
a
t
h
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
o
o
t
_
m
e
n
u
_
m
o
d
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
B
I
O
S
B
o
o
t
M
e
n
u
M
o
d
e
 
v
a
l
u
e
 
f
o
r
 
'
b
o
o
t
M
e
n
u
M
o
d
e
'


 
 
 
 
 
 
 
 
M
o
d
e
 
o
f
 
t
h
e
 
B
I
O
S
 
b
o
o
t
 
d
e
v
i
c
e
 
m
e
n
u
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
o
o
t
M
e
n
u
M
o
d
e
'
,
 
B
I
O
S
B
o
o
t
M
e
n
u
M
o
d
e
)




 
 
 
 
@
b
o
o
t
_
m
e
n
u
_
m
o
d
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
b
o
o
t
_
m
e
n
u
_
m
o
d
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
b
o
o
t
M
e
n
u
M
o
d
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
c
p
i
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
A
C
P
I
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
A
C
P
I
 
s
u
p
p
o
r
t
 
f
l
a
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
A
C
P
I
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
a
c
p
i
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
c
p
i
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
A
C
P
I
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
o
a
p
i
c
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
I
O
A
P
I
C
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
I
O
 
A
P
I
C
 
s
u
p
p
o
r
t
 
f
l
a
g
.
 
I
f
 
s
e
t
,
 
V
i
r
t
u
a
l
B
o
x
 
w
i
l
l
 
p
r
o
v
i
d
e
 
a
n
 
I
O
 
A
P
I
C


 
 
 
 
 
 
 
 
a
n
d
 
s
u
p
p
o
r
t
 
I
R
Q
s
 
a
b
o
v
e
 
1
5
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
O
A
P
I
C
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
i
o
a
p
i
c
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
i
o
a
p
i
c
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
I
O
A
P
I
C
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
i
m
e
_
o
f
f
s
e
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
t
i
m
e
O
f
f
s
e
t
'


 
 
 
 
 
 
 
 
O
f
f
s
e
t
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
 
f
r
o
m
 
t
h
e
 
h
o
s
t
 
s
y
s
t
e
m
 
t
i
m
e
.
 
T
h
i
s
 
a
l
l
o
w
s
 
f
o
r


 
 
 
 
 
 
 
 
g
u
e
s
t
s
 
r
u
n
n
i
n
g
 
w
i
t
h
 
a
 
d
i
f
f
e
r
e
n
t
 
s
y
s
t
e
m
 
d
a
t
e
/
t
i
m
e
 
t
h
a
n
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
I
t
 
i
s
 
e
q
u
i
v
a
l
e
n
t
 
t
o
 
s
e
t
t
i
n
g
 
t
h
e
 
s
y
s
t
e
m
 
d
a
t
e
/
t
i
m
e
 
i
n
 
t
h
e
 
B
I
O
S
 
e
x
c
e
p
t


 
 
 
 
 
 
 
 
i
t
 
i
s
 
n
o
t
 
a
n
 
a
b
s
o
l
u
t
e
 
v
a
l
u
e
 
b
u
t
 
a
 
r
e
l
a
t
i
v
e
 
o
n
e
.
 
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s


 
 
 
 
 
 
 
 
t
i
m
e
 
s
y
n
c
h
r
o
n
i
z
a
t
i
o
n
 
h
o
n
o
r
s
 
t
h
i
s
 
o
f
f
s
e
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
i
m
e
O
f
f
s
e
t
'
,
 
i
n
t
)




 
 
 
 
@
t
i
m
e
_
o
f
f
s
e
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
t
i
m
e
_
o
f
f
s
e
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
t
i
m
e
O
f
f
s
e
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
x
e
_
d
e
b
u
g
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
P
X
E
D
e
b
u
g
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
P
X
E
 
d
e
b
u
g
 
l
o
g
g
i
n
g
 
f
l
a
g
.
 
I
f
 
s
e
t
,
 
V
i
r
t
u
a
l
B
o
x
 
w
i
l
l
 
w
r
i
t
e
 
e
x
t
e
n
s
i
v
e


 
 
 
 
 
 
 
 
P
X
E
 
t
r
a
c
e
 
i
n
f
o
r
m
a
t
i
o
n
 
t
o
 
t
h
e
 
r
e
l
e
a
s
e
 
l
o
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
P
X
E
D
e
b
u
g
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
p
x
e
_
d
e
b
u
g
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
p
x
e
_
d
e
b
u
g
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
P
X
E
D
e
b
u
g
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)






c
l
a
s
s
 
I
P
C
I
A
d
d
r
e
s
s
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
A
d
d
r
e
s
s
 
o
n
 
t
h
e
 
P
C
I
 
b
u
s
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
D
8
8
B
3
2
4
F
-
D
B
1
9
-
4
D
3
B
-
A
1
A
9
-
B
F
5
B
1
2
7
1
9
9
A
8
'


 
 
 
 
w
s
m
a
p
 
=
 
'
s
t
r
u
c
t
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
u
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
b
u
s
'


 
 
 
 
 
 
 
 
B
u
s
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
u
s
'
,
 
i
n
t
)




 
 
 
 
@
b
u
s
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
b
u
s
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
b
u
s
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
v
i
c
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
d
e
v
i
c
e
'


 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
v
i
c
e
'
,
 
i
n
t
)




 
 
 
 
@
d
e
v
i
c
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
v
i
c
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
v
i
c
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
v
_
f
u
n
c
t
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
d
e
v
F
u
n
c
t
i
o
n
'


 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
f
u
n
c
t
i
o
n
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
v
F
u
n
c
t
i
o
n
'
,
 
i
n
t
)




 
 
 
 
@
d
e
v
_
f
u
n
c
t
i
o
n
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
v
_
f
u
n
c
t
i
o
n
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
v
F
u
n
c
t
i
o
n
'
,
 
v
a
l
u
e
)




 
 
 
 
d
e
f
 
a
s
_
l
o
n
g
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
C
o
n
v
e
r
t
 
P
C
I
 
a
d
d
r
e
s
s
 
i
n
t
o
 
l
o
n
g
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
s
L
o
n
g
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
u
l
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
r
o
m
_
l
o
n
g
(
s
e
l
f
,
 
n
u
m
b
e
r
)
:


 
 
 
 
 
 
 
 
"
"
"
M
a
k
e
 
P
C
I
 
a
d
d
r
e
s
s
 
f
r
o
m
 
l
o
n
g
.




 
 
 
 
 
 
 
 
i
n
 
n
u
m
b
e
r
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
r
o
m
L
o
n
g
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
u
m
b
e
r
]
)


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
P
C
I
D
e
v
i
c
e
A
t
t
a
c
h
m
e
n
t
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
I
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
P
C
I
 
a
t
t
a
c
h
m
e
n
t
s
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
9
1
f
3
3
d
6
f
-
e
6
2
1
-
4
f
7
0
-
a
7
7
e
-
1
5
f
0
e
3
c
7
1
4
d
5
'


 
 
 
 
w
s
m
a
p
 
=
 
'
s
t
r
u
c
t
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
a
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
a
m
e
'


 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
n
a
m
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
a
m
e
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
s
_
p
h
y
s
i
c
a
l
_
d
e
v
i
c
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
i
s
P
h
y
s
i
c
a
l
D
e
v
i
c
e
'


 
 
 
 
 
 
 
 
I
f
 
t
h
i
s
 
i
s
 
p
h
y
s
i
c
a
l
 
o
r
 
v
i
r
t
u
a
l
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
s
P
h
y
s
i
c
a
l
D
e
v
i
c
e
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
o
s
t
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
h
o
s
t
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
A
d
d
r
e
s
s
 
o
f
 
d
e
v
i
c
e
 
o
n
 
t
h
e
 
h
o
s
t
,
 
a
p
p
l
i
c
a
b
l
e
 
o
n
l
y
 
t
o
 
h
o
s
t
 
d
e
v
i
c
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
h
o
s
t
A
d
d
r
e
s
s
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
u
e
s
t
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
g
u
e
s
t
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
A
d
d
r
e
s
s
 
o
f
 
d
e
v
i
c
e
 
o
n
 
t
h
e
 
g
u
e
s
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
u
e
s
t
A
d
d
r
e
s
s
'
,
 
i
n
t
)






c
l
a
s
s
 
I
M
a
c
h
i
n
e
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
M
a
c
h
i
n
e
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
,
 
o
r
 
g
u
e
s
t
,
 
c
r
e
a
t
e
d


 
 
 
 
 
 
i
n
 
V
i
r
t
u
a
l
B
o
x
.




 
 
 
 
 
 
T
h
i
s
 
i
n
t
e
r
f
a
c
e
 
i
s
 
u
s
e
d
 
i
n
 
t
w
o
 
c
o
n
t
e
x
t
s
.
 
F
i
r
s
t
 
o
f
 
a
l
l
,
 
a
 
c
o
l
l
e
c
t
i
o
n
 
o
f


 
 
 
 
 
 
o
b
j
e
c
t
s
 
i
m
p
l
e
m
e
n
t
i
n
g
 
t
h
i
s
 
i
n
t
e
r
f
a
c
e
 
i
s
 
s
t
o
r
e
d
 
i
n
 
t
h
e


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
m
a
c
h
i
n
e
s
"
/
>
 
a
t
t
r
i
b
u
t
e
 
w
h
i
c
h
 
l
i
s
t
s
 
a
l
l
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
m
a
c
h
i
n
e
s
 
t
h
a
t
 
a
r
e
 
c
u
r
r
e
n
t
l
y
 
r
e
g
i
s
t
e
r
e
d
 
w
i
t
h
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
i
n
s
t
a
l
l
a
t
i
o
n
.
 
A
l
s
o
,
 
o
n
c
e
 
a
 
s
e
s
s
i
o
n
 
h
a
s
 
b
e
e
n
 
o
p
e
n
e
d
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
v
i
r
t
u
a
l


 
 
 
 
 
 
m
a
c
h
i
n
e
 
(
e
.
g
.
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
r
u
n
n
i
n
g
)
,
 
t
h
e
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t


 
 
 
 
 
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
t
h
e
 
o
p
e
n
 
s
e
s
s
i
o
n
 
c
a
n
 
b
e
 
q
u
e
r
i
e
d
 
f
r
o
m
 
t
h
e
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
;


 
 
 
 
 
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
"
/
>
 
f
o
r
 
d
e
t
a
i
l
s
.




 
 
 
 
 
 
T
h
e
 
m
a
i
n
 
r
o
l
e
 
o
f
 
t
h
i
s
 
i
n
t
e
r
f
a
c
e
 
i
s
 
t
o
 
e
x
p
o
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
m
a
c
h
i
n
e
 
a
n
d
 
p
r
o
v
i
d
e
 
m
e
t
h
o
d
s
 
t
o
 
c
h
a
n
g
e
 
v
a
r
i
o
u
s
 
a
s
p
e
c
t
s
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
m
a
c
h
i
n
e
'
s
 
c
o
n
f
i
g
u
r
a
t
i
o
n
.
 
F
o
r
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
s
 
s
t
o
r
e
d
 
i
n
 
t
h
e


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
m
a
c
h
i
n
e
s
"
/
>
 
c
o
l
l
e
c
t
i
o
n
,
 
a
l
l
 
a
t
t
r
i
b
u
t
e
s
 
a
r
e


 
 
 
 
 
 
r
e
a
d
-
o
n
l
y
 
u
n
l
e
s
s
 
e
x
p
l
i
c
i
t
l
y
 
s
t
a
t
e
d
 
o
t
h
e
r
w
i
s
e
 
i
n
 
i
n
d
i
v
i
d
u
a
l
 
a
t
t
r
i
b
u
t
e


 
 
 
 
 
 
a
n
d
 
m
e
t
h
o
d
 
d
e
s
c
r
i
p
t
i
o
n
s
.




 
 
 
 
 
 
I
n
 
o
r
d
e
r
 
t
o
 
c
h
a
n
g
e
 
a
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
,
 
a
 
s
e
s
s
i
o
n
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
 
m
u
s
t
 
b
e


 
 
 
 
 
 
o
p
e
n
e
d
 
u
s
i
n
g
 
o
n
e
 
o
f
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
o
c
k
M
a
c
h
i
n
e
"
/
>
 
o
r


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
m
e
t
h
o
d
s
.
 
A
f
t
e
r
 
t
h
e


 
 
 
 
 
 
m
a
c
h
i
n
e
 
h
a
s
 
b
e
e
n
 
s
u
c
c
e
s
s
f
u
l
l
y
 
l
o
c
k
e
d
 
f
o
r
 
a
 
s
e
s
s
i
o
n
,
 
a
 
m
u
t
a
b
l
e
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t


 
 
 
 
 
 
n
e
e
d
s
 
t
o
 
b
e
 
q
u
e
r
i
e
d
 
f
r
o
m
 
t
h
e
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
 
a
n
d
 
t
h
e
n
 
t
h
e
 
d
e
s
i
r
e
d
 
s
e
t
t
i
n
g
s


 
 
 
 
 
 
c
h
a
n
g
e
s
 
c
a
n
 
b
e
 
a
p
p
l
i
e
d
 
t
o
 
t
h
e
 
r
e
t
u
r
n
e
d
 
o
b
j
e
c
t
 
u
s
i
n
g
 
I
M
a
c
h
i
n
e
 
a
t
t
r
i
b
u
t
e
s
 
a
n
d


 
 
 
 
 
 
m
e
t
h
o
d
s
.
 
S
e
e
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
"
/
>
 
i
n
t
e
r
f
a
c
e
 
d
e
s
c
r
i
p
t
i
o
n
 
f
o
r
 
m
o
r
e


 
 
 
 
 
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
s
e
s
s
i
o
n
s
.




 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
I
M
a
c
h
i
n
e
 
d
o
e
s
 
n
o
t
 
p
r
o
v
i
d
e
 
m
e
t
h
o
d
s
 
t
o
 
c
o
n
t
r
o
l
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e


 
 
 
 
 
 
e
x
e
c
u
t
i
o
n
 
(
s
u
c
h
 
a
s
 
s
t
a
r
t
 
t
h
e
 
m
a
c
h
i
n
e
,
 
o
r
 
p
o
w
e
r
 
i
t
 
d
o
w
n
)
 
-
-
 
t
h
e
s
e
 
m
e
t
h
o
d
s


 
 
 
 
 
 
a
r
e
 
g
r
o
u
p
e
d
 
i
n
 
a
 
s
e
p
a
r
a
t
e
 
i
n
t
e
r
f
a
c
e
 
c
a
l
l
e
d
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
"
/
>
.




 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
"
/
>
,
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
"
/
>


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
2
5
8
f
4
e
5
5
-
4
0
f
6
-
4
8
0
4
-
a
1
6
2
-
6
0
c
3
0
2
a
3
4
d
9
9
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
a
r
e
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
V
i
r
t
u
a
l
B
o
x
 
v
a
l
u
e
 
f
o
r
 
'
p
a
r
e
n
t
'


 
 
 
 
 
 
 
 
A
s
s
o
c
i
a
t
e
d
 
p
a
r
e
n
t
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
a
r
e
n
t
'
,
 
I
V
i
r
t
u
a
l
B
o
x
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
c
c
e
s
s
i
b
l
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
c
c
e
s
s
i
b
l
e
'


 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
i
s
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
c
u
r
r
e
n
t
l
y
 
a
c
c
e
s
s
i
b
l
e
 
o
r
 
n
o
t
.




 
 
 
 
 
 
 
 
A
 
m
a
c
h
i
n
e
 
i
s
 
a
l
w
a
y
s
 
d
e
e
m
e
d
 
a
c
c
e
s
s
i
b
l
e
 
u
n
l
e
s
s
 
i
t
 
i
s
 
r
e
g
i
s
t
e
r
e
d
 
a
n
d


 
 
 
 
 
 
 
 
i
t
s
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
c
a
n
n
o
t
 
b
e
 
r
e
a
d
 
o
r
 
p
a
r
s
e
d
 
(
e
i
t
h
e
r
 
b
e
c
a
u
s
e
 
t
h
e
 
f
i
l
e
 
i
t
s
e
l
f


 
 
 
 
 
 
 
 
i
s
 
u
n
a
v
a
i
l
a
b
l
e
 
o
r
 
h
a
s
 
i
n
v
a
l
i
d
 
X
M
L
 
c
o
n
t
e
n
t
s
)
.




 
 
 
 
 
 
 
 
E
v
e
r
y
 
t
i
m
e
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
r
e
a
d
,
 
t
h
e
 
a
c
c
e
s
s
i
b
i
l
i
t
y
 
s
t
a
t
e
 
o
f


 
 
 
 
 
 
 
 
t
h
i
s
 
m
a
c
h
i
n
e
 
i
s
 
r
e
-
e
v
a
l
u
a
t
e
d
.
 
I
f
 
t
h
e
 
r
e
t
u
r
n
e
d
 
v
a
l
u
e
 
i
s
 
@
c
 
f
a
l
s
e
,


 
 
 
 
 
 
 
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
a
c
c
e
s
s
E
r
r
o
r
"
/
>
 
p
r
o
p
e
r
t
y
 
m
a
y
 
b
e
 
u
s
e
d
 
t
o
 
g
e
t
 
t
h
e


 
 
 
 
 
 
 
 
d
e
t
a
i
l
e
d
 
e
r
r
o
r
 
i
n
f
o
r
m
a
t
i
o
n
 
d
e
s
c
r
i
b
i
n
g
 
t
h
e
 
r
e
a
s
o
n
 
o
f


 
 
 
 
 
 
 
 
i
n
a
c
c
e
s
s
i
b
i
l
i
t
y
,
 
i
n
c
l
u
d
i
n
g
 
X
M
L
 
e
r
r
o
r
 
m
e
s
s
a
g
e
s
.




 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
i
n
a
c
c
e
s
s
i
b
l
e
,
 
o
n
l
y
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
p
r
o
p
e
r
t
i
e
s


 
 
 
 
 
 
 
 
c
a
n
 
b
e
 
u
s
e
d
 
o
n
 
i
t
:


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
p
a
r
e
n
t
"
/
>


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
i
d
"
/
>


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
e
t
t
i
n
g
s
F
i
l
e
P
a
t
h
"
/
>


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
a
c
c
e
s
s
i
b
l
e
"
/
>


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
a
c
c
e
s
s
E
r
r
o
r
"
/
>


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
A
n
 
a
t
t
e
m
p
t
 
t
o
 
a
c
c
e
s
s
 
a
n
y
 
o
t
h
e
r
 
p
r
o
p
e
r
t
y
 
o
r
 
m
e
t
h
o
d
 
w
i
l
l
 
r
e
t
u
r
n


 
 
 
 
 
 
 
 
a
n
 
e
r
r
o
r
.




 
 
 
 
 
 
 
 
T
h
e
 
o
n
l
y
 
p
o
s
s
i
b
l
e
 
a
c
t
i
o
n
 
y
o
u
 
c
a
n
 
p
e
r
f
o
r
m
 
o
n
 
a
n
 
i
n
a
c
c
e
s
s
i
b
l
e


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
i
s
 
t
o
 
u
n
r
e
g
i
s
t
e
r
 
i
t
 
u
s
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
u
n
r
e
g
i
s
t
e
r
"
/
>
 
c
a
l
l
 
(
o
r
,
 
t
o
 
c
h
e
c
k


 
 
 
 
 
 
 
 
f
o
r
 
t
h
e
 
a
c
c
e
s
s
i
b
i
l
i
t
y
 
s
t
a
t
e
 
o
n
c
e
 
m
o
r
e
 
b
y
 
q
u
e
r
y
i
n
g
 
t
h
i
s


 
 
 
 
 
 
 
 
p
r
o
p
e
r
t
y
)
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
n
 
t
h
e
 
c
u
r
r
e
n
t
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
,
 
o
n
c
e
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
r
e
t
u
r
n
s


 
 
 
 
 
 
 
 
 
 
@
c
 
t
r
u
e
,
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
n
e
v
e
r
 
b
e
c
o
m
e
 
i
n
a
c
c
e
s
s
i
b
l
e


 
 
 
 
 
 
 
 
 
 
l
a
t
e
r
,
 
e
v
e
n
 
i
f
 
i
t
s
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
c
a
n
n
o
t
 
b
e
 
s
u
c
c
e
s
s
f
u
l
l
y


 
 
 
 
 
 
 
 
 
 
r
e
a
d
/
w
r
i
t
t
e
n
 
a
n
y
 
m
o
r
e
 
(
a
t
 
l
e
a
s
t
,
 
u
n
t
i
l
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
i
s
 
r
e
s
t
a
r
t
e
d
)
.
 
T
h
i
s
 
l
i
m
i
t
a
t
i
o
n
 
m
a
y
 
b
e
 
r
e
m
o
v
e
d
 
i
n


 
 
 
 
 
 
 
 
 
 
f
u
t
u
r
e
 
r
e
l
e
a
s
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
c
c
e
s
s
i
b
l
e
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
c
c
e
s
s
_
e
r
r
o
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
 
v
a
l
u
e
 
f
o
r
 
'
a
c
c
e
s
s
E
r
r
o
r
'


 
 
 
 
 
 
 
 
E
r
r
o
r
 
i
n
f
o
r
m
a
t
i
o
n
 
d
e
s
c
r
i
b
i
n
g
 
t
h
e
 
r
e
a
s
o
n
 
o
f
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
i
n
a
c
c
e
s
s
i
b
i
l
i
t
y
.




 
 
 
 
 
 
 
 
R
e
a
d
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
o
n
l
y
 
v
a
l
i
d
 
a
f
t
e
r
 
t
h
e
 
l
a
s
t
 
c
a
l
l
 
t
o


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
a
c
c
e
s
s
i
b
l
e
"
/
>
 
r
e
t
u
r
n
e
d
 
@
c
 
f
a
l
s
e
 
(
i
.
e
.
 
t
h
e


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
i
s
 
c
u
r
r
e
n
t
l
y
 
i
n
a
c
c
e
s
s
i
b
l
e
)
.
 
O
t
h
e
r
w
i
s
e
,
 
a
 
@
c
 
n
u
l
l


 
 
 
 
 
 
 
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
 
o
b
j
e
c
t
 
w
i
l
l
 
b
e
 
r
e
t
u
r
n
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
c
c
e
s
s
E
r
r
o
r
'
,
 
I
V
i
r
t
u
a
l
B
o
x
E
r
r
o
r
I
n
f
o
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
a
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
a
m
e
'


 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
B
e
s
i
d
e
s
 
b
e
i
n
g
 
u
s
e
d
 
f
o
r
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
i
d
e
n
t
i
f
i
c
a
t
i
o
n
 
p
u
r
p
o
s
e
s


 
 
 
 
 
 
 
 
e
v
e
r
y
w
h
e
r
e
 
i
n
 
V
i
r
t
u
a
l
B
o
x
,
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
a
m
e
 
i
s
 
a
l
s
o
 
u
s
e
d


 
 
 
 
 
 
 
 
a
s
 
a
 
n
a
m
e
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
a
n
d
 
a
s
 
a
 
n
a
m
e
 
o
f
 
t
h
e


 
 
 
 
 
 
 
 
s
u
b
d
i
r
e
c
t
o
r
y
 
t
h
i
s
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
r
e
s
i
d
e
s
 
i
n
.
 
T
h
u
s
,
 
e
v
e
r
y
 
t
i
m
e
 
y
o
u


 
 
 
 
 
 
 
 
c
h
a
n
g
e
 
t
h
e
 
v
a
l
u
e
 
o
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
,
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
r
e
n
a
m
e
d
 
o
n
c
e
 
y
o
u
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
t
o
 
c
o
n
f
i
r
m
 
t
h
e


 
 
 
 
 
 
 
 
c
h
a
n
g
e
.
 
T
h
e
 
c
o
n
t
a
i
n
i
n
g
 
s
u
b
d
i
r
e
c
t
o
r
y
 
w
i
l
l
 
b
e
 
a
l
s
o
 
r
e
n
a
m
e
d
,
 
b
u
t


 
 
 
 
 
 
 
 
o
n
l
y
 
i
f
 
i
t
 
h
a
s
 
e
x
a
c
t
l
y
 
t
h
e
 
s
a
m
e
 
n
a
m
e
 
a
s
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e


 
 
 
 
 
 
 
 
i
t
s
e
l
f
 
p
r
i
o
r
 
t
o
 
c
h
a
n
g
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
(
f
o
r
 
b
a
c
k
w
a
r
d
 
c
o
m
p
a
t
i
b
i
l
i
t
y


 
 
 
 
 
 
 
 
w
i
t
h
 
p
r
e
v
i
o
u
s
 
A
P
I
 
r
e
l
e
a
s
e
s
)
.
 
T
h
e
 
a
b
o
v
e
 
i
m
p
l
i
e
s
 
t
h
e
 
f
o
l
l
o
w
i
n
g


 
 
 
 
 
 
 
 
l
i
m
i
t
a
t
i
o
n
s
:


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
c
h
i
n
e
 
n
a
m
e
 
c
a
n
n
o
t
 
b
e
 
e
m
p
t
y
.


 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
c
h
i
n
e
 
n
a
m
e
 
c
a
n
 
c
o
n
t
a
i
n
 
o
n
l
y
 
c
h
a
r
a
c
t
e
r
s
 
t
h
a
t
 
a
r
e
 
v
a
l
i
d


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
 
n
a
m
e
 
c
h
a
r
a
c
t
e
r
s
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
 
r
u
l
e
s
 
o
f
 
t
h
e
 
f
i
l
e


 
 
 
 
 
 
 
 
 
 
 
 
s
y
s
t
e
m
 
u
s
e
d
 
t
o
 
s
t
o
r
e
 
V
i
r
t
u
a
l
B
o
x
 
c
o
n
f
i
g
u
r
a
t
i
o
n
.


 
 
 
 
 
 
 
 
 
 
Y
o
u
 
c
a
n
n
o
t
 
h
a
v
e
 
t
w
o
 
o
r
 
m
o
r
e
 
m
a
c
h
i
n
e
s
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
n
a
m
e


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
t
h
e
y
 
u
s
e
 
t
h
e
 
s
a
m
e
 
s
u
b
d
i
r
e
c
t
o
r
y
 
f
o
r
 
s
t
o
r
i
n
g
 
t
h
e
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
s
 
f
i
l
e
s
.


 
 
 
 
 
 
 
 
 
 
Y
o
u
 
c
a
n
n
o
t
 
c
h
a
n
g
e
 
t
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
f
 
i
t
 
i
s
 
r
u
n
n
i
n
g
,


 
 
 
 
 
 
 
 
 
 
 
 
o
r
 
i
f
 
a
n
y
 
f
i
l
e
 
i
n
 
t
h
e
 
d
i
r
e
c
t
o
r
y
 
c
o
n
t
a
i
n
i
n
g
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e


 
 
 
 
 
 
 
 
 
 
 
 
i
s
 
b
e
i
n
g
 
u
s
e
d
 
b
y
 
a
n
o
t
h
e
r
 
r
u
n
n
i
n
g
 
m
a
c
h
i
n
e
 
o
r
 
b
y
 
a
n
y
 
o
t
h
e
r


 
 
 
 
 
 
 
 
 
 
 
 
p
r
o
c
e
s
s
 
i
n
 
t
h
e
 
h
o
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
 
a
t
 
a
 
t
i
m
e
 
w
h
e
n


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
i
s
 
c
a
l
l
e
d
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
I
f
 
a
n
y
 
o
f
 
t
h
e
 
a
b
o
v
e
 
l
i
m
i
t
a
t
i
o
n
s
 
a
r
e
 
h
i
t
,
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>


 
 
 
 
 
 
 
 
w
i
l
l
 
r
e
t
u
r
n
 
a
n
 
a
p
p
r
o
p
r
i
a
t
e
 
e
r
r
o
r
 
m
e
s
s
a
g
e
 
e
x
p
l
a
i
n
i
n
g
 
t
h
e
 
e
x
a
c
t


 
 
 
 
 
 
 
 
r
e
a
s
o
n
 
a
n
d
 
t
h
e
 
c
h
a
n
g
e
s
 
y
o
u
 
m
a
d
e
 
t
o
 
t
h
i
s
 
m
a
c
h
i
n
e
 
w
i
l
l
 
n
o
t
 
b
e
 
s
a
v
e
d
.




 
 
 
 
 
 
 
 
S
t
a
r
t
i
n
g
 
w
i
t
h
 
V
i
r
t
u
a
l
B
o
x
 
4
.
0
,
 
a
 
"
.
v
b
o
x
"
 
e
x
t
e
n
s
i
o
n
 
o
f
 
t
h
e
 
s
e
t
t
i
n
g
s


 
 
 
 
 
 
 
 
f
i
l
e
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
,
 
b
u
t
 
n
o
t
 
e
n
f
o
r
c
e
d
.
 
(
P
r
e
v
i
o
u
s
 
v
e
r
s
i
o
n
s
 
a
l
w
a
y
s


 
 
 
 
 
 
 
 
u
s
e
d
 
a
 
g
e
n
e
r
i
c
 
"
.
x
m
l
"
 
e
x
t
e
n
s
i
o
n
.
)


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
a
m
e
'
,
 
s
t
r
)




 
 
 
 
@
n
a
m
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
n
a
m
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
n
a
m
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
s
c
r
i
p
t
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
s
c
r
i
p
t
i
o
n
'


 
 
 
 
 
 
 
 
D
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
T
h
e
 
d
e
s
c
r
i
p
t
i
o
n
 
a
t
t
r
i
b
u
t
e
 
c
a
n
 
c
o
n
t
a
i
n
 
a
n
y
 
t
e
x
t
 
a
n
d
 
i
s


 
 
 
 
 
 
 
 
t
y
p
i
c
a
l
l
y
 
u
s
e
d
 
t
o
 
d
e
s
c
r
i
b
e
 
t
h
e
 
h
a
r
d
w
a
r
e
 
a
n
d
 
s
o
f
t
w
a
r
e


 
 
 
 
 
 
 
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
n
 
d
e
t
a
i
l
 
(
i
.
e
.
 
n
e
t
w
o
r
k


 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
s
,
 
v
e
r
s
i
o
n
s
 
o
f
 
t
h
e
 
i
n
s
t
a
l
l
e
d
 
s
o
f
t
w
a
r
e
 
a
n
d
 
s
o
 
o
n
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
s
c
r
i
p
t
i
o
n
'
,
 
s
t
r
)




 
 
 
 
@
d
e
s
c
r
i
p
t
i
o
n
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
s
c
r
i
p
t
i
o
n
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
s
c
r
i
p
t
i
o
n
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
d
_
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
i
d
'


 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
d
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
r
o
u
p
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
g
r
o
u
p
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
m
a
c
h
i
n
e
 
g
r
o
u
p
 
n
a
m
e
s
 
o
f
 
w
h
i
c
h
 
t
h
i
s
 
m
a
c
h
i
n
e
 
i
s
 
a
 
m
e
m
b
e
r
.


 
 
 
 
 
 
 
 
"
"
 
a
n
d
 
"
/
"
 
a
r
e
 
s
y
n
o
n
y
m
s
 
f
o
r
 
t
h
e
 
t
o
p
l
e
v
e
l
 
g
r
o
u
p
.
 
E
a
c
h


 
 
 
 
 
 
 
 
g
r
o
u
p
 
i
s
 
o
n
l
y
 
l
i
s
t
e
d
 
o
n
c
e
,
 
h
o
w
e
v
e
r
 
t
h
e
y
 
a
r
e
 
l
i
s
t
e
d
 
i
n
 
n
o
 
p
a
r
t
i
c
u
l
a
r


 
 
 
 
 
 
 
 
o
r
d
e
r
 
a
n
d
 
t
h
e
r
e
 
i
s
 
n
o
 
g
u
a
r
a
n
t
e
e
 
t
h
a
t
 
t
h
e
r
e
 
a
r
e
 
n
o
 
g
a
p
s
 
i
n
 
t
h
e
 
g
r
o
u
p


 
 
 
 
 
 
 
 
h
i
e
r
a
r
c
h
y
 
(
i
.
e
.
 
"
/
g
r
o
u
p
"
,


 
 
 
 
 
 
 
 
"
/
g
r
o
u
p
/
s
u
b
g
r
o
u
p
/
s
u
b
s
u
b
g
r
o
u
p
"
 
i
s
 
a
 
v
a
l
i
d
 
r
e
s
u
l
t
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
r
o
u
p
s
'
,
 
s
t
r
)




 
 
 
 
@
g
r
o
u
p
s
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
g
r
o
u
p
s
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
g
r
o
u
p
s
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
o
s
_
t
y
p
e
_
i
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
O
S
T
y
p
e
I
d
'


 
 
 
 
 
 
 
 
U
s
e
r
-
d
e
f
i
n
e
d
 
i
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
G
u
e
s
t
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
Y
o
u
 
m
a
y
 
u
s
e
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
g
e
t
G
u
e
s
t
O
S
T
y
p
e
"
/
>
 
t
o
 
o
b
t
a
i
n


 
 
 
 
 
 
 
 
a
n
 
I
G
u
e
s
t
O
S
T
y
p
e
 
o
b
j
e
c
t
 
r
e
p
r
e
s
e
n
t
i
n
g
 
d
e
t
a
i
l
s
 
a
b
o
u
t
 
t
h
e
 
g
i
v
e
n


 
 
 
 
 
 
 
 
G
u
e
s
t
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
v
a
l
u
e
 
m
a
y
 
d
i
f
f
e
r
 
f
r
o
m
 
t
h
e
 
v
a
l
u
e
 
r
e
t
u
r
n
e
d
 
b
y


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
G
u
e
s
t
:
:
O
S
T
y
p
e
I
d
"
/
>
 
i
f
 
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
a
r
e


 
 
 
 
 
 
 
 
 
 
i
n
s
t
a
l
l
e
d
 
t
o
 
t
h
e
 
g
u
e
s
t
 
O
S
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
O
S
T
y
p
e
I
d
'
,
 
s
t
r
)




 
 
 
 
@
o
s
_
t
y
p
e
_
i
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
o
s
_
t
y
p
e
_
i
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
O
S
T
y
p
e
I
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
a
r
d
w
a
r
e
_
v
e
r
s
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
h
a
r
d
w
a
r
e
V
e
r
s
i
o
n
'


 
 
 
 
 
 
 
 
H
a
r
d
w
a
r
e
 
v
e
r
s
i
o
n
 
i
d
e
n
t
i
f
i
e
r
.
 
I
n
t
e
r
n
a
l
 
u
s
e
 
o
n
l
y
 
f
o
r
 
n
o
w
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
h
a
r
d
w
a
r
e
V
e
r
s
i
o
n
'
,
 
s
t
r
)




 
 
 
 
@
h
a
r
d
w
a
r
e
_
v
e
r
s
i
o
n
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
h
a
r
d
w
a
r
e
_
v
e
r
s
i
o
n
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
h
a
r
d
w
a
r
e
V
e
r
s
i
o
n
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
a
r
d
w
a
r
e
_
u
u
i
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
h
a
r
d
w
a
r
e
U
U
I
D
'


 
 
 
 
 
 
 
 
T
h
e
 
U
U
I
D
 
p
r
e
s
e
n
t
e
d
 
t
o
 
t
h
e
 
g
u
e
s
t
 
v
i
a
 
m
e
m
o
r
y
 
t
a
b
l
e
s
,
 
h
a
r
d
w
a
r
e
 
a
n
d
 
g
u
e
s
t


 
 
 
 
 
 
 
 
p
r
o
p
e
r
t
i
e
s
.
 
F
o
r
 
m
o
s
t
 
V
M
s
 
t
h
i
s
 
i
s
 
t
h
e
 
s
a
m
e
 
a
s
 
t
h
e
 
@
a
 
i
d
,
 
b
u
t
 
f
o
r
 
V
M
s


 
 
 
 
 
 
 
 
w
h
i
c
h
 
h
a
v
e
 
b
e
e
n
 
c
l
o
n
e
d
 
o
r
 
t
e
l
e
p
o
r
t
e
d
 
i
t
 
m
a
y
 
b
e
 
t
h
e
 
s
a
m
e
 
a
s
 
t
h
e
 
s
o
u
r
c
e


 
 
 
 
 
 
 
 
V
M
.
 
T
h
e
 
l
a
t
t
e
r
 
i
s
 
b
e
c
a
u
s
e
 
t
h
e
 
g
u
e
s
t
 
s
h
o
u
l
d
n
'
t
 
n
o
t
i
c
e
 
t
h
a
t
 
i
t
 
w
a
s


 
 
 
 
 
 
 
 
c
l
o
n
e
d
 
o
r
 
t
e
l
e
p
o
r
t
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
h
a
r
d
w
a
r
e
U
U
I
D
'
,
 
s
t
r
)




 
 
 
 
@
h
a
r
d
w
a
r
e
_
u
u
i
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
h
a
r
d
w
a
r
e
_
u
u
i
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
h
a
r
d
w
a
r
e
U
U
I
D
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
p
u
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
C
P
U
C
o
u
n
t
'


 
 
 
 
 
 
 
 
N
u
m
b
e
r
 
o
f
 
v
i
r
t
u
a
l
 
C
P
U
s
 
i
n
 
t
h
e
 
V
M
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
C
P
U
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
c
p
u
_
c
o
u
n
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
c
p
u
_
c
o
u
n
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
C
P
U
C
o
u
n
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
p
u
_
h
o
t
_
p
l
u
g
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
C
P
U
H
o
t
P
l
u
g
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
V
i
r
t
u
a
l
B
o
x
 
a
l
l
o
w
s
 
C
P
U


 
 
 
 
 
 
 
 
h
o
t
p
l
u
g
g
i
n
g
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
C
P
U
H
o
t
P
l
u
g
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
c
p
u
_
h
o
t
_
p
l
u
g
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
c
p
u
_
h
o
t
_
p
l
u
g
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
C
P
U
H
o
t
P
l
u
g
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
p
u
_
e
x
e
c
u
t
i
o
n
_
c
a
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
C
P
U
E
x
e
c
u
t
i
o
n
C
a
p
'


 
 
 
 
 
 
 
 
M
e
a
n
s
 
t
o
 
l
i
m
i
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
C
P
U
 
c
y
c
l
e
s
 
a
 
g
u
e
s
t
 
c
a
n
 
u
s
e
.
 
T
h
e
 
u
n
i
t


 
 
 
 
 
 
 
 
i
s
 
p
e
r
c
e
n
t
a
g
e
 
o
f
 
h
o
s
t
 
C
P
U
 
c
y
c
l
e
s
 
p
e
r
 
s
e
c
o
n
d
.
 
T
h
e
 
v
a
l
i
d
 
r
a
n
g
e


 
 
 
 
 
 
 
 
i
s
 
1
 
-
 
1
0
0
.
 
1
0
0
 
(
t
h
e
 
d
e
f
a
u
l
t
)
 
i
m
p
l
i
e
s
 
n
o
 
l
i
m
i
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
C
P
U
E
x
e
c
u
t
i
o
n
C
a
p
'
,
 
i
n
t
)




 
 
 
 
@
c
p
u
_
e
x
e
c
u
t
i
o
n
_
c
a
p
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
c
p
u
_
e
x
e
c
u
t
i
o
n
_
c
a
p
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
C
P
U
E
x
e
c
u
t
i
o
n
C
a
p
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
e
m
o
r
y
_
s
i
z
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
e
m
o
r
y
S
i
z
e
'


 
 
 
 
 
 
 
 
S
y
s
t
e
m
 
m
e
m
o
r
y
 
s
i
z
e
 
i
n
 
m
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
e
m
o
r
y
S
i
z
e
'
,
 
i
n
t
)




 
 
 
 
@
m
e
m
o
r
y
_
s
i
z
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
m
e
m
o
r
y
_
s
i
z
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
m
e
m
o
r
y
S
i
z
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
e
m
o
r
y
_
b
a
l
l
o
o
n
_
s
i
z
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
e
m
o
r
y
B
a
l
l
o
o
n
S
i
z
e
'


 
 
 
 
 
 
 
 
M
e
m
o
r
y
 
b
a
l
l
o
o
n
 
s
i
z
e
 
i
n
 
m
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
e
m
o
r
y
B
a
l
l
o
o
n
S
i
z
e
'
,
 
i
n
t
)




 
 
 
 
@
m
e
m
o
r
y
_
b
a
l
l
o
o
n
_
s
i
z
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
m
e
m
o
r
y
_
b
a
l
l
o
o
n
_
s
i
z
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
m
e
m
o
r
y
B
a
l
l
o
o
n
S
i
z
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
a
g
e
_
f
u
s
i
o
n
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
p
a
g
e
F
u
s
i
o
n
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
V
i
r
t
u
a
l
B
o
x
 
a
l
l
o
w
s
 
p
a
g
e


 
 
 
 
 
 
 
 
f
u
s
i
o
n
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
 
(
6
4
-
b
i
t
 
h
o
s
t
s
 
o
n
l
y
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
a
g
e
F
u
s
i
o
n
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
p
a
g
e
_
f
u
s
i
o
n
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
p
a
g
e
_
f
u
s
i
o
n
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
p
a
g
e
F
u
s
i
o
n
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
r
a
p
h
i
c
s
_
c
o
n
t
r
o
l
l
e
r
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
G
r
a
p
h
i
c
s
C
o
n
t
r
o
l
l
e
r
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
g
r
a
p
h
i
c
s
C
o
n
t
r
o
l
l
e
r
T
y
p
e
'


 
 
 
 
 
 
 
 
G
r
a
p
h
i
c
s
 
c
o
n
t
r
o
l
l
e
r
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
r
a
p
h
i
c
s
C
o
n
t
r
o
l
l
e
r
T
y
p
e
'
,
 
G
r
a
p
h
i
c
s
C
o
n
t
r
o
l
l
e
r
T
y
p
e
)




 
 
 
 
@
g
r
a
p
h
i
c
s
_
c
o
n
t
r
o
l
l
e
r
_
t
y
p
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
g
r
a
p
h
i
c
s
_
c
o
n
t
r
o
l
l
e
r
_
t
y
p
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
g
r
a
p
h
i
c
s
C
o
n
t
r
o
l
l
e
r
T
y
p
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
r
a
m
_
s
i
z
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
V
R
A
M
S
i
z
e
'


 
 
 
 
 
 
 
 
V
i
d
e
o
 
m
e
m
o
r
y
 
s
i
z
e
 
i
n
 
m
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
R
A
M
S
i
z
e
'
,
 
i
n
t
)




 
 
 
 
@
v
r
a
m
_
s
i
z
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
r
a
m
_
s
i
z
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
R
A
M
S
i
z
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
c
c
e
l
e
r
a
t
e
3
_
d
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
c
c
e
l
e
r
a
t
e
3
D
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
V
i
r
t
u
a
l
B
o
x
 
a
l
l
o
w
s
 
t
h
i
s
 
m
a
c
h
i
n
e
 
t
o
 
m
a
k
e


 
 
 
 
 
 
 
 
u
s
e
 
o
f
 
t
h
e
 
3
D
 
g
r
a
p
h
i
c
s
 
s
u
p
p
o
r
t
 
a
v
a
i
l
a
b
l
e
 
o
n
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
c
c
e
l
e
r
a
t
e
3
D
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
a
c
c
e
l
e
r
a
t
e
3
_
d
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
c
c
e
l
e
r
a
t
e
3
_
d
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
c
c
e
l
e
r
a
t
e
3
D
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
c
c
e
l
e
r
a
t
e
2
_
d
_
v
i
d
e
o
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
c
c
e
l
e
r
a
t
e
2
D
V
i
d
e
o
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
V
i
r
t
u
a
l
B
o
x
 
a
l
l
o
w
s
 
t
h
i
s
 
m
a
c
h
i
n
e
 
t
o
 
m
a
k
e


 
 
 
 
 
 
 
 
u
s
e
 
o
f
 
t
h
e
 
2
D
 
v
i
d
e
o
 
a
c
c
e
l
e
r
a
t
i
o
n
 
s
u
p
p
o
r
t
 
a
v
a
i
l
a
b
l
e
 
o
n
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
c
c
e
l
e
r
a
t
e
2
D
V
i
d
e
o
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
a
c
c
e
l
e
r
a
t
e
2
_
d
_
v
i
d
e
o
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
c
c
e
l
e
r
a
t
e
2
_
d
_
v
i
d
e
o
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
c
c
e
l
e
r
a
t
e
2
D
V
i
d
e
o
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
o
n
i
t
o
r
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
o
n
i
t
o
r
C
o
u
n
t
'


 
 
 
 
 
 
 
 
N
u
m
b
e
r
 
o
f
 
v
i
r
t
u
a
l
 
m
o
n
i
t
o
r
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
O
n
l
y
 
e
f
f
e
c
t
i
v
e
 
o
n
 
W
i
n
d
o
w
s
 
X
P
 
a
n
d
 
l
a
t
e
r
 
g
u
e
s
t
s
 
w
i
t
h


 
 
 
 
 
 
 
 
 
 
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
i
n
s
t
a
l
l
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
o
n
i
t
o
r
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
m
o
n
i
t
o
r
_
c
o
u
n
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
m
o
n
i
t
o
r
_
c
o
u
n
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
m
o
n
i
t
o
r
C
o
u
n
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
V
i
d
e
o
C
a
p
t
u
r
e
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
w
h
e
t
h
e
r
 
V
i
r
t
u
a
l
B
o
x
 
u
s
e
s
 
v
i
d
e
o
 
r
e
c
o
r
d
i
n
g
 
t
o


 
 
 
 
 
 
 
 
r
e
c
o
r
d
 
V
M
 
s
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
v
i
d
e
o
_
c
a
p
t
u
r
e
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
s
c
r
e
e
n
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
V
i
d
e
o
C
a
p
t
u
r
e
S
c
r
e
e
n
s
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
f
o
r
 
w
h
i
c
h
 
s
c
r
e
e
n
s
 
v
i
d
e
o
 
r
e
c
o
r
d
i
n
g
 
i
s


 
 
 
 
 
 
 
 
e
n
a
b
l
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
S
c
r
e
e
n
s
'
,
 
b
o
o
l
)




 
 
 
 
@
v
i
d
e
o
_
c
a
p
t
u
r
e
_
s
c
r
e
e
n
s
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
s
c
r
e
e
n
s
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
S
c
r
e
e
n
s
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
f
i
l
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
V
i
d
e
o
C
a
p
t
u
r
e
F
i
l
e
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
t
h
e
 
f
i
l
e
n
a
m
e
 
V
i
r
t
u
a
l
B
o
x
 
u
s
e
s
 
t
o
 
s
a
v
e


 
 
 
 
 
 
 
 
t
h
e
 
r
e
c
o
r
d
e
d
 
c
o
n
t
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
F
i
l
e
'
,
 
s
t
r
)




 
 
 
 
@
v
i
d
e
o
_
c
a
p
t
u
r
e
_
f
i
l
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
f
i
l
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
F
i
l
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
w
i
d
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
V
i
d
e
o
C
a
p
t
u
r
e
W
i
d
t
h
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
t
h
e
 
h
o
r
i
z
o
n
t
a
l
 
r
e
s
o
l
u
t
i
o
n
 
o
f
 
t
h
e
 
r
e
c
o
r
d
e
d
 
v
i
d
e
o
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
W
i
d
t
h
'
,
 
i
n
t
)




 
 
 
 
@
v
i
d
e
o
_
c
a
p
t
u
r
e
_
w
i
d
t
h
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
w
i
d
t
h
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
W
i
d
t
h
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
h
e
i
g
h
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
V
i
d
e
o
C
a
p
t
u
r
e
H
e
i
g
h
t
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
t
h
e
 
v
e
r
t
i
c
a
l
 
r
e
s
o
l
u
t
i
o
n
 
o
f
 
t
h
e
 
r
e
c
o
r
d
e
d
 
v
i
d
e
o
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
H
e
i
g
h
t
'
,
 
i
n
t
)




 
 
 
 
@
v
i
d
e
o
_
c
a
p
t
u
r
e
_
h
e
i
g
h
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
h
e
i
g
h
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
H
e
i
g
h
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
r
a
t
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
V
i
d
e
o
C
a
p
t
u
r
e
R
a
t
e
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
t
h
e
 
b
i
t
r
a
t
e
 
i
n
 
k
i
l
o
b
i
t
s
 
p
e
r
 
s
e
c
o
n
d
.


 
 
 
 
 
 
 
 
I
n
c
r
e
a
s
i
n
g
 
t
h
i
s
 
v
a
l
u
e
 
m
a
k
e
s
 
t
h
e
 
v
i
d
e
o
 
l
o
o
k
 
b
e
t
t
e
r
 
f
o
r
 
t
h
e


 
 
 
 
 
 
 
 
c
o
s
t
 
o
f
 
a
n
 
i
n
c
r
e
a
s
e
d
 
f
i
l
e
 
s
i
z
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
R
a
t
e
'
,
 
i
n
t
)




 
 
 
 
@
v
i
d
e
o
_
c
a
p
t
u
r
e
_
r
a
t
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
r
a
t
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
R
a
t
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
f
p
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
V
i
d
e
o
C
a
p
t
u
r
e
F
p
s
'


 
 
 
 
 
 
 
 
T
h
i
s
 
s
e
t
t
i
n
g
 
d
e
t
e
r
m
i
n
e
s
 
t
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
f
r
a
m
e
s
 
p
e
r
 
s
e
c
o
n
d
.


 
 
 
 
 
 
 
 
F
r
a
m
e
s
 
w
i
t
h
 
a
 
h
i
g
h
e
r
 
f
r
e
q
u
e
n
c
y
 
w
i
l
l
 
b
e
 
s
k
i
p
p
e
d
.
 
R
e
d
u
c
i
n
g
 
t
h
i
s


 
 
 
 
 
 
 
 
v
a
l
u
e
 
i
n
c
r
e
s
e
s
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
s
k
i
p
p
e
d
 
f
r
a
m
e
s
 
b
u
t
 
r
e
d
u
c
e
s
 
t
h
e


 
 
 
 
 
 
 
 
f
i
l
e
 
s
i
z
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
F
p
s
'
,
 
i
n
t
)




 
 
 
 
@
v
i
d
e
o
_
c
a
p
t
u
r
e
_
f
p
s
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
i
d
e
o
_
c
a
p
t
u
r
e
_
f
p
s
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
i
d
e
o
C
a
p
t
u
r
e
F
p
s
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
i
o
s
_
s
e
t
t
i
n
g
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
B
I
O
S
S
e
t
t
i
n
g
s
 
v
a
l
u
e
 
f
o
r
 
'
B
I
O
S
S
e
t
t
i
n
g
s
'


 
 
 
 
 
 
 
 
O
b
j
e
c
t
 
c
o
n
t
a
i
n
i
n
g
 
a
l
l
 
B
I
O
S
 
s
e
t
t
i
n
g
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
B
I
O
S
S
e
t
t
i
n
g
s
'
,
 
I
B
I
O
S
S
e
t
t
i
n
g
s
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
i
r
m
w
a
r
e
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
F
i
r
m
w
a
r
e
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
f
i
r
m
w
a
r
e
T
y
p
e
'


 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
f
i
r
m
w
a
r
e
 
(
s
u
c
h
 
a
s
 
l
e
g
a
c
y
 
B
I
O
S
 
o
r
 
E
F
I
)
,
 
u
s
e
d
 
f
o
r
 
i
n
i
t
i
a
l


 
 
 
 
 
 
 
 
b
o
o
t
s
t
r
a
p
 
i
n
 
t
h
i
s
 
V
M
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
i
r
m
w
a
r
e
T
y
p
e
'
,
 
F
i
r
m
w
a
r
e
T
y
p
e
)




 
 
 
 
@
f
i
r
m
w
a
r
e
_
t
y
p
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
i
r
m
w
a
r
e
_
t
y
p
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
i
r
m
w
a
r
e
T
y
p
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
o
i
n
t
i
n
g
_
h
i
d
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
P
o
i
n
t
i
n
g
H
I
D
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
p
o
i
n
t
i
n
g
H
I
D
T
y
p
e
'


 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
p
o
i
n
t
i
n
g
 
H
I
D
 
(
s
u
c
h
 
a
s
 
m
o
u
s
e
 
o
r
 
t
a
b
l
e
t
)
 
u
s
e
d
 
i
n
 
t
h
i
s
 
V
M
.


 
 
 
 
 
 
 
 
T
h
e
 
d
e
f
a
u
l
t
 
i
s
 
t
y
p
i
c
a
l
l
y
 
"
P
S
2
M
o
u
s
e
"
 
b
u
t
 
c
a
n
 
v
a
r
y
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e


 
 
 
 
 
 
 
 
r
e
q
u
i
r
e
m
e
n
t
s
 
o
f
 
t
h
e
 
g
u
e
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
o
i
n
t
i
n
g
H
I
D
T
y
p
e
'
,
 
P
o
i
n
t
i
n
g
H
I
D
T
y
p
e
)




 
 
 
 
@
p
o
i
n
t
i
n
g
_
h
i
d
_
t
y
p
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
p
o
i
n
t
i
n
g
_
h
i
d
_
t
y
p
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
p
o
i
n
t
i
n
g
H
I
D
T
y
p
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
k
e
y
b
o
a
r
d
_
h
i
d
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
K
e
y
b
o
a
r
d
H
I
D
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
k
e
y
b
o
a
r
d
H
I
D
T
y
p
e
'


 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
k
e
y
b
o
a
r
d
 
H
I
D
 
u
s
e
d
 
i
n
 
t
h
i
s
 
V
M
.


 
 
 
 
 
 
 
 
T
h
e
 
d
e
f
a
u
l
t
 
i
s
 
t
y
p
i
c
a
l
l
y
 
"
P
S
2
K
e
y
b
o
a
r
d
"
 
b
u
t
 
c
a
n
 
v
a
r
y
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e


 
 
 
 
 
 
 
 
r
e
q
u
i
r
e
m
e
n
t
s
 
o
f
 
t
h
e
 
g
u
e
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
k
e
y
b
o
a
r
d
H
I
D
T
y
p
e
'
,
 
K
e
y
b
o
a
r
d
H
I
D
T
y
p
e
)




 
 
 
 
@
k
e
y
b
o
a
r
d
_
h
i
d
_
t
y
p
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
k
e
y
b
o
a
r
d
_
h
i
d
_
t
y
p
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
k
e
y
b
o
a
r
d
H
I
D
T
y
p
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
p
e
t
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
H
P
E
T
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
T
h
i
s
 
a
t
t
r
i
b
u
t
e
 
c
o
n
t
r
o
l
s
 
i
f
 
H
i
g
h
 
P
r
e
c
i
s
i
o
n
 
E
v
e
n
t
 
T
i
m
e
r
 
(
H
P
E
T
)
 
i
s


 
 
 
 
 
 
 
 
e
n
a
b
l
e
d
 
i
n
 
t
h
i
s
 
V
M
.
 
U
s
e
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
f
 
y
o
u
 
w
a
n
t
 
t
o
 
p
r
o
v
i
d
e
 
g
u
e
s
t
s


 
 
 
 
 
 
 
 
w
i
t
h
 
a
d
d
i
t
i
o
n
a
l
 
t
i
m
e
 
s
o
u
r
c
e
,
 
o
r
 
i
f
 
g
u
e
s
t
 
r
e
q
u
i
r
e
s
 
H
P
E
T
 
t
o
 
f
u
n
c
t
i
o
n
 
c
o
r
r
e
c
t
l
y
.


 
 
 
 
 
 
 
 
D
e
f
a
u
l
t
 
i
s
 
f
a
l
s
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
H
P
E
T
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
h
p
e
t
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
h
p
e
t
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
H
P
E
T
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
h
i
p
s
e
t
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
C
h
i
p
s
e
t
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
c
h
i
p
s
e
t
T
y
p
e
'


 
 
 
 
 
 
 
 
C
h
i
p
s
e
t
 
t
y
p
e
 
u
s
e
d
 
i
n
 
t
h
i
s
 
V
M
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
h
i
p
s
e
t
T
y
p
e
'
,
 
C
h
i
p
s
e
t
T
y
p
e
)




 
 
 
 
@
c
h
i
p
s
e
t
_
t
y
p
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
c
h
i
p
s
e
t
_
t
y
p
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
c
h
i
p
s
e
t
T
y
p
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
n
a
p
s
h
o
t
_
f
o
l
d
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
s
n
a
p
s
h
o
t
F
o
l
d
e
r
'


 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
d
i
r
e
c
t
o
r
y
 
u
s
e
d
 
t
o
 
s
t
o
r
e
 
s
n
a
p
s
h
o
t
 
d
a
t
a


 
 
 
 
 
 
 
 
(
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
 
a
n
d
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
s
)
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
T
h
e
 
i
n
i
t
i
a
l
 
v
a
l
u
e
 
o
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s


 
 
 
 
 
 
 
 
<
<
l
i
n
k
 
t
o
=
"
#
s
e
t
t
i
n
g
s
F
i
l
e
P
a
t
h
"
>


 
 
 
 
 
 
 
 
 
 
p
a
t
h
_
t
o
_
s
e
t
t
i
n
g
s
_
f
i
l
e
<
/
l
i
n
k
>
>
/
<


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
i
d
"
>
m
a
c
h
i
n
e
_
u
u
i
d
<
/
l
i
n
k
>


 
 
 
 
 
 
 
 
>
.




 
 
 
 
 
 
 
 
C
u
r
r
e
n
t
l
y
,
 
i
t
 
i
s
 
a
n
 
e
r
r
o
r
 
t
o
 
t
r
y
 
t
o
 
c
h
a
n
g
e
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
o
n


 
 
 
 
 
 
 
 
a
 
m
a
c
h
i
n
e
 
t
h
a
t
 
h
a
s
 
s
n
a
p
s
h
o
t
s
 
(
b
e
c
a
u
s
e
 
t
h
i
s
 
w
o
u
l
d
 
r
e
q
u
i
r
e
 
t
o


 
 
 
 
 
 
 
 
m
o
v
e
 
p
o
s
s
i
b
l
y
 
l
a
r
g
e
 
f
i
l
e
s
 
t
o
 
a
 
d
i
f
f
e
r
e
n
t
 
l
o
c
a
t
i
o
n
)
.


 
 
 
 
 
 
 
 
A
 
s
e
p
a
r
a
t
e
 
m
e
t
h
o
d
 
w
i
l
l
 
b
e
 
a
v
a
i
l
a
b
l
e
 
f
o
r
 
t
h
i
s
 
p
u
r
p
o
s
e
 
l
a
t
e
r
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
t
o
 
@
c
 
n
u
l
l
 
o
r
 
t
o
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
w
i
l
l
 
r
e
s
t
o
r
e


 
 
 
 
 
 
 
 
 
 
t
h
e
 
i
n
i
t
i
a
l
 
v
a
l
u
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
W
h
e
n
 
s
e
t
t
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
,
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
a
t
h
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
 
 
a
b
s
o
l
u
t
e
 
(
f
u
l
l
 
p
a
t
h
)
 
o
r
 
r
e
l
a
t
i
v
e
 
t
o
 
t
h
e
 
d
i
r
e
c
t
o
r
y
 
w
h
e
r
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
e
t
t
i
n
g
s
F
i
l
e
P
a
t
h
"
>
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
<
/
l
i
n
k
>


 
 
 
 
 
 
 
 
 
 
i
s
 
l
o
c
a
t
e
d
.
 
W
h
e
n
 
r
e
a
d
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
,
 
a
 
f
u
l
l
 
p
a
t
h
 
i
s


 
 
 
 
 
 
 
 
 
 
a
l
w
a
y
s
 
r
e
t
u
r
n
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
p
a
t
h
 
m
a
y
 
n
o
t
 
e
x
i
s
t
,
 
i
t
 
w
i
l
l
 
b
e
 
c
r
e
a
t
e
d


 
 
 
 
 
 
 
 
 
 
w
h
e
n
 
n
e
c
e
s
s
a
r
y
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
n
a
p
s
h
o
t
F
o
l
d
e
r
'
,
 
s
t
r
)




 
 
 
 
@
s
n
a
p
s
h
o
t
_
f
o
l
d
e
r
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
s
n
a
p
s
h
o
t
_
f
o
l
d
e
r
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
s
n
a
p
s
h
o
t
F
o
l
d
e
r
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
r
d
e
_
s
e
r
v
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
V
R
D
E
S
e
r
v
e
r
 
v
a
l
u
e
 
f
o
r
 
'
V
R
D
E
S
e
r
v
e
r
'


 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
 
R
e
m
o
t
e
 
D
e
s
k
t
o
p
 
E
x
t
e
n
s
i
o
n
 
(
V
R
D
E
)
 
s
e
r
v
e
r
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
R
D
E
S
e
r
v
e
r
'
,
 
I
V
R
D
E
S
e
r
v
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
m
u
l
a
t
e
d
_
u
s
b
_
w
e
b
c
a
m
e
r
a
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
e
m
u
l
a
t
e
d
U
S
B
W
e
b
c
a
m
e
r
a
E
n
a
b
l
e
d
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
m
u
l
a
t
e
d
U
S
B
W
e
b
c
a
m
e
r
a
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
e
m
u
l
a
t
e
d
_
u
s
b
_
w
e
b
c
a
m
e
r
a
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
e
m
u
l
a
t
e
d
_
u
s
b
_
w
e
b
c
a
m
e
r
a
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
e
m
u
l
a
t
e
d
U
S
B
W
e
b
c
a
m
e
r
a
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
m
u
l
a
t
e
d
_
u
s
b
_
c
a
r
d
_
r
e
a
d
e
r
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
e
m
u
l
a
t
e
d
U
S
B
C
a
r
d
R
e
a
d
e
r
E
n
a
b
l
e
d
'
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
m
u
l
a
t
e
d
U
S
B
C
a
r
d
R
e
a
d
e
r
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
e
m
u
l
a
t
e
d
_
u
s
b
_
c
a
r
d
_
r
e
a
d
e
r
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
e
m
u
l
a
t
e
d
_
u
s
b
_
c
a
r
d
_
r
e
a
d
e
r
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
e
m
u
l
a
t
e
d
U
S
B
C
a
r
d
R
e
a
d
e
r
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
m
e
d
i
a
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
s
'
,
 
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
s
b
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
U
S
B
C
o
n
t
r
o
l
l
e
r
 
v
a
l
u
e
 
f
o
r
 
'
U
S
B
C
o
n
t
r
o
l
l
e
r
'


 
 
 
 
 
 
 
 
A
s
s
o
c
i
a
t
e
d
 
U
S
B
 
c
o
n
t
r
o
l
l
e
r
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
U
S
B
 
f
u
n
c
t
i
o
n
a
l
i
t
y
 
i
s
 
n
o
t
 
a
v
a
i
l
a
b
l
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
e
d
i
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
s
e
t
 
t
h
e
 
r
e
s
u
l
t
 
c
o
d
e
 
t
o
 
@
c
 
E
_
N
O
T
I
M
P
L
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
U
S
B
C
o
n
t
r
o
l
l
e
r
'
,
 
I
U
S
B
C
o
n
t
r
o
l
l
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
u
d
i
o
_
a
d
a
p
t
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
A
u
d
i
o
A
d
a
p
t
e
r
 
v
a
l
u
e
 
f
o
r
 
'
a
u
d
i
o
A
d
a
p
t
e
r
'


 
 
 
 
 
 
 
 
A
s
s
o
c
i
a
t
e
d
 
a
u
d
i
o
 
a
d
a
p
t
e
r
,
 
a
l
w
a
y
s
 
p
r
e
s
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
u
d
i
o
A
d
a
p
t
e
r
'
,
 
I
A
u
d
i
o
A
d
a
p
t
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
 
v
a
l
u
e
 
f
o
r
 
'
s
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
s
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
s
'
,
 
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
e
t
t
i
n
g
s
_
f
i
l
e
_
p
a
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
s
e
t
t
i
n
g
s
F
i
l
e
P
a
t
h
'


 
 
 
 
 
 
 
 
F
u
l
l
 
n
a
m
e
 
o
f
 
t
h
e
 
f
i
l
e
 
c
o
n
t
a
i
n
i
n
g
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
d
a
t
a
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
e
t
t
i
n
g
s
F
i
l
e
P
a
t
h
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
e
t
t
i
n
g
s
_
m
o
d
i
f
i
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
s
e
t
t
i
n
g
s
M
o
d
i
f
i
e
d
'


 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
 
h
a
v
e
 
b
e
e
n
 
m
o
d
i
f
i
e
d


 
 
 
 
 
 
 
 
(
b
u
t
 
n
e
i
t
h
e
r
 
y
e
t
 
s
a
v
e
d
 
n
o
r
 
d
i
s
c
a
r
d
e
d
)
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
R
e
a
d
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
o
n
l
y
 
v
a
l
i
d
 
o
n
 
i
n
s
t
a
n
c
e
s
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
 
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>
 
a
n
d
 
o
n
 
n
e
w
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
o
r
 
o
p
e
n
e
d


 
 
 
 
 
 
 
 
 
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
a
c
h
i
n
e
"
/
>
 
b
u
t
 
n
o
t


 
 
 
 
 
 
 
 
 
 
y
e
t
 
r
e
g
i
s
t
e
r
e
d
,
 
o
r
 
o
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
 
a
f
t
e
r
 
c
a
l
l
i
n
g


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
u
n
r
e
g
i
s
t
e
r
"
/
>
.
 
F
o
r
 
a
l
l
 
o
t
h
e
r


 
 
 
 
 
 
 
 
 
 
c
a
s
e
s
,
 
t
h
e
 
s
e
t
t
i
n
g
s
 
c
a
n
 
n
e
v
e
r
 
b
e
 
m
o
d
i
f
i
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
F
o
r
 
n
e
w
l
y
 
c
r
e
a
t
e
d
 
u
n
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
,
 
t
h
e
 
v
a
l
u
e
 
o
f
 
t
h
i
s


 
 
 
 
 
 
 
 
 
 
p
r
o
p
e
r
t
y
 
i
s
 
a
l
w
a
y
s
 
@
c
 
t
r
u
e
 
u
n
t
i
l
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>


 
 
 
 
 
 
 
 
 
 
i
s
 
c
a
l
l
e
d
 
(
n
o
 
m
a
t
t
e
r
 
i
f
 
a
n
y
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
h
a
v
e
 
b
e
e
n


 
 
 
 
 
 
 
 
 
 
c
h
a
n
g
e
d
 
a
f
t
e
r
 
t
h
e
 
c
r
e
a
t
i
o
n
 
o
r
 
n
o
t
)
.
 
F
o
r
 
o
p
e
n
e
d
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 
 
 
t
h
e
 
v
a
l
u
e
 
i
s
 
s
e
t
 
t
o
 
@
c
 
f
a
l
s
e
 
(
a
n
d
 
t
h
e
n
 
f
o
l
l
o
w
s
 
t
o
 
n
o
r
m
a
l
 
r
u
l
e
s
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
e
t
t
i
n
g
s
M
o
d
i
f
i
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
e
s
s
i
o
n
_
s
t
a
t
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
S
e
s
s
i
o
n
S
t
a
t
e
 
v
a
l
u
e
 
f
o
r
 
'
s
e
s
s
i
o
n
S
t
a
t
e
'


 
 
 
 
 
 
 
 
C
u
r
r
e
n
t
 
s
e
s
s
i
o
n
 
s
t
a
t
e
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
e
s
s
i
o
n
S
t
a
t
e
'
,
 
S
e
s
s
i
o
n
S
t
a
t
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
e
s
s
i
o
n
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
s
e
s
s
i
o
n
T
y
p
e
'


 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
t
h
e
 
s
e
s
s
i
o
n
.
 
I
f
 
<
l
i
n
k
 
t
o
=
"
#
s
e
s
s
i
o
n
S
t
a
t
e
"
/
>
 
i
s


 
 
 
 
 
 
 
 
S
p
a
w
n
i
n
g
 
o
r
 
L
o
c
k
e
d
,
 
t
h
i
s
 
a
t
t
r
i
b
u
t
e
 
c
o
n
t
a
i
n
s
 
t
h
e


 
 
 
 
 
 
 
 
s
a
m
e
 
v
a
l
u
e
 
a
s
 
p
a
s
s
e
d
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
m
e
t
h
o
d
 
i
n
 
t
h
e


 
 
 
 
 
 
 
 
@
a
 
t
y
p
e
 
p
a
r
a
m
e
t
e
r
.
 
I
f
 
t
h
e
 
s
e
s
s
i
o
n
 
w
a
s
 
u
s
e
d
 
w
i
t
h


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
o
c
k
M
a
c
h
i
n
e
"
/
>
,
 
o
r
 
i
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
e
s
s
i
o
n
S
t
a
t
e
"
/
>
 
i
s
 
S
e
s
s
i
o
n
C
l
o
s
e
d
,
 
t
h
e
 
v
a
l
u
e
 
o
f
 
t
h
i
s


 
 
 
 
 
 
 
 
a
t
t
r
i
b
u
t
e
 
i
s
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
e
s
s
i
o
n
T
y
p
e
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
e
s
s
i
o
n
_
p
i
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
s
e
s
s
i
o
n
P
I
D
'


 
 
 
 
 
 
 
 
I
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
s
e
s
s
i
o
n
 
p
r
o
c
e
s
s
.
 
T
h
i
s
 
a
t
t
r
i
b
u
t
e
 
c
o
n
t
a
i
n
s
 
t
h
e


 
 
 
 
 
 
 
 
p
l
a
t
f
o
r
m
-
d
e
p
e
n
d
e
n
t
 
i
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
p
r
o
c
e
s
s
 
w
h
o
s
e
 
s
e
s
s
i
o
n
 
w
a
s


 
 
 
 
 
 
 
 
u
s
e
d
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
o
c
k
M
a
c
h
i
n
e
"
/
>
 
c
a
l
l
.
 
T
h
e
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
v
a
l
u
e
 
i
s
 
o
n
l
y
 
v
a
l
i
d
 
i
f
 
<
l
i
n
k
 
t
o
=
"
#
s
e
s
s
i
o
n
S
t
a
t
e
"
/
>
 
i
s
 
L
o
c
k
e
d
 
o
r


 
 
 
 
 
 
 
 
U
n
l
o
c
k
i
n
g
 
b
y
 
t
h
e
 
t
i
m
e
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
r
e
a
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
e
s
s
i
o
n
P
I
D
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
t
a
t
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
M
a
c
h
i
n
e
S
t
a
t
e
 
v
a
l
u
e
 
f
o
r
 
'
s
t
a
t
e
'


 
 
 
 
 
 
 
 
C
u
r
r
e
n
t
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
t
a
t
e
'
,
 
M
a
c
h
i
n
e
S
t
a
t
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
a
s
t
_
s
t
a
t
e
_
c
h
a
n
g
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
l
a
s
t
S
t
a
t
e
C
h
a
n
g
e
'


 
 
 
 
 
 
 
 
T
i
m
e
 
s
t
a
m
p
 
o
f
 
t
h
e
 
l
a
s
t
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
c
h
a
n
g
e
,


 
 
 
 
 
 
 
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
 
s
i
n
c
e
 
1
9
7
0
-
0
1
-
0
1
 
U
T
C
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
a
s
t
S
t
a
t
e
C
h
a
n
g
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
t
a
t
e
_
f
i
l
e
_
p
a
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
s
t
a
t
e
F
i
l
e
P
a
t
h
'


 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
f
i
l
e
 
t
h
a
t
 
s
t
o
r
e
s
 
t
h
e
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
o
f


 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
w
h
e
n
 
i
t
 
i
s
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
M
a
c
h
i
n
e
S
t
a
t
e
_
S
a
v
e
d
"
/
>
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
i
n
 
t
h
e
 
S
a
v
e
d
 
s
t
a
t
e
,
 
t
h
i
s
 
a
t
t
r
i
b
u
t
e
 
i
s


 
 
 
 
 
 
 
 
 
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
t
a
t
e
F
i
l
e
P
a
t
h
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
o
g
_
f
o
l
d
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
l
o
g
F
o
l
d
e
r
'


 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
f
o
l
d
e
r
 
t
h
a
t
 
s
t
o
r
e
s
 
a
 
s
e
t
 
o
f
 
r
o
t
a
t
e
d
 
l
o
g
 
f
i
l
e
s


 
 
 
 
 
 
 
 
r
e
c
o
r
d
e
d
 
d
u
r
i
n
g
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
.
 
T
h
e
 
m
o
s
t
 
r
e
c
e
n
t
 
l
o
g
 
f
i
l
e
 
i
s


 
 
 
 
 
 
 
 
n
a
m
e
d
 
V
B
o
x
.
l
o
g
,
 
t
h
e
 
p
r
e
v
i
o
u
s
 
l
o
g
 
f
i
l
e
 
i
s


 
 
 
 
 
 
 
 
n
a
m
e
d
 
V
B
o
x
.
l
o
g
.
1
 
a
n
d
 
s
o
 
o
n
 
(
u
p
 
t
o
 
V
B
o
x
.
l
o
g
.
3


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
c
u
r
r
e
n
t
 
v
e
r
s
i
o
n
)
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
o
g
F
o
l
d
e
r
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
u
r
r
e
n
t
_
s
n
a
p
s
h
o
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
S
n
a
p
s
h
o
t
 
v
a
l
u
e
 
f
o
r
 
'
c
u
r
r
e
n
t
S
n
a
p
s
h
o
t
'


 
 
 
 
 
 
 
 
C
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
.
 
T
h
i
s
 
i
s
 
@
c
 
n
u
l
l
 
i
f
 
t
h
e
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
l
y
 
h
a
s
 
n
o
 
s
n
a
p
s
h
o
t
s
.
 
I
f
 
i
t
 
i
s
 
n
o
t
 
@
c
 
n
u
l
l
,
 
t
h
e
n
 
i
t
 
w
a
s


 
 
 
 
 
 
 
 
s
e
t
 
b
y
 
o
n
e
 
o
f
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
t
a
k
e
S
n
a
p
s
h
o
t
"
/
>
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
d
e
l
e
t
e
S
n
a
p
s
h
o
t
"
/
>


 
 
 
 
 
 
 
 
o
r
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
r
e
s
t
o
r
e
S
n
a
p
s
h
o
t
"
/
>
,
 
d
e
p
e
n
d
i
n
g
 
o
n
 
w
h
i
c
h


 
 
 
 
 
 
 
 
w
a
s
 
c
a
l
l
e
d
 
l
a
s
t
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
"
/
>
 
f
o
r
 
d
e
t
a
i
l
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
u
r
r
e
n
t
S
n
a
p
s
h
o
t
'
,
 
I
S
n
a
p
s
h
o
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
n
a
p
s
h
o
t
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
s
n
a
p
s
h
o
t
C
o
u
n
t
'


 
 
 
 
 
 
 
 
N
u
m
b
e
r
 
o
f
 
s
n
a
p
s
h
o
t
s
 
t
a
k
e
n
 
o
n
 
t
h
i
s
 
m
a
c
h
i
n
e
.
 
Z
e
r
o
 
m
e
a
n
s
 
t
h
e


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
d
o
e
s
n
'
t
 
h
a
v
e
 
a
n
y
 
s
n
a
p
s
h
o
t
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
n
a
p
s
h
o
t
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
u
r
r
e
n
t
_
s
t
a
t
e
_
m
o
d
i
f
i
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
c
u
r
r
e
n
t
S
t
a
t
e
M
o
d
i
f
i
e
d
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
t
h
e
 
c
u
r
r
e
n
t
 
s
t
a
t
e
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t


 
 
 
 
 
 
 
 
i
d
e
n
t
i
c
a
l
 
t
o
 
t
h
e
 
s
t
a
t
e
 
s
t
o
r
e
d
 
i
n
 
t
h
e
 
c
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
.




 
 
 
 
 
 
 
 
T
h
e
 
c
u
r
r
e
n
t
 
s
t
a
t
e
 
i
s
 
i
d
e
n
t
i
c
a
l
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
 
o
n
l
y


 
 
 
 
 
 
 
 
d
i
r
e
c
t
l
y
 
a
f
t
e
r
 
o
n
e
 
o
f
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
c
a
l
l
s
 
a
r
e
 
m
a
d
e
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
r
e
s
t
o
r
e
S
n
a
p
s
h
o
t
"
/
>


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
t
a
k
e
S
n
a
p
s
h
o
t
"
/
>
 
(
i
s
s
u
e
d
 
o
n
 
a


 
 
 
 
 
 
 
 
 
 
 
 
"
p
o
w
e
r
e
d
 
o
f
f
"
 
o
r
 
"
s
a
v
e
d
"
 
m
a
c
h
i
n
e
,
 
f
o
r
 
w
h
i
c
h


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
e
t
t
i
n
g
s
M
o
d
i
f
i
e
d
"
/
>
 
r
e
t
u
r
n
s
 
@
c
 
f
a
l
s
e
)


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
T
h
e
 
c
u
r
r
e
n
t
 
s
t
a
t
e
 
r
e
m
a
i
n
s
 
i
d
e
n
t
i
c
a
l
 
u
n
t
i
l
 
o
n
e
 
o
f
 
t
h
e
 
f
o
l
l
o
w
i
n
g


 
 
 
 
 
 
 
 
h
a
p
p
e
n
s
:


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
a
r
e
 
c
h
a
n
g
e
d


 
 
 
 
 
 
 
 
 
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
i
s
 
d
e
l
e
t
e
d


 
 
 
 
 
 
 
 
 
 
t
h
e
 
c
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
 
i
s
 
d
e
l
e
t
e
d


 
 
 
 
 
 
 
 
 
 
a
n
 
a
t
t
e
m
p
t
 
t
o
 
e
x
e
c
u
t
e
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
m
a
d
e


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
F
o
r
 
m
a
c
h
i
n
e
s
 
t
h
a
t
 
d
o
n
'
t
 
h
a
v
e
 
s
n
a
p
s
h
o
t
s
,
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s


 
 
 
 
 
 
 
 
 
 
a
l
w
a
y
s
 
@
c
 
f
a
l
s
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
u
r
r
e
n
t
S
t
a
t
e
M
o
d
i
f
i
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
h
a
r
e
d
_
f
o
l
d
e
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
S
h
a
r
e
d
F
o
l
d
e
r
 
v
a
l
u
e
 
f
o
r
 
'
s
h
a
r
e
d
F
o
l
d
e
r
s
'


 
 
 
 
 
 
 
 
C
o
l
l
e
c
t
i
o
n
 
o
f
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
 
(
p
e
r
m
a
n
e
n
t
 
s
h
a
r
e
d


 
 
 
 
 
 
 
 
f
o
l
d
e
r
s
)
.
 
T
h
e
s
e
 
f
o
l
d
e
r
s
 
a
r
e
 
s
h
a
r
e
d
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
a
t
 
m
a
c
h
i
n
e
 
s
t
a
r
t
u
p


 
 
 
 
 
 
 
 
a
n
d
 
a
v
a
i
l
a
b
l
e
 
o
n
l
y
 
t
o
 
t
h
e
 
g
u
e
s
t
 
O
S
 
i
n
s
t
a
l
l
e
d
 
w
i
t
h
i
n
 
t
h
i
s
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
N
e
w
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
r
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
.
 
E
x
i
s
t
i
n
g
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
r
e
m
o
v
e
d
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
#
r
e
m
o
v
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
h
a
r
e
d
F
o
l
d
e
r
s
'
,
 
I
S
h
a
r
e
d
F
o
l
d
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
l
i
p
b
o
a
r
d
_
m
o
d
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
C
l
i
p
b
o
a
r
d
M
o
d
e
 
v
a
l
u
e
 
f
o
r
 
'
c
l
i
p
b
o
a
r
d
M
o
d
e
'


 
 
 
 
 
 
 
 
S
y
n
c
h
r
o
n
i
z
a
t
i
o
n
 
m
o
d
e
 
b
e
t
w
e
e
n
 
t
h
e
 
h
o
s
t
 
O
S
 
c
l
i
p
b
o
a
r
d


 
 
 
 
 
 
 
 
a
n
d
 
t
h
e
 
g
u
e
s
t
 
O
S
 
c
l
i
p
b
o
a
r
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
l
i
p
b
o
a
r
d
M
o
d
e
'
,
 
C
l
i
p
b
o
a
r
d
M
o
d
e
)




 
 
 
 
@
c
l
i
p
b
o
a
r
d
_
m
o
d
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
c
l
i
p
b
o
a
r
d
_
m
o
d
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
c
l
i
p
b
o
a
r
d
M
o
d
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
r
a
g
_
a
n
d
_
d
r
o
p
_
m
o
d
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
D
r
a
g
A
n
d
D
r
o
p
M
o
d
e
 
v
a
l
u
e
 
f
o
r
 
'
d
r
a
g
A
n
d
D
r
o
p
M
o
d
e
'


 
 
 
 
 
 
 
 
W
h
i
c
h
 
m
o
d
e
 
i
s
 
a
l
l
o
w
e
d
 
f
o
r
 
d
r
a
g
'
n
'
d
r
o
p
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
r
a
g
A
n
d
D
r
o
p
M
o
d
e
'
,
 
D
r
a
g
A
n
d
D
r
o
p
M
o
d
e
)




 
 
 
 
@
d
r
a
g
_
a
n
d
_
d
r
o
p
_
m
o
d
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
r
a
g
_
a
n
d
_
d
r
o
p
_
m
o
d
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
r
a
g
A
n
d
D
r
o
p
M
o
d
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
u
e
s
t
_
p
r
o
p
e
r
t
y
_
n
o
t
i
f
i
c
a
t
i
o
n
_
p
a
t
t
e
r
n
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
g
u
e
s
t
P
r
o
p
e
r
t
y
N
o
t
i
f
i
c
a
t
i
o
n
P
a
t
t
e
r
n
s
'


 
 
 
 
 
 
 
 
A
 
c
o
m
m
a
-
s
e
p
a
r
a
t
e
d
 
l
i
s
t
 
o
f
 
s
i
m
p
l
e
 
g
l
o
b
 
p
a
t
t
e
r
n
s
.
 
C
h
a
n
g
e
s
 
t
o
 
g
u
e
s
t


 
 
 
 
 
 
 
 
p
r
o
p
e
r
t
i
e
s
 
w
h
o
s
e
 
n
a
m
e
 
m
a
t
c
h
e
s
 
o
n
e
 
o
f
 
t
h
e
 
p
a
t
t
e
r
n
s
 
w
i
l
l
 
g
e
n
e
r
a
t
e
 
a
n


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
G
u
e
s
t
P
r
o
p
e
r
t
y
C
h
a
n
g
e
d
E
v
e
n
t
"
/
>
 
s
i
g
n
a
l
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
u
e
s
t
P
r
o
p
e
r
t
y
N
o
t
i
f
i
c
a
t
i
o
n
P
a
t
t
e
r
n
s
'
,
 
s
t
r
)




 
 
 
 
@
g
u
e
s
t
_
p
r
o
p
e
r
t
y
_
n
o
t
i
f
i
c
a
t
i
o
n
_
p
a
t
t
e
r
n
s
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
g
u
e
s
t
_
p
r
o
p
e
r
t
y
_
n
o
t
i
f
i
c
a
t
i
o
n
_
p
a
t
t
e
r
n
s
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
g
u
e
s
t
P
r
o
p
e
r
t
y
N
o
t
i
f
i
c
a
t
i
o
n
P
a
t
t
e
r
n
s
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
t
e
l
e
p
o
r
t
e
r
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
W
h
e
n
 
s
e
t
 
t
o
 
@
a
 
t
r
u
e
,
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
b
e
c
o
m
e
s
 
a
 
t
a
r
g
e
t
 
t
e
l
e
p
o
r
t
e
r


 
 
 
 
 
 
 
 
t
h
e
 
n
e
x
t
 
t
i
m
e
 
i
t
 
i
s
 
p
o
w
e
r
e
d
 
o
n
.
 
T
h
i
s
 
c
a
n
 
o
n
l
y
 
s
e
t
 
t
o
 
@
a
 
t
r
u
e
 
w
h
e
n
 
t
h
e


 
 
 
 
 
 
 
 
V
M
 
i
s
 
i
n
 
t
h
e
 
@
a
 
P
o
w
e
r
e
d
O
f
f
 
o
r
 
@
a
 
A
b
o
r
t
e
d
 
s
t
a
t
e
.




 
 
 
 
 
 
 
 
<
!
-
-
 
T
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
s
e
t
 
t
o
 
@
a
 
f
a
l
s
e
 
w
h
e
n
 
t
h
e
 
V
M
 
i
s
 
p
o
w
e
r
e
d


 
 
 
 
 
 
 
 
o
n
.
 
(
b
i
r
d
:
 
T
h
i
s
 
d
o
e
s
n
'
t
 
w
o
r
k
 
y
e
t
 
)
 
-
-
>


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
t
e
l
e
p
o
r
t
e
r
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
p
o
r
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
t
e
l
e
p
o
r
t
e
r
P
o
r
t
'


 
 
 
 
 
 
 
 
T
h
e
 
T
C
P
 
p
o
r
t
 
t
h
e
 
t
a
r
g
e
t
 
t
e
l
e
p
o
r
t
e
r
 
w
i
l
l
 
l
i
s
t
e
n
 
f
o
r
 
i
n
c
o
m
i
n
g


 
 
 
 
 
 
 
 
t
e
l
e
p
o
r
t
a
t
i
o
n
s
 
o
n
.




 
 
 
 
 
 
 
 
0
 
m
e
a
n
s
 
t
h
e
 
p
o
r
t
 
i
s
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
s
e
l
e
c
t
e
d
 
u
p
o
n
 
p
o
w
e
r
 
o
n
.
 
T
h
e
 
a
c
t
u
a
l


 
 
 
 
 
 
 
 
v
a
l
u
e
 
c
a
n
 
b
e
 
r
e
a
d
 
f
r
o
m
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
w
h
i
l
e
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
w
a
i
t
i
n
g
 
f
o
r


 
 
 
 
 
 
 
 
i
n
c
o
m
i
n
g
 
t
e
l
e
p
o
r
t
a
t
i
o
n
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
P
o
r
t
'
,
 
i
n
t
)




 
 
 
 
@
t
e
l
e
p
o
r
t
e
r
_
p
o
r
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
p
o
r
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
P
o
r
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
t
e
l
e
p
o
r
t
e
r
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
T
h
e
 
a
d
d
r
e
s
s
 
t
h
e
 
t
a
r
g
e
t
 
t
e
l
e
p
o
r
t
e
r
 
w
i
l
l
 
l
i
s
t
e
n
 
o
n
.
 
I
f
 
s
e
t
 
t
o
 
a
n
 
e
m
p
t
y


 
 
 
 
 
 
 
 
s
t
r
i
n
g
,
 
i
t
 
w
i
l
l
 
l
i
s
t
e
n
 
o
n
 
a
l
l
 
a
d
d
r
e
s
s
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
A
d
d
r
e
s
s
'
,
 
s
t
r
)




 
 
 
 
@
t
e
l
e
p
o
r
t
e
r
_
a
d
d
r
e
s
s
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
a
d
d
r
e
s
s
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
A
d
d
r
e
s
s
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
p
a
s
s
w
o
r
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
t
e
l
e
p
o
r
t
e
r
P
a
s
s
w
o
r
d
'


 
 
 
 
 
 
 
 
T
h
e
 
p
a
s
s
w
o
r
d
 
t
o
 
c
h
e
c
k
 
f
o
r
 
o
n
 
t
h
e
 
t
a
r
g
e
t
 
t
e
l
e
p
o
r
t
e
r
.
 
T
h
i
s
 
i
s
 
j
u
s
t
 
a


 
 
 
 
 
 
 
 
v
e
r
y
 
b
a
s
i
c
 
m
e
a
s
u
r
e
 
t
o
 
p
r
e
v
e
n
t
 
s
i
m
p
l
e
 
h
a
c
k
s
 
a
n
d
 
o
p
e
r
a
t
o
r
s
 
a
c
c
i
d
e
n
t
a
l
l
y


 
 
 
 
 
 
 
 
b
e
a
m
i
n
g
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
t
o
 
t
h
e
 
w
r
o
n
g
 
p
l
a
c
e
.




 
 
 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
y
o
u
 
S
E
T
 
a
 
p
l
a
i
n
 
t
e
x
t
 
p
a
s
s
w
o
r
d
 
w
h
i
l
e
 
r
e
a
d
i
n
g
 
b
a
c
k
 
a
 
H
A
S
H
E
D


 
 
 
 
 
 
 
 
p
a
s
s
w
o
r
d
.
 
S
e
t
t
i
n
g
 
a
 
h
a
s
h
e
d
 
p
a
s
s
w
o
r
d
 
i
s
 
c
u
r
r
e
n
t
l
y
 
n
o
t
 
s
u
p
p
o
r
t
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
P
a
s
s
w
o
r
d
'
,
 
s
t
r
)




 
 
 
 
@
t
e
l
e
p
o
r
t
e
r
_
p
a
s
s
w
o
r
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
e
r
_
p
a
s
s
w
o
r
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
t
e
l
e
p
o
r
t
e
r
P
a
s
s
w
o
r
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
s
t
a
t
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
F
a
u
l
t
T
o
l
e
r
a
n
c
e
S
t
a
t
e
 
v
a
l
u
e
 
f
o
r
 
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
S
t
a
t
e
'


 
 
 
 
 
 
 
 
F
a
u
l
t
 
t
o
l
e
r
a
n
c
e
 
s
t
a
t
e
;
 
d
i
s
a
b
l
e
d
,
 
s
o
u
r
c
e
 
o
r
 
t
a
r
g
e
t
.


 
 
 
 
 
 
 
 
T
h
i
s
 
p
r
o
p
e
r
t
y
 
c
a
n
 
b
e
 
c
h
a
n
g
e
d
 
a
t
 
a
n
y
 
t
i
m
e
.
 
I
f
 
y
o
u
 
c
h
a
n
g
e
 
i
t
 
f
o
r
 
a
 
r
u
n
n
i
n
g


 
 
 
 
 
 
 
 
V
M
,
 
t
h
e
n
 
t
h
e
 
f
a
u
l
t
 
t
o
l
e
r
a
n
c
e
 
a
d
d
r
e
s
s
 
a
n
d
 
p
o
r
t
 
m
u
s
t
 
b
e
 
s
e
t
 
b
e
f
o
r
e
h
a
n
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
S
t
a
t
e
'
,
 
F
a
u
l
t
T
o
l
e
r
a
n
c
e
S
t
a
t
e
)




 
 
 
 
@
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
s
t
a
t
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
s
t
a
t
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
S
t
a
t
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
p
o
r
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
P
o
r
t
'


 
 
 
 
 
 
 
 
T
h
e
 
T
C
P
 
p
o
r
t
 
t
h
e
 
f
a
u
l
t
 
t
o
l
e
r
a
n
c
e
 
s
o
u
r
c
e
 
o
r
 
t
a
r
g
e
t
 
w
i
l
l
 
u
s
e
 
f
o
r


 
 
 
 
 
 
 
 
c
o
m
m
u
n
i
c
a
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
P
o
r
t
'
,
 
i
n
t
)




 
 
 
 
@
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
p
o
r
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
p
o
r
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
P
o
r
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
T
h
e
 
a
d
d
r
e
s
s
 
t
h
e
 
f
a
u
l
t
 
t
o
l
e
r
a
n
c
e
 
s
o
u
r
c
e
 
o
r
 
t
a
r
g
e
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
A
d
d
r
e
s
s
'
,
 
s
t
r
)




 
 
 
 
@
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
a
d
d
r
e
s
s
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
a
d
d
r
e
s
s
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
A
d
d
r
e
s
s
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
p
a
s
s
w
o
r
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
P
a
s
s
w
o
r
d
'


 
 
 
 
 
 
 
 
T
h
e
 
p
a
s
s
w
o
r
d
 
t
o
 
c
h
e
c
k
 
f
o
r
 
o
n
 
t
h
e
 
s
t
a
n
d
b
y
 
V
M
.
 
T
h
i
s
 
i
s
 
j
u
s
t
 
a


 
 
 
 
 
 
 
 
v
e
r
y
 
b
a
s
i
c
 
m
e
a
s
u
r
e
 
t
o
 
p
r
e
v
e
n
t
 
s
i
m
p
l
e
 
h
a
c
k
s
 
a
n
d
 
o
p
e
r
a
t
o
r
s
 
a
c
c
i
d
e
n
t
a
l
l
y


 
 
 
 
 
 
 
 
c
h
o
o
s
i
n
g
 
t
h
e
 
w
r
o
n
g
 
s
t
a
n
d
b
y
 
V
M
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
P
a
s
s
w
o
r
d
'
,
 
s
t
r
)




 
 
 
 
@
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
p
a
s
s
w
o
r
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
p
a
s
s
w
o
r
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
P
a
s
s
w
o
r
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
s
y
n
c
_
i
n
t
e
r
v
a
l
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
S
y
n
c
I
n
t
e
r
v
a
l
'


 
 
 
 
 
 
 
 
T
h
e
 
i
n
t
e
r
v
a
l
 
i
n
 
m
s
 
u
s
e
d
 
f
o
r
 
s
y
n
c
i
n
g
 
t
h
e
 
s
t
a
t
e
 
b
e
t
w
e
e
n
 
s
o
u
r
c
e
 
a
n
d
 
t
a
r
g
e
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
S
y
n
c
I
n
t
e
r
v
a
l
'
,
 
i
n
t
)




 
 
 
 
@
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
s
y
n
c
_
i
n
t
e
r
v
a
l
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
a
u
l
t
_
t
o
l
e
r
a
n
c
e
_
s
y
n
c
_
i
n
t
e
r
v
a
l
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
a
u
l
t
T
o
l
e
r
a
n
c
e
S
y
n
c
I
n
t
e
r
v
a
l
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
t
c
_
u
s
e
_
u
t
c
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
R
T
C
U
s
e
U
T
C
'


 
 
 
 
 
 
 
 
W
h
e
n
 
s
e
t
 
t
o
 
@
a
 
t
r
u
e
,
 
t
h
e
 
R
T
C
 
d
e
v
i
c
e
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
w
i
l
l
 
r
u
n


 
 
 
 
 
 
 
 
i
n
 
U
T
C
 
t
i
m
e
,
 
o
t
h
e
r
w
i
s
e
 
i
n
 
l
o
c
a
l
 
t
i
m
e
.
 
E
s
p
e
c
i
a
l
l
y
 
U
n
i
x
 
g
u
e
s
t
s
 
p
r
e
f
e
r


 
 
 
 
 
 
 
 
t
h
e
 
t
i
m
e
 
i
n
 
U
T
C
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
R
T
C
U
s
e
U
T
C
'
,
 
b
o
o
l
)




 
 
 
 
@
r
t
c
_
u
s
e
_
u
t
c
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
r
t
c
_
u
s
e
_
u
t
c
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
R
T
C
U
s
e
U
T
C
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
o
_
c
a
c
h
e
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
I
O
C
a
c
h
e
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
W
h
e
n
 
s
e
t
 
t
o
 
@
a
 
t
r
u
e
,
 
t
h
e
 
b
u
i
l
t
i
n
 
I
/
O
 
c
a
c
h
e
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
e
n
a
b
l
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
O
C
a
c
h
e
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
i
o
_
c
a
c
h
e
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
i
o
_
c
a
c
h
e
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
I
O
C
a
c
h
e
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
o
_
c
a
c
h
e
_
s
i
z
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
I
O
C
a
c
h
e
S
i
z
e
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
s
i
z
e
 
o
f
 
t
h
e
 
I
/
O
 
c
a
c
h
e
 
i
n
 
M
B
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
O
C
a
c
h
e
S
i
z
e
'
,
 
i
n
t
)




 
 
 
 
@
i
o
_
c
a
c
h
e
_
s
i
z
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
i
o
_
c
a
c
h
e
_
s
i
z
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
I
O
C
a
c
h
e
S
i
z
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
c
i
_
d
e
v
i
c
e
_
a
s
s
i
g
n
m
e
n
t
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
P
C
I
D
e
v
i
c
e
A
t
t
a
c
h
m
e
n
t
 
v
a
l
u
e
 
f
o
r
 
'
P
C
I
D
e
v
i
c
e
A
s
s
i
g
n
m
e
n
t
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
P
C
I
 
d
e
v
i
c
e
s
 
a
s
s
i
g
n
e
d
 
t
o
 
t
h
i
s
 
m
a
c
h
i
n
e
,
 
t
o
 
g
e
t
 
l
i
s
t
 
o
f
 
a
l
l


 
 
 
 
 
 
 
 
P
C
I
 
d
e
v
i
c
e
s
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
 
u
s
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
a
t
t
a
c
h
e
d
P
C
I
D
e
v
i
c
e
s
"
/
>
 
a
t
t
r
i
b
u
t
e
,
 
a
s
 
t
h
i
s
 
a
t
t
r
i
b
u
t
e


 
 
 
 
 
 
 
 
i
s
 
i
n
t
e
n
d
e
d
 
t
o
 
l
i
s
t
 
o
n
l
y
 
d
e
v
i
c
e
s
 
a
d
d
i
t
i
o
n
a
l
 
t
o
 
w
h
a
t
 
d
e
s
c
r
i
b
e
d
 
i
n


 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
h
a
r
d
w
a
r
e
 
c
o
n
f
i
g
.
 
U
s
u
a
l
l
y
,
 
t
h
i
s
 
l
i
s
t
 
k
e
e
p
s
 
h
o
s
t
'
s
 
p
h
y
s
i
c
a
l


 
 
 
 
 
 
 
 
d
e
v
i
c
e
s
 
a
s
s
i
g
n
e
d
 
t
o
 
t
h
e
 
p
a
r
t
i
c
u
l
a
r
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
P
C
I
D
e
v
i
c
e
A
s
s
i
g
n
m
e
n
t
s
'
,
 
I
P
C
I
D
e
v
i
c
e
A
t
t
a
c
h
m
e
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
a
n
d
w
i
d
t
h
_
c
o
n
t
r
o
l
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
B
a
n
d
w
i
d
t
h
C
o
n
t
r
o
l
 
v
a
l
u
e
 
f
o
r
 
'
b
a
n
d
w
i
d
t
h
C
o
n
t
r
o
l
'


 
 
 
 
 
 
 
 
B
a
n
d
w
i
d
t
h
 
c
o
n
t
r
o
l
 
m
a
n
a
g
e
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
a
n
d
w
i
d
t
h
C
o
n
t
r
o
l
'
,
 
I
B
a
n
d
w
i
d
t
h
C
o
n
t
r
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
r
a
c
i
n
g
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
t
r
a
c
i
n
g
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
E
n
a
b
l
e
s
 
t
h
e
 
t
r
a
c
i
n
g
 
f
a
c
i
l
i
t
y
 
i
n
 
t
h
e
 
V
M
M
 
(
i
n
c
l
u
d
i
n
g
 
P
D
M
 
d
e
v
i
c
e
s
 
+


 
 
 
 
 
 
 
 
d
r
i
v
e
r
s
)
.
 
T
h
e
 
V
M
M
 
w
i
l
l
 
c
o
n
s
u
m
e
 
a
b
o
u
t
 
0
.
5
M
B
 
o
f
 
m
o
r
e
 
m
e
m
o
r
y
 
w
h
e
n


 
 
 
 
 
 
 
 
e
n
a
b
l
e
d
 
a
n
d
 
t
h
e
r
e
 
m
a
y
 
b
e
 
s
o
m
e
 
e
x
t
r
a
 
o
v
e
r
h
e
a
d
 
f
r
o
m
 
t
r
a
c
e
p
o
i
n
t
s
 
t
h
a
t
 
a
r
e


 
 
 
 
 
 
 
 
a
l
w
a
y
s
 
e
n
a
b
l
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
r
a
c
i
n
g
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
t
r
a
c
i
n
g
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
t
r
a
c
i
n
g
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
t
r
a
c
i
n
g
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
t
r
a
c
i
n
g
_
c
o
n
f
i
g
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
t
r
a
c
i
n
g
C
o
n
f
i
g
'


 
 
 
 
 
 
 
 
T
r
a
c
e
p
o
i
n
t
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
t
o
 
a
p
p
l
y
 
a
t
 
s
t
a
r
t
u
p
 
w
h
e
n


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
t
r
a
c
i
n
g
E
n
a
b
l
e
d
"
/
>
 
i
s
 
t
r
u
e
.
 
T
h
e
 
s
t
r
i
n
g
 
s
p
e
c
i
f
i
e
s


 
 
 
 
 
 
 
 
a
 
s
p
a
c
e
 
s
e
p
a
r
a
t
e
d
 
o
f
 
t
r
a
c
e
p
o
i
n
t
 
g
r
o
u
p
 
n
a
m
e
s
 
t
o
 
e
n
a
b
l
e
.
 
T
h
e
 
s
p
e
c
i
a
l


 
 
 
 
 
 
 
 
g
r
o
u
p
 
'
a
l
l
'
 
e
n
a
b
l
e
s
 
a
l
l
 
t
r
a
c
e
p
o
i
n
t
s
.
 
C
h
e
c
k
 
D
B
G
F
R
3
T
r
a
c
i
n
g
C
o
n
f
i
g
 
f
o
r


 
 
 
 
 
 
 
 
m
o
r
e
 
d
e
t
a
i
l
s
 
o
n
 
a
v
a
i
l
a
b
l
e
 
t
r
a
c
e
p
o
i
n
t
 
g
r
o
u
p
s
 
a
n
d
 
s
u
c
h
.




 
 
 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
o
n
 
h
o
s
t
s
 
s
u
p
p
o
r
t
i
n
g
 
D
T
r
a
c
e
 
(
o
r
 
s
i
m
i
l
a
r
)
,
 
a
 
l
o
t
 
o
f
 
t
h
e


 
 
 
 
 
 
 
 
t
r
a
c
e
p
o
i
n
t
s
 
m
a
y
 
b
e
 
i
m
p
l
e
m
e
n
t
e
d
 
e
x
c
l
u
s
i
v
l
y
 
a
s
 
D
T
r
a
c
e
 
p
r
o
b
e
s
.
 
S
o
,
 
t
h
e


 
 
 
 
 
 
 
 
e
f
f
e
c
t
 
o
f
 
t
h
e
 
s
a
m
e
 
c
o
n
f
i
g
 
m
a
y
 
d
i
f
f
e
r
 
b
e
t
w
e
e
n
 
S
o
l
a
r
i
s
 
a
n
d
 
W
i
n
d
o
w
s
 
f
o
r


 
 
 
 
 
 
 
 
e
x
a
m
p
l
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
t
r
a
c
i
n
g
C
o
n
f
i
g
'
,
 
s
t
r
)




 
 
 
 
@
t
r
a
c
i
n
g
_
c
o
n
f
i
g
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
t
r
a
c
i
n
g
_
c
o
n
f
i
g
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
t
r
a
c
i
n
g
C
o
n
f
i
g
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
l
l
o
w
_
t
r
a
c
i
n
g
_
t
o
_
a
c
c
e
s
s
_
v
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
l
l
o
w
T
r
a
c
i
n
g
T
o
A
c
c
e
s
s
V
M
'


 
 
 
 
 
 
 
 
E
n
a
b
l
e
s
 
t
r
a
c
e
p
o
i
n
t
s
 
i
n
 
P
D
M
 
d
e
v
i
c
e
s
 
a
n
d
 
d
r
i
v
e
r
s
 
t
o
 
u
s
e
 
t
h
e
 
V
M
C
P
U
 
o
r
 
V
M


 
 
 
 
 
 
 
 
s
t
r
u
c
t
u
r
e
s
 
w
h
e
n
 
f
i
r
i
n
g
 
o
f
f
 
t
r
a
c
e
 
p
o
i
n
t
s
.
 
T
h
i
s
 
i
s
 
e
s
p
e
c
i
a
l
l
y
 
u
s
e
f
u
l


 
 
 
 
 
 
 
 
w
i
t
h
 
D
T
r
a
c
e
 
t
r
a
c
e
p
o
i
n
t
s
,
 
a
s
 
i
t
 
a
l
l
o
w
s
 
y
o
u
 
t
o
 
u
s
e
 
t
h
e
 
V
M
C
P
U
 
o
r
 
V
M


 
 
 
 
 
 
 
 
p
o
i
n
t
e
r
 
t
o
 
o
b
t
a
i
n
 
u
s
e
f
u
l
 
i
n
f
o
r
m
a
t
i
o
n
 
s
u
c
h
 
a
s
 
g
u
e
s
t
 
r
e
g
i
s
t
e
r
 
s
t
a
t
e
.




 
 
 
 
 
 
 
 
T
h
i
s
 
i
s
 
d
i
s
a
b
l
e
d
 
b
y
 
d
e
f
a
u
l
t
 
b
e
c
a
u
s
e
 
d
e
v
i
c
e
s
 
a
n
d
 
d
r
i
v
e
r
s
 
n
o
r
m
a
l
l
y
 
h
a
s
 
n
o


 
 
 
 
 
 
 
 
b
u
s
i
n
e
s
s
 
a
c
c
e
s
s
i
n
g
 
t
h
e
 
V
M
C
P
U
 
o
r
 
V
M
 
s
t
r
u
c
t
u
r
e
s
,
 
a
n
d
 
a
r
e
 
t
h
e
r
e
f
o
r
e
 
u
n
a
b
l
e


 
 
 
 
 
 
 
 
t
o
 
g
e
t
 
a
n
y
 
p
o
i
n
t
e
r
s
 
t
o
 
t
h
e
s
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
l
l
o
w
T
r
a
c
i
n
g
T
o
A
c
c
e
s
s
V
M
'
,
 
b
o
o
l
)




 
 
 
 
@
a
l
l
o
w
_
t
r
a
c
i
n
g
_
t
o
_
a
c
c
e
s
s
_
v
m
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
l
l
o
w
_
t
r
a
c
i
n
g
_
t
o
_
a
c
c
e
s
s
_
v
m
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
l
l
o
w
T
r
a
c
i
n
g
T
o
A
c
c
e
s
s
V
M
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
u
t
o
s
t
a
r
t
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
u
t
o
s
t
a
r
t
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
E
n
a
b
l
e
s
 
a
u
t
o
s
t
a
r
t
 
o
f
 
t
h
e
 
V
M
 
d
u
r
i
n
g
 
s
y
s
t
e
m
 
b
o
o
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
a
r
t
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
a
u
t
o
s
t
a
r
t
_
e
n
a
b
l
e
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
u
t
o
s
t
a
r
t
_
e
n
a
b
l
e
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
a
r
t
E
n
a
b
l
e
d
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
u
t
o
s
t
a
r
t
_
d
e
l
a
y
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
a
u
t
o
s
t
a
r
t
D
e
l
a
y
'


 
 
 
 
 
 
 
 
N
u
m
b
e
r
 
o
f
 
s
e
c
o
n
d
s
 
t
o
 
w
a
i
t
 
u
n
t
i
l
 
t
h
e
 
V
M
 
s
h
o
u
l
d
 
b
e
 
s
t
a
r
t
e
d
 
d
u
r
i
n
g
 
s
y
s
t
e
m
 
b
o
o
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
a
r
t
D
e
l
a
y
'
,
 
i
n
t
)




 
 
 
 
@
a
u
t
o
s
t
a
r
t
_
d
e
l
a
y
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
u
t
o
s
t
a
r
t
_
d
e
l
a
y
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
a
r
t
D
e
l
a
y
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
u
t
o
s
t
o
p
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
A
u
t
o
s
t
o
p
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
a
u
t
o
s
t
o
p
T
y
p
e
'


 
 
 
 
 
 
 
 
A
c
t
i
o
n
 
t
y
p
e
 
t
o
 
d
o
 
w
h
e
n
 
t
h
e
 
s
y
s
t
e
m
 
i
s
 
s
h
u
t
t
i
n
g
 
d
o
w
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
o
p
T
y
p
e
'
,
 
A
u
t
o
s
t
o
p
T
y
p
e
)




 
 
 
 
@
a
u
t
o
s
t
o
p
_
t
y
p
e
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
u
t
o
s
t
o
p
_
t
y
p
e
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
o
p
T
y
p
e
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
f
r
o
n
t
e
n
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
'


 
 
 
 
 
 
 
 
S
e
l
e
c
t
s
 
w
h
i
c
h
 
V
M
 
f
r
o
n
t
e
n
d
 
s
h
o
u
l
d
 
b
e
 
u
s
e
d
 
b
y
 
d
e
f
a
u
l
t
 
w
h
e
n
 
l
a
u
n
c
h
i
n
g


 
 
 
 
 
 
 
 
t
h
i
s
 
V
M
 
t
h
r
o
u
g
h
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
m
e
t
h
o
d
.


 
 
 
 
 
 
 
 
E
m
p
t
y
 
o
r
 
@
c
 
n
u
l
l
 
s
t
r
i
n
g
s
 
d
o
 
n
o
t
 
d
e
f
i
n
e
 
a
 
p
a
r
t
i
c
u
l
a
r
 
d
e
f
a
u
l
t
,
 
i
t
 
i
s
 
u
p


 
 
 
 
 
 
 
 
t
o
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
t
o
 
s
e
l
e
c
t
 
o
n
e
.
 
S
e
e
 
t
h
e


 
 
 
 
 
 
 
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
 
f
o
r
 
t
h
e
 
v
a
l
i
d


 
 
 
 
 
 
 
 
f
r
o
n
t
e
n
d
 
t
y
p
e
s
.




 
 
 
 
 
 
 
 
T
h
i
s
 
p
e
r
-
V
M
 
s
e
t
t
i
n
g
 
o
v
e
r
r
i
d
e
s
 
t
h
e
 
d
e
f
a
u
l
t
 
d
e
f
i
n
e
d
 
b
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
"
/
>
 
a
t
t
r
i
b
u
t
e
,
 
a
n
d
 
i
s


 
 
 
 
 
 
 
 
o
v
e
r
r
i
d
d
e
n
 
b
y
 
a
 
f
r
o
n
t
e
n
d
 
t
y
p
e
 
p
a
s
s
e
d
 
t
o


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
'
,
 
s
t
r
)




 
 
 
 
@
d
e
f
a
u
l
t
_
f
r
o
n
t
e
n
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
f
r
o
n
t
e
n
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
'
,
 
v
a
l
u
e
)




 
 
 
 
d
e
f
 
l
o
c
k
_
m
a
c
h
i
n
e
(
s
e
l
f
,
 
s
e
s
s
i
o
n
,
 
l
o
c
k
_
t
y
p
e
)
:


 
 
 
 
 
 
 
 
"
"
"
L
o
c
k
s
 
t
h
e
 
m
a
c
h
i
n
e
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
e
s
s
i
o
n
 
t
o
 
e
n
a
b
l
e
 
t
h
e
 
c
a
l
l
e
r


 
 
 
 
 
 
 
 
t
o
 
m
a
k
e
 
c
h
a
n
g
e
s
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
 
o
r
 
s
t
a
r
t
 
t
h
e
 
V
M
 
o
r
 
c
o
n
t
r
o
l


 
 
 
 
 
 
 
 
V
M
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
 
 
T
h
e
r
e
 
a
r
e
 
t
w
o
 
w
a
y
s
 
t
o
 
l
o
c
k
 
a
 
m
a
c
h
i
n
e
 
f
o
r
 
s
u
c
h
 
u
s
e
s
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
y
o
u
 
w
a
n
t
 
t
o
 
m
a
k
e
 
c
h
a
n
g
e
s
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
,


 
 
 
 
 
 
 
 
 
 
 
 
y
o
u
 
m
u
s
t
 
o
b
t
a
i
n
 
a
n
 
e
x
c
l
u
s
i
v
e
 
w
r
i
t
e
 
l
o
c
k
 
o
n
 
t
h
e
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
b
y
 
s
e
t
t
i
n
g
 
@
a
 
l
o
c
k
T
y
p
e
 
t
o
 
@
c
 
W
r
i
t
e
.




 
 
 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
w
i
l
l
 
o
n
l
y
 
s
u
c
c
e
e
d
 
i
f
 
n
o
 
o
t
h
e
r
 
p
r
o
c
e
s
s
 
h
a
s
 
l
o
c
k
e
d


 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
t
o
 
p
r
e
v
e
n
t
 
c
o
n
f
l
i
c
t
i
n
g
 
c
h
a
n
g
e
s
.
 
O
n
l
y
 
a
f
t
e
r


 
 
 
 
 
 
 
 
 
 
 
 
a
n
 
e
x
c
l
u
s
i
v
e
 
w
r
i
t
e
 
l
o
c
k
 
h
a
s
 
b
e
e
n
 
o
b
t
a
i
n
e
d
 
u
s
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
,
 
o
n
e


 
 
 
 
 
 
 
 
 
 
 
 
c
a
n
 
c
h
a
n
g
e
 
a
l
l
 
V
M
 
s
e
t
t
i
n
g
s
 
o
r
 
e
x
e
c
u
t
e
 
t
h
e
 
V
M
 
i
n
 
t
h
e
 
p
r
o
c
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
s
p
a
c
e
 
o
f
 
t
h
e
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
.
 
(
N
o
t
e
 
t
h
a
t
 
t
h
e
 
l
a
t
t
e
r
 
i
s
 
o
n
l
y
 
o
f


 
 
 
 
 
 
 
 
 
 
 
 
i
n
t
e
r
e
s
t
 
i
f
 
y
o
u
 
a
c
t
u
a
l
l
y
 
w
a
n
t
 
t
o
 
w
r
i
t
e
 
a
 
n
e
w
 
f
r
o
n
t
-
e
n
d
 
f
o
r


 
 
 
 
 
 
 
 
 
 
 
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
;
 
b
u
t
 
t
h
i
s
 
A
P
I
 
g
e
t
s
 
c
a
l
l
e
d
 
i
n
t
e
r
n
a
l
l
y
 
b
y


 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
e
x
i
s
t
i
n
g
 
f
r
o
n
t
-
e
n
d
s
 
s
u
c
h
 
a
s
 
V
B
o
x
H
e
a
d
l
e
s
s
 
a
n
d
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
 
 
 
 
G
U
I
 
t
o
 
a
c
q
u
i
r
e
 
a
 
w
r
i
t
e
 
l
o
c
k
 
o
n
 
t
h
e
 
m
a
c
h
i
n
e
 
t
h
a
t
 
t
h
e
y
 
a
r
e
 
r
u
n
n
i
n
g
.
)




 
 
 
 
 
 
 
 
 
 
 
 
O
n
 
s
u
c
c
e
s
s
,
 
w
r
i
t
e
-
l
o
c
k
i
n
g
 
t
h
e
 
m
a
c
h
i
n
e
 
f
o
r
 
a
 
s
e
s
s
i
o
n
 
c
r
e
a
t
e
s


 
 
 
 
 
 
 
 
 
 
 
 
a
 
s
e
c
o
n
d
 
c
o
p
y
 
o
f
 
t
h
e
 
I
M
a
c
h
i
n
e
 
o
b
j
e
c
t
.
 
I
t
 
i
s
 
t
h
i
s
 
s
e
c
o
n
d
 
o
b
j
e
c
t


 
 
 
 
 
 
 
 
 
 
 
 
u
p
o
n
 
w
h
i
c
h
 
c
h
a
n
g
e
s
 
c
a
n
 
b
e
 
m
a
d
e
;
 
i
n
 
V
i
r
t
u
a
l
B
o
x
 
t
e
r
m
i
n
o
l
o
g
y
,
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
s
e
c
o
n
d
 
c
o
p
y
 
i
s
 
"
m
u
t
a
b
l
e
"
.
 
I
t
 
i
s
 
o
n
l
y
 
t
h
i
s
 
s
e
c
o
n
d
,
 
m
u
t
a
b
l
e
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
o
b
j
e
c
t
 
u
p
o
n
 
w
h
i
c
h
 
y
o
u
 
c
a
n
 
c
a
l
l
 
m
e
t
h
o
d
s
 
t
h
a
t
 
c
h
a
n
g
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.
 
A
f
t
e
r
 
h
a
v
i
n
g
 
c
a
l
l
e
d
 
t
h
i
s
 
m
e
t
h
o
d
,
 
y
o
u
 
c
a
n


 
 
 
 
 
 
 
 
 
 
 
 
o
b
t
a
i
n
 
t
h
i
s
 
s
e
c
o
n
d
,
 
m
u
t
a
b
l
e
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
 
u
s
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
y
o
u
 
o
n
l
y
 
w
a
n
t
 
t
o
 
c
h
e
c
k
 
t
h
e
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
o
r
 
c
o
n
t
r
o
l


 
 
 
 
 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
 
w
i
t
h
o
u
t
 
a
c
t
u
a
l
l
y
 
c
h
a
n
g
i
n
g
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
s
 
(
e
.
g
.
 
t
o
 
g
e
t
 
a
c
c
e
s
s
 
t
o
 
V
M
 
s
t
a
t
i
s
t
i
c
s
 
o
r
 
t
a
k
e


 
 
 
 
 
 
 
 
 
 
 
 
a
 
s
n
a
p
s
h
o
t
 
o
r
 
s
a
v
e
 
t
h
e
 
m
a
c
h
i
n
e
 
s
t
a
t
e
)
,
 
t
h
e
n
 
s
e
t
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
l
o
c
k
T
y
p
e
 
a
r
g
u
m
e
n
t
 
t
o
 
@
c
 
S
h
a
r
e
d
.




 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
n
o
 
o
t
h
e
r
 
s
e
s
s
i
o
n
 
h
a
s
 
o
b
t
a
i
n
e
d
 
a
 
l
o
c
k
,
 
y
o
u
 
w
i
l
l
 
o
b
t
a
i
n
 
a
n


 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
l
u
s
i
v
e
 
w
r
i
t
e
 
l
o
c
k
 
a
s
 
d
e
s
c
r
i
b
e
d
 
a
b
o
v
e
.
 
H
o
w
e
v
e
r
,
 
i
f
 
a
n
o
t
h
e
r


 
 
 
 
 
 
 
 
 
 
 
 
s
e
s
s
i
o
n
 
h
a
s
 
a
l
r
e
a
d
y
 
o
b
t
a
i
n
e
d
 
s
u
c
h
 
a
 
l
o
c
k
,
 
t
h
e
n
 
a
 
l
i
n
k
 
t
o
 
t
h
a
t


 
 
 
 
 
 
 
 
 
 
 
 
e
x
i
s
t
i
n
g
 
s
e
s
s
i
o
n
 
w
i
l
l
 
b
e
 
e
s
t
a
b
l
i
s
h
e
d
 
w
h
i
c
h
 
a
l
l
o
w
s
 
y
o
u


 
 
 
 
 
 
 
 
 
 
 
 
t
o
 
c
o
n
t
r
o
l
 
t
h
a
t
 
e
x
i
s
t
i
n
g
 
s
e
s
s
i
o
n
.




 
 
 
 
 
 
 
 
 
 
 
 
T
o
 
f
i
n
d
 
o
u
t
 
w
h
i
c
h
 
t
y
p
e
 
o
f
 
l
o
c
k
 
w
a
s
 
o
b
t
a
i
n
e
d
,
 
y
o
u
 
c
a
n


 
 
 
 
 
 
 
 
 
 
 
 
i
n
s
p
e
c
t
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
t
y
p
e
"
/
>
,
 
w
h
i
c
h
 
w
i
l
l
 
h
a
v
e
 
b
e
e
n


 
 
 
 
 
 
 
 
 
 
 
 
s
e
t
 
t
o
 
e
i
t
h
e
r
 
@
c
 
W
r
i
t
e
L
o
c
k
 
o
r
 
@
c
 
S
h
a
r
e
d
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
I
n
 
e
i
t
h
e
r
 
c
a
s
e
,
 
y
o
u
 
c
a
n
 
g
e
t
 
a
c
c
e
s
s
 
t
o
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
"
/
>


 
 
 
 
 
 
 
 
o
b
j
e
c
t
 
w
h
i
c
h
 
c
o
n
t
r
o
l
s
 
V
M
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
 
 
A
l
s
o
 
i
n
 
a
l
l
 
o
f
 
t
h
e
 
a
b
o
v
e
 
c
a
s
e
s
,
 
o
n
e
 
m
u
s
t
 
a
l
w
a
y
s
 
c
a
l
l


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
u
n
l
o
c
k
M
a
c
h
i
n
e
"
/
>
 
t
o
 
r
e
l
e
a
s
e
 
t
h
e
 
l
o
c
k
 
o
n
 
t
h
e
 
m
a
c
h
i
n
e
,
 
o
r


 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
s
t
a
t
e
 
w
i
l
l
 
e
v
e
n
t
u
a
l
l
y
 
b
e
 
s
e
t
 
t
o
 
"
A
b
o
r
t
e
d
"
.




 
 
 
 
 
 
 
 
T
o
 
c
h
a
n
g
e
 
s
e
t
t
i
n
g
s
 
o
n
 
a
 
m
a
c
h
i
n
e
,
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
e
q
u
e
n
c
e
 
i
s
 
t
y
p
i
c
a
l
l
y


 
 
 
 
 
 
 
 
p
e
r
f
o
r
m
e
d
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
C
a
l
l
 
t
h
i
s
 
m
e
t
h
o
d
 
t
o
 
o
b
t
a
i
n
 
a
n
 
e
x
c
l
u
s
i
v
e
 
w
r
i
t
e
 
l
o
c
k
 
f
o
r
 
t
h
e
 
c
u
r
r
e
n
t
 
s
e
s
s
i
o
n
.




 
 
 
 
 
 
 
 
 
 
O
b
t
a
i
n
 
a
 
m
u
t
a
b
l
e
 
I
M
a
c
h
i
n
e
 
o
b
j
e
c
t
 
f
r
o
m
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>
.




 
 
 
 
 
 
 
 
 
 
C
h
a
n
g
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
b
y
 
i
n
v
o
k
i
n
g
 
I
M
a
c
h
i
n
e
 
m
e
t
h
o
d
s
.




 
 
 
 
 
 
 
 
 
 
C
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
.




 
 
 
 
 
 
 
 
 
 
R
e
l
e
a
s
e
 
t
h
e
 
w
r
i
t
e
 
l
o
c
k
 
b
y
 
c
a
l
l
i
n
g
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
u
n
l
o
c
k
M
a
c
h
i
n
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
s
e
s
s
i
o
n
 
o
f
 
t
y
p
e
 
I
S
e
s
s
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
S
e
s
s
i
o
n
 
o
b
j
e
c
t
 
f
o
r
 
w
h
i
c
h
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
b
e
 
l
o
c
k
e
d
.




 
 
 
 
 
 
 
 
i
n
 
l
o
c
k
_
t
y
p
e
 
o
f
 
t
y
p
e
 
L
o
c
k
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
s
e
t
 
t
o
 
@
c
 
W
r
i
t
e
,
 
t
h
e
n
 
a
t
t
e
m
p
t
 
t
o
 
a
c
q
u
i
r
e
 
a
n
 
e
x
c
l
u
s
i
v
e
 
w
r
i
t
e
 
l
o
c
k
 
o
r
 
f
a
i
l
.


 
 
 
 
 
 
 
 
 
 
I
f
 
s
e
t
 
t
o
 
@
c
 
S
h
a
r
e
d
,
 
t
h
e
n
 
e
i
t
h
e
r
 
a
c
q
u
i
r
e
 
a
n
 
e
x
c
l
u
s
i
v
e
 
w
r
i
t
e
 
l
o
c
k
 
o
r
 
e
s
t
a
b
l
i
s
h


 
 
 
 
 
 
 
 
 
 
a
 
l
i
n
k
 
t
o
 
a
n
 
e
x
i
s
t
i
n
g
 
s
e
s
s
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
U
N
E
X
P
E
C
T
E
D


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
r
e
g
i
s
t
e
r
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
A
C
C
E
S
S
D
E
N
I
E
D


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
c
e
s
s
 
n
o
t
 
s
t
a
r
t
e
d
 
b
y
 
O
p
e
n
R
e
m
o
t
e
S
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
S
e
s
s
i
o
n
 
a
l
r
e
a
d
y
 
o
p
e
n
 
o
r
 
b
e
i
n
g
 
o
p
e
n
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
V
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
F
a
i
l
e
d
 
t
o
 
a
s
s
i
g
n
 
m
a
c
h
i
n
e
 
t
o
 
s
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
l
o
c
k
M
a
c
h
i
n
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
e
s
s
i
o
n
,
 
l
o
c
k
_
t
y
p
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
l
a
u
n
c
h
_
v
m
_
p
r
o
c
e
s
s
(
s
e
l
f
,
 
s
e
s
s
i
o
n
,
 
t
y
p
e
_
p
,
 
e
n
v
i
r
o
n
m
e
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
S
p
a
w
n
s
 
a
 
n
e
w
 
p
r
o
c
e
s
s
 
t
h
a
t
 
w
i
l
l
 
e
x
e
c
u
t
e
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
a
n
d
 
o
b
t
a
i
n
s
 
a
 
s
h
a
r
e
d


 
 
 
 
 
 
 
 
l
o
c
k
 
o
n
 
t
h
e
 
m
a
c
h
i
n
e
 
f
o
r
 
t
h
e
 
c
a
l
l
i
n
g
 
s
e
s
s
i
o
n
.




 
 
 
 
 
 
 
 
I
f
 
l
a
u
n
c
h
i
n
g
 
t
h
e
 
V
M
 
s
u
c
c
e
e
d
s
,
 
t
h
e
 
n
e
w
 
V
M
 
p
r
o
c
e
s
s
 
w
i
l
l
 
c
r
e
a
t
e
 
i
t
s
 
o
w
n
 
s
e
s
s
i
o
n


 
 
 
 
 
 
 
 
a
n
d
 
w
r
i
t
e
-
l
o
c
k
 
t
h
e
 
m
a
c
h
i
n
e
 
f
o
r
 
i
t
,
 
p
r
e
v
e
n
t
i
n
g
 
c
o
n
f
l
i
c
t
i
n
g
 
c
h
a
n
g
e
s
 
f
r
o
m
 
o
t
h
e
r


 
 
 
 
 
 
 
 
p
r
o
c
e
s
s
e
s
.
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
a
l
r
e
a
d
y
 
l
o
c
k
e
d
 
(
b
e
c
a
u
s
e
 
i
t
 
i
s
 
a
l
r
e
a
d
y
 
r
u
n
n
i
n
g
 
o
r


 
 
 
 
 
 
 
 
b
e
c
a
u
s
e
 
a
n
o
t
h
e
r
 
s
e
s
s
i
o
n
 
h
a
s
 
a
 
w
r
i
t
e
 
l
o
c
k
)
,
 
l
a
u
n
c
h
i
n
g
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
w
i
l
l
 
t
h
e
r
e
f
o
r
e


 
 
 
 
 
 
 
 
f
a
i
l
.
 
R
e
v
e
r
s
e
l
y
,
 
f
u
t
u
r
e
 
a
t
t
e
m
p
t
s
 
t
o
 
o
b
t
a
i
n
 
a
 
w
r
i
t
e
 
l
o
c
k
 
w
i
l
l
 
a
l
s
o
 
f
a
i
l
 
w
h
i
l
e
 
t
h
e


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
i
s
 
r
u
n
n
i
n
g
.




 
 
 
 
 
 
 
 
T
h
e
 
c
a
l
l
e
r
'
s
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
 
r
e
m
a
i
n
s
 
s
e
p
a
r
a
t
e
 
f
r
o
m
 
t
h
e
 
s
e
s
s
i
o
n
 
o
p
e
n
e
d
 
b
y
 
t
h
e
 
n
e
w


 
 
 
 
 
 
 
 
V
M
 
p
r
o
c
e
s
s
.
 
I
t
 
r
e
c
e
i
v
e
s
 
i
t
s
 
o
w
n
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
"
/
>
 
o
b
j
e
c
t
 
w
h
i
c
h
 
c
a
n
 
b
e
 
u
s
e
d


 
 
 
 
 
 
 
 
t
o
 
c
o
n
t
r
o
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
,
 
b
u
t
 
i
t
 
c
a
n
n
o
t
 
b
e
 
u
s
e
d
 
t
o
 
c
h
a
n
g
e
 
a
l
l
 
V
M
 
s
e
t
t
i
n
g
s


 
 
 
 
 
 
 
 
w
h
i
c
h
 
w
o
u
l
d
 
b
e
 
a
v
a
i
l
a
b
l
e
 
a
f
t
e
r
 
a
 
<
l
i
n
k
 
t
o
=
"
#
l
o
c
k
M
a
c
h
i
n
e
"
/
>
 
c
a
l
l
.




 
 
 
 
 
 
 
 
T
h
e
 
c
a
l
l
e
r
 
m
u
s
t
 
e
v
e
n
t
u
a
l
l
y
 
r
e
l
e
a
s
e
 
t
h
e
 
s
e
s
s
i
o
n
'
s
 
s
h
a
r
e
d
 
l
o
c
k
 
b
y
 
c
a
l
l
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
u
n
l
o
c
k
M
a
c
h
i
n
e
"
/
>
 
o
n
 
t
h
e
 
l
o
c
a
l
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
 
o
n
c
e
 
t
h
i
s
 
c
a
l
l


 
 
 
 
 
 
 
 
h
a
s
 
r
e
t
u
r
n
e
d
.
 
H
o
w
e
v
e
r
,
 
t
h
e
 
s
e
s
s
i
o
n
'
s
 
s
t
a
t
e
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
s
t
a
t
e
"
/
>
)


 
 
 
 
 
 
 
 
w
i
l
l
 
n
o
t
 
r
e
t
u
r
n
 
t
o
 
"
U
n
l
o
c
k
e
d
"
 
u
n
t
i
l
 
t
h
e
 
r
e
m
o
t
e
 
s
e
s
s
i
o
n
 
h
a
s
 
a
l
s
o
 
u
n
l
o
c
k
e
d


 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
(
i
.
e
.
 
t
h
e
 
m
a
c
h
i
n
e
 
h
a
s
 
s
t
o
p
p
e
d
 
r
u
n
n
i
n
g
)
.




 
 
 
 
 
 
 
 
L
a
u
n
c
h
i
n
g
 
a
 
V
M
 
p
r
o
c
e
s
s
 
c
a
n
 
t
a
k
e
 
s
o
m
e
 
t
i
m
e
 
(
a
 
n
e
w
 
V
M
 
i
s
 
s
t
a
r
t
e
d
 
i
n
 
a
 
n
e
w
 
p
r
o
c
e
s
s
,


 
 
 
 
 
 
 
 
f
o
r
 
w
h
i
c
h
 
m
e
m
o
r
y
 
a
n
d
 
o
t
h
e
r
 
r
e
s
o
u
r
c
e
s
 
n
e
e
d
 
t
o
 
b
e
 
s
e
t
 
u
p
)
.
 
B
e
c
a
u
s
e
 
o
f
 
t
h
i
s
,


 
 
 
 
 
 
 
 
a
n
 
<
l
i
n
k
 
t
o
=
"
I
P
r
o
g
r
e
s
s
"
/
>
 
o
b
j
e
c
t
 
i
s
 
r
e
t
u
r
n
e
d
 
t
o
 
a
l
l
o
w
 
t
h
e
 
c
a
l
l
e
r
 
t
o
 
w
a
i
t


 
 
 
 
 
 
 
 
f
o
r
 
t
h
i
s
 
a
s
y
n
c
h
r
o
n
o
u
s
 
o
p
e
r
a
t
i
o
n
 
t
o
 
b
e
 
c
o
m
p
l
e
t
e
d
.
 
U
n
t
i
l
 
t
h
e
n
,
 
t
h
e
 
c
a
l
l
e
r
'
s


 
 
 
 
 
 
 
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
 
r
e
m
a
i
n
s
 
i
n
 
t
h
e
 
"
U
n
l
o
c
k
e
d
"
 
s
t
a
t
e
,
 
a
n
d
 
i
t
s
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>


 
 
 
 
 
 
 
 
a
n
d
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
c
o
n
s
o
l
e
"
/
>
 
a
t
t
r
i
b
u
t
e
s
 
c
a
n
n
o
t
 
b
e
 
a
c
c
e
s
s
e
d
.


 
 
 
 
 
 
 
 
I
t
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
 
t
o
 
u
s
e
 
<
l
i
n
k
 
t
o
=
"
I
P
r
o
g
r
e
s
s
:
:
w
a
i
t
F
o
r
C
o
m
p
l
e
t
i
o
n
"
/
>
 
o
r


 
 
 
 
 
 
 
 
s
i
m
i
l
a
r
 
c
a
l
l
s
 
t
o
 
w
a
i
t
 
f
o
r
 
c
o
m
p
l
e
t
i
o
n
.
 
C
o
m
p
l
e
t
i
o
n
 
i
s
 
s
i
g
n
a
l
l
e
d
 
w
h
e
n
 
t
h
e
 
V
M


 
 
 
 
 
 
 
 
i
s
 
p
o
w
e
r
e
d
 
o
n
.
 
I
f
 
l
a
u
n
c
h
i
n
g
 
t
h
e
 
V
M
 
f
a
i
l
s
,
 
e
r
r
o
r
 
m
e
s
s
a
g
e
s
 
c
a
n
 
b
e
 
q
u
e
r
i
e
d


 
 
 
 
 
 
 
 
v
i
a
 
t
h
e
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
,
 
i
f
 
a
v
a
i
l
a
b
l
e
.




 
 
 
 
 
 
 
 
T
h
e
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
w
i
l
l
 
h
a
v
e
 
a
t
 
l
e
a
s
t
 
2
 
s
u
b
-
o
p
e
r
a
t
i
o
n
s
.
 
T
h
e
 
f
i
r
s
t


 
 
 
 
 
 
 
 
o
p
e
r
a
t
i
o
n
 
c
o
v
e
r
s
 
t
h
e
 
p
e
r
i
o
d
 
u
p
 
t
o
 
t
h
e
 
n
e
w
 
V
M
 
p
r
o
c
e
s
s
 
c
a
l
l
s
 
p
o
w
e
r
U
p
.


 
 
 
 
 
 
 
 
T
h
e
 
s
u
b
s
e
q
u
e
n
t
 
o
p
e
r
a
t
i
o
n
s
 
m
i
r
r
o
r
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
p
o
w
e
r
U
p
"
/
>


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
.
 
B
e
c
a
u
s
e
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
p
o
w
e
r
U
p
"
/
>
 
m
a
y
 
r
e
q
u
i
r
e


 
 
 
 
 
 
 
 
s
o
m
e
 
e
x
t
r
a
 
s
u
b
-
o
p
e
r
a
t
i
o
n
s
,
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
P
r
o
g
r
e
s
s
:
:
o
p
e
r
a
t
i
o
n
C
o
u
n
t
"
/
>


 
 
 
 
 
 
 
 
m
a
y
 
c
h
a
n
g
e
 
a
t
 
t
h
e
 
c
o
m
p
l
e
t
i
o
n
 
o
f
 
o
p
e
r
a
t
i
o
n
.




 
 
 
 
 
 
 
 
F
o
r
 
d
e
t
a
i
l
s
 
o
n
 
t
h
e
 
t
e
l
e
p
o
r
t
a
t
i
o
n
 
p
r
o
g
r
e
s
s
 
o
p
e
r
a
t
i
o
n
,
 
s
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
p
o
w
e
r
U
p
"
/
>
.




 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
e
n
v
i
r
o
n
m
e
n
t
 
a
r
g
u
m
e
n
t
 
i
s
 
a
 
s
t
r
i
n
g
 
c
o
n
t
a
i
n
i
n
g
 
d
e
f
i
n
i
t
i
o
n
s
 
o
f


 
 
 
 
 
 
 
 
e
n
v
i
r
o
n
m
e
n
t
 
v
a
r
i
a
b
l
e
s
 
i
n
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
f
o
r
m
a
t
:


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
N
A
M
E
[
=
V
A
L
U
E
]
\
n


 
 
 
 
 
 
 
 
N
A
M
E
[
=
V
A
L
U
E
]
\
n


 
 
 
 
 
 
 
 
.
.
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
w
h
e
r
e
 
\
\
n
 
i
s
 
t
h
e
 
n
e
w
 
l
i
n
e
 
c
h
a
r
a
c
t
e
r
.
 
T
h
e
s
e
 
e
n
v
i
r
o
n
m
e
n
t


 
 
 
 
 
 
 
 
v
a
r
i
a
b
l
e
s
 
w
i
l
l
 
b
e
 
a
p
p
e
n
d
e
d
 
t
o
 
t
h
e
 
e
n
v
i
r
o
n
m
e
n
t
 
o
f
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
s
e
r
v
e
r


 
 
 
 
 
 
 
 
p
r
o
c
e
s
s
.
 
I
f
 
a
n
 
e
n
v
i
r
o
n
m
e
n
t
 
v
a
r
i
a
b
l
e
 
e
x
i
s
t
s
 
b
o
t
h
 
i
n
 
t
h
e
 
s
e
r
v
e
r
 
p
r
o
c
e
s
s


 
 
 
 
 
 
 
 
a
n
d
 
i
n
 
t
h
i
s
 
l
i
s
t
,
 
t
h
e
 
v
a
l
u
e
 
f
r
o
m
 
t
h
i
s
 
l
i
s
t
 
t
a
k
e
s
 
p
r
e
c
e
d
e
n
c
e
 
o
v
e
r
 
t
h
e


 
 
 
 
 
 
 
 
s
e
r
v
e
r
'
s
 
v
a
r
i
a
b
l
e
.
 
I
f
 
t
h
e
 
v
a
l
u
e
 
o
f
 
t
h
e
 
e
n
v
i
r
o
n
m
e
n
t
 
v
a
r
i
a
b
l
e
 
i
s


 
 
 
 
 
 
 
 
o
m
i
t
t
e
d
,
 
t
h
i
s
 
v
a
r
i
a
b
l
e
 
w
i
l
l
 
b
e
 
r
e
m
o
v
e
d
 
f
r
o
m
 
t
h
e
 
r
e
s
u
l
t
i
n
g
 
e
n
v
i
r
o
n
m
e
n
t
.


 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
e
n
v
i
r
o
n
m
e
n
t
 
s
t
r
i
n
g
 
i
s
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
,
 
t
h
e
 
s
e
r
v
e
r
 
e
n
v
i
r
o
n
m
e
n
t


 
 
 
 
 
 
 
 
i
s
 
i
n
h
e
r
i
t
e
d
 
b
y
 
t
h
e
 
s
t
a
r
t
e
d
 
p
r
o
c
e
s
s
 
a
s
 
i
s
.




 
 
 
 
 
 
 
 
i
n
 
s
e
s
s
i
o
n
 
o
f
 
t
y
p
e
 
I
S
e
s
s
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
C
l
i
e
n
t
 
s
e
s
s
i
o
n
 
o
b
j
e
c
t
 
t
o
 
w
h
i
c
h
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
 
w
i
l
l
 
b
e
 
c
o
n
n
e
c
t
e
d
 
(
t
h
i
s


 
 
 
 
 
 
 
 
 
 
m
u
s
t
 
b
e
 
i
n
 
"
U
n
l
o
c
k
e
d
"
 
s
t
a
t
e
)
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
r
o
n
t
-
e
n
d
 
t
o
 
u
s
e
 
f
o
r
 
t
h
e
 
n
e
w
 
V
M
 
p
r
o
c
e
s
s
.
 
T
h
e
 
f
o
l
l
o
w
i
n
g
 
a
r
e
 
c
u
r
r
e
n
t
l
y
 
s
u
p
p
o
r
t
e
d
:


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
"
g
u
i
"
:
 
V
i
r
t
u
a
l
B
o
x
 
Q
t
 
G
U
I
 
f
r
o
n
t
-
e
n
d


 
 
 
 
 
 
 
 
 
 
 
 
"
h
e
a
d
l
e
s
s
"
:
 
V
B
o
x
H
e
a
d
l
e
s
s
 
(
V
R
D
E
 
S
e
r
v
e
r
)
 
f
r
o
n
t
-
e
n
d


 
 
 
 
 
 
 
 
 
 
 
 
"
s
d
l
"
:
 
V
i
r
t
u
a
l
B
o
x
 
S
D
L
 
f
r
o
n
t
-
e
n
d


 
 
 
 
 
 
 
 
 
 
 
 
"
e
m
e
r
g
e
n
c
y
s
t
o
p
"
:
 
r
e
s
e
r
v
e
d
 
v
a
l
u
e
,
 
u
s
e
d
 
f
o
r
 
a
b
o
r
t
i
n
g


 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
c
u
r
r
e
n
t
l
y
 
r
u
n
n
i
n
g
 
V
M
 
o
r
 
s
e
s
s
i
o
n
 
o
w
n
e
r
.
 
I
n
 
t
h
i
s
 
c
a
s
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
s
e
s
s
i
o
n
 
p
a
r
a
m
e
t
e
r
 
m
a
y
 
b
e
 
@
c
 
n
u
l
l
 
(
i
f
 
i
t
 
i
s
 
n
o
n
-
n
u
l
l
 
i
t
 
i
s
n
'
t


 
 
 
 
 
 
 
 
 
 
 
 
 
 
u
s
e
d
 
i
n
 
a
n
y
 
w
a
y
)
,
 
a
n
d
 
t
h
e
 
@
a
 
p
r
o
g
r
e
s
s
 
r
e
t
u
r
n
 
v
a
l
u
e
 
w
i
l
l
 
b
e
 
a
l
w
a
y
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
@
c
 
n
u
l
l
.
 
T
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
e
s
 
i
m
m
e
d
i
a
t
e
l
y
.


 
 
 
 
 
 
 
 
 
 
 
 
"
"
:
 
u
s
e
 
t
h
e
 
p
e
r
-
V
M
 
d
e
f
a
u
l
t
 
f
r
o
n
t
e
n
d
 
i
f
 
s
e
t
,
 
o
t
h
e
r
w
i
s
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
g
l
o
b
a
l
 
d
e
f
a
u
l
t
 
d
e
f
i
n
e
d
 
i
n
 
t
h
e
 
s
y
s
t
e
m
 
p
r
o
p
e
r
t
i
e
s
.
 
I
f
 
n
e
i
t
h
e
r


 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
r
e
 
s
e
t
,
 
t
h
e
 
A
P
I
 
w
i
l
l
 
l
a
u
n
c
h
 
a
 
"
g
u
i
"
 
s
e
s
s
i
o
n
,
 
w
h
i
c
h
 
m
a
y


 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
a
i
l
 
i
f
 
t
h
e
r
e
 
i
s
 
n
o
 
w
i
n
d
o
w
i
n
g
 
e
n
v
i
r
o
n
m
e
n
t
 
a
v
a
i
l
a
b
l
e
.
 
S
e
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
"
/
>
 
a
n
d


 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
e
n
v
i
r
o
n
m
e
n
t
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
E
n
v
i
r
o
n
m
e
n
t
 
t
o
 
p
a
s
s
 
t
o
 
t
h
e
 
V
M
 
p
r
o
c
e
s
s
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
U
N
E
X
P
E
C
T
E
D


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
r
e
g
i
s
t
e
r
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
s
e
s
s
i
o
n
 
t
y
p
e
 
@
a
 
t
y
p
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
N
o
 
m
a
c
h
i
n
e
 
m
a
t
c
h
i
n
g
 
@
a
 
m
a
c
h
i
n
e
I
d
 
f
o
u
n
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
S
e
s
s
i
o
n
 
a
l
r
e
a
d
y
 
o
p
e
n
 
o
r
 
b
e
i
n
g
 
o
p
e
n
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
P
R
T
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
L
a
u
n
c
h
i
n
g
 
p
r
o
c
e
s
s
 
f
o
r
 
m
a
c
h
i
n
e
 
f
a
i
l
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
V
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
F
a
i
l
e
d
 
t
o
 
a
s
s
i
g
n
 
m
a
c
h
i
n
e
 
t
o
 
s
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
e
s
s
i
o
n
,
 
t
y
p
e
_
p
,
 
e
n
v
i
r
o
n
m
e
n
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
b
o
o
t
_
o
r
d
e
r
(
s
e
l
f
,
 
p
o
s
i
t
i
o
n
,
 
d
e
v
i
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
P
u
t
s
 
t
h
e
 
g
i
v
e
n
 
d
e
v
i
c
e
 
t
o
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
o
s
i
t
i
o
n
 
i
n


 
 
 
 
 
 
 
 
t
h
e
 
b
o
o
t
 
o
r
d
e
r
.




 
 
 
 
 
 
 
 
T
o
 
i
n
d
i
c
a
t
e
 
t
h
a
t
 
n
o
 
d
e
v
i
c
e
 
i
s
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
p
o
s
i
t
i
o
n
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
D
e
v
i
c
e
T
y
p
e
_
N
u
l
l
"
/
>
 
s
h
o
u
l
d
 
b
e
 
u
s
e
d
.




 
 
 
 
 
 
 
 
@
t
o
d
o
 
s
e
t
H
a
r
d
D
i
s
k
B
o
o
t
O
r
d
e
r
(
)
,
 
s
e
t
N
e
t
w
o
r
k
B
o
o
t
O
r
d
e
r
(
)




 
 
 
 
 
 
 
 
i
n
 
p
o
s
i
t
i
o
n
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
s
i
t
i
o
n
 
i
n
 
t
h
e
 
b
o
o
t
 
o
r
d
e
r
 
(
@
c
 
1
 
t
o
 
t
h
e
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f


 
 
 
 
 
 
 
 
 
 
d
e
v
i
c
e
s
 
t
h
e
 
m
a
c
h
i
n
e
 
c
a
n
 
b
o
o
t
 
f
r
o
m
,
 
a
s
 
r
e
t
u
r
n
e
d
 
b
y


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
m
a
x
B
o
o
t
P
o
s
i
t
i
o
n
"
/
>
)
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
y
p
e
 
o
f
 
t
h
e
 
d
e
v
i
c
e
 
u
s
e
d
 
t
o
 
b
o
o
t
 
a
t
 
t
h
e
 
g
i
v
e
n
 
p
o
s
i
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
B
o
o
t
 
@
a
 
p
o
s
i
t
i
o
n
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
N
O
T
I
M
P
L


 
 
 
 
 
 
 
 
 
 
 
 
B
o
o
t
i
n
g
 
f
r
o
m
 
U
S
B
 
@
a
 
d
e
v
i
c
e
 
c
u
r
r
e
n
t
l
y
 
n
o
t
 
s
u
p
p
o
r
t
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
B
o
o
t
O
r
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
o
s
i
t
i
o
n
,
 
d
e
v
i
c
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
b
o
o
t
_
o
r
d
e
r
(
s
e
l
f
,
 
p
o
s
i
t
i
o
n
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
d
e
v
i
c
e
 
t
y
p
e
 
t
h
a
t
 
o
c
c
u
p
i
e
s
 
t
h
e
 
s
p
e
c
i
f
i
e
d


 
 
 
 
 
 
 
 
p
o
s
i
t
i
o
n
 
i
n
 
t
h
e
 
b
o
o
t
 
o
r
d
e
r
.




 
 
 
 
 
 
 
 
@
t
o
d
o
 
[
r
e
m
o
v
e
?
]


 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
c
a
n
 
h
a
v
e
 
m
o
r
e
 
t
h
a
n
 
o
n
e
 
d
e
v
i
c
e
 
o
f
 
t
h
e
 
r
e
t
u
r
n
e
d
 
t
y
p
e


 
 
 
 
 
 
 
 
(
s
u
c
h
 
a
s
 
h
a
r
d
 
d
i
s
k
s
)
,
 
t
h
e
n
 
a
 
s
e
p
a
r
a
t
e
 
m
e
t
h
o
d
 
s
h
o
u
l
d
 
b
e
 
u
s
e
d
 
t
o


 
 
 
 
 
 
 
 
r
e
t
r
i
e
v
e
 
t
h
e
 
i
n
d
i
v
i
d
u
a
l
 
d
e
v
i
c
e
 
t
h
a
t
 
o
c
c
u
p
i
e
s
 
t
h
e
 
g
i
v
e
n
 
p
o
s
i
t
i
o
n
.




 
 
 
 
 
 
 
 
I
f
 
h
e
r
e
 
a
r
e
 
n
o
 
d
e
v
i
c
e
s
 
a
t
 
t
h
e
 
g
i
v
e
n
 
p
o
s
i
t
i
o
n
,
 
t
h
e
n


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
D
e
v
i
c
e
T
y
p
e
_
N
u
l
l
"
/
>
 
i
s
 
r
e
t
u
r
n
e
d
.




 
 
 
 
 
 
 
 
@
t
o
d
o
 
g
e
t
H
a
r
d
D
i
s
k
B
o
o
t
O
r
d
e
r
(
)
,
 
g
e
t
N
e
t
w
o
r
k
B
o
o
t
O
r
d
e
r
(
)




 
 
 
 
 
 
 
 
i
n
 
p
o
s
i
t
i
o
n
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
s
i
t
i
o
n
 
i
n
 
t
h
e
 
b
o
o
t
 
o
r
d
e
r
 
(
@
c
 
1
 
t
o
 
t
h
e
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f


 
 
 
 
 
 
 
 
 
 
d
e
v
i
c
e
s
 
t
h
e
 
m
a
c
h
i
n
e
 
c
a
n
 
b
o
o
t
 
f
r
o
m
,
 
a
s
 
r
e
t
u
r
n
e
d
 
b
y


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
m
a
x
B
o
o
t
P
o
s
i
t
i
o
n
"
/
>
)
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
a
t
 
t
h
e
 
g
i
v
e
n
 
p
o
s
i
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
B
o
o
t
 
@
a
 
p
o
s
i
t
i
o
n
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
B
o
o
t
O
r
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
o
s
i
t
i
o
n
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
D
e
v
i
c
e
T
y
p
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
t
t
a
c
h
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
t
y
p
e
_
p
,
 
m
e
d
i
u
m
)
:


 
 
 
 
 
 
 
 
"
"
"
A
t
t
a
c
h
e
s
 
a
 
d
e
v
i
c
e
 
a
n
d
 
o
p
t
i
o
n
a
l
l
y
 
m
o
u
n
t
s
 
a
 
m
e
d
i
u
m
 
t
o
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e


 
 
 
 
 
 
 
 
c
o
n
t
r
o
l
l
e
r
 
(
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
"
/
>
,
 
i
d
e
n
t
i
f
i
e
d
 
b
y
 
@
a
 
n
a
m
e
)
,


 
 
 
 
 
 
 
 
a
t
 
t
h
e
 
i
n
d
i
c
a
t
e
d
 
p
o
r
t
 
a
n
d
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
i
n
t
e
n
d
e
d
 
f
o
r
 
m
a
n
a
g
i
n
g
 
s
t
o
r
a
g
e
 
d
e
v
i
c
e
s
 
i
n
 
g
e
n
e
r
a
l
 
w
h
i
l
e
 
a


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
i
s
 
p
o
w
e
r
e
d
 
o
f
f
.
 
I
t
 
c
a
n
 
b
e
 
u
s
e
d
 
t
o
 
a
t
t
a
c
h
 
a
n
d
 
d
e
t
a
c
h
 
f
i
x
e
d


 
 
 
 
 
 
 
 
a
n
d
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
.
 
T
h
e
 
f
o
l
l
o
w
i
n
g
 
k
i
n
d
 
o
f
 
m
e
d
i
a
 
c
a
n
 
b
e
 
a
t
t
a
c
h
e
d


 
 
 
 
 
 
 
 
t
o
 
a
 
m
a
c
h
i
n
e
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
F
o
r
 
f
i
x
e
d
 
a
n
d
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
,
 
y
o
u
 
c
a
n
 
p
a
s
s
 
i
n
 
a
 
m
e
d
i
u
m
 
t
h
a
t
 
w
a
s


 
 
 
 
 
 
 
 
 
 
 
 
p
r
e
v
i
o
u
s
l
y
 
o
p
e
n
e
d
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
e
d
i
u
m
"
/
>
.


 
 
 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
 
 
O
n
l
y
 
f
o
r
 
s
t
o
r
a
g
e
 
d
e
v
i
c
e
s
 
s
u
p
p
o
r
t
i
n
g
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
 
(
s
u
c
h
 
a
s


 
 
 
 
 
 
 
 
 
 
 
 
D
V
D
s
 
a
n
d
 
f
l
o
p
p
i
e
s
)
,
 
y
o
u
 
c
a
n
 
a
l
s
o
 
s
p
e
c
i
f
y
 
a
 
n
u
l
l
 
p
o
i
n
t
e
r
 
t
o


 
 
 
 
 
 
 
 
 
 
 
 
i
n
d
i
c
a
t
e
 
a
n
 
e
m
p
t
y
 
d
r
i
v
e
 
o
r
 
o
n
e
 
o
f
 
t
h
e
 
m
e
d
i
u
m
 
o
b
j
e
c
t
s
 
l
i
s
t
e
d


 
 
 
 
 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
:
:
D
V
D
D
r
i
v
e
s
"
/
>
 
a
n
d
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
:
:
f
l
o
p
p
y
D
r
i
v
e
s
"
/
>


 
 
 
 
 
 
 
 
 
 
 
 
a
r
r
a
y
s
 
t
o
 
i
n
d
i
c
a
t
e
 
a
 
h
o
s
t
 
d
r
i
v
e
.


 
 
 
 
 
 
 
 
 
 
 
 
F
o
r
 
r
e
m
o
v
a
b
l
e
 
d
e
v
i
c
e
s
,
 
y
o
u
 
c
a
n
 
a
l
s
o
 
u
s
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
m
o
u
n
t
M
e
d
i
u
m
"
/
>


 
 
 
 
 
 
 
 
 
 
 
 
t
o
 
c
h
a
n
g
e
 
t
h
e
 
m
e
d
i
a
 
w
h
i
l
e
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
I
n
 
a
 
V
M
'
s
 
d
e
f
a
u
l
t
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
o
f
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
,
 
t
h
e
 
s
e
c
o
n
d
a
r
y


 
 
 
 
 
 
 
 
m
a
s
t
e
r
 
o
f
 
t
h
e
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
 
i
s
 
u
s
e
d
 
f
o
r
 
a
 
C
D
/
D
V
D
 
d
r
i
v
e
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
c
a
l
l
i
n
g
 
t
h
i
s
 
r
e
t
u
r
n
s
 
s
u
c
c
e
s
s
f
u
l
l
y
,
 
a
 
n
e
w
 
i
n
s
t
a
n
c
e
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
"
/
>
 
w
i
l
l
 
a
p
p
e
a
r
 
i
n
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
l
i
s
t
 
o
f
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
s
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
m
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
s
"
/
>
)
.




 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
 
a
n
d
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
"
/
>
 
f
o
r
 
m
o
r
e


 
 
 
 
 
 
 
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
a
t
t
a
c
h
i
n
g
 
m
e
d
i
a
.




 
 
 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
d
e
v
i
c
e
 
s
l
o
t
 
m
u
s
t
 
n
o
t
 
h
a
v
e
 
a
 
d
e
v
i
c
e
 
a
t
t
a
c
h
e
d
 
t
o
 
i
t
,


 
 
 
 
 
 
 
 
o
r
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
f
a
i
l
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
Y
o
u
 
c
a
n
n
o
t
 
a
t
t
a
c
h
 
a
 
d
e
v
i
c
e
 
t
o
 
a
 
n
e
w
l
y
 
c
r
e
a
t
e
d
 
m
a
c
h
i
n
e
 
u
n
t
i
l


 
 
 
 
 
 
 
 
 
 
t
h
i
s
 
m
a
c
h
i
n
e
'
s
 
s
e
t
t
i
n
g
s
 
a
r
e
 
s
a
v
e
d
 
t
o
 
d
i
s
k
 
u
s
i
n
g


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
e
d
i
u
m
 
i
s
 
b
e
i
n
g
 
a
t
t
a
c
h
e
d
 
i
n
d
i
r
e
c
t
l
y
,
 
a
 
n
e
w
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
w
i
l
l
 
i
m
p
l
i
c
i
t
l
y
 
b
e
 
c
r
e
a
t
e
d
 
f
o
r
 
i
t
 
a
n
d
 
a
t
t
a
c
h
e
d
 
i
n
s
t
e
a
d
.
 
I
f
 
t
h
e


 
 
 
 
 
 
 
 
 
 
c
h
a
n
g
e
s
 
m
a
d
e
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
(
i
n
c
l
u
d
i
n
g
 
t
h
i
s
 
i
n
d
i
r
e
c
t


 
 
 
 
 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
)
 
a
r
e
 
l
a
t
e
r
 
c
a
n
c
e
l
l
e
d
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
#
d
i
s
c
a
r
d
S
e
t
t
i
n
g
s
"
/
>
,


 
 
 
 
 
 
 
 
 
 
t
h
i
s
 
i
m
p
l
i
c
i
t
l
y
 
c
r
e
a
t
e
d
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
u
m
 
w
i
l
l
 
i
m
p
l
i
c
i
t
l
y


 
 
 
 
 
 
 
 
 
 
b
e
 
d
e
l
e
t
e
d
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
r
t
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
o
.
 
F
o
r
 
a
n
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
,
 
0
 
s
p
e
c
i
f
i
e
s


 
 
 
 
 
 
 
 
t
h
e
 
p
r
i
m
a
r
y
 
c
o
n
t
r
o
l
l
e
r
 
a
n
d
 
1
 
s
p
e
c
i
f
i
e
s
 
t
h
e
 
s
e
c
o
n
d
a
r
y
 
c
o
n
t
r
o
l
l
e
r
.


 
 
 
 
 
 
 
 
F
o
r
 
a
 
S
C
S
I
 
c
o
n
t
r
o
l
l
e
r
,
 
t
h
i
s
 
m
u
s
t
 
r
a
n
g
e
 
f
r
o
m
 
0
 
t
o
 
1
5
;
 
f
o
r
 
a
 
S
A
T
A
 
c
o
n
t
r
o
l
l
e
r
,


 
 
 
 
 
 
 
 
f
r
o
m
 
0
 
t
o
 
2
9
;
 
f
o
r
 
a
n
 
S
A
S
 
c
o
n
t
r
o
l
l
e
r
,
 
f
r
o
m
 
0
 
t
o
 
7
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
o
.
 
T
h
i
s
 
i
s
 
o
n
l
y


 
 
 
 
 
 
 
 
r
e
l
e
v
a
n
t
 
f
o
r
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
s
,
 
f
o
r
 
w
h
i
c
h
 
0
 
s
p
e
c
i
f
i
e
s
 
t
h
e
 
m
a
s
t
e
r
 
d
e
v
i
c
e
 
a
n
d


 
 
 
 
 
 
 
 
1
 
s
p
e
c
i
f
i
e
s
 
t
h
e
 
s
l
a
v
e
 
d
e
v
i
c
e
.
 
F
o
r
 
a
l
l
 
o
t
h
e
r
 
c
o
n
t
r
o
l
l
e
r
 
t
y
p
e
s
,
 
t
h
i
s
 
m
u
s
t


 
 
 
 
 
 
 
 
b
e
 
0
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
t
y
p
e
 
o
f
 
t
h
e
 
a
t
t
a
c
h
e
d
 
d
e
v
i
c
e
.
 
F
o
r
 
m
e
d
i
a
 
o
p
e
n
e
d
 
b
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
e
d
i
u
m
"
/
>
,
 
t
h
i
s
 
m
u
s
t
 
m
a
t
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
y
p
e


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
d
 
t
h
e
r
e
.




 
 
 
 
 
 
 
 
i
n
 
m
e
d
i
u
m
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
t
o
 
m
o
u
n
t
 
o
r
 
@
c
 
n
u
l
l
 
f
o
r
 
a
n
 
e
m
p
t
y
 
d
r
i
v
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
,
 
o
r


 
 
 
 
 
 
 
 
 
 
f
i
l
e
 
o
r
 
U
U
I
D
 
n
o
t
 
f
o
u
n
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
m
u
s
t
 
b
e
 
r
e
g
i
s
t
e
r
e
d
 
b
e
f
o
r
e
 
m
e
d
i
a
 
c
a
n
 
b
e
 
a
t
t
a
c
h
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E


 
 
 
 
 
 
 
 
 
 
 
 
A
 
m
e
d
i
u
m
 
i
s
 
a
l
r
e
a
d
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
o
r
 
a
n
o
t
h
e
r
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
t
t
a
c
h
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
t
y
p
e
_
p
,
 
m
e
d
i
u
m
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
t
t
a
c
h
_
d
e
v
i
c
e
_
w
i
t
h
o
u
t
_
m
e
d
i
u
m
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
t
y
p
e
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
A
t
t
a
c
h
e
s
 
a
 
d
e
v
i
c
e
 
a
n
d
 
o
p
t
i
o
n
a
l
l
y
 
m
o
u
n
t
s
 
a
 
m
e
d
i
u
m
 
t
o
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e


 
 
 
 
 
 
c
o
n
t
r
o
l
l
e
r
 
(
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
"
/
>
,
 
i
d
e
n
t
i
f
i
e
d
 
b
y
 
@
a
 
n
a
m
e
)
,


 
 
 
 
 
 
a
t
 
t
h
e
 
i
n
d
i
c
a
t
e
d
 
p
o
r
t
 
a
n
d
 
d
e
v
i
c
e
.




 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
i
n
t
e
n
d
e
d
 
f
o
r
 
m
a
n
a
g
i
n
g
 
s
t
o
r
a
g
e
 
d
e
v
i
c
e
s
 
i
n
 
g
e
n
e
r
a
l
 
w
h
i
l
e
 
a


 
 
 
 
 
 
m
a
c
h
i
n
e
 
i
s
 
p
o
w
e
r
e
d
 
o
f
f
.
 
I
t
 
c
a
n
 
b
e
 
u
s
e
d
 
t
o
 
a
t
t
a
c
h
 
a
n
d
 
d
e
t
a
c
h
 
f
i
x
e
d


 
 
 
 
 
 
a
n
d
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
.
 
T
h
e
 
f
o
l
l
o
w
i
n
g
 
k
i
n
d
 
o
f
 
m
e
d
i
a
 
c
a
n
 
b
e
 
a
t
t
a
c
h
e
d


 
 
 
 
 
 
t
o
 
a
 
m
a
c
h
i
n
e
:


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
F
o
r
 
f
i
x
e
d
 
a
n
d
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
,
 
y
o
u
 
c
a
n
 
p
a
s
s
 
i
n
 
a
 
m
e
d
i
u
m
 
t
h
a
t
 
w
a
s


 
 
 
 
 
 
p
r
e
v
i
o
u
s
l
y
 
o
p
e
n
e
d
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
e
d
i
u
m
"
/
>
.


 
 
 
 
 
 




 
 
 
 
 
 
O
n
l
y
 
f
o
r
 
s
t
o
r
a
g
e
 
d
e
v
i
c
e
s
 
s
u
p
p
o
r
t
i
n
g
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
 
(
s
u
c
h
 
a
s


 
 
 
 
 
 
D
V
D
s
 
a
n
d
 
f
l
o
p
p
i
e
s
)
 
w
i
t
h
 
a
n
 
e
m
p
t
y
 
d
r
i
v
e
 
o
r
 
o
n
e
 
o
f
 
t
h
e
 
m
e
d
i
u
m
 
o
b
j
e
c
t
s
 
l
i
s
t
e
d


 
 
 
 
 
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
:
:
D
V
D
D
r
i
v
e
s
"
/
>
 
a
n
d
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
:
:
f
l
o
p
p
y
D
r
i
v
e
s
"
/
>


 
 
 
 
 
 
a
r
r
a
y
s
 
t
o
 
i
n
d
i
c
a
t
e
 
a
 
h
o
s
t
 
d
r
i
v
e
.


 
 
 
 
 
 
F
o
r
 
r
e
m
o
v
a
b
l
e
 
d
e
v
i
c
e
s
,
 
y
o
u
 
c
a
n
 
a
l
s
o
 
u
s
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
m
o
u
n
t
M
e
d
i
u
m
"
/
>


 
 
 
 
 
 
t
o
 
c
h
a
n
g
e
 
t
h
e
 
m
e
d
i
a
 
w
h
i
l
e
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 


 
 
 
 
 
 




 
 
 
 
 
 
I
n
 
a
 
V
M
'
s
 
d
e
f
a
u
l
t
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
o
f
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
,
 
t
h
e
 
s
e
c
o
n
d
a
r
y


 
 
 
 
 
 
m
a
s
t
e
r
 
o
f
 
t
h
e
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
 
i
s
 
u
s
e
d
 
f
o
r
 
a
 
C
D
/
D
V
D
 
d
r
i
v
e
.


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
"
/
>
 
w
i
l
l
 
a
p
p
e
a
r
 
i
n
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
l
i
s
t
 
o
f
 
m
e
d
i
u
m


 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
s
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
m
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
s
"
/
>
)
.




 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
 
a
n
d
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
"
/
>
 
f
o
r
 
m
o
r
e


 
 
 
 
 
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
a
t
t
a
c
h
i
n
g
 
m
e
d
i
a
.




 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
d
e
v
i
c
e
 
s
l
o
t
 
m
u
s
t
 
n
o
t
 
h
a
v
e
 
a
 
d
e
v
i
c
e
 
a
t
t
a
c
h
e
d
 
t
o
 
i
t
,


 
 
 
 
 
 
o
r
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
f
a
i
l
.


 
 
 
 
 
 


 
 
 
 
 
 
Y
o
u
 
c
a
n
n
o
t
 
a
t
t
a
c
h
 
a
 
d
e
v
i
c
e
 
t
o
 
a
 
n
e
w
l
y
 
c
r
e
a
t
e
d
 
m
a
c
h
i
n
e
 
u
n
t
i
l


 
 
 
 
 
 
t
h
i
s
 
m
a
c
h
i
n
e
'
s
 
s
e
t
t
i
n
g
s
 
a
r
e
 
s
a
v
e
d
 
t
o
 
d
i
s
k
 
u
s
i
n
g


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
.


 
 
 
 
 
 


 
 
 
 
 
 


 
 
 
 
 
 
I
f
 
t
h
e
 
m
e
d
i
u
m
 
i
s
 
b
e
i
n
g
 
a
t
t
a
c
h
e
d
 
i
n
d
i
r
e
c
t
l
y
,
 
a
 
n
e
w
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
u
m


 
 
 
 
 
 
w
i
l
l
 
i
m
p
l
i
c
i
t
l
y
 
b
e
 
c
r
e
a
t
e
d
 
f
o
r
 
i
t
 
a
n
d
 
a
t
t
a
c
h
e
d
 
i
n
s
t
e
a
d
.
 
I
f
 
t
h
e


 
 
 
 
 
 
c
h
a
n
g
e
s
 
m
a
d
e
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
(
i
n
c
l
u
d
i
n
g
 
t
h
i
s
 
i
n
d
i
r
e
c
t


 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
)
 
a
r
e
 
l
a
t
e
r
 
c
a
n
c
e
l
l
e
d
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
#
d
i
s
c
a
r
d
S
e
t
t
i
n
g
s
"
/
>
,


 
 
 
 
 
 
t
h
i
s
 
i
m
p
l
i
c
i
t
l
y
 
c
r
e
a
t
e
d
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
u
m
 
w
i
l
l
 
i
m
p
l
i
c
i
t
l
y


 
 
 
 
 
 
b
e
 
d
e
l
e
t
e
d
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
r
t
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
o
.
 
F
o
r
 
a
n
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
,
 
0
 
s
p
e
c
i
f
i
e
s


 
 
 
 
 
 
t
h
e
 
p
r
i
m
a
r
y
 
c
o
n
t
r
o
l
l
e
r
 
a
n
d
 
1
 
s
p
e
c
i
f
i
e
s
 
t
h
e
 
s
e
c
o
n
d
a
r
y
 
c
o
n
t
r
o
l
l
e
r
.


 
 
 
 
 
 
F
o
r
 
a
 
S
C
S
I
 
c
o
n
t
r
o
l
l
e
r
,
 
t
h
i
s
 
m
u
s
t
 
r
a
n
g
e
 
f
r
o
m
 
0
 
t
o
 
1
5
;
 
f
o
r
 
a
 
S
A
T
A
 
c
o
n
t
r
o
l
l
e
r
,


 
 
 
 
 
 
f
r
o
m
 
0
 
t
o
 
2
9
;
 
f
o
r
 
a
n
 
S
A
S
 
c
o
n
t
r
o
l
l
e
r
,
 
f
r
o
m
 
0
 
t
o
 
7
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
o
.
 
T
h
i
s
 
i
s
 
o
n
l
y


 
 
 
 
 
 
r
e
l
e
v
a
n
t
 
f
o
r
 
I
D
E
 
c
o
n
t
r
o
l
l
e
r
s
,
 
f
o
r
 
w
h
i
c
h
 
0
 
s
p
e
c
i
f
i
e
s
 
t
h
e
 
m
a
s
t
e
r
 
d
e
v
i
c
e
 
a
n
d


 
 
 
 
 
 
1
 
s
p
e
c
i
f
i
e
s
 
t
h
e
 
s
l
a
v
e
 
d
e
v
i
c
e
.
 
F
o
r
 
a
l
l
 
o
t
h
e
r
 
c
o
n
t
r
o
l
l
e
r
 
t
y
p
e
s
,
 
t
h
i
s
 
m
u
s
t


 
 
 
 
 
 
b
e
 
0
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
t
y
p
e
 
o
f
 
t
h
e
 
a
t
t
a
c
h
e
d
 
d
e
v
i
c
e
.
 
F
o
r
 
m
e
d
i
a
 
o
p
e
n
e
d
 
b
y


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
e
d
i
u
m
"
/
>
,
 
t
h
i
s
 
m
u
s
t
 
m
a
t
c
h
 
t
h
e
 
d
e
v
i
c
e
 
t
y
p
e


 
 
 
 
 
 
s
p
e
c
i
f
i
e
d
 
t
h
e
r
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
,
 
o
r


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
 
o
r
 
U
U
I
D
 
n
o
t
 
f
o
u
n
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
m
u
s
t
 
b
e
 
r
e
g
i
s
t
e
r
e
d
 
b
e
f
o
r
e
 
m
e
d
i
a
 
c
a
n
 
b
e
 
a
t
t
a
c
h
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E


 
 
 
 
 
 
 
 
 
 
 
 
A
 
m
e
d
i
u
m
 
i
s
 
a
l
r
e
a
d
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
o
r
 
a
n
o
t
h
e
r
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
t
t
a
c
h
D
e
v
i
c
e
W
i
t
h
o
u
t
M
e
d
i
u
m
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
t
y
p
e
_
p
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
t
a
c
h
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
D
e
t
a
c
h
e
s
 
t
h
e
 
d
e
v
i
c
e
 
a
t
t
a
c
h
e
d
 
t
o
 
a
 
d
e
v
i
c
e
 
s
l
o
t
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
b
u
s
.




 
 
 
 
 
 
 
 
D
e
t
a
c
h
i
n
g
 
t
h
e
 
d
e
v
i
c
e
 
f
r
o
m
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
d
e
f
e
r
r
e
d
.
 
T
h
i
s
 
m
e
a
n
s


 
 
 
 
 
 
 
 
t
h
a
t
 
t
h
e
 
m
e
d
i
u
m
 
r
e
m
a
i
n
s
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
t
h
e
 
m
a
c
h
i
n
e
 
w
h
e
n
 
t
h
i
s
 
m
e
t
h
o
d


 
 
 
 
 
 
 
 
r
e
t
u
r
n
s
 
a
n
d
 
g
e
t
s
 
a
c
t
u
a
l
l
y
 
d
e
-
a
s
s
o
c
i
a
t
e
d
 
o
n
l
y
 
a
f
t
e
r
 
a
 
s
u
c
c
e
s
s
f
u
l


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
c
a
l
l
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>


 
 
 
 
 
 
 
 
f
o
r
 
m
o
r
e
 
d
e
t
a
i
l
e
d
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
a
t
t
a
c
h
i
n
g
 
m
e
d
i
a
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
Y
o
u
 
c
a
n
n
o
t
 
d
e
t
a
c
h
 
a
 
d
e
v
i
c
e
 
f
r
o
m
 
a
 
r
u
n
n
i
n
g
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
D
e
t
a
c
h
i
n
g
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
 
i
m
p
l
i
c
i
t
l
y
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
#
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
 
f
o
r
 
t
h
e
 
i
n
d
i
r
e
c
t
 
a
t
t
a
c
h
m
e
n
t
 
u
s
i
n
g
 
t
h
i
s


 
 
 
 
 
 
 
 
 
 
m
e
t
h
o
d
 
w
i
l
l
 
n
o
t
 
i
m
p
l
i
c
i
t
l
y
 
d
e
l
e
t
e
 
t
h
e
m
.
 
T
h
e


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
d
e
l
e
t
e
S
t
o
r
a
g
e
"
/
>
 
o
p
e
r
a
t
i
o
n
 
s
h
o
u
l
d
 
b
e


 
 
 
 
 
 
 
 
 
 
e
x
p
l
i
c
i
t
l
y
 
p
e
r
f
o
r
m
e
d
 
b
y
 
t
h
e
 
c
a
l
l
e
r
 
a
f
t
e
r
 
t
h
e
 
m
e
d
i
u
m
 
i
s
 
s
u
c
c
e
s
s
f
u
l
l
y


 
 
 
 
 
 
 
 
 
 
d
e
t
a
c
h
e
d
 
a
n
d
 
t
h
e
 
s
e
t
t
i
n
g
s
 
a
r
e
 
s
a
v
e
d
 
w
i
t
h


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
,
 
i
f
 
i
t
 
i
s
 
t
h
e
 
d
e
s
i
r
e
d
 
a
c
t
i
o
n
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
o
 
d
e
t
a
c
h
 
t
h
e
 
m
e
d
i
u
m
 
f
r
o
m
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
r
t
 
n
u
m
b
e
r
 
t
o
 
d
e
t
a
c
h
 
t
h
e
 
m
e
d
i
u
m
 
f
r
o
m
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
n
u
m
b
e
r
 
t
o
 
d
e
t
a
c
h
 
t
h
e
 
m
e
d
i
u
m
 
f
r
o
m
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
d
e
t
a
c
h
 
m
e
d
i
u
m
 
f
r
o
m
 
a
 
r
u
n
n
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
N
o
 
m
e
d
i
u
m
 
a
t
t
a
c
h
e
d
 
t
o
 
g
i
v
e
n
 
s
l
o
t
/
b
u
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
N
O
T
_
S
U
P
P
O
R
T
E
D


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
f
o
r
m
a
t
 
d
o
e
s
 
n
o
t
 
s
u
p
p
o
r
t
 
s
t
o
r
a
g
e
 
d
e
l
e
t
i
o
n
 
(
o
n
l
y
 
f
o
r
 
i
m
p
l
i
c
i
t
l
y


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
,
 
s
h
o
u
l
d
 
n
o
t
 
h
a
p
p
e
n
)
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
t
a
c
h
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
p
a
s
s
t
h
r
o
u
g
h
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
p
a
s
s
t
h
r
o
u
g
h
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
t
h
e
 
p
a
s
s
t
h
r
o
u
g
h
 
m
o
d
e
 
o
f
 
a
n
 
e
x
i
s
t
i
n
g
 
D
V
D
 
d
e
v
i
c
e
.
 
C
h
a
n
g
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
 
w
h
i
l
e
 
t
h
e
 
V
M
 
i
s
 
r
u
n
n
i
n
g
 
i
s
 
f
o
r
b
i
d
d
e
n
.
 
T
h
e
 
s
e
t
t
i
n
g
 
i
s
 
o
n
l
y
 
u
s
e
d


 
 
 
 
 
 
 
 
i
f
 
a
t
 
V
M
 
s
t
a
r
t
 
t
h
e
 
d
e
v
i
c
e
 
i
s
 
c
o
n
f
i
g
u
r
e
d
 
a
s
 
a
 
h
o
s
t
 
D
V
D
 
d
r
i
v
e
,
 
i
n
 
a
l
l


 
 
 
 
 
 
 
 
o
t
h
e
r
 
c
a
s
e
s
 
i
t
 
i
s
 
i
g
n
o
r
e
d
.
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t
 
a
l
r
e
a
d
y
 
e
x
i
s
t
;
 
s
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
 
f
o
r
 
h
o
w
 
t
o
 
a
t
t
a
c
h
 
a
 
n
e
w
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
a
n
d


 
 
 
 
 
 
 
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
p
a
s
s
t
h
r
o
u
g
h
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
v
a
l
u
e
 
f
o
r
 
t
h
e
 
p
a
s
s
t
h
r
o
u
g
h
 
s
e
t
t
i
n
g
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
m
o
d
i
f
y
 
a
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
a
s
s
t
h
r
o
u
g
h
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
p
a
s
s
t
h
r
o
u
g
h
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
t
e
m
p
o
r
a
r
y
_
e
j
e
c
t
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
t
e
m
p
o
r
a
r
y
_
e
j
e
c
t
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
t
h
e
 
b
e
h
a
v
i
o
r
 
f
o
r
 
g
u
e
s
t
-
t
r
i
g
g
e
r
e
d
 
m
e
d
i
u
m
 
e
j
e
c
t
.
 
I
n
 
s
o
m
e
 
s
i
t
u
a
t
i
o
n
s


 
 
 
 
 
 
 
 
i
t
 
i
s
 
d
e
s
i
r
a
b
l
e
 
t
h
a
t
 
s
u
c
h
 
e
j
e
c
t
s
 
u
p
d
a
t
e
 
t
h
e
 
V
M
 
c
o
n
f
i
g
u
r
a
t
i
o
n
,
 
a
n
d
 
i
n


 
 
 
 
 
 
 
 
o
t
h
e
r
s
 
t
h
e
 
e
j
e
c
t
 
s
h
o
u
l
d
 
k
e
e
p
 
t
h
e
 
V
M
 
c
o
n
f
i
g
u
r
a
t
i
o
n
.
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t


 
 
 
 
 
 
 
 
a
l
r
e
a
d
y
 
e
x
i
s
t
;
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
 
f
o
r
 
h
o
w
 
t
o


 
 
 
 
 
 
 
 
a
t
t
a
c
h
 
a
 
n
e
w
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
a
n
d


 
 
 
 
 
 
 
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
t
e
m
p
o
r
a
r
y
_
e
j
e
c
t
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
v
a
l
u
e
 
f
o
r
 
t
h
e
 
e
j
e
c
t
 
b
e
h
a
v
i
o
r
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
m
o
d
i
f
y
 
a
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
t
e
m
p
o
r
a
r
y
E
j
e
c
t
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
t
e
m
p
o
r
a
r
y
_
e
j
e
c
t
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
n
o
n
_
r
o
t
a
t
i
o
n
a
l
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
n
o
n
_
r
o
t
a
t
i
o
n
a
l
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
a
 
f
l
a
g
 
i
n
 
t
h
e
 
d
e
v
i
c
e
 
i
n
f
o
r
m
a
t
i
o
n
 
w
h
i
c
h
 
i
n
d
i
c
a
t
e
s
 
t
h
a
t
 
t
h
e
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 
i
s
 
n
o
t
 
b
a
s
e
d
 
o
n
 
r
o
t
a
t
i
o
n
a
l
 
t
e
c
h
n
o
l
o
g
y
,
 
i
.
e
.
 
t
h
a
t
 
t
h
e
 
a
c
c
e
s
s
 
t
i
m
e
s
 
a
r
e


 
 
 
 
 
 
 
 
m
o
r
e
 
o
r
 
l
e
s
s
 
i
n
d
e
p
e
n
d
e
n
t
 
o
f
 
t
h
e
 
p
o
s
i
t
i
o
n
 
o
n
 
t
h
e
 
m
e
d
i
u
m
.
 
T
h
i
s
 
m
a
y
 
o
r
 
m
a
y


 
 
 
 
 
 
 
 
n
o
t
 
b
e
 
s
u
p
p
o
r
t
e
d
 
b
y
 
a
 
p
a
r
t
i
c
u
l
a
r
 
d
r
i
v
e
,
 
a
n
d
 
i
s
 
s
i
l
e
n
t
l
y
 
i
g
n
o
r
e
d
 
i
n
 
t
h
e


 
 
 
 
 
 
 
 
l
a
t
t
e
r
 
c
a
s
e
.
 
A
t
 
t
h
e
 
m
o
m
e
n
t
 
o
n
l
y
 
h
a
r
d
 
d
i
s
k
s
 
(
w
h
i
c
h
 
i
s
 
a
 
m
i
s
n
o
m
e
r
 
i
n
 
t
h
i
s


 
 
 
 
 
 
 
 
c
o
n
t
e
x
t
)
 
a
c
c
e
p
t
 
t
h
i
s
 
s
e
t
t
i
n
g
.
 
C
h
a
n
g
i
n
g
 
t
h
e
 
s
e
t
t
i
n
g
 
w
h
i
l
e
 
t
h
e
 
V
M
 
i
s


 
 
 
 
 
 
 
 
r
u
n
n
i
n
g
 
i
s
 
f
o
r
b
i
d
d
e
n
.
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t
 
a
l
r
e
a
d
y
 
e
x
i
s
t
;
 
s
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
 
f
o
r
 
h
o
w
 
t
o
 
a
t
t
a
c
h
 
a
 
n
e
w
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
a
n
d


 
 
 
 
 
 
 
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
n
o
n
_
r
o
t
a
t
i
o
n
a
l
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
v
a
l
u
e
 
f
o
r
 
t
h
e
 
n
o
n
-
r
o
t
a
t
i
o
n
a
l
 
d
e
v
i
c
e
 
f
l
a
g
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
m
o
d
i
f
y
 
a
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
n
o
n
R
o
t
a
t
i
o
n
a
l
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
n
o
n
_
r
o
t
a
t
i
o
n
a
l
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
a
u
t
o
_
d
i
s
c
a
r
d
_
f
o
r
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
d
i
s
c
a
r
d
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
a
 
f
l
a
g
 
i
n
 
t
h
e
 
d
e
v
i
c
e
 
i
n
f
o
r
m
a
t
i
o
n
 
w
h
i
c
h
 
i
n
d
i
c
a
t
e
s
 
t
h
a
t
 
t
h
e
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 
s
u
p
p
o
r
t
s
 
d
i
s
c
a
r
d
i
n
g
 
u
n
s
u
s
e
d
 
b
l
o
c
k
s
 
(
c
a
l
l
e
d
 
t
r
i
m
m
i
n
g
 
f
o
r
 
S
A
T
A
 
o
r
 
u
n
m
a
p


 
 
 
 
 
 
 
 
f
o
r
 
S
C
S
I
 
d
e
v
i
c
e
s
)
 
.
T
h
i
s
 
m
a
y
 
o
r
 
m
a
y
 
n
o
t
 
b
e
 
s
u
p
p
o
r
t
e
d
 
b
y
 
a
 
p
a
r
t
i
c
u
l
a
r
 
d
r
i
v
e
,


 
 
 
 
 
 
 
 
a
n
d
 
i
s
 
s
i
l
e
n
t
l
y
 
i
g
n
o
r
e
d
 
i
n
 
t
h
e
 
l
a
t
t
e
r
 
c
a
s
e
.
 
A
t
 
t
h
e
 
m
o
m
e
n
t
 
o
n
l
y
 
h
a
r
d
 
d
i
s
k
s


 
 
 
 
 
 
 
 
(
w
h
i
c
h
 
i
s
 
a
 
m
i
s
n
o
m
e
r
 
i
n
 
t
h
i
s
 
c
o
n
t
e
x
t
)
 
a
c
c
e
p
t
 
t
h
i
s
 
s
e
t
t
i
n
g
.
 
C
h
a
n
g
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
 
w
h
i
l
e
 
t
h
e
 
V
M
 
i
s
 
r
u
n
n
i
n
g
 
i
s
 
f
o
r
b
i
d
d
e
n
.
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t
 
a
l
r
e
a
d
y


 
 
 
 
 
 
 
 
e
x
i
s
t
;
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
 
f
o
r
 
h
o
w
 
t
o
 
a
t
t
a
c
h
 
a
 
n
e
w


 
 
 
 
 
 
 
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
a
n
d


 
 
 
 
 
 
 
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
d
i
s
c
a
r
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
v
a
l
u
e
 
f
o
r
 
t
h
e
 
d
i
s
c
a
r
d
 
d
e
v
i
c
e
 
f
l
a
g
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
S
C
S
I
 
p
o
r
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
m
o
d
i
f
y
 
a
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
A
u
t
o
D
i
s
c
a
r
d
F
o
r
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
d
i
s
c
a
r
d
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
b
a
n
d
w
i
d
t
h
_
g
r
o
u
p
_
f
o
r
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
b
a
n
d
w
i
d
t
h
_
g
r
o
u
p
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
t
h
e
 
b
a
n
d
w
i
d
t
h
 
g
r
o
u
p
 
o
f
 
a
n
 
e
x
i
s
t
i
n
g
 
s
t
o
r
a
g
e
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t
 
a
l
r
e
a
d
y
 
e
x
i
s
t
;
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>


 
 
 
 
 
 
 
 
f
o
r
 
h
o
w
 
t
o
 
a
t
t
a
c
h
 
a
 
n
e
w
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
a
n
d


 
 
 
 
 
 
 
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
b
a
n
d
w
i
d
t
h
_
g
r
o
u
p
 
o
f
 
t
y
p
e
 
I
B
a
n
d
w
i
d
t
h
G
r
o
u
p


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
v
a
l
u
e
 
f
o
r
 
t
h
e
 
b
a
n
d
w
i
d
t
h
 
g
r
o
u
p
 
o
r
 
@
c
 
n
u
l
l
 
f
o
r
 
n
o
 
g
r
o
u
p
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
m
o
d
i
f
y
 
a
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
B
a
n
d
w
i
d
t
h
G
r
o
u
p
F
o
r
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
b
a
n
d
w
i
d
t
h
_
g
r
o
u
p
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
n
o
_
b
a
n
d
w
i
d
t
h
_
g
r
o
u
p
_
f
o
r
_
d
e
v
i
c
e
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
n
o
 
b
a
n
d
w
i
d
t
h
 
g
r
o
u
p
 
f
o
r
 
a
n
 
e
x
i
s
t
i
n
g
 
s
t
o
r
a
g
e
 
d
e
v
i
c
e
.


 
 
 
 
 
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t
 
a
l
r
e
a
d
y
 
e
x
i
s
t
;
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>


 
 
 
 
 
 
f
o
r
 
h
o
w
 
t
o
 
a
t
t
a
c
h
 
a
 
n
e
w
 
d
e
v
i
c
e
.


 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
a
n
d


 
 
 
 
 
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
p
o
r
t
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
m
o
d
i
f
y
 
a
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
N
o
B
a
n
d
w
i
d
t
h
G
r
o
u
p
F
o
r
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
u
n
m
o
u
n
t
_
m
e
d
i
u
m
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
f
o
r
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
U
n
m
o
u
n
t
s
 
a
n
y
 
c
u
r
r
e
n
t
l
y
 
m
o
u
n
t
e
d
 
m
e
d
i
u
m
 
(
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
,


 
 
 
 
 
 
 
 
 
 
 
 
i
d
e
n
t
i
f
i
e
d
 
b
y
 
t
h
e
 
g
i
v
e
n
 
U
U
I
D
 
@
a
 
i
d
)
 
t
o
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 
 
 
 
 
(
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
"
/
>
,
 
i
d
e
n
t
i
f
i
e
d
 
b
y
 
@
a
 
n
a
m
e
)
,


 
 
 
 
 
 
 
 
 
 
 
 
a
t
 
t
h
e
 
i
n
d
i
c
a
t
e
d
 
p
o
r
t
 
a
n
d
 
d
e
v
i
c
e
.
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t
 
a
l
r
e
a
d
y
 
e
x
i
s
t
;




 
 
 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
i
n
t
e
n
d
e
d
 
o
n
l
y
 
f
o
r
 
m
a
n
a
g
i
n
g
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
,
 
w
h
e
r
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
i
s
 
f
i
x
e
d
 
b
u
t
 
m
e
d
i
a
 
i
s
 
c
h
a
n
g
e
a
b
l
e
 
a
t
 
r
u
n
t
i
m
e
 
(
s
u
c
h
 
a
s
 
D
V
D
s


 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
f
l
o
p
p
i
e
s
)
.
 
I
t
 
c
a
n
n
o
t
 
b
e
 
u
s
e
d
 
f
o
r
 
f
i
x
e
d
 
m
e
d
i
a
 
s
u
c
h
 
a
s
 
h
a
r
d
 
d
i
s
k
s
.




 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t


 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
d
e
v
i
c
e
 
s
l
o
t
 
m
u
s
t
 
h
a
v
e
 
a
 
m
e
d
i
u
m
 
m
o
u
n
t
e
d
,
 
w
h
i
c
h
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
 
 
 
 
u
n
m
o
u
n
t
e
d
.
 
I
f
 
t
h
e
r
e
 
i
s
 
n
o
 
m
o
u
n
t
e
d
 
m
e
d
i
u
m
 
i
t
 
w
i
l
l
 
d
o
 
n
o
t
h
i
n
g
.


 
 
 
 
 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
 
f
o
r
 
m
o
r
e
 
d
e
t
a
i
l
e
d
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t


 
 
 
 
 
 
 
 
 
 
 
 
a
t
t
a
c
h
i
n
g
/
u
n
m
o
u
n
t
i
n
g
 
m
e
d
i
a
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
o
 
u
n
m
o
u
n
t
 
t
h
e
 
m
e
d
i
u
m
 
f
r
o
m
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
r
t
 
t
o
 
u
n
m
o
u
n
t
 
t
h
e
 
m
e
d
i
u
m
 
f
r
o
m
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
t
o
 
u
n
m
o
u
n
t
 
t
h
e
 
m
e
d
i
u
m
 
f
r
o
m
.




 
 
 
 
 
 
 
 
i
n
 
f
o
r
c
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
A
l
l
o
w
s
 
t
o
 
f
o
r
c
e
 
u
n
m
o
u
n
t
 
o
f
 
a
 
m
e
d
i
u
m
 
w
h
i
c
h
 
i
s
 
l
o
c
k
e
d
 
b
y


 
 
 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
m
e
d
i
u
m
 
i
s
 
a
t
t
a
c
h
e
d
 
t
o
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
u
n
m
o
u
n
t
 
m
e
d
i
u
m
 
t
h
a
t
 
i
s
 
n
o
t
 
r
e
m
o
v
e
a
b
l
e
 
-
 
n
o
t
 
d
v
d
 
o
r
 
f
l
o
p
p
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
a
l
r
e
a
d
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
o
r
 
a
n
o
t
h
e
r
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
n
o
t
 
a
t
t
a
c
h
e
d
 
t
o
 
s
p
e
c
i
f
i
e
d
 
p
o
r
t
,
 
d
e
v
i
c
e
,
 
c
o
n
t
r
o
l
l
e
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
u
n
m
o
u
n
t
M
e
d
i
u
m
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
f
o
r
c
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
m
o
u
n
t
_
m
e
d
i
u
m
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
m
e
d
i
u
m
,
 
f
o
r
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
M
o
u
n
t
s
 
a
 
m
e
d
i
u
m
 
(
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
,
 
i
d
e
n
t
i
f
i
e
d


 
 
 
 
 
 
 
 
b
y
 
t
h
e
 
g
i
v
e
n
 
U
U
I
D
 
@
a
 
i
d
)
 
t
o
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 
(
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
"
/
>
,
 
i
d
e
n
t
i
f
i
e
d
 
b
y
 
@
a
 
n
a
m
e
)
,


 
 
 
 
 
 
 
 
a
t
 
t
h
e
 
i
n
d
i
c
a
t
e
d
 
p
o
r
t
 
a
n
d
 
d
e
v
i
c
e
.
 
T
h
e
 
d
e
v
i
c
e
 
m
u
s
t
 
a
l
r
e
a
d
y
 
e
x
i
s
t
;


 
 
 
 
 
 
 
 
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
 
f
o
r
 
h
o
w
 
t
o
 
a
t
t
a
c
h
 
a
 
n
e
w
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
i
n
t
e
n
d
e
d
 
o
n
l
y
 
f
o
r
 
m
a
n
a
g
i
n
g
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
,
 
w
h
e
r
e
 
t
h
e


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
i
s
 
f
i
x
e
d
 
b
u
t
 
m
e
d
i
a
 
i
s
 
c
h
a
n
g
e
a
b
l
e
 
a
t
 
r
u
n
t
i
m
e
 
(
s
u
c
h
 
a
s
 
D
V
D
s


 
 
 
 
 
 
 
 
a
n
d
 
f
l
o
p
p
i
e
s
)
.
 
I
t
 
c
a
n
n
o
t
 
b
e
 
u
s
e
d
 
f
o
r
 
f
i
x
e
d
 
m
e
d
i
a
 
s
u
c
h
 
a
s
 
h
a
r
d
 
d
i
s
k
s
.




 
 
 
 
 
 
 
 
T
h
e
 
@
a
 
c
o
n
t
r
o
l
l
e
r
P
o
r
t
 
a
n
d
 
@
a
 
d
e
v
i
c
e
 
p
a
r
a
m
e
t
e
r
s
 
s
p
e
c
i
f
y
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
a
n
d


 
 
 
 
 
 
 
 
h
a
v
e
 
h
a
v
e
 
t
h
e
 
s
a
m
e
 
m
e
a
n
i
n
g
 
a
s
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
.




 
 
 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
d
e
v
i
c
e
 
s
l
o
t
 
c
a
n
 
h
a
v
e
 
a
 
m
e
d
i
u
m
 
m
o
u
n
t
e
d
,
 
w
h
i
c
h
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
u
n
m
o
u
n
t
e
d
 
f
i
r
s
t
.
 
S
p
e
c
i
f
y
i
n
g
 
a
 
z
e
r
o
 
U
U
I
D
 
(
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
)
 
f
o
r


 
 
 
 
 
 
 
 
@
a
 
m
e
d
i
u
m
 
d
o
e
s
 
j
u
s
t
 
a
n
 
u
n
m
o
u
n
t
.




 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
 
f
o
r
 
m
o
r
e
 
d
e
t
a
i
l
e
d
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t


 
 
 
 
 
 
 
 
a
t
t
a
c
h
i
n
g
 
m
e
d
i
a
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
m
e
d
i
u
m
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
r
t
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
m
e
d
i
u
m
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
m
e
d
i
u
m
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
m
e
d
i
u
m
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
t
o
 
m
o
u
n
t
 
o
r
 
@
c
 
n
u
l
l
 
f
o
r
 
a
n
 
e
m
p
t
y
 
d
r
i
v
e
.




 
 
 
 
 
 
 
 
i
n
 
f
o
r
c
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
A
l
l
o
w
s
 
t
o
 
f
o
r
c
e
 
u
n
m
o
u
n
t
/
m
o
u
n
t
 
o
f
 
a
 
m
e
d
i
u
m
 
w
h
i
c
h
 
i
s
 
l
o
c
k
e
d
 
b
y


 
 
 
 
 
 
 
 
 
 
t
h
e
 
d
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
t
o
 
a
t
t
a
c
h
 
t
h
e
 
m
e
d
i
u
m
 
t
o
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
S
A
T
A
 
d
e
v
i
c
e
,
 
S
A
T
A
 
p
o
r
t
,
 
I
D
E
 
p
o
r
t
 
o
r
 
I
D
E
 
s
l
o
t
 
o
u
t
 
o
f
 
r
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
e
m
p
t
 
t
o
 
a
t
t
a
c
h
 
m
e
d
i
u
m
 
t
o
 
a
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
m
a
c
h
i
n
e
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
a
l
r
e
a
d
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
o
r
 
a
n
o
t
h
e
r
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
m
o
u
n
t
M
e
d
i
u
m
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
,
 
m
e
d
i
u
m
,
 
f
o
r
c
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
e
d
i
u
m
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
v
i
r
t
u
a
l
 
m
e
d
i
u
m
 
a
t
t
a
c
h
e
d
 
t
o
 
a
 
d
e
v
i
c
e
 
s
l
o
t
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d


 
 
 
 
 
 
 
 
b
u
s
.




 
 
 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
i
f
 
t
h
e
 
m
e
d
i
u
m
 
w
a
s
 
i
n
d
i
r
e
c
t
l
y
 
a
t
t
a
c
h
e
d
 
b
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
m
o
u
n
t
M
e
d
i
u
m
"
/
>
 
t
o
 
t
h
e
 
g
i
v
e
n
 
d
e
v
i
c
e
 
s
l
o
t
 
t
h
e
n
 
t
h
i
s


 
 
 
 
 
 
 
 
m
e
t
h
o
d
 
w
i
l
l
 
r
e
t
u
r
n
 
n
o
t
 
t
h
e
 
s
a
m
e
 
o
b
j
e
c
t
 
a
s
 
p
a
s
s
e
d
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
m
o
u
n
t
M
e
d
i
u
m
"
/
>
 
c
a
l
l
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
 
f
o
r


 
 
 
 
 
 
 
 
m
o
r
e
 
d
e
t
a
i
l
e
d
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
m
o
u
n
t
i
n
g
 
a
 
m
e
d
i
u
m
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
h
e
 
m
e
d
i
u
m
 
i
s
 
a
t
t
a
c
h
e
d
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
r
t
 
t
o
 
q
u
e
r
y
.




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
v
i
c
e
 
s
l
o
t
 
i
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
t
o
 
q
u
e
r
y
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
A
t
t
a
c
h
e
d
 
m
e
d
i
u
m
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
N
o
 
m
e
d
i
u
m
 
a
t
t
a
c
h
e
d
 
t
o
 
g
i
v
e
n
 
s
l
o
t
/
b
u
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
e
d
i
u
m
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
e
d
i
u
m
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
s
_
o
f
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
n
 
a
r
r
a
y
 
o
f
 
m
e
d
i
u
m
 
a
t
t
a
c
h
m
e
n
t
s
 
w
h
i
c
h
 
a
r
e
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
t
h
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
s
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
A
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
g
i
v
e
n
 
n
a
m
e
 
d
o
e
s
n
'
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
s
O
f
C
o
n
t
r
o
l
l
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
e
d
i
u
m
_
a
t
t
a
c
h
m
e
n
t
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
m
e
d
i
u
m
 
a
t
t
a
c
h
m
e
n
t
 
w
h
i
c
h
 
c
o
r
r
e
s
p
o
n
d
s
 
t
o
 
t
h
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h


 
 
 
 
 
 
 
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
,
 
o
n
 
t
h
e
 
g
i
v
e
n
 
p
o
r
t
 
a
n
d
 
d
e
v
i
c
e
 
s
l
o
t
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
i
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
t
t
a
c
h
m
e
n
t
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
N
o
 
a
t
t
a
c
h
m
e
n
t
 
e
x
i
s
t
s
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
c
o
n
t
r
o
l
l
e
r
/
p
o
r
t
/
d
e
v
i
c
e
 
c
o
m
b
i
n
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
t
r
o
l
l
e
r
_
p
o
r
t
,
 
d
e
v
i
c
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
t
t
a
c
h
m
e
n
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
t
t
a
c
h
_
h
o
s
t
_
p
c
i
_
d
e
v
i
c
e
(
s
e
l
f
,
 
h
o
s
t
_
a
d
d
r
e
s
s
,
 
d
e
s
i
r
e
d
_
g
u
e
s
t
_
a
d
d
r
e
s
s
,
 
t
r
y
_
t
o
_
u
n
b
i
n
d
)
:


 
 
 
 
 
 
 
 
"
"
"
A
t
t
a
c
h
e
s
 
h
o
s
t
 
P
C
I
 
d
e
v
i
c
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
(
h
o
s
t
)
 
P
C
I
 
a
d
d
r
e
s
s
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
P
C
I
 
b
u
s
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.
 
P
l
e
a
s
e
 
n
o
t
e
,
 
t
h
a
t
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n


 
 
 
 
 
 
 
 
i
s
 
t
w
o
 
p
h
a
s
e
,
 
a
s
 
r
e
a
l
 
a
t
t
a
c
h
m
e
n
t
 
w
i
l
l
 
h
a
p
p
e
n
 
w
h
e
n
 
V
M
 
w
i
l
l
 
s
t
a
r
t
,


 
 
 
 
 
 
 
 
a
n
d
 
m
o
s
t
 
i
n
f
o
r
m
a
t
i
o
n
 
w
i
l
l
 
b
e
 
d
e
l
i
v
e
r
e
d
 
a
s
 
I
H
o
s
t
P
C
I
D
e
v
i
c
e
P
l
u
g
E
v
e
n
t


 
 
 
 
 
 
 
 
o
n
 
I
V
i
r
t
u
a
l
B
o
x
 
e
v
e
n
t
 
s
o
u
r
c
e
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
P
C
I
D
e
v
i
c
e
P
l
u
g
E
v
e
n
t
"
/
>




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
A
d
d
r
e
s
s
 
o
f
 
t
h
e
 
h
o
s
t
 
P
C
I
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
i
n
 
d
e
s
i
r
e
d
_
g
u
e
s
t
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
D
e
s
i
r
e
d
 
p
o
s
i
t
i
o
n
 
o
f
 
t
h
i
s
 
d
e
v
i
c
e
 
o
n
 
g
u
e
s
t
 
P
C
I
 
b
u
s
.




 
 
 
 
 
 
 
 
i
n
 
t
r
y
_
t
o
_
u
n
b
i
n
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
I
f
 
V
M
M
 
s
h
a
l
l
 
t
r
y
 
t
o
 
u
n
b
i
n
d
 
e
x
i
s
t
i
n
g
 
d
r
i
v
e
r
s
 
f
r
o
m
 
t
h
e


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
b
e
f
o
r
e
 
a
t
t
a
c
h
i
n
g
 
i
t
 
t
o
 
t
h
e
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
i
s
 
n
o
t
 
s
t
o
p
p
e
d
 
(
P
C
I
 
h
o
t
p
l
u
g
 
n
o
t
 
y
e
t
 
i
m
p
l
e
m
e
n
t
e
d
)
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
d
o
e
s
 
n
o
t
 
h
a
v
e
 
a
 
P
C
I
 
c
o
n
t
r
o
l
l
e
r
 
a
l
l
o
w
i
n
g
 
a
t
t
a
c
h
m
e
n
t
 
o
f
 
p
h
y
s
i
c
a
l
 
d
e
v
i
c
e
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
N
O
T
_
S
U
P
P
O
R
T
E
D


 
 
 
 
 
 
 
 
 
 
 
 
H
a
r
d
w
a
r
e
 
o
r
 
h
o
s
t
 
O
S
 
d
o
e
s
n
'
t
 
a
l
l
o
w
 
P
C
I
 
d
e
v
i
c
e
 
p
a
s
s
t
h
r
o
u
g
h
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
t
t
a
c
h
H
o
s
t
P
C
I
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
h
o
s
t
_
a
d
d
r
e
s
s
,
 
d
e
s
i
r
e
d
_
g
u
e
s
t
_
a
d
d
r
e
s
s
,
 
t
r
y
_
t
o
_
u
n
b
i
n
d
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
t
a
c
h
_
h
o
s
t
_
p
c
i
_
d
e
v
i
c
e
(
s
e
l
f
,
 
h
o
s
t
_
a
d
d
r
e
s
s
)
:


 
 
 
 
 
 
 
 
"
"
"
D
e
t
a
c
h
 
h
o
s
t
 
P
C
I
 
d
e
v
i
c
e
 
f
r
o
m
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
A
l
s
o
 
H
o
s
t
P
C
I
D
e
v
i
c
e
P
l
u
g
E
v
e
n
t
 
o
n
 
I
V
i
r
t
u
a
l
B
o
x
 
e
v
e
n
t
 
s
o
u
r
c
e


 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
d
e
l
i
v
e
r
e
d
.
 
A
s
 
c
u
r
r
e
n
t
l
y
 
w
e
 
d
o
n
'
t
 
s
u
p
p
o
r
t
 
h
o
t
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 
u
n
p
l
u
g
,
 
I
H
o
s
t
P
C
I
D
e
v
i
c
e
P
l
u
g
E
v
e
n
t
 
e
v
e
n
t
 
i
s
 
d
e
l
i
v
e
r
e
d
 
i
m
m
e
d
i
a
t
e
l
y
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
P
C
I
D
e
v
i
c
e
P
l
u
g
E
v
e
n
t
"
/
>




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
A
d
d
r
e
s
s
 
o
f
 
t
h
e
 
h
o
s
t
 
P
C
I
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
i
s
 
n
o
t
 
s
t
o
p
p
e
d
 
(
P
C
I
 
h
o
t
p
l
u
g
 
n
o
t
 
y
e
t
 
i
m
p
l
e
m
e
n
t
e
d
)
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
h
o
s
t
 
d
e
v
i
c
e
 
i
s
 
n
o
t
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
d
o
e
s
 
n
o
t
 
h
a
v
e
 
a
 
P
C
I
 
c
o
n
t
r
o
l
l
e
r
 
a
l
l
o
w
i
n
g
 
a
t
t
a
c
h
m
e
n
t
 
o
f
 
p
h
y
s
i
c
a
l
 
d
e
v
i
c
e
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
N
O
T
_
S
U
P
P
O
R
T
E
D


 
 
 
 
 
 
 
 
 
 
 
 
H
a
r
d
w
a
r
e
 
o
r
 
h
o
s
t
 
O
S
 
d
o
e
s
n
'
t
 
a
l
l
o
w
 
P
C
I
 
d
e
v
i
c
e
 
p
a
s
s
t
h
r
o
u
g
h
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
t
a
c
h
H
o
s
t
P
C
I
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
h
o
s
t
_
a
d
d
r
e
s
s
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
(
s
e
l
f
,
 
s
l
o
t
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
s
l
o
t
.


 
 
 
 
 
 
 
 
S
l
o
t
s
 
a
r
e
 
n
u
m
b
e
r
e
d
 
s
e
q
u
e
n
t
i
a
l
l
y
,
 
s
t
a
r
t
i
n
g
 
w
i
t
h
 
z
e
r
o
.
 
T
h
e
 
t
o
t
a
l


 
 
 
 
 
 
 
 
n
u
m
b
e
r
 
o
f
 
a
d
a
p
t
e
r
s
 
p
e
r
 
m
a
c
h
i
n
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
g
e
t
M
a
x
N
e
t
w
o
r
k
A
d
a
p
t
e
r
s
"
/
>
 
p
r
o
p
e
r
t
y
,


 
 
 
 
 
 
 
 
s
o
 
t
h
e
 
m
a
x
i
m
u
m
 
s
l
o
t
 
n
u
m
b
e
r
 
i
s
 
o
n
e
 
l
e
s
s
 
t
h
a
n
 
t
h
a
t
 
p
r
o
p
e
r
t
y
'
s
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
i
n
 
s
l
o
t
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
d
a
p
t
e
r
 
o
f
 
t
y
p
e
 
I
N
e
t
w
o
r
k
A
d
a
p
t
e
r




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
@
a
 
s
l
o
t
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
a
d
a
p
t
e
r
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
N
e
t
w
o
r
k
A
d
a
p
t
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
l
o
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
N
e
t
w
o
r
k
A
d
a
p
t
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
d
a
p
t
e
r


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
d
d
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
,
 
n
a
m
e
,
 
c
o
n
n
e
c
t
i
o
n
_
t
y
p
e
)
:


 
 
 
 
 
 
 
 
"
"
"
A
d
d
s
 
a
 
n
e
w
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
(
S
C
S
I
,
 
S
A
S
 
o
r
 
S
A
T
A
 
c
o
n
t
r
o
l
l
e
r
)
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
a
n
d
 
r
e
t
u
r
n
s
 
i
t
 
a
s
 
a
n
 
i
n
s
t
a
n
c
e
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
"
/
>
.




 
 
 
 
 
 
 
 
@
a
 
n
a
m
e
 
i
d
e
n
t
i
f
i
e
s
 
t
h
e
 
c
o
n
t
r
o
l
l
e
r
 
f
o
r
 
s
u
b
s
e
q
u
e
n
t
 
c
a
l
l
s
 
s
u
c
h
 
a
s


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
B
y
N
a
m
e
"
/
>
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
g
e
t
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
B
y
I
n
s
t
a
n
c
e
"
/
>
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
r
e
m
o
v
e
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
"
/
>
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
a
t
t
a
c
h
D
e
v
i
c
e
"
/
>
 
o
r
 
<
l
i
n
k
 
t
o
=
"
#
m
o
u
n
t
M
e
d
i
u
m
"
/
>
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
e
 
c
o
n
t
r
o
l
l
e
r
 
h
a
s
 
b
e
e
n
 
a
d
d
e
d
,
 
y
o
u
 
c
a
n
 
s
e
t
 
i
t
s
 
e
x
a
c
t


 
 
 
 
 
 
 
 
t
y
p
e
 
b
y
 
s
e
t
t
i
n
g
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
:
:
c
o
n
t
r
o
l
l
e
r
T
y
p
e
"
/
>
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
i
n
 
c
o
n
n
e
c
t
i
o
n
_
t
y
p
e
 
o
f
 
t
y
p
e
 
S
t
o
r
a
g
e
B
u
s




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
o
n
t
r
o
l
l
e
r
 
o
f
 
t
y
p
e
 
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E


 
 
 
 
 
 
 
 
 
 
 
 
A
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
g
i
v
e
n
 
n
a
m
e
 
e
x
i
s
t
s
 
a
l
r
e
a
d
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
@
a
 
c
o
n
t
r
o
l
l
e
r
T
y
p
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
c
o
n
t
r
o
l
l
e
r
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
d
d
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
c
o
n
n
e
c
t
i
o
n
_
t
y
p
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
_
b
y
_
n
a
m
e
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
 
o
f
 
t
y
p
e
 
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
A
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
g
i
v
e
n
 
n
a
m
e
 
d
o
e
s
n
'
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
B
y
N
a
m
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
_
b
y
_
i
n
s
t
a
n
c
e
(
s
e
l
f
,
 
i
n
s
t
a
n
c
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
i
n
s
t
a
n
c
e
 
n
u
m
b
e
r
.




 
 
 
 
 
 
 
 
i
n
 
i
n
s
t
a
n
c
e
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
 
o
f
 
t
y
p
e
 
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
A
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
g
i
v
e
n
 
i
n
s
t
a
n
c
e
 
n
u
m
b
e
r
 
d
o
e
s
n
'
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
B
y
I
n
s
t
a
n
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
n
s
t
a
n
c
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
a
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
t
h
 
a
l
l
 
d
e
v
i
c
e
s
 
a
t
t
a
c
h
e
d
 
t
o
 
i
t
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
A
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
g
i
v
e
n
 
n
a
m
e
 
d
o
e
s
n
'
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
N
O
T
_
S
U
P
P
O
R
T
E
D


 
 
 
 
 
 
 
 
 
 
 
 
M
e
d
i
u
m
 
f
o
r
m
a
t
 
d
o
e
s
 
n
o
t
 
s
u
p
p
o
r
t
 
s
t
o
r
a
g
e
 
d
e
l
e
t
i
o
n
 
(
o
n
l
y
 
f
o
r
 
i
m
p
l
i
c
i
t
l
y


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
,
 
s
h
o
u
l
d
 
n
o
t
 
h
a
p
p
e
n
)
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
_
b
o
o
t
a
b
l
e
(
s
e
l
f
,
 
n
a
m
e
,
 
b
o
o
t
a
b
l
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
t
h
e
 
b
o
o
t
a
b
l
e
 
f
l
a
g
 
o
f
 
t
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r




 
 
 
 
 
 
 
 
i
n
 
b
o
o
t
a
b
l
e
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
A
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
w
i
t
h
 
g
i
v
e
n
 
n
a
m
e
 
d
o
e
s
n
'
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E


 
 
 
 
 
 
 
 
 
 
 
 
A
n
o
t
h
e
r
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
i
s
 
m
a
r
k
e
d
 
a
s
 
b
o
o
t
a
b
l
e
 
a
l
r
e
a
d
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
B
o
o
t
a
b
l
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
b
o
o
t
a
b
l
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
s
e
r
i
a
l
_
p
o
r
t
(
s
e
l
f
,
 
s
l
o
t
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
s
e
r
i
a
l
 
p
o
r
t
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
s
l
o
t
.


 
 
 
 
 
 
 
 
S
l
o
t
s
 
a
r
e
 
n
u
m
b
e
r
e
d
 
s
e
q
u
e
n
t
i
a
l
l
y
,
 
s
t
a
r
t
i
n
g
 
w
i
t
h
 
z
e
r
o
.
 
T
h
e
 
t
o
t
a
l


 
 
 
 
 
 
 
 
n
u
m
b
e
r
 
o
f
 
s
e
r
i
a
l
 
p
o
r
t
s
 
p
e
r
 
m
a
c
h
i
n
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
s
e
r
i
a
l
P
o
r
t
C
o
u
n
t
"
/
>
 
p
r
o
p
e
r
t
y
,


 
 
 
 
 
 
 
 
s
o
 
t
h
e
 
m
a
x
i
m
u
m
 
s
l
o
t
 
n
u
m
b
e
r
 
i
s
 
o
n
e
 
l
e
s
s
 
t
h
a
n
 
t
h
a
t
 
p
r
o
p
e
r
t
y
'
s
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
i
n
 
s
l
o
t
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
o
r
t
 
o
f
 
t
y
p
e
 
I
S
e
r
i
a
l
P
o
r
t




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
@
a
 
s
l
o
t
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
o
r
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
S
e
r
i
a
l
P
o
r
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
l
o
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
S
e
r
i
a
l
P
o
r
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
o
r
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
p
a
r
a
l
l
e
l
_
p
o
r
t
(
s
e
l
f
,
 
s
l
o
t
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
p
a
r
a
l
l
e
l
 
p
o
r
t
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
s
l
o
t
.


 
 
 
 
 
 
 
 
S
l
o
t
s
 
a
r
e
 
n
u
m
b
e
r
e
d
 
s
e
q
u
e
n
t
i
a
l
l
y
,
 
s
t
a
r
t
i
n
g
 
w
i
t
h
 
z
e
r
o
.
 
T
h
e
 
t
o
t
a
l


 
 
 
 
 
 
 
 
n
u
m
b
e
r
 
o
f
 
p
a
r
a
l
l
e
l
 
p
o
r
t
s
 
p
e
r
 
m
a
c
h
i
n
e
 
i
s
 
d
e
f
i
n
e
d
 
b
y
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
p
a
r
a
l
l
e
l
P
o
r
t
C
o
u
n
t
"
/
>
 
p
r
o
p
e
r
t
y
,


 
 
 
 
 
 
 
 
s
o
 
t
h
e
 
m
a
x
i
m
u
m
 
s
l
o
t
 
n
u
m
b
e
r
 
i
s
 
o
n
e
 
l
e
s
s
 
t
h
a
n
 
t
h
a
t
 
p
r
o
p
e
r
t
y
'
s
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
i
n
 
s
l
o
t
 
o
f
 
t
y
p
e
 
i
n
t




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
o
r
t
 
o
f
 
t
y
p
e
 
I
P
a
r
a
l
l
e
l
P
o
r
t




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
@
a
 
s
l
o
t
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
o
r
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
P
a
r
a
l
l
e
l
P
o
r
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
l
o
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
a
r
a
l
l
e
l
P
o
r
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
o
r
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
e
x
t
r
a
_
d
a
t
a
_
k
e
y
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
n
 
a
r
r
a
y
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
m
a
c
h
i
n
e
-
s
p
e
c
i
f
i
c
 
e
x
t
r
a
 
d
a
t
a
 
k
e
y
s


 
 
 
 
 
 
 
 
 
 
 
 
w
h
i
c
h
 
c
u
r
r
e
n
t
l
y
 
h
a
v
e
 
v
a
l
u
e
s
 
d
e
f
i
n
e
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
k
e
y
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
e
x
t
r
a
 
d
a
t
a
 
k
e
y
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
k
e
y
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
E
x
t
r
a
D
a
t
a
K
e
y
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
k
e
y
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
e
x
t
r
a
_
d
a
t
a
(
s
e
l
f
,
 
k
e
y
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
s
s
o
c
i
a
t
e
d
 
m
a
c
h
i
n
e
-
s
p
e
c
i
f
i
c
 
e
x
t
r
a
 
d
a
t
a
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
r
e
q
u
e
s
t
e
d
 
d
a
t
a
 
@
a
 
k
e
y
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
,
 
t
h
i
s
 
f
u
n
c
t
i
o
n
 
w
i
l
l


 
 
 
 
 
 
 
 
s
u
c
c
e
e
d
 
a
n
d
 
r
e
t
u
r
n
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
n
 
t
h
e
 
@
a
 
v
a
l
u
e
 
a
r
g
u
m
e
n
t
.




 
 
 
 
 
 
 
 
i
n
 
k
e
y
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
d
a
t
a
 
k
e
y
 
t
o
 
g
e
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
V
a
l
u
e
 
o
f
 
t
h
e
 
r
e
q
u
e
s
t
e
d
 
d
a
t
a
 
k
e
y
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
E
x
t
r
a
D
a
t
a
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
k
e
y
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
e
x
t
r
a
_
d
a
t
a
(
s
e
l
f
,
 
k
e
y
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
a
s
s
o
c
i
a
t
e
d
 
m
a
c
h
i
n
e
-
s
p
e
c
i
f
i
c
 
e
x
t
r
a
 
d
a
t
a
.




 
 
 
 
 
 
 
 
I
f
 
y
o
u
 
p
a
s
s
 
@
c
 
n
u
l
l
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
a
s
 
a
 
k
e
y
 
@
a
 
v
a
l
u
e
,
 
t
h
e
 
g
i
v
e
n


 
 
 
 
 
 
 
 
@
a
 
k
e
y
 
w
i
l
l
 
b
e
 
d
e
l
e
t
e
d
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
B
e
f
o
r
e
 
p
e
r
f
o
r
m
i
n
g
 
t
h
e
 
a
c
t
u
a
l
 
d
a
t
a
 
c
h
a
n
g
e
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
a
s
k
 
a
l
l


 
 
 
 
 
 
 
 
 
 
r
e
g
i
s
t
e
r
e
d
 
l
i
s
t
e
n
e
r
s
 
u
s
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
E
x
t
r
a
D
a
t
a
C
a
n
C
h
a
n
g
e
E
v
e
n
t
"
/
>


 
 
 
 
 
 
 
 
 
 
n
o
t
i
f
i
c
a
t
i
o
n
 
f
o
r
 
a
 
p
e
r
m
i
s
s
i
o
n
.
 
I
f
 
o
n
e
 
o
f
 
t
h
e
 
l
i
s
t
e
n
e
r
s
 
r
e
f
u
s
e
s
 
t
h
e


 
 
 
 
 
 
 
 
 
 
n
e
w
 
v
a
l
u
e
,
 
t
h
e
 
c
h
a
n
g
e
 
w
i
l
l
 
n
o
t
 
b
e
 
p
e
r
f
o
r
m
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
O
n
 
s
u
c
c
e
s
s
,
 
t
h
e


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
E
x
t
r
a
D
a
t
a
C
h
a
n
g
e
d
E
v
e
n
t
"
/
>
 
n
o
t
i
f
i
c
a
t
i
o
n


 
 
 
 
 
 
 
 
 
 
i
s
 
c
a
l
l
e
d
 
t
o
 
i
n
f
o
r
m
 
a
l
l
 
r
e
g
i
s
t
e
r
e
d
 
l
i
s
t
e
n
e
r
s
 
a
b
o
u
t
 
a
 
s
u
c
c
e
s
s
f
u
l
 
d
a
t
a


 
 
 
 
 
 
 
 
 
 
c
h
a
n
g
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
c
a
n
 
b
e
 
c
a
l
l
e
d
 
o
u
t
s
i
d
e
 
t
h
e
 
m
a
c
h
i
n
e
 
s
e
s
s
i
o
n
 
a
n
d
 
t
h
e
r
e
f
o
r
e


 
 
 
 
 
 
 
 
 
 
i
t
'
s
 
a
 
c
a
l
l
e
r
'
s
 
r
e
s
p
o
n
s
i
b
i
l
i
t
y
 
t
o
 
h
a
n
d
l
e
 
p
o
s
s
i
b
l
e
 
r
a
c
e
 
c
o
n
d
i
t
i
o
n
s


 
 
 
 
 
 
 
 
 
 
w
h
e
n
 
s
e
v
e
r
a
l
 
c
l
i
e
n
t
s
 
c
h
a
n
g
e
 
t
h
e
 
s
a
m
e
 
k
e
y
 
a
t
 
t
h
e
 
s
a
m
e
 
t
i
m
e
.




 
 
 
 
 
 
 
 
i
n
 
k
e
y
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
d
a
t
a
 
k
e
y
 
t
o
 
s
e
t
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
V
a
l
u
e
 
t
o
 
a
s
s
i
g
n
 
t
o
 
t
h
e
 
k
e
y
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
E
x
t
r
a
D
a
t
a
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
k
e
y
,
 
v
a
l
u
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
c
p
u
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
v
i
r
t
u
a
l
 
C
P
U
 
b
o
o
l
e
a
n
 
v
a
l
u
e
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
C
P
U
P
r
o
p
e
r
t
y
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
t
y
p
e
 
t
o
 
q
u
e
r
y
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
p
r
o
p
e
r
t
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
C
P
U
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
c
p
u
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
t
h
e
 
v
i
r
t
u
a
l
 
C
P
U
 
b
o
o
l
e
a
n
 
v
a
l
u
e
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
C
P
U
P
r
o
p
e
r
t
y
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
t
y
p
e
 
t
o
 
q
u
e
r
y
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
p
r
o
p
e
r
t
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
C
P
U
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
c
p
u
i
d
_
l
e
a
f
(
s
e
l
f
,
 
i
d
_
p
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
v
i
r
t
u
a
l
 
C
P
U
 
c
p
u
i
d
 
i
n
f
o
r
m
a
t
i
o
n
 
f
o
r
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
a
f
.




 
 
 
 
 
 
 
 
C
u
r
r
e
n
t
l
y
 
s
u
p
p
o
r
t
e
d
 
i
n
d
e
x
 
v
a
l
u
e
s
 
f
o
r
 
c
p
u
i
d
:


 
 
 
 
 
 
 
 
S
t
a
n
d
a
r
d
 
C
P
U
I
D
 
l
e
a
f
s
:
 
0
 
-
 
0
x
A


 
 
 
 
 
 
 
 
E
x
t
e
n
d
e
d
 
C
P
U
I
D
 
l
e
a
f
s
:
 
0
x
8
0
0
0
0
0
0
0
 
-
 
0
x
8
0
0
0
0
0
0
A




 
 
 
 
 
 
 
 
S
e
e
 
t
h
e
 
I
n
t
e
l
 
a
n
d
 
A
M
D
 
p
r
o
g
r
a
m
m
e
r
'
s
 
m
a
n
u
a
l
s
 
f
o
r
 
d
e
t
a
i
l
e
d
 
i
n
f
o
r
m
a
t
i
o
n


 
 
 
 
 
 
 
 
a
b
o
u
t
 
t
h
e
 
c
p
u
i
d
 
i
n
s
t
r
u
c
t
i
o
n
 
a
n
d
 
i
t
s
 
l
e
a
f
s
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
i
n
d
e
x
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
a
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
a
x
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
b
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
b
x
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
c
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
c
x
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
d
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
d
x
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
i
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
C
P
U
I
D
L
e
a
f
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
c
p
u
i
d
_
l
e
a
f
(
s
e
l
f
,
 
i
d
_
p
,
 
v
a
l
_
e
a
x
,
 
v
a
l
_
e
b
x
,
 
v
a
l
_
e
c
x
,
 
v
a
l
_
e
d
x
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
t
h
e
 
v
i
r
t
u
a
l
 
C
P
U
 
c
p
u
i
d
 
i
n
f
o
r
m
a
t
i
o
n
 
f
o
r
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
a
f
.
 
N
o
t
e
 
t
h
a
t
 
t
h
e
s
e
 
v
a
l
u
e
s


 
 
 
 
 
 
 
 
a
r
e
 
n
o
t
 
p
a
s
s
e
d
 
u
n
m
o
d
i
f
i
e
d
.
 
V
i
r
t
u
a
l
B
o
x
 
c
l
e
a
r
s
 
f
e
a
t
u
r
e
s
 
t
h
a
t
 
i
t
 
d
o
e
s
n
'
t
 
s
u
p
p
o
r
t
.




 
 
 
 
 
 
 
 
C
u
r
r
e
n
t
l
y
 
s
u
p
p
o
r
t
e
d
 
i
n
d
e
x
 
v
a
l
u
e
s
 
f
o
r
 
c
p
u
i
d
:


 
 
 
 
 
 
 
 
S
t
a
n
d
a
r
d
 
C
P
U
I
D
 
l
e
a
f
s
:
 
0
 
-
 
0
x
A


 
 
 
 
 
 
 
 
E
x
t
e
n
d
e
d
 
C
P
U
I
D
 
l
e
a
f
s
:
 
0
x
8
0
0
0
0
0
0
0
 
-
 
0
x
8
0
0
0
0
0
0
A




 
 
 
 
 
 
 
 
S
e
e
 
t
h
e
 
I
n
t
e
l
 
a
n
d
 
A
M
D
 
p
r
o
g
r
a
m
m
e
r
'
s
 
m
a
n
u
a
l
s
 
f
o
r
 
d
e
t
a
i
l
e
d
 
i
n
f
o
r
m
a
t
i
o
n


 
 
 
 
 
 
 
 
a
b
o
u
t
 
t
h
e
 
c
p
u
i
d
 
i
n
s
t
r
u
c
t
i
o
n
 
a
n
d
 
i
t
s
 
l
e
a
f
s
.




 
 
 
 
 
 
 
 
D
o
 
n
o
t
 
u
s
e
 
t
h
i
s
 
m
e
t
h
o
d
 
u
n
l
e
s
s
 
y
o
u
 
k
n
o
w
 
e
x
a
c
t
l
y
 
w
h
a
t
 
y
o
u
'
r
e
 
d
o
i
n
g
.
 
M
i
s
u
s
e
 
c
a
n
 
l
e
a
d
 
t
o


 
 
 
 
 
 
 
 
r
a
n
d
o
m
 
c
r
a
s
h
e
s
 
i
n
s
i
d
e
 
V
M
s
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
i
n
d
e
x
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
_
e
a
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
a
x
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
_
e
b
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
b
x
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
_
e
c
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
c
x
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
_
e
d
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
d
x
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
i
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
C
P
U
I
D
L
e
a
f
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
,
 
v
a
l
_
e
a
x
,
 
v
a
l
_
e
b
x
,
 
v
a
l
_
e
c
x
,
 
v
a
l
_
e
d
x
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
c
p
u
i
d
_
l
e
a
f
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
t
h
e
 
v
i
r
t
u
a
l
 
C
P
U
 
c
p
u
i
d
 
l
e
a
f
 
f
o
r
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
i
n
d
e
x




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
i
n
d
e
x
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
i
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
C
P
U
I
D
L
e
a
f
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
a
l
l
_
c
p
u
i
d
_
l
e
a
v
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
a
l
l
 
t
h
e
 
v
i
r
t
u
a
l
 
C
P
U
 
c
p
u
i
d
 
l
e
a
v
e
s




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
A
l
l
C
P
U
I
D
L
e
a
v
e
s
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
h
w
_
v
i
r
t
_
e
x
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
v
a
l
u
e
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
h
a
r
d
w
a
r
e
 
v
i
r
t
u
a
l
i
z
a
t
i
o
n
 
b
o
o
l
e
a
n
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
H
W
V
i
r
t
E
x
P
r
o
p
e
r
t
y
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
t
y
p
e
 
t
o
 
q
u
e
r
y
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
p
r
o
p
e
r
t
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
H
W
V
i
r
t
E
x
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
h
w
_
v
i
r
t
_
e
x
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
a
 
n
e
w
 
v
a
l
u
e
 
f
o
r
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
h
a
r
d
w
a
r
e
 
v
i
r
t
u
a
l
i
z
a
t
i
o
n
 
b
o
o
l
e
a
n
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
H
W
V
i
r
t
E
x
P
r
o
p
e
r
t
y
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
t
y
p
e
 
t
o
 
s
e
t
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
p
r
o
p
e
r
t
y
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
p
r
o
p
e
r
t
y
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
H
W
V
i
r
t
E
x
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
a
v
e
_
s
e
t
t
i
n
g
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
S
a
v
e
s
 
a
n
y
 
c
h
a
n
g
e
s
 
t
o
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
m
a
d
e
 
s
i
n
c
e
 
t
h
e
 
s
e
s
s
i
o
n


 
 
 
 
 
 
 
 
h
a
s
 
b
e
e
n
 
o
p
e
n
e
d
 
o
r
 
a
 
n
e
w
 
m
a
c
h
i
n
e
 
h
a
s
 
b
e
e
n
 
c
r
e
a
t
e
d
,
 
o
r
 
s
i
n
c
e
 
t
h
e


 
 
 
 
 
 
 
 
l
a
s
t
 
c
a
l
l
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
o
r
 
<
l
i
n
k
 
t
o
=
"
#
d
i
s
c
a
r
d
S
e
t
t
i
n
g
s
"
/
>
.


 
 
 
 
 
 
 
 
F
o
r
 
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
,
 
n
e
w
 
s
e
t
t
i
n
g
s
 
b
e
c
o
m
e
 
v
i
s
i
b
l
e
 
t
o
 
a
l
l


 
 
 
 
 
 
 
 
o
t
h
e
r
 
V
i
r
t
u
a
l
B
o
x
 
c
l
i
e
n
t
s
 
a
f
t
e
r
 
s
u
c
c
e
s
s
f
u
l
 
i
n
v
o
c
a
t
i
o
n
 
o
f
 
t
h
i
s


 
 
 
 
 
 
 
 
m
e
t
h
o
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
e
t
h
o
d
 
s
e
n
d
s
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
D
a
t
a
C
h
a
n
g
e
d
E
v
e
n
t
"
/
>


 
 
 
 
 
 
 
 
 
 
n
o
t
i
f
i
c
a
t
i
o
n
 
e
v
e
n
t
 
a
f
t
e
r
 
t
h
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
h
a
s
 
b
e
e
n
 
s
u
c
c
e
s
s
f
u
l
l
y


 
 
 
 
 
 
 
 
 
 
s
a
v
e
d
 
(
o
n
l
y
 
f
o
r
 
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
)
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
C
a
l
l
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
 
i
s
 
o
n
l
y
 
v
a
l
i
d
 
o
n
 
i
n
s
t
a
n
c
e
s
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
 
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>
 
a
n
d
 
o
n
 
n
e
w
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
b
u
t
 
n
o
t


 
 
 
 
 
 
 
 
 
 
y
e
t
 
r
e
g
i
s
t
e
r
e
d
,
 
o
r
 
o
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
 
a
f
t
e
r
 
c
a
l
l
i
n
g


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
u
n
r
e
g
i
s
t
e
r
"
/
>
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
s
 
f
i
l
e
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
X
M
L
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
p
a
r
s
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
A
C
C
E
S
S
D
E
N
I
E
D


 
 
 
 
 
 
 
 
 
 
 
 
M
o
d
i
f
i
c
a
t
i
o
n
 
r
e
q
u
e
s
t
 
r
e
f
u
s
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
a
v
e
S
e
t
t
i
n
g
s
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
i
s
c
a
r
d
_
s
e
t
t
i
n
g
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
D
i
s
c
a
r
d
s
 
a
n
y
 
c
h
a
n
g
e
s
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
m
a
d
e
 
s
i
n
c
e
 
t
h
e
 
s
e
s
s
i
o
n


 
 
 
 
 
 
 
 
h
a
s
 
b
e
e
n
 
o
p
e
n
e
d
 
o
r
 
s
i
n
c
e
 
t
h
e
 
l
a
s
t
 
c
a
l
l
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>


 
 
 
 
 
 
 
 
o
r
 
<
l
i
n
k
 
t
o
=
"
#
d
i
s
c
a
r
d
S
e
t
t
i
n
g
s
"
/
>
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
C
a
l
l
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
 
i
s
 
o
n
l
y
 
v
a
l
i
d
 
o
n
 
i
n
s
t
a
n
c
e
s
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
 
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>
 
a
n
d
 
o
n
 
n
e
w
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
o
r


 
 
 
 
 
 
 
 
 
 
o
p
e
n
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
a
c
h
i
n
e
"
/
>
 
b
u
t
 
n
o
t


 
 
 
 
 
 
 
 
 
 
y
e
t
 
r
e
g
i
s
t
e
r
e
d
,
 
o
r
 
o
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
 
a
f
t
e
r
 
c
a
l
l
i
n
g


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
u
n
r
e
g
i
s
t
e
r
"
/
>
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
m
u
t
a
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
i
s
c
a
r
d
S
e
t
t
i
n
g
s
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
u
n
r
e
g
i
s
t
e
r
(
s
e
l
f
,
 
c
l
e
a
n
u
p
_
m
o
d
e
)
:


 
 
 
 
 
 
 
 
"
"
"
U
n
r
e
g
i
s
t
e
r
s
 
a
 
m
a
c
h
i
n
e
 
p
r
e
v
i
o
u
s
l
y
 
r
e
g
i
s
t
e
r
e
d
 
w
i
t
h


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
r
e
g
i
s
t
e
r
M
a
c
h
i
n
e
"
/
>
 
a
n
d
 
o
p
t
i
o
n
a
l
l
y
 
d
o
 
a
d
d
i
t
i
o
n
a
l


 
 
 
 
 
 
 
 
c
l
e
a
n
u
p
 
b
e
f
o
r
e
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
u
n
r
e
g
i
s
t
e
r
e
d
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
d
o
e
s
 
n
o
t
 
d
e
l
e
t
e
 
a
n
y
 
f
i
l
e
s
.
 
I
t
 
o
n
l
y
 
c
h
a
n
g
e
s
 
t
h
e
 
m
a
c
h
i
n
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
a
n
d


 
 
 
 
 
 
 
 
t
h
e
 
l
i
s
t
 
o
f
 
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
 
i
n
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
o
b
j
e
c
t
.
 
T
o
 
d
e
l
e
t
e
 
t
h
e
 
f
i
l
e
s
 
w
h
i
c
h


 
 
 
 
 
 
 
 
b
e
l
o
n
g
e
d
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
,
 
i
n
c
l
u
d
i
n
g
 
t
h
e
 
X
M
L
 
f
i
l
e
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
t
s
e
l
f
,
 
c
a
l
l


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
C
o
n
f
i
g
"
/
>
,
 
o
p
t
i
o
n
a
l
l
y
 
w
i
t
h
 
t
h
e
 
a
r
r
a
y
 
o
f
 
I
M
e
d
i
u
m
 
o
b
j
e
c
t
s
 
w
h
i
c
h
 
w
a
s
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
f
r
o
m
 
t
h
i
s
 
m
e
t
h
o
d
.




 
 
 
 
 
 
 
 
H
o
w
 
t
h
o
r
o
u
g
h
l
y
 
t
h
i
s
 
m
e
t
h
o
d
 
c
l
e
a
n
s
 
u
p
 
t
h
e
 
m
a
c
h
i
n
e
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
b
e
f
o
r
e
 
u
n
r
e
g
i
s
t
e
r
i
n
g


 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
d
e
p
e
n
d
s
 
o
n
 
t
h
e
 
@
a
 
c
l
e
a
n
u
p
M
o
d
e
 
a
r
g
u
m
e
n
t
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
W
i
t
h
 
"
U
n
r
e
g
i
s
t
e
r
O
n
l
y
"
,
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
o
n
l
y
 
b
e
 
u
n
r
e
g
i
s
t
e
r
e
d
,
 
b
u
t
 
n
o
 
a
d
d
i
t
i
o
n
a
l


 
 
 
 
 
 
 
 
 
 
 
 
c
l
e
a
n
u
p
 
w
i
l
l
 
b
e
 
p
e
r
f
o
r
m
e
d
.
 
T
h
e
 
c
a
l
l
 
w
i
l
l
 
f
a
i
l
 
i
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
i
n
 
"
S
a
v
e
d
"
 
s
t
a
t
e


 
 
 
 
 
 
 
 
 
 
 
 
o
r
 
h
a
s
 
a
n
y
 
s
n
a
p
s
h
o
t
s
 
o
r
 
a
n
y
 
m
e
d
i
a
 
a
t
t
a
c
h
e
d
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
A
t
t
a
c
h
m
e
n
t
"
/
>
)
.


 
 
 
 
 
 
 
 
 
 
 
 
I
t
 
i
s
 
t
h
e
 
r
e
s
p
o
n
s
i
b
i
l
i
t
y
 
o
f
 
t
h
e
 
c
a
l
l
e
r
 
t
o
 
d
e
l
e
t
e
 
a
l
l
 
s
u
c
h
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
i
n
 
t
h
i
s
 
m
o
d
e
.


 
 
 
 
 
 
 
 
 
 
 
 
I
n
 
t
h
i
s
 
m
o
d
e
,
 
t
h
e
 
A
P
I
 
b
e
h
a
v
e
s
 
l
i
k
e
 
t
h
e
 
f
o
r
m
e
r
 
@
c
 
I
V
i
r
t
u
a
l
B
o
x
:
:
u
n
r
e
g
i
s
t
e
r
M
a
c
h
i
n
e
(
)
 
A
P
I


 
 
 
 
 
 
 
 
 
 
 
 
w
h
i
c
h
 
i
t
 
r
e
p
l
a
c
e
s
.


 
 
 
 
 
 
 
 
 
 
W
i
t
h
 
"
D
e
t
a
c
h
A
l
l
R
e
t
u
r
n
N
o
n
e
"
,
 
t
h
e
 
c
a
l
l
 
w
i
l
l
 
s
u
c
c
e
e
d
 
e
v
e
n
 
i
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
i
n
 
"
S
a
v
e
d
"


 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
t
e
 
o
r
 
i
f
 
i
t
 
h
a
s
 
s
n
a
p
s
h
o
t
s
 
o
r
 
m
e
d
i
a
 
a
t
t
a
c
h
e
d
.
 
A
l
l
 
m
e
d
i
a
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
t
e
 
o
r
 
i
n
 
s
n
a
p
s
h
o
t
s
 
w
i
l
l
 
b
e
 
d
e
t
a
c
h
e
d
.
 
N
o
 
m
e
d
i
u
m
 
o
b
j
e
c
t
s
 
w
i
l
l
 
b
e
 
r
e
t
u
r
n
e
d
;


 
 
 
 
 
 
 
 
 
 
 
 
a
l
l
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
m
e
d
i
a
 
w
i
l
l
 
r
e
m
a
i
n
 
o
p
e
n
.


 
 
 
 
 
 
 
 
 
 
W
i
t
h
 
"
D
e
t
a
c
h
A
l
l
R
e
t
u
r
n
H
a
r
d
D
i
s
k
s
O
n
l
y
"
,
 
t
h
e
 
c
a
l
l
 
w
i
l
l
 
b
e
h
a
v
e
 
l
i
k
e
 
w
i
t
h
 
"
D
e
t
a
c
h
A
l
l
R
e
t
u
r
n
N
o
n
e
"
,


 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
t
h
a
t
 
a
l
l
 
t
h
e
 
h
a
r
d
 
d
i
s
k
 
m
e
d
i
u
m
 
o
b
j
e
c
t
s
 
w
h
i
c
h
 
w
e
r
e
 
d
e
t
a
c
h
e
d
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l


 
 
 
 
 
 
 
 
 
 
 
 
b
e
 
r
e
t
u
r
n
e
d
 
a
s
 
a
n
 
a
r
r
a
y
.
 
T
h
i
s
 
a
l
l
o
w
s
 
f
o
r
 
q
u
i
c
k
l
y
 
p
a
s
s
i
n
g
 
t
h
e
m
 
t
o
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
C
o
n
f
i
g
"
/
>


 
 
 
 
 
 
 
 
 
 
 
 
A
P
I
 
f
o
r
 
c
l
o
s
i
n
g
 
a
n
d
 
d
e
l
e
t
i
o
n
.


 
 
 
 
 
 
 
 
 
 
W
i
t
h
 
"
F
u
l
l
"
,
 
t
h
e
 
c
a
l
l
 
w
i
l
l
 
b
e
h
a
v
e
 
l
i
k
e
 
w
i
t
h
 
"
D
e
t
a
c
h
A
l
l
R
e
t
u
r
n
H
a
r
d
D
i
s
k
s
O
n
l
y
"
,
 
e
x
c
e
p
t


 
 
 
 
 
 
 
 
 
 
 
 
t
h
a
t
 
a
l
l
 
m
e
d
i
a
 
w
i
l
l
 
b
e
 
r
e
t
u
r
n
e
d
 
i
n
 
t
h
e
 
a
r
r
a
y
,
 
i
n
c
l
u
d
i
n
g
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a
 
l
i
k
e
 
D
V
D
s
 
a
n
d


 
 
 
 
 
 
 
 
 
 
 
 
f
l
o
p
p
i
e
s
.
 
T
h
i
s
 
m
i
g
h
t
 
b
e
 
u
s
e
f
u
l
 
i
f
 
t
h
e
 
u
s
e
r
 
w
a
n
t
s
 
t
o
 
i
n
s
p
e
c
t
 
i
n
 
d
e
t
a
i
l
 
w
h
i
c
h
 
m
e
d
i
a
 
w
e
r
e


 
 
 
 
 
 
 
 
 
 
 
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
m
a
c
h
i
n
e
.
 
B
e
 
c
a
r
e
f
u
l
 
w
h
e
n
 
p
a
s
s
i
n
g
 
t
h
e
 
m
e
d
i
a
 
a
r
r
a
y
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
C
o
n
f
i
g
"
/
>


 
 
 
 
 
 
 
 
 
 
 
 
i
n
 
t
h
a
t
 
c
a
s
e
 
b
e
c
a
u
s
e
 
u
s
e
r
s
 
w
i
l
l
 
t
y
p
i
c
a
l
l
y
 
w
a
n
t
 
t
o
 
p
r
e
s
e
r
v
e
 
I
S
O
 
a
n
d
 
R
A
W
 
i
m
a
g
e
 
f
i
l
e
s
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
A
 
t
y
p
i
c
a
l
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
 
w
i
l
l
 
u
s
e
 
"
D
e
t
a
c
h
A
l
l
R
e
t
u
r
n
H
a
r
d
D
i
s
k
s
O
n
l
y
"
 
a
n
d
 
t
h
e
n
 
p
a
s
s
 
t
h
e


 
 
 
 
 
 
 
 
r
e
s
u
l
t
i
n
g
 
I
M
e
d
i
u
m
 
a
r
r
a
y
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
C
o
n
f
i
g
"
/
>
.
 
T
h
i
s
 
w
a
y
,
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
c
o
m
p
l
e
t
e
l
y


 
 
 
 
 
 
 
 
d
e
l
e
t
e
d
 
w
i
t
h
 
a
l
l
 
i
t
s
 
s
a
v
e
d
 
s
t
a
t
e
s
 
a
n
d
 
h
a
r
d
 
d
i
s
k
 
i
m
a
g
e
s
,
 
b
u
t
 
i
m
a
g
e
s
 
f
o
r
 
r
e
m
o
v
a
b
l
e


 
 
 
 
 
 
 
 
d
r
i
v
e
s
 
(
s
u
c
h
 
a
s
 
I
S
O
 
a
n
d
 
R
A
W
 
f
i
l
e
s
)
 
w
i
l
l
 
r
e
m
a
i
n
 
o
n
 
d
i
s
k
.




 
 
 
 
 
 
 
 
T
h
i
s
 
A
P
I
 
d
o
e
s
 
n
o
t
 
v
e
r
i
f
y
 
w
h
e
t
h
e
r
 
t
h
e
 
m
e
d
i
a
 
f
i
l
e
s
 
r
e
t
u
r
n
e
d
 
i
n
 
t
h
e
 
a
r
r
a
y
 
a
r
e
 
s
t
i
l
l


 
 
 
 
 
 
 
 
a
t
t
a
c
h
e
d
 
t
o
 
o
t
h
e
r
 
m
a
c
h
i
n
e
s
 
(
i
.
e
.
 
s
h
a
r
e
d
 
b
e
t
w
e
e
n
 
s
e
v
e
r
a
l
 
m
a
c
h
i
n
e
s
)
.
 
I
f
 
s
u
c
h
 
a
 
s
h
a
r
e
d


 
 
 
 
 
 
 
 
i
m
a
g
e
 
i
s
 
p
a
s
s
e
d
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
C
o
n
f
i
g
"
/
>
 
h
o
w
e
v
e
r
,
 
c
l
o
s
i
n
g
 
t
h
e
 
i
m
a
g
e
 
w
i
l
l
 
f
a
i
l
 
t
h
e
r
e


 
 
 
 
 
 
 
 
a
n
d
 
t
h
e
 
i
m
a
g
e
 
w
i
l
l
 
b
e
 
s
i
l
e
n
t
l
y
 
s
k
i
p
p
e
d
.




 
 
 
 
 
 
 
 
T
h
i
s
 
A
P
I
 
m
a
y
,
 
h
o
w
e
v
e
r
,
 
m
o
v
e
 
m
e
d
i
a
 
f
r
o
m
 
t
h
i
s
 
m
a
c
h
i
n
e
'
s
 
m
e
d
i
a
 
r
e
g
i
s
t
r
y
 
t
o
 
o
t
h
e
r
 
m
e
d
i
a


 
 
 
 
 
 
 
 
r
e
g
i
s
t
r
i
e
s
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
"
/
>
 
f
o
r
 
d
e
t
a
i
l
s
 
o
n
 
m
e
d
i
a
 
r
e
g
i
s
t
r
i
e
s
)
.
 
F
o
r
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
w
i
t
h
 
V
i
r
t
u
a
l
B
o
x
 
4
.
0
 
o
r
 
l
a
t
e
r
,
 
i
f
 
m
e
d
i
a
 
f
r
o
m
 
t
h
i
s
 
m
a
c
h
i
n
e
'
s
 
m
e
d
i
a
 
r
e
g
i
s
t
r
y


 
 
 
 
 
 
 
 
a
r
e
 
a
l
s
o
 
a
t
t
a
c
h
e
d
 
t
o
 
a
n
o
t
h
e
r
 
m
a
c
h
i
n
e
 
(
s
h
a
r
e
d
 
a
t
t
a
c
h
m
e
n
t
s
)
,
 
e
a
c
h
 
s
u
c
h
 
m
e
d
i
u
m
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
m
o
v
e
d
 
t
o
 
a
n
o
t
h
e
r
 
m
a
c
h
i
n
e
'
s
 
r
e
g
i
s
t
r
y
.
 
T
h
i
s
 
i
s
 
b
e
c
a
u
s
e
 
w
i
t
h
o
u
t
 
t
h
i
s
 
m
a
c
h
i
n
e
'
s
 
m
e
d
i
a


 
 
 
 
 
 
 
 
r
e
g
i
s
t
r
y
,
 
t
h
e
 
o
t
h
e
r
 
m
a
c
h
i
n
e
 
c
a
n
n
o
t
 
f
i
n
d
 
i
t
s
 
m
e
d
i
a
 
a
n
y
 
m
o
r
e
 
a
n
d
 
w
o
u
l
d
 
b
e
c
o
m
e
 
i
n
a
c
c
e
s
s
i
b
l
e
.




 
 
 
 
 
 
 
 
T
h
i
s
 
A
P
I
 
i
m
p
l
i
c
i
t
l
y
 
c
a
l
l
s
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
t
o
 
s
a
v
e
 
a
l
l
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s


 
 
 
 
 
 
 
 
b
e
f
o
r
e
 
u
n
r
e
g
i
s
t
e
r
i
n
g
 
i
t
.
 
I
t
 
m
a
y
 
a
l
s
o
 
s
i
l
e
n
t
l
y
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
o
n
 
o
t
h
e
r
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 
i
f
 
m
e
d
i
a
 
a
r
e
 
m
o
v
e
d
 
t
o
 
o
t
h
e
r
 
m
a
c
h
i
n
e
s
'
 
m
e
d
i
a
 
r
e
g
i
s
t
r
i
e
s
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
s
u
c
c
e
s
s
f
u
l
 
m
e
t
h
o
d
 
i
n
v
o
c
a
t
i
o
n
,
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
R
e
g
i
s
t
e
r
e
d
E
v
e
n
t
"
/
>
 
e
v
e
n
t


 
 
 
 
 
 
 
 
i
s
 
f
i
r
e
d
.




 
 
 
 
 
 
 
 
T
h
e
 
c
a
l
l
 
w
i
l
l
 
f
a
i
l
 
i
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
c
u
r
r
e
n
t
l
y
 
l
o
c
k
e
d
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
"
/
>
)
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
g
i
v
e
n
 
m
a
c
h
i
n
e
 
i
s
 
i
n
a
c
c
e
s
s
i
b
l
e
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
#
a
c
c
e
s
s
i
b
l
e
"
/
>
)
,
 
i
t


 
 
 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
u
n
r
e
g
i
s
t
e
r
e
d
 
a
n
d
 
f
u
l
l
y
 
u
n
i
n
i
t
i
a
l
i
z
e
d
 
r
i
g
h
t
 
a
f
t
e
r
w
a
r
d
s
.
 
A
s
 
a
 
r
e
s
u
l
t
,


 
 
 
 
 
 
 
 
 
 
t
h
e
 
r
e
t
u
r
n
e
d
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
 
w
i
l
l
 
b
e
 
u
n
u
s
a
b
l
e
 
a
n
d
 
a
n
 
a
t
t
e
m
p
t
 
t
o
 
c
a
l
l


 
 
 
 
 
 
 
 
 
 
a
n
y
 
m
e
t
h
o
d
 
w
i
l
l
 
r
e
t
u
r
n
 
t
h
e
 
"
O
b
j
e
c
t
 
n
o
t
 
r
e
a
d
y
"
 
e
r
r
o
r
.




 
 
 
 
 
 
 
 
i
n
 
c
l
e
a
n
u
p
_
m
o
d
e
 
o
f
 
t
y
p
e
 
C
l
e
a
n
u
p
M
o
d
e


 
 
 
 
 
 
 
 
 
 
 
 
H
o
w
 
t
o
 
c
l
e
a
n
 
u
p
 
a
f
t
e
r
 
t
h
e
 
m
a
c
h
i
n
e
 
h
a
s
 
b
e
e
n
 
u
n
r
e
g
i
s
t
e
r
e
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
a
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
m
e
d
i
a
 
d
e
t
a
c
h
e
d
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
,
 
d
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
@
a
 
c
l
e
a
n
u
p
M
o
d
e
 
p
a
r
a
m
e
t
e
r
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
i
s
 
c
u
r
r
e
n
t
l
y
 
l
o
c
k
e
d
 
f
o
r
 
a
 
s
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
e
d
i
a
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
u
n
r
e
g
i
s
t
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
l
e
a
n
u
p
_
m
o
d
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
e
d
i
a


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
l
e
t
e
_
c
o
n
f
i
g
(
s
e
l
f
,
 
m
e
d
i
a
)
:


 
 
 
 
 
 
 
 
"
"
"
D
e
l
e
t
e
s
 
t
h
e
 
f
i
l
e
s
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
t
h
i
s
 
m
a
c
h
i
n
e
 
f
r
o
m
 
d
i
s
k
.
 
I
f
 
m
e
d
i
u
m
 
o
b
j
e
c
t
s
 
a
r
e
 
p
a
s
s
e
d


 
 
 
 
 
 
 
 
i
n
 
w
i
t
h
 
t
h
e
 
@
a
 
a
M
e
d
i
a
 
a
r
g
u
m
e
n
t
,
 
t
h
e
y
 
a
r
e
 
c
l
o
s
e
d
 
a
n
d
,
 
i
f
 
c
l
o
s
i
n
g
 
w
a
s
 
s
u
c
c
e
s
s
f
u
l
,
 
t
h
e
i
r


 
 
 
 
 
 
 
 
s
t
o
r
a
g
e
 
f
i
l
e
s
 
a
r
e
 
d
e
l
e
t
e
d
 
a
s
 
w
e
l
l
.
 
F
o
r
 
c
o
n
v
e
n
i
e
n
c
e
,
 
t
h
i
s
 
a
r
r
a
y
 
o
f
 
m
e
d
i
a
 
f
i
l
e
s
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
t
h
e
 
s
a
m
e
 
a
s
 
t
h
e
 
o
n
e
 
r
e
t
u
r
n
e
d
 
f
r
o
m
 
a
 
p
r
e
v
i
o
u
s
 
<
l
i
n
k
 
t
o
=
"
#
u
n
r
e
g
i
s
t
e
r
"
/
>
 
c
a
l
l
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
m
u
s
t
 
o
n
l
y
 
b
e
 
c
a
l
l
e
d
 
o
n
 
m
a
c
h
i
n
e
s
 
w
h
i
c
h
 
a
r
e
 
e
i
t
h
e
r
 
w
r
i
t
e
-
l
o
c
k
e
d
 
(
i
.
e
.
 
o
n
 
i
n
s
t
a
n
c
e
s


 
 
 
 
 
 
 
 
r
e
t
u
r
n
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>
)
 
o
r
 
o
n
 
u
n
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
 
(
i
.
e
.
 
n
o
t
 
y
e
t


 
 
 
 
 
 
 
 
r
e
g
i
s
t
e
r
e
d
 
m
a
c
h
i
n
e
s
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
 
o
r
 
o
p
e
n
e
d
 
b
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
a
c
h
i
n
e
"
/
>
,
 
o
r
 
a
f
t
e
r
 
h
a
v
i
n
g
 
c
a
l
l
e
d
 
<
l
i
n
k
 
t
o
=
"
#
u
n
r
e
g
i
s
t
e
r
"
/
>
)
.




 
 
 
 
 
 
 
 
T
h
e
 
f
o
l
l
o
w
i
n
g
 
f
i
l
e
s
 
w
i
l
l
 
b
e
 
d
e
l
e
t
e
d
 
b
y
 
t
h
i
s
 
m
e
t
h
o
d
:


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
<
l
i
n
k
 
t
o
=
"
#
u
n
r
e
g
i
s
t
e
r
"
/
>
 
h
a
d
 
b
e
e
n
 
p
r
e
v
i
o
u
s
l
y
 
c
a
l
l
e
d
 
w
i
t
h
 
a
 
@
a
 
c
l
e
a
n
u
p
M
o
d
e


 
 
 
 
 
 
 
 
 
 
 
 
a
r
g
u
m
e
n
t
 
o
t
h
e
r
 
t
h
a
n
 
"
U
n
r
e
g
i
s
t
e
r
O
n
l
y
"
,
 
t
h
i
s
 
w
i
l
l
 
d
e
l
e
t
e
 
a
l
l
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
s
 
t
h
a
t


 
 
 
 
 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
h
a
d
 
i
n
 
u
s
e
;
 
p
o
s
s
i
b
l
y
 
o
n
e
 
i
f
 
t
h
e
 
m
a
c
h
i
n
e
 
w
a
s
 
i
n
 
"
S
a
v
e
d
"
 
s
t
a
t
e
 
a
n
d
 
o
n
e


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
e
a
c
h
 
o
n
l
i
n
e
 
s
n
a
p
s
h
o
t
 
t
h
a
t
 
t
h
e
 
m
a
c
h
i
n
e
 
h
a
d
.


 
 
 
 
 
 
 
 
 
 
O
n
 
e
a
c
h
 
m
e
d
i
u
m
 
o
b
j
e
c
t
 
p
a
s
s
e
d
 
i
n
 
t
h
e
 
@
a
 
a
M
e
d
i
a
 
a
r
r
a
y
,
 
t
h
i
s
 
w
i
l
l
 
c
a
l
l


 
 
 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
c
l
o
s
e
"
/
>
.
 
I
f
 
t
h
a
t
 
s
u
c
c
e
e
d
s
,
 
t
h
i
s
 
w
i
l
l
 
a
t
t
e
m
p
t
 
t
o
 
d
e
l
e
t
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
m
e
d
i
u
m
'
s
 
s
t
o
r
a
g
e
 
o
n
 
d
i
s
k
.
 
S
i
n
c
e
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
c
l
o
s
e
"
/
>
 
c
a
l
l
 
w
i
l
l
 
f
a
i
l
 
i
f
 
t
h
e
 
m
e
d
i
u
m
 
i
s
 
s
t
i
l
l


 
 
 
 
 
 
 
 
 
 
 
 
i
n
 
u
s
e
,
 
e
.
g
.
 
b
e
c
a
u
s
e
 
i
t
 
i
s
 
s
t
i
l
l
 
a
t
t
a
c
h
e
d
 
t
o
 
a
 
s
e
c
o
n
d
 
m
a
c
h
i
n
e
;
 
i
n
 
t
h
a
t
 
c
a
s
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
s
t
o
r
a
g
e
 
w
i
l
l
 
n
o
t
 
b
e
 
d
e
l
e
t
e
d
.


 
 
 
 
 
 
 
 
 
 
F
i
n
a
l
l
y
,
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
o
w
n
 
X
M
L
 
f
i
l
e
 
w
i
l
l
 
b
e
 
d
e
l
e
t
e
d
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
S
i
n
c
e
 
d
e
l
e
t
i
n
g
 
l
a
r
g
e
 
d
i
s
k
 
i
m
a
g
e
 
f
i
l
e
s
 
c
a
n
 
b
e
 
a
 
t
i
m
e
-
c
o
n
s
u
m
i
n
g
 
I
/
O
 
o
p
e
r
a
t
i
o
n
,
 
t
h
i
s


 
 
 
 
 
 
 
 
m
e
t
h
o
d
 
o
p
e
r
a
t
e
s
 
a
s
y
n
c
h
r
o
n
o
u
s
l
y
 
a
n
d
 
r
e
t
u
r
n
s
 
a
n
 
I
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
a
l
l
o
w
 
t
h
e
 
c
a
l
l
e
r


 
 
 
 
 
 
 
 
t
o
 
m
o
n
i
t
o
r
 
t
h
e
 
p
r
o
g
r
e
s
s
.
 
T
h
e
r
e
 
w
i
l
l
 
b
e
 
o
n
e
 
s
u
b
-
o
p
e
r
a
t
i
o
n
 
f
o
r
 
e
a
c
h
 
f
i
l
e
 
t
h
a
t
 
i
s


 
 
 
 
 
 
 
 
b
e
i
n
g
 
d
e
l
e
t
e
d
 
(
s
a
v
e
d
 
s
t
a
t
e
 
o
r
 
m
e
d
i
u
m
 
s
t
o
r
a
g
e
 
f
i
l
e
)
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
e
t
t
i
n
g
s
M
o
d
i
f
i
e
d
"
/
>
 
w
i
l
l
 
r
e
t
u
r
n
 
@
c
 
t
r
u
e
 
a
f
t
e
r
 
t
h
i
s


 
 
 
 
 
 
 
 
 
 
m
e
t
h
o
d
 
s
u
c
c
e
s
s
f
u
l
l
y
 
r
e
t
u
r
n
s
.




 
 
 
 
 
 
 
 
i
n
 
m
e
d
i
a
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
m
e
d
i
a
 
t
o
 
b
e
 
c
l
o
s
e
d
 
a
n
d
 
w
h
o
s
e
 
s
t
o
r
a
g
e
 
f
i
l
e
s
 
w
i
l
l
 
b
e
 
d
e
l
e
t
e
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
i
s
 
r
e
g
i
s
t
e
r
e
d
 
b
u
t
 
n
o
t
 
w
r
i
t
e
-
l
o
c
k
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
P
R
T
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
u
l
d
 
n
o
t
 
d
e
l
e
t
e
 
t
h
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
l
e
t
e
C
o
n
f
i
g
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
m
e
d
i
a
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
x
p
o
r
t
_
t
o
(
s
e
l
f
,
 
a
p
p
l
i
a
n
c
e
,
 
l
o
c
a
t
i
o
n
)
:


 
 
 
 
 
 
 
 
"
"
"
E
x
p
o
r
t
s
 
t
h
e
 
m
a
c
h
i
n
e
 
t
o
 
a
n
 
O
V
F
 
a
p
p
l
i
a
n
c
e
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
A
p
p
l
i
a
n
c
e
"
/
>
 
f
o
r
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
s
t
e
p
s
 
r
e
q
u
i
r
e
d
 
t
o
 
e
x
p
o
r
t
 
V
i
r
t
u
a
l
B
o
x
 
m
a
c
h
i
n
e
s
 
t
o
 
O
V
F
.




 
 
 
 
 
 
 
 
i
n
 
a
p
p
l
i
a
n
c
e
 
o
f
 
t
y
p
e
 
I
A
p
p
l
i
a
n
c
e


 
 
 
 
 
 
 
 
 
 
 
 
A
p
p
l
i
a
n
c
e
 
t
o
 
e
x
p
o
r
t
 
t
h
i
s
 
m
a
c
h
i
n
e
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
l
o
c
a
t
i
o
n
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
a
r
g
e
t
 
l
o
c
a
t
i
o
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
y
p
e
 
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
 
o
b
j
e
c
t
 
w
h
i
c
h
 
i
s
 
c
r
e
a
t
e
d
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
s
c
r
i
p
t
i
o
n
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
x
p
o
r
t
T
o
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
a
p
p
l
i
a
n
c
e
,
 
l
o
c
a
t
i
o
n
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
V
i
r
t
u
a
l
S
y
s
t
e
m
D
e
s
c
r
i
p
t
i
o
n
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
s
c
r
i
p
t
i
o
n


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
n
a
m
e
_
o
r
_
i
d
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
a
 
s
n
a
p
s
h
o
t
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
 
o
r
 
U
U
I
D
.




 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
a
 
s
n
a
p
s
h
o
t
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
U
U
I
D
.


 
 
 
 
 
 
 
 
A
 
@
c
 
n
u
l
l
 
a
r
g
u
m
e
n
t
 
c
a
n
 
b
e
 
u
s
e
d
 
t
o
 
o
b
t
a
i
n
 
t
h
e
 
f
i
r
s
t
 
s
n
a
p
s
h
o
t


 
 
 
 
 
 
 
 
t
a
k
e
n
 
o
n
 
t
h
i
s
 
m
a
c
h
i
n
e
.
 
T
o
 
t
r
a
v
e
r
s
e
 
t
h
e
 
w
h
o
l
e
 
t
r
e
e
 
o
f
 
s
n
a
p
s
h
o
t
s


 
 
 
 
 
 
 
 
s
t
a
r
t
i
n
g
 
f
r
o
m
 
t
h
e
 
r
o
o
t
,
 
i
n
s
p
e
c
t
 
t
h
e
 
r
o
o
t
 
s
n
a
p
s
h
o
t
'
s


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
:
:
c
h
i
l
d
r
e
n
"
/
>
 
a
t
t
r
i
b
u
t
e
 
a
n
d
 
r
e
c
u
r
s
e
 
o
v
e
r
 
t
h
o
s
e
 
c
h
i
l
d
r
e
n
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
_
o
r
_
i
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
W
h
a
t
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.
 
N
a
m
e
 
o
r
 
U
U
I
D
 
o
f
 
t
h
e
 
s
n
a
p
s
h
o
t
 
t
o
 
f
i
n
d




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
n
a
p
s
h
o
t
 
o
f
 
t
y
p
e
 
I
S
n
a
p
s
h
o
t


 
 
 
 
 
 
 
 
 
 
 
 
S
n
a
p
s
h
o
t
 
o
b
j
e
c
t
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
h
a
s
 
n
o
 
s
n
a
p
s
h
o
t
s
 
o
r
 
s
n
a
p
s
h
o
t
 
n
o
t
 
f
o
u
n
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
_
o
r
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
S
n
a
p
s
h
o
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
n
a
p
s
h
o
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
s
h
a
r
e
d
_
f
o
l
d
e
r
(
s
e
l
f
,
 
n
a
m
e
,
 
h
o
s
t
_
p
a
t
h
,
 
w
r
i
t
a
b
l
e
,
 
a
u
t
o
m
o
u
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
n
e
w
 
p
e
r
m
a
n
e
n
t
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
b
y
 
a
s
s
o
c
i
a
t
i
n
g
 
t
h
e
 
g
i
v
e
n
 
l
o
g
i
c
a
l


 
 
 
 
 
 
 
 
n
a
m
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
h
o
s
t
 
p
a
t
h
,
 
a
d
d
s
 
i
t
 
t
o
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
o
f
 
s
h
a
r
e
d


 
 
 
 
 
 
 
 
f
o
l
d
e
r
s
 
a
n
d
 
s
t
a
r
t
s
 
s
h
a
r
i
n
g
 
i
t
.
 
R
e
f
e
r
 
t
o
 
t
h
e
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
 
t
o
 
r
e
a
d
 
m
o
r
e
 
a
b
o
u
t
 
l
o
g
i
c
a
l
 
n
a
m
e
s
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
n
i
q
u
e
 
l
o
g
i
c
a
l
 
n
a
m
e
 
o
f
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
.




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
_
p
a
t
h
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
i
n
 
t
h
e
 
h
o
s
t
 
f
i
l
e
 
s
y
s
t
e
m
.




 
 
 
 
 
 
 
 
i
n
 
w
r
i
t
a
b
l
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
s
h
a
r
e
 
i
s
 
w
r
i
t
a
b
l
e
 
o
r
 
r
e
a
d
o
n
l
y
.




 
 
 
 
 
 
 
 
i
n
 
a
u
t
o
m
o
u
n
t
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
s
h
a
r
e
 
g
e
t
s
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
m
o
u
n
t
e
d
 
b
y
 
t
h
e
 
g
u
e
s
t


 
 
 
 
 
 
 
 
 
 
o
r
 
n
o
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
I
N
_
U
S
E


 
 
 
 
 
 
 
 
 
 
 
 
S
h
a
r
e
d
 
f
o
l
d
e
r
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
h
a
r
e
d
 
f
o
l
d
e
r
 
@
a
 
h
o
s
t
P
a
t
h
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
h
o
s
t
_
p
a
t
h
,
 
w
r
i
t
a
b
l
e
,
 
a
u
t
o
m
o
u
n
t
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
s
h
a
r
e
d
_
f
o
l
d
e
r
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
t
h
e
 
p
e
r
m
a
n
e
n
t
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
 
p
r
e
v
i
o
u
s
l
y


 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
 
f
r
o
m
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
n
d
 
s
t
o
p
s
 
s
h
a
r
i
n
g
 
i
t
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
L
o
g
i
c
a
l
 
n
a
m
e
 
o
f
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
t
o
 
r
e
m
o
v
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
m
u
t
a
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
S
h
a
r
e
d
 
f
o
l
d
e
r
 
@
a
 
n
a
m
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
S
h
a
r
e
d
F
o
l
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
a
n
_
s
h
o
w
_
c
o
n
s
o
l
e
_
w
i
n
d
o
w
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
t
h
e
 
V
M
 
c
o
n
s
o
l
e
 
p
r
o
c
e
s
s
 
c
a
n
 
a
c
t
i
v
a
t
e
 
t
h
e


 
 
 
 
 
 
 
 
c
o
n
s
o
l
e
 
w
i
n
d
o
w
 
a
n
d
 
b
r
i
n
g
 
i
t
 
t
o
 
f
o
r
e
g
r
o
u
n
d
 
o
n
 
t
h
e
 
d
e
s
k
t
o
p
 
o
f


 
 
 
 
 
 
 
 
t
h
e
 
h
o
s
t
 
P
C
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
f
a
i
l
 
i
f
 
a
 
s
e
s
s
i
o
n
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t


 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
l
y
 
o
p
e
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
a
n
_
s
h
o
w
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
@
c
 
t
r
u
e
 
i
f
 
t
h
e
 
c
o
n
s
o
l
e
 
w
i
n
d
o
w
 
c
a
n
 
b
e
 
s
h
o
w
n
 
a
n
d
 
@
c
 
f
a
l
s
e
 
o
t
h
e
r
w
i
s
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
s
e
s
s
i
o
n
 
i
s
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
c
a
n
_
s
h
o
w
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
a
n
S
h
o
w
C
o
n
s
o
l
e
W
i
n
d
o
w
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
a
n
_
s
h
o
w


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
h
o
w
_
c
o
n
s
o
l
e
_
w
i
n
d
o
w
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
A
c
t
i
v
a
t
e
s
 
t
h
e
 
c
o
n
s
o
l
e
 
w
i
n
d
o
w
 
a
n
d
 
b
r
i
n
g
s
 
i
t
 
t
o
 
f
o
r
e
g
r
o
u
n
d
 
o
n


 
 
 
 
 
 
 
 
t
h
e
 
d
e
s
k
t
o
p
 
o
f
 
t
h
e
 
h
o
s
t
 
P
C
.
 
M
a
n
y
 
m
o
d
e
r
n
 
w
i
n
d
o
w
 
m
a
n
a
g
e
r
s
 
o
n


 
 
 
 
 
 
 
 
m
a
n
y
 
p
l
a
t
f
o
r
m
s
 
i
m
p
l
e
m
e
n
t
 
s
o
m
e
 
s
o
r
t
 
o
f
 
f
o
c
u
s
 
s
t
e
a
l
i
n
g


 
 
 
 
 
 
 
 
p
r
e
v
e
n
t
i
o
n
 
l
o
g
i
c
,
 
s
o
 
t
h
a
t
 
i
t
 
m
a
y
 
b
e
 
i
m
p
o
s
s
i
b
l
e
 
t
o
 
a
c
t
i
v
a
t
e


 
 
 
 
 
 
 
 
a
 
w
i
n
d
o
w
 
w
i
t
h
o
u
t
 
t
h
e
 
h
e
l
p
 
o
f
 
t
h
e
 
c
u
r
r
e
n
t
l
y
 
a
c
t
i
v
e


 
 
 
 
 
 
 
 
a
p
p
l
i
c
a
t
i
o
n
.
 
I
n
 
t
h
i
s
 
c
a
s
e
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
r
e
t
u
r
n
 
a
 
n
o
n
-
z
e
r
o


 
 
 
 
 
 
 
 
i
d
e
n
t
i
f
i
e
r
 
t
h
a
t
 
r
e
p
r
e
s
e
n
t
s
 
t
h
e
 
t
o
p
-
l
e
v
e
l
 
w
i
n
d
o
w
 
o
f
 
t
h
e
 
V
M


 
 
 
 
 
 
 
 
c
o
n
s
o
l
e
 
p
r
o
c
e
s
s
.
 
T
h
e
 
c
a
l
l
e
r
,
 
i
f
 
i
t
 
r
e
p
r
e
s
e
n
t
s
 
a
 
c
u
r
r
e
n
t
l
y


 
 
 
 
 
 
 
 
a
c
t
i
v
e
 
p
r
o
c
e
s
s
,
 
i
s
 
r
e
s
p
o
n
s
i
b
l
e
 
t
o
 
u
s
e
 
t
h
i
s
 
i
d
e
n
t
i
f
i
e
r
 
(
i
n
 
a


 
 
 
 
 
 
 
 
p
l
a
t
f
o
r
m
-
d
e
p
e
n
d
e
n
t
 
m
a
n
n
e
r
)
 
t
o
 
p
e
r
f
o
r
m
 
a
c
t
u
a
l
 
w
i
n
d
o
w


 
 
 
 
 
 
 
 
a
c
t
i
v
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
f
a
i
l
 
i
f
 
a
 
s
e
s
s
i
o
n
 
f
o
r
 
t
h
i
s
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t


 
 
 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
l
y
 
o
p
e
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
w
i
n
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
l
a
t
f
o
r
m
-
d
e
p
e
n
d
e
n
t
 
i
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
t
o
p
-
l
e
v
e
l
 
V
M
 
c
o
n
s
o
l
e


 
 
 
 
 
 
 
 
 
 
w
i
n
d
o
w
,
 
o
r
 
z
e
r
o
 
i
f
 
t
h
i
s
 
m
e
t
h
o
d
 
h
a
s
 
p
e
r
f
o
r
m
e
d
 
a
l
l
 
a
c
t
i
o
n
s


 
 
 
 
 
 
 
 
 
 
n
e
c
e
s
s
a
r
y
 
t
o
 
i
m
p
l
e
m
e
n
t
 
t
h
e
 
s
h
o
w
 
w
i
n
d
o
w
 
s
e
m
a
n
t
i
c
s
 
f
o
r


 
 
 
 
 
 
 
 
 
 
t
h
e
 
g
i
v
e
n
 
p
l
a
t
f
o
r
m
 
a
n
d
/
o
r
 
V
i
r
t
u
a
l
B
o
x
 
f
r
o
n
t
-
e
n
d
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
s
e
s
s
i
o
n
 
i
s
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
w
i
n
_
i
d
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
h
o
w
C
o
n
s
o
l
e
W
i
n
d
o
w
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
w
i
n
_
i
d


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
g
u
e
s
t
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
n
a
m
e
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
a
d
s
 
a
n
 
e
n
t
r
y
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
g
u
e
s
t
 
p
r
o
p
e
r
t
y
 
s
t
o
r
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
r
e
a
d
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
v
a
l
u
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
.
 
I
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
 
t
h
e
n
 
t
h
i
s


 
 
 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
e
m
p
t
y
.




 
 
 
 
 
 
 
 
o
u
t
 
t
i
m
e
s
t
a
m
p
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
i
m
e
 
a
t
 
w
h
i
c
h
 
t
h
e
 
p
r
o
p
e
r
t
y
 
w
a
s
 
l
a
s
t
 
m
o
d
i
f
i
e
d
,
 
a
s
 
s
e
e
n
 
b
y
 
t
h
e


 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
p
r
o
c
e
s
s
.




 
 
 
 
 
 
 
 
o
u
t
 
f
l
a
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
d
d
i
t
i
o
n
a
l
 
p
r
o
p
e
r
t
y
 
p
a
r
a
m
e
t
e
r
s
,
 
p
a
s
s
e
d
 
a
s
 
a
 
c
o
m
m
a
-
s
e
p
a
r
a
t
e
d
 
l
i
s
t
 
o
f


 
 
 
 
 
 
 
 
 
 
"
n
a
m
e
=
v
a
l
u
e
"
 
t
y
p
e
 
e
n
t
r
i
e
s
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
s
e
s
s
i
o
n
 
i
s
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
G
u
e
s
t
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
g
u
e
s
t
_
p
r
o
p
e
r
t
y
_
v
a
l
u
e
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
a
d
s
 
a
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
g
u
e
s
t
 
p
r
o
p
e
r
t
y
 
s
t
o
r
e
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
r
e
a
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
v
a
l
u
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
.
 
I
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
 
t
h
e
n
 
t
h
i
s


 
 
 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
e
m
p
t
y
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
s
e
s
s
i
o
n
 
i
s
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
G
u
e
s
t
P
r
o
p
e
r
t
y
V
a
l
u
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
g
u
e
s
t
_
p
r
o
p
e
r
t
y
_
t
i
m
e
s
t
a
m
p
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
a
d
s
 
a
 
p
r
o
p
e
r
t
y
 
t
i
m
e
s
t
a
m
p
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
g
u
e
s
t
 
p
r
o
p
e
r
t
y
 
s
t
o
r
e
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
r
e
a
d
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
i
m
e
s
t
a
m
p
.
 
I
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
 
t
h
e
n
 
t
h
i
s
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
 
 
e
m
p
t
y
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
s
e
s
s
i
o
n
 
i
s
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
v
a
l
u
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
G
u
e
s
t
P
r
o
p
e
r
t
y
T
i
m
e
s
t
a
m
p
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
v
a
l
u
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
g
u
e
s
t
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
,
 
f
l
a
g
s
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
,
 
c
h
a
n
g
e
s
 
o
r
 
d
e
l
e
t
e
s
 
a
n
 
e
n
t
r
y
 
i
n
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
g
u
e
s
t
 
p
r
o
p
e
r
t
y


 
 
 
 
 
 
 
 
s
t
o
r
e
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
s
e
t
,
 
c
h
a
n
g
e
 
o
r
 
d
e
l
e
t
e
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
e
w
 
v
a
l
u
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
s
e
t
,
 
c
h
a
n
g
e
 
o
r
 
d
e
l
e
t
e
.
 
I
f
 
t
h
e


 
 
 
 
 
 
 
 
 
 
p
r
o
p
e
r
t
y
 
d
o
e
s
 
n
o
t
 
y
e
t
 
e
x
i
s
t
 
a
n
d
 
v
a
l
u
e
 
i
s
 
n
o
n
-
e
m
p
t
y
,
 
i
t
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
.
 
I
f
 
t
h
e
 
v
a
l
u
e
 
i
s
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
,
 
t
h
e
 
p
r
o
p
e
r
t
y
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
 
 
d
e
l
e
t
e
d
 
i
f
 
i
t
 
e
x
i
s
t
s
.




 
 
 
 
 
 
 
 
i
n
 
f
l
a
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
d
d
i
t
i
o
n
a
l
 
p
r
o
p
e
r
t
y
 
p
a
r
a
m
e
t
e
r
s
,
 
p
a
s
s
e
d
 
a
s
 
a
 
c
o
m
m
a
-
s
e
p
a
r
a
t
e
d
 
l
i
s
t
 
o
f


 
 
 
 
 
 
 
 
 
 
"
n
a
m
e
=
v
a
l
u
e
"
 
t
y
p
e
 
e
n
t
r
i
e
s
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
A
C
C
E
S
S
D
E
N
I
E
D


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
c
a
n
n
o
t
 
b
e
 
c
h
a
n
g
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
@
a
 
f
l
a
g
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
m
u
t
a
b
l
e
 
o
r
 
s
e
s
s
i
o
n
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
C
a
n
n
o
t
 
s
e
t
 
t
r
a
n
s
i
e
n
t
 
p
r
o
p
e
r
t
y
 
w
h
e
n
 
m
a
c
h
i
n
e
 
n
o
t
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
G
u
e
s
t
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
,
 
f
l
a
g
s
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
e
t
_
g
u
e
s
t
_
p
r
o
p
e
r
t
y
_
v
a
l
u
e
(
s
e
l
f
,
 
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
t
s
 
o
r
 
c
h
a
n
g
e
s
 
a
 
v
a
l
u
e
 
i
n
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
g
u
e
s
t
 
p
r
o
p
e
r
t
y


 
 
 
 
 
 
 
 
s
t
o
r
e
.
 
T
h
e
 
f
l
a
g
s
 
f
i
e
l
d
 
w
i
l
l
 
b
e
 
l
e
f
t
 
u
n
c
h
a
n
g
e
d
 
o
r
 
c
r
e
a
t
e
d
 
e
m
p
t
y
 
f
o
r
 
a


 
 
 
 
 
 
 
 
n
e
w
 
p
r
o
p
e
r
t
y
.




 
 
 
 
 
 
 
 
i
n
 
p
r
o
p
e
r
t
y
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
s
e
t
 
o
r
 
c
h
a
n
g
e
.




 
 
 
 
 
 
 
 
i
n
 
v
a
l
u
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
e
w
 
v
a
l
u
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
s
e
t
 
o
r
 
c
h
a
n
g
e
.
 
I
f
 
t
h
e


 
 
 
 
 
 
 
 
 
 
p
r
o
p
e
r
t
y
 
d
o
e
s
 
n
o
t
 
y
e
t
 
e
x
i
s
t
 
a
n
d
 
v
a
l
u
e
 
i
s
 
n
o
n
-
e
m
p
t
y
,
 
i
t
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
A
C
C
E
S
S
D
E
N
I
E
D


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
y
 
c
a
n
n
o
t
 
b
e
 
c
h
a
n
g
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
m
u
t
a
b
l
e
 
o
r
 
s
e
s
s
i
o
n
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
C
a
n
n
o
t
 
s
e
t
 
t
r
a
n
s
i
e
n
t
 
p
r
o
p
e
r
t
y
 
w
h
e
n
 
m
a
c
h
i
n
e
 
n
o
t
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
e
t
G
u
e
s
t
P
r
o
p
e
r
t
y
V
a
l
u
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
r
o
p
e
r
t
y
_
p
,
 
v
a
l
u
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
l
e
t
e
_
g
u
e
s
t
_
p
r
o
p
e
r
t
y
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
D
e
l
e
t
e
s
 
a
n
 
e
n
t
r
y
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
g
u
e
s
t
 
p
r
o
p
e
r
t
y
 
s
t
o
r
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
y
 
t
o
 
d
e
l
e
t
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
s
e
s
s
i
o
n
 
i
s
 
n
o
t
 
o
p
e
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
l
e
t
e
G
u
e
s
t
P
r
o
p
e
r
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
u
m
e
r
a
t
e
_
g
u
e
s
t
_
p
r
o
p
e
r
t
i
e
s
(
s
e
l
f
,
 
p
a
t
t
e
r
n
s
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
 
a
 
l
i
s
t
 
o
f
 
t
h
e
 
g
u
e
s
t
 
p
r
o
p
e
r
t
i
e
s
 
m
a
t
c
h
i
n
g
 
a
 
s
e
t
 
o
f
 
p
a
t
t
e
r
n
s
 
a
l
o
n
g


 
 
 
 
 
 
 
 
w
i
t
h
 
t
h
e
i
r
 
v
a
l
u
e
s
,
 
t
i
m
e
 
s
t
a
m
p
s
 
a
n
d
 
f
l
a
g
s
.




 
 
 
 
 
 
 
 
i
n
 
p
a
t
t
e
r
n
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
p
a
t
t
e
r
n
s
 
t
o
 
m
a
t
c
h
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
a
g
a
i
n
s
t
,
 
s
e
p
a
r
a
t
e
d
 
b
y
 
'
|
'


 
 
 
 
 
 
 
 
 
 
c
h
a
r
a
c
t
e
r
s
.
 
I
f
 
t
h
i
s
 
i
s
 
e
m
p
t
y
 
o
r
 
@
c
 
n
u
l
l
,
 
a
l
l
 
p
r
o
p
e
r
t
i
e
s
 
w
i
l
l
 
m
a
t
c
h
.




 
 
 
 
 
 
 
 
o
u
t
 
n
a
m
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
u
e
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
v
a
l
u
e
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.
 
T
h
e
 
a
r
r
a
y
 
e
n
t
r
i
e
s
 
m
a
t
c
h
 
t
h
e


 
 
 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
e
n
t
r
i
e
s
 
i
n
 
t
h
e
 
@
a
 
n
a
m
e
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
o
u
t
 
t
i
m
e
s
t
a
m
p
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
t
i
m
e
 
s
t
a
m
p
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.
 
T
h
e
 
a
r
r
a
y
 
e
n
t
r
i
e
s
 
m
a
t
c
h


 
 
 
 
 
 
 
 
 
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
e
n
t
r
i
e
s
 
i
n
 
t
h
e
 
@
a
 
n
a
m
e
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
o
u
t
 
f
l
a
g
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
f
l
a
g
s
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
r
e
t
u
r
n
e
d
.
 
T
h
e
 
a
r
r
a
y
 
e
n
t
r
i
e
s
 
m
a
t
c
h
 
t
h
e


 
 
 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
e
n
t
r
i
e
s
 
i
n
 
t
h
e
 
@
a
 
n
a
m
e
 
a
r
r
a
y
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
u
m
e
r
a
t
e
G
u
e
s
t
P
r
o
p
e
r
t
i
e
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
a
t
t
e
r
n
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
q
u
e
r
y
_
s
a
v
e
d
_
g
u
e
s
t
_
s
c
r
e
e
n
_
i
n
f
o
(
s
e
l
f
,
 
s
c
r
e
e
n
_
i
d
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
g
u
e
s
t
 
d
i
m
e
n
s
i
o
n
s
 
f
r
o
m
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
.




 
 
 
 
 
 
 
 
i
n
 
s
c
r
e
e
n
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
a
v
e
d
 
g
u
e
s
t
 
s
c
r
e
e
n
 
t
o
 
q
u
e
r
y
 
i
n
f
o
 
f
r
o
m
.




 
 
 
 
 
 
 
 
o
u
t
 
o
r
i
g
i
n
_
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
X
 
p
o
s
i
t
i
o
n
 
o
f
 
t
h
e
 
g
u
e
s
t
 
m
o
n
i
t
o
r
 
t
o
p
 
l
e
f
t
 
c
o
r
n
e
r
.




 
 
 
 
 
 
 
 
o
u
t
 
o
r
i
g
i
n
_
y
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
Y
 
p
o
s
i
t
i
o
n
 
o
f
 
t
h
e
 
g
u
e
s
t
 
m
o
n
i
t
o
r
 
t
o
p
 
l
e
f
t
 
c
o
r
n
e
r
.




 
 
 
 
 
 
 
 
o
u
t
 
w
i
d
t
h
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
G
u
e
s
t
 
w
i
d
t
h
 
a
t
 
t
h
e
 
t
i
m
e
 
o
f
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
w
a
s
 
t
a
k
e
n
.




 
 
 
 
 
 
 
 
o
u
t
 
h
e
i
g
h
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
G
u
e
s
t
 
h
e
i
g
h
t
 
a
t
 
t
h
e
 
t
i
m
e
 
o
f
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
w
a
s
 
t
a
k
e
n
.




 
 
 
 
 
 
 
 
o
u
t
 
e
n
a
b
l
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
m
o
n
i
t
o
r
 
i
s
 
e
n
a
b
l
e
d
 
i
n
 
t
h
e
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
q
u
e
r
y
S
a
v
e
d
G
u
e
s
t
S
c
r
e
e
n
I
n
f
o
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
c
r
e
e
n
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
q
u
e
r
y
_
s
a
v
e
d
_
t
h
u
m
b
n
a
i
l
_
s
i
z
e
(
s
e
l
f
,
 
s
c
r
e
e
n
_
i
d
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
a
n
d
 
d
i
m
e
n
s
i
o
n
s
 
i
n
 
p
i
x
e
l
s
 
o
f
 
a
 
s
a
v
e
d
 
t
h
u
m
b
n
a
i
l
 
b
i
t
m
a
p
 
f
r
o
m
 
s
a
v
e
d
 
s
t
a
t
e
.




 
 
 
 
 
 
 
 
i
n
 
s
c
r
e
e
n
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
a
v
e
d
 
g
u
e
s
t
 
s
c
r
e
e
n
 
t
o
 
q
u
e
r
y
 
i
n
f
o
 
f
r
o
m
.




 
 
 
 
 
 
 
 
o
u
t
 
s
i
z
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
i
z
e
 
o
f
 
b
u
f
f
e
r
 
r
e
q
u
i
r
e
d
 
t
o
 
s
t
o
r
e
 
t
h
e
 
b
i
t
m
a
p
.




 
 
 
 
 
 
 
 
o
u
t
 
w
i
d
t
h
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
B
i
t
m
a
p
 
w
i
d
t
h
.




 
 
 
 
 
 
 
 
o
u
t
 
h
e
i
g
h
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
B
i
t
m
a
p
 
h
e
i
g
h
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
q
u
e
r
y
S
a
v
e
d
T
h
u
m
b
n
a
i
l
S
i
z
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
c
r
e
e
n
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
a
d
_
s
a
v
e
d
_
t
h
u
m
b
n
a
i
l
_
t
o
_
a
r
r
a
y
(
s
e
l
f
,
 
s
c
r
e
e
n
_
i
d
,
 
b
g
r
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
T
h
u
m
b
n
a
i
l
 
i
s
 
r
e
t
r
i
e
v
e
d
 
t
o
 
a
n
 
a
r
r
a
y
 
o
f
 
b
y
t
e
s
 
i
n
 
u
n
c
o
m
p
r
e
s
s
e
d
 
3
2
-
b
i
t
 
B
G
R
A
 
o
r
 
R
G
B
A
 
f
o
r
m
a
t
.




 
 
 
 
 
 
 
 
i
n
 
s
c
r
e
e
n
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
a
v
e
d
 
g
u
e
s
t
 
s
c
r
e
e
n
 
t
o
 
r
e
a
d
 
f
r
o
m
.




 
 
 
 
 
 
 
 
i
n
 
b
g
r
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
H
o
w
 
t
o
 
o
r
d
e
r
 
b
y
t
e
s
 
i
n
 
t
h
e
 
p
i
x
e
l
.
 
A
 
p
i
x
e
l
 
c
o
n
s
i
s
t
s
 
o
f
 
4
 
b
y
t
e
s
.
 
I
f
 
t
h
i
s
 
p
a
r
a
m
e
t
e
r
 
i
s
 
t
r
u
e
,
 
t
h
e
n


 
 
 
 
 
 
 
 
 
 
b
y
t
e
s
 
o
r
d
e
r
 
i
s
:
 
B
,
 
G
,
 
R
,
 
0
x
F
F
.
 
I
f
 
t
h
i
s
 
p
a
r
a
m
e
t
e
r
 
i
s
 
f
a
l
s
e
,
 
t
h
e
n
 
b
y
t
e
s
 
o
r
d
e
r
 
i
s
:
 
R
,
 
G
,
 
B
,
 
0
x
F
F
.




 
 
 
 
 
 
 
 
o
u
t
 
w
i
d
t
h
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
B
i
t
m
a
p
 
w
i
d
t
h
.




 
 
 
 
 
 
 
 
o
u
t
 
h
e
i
g
h
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
B
i
t
m
a
p
 
h
e
i
g
h
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
r
r
a
y
 
w
i
t
h
 
r
e
s
u
l
t
i
n
g
 
b
i
t
m
a
p
 
d
a
t
a
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
a
t
a
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
a
d
S
a
v
e
d
T
h
u
m
b
n
a
i
l
T
o
A
r
r
a
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
c
r
e
e
n
_
i
d
,
 
b
g
r
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
a
d
_
s
a
v
e
d
_
t
h
u
m
b
n
a
i
l
_
p
n
g
_
t
o
_
a
r
r
a
y
(
s
e
l
f
,
 
s
c
r
e
e
n
_
i
d
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
T
h
u
m
b
n
a
i
l
 
i
n
 
P
N
G
 
f
o
r
m
a
t
 
i
s
 
r
e
t
r
i
e
v
e
d
 
t
o
 
a
n
 
a
r
r
a
y
 
o
f
 
b
y
t
e
s
.




 
 
 
 
 
 
 
 
i
n
 
s
c
r
e
e
n
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
a
v
e
d
 
g
u
e
s
t
 
s
c
r
e
e
n
 
t
o
 
r
e
a
d
 
f
r
o
m
.




 
 
 
 
 
 
 
 
o
u
t
 
w
i
d
t
h
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
m
a
g
e
 
w
i
d
t
h
.




 
 
 
 
 
 
 
 
o
u
t
 
h
e
i
g
h
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
m
a
g
e
 
h
e
i
g
h
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
r
r
a
y
 
w
i
t
h
 
r
e
s
u
l
t
i
n
g
 
P
N
G
 
d
a
t
a
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
a
t
a
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
a
d
S
a
v
e
d
T
h
u
m
b
n
a
i
l
P
N
G
T
o
A
r
r
a
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
c
r
e
e
n
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
q
u
e
r
y
_
s
a
v
e
d
_
s
c
r
e
e
n
s
h
o
t
_
p
n
g
_
s
i
z
e
(
s
e
l
f
,
 
s
c
r
e
e
n
_
i
d
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
a
n
d
 
d
i
m
e
n
s
i
o
n
s
 
o
f
 
a
 
s
a
v
e
d
 
P
N
G
 
i
m
a
g
e
 
o
f
 
s
c
r
e
e
n
s
h
o
t
 
f
r
o
m
 
s
a
v
e
d
 
s
t
a
t
e
.




 
 
 
 
 
 
 
 
i
n
 
s
c
r
e
e
n
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
a
v
e
d
 
g
u
e
s
t
 
s
c
r
e
e
n
 
t
o
 
q
u
e
r
y
 
i
n
f
o
 
f
r
o
m
.




 
 
 
 
 
 
 
 
o
u
t
 
s
i
z
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
i
z
e
 
o
f
 
b
u
f
f
e
r
 
r
e
q
u
i
r
e
d
 
t
o
 
s
t
o
r
e
 
t
h
e
 
P
N
G
 
b
i
n
a
r
y
 
d
a
t
a
.




 
 
 
 
 
 
 
 
o
u
t
 
w
i
d
t
h
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
m
a
g
e
 
w
i
d
t
h
.




 
 
 
 
 
 
 
 
o
u
t
 
h
e
i
g
h
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
m
a
g
e
 
h
e
i
g
h
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
q
u
e
r
y
S
a
v
e
d
S
c
r
e
e
n
s
h
o
t
P
N
G
S
i
z
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
c
r
e
e
n
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
a
d
_
s
a
v
e
d
_
s
c
r
e
e
n
s
h
o
t
_
p
n
g
_
t
o
_
a
r
r
a
y
(
s
e
l
f
,
 
s
c
r
e
e
n
_
i
d
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
S
c
r
e
e
n
s
h
o
t
 
i
n
 
P
N
G
 
f
o
r
m
a
t
 
i
s
 
r
e
t
r
i
e
v
e
d
 
t
o
 
a
n
 
a
r
r
a
y
 
o
f
 
b
y
t
e
s
.




 
 
 
 
 
 
 
 
i
n
 
s
c
r
e
e
n
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
a
v
e
d
 
g
u
e
s
t
 
s
c
r
e
e
n
 
t
o
 
r
e
a
d
 
f
r
o
m
.




 
 
 
 
 
 
 
 
o
u
t
 
w
i
d
t
h
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
m
a
g
e
 
w
i
d
t
h
.




 
 
 
 
 
 
 
 
o
u
t
 
h
e
i
g
h
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
m
a
g
e
 
h
e
i
g
h
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
r
r
a
y
 
w
i
t
h
 
r
e
s
u
l
t
i
n
g
 
P
N
G
 
d
a
t
a
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
a
t
a
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
a
d
S
a
v
e
d
S
c
r
e
e
n
s
h
o
t
P
N
G
T
o
A
r
r
a
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
c
r
e
e
n
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
h
o
t
_
p
l
u
g
_
c
p
u
(
s
e
l
f
,
 
c
p
u
)
:


 
 
 
 
 
 
 
 
"
"
"
P
l
u
g
s
 
a
 
C
P
U
 
i
n
t
o
 
t
h
e
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
C
P
U
 
i
d
 
t
o
 
i
n
s
e
r
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
h
o
t
P
l
u
g
C
P
U
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
p
u
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
h
o
t
_
u
n
p
l
u
g
_
c
p
u
(
s
e
l
f
,
 
c
p
u
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
a
 
C
P
U
 
f
r
o
m
 
t
h
e
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
C
P
U
 
i
d
 
t
o
 
r
e
m
o
v
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
h
o
t
U
n
p
l
u
g
C
P
U
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
p
u
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
c
p
u
_
s
t
a
t
u
s
(
s
e
l
f
,
 
c
p
u
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
c
u
r
r
e
n
t
 
s
t
a
t
u
s
 
o
f
 
t
h
e
 
g
i
v
e
n
 
C
P
U
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
C
P
U
 
i
d
 
t
o
 
c
h
e
c
k
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
t
t
a
c
h
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
S
t
a
t
u
s
 
o
f
 
t
h
e
 
C
P
U
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
a
t
t
a
c
h
e
d
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
C
P
U
S
t
a
t
u
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
p
u
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
t
t
a
c
h
e
d


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
q
u
e
r
y
_
l
o
g
_
f
i
l
e
n
a
m
e
(
s
e
l
f
,
 
i
d
x
)
:


 
 
 
 
 
 
 
 
"
"
"
Q
u
e
r
i
e
s
 
f
o
r
 
t
h
e
 
V
M
 
l
o
g
 
f
i
l
e
 
n
a
m
e
 
o
f
 
a
n
 
g
i
v
e
n
 
i
n
d
e
x
.
 
R
e
t
u
r
n
s
 
a
n
 
e
m
p
t
y


 
 
 
 
 
 
 
 
s
t
r
i
n
g
 
i
f
 
a
 
l
o
g
 
f
i
l
e
 
w
i
t
h
 
t
h
a
t
 
i
n
d
e
x
 
d
o
e
s
n
'
t
 
e
x
i
s
t
s
.




 
 
 
 
 
 
 
 
i
n
 
i
d
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
W
h
i
c
h
 
l
o
g
 
f
i
l
e
 
n
a
m
e
 
t
o
 
q
u
e
r
y
.
 
0
=
c
u
r
r
e
n
t
 
l
o
g
 
f
i
l
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
e
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
O
n
 
r
e
t
u
r
n
 
t
h
e
 
f
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
l
o
g
 
f
i
l
e
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
o
n
 
e
r
r
o
r
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
f
i
l
e
n
a
m
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
q
u
e
r
y
L
o
g
F
i
l
e
n
a
m
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
x
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
e
n
a
m
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
a
d
_
l
o
g
(
s
e
l
f
,
 
i
d
x
,
 
o
f
f
s
e
t
,
 
s
i
z
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
a
d
s
 
t
h
e
 
V
M
 
l
o
g
 
f
i
l
e
.
 
T
h
e
 
c
h
u
n
k
 
s
i
z
e
 
i
s
 
l
i
m
i
t
e
d
,
 
s
o
 
e
v
e
n
 
i
f
 
y
o
u


 
 
 
 
 
 
 
 
a
s
k
 
f
o
r
 
a
 
b
i
g
 
p
i
e
c
e
 
t
h
e
r
e
 
m
i
g
h
t
 
b
e
 
l
e
s
s
 
d
a
t
a
 
r
e
t
u
r
n
e
d
.




 
 
 
 
 
 
 
 
i
n
 
i
d
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
W
h
i
c
h
 
l
o
g
 
f
i
l
e
 
t
o
 
r
e
a
d
.
 
0
=
c
u
r
r
e
n
t
 
l
o
g
 
f
i
l
e
.




 
 
 
 
 
 
 
 
i
n
 
o
f
f
s
e
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
O
f
f
s
e
t
 
i
n
 
t
h
e
 
l
o
g
 
f
i
l
e
.




 
 
 
 
 
 
 
 
i
n
 
s
i
z
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
h
u
n
k
 
s
i
z
e
 
t
o
 
r
e
a
d
 
i
n
 
t
h
e
 
l
o
g
 
f
i
l
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
D
a
t
a
 
r
e
a
d
 
f
r
o
m
 
t
h
e
 
l
o
g
 
f
i
l
e
.
 
A
 
d
a
t
a
 
s
i
z
e
 
o
f
 
0
 
m
e
a
n
s
 
e
n
d
 
o
f
 
f
i
l
e


 
 
 
 
 
 
 
 
 
 
i
f
 
t
h
e
 
r
e
q
u
e
s
t
e
d
 
c
h
u
n
k
 
s
i
z
e
 
w
a
s
 
n
o
t
 
0
.
 
T
h
i
s
 
i
s
 
t
h
e
 
u
n
p
r
o
c
e
s
s
e
d


 
 
 
 
 
 
 
 
 
 
f
i
l
e
 
d
a
t
a
,
 
i
.
e
.
 
t
h
e
 
l
i
n
e
 
e
n
d
i
n
g
 
s
t
y
l
e
 
d
e
p
e
n
d
s
 
o
n
 
t
h
e
 
p
l
a
t
f
o
r
m
 
o
f


 
 
 
 
 
 
 
 
 
 
t
h
e
 
s
y
s
t
e
m
 
t
h
e
 
s
e
r
v
e
r
 
i
s
 
r
u
n
n
i
n
g
 
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
a
t
a
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
a
d
L
o
g
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
x
,
 
o
f
f
s
e
t
,
 
s
i
z
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
a
t
a


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
l
o
n
e
_
t
o
(
s
e
l
f
,
 
t
a
r
g
e
t
,
 
m
o
d
e
,
 
o
p
t
i
o
n
s
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
c
l
o
n
e
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
,
 
e
i
t
h
e
r
 
a
s
 
a
 
f
u
l
l
 
c
l
o
n
e
 
(
w
h
i
c
h
 
m
e
a
n
s


 
 
 
 
 
 
 
 
c
r
e
a
t
i
n
g
 
i
n
d
e
p
e
n
d
e
n
t
 
c
o
p
i
e
s
 
o
f
 
t
h
e
 
h
a
r
d
 
d
i
s
k
 
m
e
d
i
a
,
 
s
a
v
e
 
s
t
a
t
e
s
 
a
n
d
 
s
o


 
 
 
 
 
 
 
 
o
n
)
,
 
o
r
 
a
s
 
a
 
l
i
n
k
e
d
 
c
l
o
n
e
 
(
w
h
i
c
h
 
u
s
e
s
 
i
t
s
 
o
w
n
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
,


 
 
 
 
 
 
 
 
s
h
a
r
i
n
g
 
t
h
e
 
p
a
r
e
n
t
 
m
e
d
i
a
 
w
i
t
h
 
t
h
e
 
s
o
u
r
c
e
 
m
a
c
h
i
n
e
)
.




 
 
 
 
 
 
 
 
T
h
e
 
t
a
r
g
e
t
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
 
m
u
s
t
 
h
a
v
e
 
b
e
e
n
 
c
r
e
a
t
e
d
 
p
r
e
v
i
o
u
s
l
y
 
w
i
t
h
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
,
 
a
n
d
 
a
l
l
 
t
h
e
 
s
e
t
t
i
n
g
s
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
t
r
a
n
s
f
e
r
r
e
d
 
e
x
c
e
p
t
 
t
h
e
 
V
M
 
n
a
m
e
 
a
n
d
 
t
h
e
 
h
a
r
d
w
a
r
e
 
U
U
I
D
.
 
Y
o
u
 
c
a
n
 
s
e
t
 
t
h
e


 
 
 
 
 
 
 
 
V
M
 
n
a
m
e
 
a
n
d
 
t
h
e
 
n
e
w
 
h
a
r
d
w
a
r
e
 
U
U
I
D
 
w
h
e
n
 
c
r
e
a
t
i
n
g
 
t
h
e
 
t
a
r
g
e
t
 
m
a
c
h
i
n
e
.
 
T
h
e


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
 
M
A
C
 
a
d
d
r
e
s
s
e
s
 
a
r
e
 
n
e
w
l
y
 
c
r
e
a
t
e
d
 
f
o
r
 
a
l
l
 
n
e
w
t
w
o
r
k
 
a
d
a
p
t
e
r
s
.
 
Y
o
u


 
 
 
 
 
 
 
 
c
a
n
 
c
h
a
n
g
e
 
t
h
a
t
 
b
e
h
a
v
i
o
u
r
 
w
i
t
h
 
t
h
e
 
o
p
t
i
o
n
s
 
p
a
r
a
m
e
t
e
r
.
 
T
h
e
 
o
p
e
r
a
t
i
o
n
 
i
s


 
 
 
 
 
 
 
 
p
e
r
f
o
r
m
e
d
 
a
s
y
n
c
h
r
o
n
o
u
s
l
y
,
 
s
o
 
t
h
e
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
 
w
i
l
l
 
b
e
 
n
o
t
 
b
e
 
u
s
a
b
l
e


 
 
 
 
 
 
 
 
u
n
t
i
l
 
t
h
e
 
@
a
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
s
i
g
n
a
l
s
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
i
n
 
t
a
r
g
e
t
 
o
f
 
t
y
p
e
 
I
M
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
 
 
T
a
r
g
e
t
 
m
a
c
h
i
n
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
i
n
 
m
o
d
e
 
o
f
 
t
y
p
e
 
C
l
o
n
e
M
o
d
e


 
 
 
 
 
 
 
 
 
 
 
 
W
h
i
c
h
 
s
t
a
t
e
s
 
s
h
o
u
l
d
 
b
e
 
c
l
o
n
e
d
.




 
 
 
 
 
 
 
 
i
n
 
o
p
t
i
o
n
s
 
o
f
 
t
y
p
e
 
C
l
o
n
e
O
p
t
i
o
n
s


 
 
 
 
 
 
 
 
 
 
 
 
O
p
t
i
o
n
s
 
f
o
r
 
t
h
e
 
c
l
o
n
i
n
g
 
o
p
e
r
a
t
i
o
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
@
a
 
t
a
r
g
e
t
 
i
s
 
@
c
 
n
u
l
l
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
l
o
n
e
T
o
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
t
a
r
g
e
t
,
 
m
o
d
e
,
 
o
p
t
i
o
n
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
V
R
D
E
S
e
r
v
e
r
I
n
f
o
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
t
a
i
n
s
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
t
h
e
 
r
e
m
o
t
e
 
d
e
s
k
t
o
p
 
(
V
R
D
E
)
 
s
e
r
v
e
r
 
c
a
p
a
b
i
l
i
t
i
e
s
 
a
n
d
 
s
t
a
t
u
s
.


 
 
 
 
 
 
T
h
i
s
 
i
s
 
u
s
e
d
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
V
R
D
E
S
e
r
v
e
r
I
n
f
o
"
/
>
 
a
t
t
r
i
b
u
t
e
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
7
1
4
4
3
4
a
1
-
5
8
c
3
-
4
a
a
b
-
9
0
4
9
-
7
6
5
2
c
5
d
f
1
1
3
b
'


 
 
 
 
w
s
m
a
p
 
=
 
'
s
t
r
u
c
t
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
c
t
i
v
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
c
t
i
v
e
'


 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
r
e
m
o
t
e
 
d
e
s
k
t
o
p
 
c
o
n
n
e
c
t
i
o
n
 
i
s
 
a
c
t
i
v
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
c
t
i
v
e
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
o
r
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
p
o
r
t
'


 
 
 
 
 
 
 
 
V
R
D
E
 
s
e
r
v
e
r
 
p
o
r
t
 
n
u
m
b
e
r
.
 
I
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
e
q
u
a
l
 
t
o
 
0
,
 
t
h
e
n


 
 
 
 
 
 
 
 
t
h
e
 
V
R
D
E
 
s
e
r
v
e
r
 
f
a
i
l
e
d
 
t
o
 
s
t
a
r
t
,
 
u
s
u
a
l
l
y
 
b
e
c
a
u
s
e
 
t
h
e
r
e
 
a
r
e
 
n
o
 
f
r
e
e
 
I
P


 
 
 
 
 
 
 
 
p
o
r
t
s
 
t
o
 
b
i
n
d
 
t
o
.
 
I
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
e
q
u
a
l
 
t
o
 
-
1
,
 
t
h
e
n
 
t
h
e
 
V
R
D
E


 
 
 
 
 
 
 
 
s
e
r
v
e
r
 
h
a
s
 
n
o
t
 
y
e
t
 
b
e
e
n
 
s
t
a
r
t
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
o
r
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
u
m
b
e
r
_
o
f
_
c
l
i
e
n
t
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
n
u
m
b
e
r
O
f
C
l
i
e
n
t
s
'


 
 
 
 
 
 
 
 
H
o
w
 
m
a
n
y
 
t
i
m
e
s
 
a
 
c
l
i
e
n
t
 
c
o
n
n
e
c
t
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
u
m
b
e
r
O
f
C
l
i
e
n
t
s
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
e
g
i
n
_
t
i
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
b
e
g
i
n
T
i
m
e
'


 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
l
a
s
t
 
c
o
n
n
e
c
t
i
o
n
 
w
a
s
 
e
s
t
a
b
l
i
s
h
e
d
,
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
 
s
i
n
c
e
 
1
9
7
0
-
0
1
-
0
1
 
U
T
C
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
e
g
i
n
T
i
m
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
n
d
_
t
i
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
e
n
d
T
i
m
e
'


 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
l
a
s
t
 
c
o
n
n
e
c
t
i
o
n
 
w
a
s
 
t
e
r
m
i
n
a
t
e
d
 
o
r
 
t
h
e
 
c
u
r
r
e
n
t
 
t
i
m
e
,
 
i
f


 
 
 
 
 
 
 
 
c
o
n
n
e
c
t
i
o
n
 
i
s
 
s
t
i
l
l
 
a
c
t
i
v
e
,
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
 
s
i
n
c
e
 
1
9
7
0
-
0
1
-
0
1
 
U
T
C
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
n
d
T
i
m
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
y
t
e
s
_
s
e
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
b
y
t
e
s
S
e
n
t
'


 
 
 
 
 
 
 
 
H
o
w
 
m
a
n
y
 
b
y
t
e
s
 
w
e
r
e
 
s
e
n
t
 
i
n
 
l
a
s
t
 
o
r
 
c
u
r
r
e
n
t
,
 
i
f
 
s
t
i
l
l
 
a
c
t
i
v
e
,
 
c
o
n
n
e
c
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
y
t
e
s
S
e
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
y
t
e
s
_
s
e
n
t
_
t
o
t
a
l
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
b
y
t
e
s
S
e
n
t
T
o
t
a
l
'


 
 
 
 
 
 
 
 
H
o
w
 
m
a
n
y
 
b
y
t
e
s
 
w
e
r
e
 
s
e
n
t
 
i
n
 
a
l
l
 
c
o
n
n
e
c
t
i
o
n
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
y
t
e
s
S
e
n
t
T
o
t
a
l
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
y
t
e
s
_
r
e
c
e
i
v
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
b
y
t
e
s
R
e
c
e
i
v
e
d
'


 
 
 
 
 
 
 
 
H
o
w
 
m
a
n
y
 
b
y
t
e
s
 
w
e
r
e
 
r
e
c
e
i
v
e
d
 
i
n
 
l
a
s
t
 
o
r
 
c
u
r
r
e
n
t
,
 
i
f
 
s
t
i
l
l
 
a
c
t
i
v
e
,
 
c
o
n
n
e
c
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
y
t
e
s
R
e
c
e
i
v
e
d
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
b
y
t
e
s
_
r
e
c
e
i
v
e
d
_
t
o
t
a
l
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
b
y
t
e
s
R
e
c
e
i
v
e
d
T
o
t
a
l
'


 
 
 
 
 
 
 
 
H
o
w
 
m
a
n
y
 
b
y
t
e
s
 
w
e
r
e
 
r
e
c
e
i
v
e
d
 
i
n
 
a
l
l
 
c
o
n
n
e
c
t
i
o
n
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
b
y
t
e
s
R
e
c
e
i
v
e
d
T
o
t
a
l
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
s
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
u
s
e
r
'


 
 
 
 
 
 
 
 
L
o
g
i
n
 
u
s
e
r
 
n
a
m
e
 
s
u
p
p
l
i
e
d
 
b
y
 
t
h
e
 
c
l
i
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
u
s
e
r
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
o
m
a
i
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
o
m
a
i
n
'


 
 
 
 
 
 
 
 
L
o
g
i
n
 
d
o
m
a
i
n
 
n
a
m
e
 
s
u
p
p
l
i
e
d
 
b
y
 
t
h
e
 
c
l
i
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
o
m
a
i
n
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
l
i
e
n
t
_
n
a
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
c
l
i
e
n
t
N
a
m
e
'


 
 
 
 
 
 
 
 
T
h
e
 
c
l
i
e
n
t
 
n
a
m
e
 
s
u
p
p
l
i
e
d
 
b
y
 
t
h
e
 
c
l
i
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
l
i
e
n
t
N
a
m
e
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
l
i
e
n
t
_
i
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
c
l
i
e
n
t
I
P
'


 
 
 
 
 
 
 
 
T
h
e
 
I
P
 
a
d
d
r
e
s
s
 
o
f
 
t
h
e
 
c
l
i
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
l
i
e
n
t
I
P
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
c
l
i
e
n
t
_
v
e
r
s
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
c
l
i
e
n
t
V
e
r
s
i
o
n
'


 
 
 
 
 
 
 
 
T
h
e
 
c
l
i
e
n
t
 
s
o
f
t
w
a
r
e
 
v
e
r
s
i
o
n
 
n
u
m
b
e
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
c
l
i
e
n
t
V
e
r
s
i
o
n
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
n
c
r
y
p
t
i
o
n
_
s
t
y
l
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
e
n
c
r
y
p
t
i
o
n
S
t
y
l
e
'


 
 
 
 
 
 
 
 
P
u
b
l
i
c
 
k
e
y
 
e
x
c
h
a
n
g
e
 
m
e
t
h
o
d
 
u
s
e
d
 
w
h
e
n
 
c
o
n
n
e
c
t
i
o
n
 
w
a
s
 
e
s
t
a
b
l
i
s
h
e
d
.


 
 
 
 
 
 
 
 
V
a
l
u
e
s
:
 
0
 
-
 
R
D
P
4
 
p
u
b
l
i
c
 
k
e
y
 
e
x
c
h
a
n
g
e
 
s
c
h
e
m
e
.


 
 
 
 
 
 
 
 
1
 
-
 
X
5
0
9
 
c
e
r
t
i
f
i
c
a
t
e
s
 
w
e
r
e
 
s
e
n
t
 
t
o
 
c
l
i
e
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
n
c
r
y
p
t
i
o
n
S
t
y
l
e
'
,
 
i
n
t
)






c
l
a
s
s
 
I
C
o
n
s
o
l
e
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
C
o
n
s
o
l
e
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
a
n
 
i
n
t
e
r
f
a
c
e
 
t
o
 
c
o
n
t
r
o
l
 
v
i
r
t
u
a
l


 
 
 
 
 
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
A
 
c
o
n
s
o
l
e
 
o
b
j
e
c
t
 
g
e
t
s
 
c
r
e
a
t
e
d
 
w
h
e
n
 
a
 
m
a
c
h
i
n
e
 
h
a
s
 
b
e
e
n
 
l
o
c
k
e
d
 
f
o
r
 
a


 
 
 
 
 
 
p
a
r
t
i
c
u
l
a
r
 
s
e
s
s
i
o
n
 
(
c
l
i
e
n
t
 
p
r
o
c
e
s
s
)
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
o
c
k
M
a
c
h
i
n
e
"
/
>


 
 
 
 
 
 
o
r
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
.
 
T
h
e
 
c
o
n
s
o
l
e
 
o
b
j
e
c
t
 
c
a
n


 
 
 
 
 
 
t
h
e
n
 
b
e
 
f
o
u
n
d
 
i
n
 
t
h
e
 
s
e
s
s
i
o
n
'
s
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
c
o
n
s
o
l
e
"
/
>
 
a
t
t
r
i
b
u
t
e
.




 
 
 
 
 
 
M
e
t
h
o
d
s
 
o
f
 
t
h
e
 
I
C
o
n
s
o
l
e
 
i
n
t
e
r
f
a
c
e
 
a
l
l
o
w
 
t
h
e
 
c
a
l
l
e
r
 
t
o
 
q
u
e
r
y
 
t
h
e
 
c
u
r
r
e
n
t


 
 
 
 
 
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
,
 
p
a
u
s
e
 
t
h
e
 
m
a
c
h
i
n
e
 
o
r
 
p
o
w
e
r
 
i
t
 
d
o
w
n
,
 
s
a
v
e


 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
o
r
 
t
a
k
e
 
a
 
s
n
a
p
s
h
o
t
,
 
a
t
t
a
c
h
 
a
n
d
 
d
e
t
a
c
h
 
r
e
m
o
v
a
b
l
e
 
m
e
d
i
a


 
 
 
 
 
 
a
n
d
 
s
o
 
o
n
.




 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
"
/
>


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
d
b
7
a
b
4
c
a
-
2
a
3
f
-
4
1
8
3
-
9
2
4
3
-
c
1
2
0
8
d
a
9
2
3
9
2
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
c
h
i
n
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
a
c
h
i
n
e
 
v
a
l
u
e
 
f
o
r
 
'
m
a
c
h
i
n
e
'


 
 
 
 
 
 
 
 
M
a
c
h
i
n
e
 
o
b
j
e
c
t
 
f
o
r
 
t
h
i
s
 
c
o
n
s
o
l
e
 
s
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
i
s
 
a
 
c
o
n
v
e
n
i
e
n
c
e
 
p
r
o
p
e
r
t
y
,
 
i
t
 
h
a
s
 
t
h
e
 
s
a
m
e
 
v
a
l
u
e
 
a
s


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
e
s
s
i
o
n
:
:
m
a
c
h
i
n
e
"
/
>
 
o
f
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
s
e
s
s
i
o
n


 
 
 
 
 
 
 
 
 
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
c
h
i
n
e
'
,
 
I
M
a
c
h
i
n
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
t
a
t
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
M
a
c
h
i
n
e
S
t
a
t
e
 
v
a
l
u
e
 
f
o
r
 
'
s
t
a
t
e
'


 
 
 
 
 
 
 
 
C
u
r
r
e
n
t
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
p
r
o
p
e
r
t
y
 
a
l
w
a
y
s
 
r
e
t
u
r
n
s
 
t
h
e
 
s
a
m
e
 
v
a
l
u
e
 
a
s
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g


 
 
 
 
 
 
 
 
 
 
p
r
o
p
e
r
t
y
 
o
f
 
t
h
e
 
I
M
a
c
h
i
n
e
 
o
b
j
e
c
t
 
f
o
r
 
t
h
i
s
 
c
o
n
s
o
l
e
 
s
e
s
s
i
o
n
.


 
 
 
 
 
 
 
 
 
 
F
o
r
 
t
h
e
 
p
r
o
c
e
s
s
 
t
h
a
t
 
o
w
n
s
 
(
e
x
e
c
u
t
e
s
)
 
t
h
e
 
V
M
,
 
t
h
i
s
 
i
s
 
t
h
e


 
 
 
 
 
 
 
 
 
 
p
r
e
f
e
r
a
b
l
e
 
w
a
y
 
o
f
 
q
u
e
r
y
i
n
g
 
t
h
e
 
V
M
 
s
t
a
t
e
,
 
b
e
c
a
u
s
e
 
n
o
 
I
P
C


 
 
 
 
 
 
 
 
 
 
c
a
l
l
s
 
a
r
e
 
m
a
d
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
t
a
t
e
'
,
 
M
a
c
h
i
n
e
S
t
a
t
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
g
u
e
s
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
G
u
e
s
t
 
v
a
l
u
e
 
f
o
r
 
'
g
u
e
s
t
'


 
 
 
 
 
 
 
 
G
u
e
s
t
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
g
u
e
s
t
'
,
 
I
G
u
e
s
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
k
e
y
b
o
a
r
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
K
e
y
b
o
a
r
d
 
v
a
l
u
e
 
f
o
r
 
'
k
e
y
b
o
a
r
d
'


 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
k
e
y
b
o
a
r
d
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
r
u
n
n
i
n
g
,
 
a
n
y
 
a
t
t
e
m
p
t
 
t
o
 
u
s
e


 
 
 
 
 
 
 
 
 
 
t
h
e
 
r
e
t
u
r
n
e
d
 
o
b
j
e
c
t
 
w
i
l
l
 
r
e
s
u
l
t
 
i
n
 
a
n
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
k
e
y
b
o
a
r
d
'
,
 
I
K
e
y
b
o
a
r
d
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
o
u
s
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
o
u
s
e
 
v
a
l
u
e
 
f
o
r
 
'
m
o
u
s
e
'


 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
o
u
s
e
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
r
u
n
n
i
n
g
,
 
a
n
y
 
a
t
t
e
m
p
t
 
t
o
 
u
s
e


 
 
 
 
 
 
 
 
 
 
t
h
e
 
r
e
t
u
r
n
e
d
 
o
b
j
e
c
t
 
w
i
l
l
 
r
e
s
u
l
t
 
i
n
 
a
n
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
o
u
s
e
'
,
 
I
M
o
u
s
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
i
s
p
l
a
y
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
D
i
s
p
l
a
y
 
v
a
l
u
e
 
f
o
r
 
'
d
i
s
p
l
a
y
'


 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
d
i
s
p
l
a
y
 
o
b
j
e
c
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
r
u
n
n
i
n
g
,
 
a
n
y
 
a
t
t
e
m
p
t
 
t
o
 
u
s
e


 
 
 
 
 
 
 
 
 
 
t
h
e
 
r
e
t
u
r
n
e
d
 
o
b
j
e
c
t
 
w
i
l
l
 
r
e
s
u
l
t
 
i
n
 
a
n
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
i
s
p
l
a
y
'
,
 
I
D
i
s
p
l
a
y
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
b
u
g
g
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
a
c
h
i
n
e
D
e
b
u
g
g
e
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
b
u
g
g
e
r
'


 
 
 
 
 
 
 
 
D
e
b
u
g
g
i
n
g
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
b
u
g
g
e
r
'
,
 
I
M
a
c
h
i
n
e
D
e
b
u
g
g
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
s
b
_
d
e
v
i
c
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
U
S
B
D
e
v
i
c
e
 
v
a
l
u
e
 
f
o
r
 
'
U
S
B
D
e
v
i
c
e
s
'


 
 
 
 
 
 
 
 
C
o
l
l
e
c
t
i
o
n
 
o
f
 
U
S
B
 
d
e
v
i
c
e
s
 
c
u
r
r
e
n
t
l
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
v
i
r
t
u
a
l


 
 
 
 
 
 
 
 
U
S
B
 
c
o
n
t
r
o
l
l
e
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
o
l
l
e
c
t
i
o
n
 
i
s
 
e
m
p
t
y
 
i
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
n
o
t
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
U
S
B
D
e
v
i
c
e
s
'
,
 
I
U
S
B
D
e
v
i
c
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
m
o
t
e
_
u
s
b
_
d
e
v
i
c
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
 
v
a
l
u
e
 
f
o
r
 
'
r
e
m
o
t
e
U
S
B
D
e
v
i
c
e
s
'


 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
U
S
B
 
d
e
v
i
c
e
s
 
c
u
r
r
e
n
t
l
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
r
e
m
o
t
e
 
V
R
D
E
 
c
l
i
e
n
t
.


 
 
 
 
 
 
 
 
O
n
c
e
 
a
 
n
e
w
 
d
e
v
i
c
e
 
i
s
 
p
h
y
s
i
c
a
l
l
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
r
e
m
o
t
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
,


 
 
 
 
 
 
 
 
i
t
 
a
p
p
e
a
r
s
 
i
n
 
t
h
i
s
 
l
i
s
t
 
a
n
d
 
r
e
m
a
i
n
s
 
t
h
e
r
e
 
u
n
t
i
l
 
d
e
t
a
c
h
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
m
o
t
e
U
S
B
D
e
v
i
c
e
s
'
,
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
h
a
r
e
d
_
f
o
l
d
e
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
S
h
a
r
e
d
F
o
l
d
e
r
 
v
a
l
u
e
 
f
o
r
 
'
s
h
a
r
e
d
F
o
l
d
e
r
s
'


 
 
 
 
 
 
 
 
C
o
l
l
e
c
t
i
o
n
 
o
f
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
f
o
r
 
t
h
e
 
c
u
r
r
e
n
t
 
s
e
s
s
i
o
n
.
 
T
h
e
s
e
 
f
o
l
d
e
r
s


 
 
 
 
 
 
 
 
a
r
e
 
c
a
l
l
e
d
 
t
r
a
n
s
i
e
n
t
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
b
e
c
a
u
s
e
 
t
h
e
y
 
a
r
e
 
a
v
a
i
l
a
b
l
e
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
g
u
e
s
t
 
O
S
 
r
u
n
n
i
n
g
 
i
n
s
i
d
e
 
t
h
e
 
a
s
s
o
c
i
a
t
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
o
n
l
y
 
f
o
r
 
t
h
e


 
 
 
 
 
 
 
 
d
u
r
a
t
i
o
n
 
o
f
 
t
h
e
 
s
e
s
s
i
o
n
 
(
a
s
 
o
p
p
o
s
e
d
 
t
o


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
h
a
r
e
d
F
o
l
d
e
r
s
"
/
>
 
w
h
i
c
h
 
r
e
p
r
e
s
e
n
t
 
p
e
r
m
a
n
e
n
t
 
s
h
a
r
e
d


 
 
 
 
 
 
 
 
f
o
l
d
e
r
s
)
.
 
W
h
e
n
 
t
h
e
 
s
e
s
s
i
o
n
 
i
s
 
c
l
o
s
e
d
 
(
e
.
g
.
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
p
o
w
e
r
e
d
 
d
o
w
n
)
,


 
 
 
 
 
 
 
 
t
h
e
s
e
 
f
o
l
d
e
r
s
 
a
r
e
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
d
i
s
c
a
r
d
e
d
.




 
 
 
 
 
 
 
 
N
e
w
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
r
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
.
 
E
x
i
s
t
i
n
g
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
r
e
m
o
v
e
d
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
#
r
e
m
o
v
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
h
a
r
e
d
F
o
l
d
e
r
s
'
,
 
I
S
h
a
r
e
d
F
o
l
d
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
r
d
e
_
s
e
r
v
e
r
_
i
n
f
o
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
V
R
D
E
S
e
r
v
e
r
I
n
f
o
 
v
a
l
u
e
 
f
o
r
 
'
V
R
D
E
S
e
r
v
e
r
I
n
f
o
'


 
 
 
 
 
 
 
 
I
n
t
e
r
f
a
c
e
 
t
h
a
t
 
p
r
o
v
i
d
e
s
 
i
n
f
o
r
m
a
t
i
o
n
 
o
n
 
R
e
m
o
t
e
 
D
e
s
k
t
o
p
 
E
x
t
e
n
s
i
o
n
 
(
V
R
D
E
)
 
c
o
n
n
e
c
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
R
D
E
S
e
r
v
e
r
I
n
f
o
'
,
 
I
V
R
D
E
S
e
r
v
e
r
I
n
f
o
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
e
v
e
n
t
_
s
o
u
r
c
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
E
v
e
n
t
S
o
u
r
c
e
 
v
a
l
u
e
 
f
o
r
 
'
e
v
e
n
t
S
o
u
r
c
e
'


 
 
 
 
 
 
 
 
E
v
e
n
t
 
s
o
u
r
c
e
 
f
o
r
 
c
o
n
s
o
l
e
 
e
v
e
n
t
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
e
v
e
n
t
S
o
u
r
c
e
'
,
 
I
E
v
e
n
t
S
o
u
r
c
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
t
t
a
c
h
e
d
_
p
c
i
_
d
e
v
i
c
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
P
C
I
D
e
v
i
c
e
A
t
t
a
c
h
m
e
n
t
 
v
a
l
u
e
 
f
o
r
 
'
a
t
t
a
c
h
e
d
P
C
I
D
e
v
i
c
e
s
'


 
 
 
 
 
 
 
 
A
r
r
a
y
 
o
f
 
P
C
I
 
d
e
v
i
c
e
s
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
t
t
a
c
h
e
d
P
C
I
D
e
v
i
c
e
s
'
,
 
I
P
C
I
D
e
v
i
c
e
A
t
t
a
c
h
m
e
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
s
e
_
h
o
s
t
_
c
l
i
p
b
o
a
r
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
u
s
e
H
o
s
t
C
l
i
p
b
o
a
r
d
'


 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
g
u
e
s
t
 
c
l
i
p
b
o
a
r
d
 
s
h
o
u
l
d
 
b
e
 
c
o
n
n
e
c
t
e
d
 
t
o
 
t
h
e
 
h
o
s
t
 
o
n
e
 
o
r


 
 
 
 
 
 
 
 
w
h
e
t
h
e
r
 
i
t
 
s
h
o
u
l
d
 
o
n
l
y
 
b
e
 
a
l
l
o
w
e
d
 
a
c
c
e
s
s
 
t
o
 
t
h
e
 
V
R
D
E
 
c
l
i
p
b
o
a
r
d
.
 
T
h
i
s


 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
 
m
a
y
 
n
o
t
 
a
f
f
e
c
t
 
e
x
i
s
t
i
n
g
 
g
u
e
s
t
 
c
l
i
p
b
o
a
r
d
 
c
o
n
n
e
c
t
i
o
n
s
 
w
h
i
c
h


 
 
 
 
 
 
 
 
a
r
e
 
a
l
r
e
a
d
y
 
c
o
n
n
e
c
t
e
d
 
t
o
 
t
h
e
 
h
o
s
t
 
c
l
i
p
b
o
a
r
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
u
s
e
H
o
s
t
C
l
i
p
b
o
a
r
d
'
,
 
b
o
o
l
)




 
 
 
 
@
u
s
e
_
h
o
s
t
_
c
l
i
p
b
o
a
r
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
u
s
e
_
h
o
s
t
_
c
l
i
p
b
o
a
r
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
u
s
e
H
o
s
t
C
l
i
p
b
o
a
r
d
'
,
 
v
a
l
u
e
)




 
 
 
 
d
e
f
 
p
o
w
e
r
_
u
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
S
t
a
r
t
s
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
 
u
s
i
n
g
 
t
h
e
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
s
t
a
t
e
 
(
t
h
a
t
 
i
s
,
 
i
t
s
 
c
u
r
r
e
n
t
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
,
 
c
u
r
r
e
n
t
 
s
e
t
t
i
n
g
s
 
a
n
d


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
 
s
t
o
r
a
g
e
 
d
e
v
i
c
e
s
)
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
s
 
o
n
l
y
 
u
s
e
f
u
l
 
f
o
r
 
f
r
o
n
t
-
e
n
d
s
 
t
h
a
t
 
w
a
n
t
 
t
o
 
a
c
t
u
a
l
l
y


 
 
 
 
 
 
 
 
 
 
e
x
e
c
u
t
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
 
i
n
 
t
h
e
i
r
 
o
w
n
 
p
r
o
c
e
s
s
 
(
l
i
k
e
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
 
 
o
r
 
V
B
o
x
S
D
L
 
f
r
o
n
t
-
e
n
d
s
)
.
 
U
n
l
e
s
s
 
y
o
u
 
a
r
e
 
i
n
t
e
n
d
i
n
g
 
t
o
 
w
r
i
t
e
 
s
u
c
h
 
a


 
 
 
 
 
 
 
 
 
 
f
r
o
n
t
-
e
n
d
,
 
d
o
 
n
o
t
 
c
a
l
l
 
t
h
i
s
 
m
e
t
h
o
d
.
 
I
f
 
y
o
u
 
s
i
m
p
l
y
 
w
a
n
t
 
t
o


 
 
 
 
 
 
 
 
 
 
s
t
a
r
t
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
 
u
s
i
n
g
 
o
n
e
 
o
f
 
t
h
e
 
e
x
i
s
t
i
n
g
 
f
r
o
n
t
-
e
n
d
s


 
 
 
 
 
 
 
 
 
 
(
f
o
r
 
e
x
a
m
p
l
e
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
G
U
I
 
o
r
 
h
e
a
d
l
e
s
s
 
s
e
r
v
e
r
)
,
 
u
s
e


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
i
n
s
t
e
a
d
;
 
t
h
e
s
e


 
 
 
 
 
 
 
 
 
 
f
r
o
n
t
-
e
n
d
s
 
w
i
l
l
 
p
o
w
e
r
 
u
p
 
t
h
e
 
m
a
c
h
i
n
e
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
f
o
r
 
y
o
u
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
p
o
w
e
r
e
d
 
o
f
f
 
o
r
 
a
b
o
r
t
e
d
,
 
t
h
e
 
e
x
e
c
u
t
i
o
n
 
w
i
l
l


 
 
 
 
 
 
 
 
s
t
a
r
t
 
f
r
o
m
 
t
h
e
 
b
e
g
i
n
n
i
n
g
 
(
a
s
 
i
f
 
t
h
e
 
r
e
a
l
 
h
a
r
d
w
a
r
e
 
w
e
r
e
 
j
u
s
t


 
 
 
 
 
 
 
 
p
o
w
e
r
e
d
 
o
n
)
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
M
a
c
h
i
n
e
S
t
a
t
e
_
S
a
v
e
d
"
/
>
 
s
t
a
t
e
,


 
 
 
 
 
 
 
 
i
t
 
w
i
l
l
 
c
o
n
t
i
n
u
e
 
i
t
s
 
e
x
e
c
u
t
i
o
n
 
t
h
e
 
p
o
i
n
t
 
w
h
e
r
e
 
t
h
e
 
s
t
a
t
e
 
h
a
s


 
 
 
 
 
 
 
 
b
e
e
n
 
s
a
v
e
d
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
t
e
l
e
p
o
r
t
e
r
E
n
a
b
l
e
d
"
/
>
 
p
r
o
p
e
r
t
y
 
i
s


 
 
 
 
 
 
 
 
e
n
a
b
l
e
d
 
o
n
 
t
h
e
 
m
a
c
h
i
n
e
 
b
e
i
n
g
 
p
o
w
e
r
e
d
 
u
p
,
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
w
a
i
t
 
f
o
r
 
a
n


 
 
 
 
 
 
 
 
i
n
c
o
m
i
n
g
 
t
e
l
e
p
o
r
t
a
t
i
o
n
 
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
M
a
c
h
i
n
e
S
t
a
t
e
_
T
e
l
e
p
o
r
t
i
n
g
I
n
"
/
>


 
 
 
 
 
 
 
 
s
t
a
t
e
.
 
T
h
e
 
r
e
t
u
r
n
e
d
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
w
i
l
l
 
h
a
v
e
 
a
t
 
l
e
a
s
t
 
t
h
r
e
e


 
 
 
 
 
 
 
 
o
p
e
r
a
t
i
o
n
s
 
w
h
e
r
e
 
t
h
e
 
l
a
s
t
 
t
h
r
e
e
 
a
r
e
 
d
e
f
i
n
e
d
 
a
s
:
 
(
1
)
 
p
o
w
e
r
i
n
g
 
u
p
 
a
n
d


 
 
 
 
 
 
 
 
s
t
a
r
t
i
n
g
 
T
C
P
 
s
e
r
v
e
r
,
 
(
2
)
 
w
a
i
t
i
n
g
 
f
o
r
 
i
n
c
o
m
i
n
g
 
t
e
l
e
p
o
r
t
a
t
i
o
n
s
,
 
a
n
d


 
 
 
 
 
 
 
 
(
3
)
 
p
e
r
f
o
r
m
 
t
e
l
e
p
o
r
t
a
t
i
o
n
.
 
T
h
e
s
e
 
o
p
e
r
a
t
i
o
n
s
 
w
i
l
l
 
b
e
 
r
e
f
l
e
c
t
e
d
 
a
s
 
t
h
e


 
 
 
 
 
 
 
 
l
a
s
t
 
t
h
r
e
e
 
o
p
e
r
a
t
i
o
n
s
 
o
f
 
t
h
e
 
p
r
o
g
r
e
s
s
 
o
b
j
e
c
t
e
d
 
r
e
t
u
r
n
e
d
 
b
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
a
s
 
w
e
l
l
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
t
a
t
e
"
/
>




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
a
l
r
e
a
d
y
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
H
O
S
T
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
H
o
s
t
 
i
n
t
e
r
f
a
c
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
 
o
r
 
n
a
m
e
 
n
o
t
 
s
e
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
o
w
e
r
U
p
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
p
o
w
e
r
_
u
p
_
p
a
u
s
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
I
d
e
n
t
i
c
a
l
 
t
o
 
p
o
w
e
r
U
p
 
e
x
c
e
p
t
 
t
h
a
t
 
t
h
e
 
V
M
 
w
i
l
l
 
e
n
t
e
r
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
M
a
c
h
i
n
e
S
t
a
t
e
_
P
a
u
s
e
d
"
/
>
 
s
t
a
t
e
,
 
i
n
s
t
e
a
d
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
M
a
c
h
i
n
e
S
t
a
t
e
_
R
u
n
n
i
n
g
"
/
>
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
p
o
w
e
r
U
p
"
/
>




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
a
l
r
e
a
d
y
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
H
O
S
T
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
H
o
s
t
 
i
n
t
e
r
f
a
c
e
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
 
o
r
 
n
a
m
e
 
n
o
t
 
s
e
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
o
w
e
r
U
p
P
a
u
s
e
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
p
o
w
e
r
_
d
o
w
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
I
n
i
t
i
a
t
e
s
 
t
h
e
 
p
o
w
e
r
 
d
o
w
n
 
p
r
o
c
e
d
u
r
e
 
t
o
 
s
t
o
p
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
 
 
T
h
e
 
c
o
m
p
l
e
t
i
o
n
 
o
f
 
t
h
e
 
p
o
w
e
r
 
d
o
w
n
 
p
r
o
c
e
d
u
r
e
 
i
s
 
t
r
a
c
k
e
d
 
u
s
i
n
g
 
t
h
e
 
r
e
t
u
r
n
e
d


 
 
 
 
 
 
 
 
I
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
.
 
A
f
t
e
r
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
i
s
 
c
o
m
p
l
e
t
e
,
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
g
o


 
 
 
 
 
 
 
 
t
o
 
t
h
e
 
P
o
w
e
r
e
d
O
f
f
 
s
t
a
t
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
m
u
s
t
 
b
e
 
R
u
n
n
i
n
g
,
 
P
a
u
s
e
d
 
o
r
 
S
t
u
c
k
 
t
o
 
b
e
 
p
o
w
e
r
e
d
 
d
o
w
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
o
w
e
r
D
o
w
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
s
e
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
s
e
t
s
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
i
n
 
R
u
n
n
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
V
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
r
r
o
r
 
i
n
 
r
e
s
e
t
 
o
p
e
r
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
s
e
t
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
p
a
u
s
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
P
a
u
s
e
s
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
i
n
 
R
u
n
n
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
V
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
r
r
o
r
 
i
n
 
s
u
s
p
e
n
d
 
o
p
e
r
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
a
u
s
e
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
s
u
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
s
u
m
e
s
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
i
n
 
P
a
u
s
e
d
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
V
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
e
r
r
o
r
 
i
n
 
r
e
s
u
m
e
 
o
p
e
r
a
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
s
u
m
e
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
p
o
w
e
r
_
b
u
t
t
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
n
d
s
 
t
h
e
 
A
C
P
I
 
p
o
w
e
r
 
b
u
t
t
o
n
 
e
v
e
n
t
 
t
o
 
t
h
e
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
i
n
 
R
u
n
n
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
o
n
t
r
o
l
l
e
d
 
p
o
w
e
r
 
o
f
f
 
f
a
i
l
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
p
o
w
e
r
B
u
t
t
o
n
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
l
e
e
p
_
b
u
t
t
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
n
d
s
 
t
h
e
 
A
C
P
I
 
s
l
e
e
p
 
b
u
t
t
o
n
 
e
v
e
n
t
 
t
o
 
t
h
e
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
i
n
 
R
u
n
n
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
e
n
d
i
n
g
 
s
l
e
e
p
 
b
u
t
t
o
n
 
e
v
e
n
t
 
f
a
i
l
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
l
e
e
p
B
u
t
t
o
n
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
p
o
w
e
r
_
b
u
t
t
o
n
_
h
a
n
d
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
C
h
e
c
k
s
 
i
f
 
t
h
e
 
l
a
s
t
 
p
o
w
e
r
 
b
u
t
t
o
n
 
e
v
e
n
t
 
w
a
s
 
h
a
n
d
l
e
d
 
b
y
 
g
u
e
s
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
h
a
n
d
l
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
C
h
e
c
k
i
n
g
 
i
f
 
t
h
e
 
e
v
e
n
t
 
w
a
s
 
h
a
n
d
l
e
d
 
b
y
 
t
h
e
 
g
u
e
s
t
 
O
S
 
f
a
i
l
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
h
a
n
d
l
e
d
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
P
o
w
e
r
B
u
t
t
o
n
H
a
n
d
l
e
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
h
a
n
d
l
e
d


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
g
u
e
s
t
_
e
n
t
e
r
e
d
_
a
c
p
i
_
m
o
d
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
C
h
e
c
k
s
 
i
f
 
t
h
e
 
g
u
e
s
t
 
e
n
t
e
r
e
d
 
t
h
e
 
A
C
P
I
 
m
o
d
e
 
G
0
 
(
w
o
r
k
i
n
g
)
 
o
r


 
 
 
 
 
 
 
 
G
1
 
(
s
l
e
e
p
i
n
g
)
.
 
I
f
 
t
h
i
s
 
m
e
t
h
o
d
 
r
e
t
u
r
n
s
 
@
c
 
f
a
l
s
e
,
 
t
h
e
 
g
u
e
s
t
 
w
i
l
l


 
 
 
 
 
 
 
 
m
o
s
t
 
l
i
k
e
l
y
 
n
o
t
 
r
e
s
p
o
n
d
 
t
o
 
e
x
t
e
r
n
a
l
 
A
C
P
I
 
e
v
e
n
t
s
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
n
t
e
r
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
i
n
 
R
u
n
n
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
e
n
t
e
r
e
d
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
G
u
e
s
t
E
n
t
e
r
e
d
A
C
P
I
M
o
d
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
n
t
e
r
e
d


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
s
a
v
e
_
s
t
a
t
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
S
a
v
e
s
 
t
h
e
 
c
u
r
r
e
n
t
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
o
f
 
a
 
r
u
n
n
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
a
n
d
 
s
t
o
p
s
 
i
t
s
 
e
x
e
c
u
t
i
o
n
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
e
s
,
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
g
o
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
S
a
v
e
d
 
s
t
a
t
e
.
 
N
e
x
t
 
t
i
m
e
 
i
t
 
i
s
 
p
o
w
e
r
e
d
 
u
p
,
 
t
h
i
s
 
s
t
a
t
e
 
w
i
l
l


 
 
 
 
 
 
 
 
b
e
 
r
e
s
t
o
r
e
d
 
a
n
d
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
c
o
n
t
i
n
u
e
 
i
t
s
 
e
x
e
c
u
t
i
o
n
 
f
r
o
m


 
 
 
 
 
 
 
 
t
h
e
 
p
l
a
c
e
 
w
h
e
r
e
 
i
t
 
w
a
s
 
s
a
v
e
d
.




 
 
 
 
 
 
 
 
T
h
i
s
 
o
p
e
r
a
t
i
o
n
 
d
i
f
f
e
r
s
 
f
r
o
m
 
t
a
k
i
n
g
 
a
 
s
n
a
p
s
h
o
t
 
t
o
 
t
h
e
 
e
f
f
e
c
t


 
 
 
 
 
 
 
 
t
h
a
t
 
i
t
 
d
o
e
s
n
'
t
 
c
r
e
a
t
e
 
n
e
w
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
.
 
A
l
s
o
,
 
o
n
c
e


 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
p
o
w
e
r
e
d
 
u
p
 
f
r
o
m
 
t
h
e
 
s
t
a
t
e
 
s
a
v
e
d
 
u
s
i
n
g
 
t
h
i
s
 
m
e
t
h
o
d
,


 
 
 
 
 
 
 
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
i
s
 
d
e
l
e
t
e
d
,
 
s
o
 
i
t
 
w
i
l
l
 
b
e
 
i
m
p
o
s
s
i
b
l
e
 
t
o
 
r
e
t
u
r
n


 
 
 
 
 
 
 
 
t
o
 
t
h
i
s
 
s
t
a
t
e
 
l
a
t
e
r
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
O
n
 
s
u
c
c
e
s
s
,
 
t
h
i
s
 
m
e
t
h
o
d
 
i
m
p
l
i
c
i
t
l
y
 
c
a
l
l
s


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
t
o
 
s
a
v
e
 
a
l
l
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
s
 
(
i
n
c
l
u
d
i
n
g
 
r
u
n
t
i
m
e
 
c
h
a
n
g
e
s
 
t
o
 
t
h
e
 
D
V
D
 
m
e
d
i
u
m
,
 
e
t
c
.
)
.


 
 
 
 
 
 
 
 
 
 
T
o
g
e
t
h
e
r
 
w
i
t
h
 
t
h
e
 
i
m
p
o
s
s
i
b
i
l
i
t
y
 
t
o
 
c
h
a
n
g
e
 
a
n
y
 
V
M
 
s
e
t
t
i
n
g
s
 
w
h
e
n
 
i
t
 
i
s


 
 
 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
S
a
v
e
d
 
s
t
a
t
e
,
 
t
h
i
s
 
g
u
a
r
a
n
t
e
e
s
 
a
d
e
q
u
a
t
e
 
h
a
r
d
w
a
r
e


 
 
 
 
 
 
 
 
 
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
w
h
e
n
 
i
t
 
i
s
 
r
e
s
t
o
r
e
d
 
f
r
o
m
 
t
h
e
 
s
a
v
e
d


 
 
 
 
 
 
 
 
 
 
s
t
a
t
e
 
f
i
l
e
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
c
h
i
n
e
 
m
u
s
t
 
b
e
 
i
n
 
t
h
e
 
R
u
n
n
i
n
g
 
o
r
 
P
a
u
s
e
d
 
s
t
a
t
e
,
 
o
t
h
e
r
w
i
s
e


 
 
 
 
 
 
 
 
 
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
w
i
l
l
 
f
a
i
l
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
t
a
k
e
S
n
a
p
s
h
o
t
"
/
>




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
n
e
i
t
h
e
r
 
R
u
n
n
i
n
g
 
n
o
r
 
P
a
u
s
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
F
a
i
l
e
d
 
t
o
 
c
r
e
a
t
e
 
d
i
r
e
c
t
o
r
y
 
f
o
r
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
s
a
v
e
S
t
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
d
o
p
t
_
s
a
v
e
d
_
s
t
a
t
e
(
s
e
l
f
,
 
s
a
v
e
d
_
s
t
a
t
e
_
f
i
l
e
)
:


 
 
 
 
 
 
 
 
"
"
"
A
s
s
o
c
i
a
t
e
s
 
t
h
e
 
g
i
v
e
n
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
t
o
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
O
n
 
s
u
c
c
e
s
s
,
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
g
o
 
t
o
 
t
h
e
 
S
a
v
e
d
 
s
t
a
t
e
.
 
N
e
x
t
 
t
i
m
e
 
i
t
 
i
s


 
 
 
 
 
 
 
 
p
o
w
e
r
e
d
 
u
p
,
 
i
t
 
w
i
l
l
 
b
e
 
r
e
s
t
o
r
e
d
 
f
r
o
m
 
t
h
e
 
a
d
o
p
t
e
d
 
s
a
v
e
d
 
s
t
a
t
e
 
a
n
d


 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e
 
e
x
e
c
u
t
i
o
n
 
f
r
o
m
 
t
h
e
 
p
l
a
c
e
 
w
h
e
r
e
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
w
a
s


 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
.




 
 
 
 
 
 
 
 
T
h
e
 
s
p
e
c
i
f
i
e
d
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
p
a
t
h
 
m
a
y
 
b
e
 
a
b
s
o
l
u
t
e
 
o
r
 
r
e
l
a
t
i
v
e
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
f
o
l
d
e
r
 
t
h
e
 
V
M
 
n
o
r
m
a
l
l
y
 
s
a
v
e
s
 
t
h
e
 
s
t
a
t
e
 
t
o
 
(
u
s
u
a
l
l
y
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
n
a
p
s
h
o
t
F
o
l
d
e
r
"
/
>
)
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
t
'
s
 
a
 
c
a
l
l
e
r
'
s
 
r
e
s
p
o
n
s
i
b
i
l
i
t
y
 
t
o
 
m
a
k
e
 
s
u
r
e
 
t
h
e
 
g
i
v
e
n
 
s
a
v
e
d
 
s
t
a
t
e


 
 
 
 
 
 
 
 
 
 
f
i
l
e
 
i
s
 
c
o
m
p
a
t
i
b
l
e
 
w
i
t
h
 
t
h
e
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
i
s
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
t
h
a
t


 
 
 
 
 
 
 
 
 
 
r
e
p
r
e
s
e
n
t
 
i
t
s
 
v
i
r
t
u
a
l
 
h
a
r
d
w
a
r
e
 
(
m
e
m
o
r
y
 
s
i
z
e
,
 
s
t
o
r
a
g
e
 
d
i
s
k
 
c
o
n
f
i
g
u
r
a
t
i
o
n


 
 
 
 
 
 
 
 
 
 
e
t
c
.
)
.
 
I
f
 
t
h
e
r
e
 
i
s
 
a
 
m
i
s
m
a
t
c
h
,
 
t
h
e
 
b
e
h
a
v
i
o
r
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
i
s
 
u
n
d
e
f
i
n
e
d
.




 
 
 
 
 
 
 
 
i
n
 
s
a
v
e
d
_
s
t
a
t
e
_
f
i
l
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
P
a
t
h
 
t
o
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
t
o
 
a
d
o
p
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
n
e
i
t
h
e
r
 
P
o
w
e
r
e
d
O
f
f
 
n
o
r
 
A
b
o
r
t
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
d
o
p
t
S
a
v
e
d
S
t
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
a
v
e
d
_
s
t
a
t
e
_
f
i
l
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
i
s
c
a
r
d
_
s
a
v
e
d
_
s
t
a
t
e
(
s
e
l
f
,
 
f
_
r
e
m
o
v
e
_
f
i
l
e
)
:


 
 
 
 
 
 
 
 
"
"
"
F
o
r
c
i
b
l
y
 
r
e
s
e
t
s
 
t
h
e
 
m
a
c
h
i
n
e
 
t
o
 
"
P
o
w
e
r
e
d
 
O
f
f
"
 
s
t
a
t
e
 
i
f
 
i
t
 
i
s


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
l
y
 
i
n
 
t
h
e
 
"
S
a
v
e
d
"
 
s
t
a
t
e
 
(
p
r
e
v
i
o
u
s
l
y
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
t
a
t
e
"
/
>
)
.


 
 
 
 
 
 
 
 
N
e
x
t
 
t
i
m
e
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
p
o
w
e
r
e
d
 
u
p
,
 
a
 
c
l
e
a
n
 
b
o
o
t
 
w
i
l
l
 
o
c
c
u
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
e
q
u
i
v
a
l
e
n
t
 
t
o
 
r
e
s
e
t
t
i
n
g
 
o
r
 
p
o
w
e
r
i
n
g
 
o
f
f


 
 
 
 
 
 
 
 
 
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
t
h
o
u
t
 
d
o
i
n
g
 
a
 
p
r
o
p
e
r
 
s
h
u
t
d
o
w
n
 
o
f
 
t
h
e
 
g
u
e
s
t


 
 
 
 
 
 
 
 
 
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
;
 
a
s
 
w
i
t
h
 
r
e
s
e
t
t
i
n
g
 
a
 
r
u
n
n
i
n
g
 
p
h
y
i
s
c
a
l


 
 
 
 
 
 
 
 
 
 
c
o
m
p
u
t
e
r
,
 
i
t
 
c
a
n
 
c
a
n
 
l
e
a
d
 
t
o
 
d
a
t
a
 
l
o
s
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
I
f
 
@
a
 
f
R
e
m
o
v
e
F
i
l
e
 
i
s
 
@
c
 
t
r
u
e
,
 
t
h
e
 
f
i
l
e
 
i
n
 
t
h
e
 
m
a
c
h
i
n
e
 
d
i
r
e
c
t
o
r
y


 
 
 
 
 
 
 
 
i
n
t
o
 
w
h
i
c
h
 
t
h
e
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
w
a
s
 
s
a
v
e
d
 
i
s
 
a
l
s
o
 
d
e
l
e
t
e
d
.
 
I
f


 
 
 
 
 
 
 
 
t
h
i
s
 
i
s
 
@
c
 
f
a
l
s
e
,
 
t
h
e
n
 
t
h
e
 
s
t
a
t
e
 
c
a
n
 
b
e
 
r
e
c
o
v
e
r
e
d
 
a
n
d
 
l
a
t
e
r


 
 
 
 
 
 
 
 
r
e
-
i
n
s
e
r
t
e
d
 
i
n
t
o
 
a
 
m
a
c
h
i
n
e
 
u
s
i
n
g
 
<
l
i
n
k
 
t
o
=
"
#
a
d
o
p
t
S
a
v
e
d
S
t
a
t
e
"
/
>
.


 
 
 
 
 
 
 
 
T
h
e
 
l
o
c
a
t
i
o
n
 
o
f
 
t
h
e
 
f
i
l
e
 
c
a
n
 
b
e
 
f
o
u
n
d
 
i
n
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
t
a
t
e
F
i
l
e
P
a
t
h
"
/
>
 
a
t
t
r
i
b
u
t
e
.




 
 
 
 
 
 
 
 
i
n
 
f
_
r
e
m
o
v
e
_
f
i
l
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
o
 
a
l
s
o
 
r
e
m
o
v
e
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
i
n
 
s
t
a
t
e
 
S
a
v
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
i
s
c
a
r
d
S
a
v
e
d
S
t
a
t
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
f
_
r
e
m
o
v
e
_
f
i
l
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
d
e
v
i
c
e
_
a
c
t
i
v
i
t
y
(
s
e
l
f
,
 
t
y
p
e
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
s
 
t
h
e
 
c
u
r
r
e
n
t
 
a
c
t
i
v
i
t
y
 
t
y
p
e
 
o
f
 
a
 
g
i
v
e
n
 
d
e
v
i
c
e
 
o
r
 
d
e
v
i
c
e
 
g
r
o
u
p
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
T
y
p
e




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
c
t
i
v
i
t
y
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
A
c
t
i
v
i
t
y




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
I
n
v
a
l
i
d
 
d
e
v
i
c
e
 
t
y
p
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
a
c
t
i
v
i
t
y
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
D
e
v
i
c
e
A
c
t
i
v
i
t
y
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
t
y
p
e
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
D
e
v
i
c
e
A
c
t
i
v
i
t
y
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
c
t
i
v
i
t
y


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
a
t
t
a
c
h
_
u
s
b
_
d
e
v
i
c
e
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
A
t
t
a
c
h
e
s
 
a
 
h
o
s
t
 
U
S
B
 
d
e
v
i
c
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
U
U
I
D
 
t
o
 
t
h
e


 
 
 
 
 
 
 
 
U
S
B
 
c
o
n
t
r
o
l
l
e
r
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
T
h
e
 
d
e
v
i
c
e
 
n
e
e
d
s
 
t
o
 
b
e
 
i
n
 
o
n
e
 
o
f
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
t
a
t
e
s
:


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
B
u
s
y
"
/
>
,


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
A
v
a
i
l
a
b
l
e
"
/
>
 
o
r


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
H
e
l
d
"
/
>
,


 
 
 
 
 
 
 
 
o
t
h
e
r
w
i
s
e
 
a
n
 
e
r
r
o
r
 
i
s
 
i
m
m
e
d
i
a
t
e
l
y
 
r
e
t
u
r
n
e
d
.




 
 
 
 
 
 
 
 
W
h
e
n
 
t
h
e
 
d
e
v
i
c
e
 
s
t
a
t
e
 
i
s


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
_
B
u
s
y
"
>
B
u
s
y
<
/
l
i
n
k
>
,
 
a
n
 
e
r
r
o
r
 
m
a
y
 
a
l
s
o


 
 
 
 
 
 
 
 
b
e
 
r
e
t
u
r
n
e
d
 
i
f
 
t
h
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
 
r
e
f
u
s
e
s
 
t
o
 
r
e
l
e
a
s
e
 
i
t
 
f
o
r
 
s
o
m
e
 
r
e
a
s
o
n
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
U
S
B
C
o
n
t
r
o
l
l
e
r
:
:
d
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>
,


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
"
/
>




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
h
o
s
t
 
U
S
B
 
d
e
v
i
c
e
 
t
o
 
a
t
t
a
c
h
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
n
e
i
t
h
e
r
 
R
u
n
n
i
n
g
 
n
o
r
 
P
a
u
s
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
d
o
e
s
 
n
o
t
 
h
a
v
e
 
a
 
U
S
B
 
c
o
n
t
r
o
l
l
e
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
a
t
t
a
c
h
U
S
B
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
t
a
c
h
_
u
s
b
_
d
e
v
i
c
e
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
D
e
t
a
c
h
e
s
 
a
n
 
U
S
B
 
d
e
v
i
c
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
U
U
I
D
 
f
r
o
m
 
t
h
e
 
U
S
B
 
c
o
n
t
r
o
l
l
e
r


 
 
 
 
 
 
 
 
o
f
 
t
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
i
s
 
m
e
t
h
o
d
 
s
u
c
c
e
e
d
s
,
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
s
e
r
v
e
r
 
r
e
-
i
n
i
t
i
a
t
e
s


 
 
 
 
 
 
 
 
a
l
l
 
U
S
B
 
f
i
l
t
e
r
s
 
a
s
 
i
f
 
t
h
e
 
d
e
v
i
c
e
 
w
e
r
e
 
j
u
s
t
 
p
h
y
s
i
c
a
l
l
y
 
a
t
t
a
c
h
e
d


 
 
 
 
 
 
 
 
t
o
 
t
h
e
 
h
o
s
t
,
 
b
u
t
 
f
i
l
t
e
r
s
 
o
f
 
t
h
i
s
 
m
a
c
h
i
n
e
 
a
r
e
 
i
g
n
o
r
e
d
 
t
o
 
a
v
o
i
d


 
 
 
 
 
 
 
 
a
 
p
o
s
s
i
b
l
e
 
a
u
t
o
m
a
t
i
c
 
r
e
-
a
t
t
a
c
h
m
e
n
t
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
U
S
B
C
o
n
t
r
o
l
l
e
r
:
:
d
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>
,


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
"
/
>




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
U
S
B
 
d
e
v
i
c
e
 
t
o
 
d
e
t
a
c
h
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
I
U
S
B
D
e
v
i
c
e


 
 
 
 
 
 
 
 
 
 
 
 
D
e
t
a
c
h
e
d
 
U
S
B
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
P
D
M
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
d
o
e
s
 
n
o
t
 
h
a
v
e
 
a
 
U
S
B
 
c
o
n
t
r
o
l
l
e
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
U
S
B
 
d
e
v
i
c
e
 
n
o
t
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
i
s
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
t
a
c
h
U
S
B
D
e
v
i
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
U
S
B
D
e
v
i
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
u
s
b
_
d
e
v
i
c
e
_
b
y
_
a
d
d
r
e
s
s
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
f
o
r
 
a
 
U
S
B
 
d
e
v
i
c
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
h
o
s
t
 
a
d
d
r
e
s
s
.




 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
U
S
B
D
e
v
i
c
e
:
:
a
d
d
r
e
s
s
"
/
>




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
d
d
r
e
s
s
 
o
f
 
t
h
e
 
U
S
B
 
d
e
v
i
c
e
 
(
a
s
 
a
s
s
i
g
n
e
d
 
b
y
 
t
h
e
 
h
o
s
t
)
 
t
o


 
 
 
 
 
 
 
 
 
 
s
e
a
r
c
h
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
I
U
S
B
D
e
v
i
c
e


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
U
S
B
 
d
e
v
i
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
G
i
v
e
n
 
@
c
 
n
a
m
e
 
d
o
e
s
 
n
o
t
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
U
S
B
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
U
S
B
D
e
v
i
c
e
B
y
A
d
d
r
e
s
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
U
S
B
D
e
v
i
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
u
s
b
_
d
e
v
i
c
e
_
b
y
_
i
d
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
f
o
r
 
a
 
U
S
B
 
d
e
v
i
c
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
U
U
I
D
.




 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
U
S
B
D
e
v
i
c
e
:
:
i
d
"
/
>




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
U
S
B
 
d
e
v
i
c
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
I
U
S
B
D
e
v
i
c
e


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
U
S
B
 
d
e
v
i
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
G
i
v
e
n
 
@
c
 
i
d
 
d
o
e
s
 
n
o
t
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
U
S
B
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
U
S
B
D
e
v
i
c
e
B
y
I
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
U
S
B
D
e
v
i
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
s
h
a
r
e
d
_
f
o
l
d
e
r
(
s
e
l
f
,
 
n
a
m
e
,
 
h
o
s
t
_
p
a
t
h
,
 
w
r
i
t
a
b
l
e
,
 
a
u
t
o
m
o
u
n
t
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
t
r
a
n
s
i
e
n
t
 
n
e
w
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
b
y
 
a
s
s
o
c
i
a
t
i
n
g
 
t
h
e
 
g
i
v
e
n
 
l
o
g
i
c
a
l


 
 
 
 
 
 
 
 
n
a
m
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
h
o
s
t
 
p
a
t
h
,
 
a
d
d
s
 
i
t
 
t
o
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
o
f
 
s
h
a
r
e
d


 
 
 
 
 
 
 
 
f
o
l
d
e
r
s
 
a
n
d
 
s
t
a
r
t
s
 
s
h
a
r
i
n
g
 
i
t
.
 
R
e
f
e
r
 
t
o
 
t
h
e
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
 
t
o
 
r
e
a
d
 
m
o
r
e
 
a
b
o
u
t
 
l
o
g
i
c
a
l
 
n
a
m
e
s
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
n
i
q
u
e
 
l
o
g
i
c
a
l
 
n
a
m
e
 
o
f
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
.




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
_
p
a
t
h
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
i
n
 
t
h
e
 
h
o
s
t
 
f
i
l
e
 
s
y
s
t
e
m
.




 
 
 
 
 
 
 
 
i
n
 
w
r
i
t
a
b
l
e
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
s
h
a
r
e
 
i
s
 
w
r
i
t
a
b
l
e
 
o
r
 
r
e
a
d
o
n
l
y




 
 
 
 
 
 
 
 
i
n
 
a
u
t
o
m
o
u
n
t
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
W
h
e
t
h
e
r
 
t
h
e
 
s
h
a
r
e
 
g
e
t
s
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
m
o
u
n
t
e
d
 
b
y
 
t
h
e
 
g
u
e
s
t


 
 
 
 
 
 
 
 
 
 
o
r
 
n
o
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
n
 
S
a
v
e
d
 
s
t
a
t
e
 
o
r
 
c
u
r
r
e
n
t
l
y
 
c
h
a
n
g
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
h
a
r
e
d
 
f
o
l
d
e
r
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
 
o
r
 
n
o
t
 
a
c
c
e
s
s
i
b
l
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
h
o
s
t
_
p
a
t
h
,
 
w
r
i
t
a
b
l
e
,
 
a
u
t
o
m
o
u
n
t
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
s
h
a
r
e
d
_
f
o
l
d
e
r
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
a
 
t
r
a
n
s
i
e
n
t
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
n
a
m
e
 
p
r
e
v
i
o
u
s
l
y


 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
 
b
y
 
<
l
i
n
k
 
t
o
=
"
#
c
r
e
a
t
e
S
h
a
r
e
d
F
o
l
d
e
r
"
/
>
 
f
r
o
m
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
s
h
a
r
e
d
 
f
o
l
d
e
r
s
 
a
n
d
 
s
t
o
p
s
 
s
h
a
r
i
n
g
 
i
t
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
L
o
g
i
c
a
l
 
n
a
m
e
 
o
f
 
t
h
e
 
s
h
a
r
e
d
 
f
o
l
d
e
r
 
t
o
 
r
e
m
o
v
e
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
n
 
S
a
v
e
d
 
s
t
a
t
e
 
o
r
 
c
u
r
r
e
n
t
l
y
 
c
h
a
n
g
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
F
I
L
E
_
E
R
R
O
R


 
 
 
 
 
 
 
 
 
 
 
 
S
h
a
r
e
d
 
f
o
l
d
e
r
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
S
h
a
r
e
d
F
o
l
d
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
t
a
k
e
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
n
a
m
e
,
 
d
e
s
c
r
i
p
t
i
o
n
)
:


 
 
 
 
 
 
 
 
"
"
"
S
a
v
e
s
 
t
h
e
 
c
u
r
r
e
n
t
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e


 
 
 
 
 
 
 
 
a
n
d
 
a
l
l
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
 
a
n
d
 
c
r
e
a
t
e
s
 
d
i
f
f
e
r
e
n
c
i
n
g
 
i
m
a
g
e
s


 
 
 
 
 
 
 
 
f
o
r
 
a
l
l
 
n
o
r
m
a
l
 
(
n
o
n
-
i
n
d
e
p
e
n
d
e
n
t
)
 
m
e
d
i
a
.


 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
"
/
>
 
f
o
r
 
a
n
 
i
n
t
r
o
d
u
c
t
i
o
n
 
t
o
 
s
n
a
p
s
h
o
t
s
.




 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
c
a
n
 
b
e
 
c
a
l
l
e
d
 
f
o
r
 
a
 
P
o
w
e
r
e
d
O
f
f
,
 
S
a
v
e
d
 
(
s
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
s
a
v
e
S
t
a
t
e
"
/
>
)
,
 
R
u
n
n
i
n
g
 
o
r


 
 
 
 
 
 
 
 
P
a
u
s
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
.
 
W
h
e
n
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
P
o
w
e
r
e
d
O
f
f
,
 
a
n


 
 
 
 
 
 
 
 
o
f
f
l
i
n
e
 
s
n
a
p
s
h
o
t
 
i
s
 
c
r
e
a
t
e
d
.
 
W
h
e
n
 
t
h
e
 
m
a
c
h
i
n
e
 
i
s
 
R
u
n
n
i
n
g
 
a
 
l
i
v
e


 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
 
i
s
 
c
r
e
a
t
e
d
,
 
a
n
d
 
a
n
 
o
n
l
i
n
e
 
s
n
a
p
s
h
o
t
 
i
s
 
c
r
e
a
t
e
d
 
w
h
e
n
 
P
a
u
s
e
d
.




 
 
 
 
 
 
 
 
T
h
e
 
t
a
k
e
n
 
s
n
a
p
s
h
o
t
 
i
s
 
a
l
w
a
y
s
 
b
a
s
e
d
 
o
n
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
c
u
r
r
e
n
t
S
n
a
p
s
h
o
t
"
>
c
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
<
/
l
i
n
k
>


 
 
 
 
 
 
 
 
o
f
 
t
h
e
 
a
s
s
o
c
i
a
t
e
d
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
a
n
d
 
b
e
c
o
m
e
s
 
a
 
n
e
w
 
c
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
i
s
 
m
e
t
h
o
d
 
i
m
p
l
i
c
i
t
l
y
 
c
a
l
l
s
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>
 
t
o


 
 
 
 
 
 
 
 
 
 
s
a
v
e
 
a
l
l
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
b
e
f
o
r
e
 
t
a
k
i
n
g
 
a
n
 
o
f
f
l
i
n
e
 
s
n
a
p
s
h
o
t
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
S
h
o
r
t
 
n
a
m
e
 
f
o
r
 
t
h
e
 
s
n
a
p
s
h
o
t
.




 
 
 
 
 
 
 
 
i
n
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
O
p
t
i
o
n
a
l
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
h
e
 
s
n
a
p
s
h
o
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
c
u
r
r
e
n
t
l
y
 
c
h
a
n
g
i
n
g
 
s
t
a
t
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
t
a
k
e
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
,
 
d
e
s
c
r
i
p
t
i
o
n
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
l
e
t
e
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
S
t
a
r
t
s
 
d
e
l
e
t
i
n
g
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
s
n
a
p
s
h
o
t
 
a
s
y
n
c
h
r
o
n
o
u
s
l
y
.


 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
"
/
>
 
f
o
r
 
a
n
 
i
n
t
r
o
d
u
c
t
i
o
n
 
t
o
 
s
n
a
p
s
h
o
t
s
.




 
 
 
 
 
 
 
 
T
h
e
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
a
n
d
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
e
 
a
s
s
o
c
i
a
t
e
d
 
m
a
c
h
i
n
e
 
s
t
o
r
e
d
 
i
n


 
 
 
 
 
 
 
 
t
h
e
 
s
n
a
p
s
h
o
t
 
w
i
l
l
 
b
e
 
d
e
l
e
t
e
d
.
 
T
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
a
l
l
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
 
o
f


 
 
 
 
 
 
 
 
t
h
i
s
 
s
n
a
p
s
h
o
t
 
w
i
l
l
 
b
e
 
m
e
r
g
e
d
 
w
i
t
h
 
t
h
e
 
c
o
n
t
e
n
t
s
 
o
f
 
t
h
e
i
r
 
d
e
p
e
n
d
e
n
t
 
c
h
i
l
d


 
 
 
 
 
 
 
 
m
e
d
i
a
 
t
o
 
k
e
e
p
 
t
h
e
 
m
e
d
i
u
m
 
c
h
a
i
n
 
v
a
l
i
d
 
(
i
n
 
o
t
h
e
r
 
w
o
r
d
s
,
 
a
l
l
 
c
h
a
n
g
e
s


 
 
 
 
 
 
 
 
r
e
p
r
e
s
e
n
t
e
d
 
b
y
 
m
e
d
i
a
 
b
e
i
n
g
 
d
e
l
e
t
e
d
 
w
i
l
l
 
b
e
 
p
r
o
p
a
g
a
t
e
d
 
t
o
 
t
h
e
i
r
 
c
h
i
l
d


 
 
 
 
 
 
 
 
m
e
d
i
u
m
)
.
 
A
f
t
e
r
 
t
h
a
t
,
 
t
h
i
s
 
s
n
a
p
s
h
o
t
'
s
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
u
m
 
w
i
l
l
 
b
e


 
 
 
 
 
 
 
 
d
e
l
e
t
e
d
.
 
T
h
e
 
p
a
r
e
n
t
 
o
f
 
t
h
i
s
 
s
n
a
p
s
h
o
t
 
w
i
l
l
 
b
e
c
o
m
e
 
a
 
n
e
w
 
p
a
r
e
n
t
 
f
o
r
 
a
l
l


 
 
 
 
 
 
 
 
i
t
s
 
c
h
i
l
d
 
s
n
a
p
s
h
o
t
s
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
d
e
l
e
t
e
d
 
s
n
a
p
s
h
o
t
 
i
s
 
t
h
e
 
c
u
r
r
e
n
t
 
o
n
e
,
 
i
t
s
 
p
a
r
e
n
t
 
s
n
a
p
s
h
o
t
 
w
i
l
l


 
 
 
 
 
 
 
 
b
e
c
o
m
e
 
a
 
n
e
w
 
c
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
.
 
T
h
e
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
i
s
 
n
o
t
 
d
i
r
e
c
t
l
y


 
 
 
 
 
 
 
 
a
f
f
e
c
t
e
d
 
i
n
 
t
h
i
s
 
c
a
s
e
,
 
e
x
c
e
p
t
 
t
h
a
t
 
c
u
r
r
e
n
t
l
y
 
a
t
t
a
c
h
e
d
 
d
i
f
f
e
r
e
n
c
i
n
g


 
 
 
 
 
 
 
 
m
e
d
i
a
 
b
a
s
e
d
 
o
n
 
m
e
d
i
a
 
o
f
 
t
h
e
 
d
e
l
e
t
e
d
 
s
n
a
p
s
h
o
t
 
w
i
l
l
 
b
e
 
a
l
s
o
 
m
e
r
g
e
d
 
a
s


 
 
 
 
 
 
 
 
d
e
s
c
r
i
b
e
d
 
a
b
o
v
e
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
d
e
l
e
t
e
d
 
s
n
a
p
s
h
o
t
 
i
s
 
t
h
e
 
f
i
r
s
t
 
o
r
 
c
u
r
r
e
n
t
 
s
n
a
p
s
h
o
t
,
 
t
h
e
n
 
t
h
e


 
 
 
 
 
 
 
 
r
e
s
p
e
c
t
i
v
e
 
I
M
a
c
h
i
n
e
 
a
t
t
r
i
b
u
t
e
s
 
w
i
l
l
 
b
e
 
a
d
j
u
s
t
e
d
.
 
D
e
l
e
t
i
n
g
 
t
h
e
 
c
u
r
r
e
n
t


 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
 
w
i
l
l
 
a
l
s
o
 
i
m
p
l
i
c
i
t
l
y
 
c
a
l
l
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
a
v
e
S
e
t
t
i
n
g
s
"
/
>


 
 
 
 
 
 
 
 
t
o
 
m
a
k
e
 
a
l
l
 
c
u
r
r
e
n
t
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
p
e
r
m
a
n
e
n
t
.




 
 
 
 
 
 
 
 
D
e
l
e
t
i
n
g
 
a
 
s
n
a
p
s
h
o
t
 
h
a
s
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
p
r
e
c
o
n
d
i
t
i
o
n
s
:




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
C
h
i
l
d
 
m
e
d
i
a
 
o
f
 
a
l
l
 
n
o
r
m
a
l
 
m
e
d
i
a
 
o
f
 
t
h
e
 
d
e
l
e
t
e
d
 
s
n
a
p
s
h
o
t


 
 
 
 
 
 
 
 
 
 
m
u
s
t
 
b
e
 
a
c
c
e
s
s
i
b
l
e
 
(
s
e
e
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
:
:
s
t
a
t
e
"
/
>
)
 
f
o
r
 
t
h
i
s


 
 
 
 
 
 
 
 
 
 
o
p
e
r
a
t
i
o
n
 
t
o
 
s
u
c
c
e
e
d
.
 
I
f
 
o
n
l
y
 
o
n
e
 
r
u
n
n
i
n
g
 
V
M
 
r
e
f
e
r
s
 
t
o
 
a
l
l
 
i
m
a
g
e
s


 
 
 
 
 
 
 
 
 
 
w
h
i
c
h
 
p
a
r
t
i
c
i
p
a
t
e
s
 
i
n
 
m
e
r
g
i
n
g
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
a
n
 
b
e
 
p
e
r
f
o
r
m
e
d
 
w
h
i
l
e


 
 
 
 
 
 
 
 
 
 
t
h
e
 
V
M
 
i
s
 
r
u
n
n
i
n
g
.
 
O
t
h
e
r
w
i
s
e
 
a
l
l
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s
 
w
h
o
s
e
 
m
e
d
i
a
 
a
r
e


 
 
 
 
 
 
 
 
 
 
d
i
r
e
c
t
l
y
 
o
r
 
i
n
d
i
r
e
c
t
l
y
 
b
a
s
e
d
 
o
n
 
t
h
e
 
m
e
d
i
a
 
o
f
 
d
e
l
e
t
e
d
 
s
n
a
p
s
h
o
t
 
m
u
s
t


 
 
 
 
 
 
 
 
 
 
b
e
 
p
o
w
e
r
e
d
 
o
f
f
.
 
I
n
 
a
n
y
 
c
a
s
e
,
 
o
n
l
i
n
e
 
s
n
a
p
s
h
o
t
 
d
e
l
e
t
i
n
g
 
u
s
u
a
l
l
y
 
i
s


 
 
 
 
 
 
 
 
 
 
s
l
o
w
e
r
 
t
h
a
n
 
t
h
e
 
s
a
m
e
 
o
p
e
r
a
t
i
o
n
 
w
i
t
h
o
u
t
 
a
n
y
 
r
u
n
n
i
n
g
 
V
M
.




 
 
 
 
 
 
 
 
 
 
Y
o
u
 
c
a
n
n
o
t
 
d
e
l
e
t
e
 
t
h
e
 
s
n
a
p
s
h
o
t
 
i
f
 
a
 
m
e
d
i
u
m
 
a
t
t
a
c
h
e
d
 
t
o
 
i
t
 
h
a
s


 
 
 
 
 
 
 
 
 
 
m
o
r
e
 
t
h
a
n
 
o
n
e
 
c
h
i
l
d
 
m
e
d
i
u
m
 
(
d
i
f
f
e
r
e
n
c
i
n
g
 
i
m
a
g
e
s
)
 
b
e
c
a
u
s
e
 
o
t
h
e
r
w
i
s
e


 
 
 
 
 
 
 
 
 
 
m
e
r
g
i
n
g
 
w
o
u
l
d
 
b
e
 
i
m
p
o
s
s
i
b
l
e
.
 
T
h
i
s
 
m
i
g
h
t
 
b
e
 
t
h
e
 
c
a
s
e
 
i
f
 
t
h
e
r
e
 
i
s


 
 
 
 
 
 
 
 
 
 
m
o
r
e
 
t
h
a
n
 
o
n
e
 
c
h
i
l
d
 
s
n
a
p
s
h
o
t
 
o
r
 
d
i
f
f
e
r
e
n
c
i
n
g
 
i
m
a
g
e
s
 
w
e
r
e
 
c
r
e
a
t
e
d


 
 
 
 
 
 
 
 
 
 
f
o
r
 
o
t
h
e
r
 
r
e
a
s
o
n
 
(
e
.
g
.
 
i
m
p
l
i
c
i
t
l
y
 
b
e
c
a
u
s
e
 
o
f
 
m
u
l
t
i
p
l
e
 
m
a
c
h
i
n
e


 
 
 
 
 
 
 
 
 
 
a
t
t
a
c
h
m
e
n
t
s
)
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
T
h
e
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
'
s
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
t
a
t
e
"
>
s
t
a
t
e
<
/
l
i
n
k
>
 
i
s


 
 
 
 
 
 
 
 
c
h
a
n
g
e
d
 
t
o
 
"
D
e
l
e
t
i
n
g
S
n
a
p
s
h
o
t
"
,
 
"
D
e
l
e
t
i
n
g
S
n
a
p
s
h
o
t
O
n
l
i
n
e
"
 
o
r


 
 
 
 
 
 
 
 
"
D
e
l
e
t
i
n
g
S
n
a
p
s
h
o
t
P
a
u
s
e
d
"
 
w
h
i
l
e
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
i
n
 
p
r
o
g
r
e
s
s
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
M
e
r
g
i
n
g
 
m
e
d
i
u
m
 
c
o
n
t
e
n
t
s
 
c
a
n
 
b
e
 
v
e
r
y
 
t
i
m
e
 
a
n
d
 
d
i
s
k
 
s
p
a
c
e


 
 
 
 
 
 
 
 
 
 
c
o
n
s
u
m
i
n
g
,
 
i
f
 
t
h
e
s
e
 
m
e
d
i
a
 
a
r
e
 
b
i
g
 
i
n
 
s
i
z
e
 
a
n
d
 
h
a
v
e
 
m
a
n
y


 
 
 
 
 
 
 
 
 
 
c
h
i
l
d
r
e
n
.
 
H
o
w
e
v
e
r
,
 
i
f
 
t
h
e
 
s
n
a
p
s
h
o
t
 
b
e
i
n
g
 
d
e
l
e
t
e
d
 
i
s
 
t
h
e
 
l
a
s
t


 
 
 
 
 
 
 
 
 
 
(
h
e
a
d
)
 
s
n
a
p
s
h
o
t
 
o
n
 
t
h
e
 
b
r
a
n
c
h
,
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
w
i
l
l
 
b
e
 
r
a
t
h
e
r


 
 
 
 
 
 
 
 
 
 
q
u
i
c
k
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
s
n
a
p
s
h
o
t
 
t
o
 
d
e
l
e
t
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
r
u
n
n
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
p
r
e
v
e
n
t
s
 
d
e
l
e
t
i
n
g
 
t
h
i
s
 
s
n
a
p
s
h
o
t
.
 
T
h
i
s


 
 
 
 
 
 
 
 
 
 
h
a
p
p
e
n
s
 
o
n
l
y
 
i
n
 
v
e
r
y
 
s
p
e
c
i
f
i
c
 
s
i
t
u
a
t
i
o
n
s
,
 
u
s
u
a
l
l
y
 
s
n
a
p
s
h
o
t
s
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
 
 
d
e
l
e
t
e
d
 
w
i
t
h
o
u
t
 
t
r
o
u
b
l
e
 
w
h
i
l
e
 
a
 
V
M
 
i
s
 
r
u
n
n
i
n
g
.
 
T
h
e
 
e
r
r
o
r
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
 
 
t
e
x
t
 
e
x
p
l
a
i
n
s
 
t
h
e
 
r
e
a
s
o
n
 
f
o
r
 
t
h
e
 
f
a
i
l
u
r
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
l
e
t
e
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
l
e
t
e
_
s
n
a
p
s
h
o
t
_
a
n
d
_
a
l
l
_
c
h
i
l
d
r
e
n
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
S
t
a
r
t
s
 
d
e
l
e
t
i
n
g
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
s
n
a
p
s
h
o
t
 
a
n
d
 
a
l
l
 
i
t
s
 
c
h
i
l
d
r
e
n


 
 
 
 
 
 
 
 
a
s
y
n
c
h
r
o
n
o
u
s
l
y
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
"
/
>
 
f
o
r
 
a
n
 
i
n
t
r
o
d
u
c
t
i
o
n
 
t
o


 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
s
.
 
T
h
e
 
c
o
n
d
i
t
i
o
n
s
 
a
n
d
 
m
a
n
y
 
d
e
t
a
i
l
s
 
a
r
e
 
t
h
e
 
s
a
m
e
 
a
s
 
w
i
t
h


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
S
n
a
p
s
h
o
t
"
/
>
.




 
 
 
 
 
 
 
 
T
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
v
e
r
y
 
f
a
s
t
 
i
f
 
t
h
e
 
s
n
a
p
s
h
o
t
 
s
u
b
t
r
e
e
 
d
o
e
s
 
n
o
t
 
i
n
c
l
u
d
e


 
 
 
 
 
 
 
 
t
h
e
 
c
u
r
r
e
n
t
 
s
t
a
t
e
.
 
I
t
 
i
s
 
s
t
i
l
l
 
s
i
g
n
i
f
i
c
a
n
t
l
y
 
f
a
s
t
e
r
 
t
h
a
n
 
d
e
l
e
t
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
s
 
o
n
e
 
b
y
 
o
n
e
 
i
f
 
t
h
e
 
c
u
r
r
e
n
t
 
s
t
a
t
e
 
i
s
 
i
n
 
t
h
e
 
s
u
b
t
r
e
e
 
a
n
d
 
t
h
e
r
e


 
 
 
 
 
 
 
 
a
r
e
 
m
o
r
e
 
t
h
a
n
 
o
n
e
 
s
n
a
p
s
h
o
t
s
 
f
r
o
m
 
c
u
r
r
e
n
t
 
s
t
a
t
e
 
t
o
 
t
h
e
 
s
n
a
p
s
h
o
t
 
w
h
i
c
h


 
 
 
 
 
 
 
 
m
a
r
k
s
 
t
h
e
 
s
u
b
t
r
e
e
,
 
s
i
n
c
e
 
i
t
 
e
l
i
m
i
n
a
t
e
s
 
t
h
e
 
i
n
c
r
e
m
e
n
t
a
l
 
i
m
a
g
e
 
m
e
r
g
i
n
g
.




 
 
 
 
 
 
 
 
T
h
i
s
 
A
P
I
 
m
e
t
h
o
d
 
i
s
 
r
i
g
h
t
 
n
o
w
 
n
o
t
 
i
m
p
l
e
m
e
n
t
e
d
!




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
s
n
a
p
s
h
o
t
 
t
o
 
d
e
l
e
t
e
,
 
i
n
c
l
u
d
i
n
g
 
a
l
l
 
i
t
s
 
c
h
i
l
d
r
e
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
r
u
n
n
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
p
r
e
v
e
n
t
s
 
d
e
l
e
t
i
n
g
 
t
h
i
s
 
s
n
a
p
s
h
o
t
.
 
T
h
i
s


 
 
 
 
 
 
 
 
 
 
h
a
p
p
e
n
s
 
o
n
l
y
 
i
n
 
v
e
r
y
 
s
p
e
c
i
f
i
c
 
s
i
t
u
a
t
i
o
n
s
,
 
u
s
u
a
l
l
y
 
s
n
a
p
s
h
o
t
s
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
 
 
d
e
l
e
t
e
d
 
w
i
t
h
o
u
t
 
t
r
o
u
b
l
e
 
w
h
i
l
e
 
a
 
V
M
 
i
s
 
r
u
n
n
i
n
g
.
 
T
h
e
 
e
r
r
o
r
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
 
 
t
e
x
t
 
e
x
p
l
a
i
n
s
 
t
h
e
 
r
e
a
s
o
n
 
f
o
r
 
t
h
e
 
f
a
i
l
u
r
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
N
O
T
I
M
P
L


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
e
t
h
o
d
 
i
s
 
n
o
t
 
i
m
p
l
e
m
e
n
t
e
d
 
y
e
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
l
e
t
e
S
n
a
p
s
h
o
t
A
n
d
A
l
l
C
h
i
l
d
r
e
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
e
l
e
t
e
_
s
n
a
p
s
h
o
t
_
r
a
n
g
e
(
s
e
l
f
,
 
s
t
a
r
t
_
i
d
,
 
e
n
d
_
i
d
)
:


 
 
 
 
 
 
 
 
"
"
"
S
t
a
r
t
s
 
d
e
l
e
t
i
n
g
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
s
n
a
p
s
h
o
t
 
r
a
n
g
e
.
 
T
h
i
s
 
i
s
 
l
i
m
i
t
e
d
 
t
o


 
 
 
 
 
 
 
 
l
i
n
e
a
r
 
s
n
a
p
s
h
o
t
 
l
i
s
t
s
,
 
w
h
i
c
h
 
m
e
a
n
s
 
t
h
e
r
e
 
m
a
y
 
n
o
t
 
b
e
 
a
n
y
 
o
t
h
e
r
 
c
h
i
l
d


 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
s
 
o
t
h
e
r
 
t
h
a
n
 
t
h
e
 
d
i
r
e
c
t
 
s
e
q
u
e
n
c
e
 
b
e
t
w
e
e
n
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d


 
 
 
 
 
 
 
 
s
n
a
p
s
h
o
t
.
 
I
f
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
s
n
a
p
s
h
o
t
 
p
o
i
n
t
 
t
o
 
t
h
e
 
s
a
m
e
 
s
n
a
p
s
h
o
t
 
t
h
i
s


 
 
 
 
 
 
 
 
m
e
t
h
o
d
 
i
s
 
c
o
m
p
l
e
t
e
l
y
 
e
q
u
i
v
a
l
e
n
t
 
t
o
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
S
n
a
p
s
h
o
t
"
/
>
.
 
S
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
"
/
>
 
f
o
r
 
a
n
 
i
n
t
r
o
d
u
c
t
i
o
n
 
t
o
 
s
n
a
p
s
h
o
t
s
.
 
T
h
e


 
 
 
 
 
 
 
 
c
o
n
d
i
t
i
o
n
s
 
a
n
d
 
m
a
n
y
 
d
e
t
a
i
l
s
 
a
r
e
 
t
h
e
 
s
a
m
e
 
a
s
 
w
i
t
h


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
d
e
l
e
t
e
S
n
a
p
s
h
o
t
"
/
>
.




 
 
 
 
 
 
 
 
T
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
g
e
n
e
r
a
l
l
y
 
f
a
s
t
e
r
 
t
h
a
n
 
d
e
l
e
t
i
n
g
 
s
n
a
p
s
h
o
t
s
 
o
n
e
 
b
y
 
o
n
e


 
 
 
 
 
 
 
 
a
n
d
 
o
f
t
e
n
 
a
l
s
o
 
n
e
e
d
s
 
l
e
s
s
 
e
x
t
r
a
 
d
i
s
k
 
s
p
a
c
e
 
b
e
f
o
r
e
 
f
r
e
e
i
n
g
 
u
p
 
d
i
s
k
 
s
p
a
c
e


 
 
 
 
 
 
 
 
b
y
 
d
e
l
e
t
i
n
g
 
t
h
e
 
r
e
m
o
v
e
d
 
d
i
s
k
 
i
m
a
g
e
s
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
o
 
t
h
e
 
s
n
a
p
s
h
o
t
.




 
 
 
 
 
 
 
 
T
h
i
s
 
A
P
I
 
m
e
t
h
o
d
 
i
s
 
r
i
g
h
t
 
n
o
w
 
n
o
t
 
i
m
p
l
e
m
e
n
t
e
d
!




 
 
 
 
 
 
 
 
i
n
 
s
t
a
r
t
_
i
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
f
i
r
s
t
 
s
n
a
p
s
h
o
t
 
t
o
 
d
e
l
e
t
e
.




 
 
 
 
 
 
 
 
i
n
 
e
n
d
_
i
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
l
a
s
t
 
s
n
a
p
s
h
o
t
 
t
o
 
d
e
l
e
t
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
r
u
n
n
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
p
r
e
v
e
n
t
s
 
d
e
l
e
t
i
n
g
 
t
h
i
s
 
s
n
a
p
s
h
o
t
.
 
T
h
i
s


 
 
 
 
 
 
 
 
 
 
h
a
p
p
e
n
s
 
o
n
l
y
 
i
n
 
v
e
r
y
 
s
p
e
c
i
f
i
c
 
s
i
t
u
a
t
i
o
n
s
,
 
u
s
u
a
l
l
y
 
s
n
a
p
s
h
o
t
s
 
c
a
n
 
b
e


 
 
 
 
 
 
 
 
 
 
d
e
l
e
t
e
d
 
w
i
t
h
o
u
t
 
t
r
o
u
b
l
e
 
w
h
i
l
e
 
a
 
V
M
 
i
s
 
r
u
n
n
i
n
g
.
 
T
h
e
 
e
r
r
o
r
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
 
 
t
e
x
t
 
e
x
p
l
a
i
n
s
 
t
h
e
 
r
e
a
s
o
n
 
f
o
r
 
t
h
e
 
f
a
i
l
u
r
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
N
O
T
I
M
P
L


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
e
t
h
o
d
 
i
s
 
n
o
t
 
i
m
p
l
e
m
e
n
t
e
d
 
y
e
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
d
e
l
e
t
e
S
n
a
p
s
h
o
t
R
a
n
g
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
t
a
r
t
_
i
d
,
 
e
n
d
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
s
t
o
r
e
_
s
n
a
p
s
h
o
t
(
s
e
l
f
,
 
s
n
a
p
s
h
o
t
)
:


 
 
 
 
 
 
 
 
"
"
"
S
t
a
r
t
s
 
r
e
s
e
t
t
i
n
g
 
t
h
e
 
m
a
c
h
i
n
e
'
s
 
c
u
r
r
e
n
t
 
s
t
a
t
e
 
t
o
 
t
h
e
 
s
t
a
t
e
 
c
o
n
t
a
i
n
e
d


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
g
i
v
e
n
 
s
n
a
p
s
h
o
t
,
 
a
s
y
n
c
h
r
o
n
o
u
s
l
y
.
 
A
l
l
 
c
u
r
r
e
n
t
 
s
e
t
t
i
n
g
s
 
o
f
 
t
h
e


 
 
 
 
 
 
 
 
m
a
c
h
i
n
e
 
w
i
l
l
 
b
e
 
r
e
s
e
t
 
a
n
d
 
c
h
a
n
g
e
s
 
s
t
o
r
e
d
 
i
n
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a


 
 
 
 
 
 
 
 
w
i
l
l
 
b
e
 
l
o
s
t
.


 
 
 
 
 
 
 
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
S
n
a
p
s
h
o
t
"
/
>
 
f
o
r
 
a
n
 
i
n
t
r
o
d
u
c
t
i
o
n
 
t
o
 
s
n
a
p
s
h
o
t
s
.




 
 
 
 
 
 
 
 
A
f
t
e
r
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
i
s
 
s
u
c
c
e
s
s
f
u
l
l
y
 
c
o
m
p
l
e
t
e
d
,
 
n
e
w
 
e
m
p
t
y
 
d
i
f
f
e
r
e
n
c
i
n
g


 
 
 
 
 
 
 
 
m
e
d
i
a
 
a
r
e
 
c
r
e
a
t
e
d
 
f
o
r
 
a
l
l
 
n
o
r
m
a
l
 
m
e
d
i
a
 
o
f
 
t
h
e
 
m
a
c
h
i
n
e
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
g
i
v
e
n
 
s
n
a
p
s
h
o
t
 
i
s
 
a
n
 
o
n
l
i
n
e
 
s
n
a
p
s
h
o
t
,
 
t
h
e
 
m
a
c
h
i
n
e
 
w
i
l
l
 
g
o
 
t
o


 
 
 
 
 
 
 
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
M
a
c
h
i
n
e
S
t
a
t
e
_
S
a
v
e
d
"
>
 
s
a
v
e
d
 
s
t
a
t
e
<
/
l
i
n
k
>
,
 
s
o
 
t
h
a
t
 
t
h
e


 
 
 
 
 
 
 
 
n
e
x
t
 
t
i
m
e
 
i
t
 
i
s
 
p
o
w
e
r
e
d
 
o
n
,
 
t
h
e
 
e
x
e
c
u
t
i
o
n
 
s
t
a
t
e
 
w
i
l
l
 
b
e
 
r
e
s
t
o
r
e
d


 
 
 
 
 
 
 
 
f
r
o
m
 
t
h
e
 
s
t
a
t
e
 
o
f
 
t
h
e
 
s
n
a
p
s
h
o
t
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
c
h
i
n
e
 
m
u
s
t
 
n
o
t
 
b
e
 
r
u
n
n
i
n
g
,
 
o
t
h
e
r
w
i
s
e
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
w
i
l
l
 
f
a
i
l
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
m
a
c
h
i
n
e
 
s
t
a
t
e
 
i
s
 
<
l
i
n
k
 
t
o
=
"
M
a
c
h
i
n
e
S
t
a
t
e
_
S
a
v
e
d
"
>
S
a
v
e
d
<
/
l
i
n
k
>


 
 
 
 
 
 
 
 
 
 
p
r
i
o
r
 
t
o
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
,
 
t
h
e
 
s
a
v
e
d
 
s
t
a
t
e
 
f
i
l
e
 
w
i
l
l
 
b
e
 
i
m
p
l
i
c
i
t
l
y


 
 
 
 
 
 
 
 
 
 
d
e
l
e
t
e
d
 
(
a
s
 
i
f
 
<
l
i
n
k
 
t
o
=
"
I
C
o
n
s
o
l
e
:
:
d
i
s
c
a
r
d
S
a
v
e
d
S
t
a
t
e
"
/
>
 
w
e
r
e


 
 
 
 
 
 
 
 
 
 
c
a
l
l
e
d
)
.




 
 
 
 
 
 
 
 
i
n
 
s
n
a
p
s
h
o
t
 
o
f
 
t
y
p
e
 
I
S
n
a
p
s
h
o
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
n
a
p
s
h
o
t
 
t
o
 
r
e
s
t
o
r
e
 
t
h
e
 
V
M
 
s
t
a
t
e
 
f
r
o
m
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
i
s
 
r
u
n
n
i
n
g
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
s
t
o
r
e
S
n
a
p
s
h
o
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
s
n
a
p
s
h
o
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
t
e
l
e
p
o
r
t
(
s
e
l
f
,
 
h
o
s
t
n
a
m
e
,
 
t
c
p
p
o
r
t
,
 
p
a
s
s
w
o
r
d
,
 
m
a
x
_
d
o
w
n
t
i
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
T
e
l
e
p
o
r
t
 
t
h
e
 
V
M
 
t
o
 
a
 
d
i
f
f
e
r
e
n
t
 
h
o
s
t
 
m
a
c
h
i
n
e
 
o
r
 
p
r
o
c
e
s
s
.




 
 
 
 
 
 
 
 
T
O
D
O
 
e
x
p
l
a
i
n
 
t
h
e
 
d
e
t
a
i
l
s
.




 
 
 
 
 
 
 
 
i
n
 
h
o
s
t
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
r
 
I
P
 
o
f
 
t
h
e
 
h
o
s
t
 
t
o
 
t
e
l
e
p
o
r
t
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
t
c
p
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
T
C
P
 
p
o
r
t
 
t
o
 
c
o
n
n
e
c
t
 
t
o
 
(
1
.
.
6
5
5
3
5
)
.




 
 
 
 
 
 
 
 
i
n
 
p
a
s
s
w
o
r
d
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
p
a
s
s
w
o
r
d
.




 
 
 
 
 
 
 
 
i
n
 
m
a
x
_
d
o
w
n
t
i
m
e
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
x
i
m
u
m
 
a
l
l
o
w
e
d
 
d
o
w
n
t
i
m
e
 
g
i
v
e
n
 
a
s
 
m
i
l
l
i
s
e
c
o
n
d
s
.
 
0
 
i
s
 
n
o
t
 
a
 
v
a
l
i
d


 
 
 
 
 
 
 
 
 
 
v
a
l
u
e
.
 
R
e
c
o
m
m
e
n
d
e
d
 
v
a
l
u
e
:
 
2
5
0
 
m
s
.




 
 
 
 
 
 
 
 
 
 
T
h
e
 
h
i
g
h
e
r
 
t
h
e
 
v
a
l
u
e
 
i
s
,
 
t
h
e
 
g
r
e
a
t
e
r
 
t
h
e
 
c
h
a
n
c
e
 
f
o
r
 
a
 
s
u
c
c
e
s
s
f
u
l


 
 
 
 
 
 
 
 
 
 
t
e
l
e
p
o
r
t
a
t
i
o
n
.
 
A
 
s
m
a
l
l
 
v
a
l
u
e
 
m
a
y
 
e
a
s
i
l
y
 
r
e
s
u
l
t
 
i
n
 
t
h
e
 
t
e
l
e
p
o
r
t
a
t
i
o
n


 
 
 
 
 
 
 
 
 
 
p
r
o
c
e
s
s
 
t
a
k
i
n
g
 
h
o
u
r
s
 
a
n
d
 
e
v
e
n
t
u
a
l
l
y
 
f
a
i
l
.




 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
u
r
r
e
n
t
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
 
t
r
e
a
t
s
 
t
h
i
s
 
a
 
g
u
i
d
e
l
i
n
e
,
 
n
o
t
 
a
s
 
a
n


 
 
 
 
 
 
 
 
 
 
 
 
a
b
s
o
l
u
t
e
 
r
u
l
e
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
V
M
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
 
m
a
c
h
i
n
e
 
n
o
t
 
r
u
n
n
i
n
g
 
o
r
 
p
a
u
s
e
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
t
e
l
e
p
o
r
t
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
h
o
s
t
n
a
m
e
,
 
t
c
p
p
o
r
t
,
 
p
a
s
s
w
o
r
d
,
 
m
a
x
_
d
o
w
n
t
i
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
R
e
p
r
e
s
e
n
t
s
 
o
n
e
 
o
f
 
h
o
s
t
'
s
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
s
.
 
I
P
 
V
6
 
a
d
d
r
e
s
s
 
a
n
d
 
n
e
t
w
o
r
k


 
 
 
 
 
 
m
a
s
k
 
a
r
e
 
s
t
r
i
n
g
s
 
o
f
 
3
2
 
h
e
x
d
e
c
i
m
a
l
 
d
i
g
i
t
s
 
g
r
o
u
p
e
d
 
b
y
 
f
o
u
r
.
 
G
r
o
u
p
s
 
a
r
e


 
 
 
 
 
 
s
e
p
a
r
a
t
e
d
 
b
y
 
c
o
l
o
n
s
.


 
 
 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
,
 
f
e
8
0
:
0
0
0
0
:
0
0
0
0
:
0
0
0
0
:
0
2
1
e
:
c
2
f
f
:
f
e
d
2
:
b
0
3
0
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
8
7
a
4
1
5
3
d
-
6
8
8
9
-
4
d
d
6
-
9
6
5
4
-
2
e
9
f
f
0
a
e
8
d
e
c
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
a
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
a
m
e
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
n
a
m
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
a
m
e
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
d
_
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
i
d
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
i
n
t
e
r
f
a
c
e
 
U
U
I
D
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
d
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
_
n
a
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
e
t
w
o
r
k
N
a
m
e
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
n
a
m
e
 
o
f
 
a
 
v
i
r
t
u
a
l
 
n
e
t
w
o
r
k
 
t
h
e
 
i
n
t
e
r
f
a
c
e
 
g
e
t
s
 
a
t
t
a
c
h
e
d
 
t
o
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
t
w
o
r
k
N
a
m
e
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
h
c
p
_
e
n
a
b
l
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
D
H
C
P
E
n
a
b
l
e
d
'


 
 
 
 
 
 
 
 
S
p
e
c
i
f
i
e
s
 
w
h
e
t
h
e
r
 
t
h
e
 
D
H
C
P
 
i
s
 
e
n
a
b
l
e
d
 
f
o
r
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
D
H
C
P
E
n
a
b
l
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
p
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
I
P
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
I
P
 
V
4
 
a
d
d
r
e
s
s
 
o
f
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
P
A
d
d
r
e
s
s
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
_
m
a
s
k
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
n
e
t
w
o
r
k
M
a
s
k
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
n
e
t
w
o
r
k
 
m
a
s
k
 
o
f
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
t
w
o
r
k
M
a
s
k
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
p
v
6
_
s
u
p
p
o
r
t
e
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
I
P
V
6
S
u
p
p
o
r
t
e
d
'


 
 
 
 
 
 
 
 
S
p
e
c
i
f
i
e
s
 
w
h
e
t
h
e
r
 
t
h
e
 
I
P
 
V
6
 
i
s
 
s
u
p
p
o
r
t
e
d
/
e
n
a
b
l
e
d
 
f
o
r
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
P
V
6
S
u
p
p
o
r
t
e
d
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
p
v
6
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
I
P
V
6
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
I
P
 
V
6
 
a
d
d
r
e
s
s
 
o
f
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
P
V
6
A
d
d
r
e
s
s
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
p
v
6
_
n
e
t
w
o
r
k
_
m
a
s
k
_
p
r
e
f
i
x
_
l
e
n
g
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
I
P
V
6
N
e
t
w
o
r
k
M
a
s
k
P
r
e
f
i
x
L
e
n
g
t
h
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
l
e
n
g
t
h
 
I
P
 
V
6
 
n
e
t
w
o
r
k
 
m
a
s
k
 
p
r
e
f
i
x
 
o
f
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
I
P
V
6
N
e
t
w
o
r
k
M
a
s
k
P
r
e
f
i
x
L
e
n
g
t
h
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
h
a
r
d
w
a
r
e
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
h
a
r
d
w
a
r
e
A
d
d
r
e
s
s
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
h
a
r
d
w
a
r
e
 
a
d
d
r
e
s
s
.
 
F
o
r
 
E
t
h
e
r
n
e
t
 
i
t
 
i
s
 
M
A
C
 
a
d
d
r
e
s
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
h
a
r
d
w
a
r
e
A
d
d
r
e
s
s
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
e
d
i
u
m
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
M
e
d
i
u
m
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
m
e
d
i
u
m
T
y
p
e
'


 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
p
r
o
t
o
c
o
l
 
e
n
c
a
p
s
u
l
a
t
i
o
n
 
u
s
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
e
d
i
u
m
T
y
p
e
'
,
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
M
e
d
i
u
m
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
t
a
t
u
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
S
t
a
t
u
s
 
v
a
l
u
e
 
f
o
r
 
'
s
t
a
t
u
s
'


 
 
 
 
 
 
 
 
S
t
a
t
u
s
 
o
f
 
t
h
e
 
i
n
t
e
r
f
a
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
t
a
t
u
s
'
,
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
S
t
a
t
u
s
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
n
t
e
r
f
a
c
e
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
i
n
t
e
r
f
a
c
e
T
y
p
e
'


 
 
 
 
 
 
 
 
s
p
e
c
i
f
i
e
s
 
t
h
e
 
h
o
s
t
 
i
n
t
e
r
f
a
c
e
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
n
t
e
r
f
a
c
e
T
y
p
e
'
,
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
T
y
p
e
)




 
 
 
 
d
e
f
 
e
n
a
b
l
e
_
s
t
a
t
i
c
_
i
p
_
c
o
n
f
i
g
(
s
e
l
f
,
 
i
p
_
a
d
d
r
e
s
s
,
 
n
e
t
w
o
r
k
_
m
a
s
k
)
:


 
 
 
 
 
 
 
 
"
"
"
s
e
t
s
 
a
n
d
 
e
n
a
b
l
e
s
 
t
h
e
 
s
t
a
t
i
c
 
I
P
 
V
4
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
i
n
t
e
r
f
a
c
e
.




 
 
 
 
 
 
 
 
i
n
 
i
p
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
I
P
 
a
d
d
r
e
s
s
.




 
 
 
 
 
 
 
 
i
n
 
n
e
t
w
o
r
k
_
m
a
s
k
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
 
m
a
s
k
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
a
b
l
e
S
t
a
t
i
c
I
P
C
o
n
f
i
g
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
p
_
a
d
d
r
e
s
s
,
 
n
e
t
w
o
r
k
_
m
a
s
k
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
a
b
l
e
_
s
t
a
t
i
c
_
i
p
_
c
o
n
f
i
g
_
v
6
(
s
e
l
f
,
 
i
p
v
6
_
a
d
d
r
e
s
s
,
 
i
p
v
6
_
n
e
t
w
o
r
k
_
m
a
s
k
_
p
r
e
f
i
x
_
l
e
n
g
t
h
)
:


 
 
 
 
 
 
 
 
"
"
"
s
e
t
s
 
a
n
d
 
e
n
a
b
l
e
s
 
t
h
e
 
s
t
a
t
i
c
 
I
P
 
V
6
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
i
n
t
e
r
f
a
c
e
.




 
 
 
 
 
 
 
 
i
n
 
i
p
v
6
_
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
I
P
 
a
d
d
r
e
s
s
.




 
 
 
 
 
 
 
 
i
n
 
i
p
v
6
_
n
e
t
w
o
r
k
_
m
a
s
k
_
p
r
e
f
i
x
_
l
e
n
g
t
h
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
 
m
a
s
k
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
a
b
l
e
S
t
a
t
i
c
I
P
C
o
n
f
i
g
V
6
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
p
v
6
_
a
d
d
r
e
s
s
,
 
i
p
v
6
_
n
e
t
w
o
r
k
_
m
a
s
k
_
p
r
e
f
i
x
_
l
e
n
g
t
h
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
e
n
a
b
l
e
_
d
y
n
a
m
i
c
_
i
p
_
c
o
n
f
i
g
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
e
n
a
b
l
e
s
 
t
h
e
 
d
y
n
a
m
i
c
 
I
P
 
c
o
n
f
i
g
u
r
a
t
i
o
n
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
e
n
a
b
l
e
D
y
n
a
m
i
c
I
P
C
o
n
f
i
g
'
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
d
h
c
p
_
r
e
d
i
s
c
o
v
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
r
e
f
r
e
s
h
e
s
 
t
h
e
 
I
P
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
f
o
r
 
D
H
C
P
-
e
n
a
b
l
e
d
 
i
n
t
e
r
f
a
c
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
D
H
C
P
R
e
d
i
s
c
o
v
e
r
'
)


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
H
o
s
t
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
H
o
s
t
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
t
h
e
 
p
h
y
s
i
c
a
l
 
m
a
c
h
i
n
e
 
t
h
a
t
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
i
n
s
t
a
l
l
a
t
i
o
n
 
r
u
n
s
 
o
n
.




 
 
 
 
 
 
A
n
 
o
b
j
e
c
t
 
i
m
p
l
e
m
e
n
t
i
n
g
 
t
h
i
s
 
i
n
t
e
r
f
a
c
e
 
i
s
 
r
e
t
u
r
n
e
d
 
b
y
 
t
h
e


 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
h
o
s
t
"
/
>
 
a
t
t
r
i
b
u
t
e
.
 
T
h
i
s
 
i
n
t
e
r
f
a
c
e
 
c
o
n
t
a
i
n
s


 
 
 
 
 
 
r
e
a
d
-
o
n
l
y
 
i
n
f
o
r
m
a
t
i
o
n
 
a
b
o
u
t
 
t
h
e
 
h
o
s
t
'
s
 
p
h
y
s
i
c
a
l
 
h
a
r
d
w
a
r
e
 
(
s
u
c
h
 
a
s
 
w
h
a
t


 
 
 
 
 
 
p
r
o
c
e
s
s
o
r
s
 
a
n
d
 
d
i
s
k
s
 
a
r
e
 
a
v
a
i
l
a
b
l
e
,
 
w
h
a
t
 
t
h
e
 
h
o
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
 
i
s
,


 
 
 
 
 
 
a
n
d
 
s
o
 
o
n
)
 
a
n
d
 
a
l
s
o
 
a
l
l
o
w
s
 
f
o
r
 
m
a
n
i
p
u
l
a
t
i
n
g
 
s
o
m
e
 
o
f
 
t
h
e
 
h
o
s
t
'
s
 
h
a
r
d
w
a
r
e
,


 
 
 
 
 
 
s
u
c
h
 
a
s
 
g
l
o
b
a
l
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
s
 
a
n
d
 
h
o
s
t
 
i
n
t
e
r
f
a
c
e
 
n
e
t
w
o
r
k
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
3
0
6
7
8
9
4
3
-
3
2
d
f
-
4
8
3
0
-
b
4
1
3
-
9
3
1
b
2
5
a
c
8
6
a
0
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
v
d
_
d
r
i
v
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
e
d
i
u
m
 
v
a
l
u
e
 
f
o
r
 
'
D
V
D
D
r
i
v
e
s
'


 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
D
V
D
 
d
r
i
v
e
s
 
a
v
a
i
l
a
b
l
e
 
o
n
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
D
V
D
D
r
i
v
e
s
'
,
 
I
M
e
d
i
u
m
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
l
o
p
p
y
_
d
r
i
v
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
e
d
i
u
m
 
v
a
l
u
e
 
f
o
r
 
'
f
l
o
p
p
y
D
r
i
v
e
s
'


 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
f
l
o
p
p
y
 
d
r
i
v
e
s
 
a
v
a
i
l
a
b
l
e
 
o
n
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
l
o
p
p
y
D
r
i
v
e
s
'
,
 
I
M
e
d
i
u
m
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
s
b
_
d
e
v
i
c
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
 
v
a
l
u
e
 
f
o
r
 
'
U
S
B
D
e
v
i
c
e
s
'


 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
U
S
B
 
d
e
v
i
c
e
s
 
c
u
r
r
e
n
t
l
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
O
n
c
e
 
a
 
n
e
w
 
d
e
v
i
c
e
 
i
s
 
p
h
y
s
i
c
a
l
l
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
,


 
 
 
 
 
 
 
 
i
t
 
a
p
p
e
a
r
s
 
i
n
 
t
h
i
s
 
l
i
s
t
 
a
n
d
 
r
e
m
a
i
n
s
 
t
h
e
r
e
 
u
n
t
i
l
 
d
e
t
a
c
h
e
d
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
U
S
B
 
f
u
n
c
t
i
o
n
a
l
i
t
y
 
i
s
 
n
o
t
 
a
v
a
i
l
a
b
l
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
e
d
i
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
s
e
t
 
t
h
e
 
r
e
s
u
l
t
 
c
o
d
e
 
t
o
 
@
c
 
E
_
N
O
T
I
M
P
L
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
U
S
B
D
e
v
i
c
e
s
'
,
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
s
b
_
d
e
v
i
c
e
_
f
i
l
t
e
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
 
v
a
l
u
e
 
f
o
r
 
'
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
s
'


 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
s
 
i
n
 
a
c
t
i
o
n
.


 
 
 
 
 
 
 
 
W
h
e
n
 
a
 
n
e
w
 
d
e
v
i
c
e
 
i
s
 
p
h
y
s
i
c
a
l
l
y
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
h
o
s
t
 
c
o
m
p
u
t
e
r
,


 
 
 
 
 
 
 
 
f
i
l
t
e
r
s
 
f
r
o
m
 
t
h
i
s
 
l
i
s
t
 
a
r
e
 
a
p
p
l
i
e
d
 
t
o
 
i
t
 
(
i
n
 
o
r
d
e
r
 
t
h
e
y
 
a
r
e
 
s
t
o
r
e
d


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
l
i
s
t
)
.
 
T
h
e
 
f
i
r
s
t
 
m
a
t
c
h
e
d
 
f
i
l
t
e
r
 
w
i
l
l
 
d
e
t
e
r
m
i
n
e
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
:
:
a
c
t
i
o
n
"
>
a
c
t
i
o
n
<
/
l
i
n
k
>


 
 
 
 
 
 
 
 
p
e
r
f
o
r
m
e
d
 
o
n
 
t
h
e
 
d
e
v
i
c
e
.




 
 
 
 
 
 
 
 
U
n
l
e
s
s
 
t
h
e
 
d
e
v
i
c
e
 
i
s
 
i
g
n
o
r
e
d
 
b
y
 
t
h
e
s
e
 
f
i
l
t
e
r
s
,
 
f
i
l
t
e
r
s
 
o
f
 
a
l
l


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
l
y
 
r
u
n
n
i
n
g
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
s


 
 
 
 
 
 
 
 
(
<
l
i
n
k
 
t
o
=
"
I
U
S
B
C
o
n
t
r
o
l
l
e
r
:
:
d
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>
)
 
a
r
e
 
a
p
p
l
i
e
d
 
t
o
 
i
t
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
U
S
B
 
f
u
n
c
t
i
o
n
a
l
i
t
y
 
i
s
 
n
o
t
 
a
v
a
i
l
a
b
l
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
e
d
i
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
s
e
t
 
t
h
e
 
r
e
s
u
l
t
 
c
o
d
e
 
t
o
 
@
c
 
E
_
N
O
T
I
M
P
L
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
"
/
>
,


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
U
S
B
D
e
v
i
c
e
S
t
a
t
e
"
/
>


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
s
'
,
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
 
v
a
l
u
e
 
f
o
r
 
'
n
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
s
'


 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
s
 
c
u
r
r
e
n
t
l
y
 
d
e
f
i
n
e
d
 
o
n
 
t
h
e
 
h
o
s
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
n
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
s
'
,
 
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
r
o
c
e
s
s
o
r
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
p
r
o
c
e
s
s
o
r
C
o
u
n
t
'


 
 
 
 
 
 
 
 
N
u
m
b
e
r
 
o
f
 
(
l
o
g
i
c
a
l
)
 
C
P
U
s
 
i
n
s
t
a
l
l
e
d
 
i
n
 
t
h
e
 
h
o
s
t
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
r
o
c
e
s
s
o
r
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
r
o
c
e
s
s
o
r
_
o
n
l
i
n
e
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
p
r
o
c
e
s
s
o
r
O
n
l
i
n
e
C
o
u
n
t
'


 
 
 
 
 
 
 
 
N
u
m
b
e
r
 
o
f
 
(
l
o
g
i
c
a
l
)
 
C
P
U
s
 
o
n
l
i
n
e
 
i
n
 
t
h
e
 
h
o
s
t
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
r
o
c
e
s
s
o
r
O
n
l
i
n
e
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
r
o
c
e
s
s
o
r
_
c
o
r
e
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
p
r
o
c
e
s
s
o
r
C
o
r
e
C
o
u
n
t
'


 
 
 
 
 
 
 
 
N
u
m
b
e
r
 
o
f
 
p
h
y
s
i
c
a
l
 
p
r
o
c
e
s
s
o
r
 
c
o
r
e
s
 
i
n
s
t
a
l
l
e
d
 
i
n
 
t
h
e
 
h
o
s
t
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
r
o
c
e
s
s
o
r
C
o
r
e
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
d
e
f
 
g
e
t
_
p
r
o
c
e
s
s
o
r
_
s
p
e
e
d
(
s
e
l
f
,
 
c
p
u
_
i
d
)
:


 
 
 
 
 
 
 
 
"
"
"
Q
u
e
r
y
 
t
h
e
 
(
a
p
p
r
o
x
i
m
a
t
e
)
 
m
a
x
i
m
u
m
 
s
p
e
e
d
 
o
f
 
a
 
s
p
e
c
i
f
i
e
d
 
h
o
s
t
 
C
P
U
 
i
n


 
 
 
 
 
 
 
 
M
e
g
a
h
e
r
t
z
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
C
P
U
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
p
e
e
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
S
p
e
e
d
 
v
a
l
u
e
.
 
0
 
i
s
 
r
e
t
u
r
n
e
d
 
i
f
 
v
a
l
u
e
 
i
s
 
n
o
t
 
k
n
o
w
n
 
o
r
 
@
a
 
c
p
u
I
d
 
i
s


 
 
 
 
 
 
 
 
 
 
i
n
v
a
l
i
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
p
e
e
d
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
P
r
o
c
e
s
s
o
r
S
p
e
e
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
p
u
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
p
e
e
d


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
p
r
o
c
e
s
s
o
r
_
f
e
a
t
u
r
e
(
s
e
l
f
,
 
f
e
a
t
u
r
e
)
:


 
 
 
 
 
 
 
 
"
"
"
Q
u
e
r
y
 
w
h
e
t
h
e
r
 
a
 
C
P
U
 
f
e
a
t
u
r
e
 
i
s
 
s
u
p
p
o
r
t
e
d
 
o
r
 
n
o
t
.




 
 
 
 
 
 
 
 
i
n
 
f
e
a
t
u
r
e
 
o
f
 
t
y
p
e
 
P
r
o
c
e
s
s
o
r
F
e
a
t
u
r
e


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
 
F
e
a
t
u
r
e
 
i
d
e
n
t
i
f
i
e
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
u
p
p
o
r
t
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
F
e
a
t
u
r
e
 
i
s
 
s
u
p
p
o
r
t
e
d
 
o
r
 
n
o
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
u
p
p
o
r
t
e
d
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
P
r
o
c
e
s
s
o
r
F
e
a
t
u
r
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
f
e
a
t
u
r
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
u
p
p
o
r
t
e
d


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
p
r
o
c
e
s
s
o
r
_
d
e
s
c
r
i
p
t
i
o
n
(
s
e
l
f
,
 
c
p
u
_
i
d
)
:


 
 
 
 
 
 
 
 
"
"
"
Q
u
e
r
y
 
t
h
e
 
m
o
d
e
l
 
s
t
r
i
n
g
 
o
f
 
a
 
s
p
e
c
i
f
i
e
d
 
h
o
s
t
 
C
P
U
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
C
P
U
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
u
r
r
e
n
t
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
 
m
i
g
h
t
 
n
o
t
 
n
e
c
e
s
s
a
r
i
l
y
 
r
e
t
u
r
n
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
d
e
s
c
r
i
p
t
i
o
n
 
f
o
r
 
t
h
i
s
 
e
x
a
c
t
 
C
P
U
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
M
o
d
e
l
 
s
t
r
i
n
g
.
 
A
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
i
s
 
r
e
t
u
r
n
e
d
 
i
f
 
v
a
l
u
e
 
i
s
 
n
o
t
 
k
n
o
w
n
 
o
r


 
 
 
 
 
 
 
 
 
 
@
a
 
c
p
u
I
d
 
i
s
 
i
n
v
a
l
i
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
s
c
r
i
p
t
i
o
n
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
P
r
o
c
e
s
s
o
r
D
e
s
c
r
i
p
t
i
o
n
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
p
u
_
i
d
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
s
c
r
i
p
t
i
o
n


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
p
r
o
c
e
s
s
o
r
_
c
p
u
i
d
_
l
e
a
f
(
s
e
l
f
,
 
c
p
u
_
i
d
,
 
l
e
a
f
,
 
s
u
b
_
l
e
a
f
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
C
P
U
 
c
p
u
i
d
 
i
n
f
o
r
m
a
t
i
o
n
 
f
o
r
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
l
e
a
f
.




 
 
 
 
 
 
 
 
i
n
 
c
p
u
_
i
d
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
I
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
C
P
U
.
 
T
h
e
 
C
P
U
 
m
o
s
t
 
b
e
 
o
n
l
i
n
e
.


 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
u
r
r
e
n
t
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
 
m
i
g
h
t
 
n
o
t
 
n
e
c
e
s
s
a
r
i
l
y
 
r
e
t
u
r
n
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
d
e
s
c
r
i
p
t
i
o
n
 
f
o
r
 
t
h
i
s
 
e
x
a
c
t
 
C
P
U
.




 
 
 
 
 
 
 
 
i
n
 
l
e
a
f
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
i
n
d
e
x
 
(
e
a
x
)
.




 
 
 
 
 
 
 
 
i
n
 
s
u
b
_
l
e
a
f
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
s
u
b
 
i
n
d
e
x
 
(
e
c
x
)
.
 
T
h
i
s
 
c
u
r
r
e
n
t
l
y
 
o
n
l
y
 
a
p
p
l
i
e
s
 
t
o
 
c
a
c
h
e


 
 
 
 
 
 
 
 
 
 
i
n
f
o
r
m
a
t
i
o
n
 
o
n
 
I
n
t
e
l
 
C
P
U
s
.
 
U
s
e
 
0
 
i
f
 
r
e
t
r
i
e
v
i
n
g
 
v
a
l
u
e
s
 
f
o
r


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
e
t
C
P
U
I
D
L
e
a
f
"
/
>
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
a
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
a
x
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
b
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
b
x
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
c
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
c
x
.




 
 
 
 
 
 
 
 
o
u
t
 
v
a
l
_
e
d
x
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
C
P
U
I
D
 
l
e
a
f
 
v
a
l
u
e
 
f
o
r
 
r
e
g
i
s
t
e
r
 
e
d
x
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
P
r
o
c
e
s
s
o
r
C
P
U
I
D
L
e
a
f
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
p
u
_
i
d
,
 
l
e
a
f
,
 
s
u
b
_
l
e
a
f
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
)


 
 
 
 
 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
e
m
o
r
y
_
s
i
z
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
e
m
o
r
y
S
i
z
e
'


 
 
 
 
 
 
 
 
A
m
o
u
n
t
 
o
f
 
s
y
s
t
e
m
 
m
e
m
o
r
y
 
i
n
 
m
e
g
a
b
y
t
e
s
 
i
n
s
t
a
l
l
e
d
 
i
n
 
t
h
e
 
h
o
s
t
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
e
m
o
r
y
S
i
z
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
e
m
o
r
y
_
a
v
a
i
l
a
b
l
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
e
m
o
r
y
A
v
a
i
l
a
b
l
e
'


 
 
 
 
 
 
 
 
A
v
a
i
l
a
b
l
e
 
s
y
s
t
e
m
 
m
e
m
o
r
y
 
i
n
 
t
h
e
 
h
o
s
t
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
e
m
o
r
y
A
v
a
i
l
a
b
l
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
o
p
e
r
a
t
i
n
g
_
s
y
s
t
e
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
o
p
e
r
a
t
i
n
g
S
y
s
t
e
m
'


 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
h
o
s
t
 
s
y
s
t
e
m
'
s
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
o
p
e
r
a
t
i
n
g
S
y
s
t
e
m
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
o
s
_
v
e
r
s
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
O
S
V
e
r
s
i
o
n
'


 
 
 
 
 
 
 
 
H
o
s
t
 
o
p
e
r
a
t
i
n
g
 
s
y
s
t
e
m
'
s
 
v
e
r
s
i
o
n
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
O
S
V
e
r
s
i
o
n
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
u
t
c
_
t
i
m
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
U
T
C
T
i
m
e
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
t
h
e
 
c
u
r
r
e
n
t
 
h
o
s
t
 
t
i
m
e
 
i
n
 
m
i
l
l
i
s
e
c
o
n
d
s
 
s
i
n
c
e
 
1
9
7
0
-
0
1
-
0
1
 
U
T
C
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
U
T
C
T
i
m
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
c
c
e
l
e
r
a
t
i
o
n
3
_
d
_
a
v
a
i
l
a
b
l
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
a
c
c
e
l
e
r
a
t
i
o
n
3
D
A
v
a
i
l
a
b
l
e
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
w
h
e
n
 
t
h
e
 
h
o
s
t
 
s
u
p
p
o
r
t
s
 
3
D
 
h
a
r
d
w
a
r
e
 
a
c
c
e
l
e
r
a
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
c
c
e
l
e
r
a
t
i
o
n
3
D
A
v
a
i
l
a
b
l
e
'
,
 
b
o
o
l
)




 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
h
o
s
t
_
o
n
l
y
_
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
(
s
e
l
f
,
 
o
u
t
_
p
=
{
}
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
n
e
w
 
a
d
a
p
t
e
r
 
f
o
r
 
H
o
s
t
 
O
n
l
y
 
N
e
t
w
o
r
k
i
n
g
.




 
 
 
 
 
 
 
 
o
u
t
 
h
o
s
t
_
i
n
t
e
r
f
a
c
e
 
o
f
 
t
y
p
e
 
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e


 
 
 
 
 
 
 
 
 
 
 
 
C
r
e
a
t
e
d
 
h
o
s
t
 
i
n
t
e
r
f
a
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
H
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
@
a
 
n
a
m
e
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
H
o
s
t
O
n
l
y
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
u
t
_
p
=
o
u
t
_
p
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
h
o
s
t
_
o
n
l
y
_
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
t
h
e
 
g
i
v
e
n
 
H
o
s
t
 
O
n
l
y
 
N
e
t
w
o
r
k
i
n
g
 
i
n
t
e
r
f
a
c
e
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
d
a
p
t
e
r
 
G
U
I
D
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s
 
o
f
 
t
y
p
e
 
I
P
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 
 
 
 
 
P
r
o
g
r
e
s
s
 
o
b
j
e
c
t
 
t
o
 
t
r
a
c
k
 
t
h
e
 
o
p
e
r
a
t
i
o
n
 
c
o
m
p
l
e
t
i
o
n
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
N
o
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
m
a
t
c
h
i
n
g
 
@
a
 
i
d
 
f
o
u
n
d
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
o
g
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
H
o
s
t
O
n
l
y
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
P
r
o
g
r
e
s
s
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
r
o
g
r
e
s
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
c
r
e
a
t
e
_
u
s
b
_
d
e
v
i
c
e
_
f
i
l
t
e
r
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
C
r
e
a
t
e
s
 
a
 
n
e
w
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
.
 
A
l
l
 
a
t
t
r
i
b
u
t
e
s
 
e
x
c
e
p
t


 
 
 
 
 
 
 
 
t
h
e
 
f
i
l
t
e
r
 
n
a
m
e
 
a
r
e
 
s
e
t
 
t
o
 
e
m
p
t
y
 
(
a
n
y
 
m
a
t
c
h
)
,


 
 
 
 
 
 
 
 
a
c
t
i
v
e
 
i
s
 
@
c
 
f
a
l
s
e
 
(
t
h
e
 
f
i
l
t
e
r
 
i
s
 
n
o
t
 
a
c
t
i
v
e
)
.




 
 
 
 
 
 
 
 
T
h
e
 
c
r
e
a
t
e
d
 
f
i
l
t
e
r
 
c
a
n
 
b
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
l
i
s
t
 
o
f
 
f
i
l
t
e
r
s
 
u
s
i
n
g


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
i
n
s
e
r
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
"
/
>
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
F
i
l
t
e
r
 
n
a
m
e
.
 
S
e
e
 
<
l
i
n
k
 
t
o
=
"
I
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
:
:
n
a
m
e
"
/
>
 
f
o
r
 
m
o
r
e
 
i
n
f
o
r
m
a
t
i
o
n
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
t
e
r
_
p
 
o
f
 
t
y
p
e
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r


 
 
 
 
 
 
 
 
 
 
 
 
C
r
e
a
t
e
d
 
f
i
l
t
e
r
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
f
i
l
t
e
r
_
p
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
c
r
e
a
t
e
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
i
l
t
e
r
_
p


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
i
n
s
e
r
t
_
u
s
b
_
d
e
v
i
c
e
_
f
i
l
t
e
r
(
s
e
l
f
,
 
p
o
s
i
t
i
o
n
,
 
f
i
l
t
e
r
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
I
n
s
e
r
t
s
 
t
h
e
 
g
i
v
e
n
 
U
S
B
 
d
e
v
i
c
e
 
t
o
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
o
s
i
t
i
o
n


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
l
i
s
t
 
o
f
 
f
i
l
t
e
r
s
.




 
 
 
 
 
 
 
 
P
o
s
i
t
i
o
n
s
 
a
r
e
 
n
u
m
b
e
r
e
d
 
s
t
a
r
t
i
n
g
 
f
r
o
m
 
@
c
 
0
.
 
I
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d


 
 
 
 
 
 
 
 
p
o
s
i
t
i
o
n
 
i
s
 
e
q
u
a
l
 
t
o
 
o
r
 
g
r
e
a
t
e
r
 
t
h
a
n
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
e
l
e
m
e
n
t
s
 
i
n


 
 
 
 
 
 
 
 
t
h
e
 
l
i
s
t
,
 
t
h
e
 
f
i
l
t
e
r
 
i
s
 
a
d
d
e
d
 
a
t
 
t
h
e
 
e
n
d
 
o
f
 
t
h
e
 
c
o
l
l
e
c
t
i
o
n
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
D
u
p
l
i
c
a
t
e
s
 
a
r
e
 
n
o
t
 
a
l
l
o
w
e
d
,
 
s
o
 
a
n
 
a
t
t
e
m
p
t
 
t
o
 
i
n
s
e
r
t
 
a


 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
 
a
l
r
e
a
d
y
 
i
n
 
t
h
e
 
l
i
s
t
 
i
s
 
a
n
 
e
r
r
o
r
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
U
S
B
 
f
u
n
c
t
i
o
n
a
l
i
t
y
 
i
s
 
n
o
t
 
a
v
a
i
l
a
b
l
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
e
d
i
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
s
e
t
 
t
h
e
 
r
e
s
u
l
t
 
c
o
d
e
 
t
o
 
@
c
 
E
_
N
O
T
I
M
P
L
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>




 
 
 
 
 
 
 
 
i
n
 
p
o
s
i
t
i
o
n
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
s
i
t
i
o
n
 
t
o
 
i
n
s
e
r
t
 
t
h
e
 
f
i
l
t
e
r
 
t
o
.




 
 
 
 
 
 
 
 
i
n
 
f
i
l
t
e
r
_
p
 
o
f
 
t
y
p
e
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r


 
 
 
 
 
 
 
 
 
 
 
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
 
t
o
 
i
n
s
e
r
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
I
N
V
A
L
I
D
_
O
B
J
E
C
T
_
S
T
A
T
E


 
 
 
 
 
 
 
 
 
 
 
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
 
i
s
 
n
o
t
 
c
r
e
a
t
e
d
 
w
i
t
h
i
n
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
n
c
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
 
a
l
r
e
a
d
y
 
i
n
 
l
i
s
t
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
i
n
s
e
r
t
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
o
s
i
t
i
o
n
,
 
f
i
l
t
e
r
_
p
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
r
e
m
o
v
e
_
u
s
b
_
d
e
v
i
c
e
_
f
i
l
t
e
r
(
s
e
l
f
,
 
p
o
s
i
t
i
o
n
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
m
o
v
e
s
 
a
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
 
f
r
o
m
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
p
o
s
i
t
i
o
n
 
i
n
 
t
h
e


 
 
 
 
 
 
 
 
l
i
s
t
 
o
f
 
f
i
l
t
e
r
s
.




 
 
 
 
 
 
 
 
P
o
s
i
t
i
o
n
s
 
a
r
e
 
n
u
m
b
e
r
e
d
 
s
t
a
r
t
i
n
g
 
f
r
o
m
 
@
c
 
0
.
 
S
p
e
c
i
f
y
i
n
g
 
a


 
 
 
 
 
 
 
 
p
o
s
i
t
i
o
n
 
e
q
u
a
l
 
t
o
 
o
r
 
g
r
e
a
t
e
r
 
t
h
a
n
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
e
l
e
m
e
n
t
s
 
i
n


 
 
 
 
 
 
 
 
t
h
e
 
l
i
s
t
 
w
i
l
l
 
p
r
o
d
u
c
e
 
a
n
 
e
r
r
o
r
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
I
f
 
U
S
B
 
f
u
n
c
t
i
o
n
a
l
i
t
y
 
i
s
 
n
o
t
 
a
v
a
i
l
a
b
l
e
 
i
n
 
t
h
e
 
g
i
v
e
n
 
e
d
i
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
,
 
t
h
i
s
 
m
e
t
h
o
d
 
w
i
l
l
 
s
e
t
 
t
h
e
 
r
e
s
u
l
t
 
c
o
d
e
 
t
o
 
@
c
 
E
_
N
O
T
I
M
P
L
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
s
"
/
>




 
 
 
 
 
 
 
 
i
n
 
p
o
s
i
t
i
o
n
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
P
o
s
i
t
i
o
n
 
t
o
 
r
e
m
o
v
e
 
t
h
e
 
f
i
l
t
e
r
 
f
r
o
m
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
E
_
I
N
V
A
L
I
D
A
R
G


 
 
 
 
 
 
 
 
 
 
 
 
U
S
B
 
d
e
v
i
c
e
 
f
i
l
t
e
r
 
l
i
s
t
 
e
m
p
t
y
 
o
r
 
i
n
v
a
l
i
d
 
@
a
 
p
o
s
i
t
i
o
n
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
r
e
m
o
v
e
U
S
B
D
e
v
i
c
e
F
i
l
t
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
p
o
s
i
t
i
o
n
]
)


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
h
o
s
t
_
d
v
d
_
d
r
i
v
e
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
f
o
r
 
a
 
h
o
s
t
 
D
V
D
 
d
r
i
v
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
@
c
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
h
o
s
t
 
d
r
i
v
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
r
i
v
e
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
h
o
s
t
 
d
r
i
v
e
 
o
b
j
e
c
t




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
G
i
v
e
n
 
@
c
 
n
a
m
e
 
d
o
e
s
 
n
o
t
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
h
o
s
t
 
d
r
i
v
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
r
i
v
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
H
o
s
t
D
V
D
D
r
i
v
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
r
i
v
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
h
o
s
t
_
f
l
o
p
p
y
_
d
r
i
v
e
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
f
o
r
 
a
 
h
o
s
t
 
f
l
o
p
p
y
 
d
r
i
v
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
@
c
 
n
a
m
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
h
o
s
t
 
f
l
o
p
p
y
 
d
r
i
v
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
r
i
v
e
 
o
f
 
t
y
p
e
 
I
M
e
d
i
u
m


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
h
o
s
t
 
f
l
o
p
p
y
 
d
r
i
v
e
 
o
b
j
e
c
t




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
G
i
v
e
n
 
@
c
 
n
a
m
e
 
d
o
e
s
 
n
o
t
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
h
o
s
t
 
f
l
o
p
p
y
 
d
r
i
v
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
r
i
v
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
H
o
s
t
F
l
o
p
p
y
D
r
i
v
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
M
e
d
i
u
m
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
r
i
v
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
h
o
s
t
_
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
_
b
y
_
n
a
m
e
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
t
h
r
o
u
g
h
 
a
l
l
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
s
 
f
o
r
 
a
n
 
i
n
t
e
r
f
a
c
e
 
w
i
t
h


 
 
 
 
 
 
 
 
t
h
e
 
g
i
v
e
n
 
@
c
 
n
a
m
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
e
t
h
o
d
 
r
e
t
u
r
n
s
 
a
n
 
e
r
r
o
r
 
i
f
 
t
h
e
 
g
i
v
e
n
 
@
c
 
n
a
m
e
 
d
o
e
s
 
n
o
t


 
 
 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
.




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
a
m
e
 
o
f
 
t
h
e
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
 
o
f
 
t
y
p
e
 
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
B
y
N
a
m
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
h
o
s
t
_
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
_
b
y
_
i
d
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
t
h
r
o
u
g
h
 
a
l
l
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
s
 
f
o
r
 
a
n
 
i
n
t
e
r
f
a
c
e
 
w
i
t
h


 
 
 
 
 
 
 
 
t
h
e
 
g
i
v
e
n
 
G
U
I
D
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
e
t
h
o
d
 
r
e
t
u
r
n
s
 
a
n
 
e
r
r
o
r
 
i
f
 
t
h
e
 
g
i
v
e
n
 
G
U
I
D
 
d
o
e
s
 
n
o
t


 
 
 
 
 
 
 
 
 
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
.




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
G
U
I
D
 
o
f
 
t
h
e
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
 
o
f
 
t
y
p
e
 
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
B
y
I
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
h
o
s
t
_
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
s
_
o
f
_
t
y
p
e
(
s
e
l
f
,
 
t
y
p
e
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
t
h
r
o
u
g
h
 
a
l
l
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
s
 
a
n
d
 
r
e
t
u
r
n
s
 
a
 
l
i
s
t
 
o
f
 
i
n
t
e
r
f
a
c
e
s
 
o
f
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
t
y
p
e




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
t
y
p
e
 
o
f
 
t
h
e
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
s
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
s
 
o
f
 
t
y
p
e
 
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
h
o
s
t
 
n
e
t
w
o
r
k
 
i
n
t
e
r
f
a
c
e
 
o
b
j
e
c
t
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
s
O
f
T
y
p
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
t
y
p
e
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
H
o
s
t
N
e
t
w
o
r
k
I
n
t
e
r
f
a
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
t
w
o
r
k
_
i
n
t
e
r
f
a
c
e
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
u
s
b
_
d
e
v
i
c
e
_
b
y
_
i
d
(
s
e
l
f
,
 
i
d
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
f
o
r
 
a
 
U
S
B
 
d
e
v
i
c
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
U
U
I
D
.




 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
U
S
B
D
e
v
i
c
e
:
:
i
d
"
/
>




 
 
 
 
 
 
 
 
i
n
 
i
d
_
p
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
U
U
I
D
 
o
f
 
t
h
e
 
U
S
B
 
d
e
v
i
c
e
 
t
o
 
s
e
a
r
c
h
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
U
S
B
 
d
e
v
i
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
G
i
v
e
n
 
@
c
 
i
d
 
d
o
e
s
 
n
o
t
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
U
S
B
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
U
S
B
D
e
v
i
c
e
B
y
I
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
i
d
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
H
o
s
t
U
S
B
D
e
v
i
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
f
i
n
d
_
u
s
b
_
d
e
v
i
c
e
_
b
y
_
a
d
d
r
e
s
s
(
s
e
l
f
,
 
n
a
m
e
)
:


 
 
 
 
 
 
 
 
"
"
"
S
e
a
r
c
h
e
s
 
f
o
r
 
a
 
U
S
B
 
d
e
v
i
c
e
 
w
i
t
h
 
t
h
e
 
g
i
v
e
n
 
h
o
s
t
 
a
d
d
r
e
s
s
.




 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
U
S
B
D
e
v
i
c
e
:
:
a
d
d
r
e
s
s
"
/
>




 
 
 
 
 
 
 
 
i
n
 
n
a
m
e
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
A
d
d
r
e
s
s
 
o
f
 
t
h
e
 
U
S
B
 
d
e
v
i
c
e
 
(
a
s
 
a
s
s
i
g
n
e
d
 
b
y
 
t
h
e
 
h
o
s
t
)
 
t
o


 
 
 
 
 
 
 
 
 
 
s
e
a
r
c
h
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
 
o
f
 
t
y
p
e
 
I
H
o
s
t
U
S
B
D
e
v
i
c
e


 
 
 
 
 
 
 
 
 
 
 
 
F
o
u
n
d
 
U
S
B
 
d
e
v
i
c
e
 
o
b
j
e
c
t
.




 
 
 
 
 
 
 
 
r
a
i
s
e
s
 
V
B
O
X
_
E
_
O
B
J
E
C
T
_
N
O
T
_
F
O
U
N
D


 
 
 
 
 
 
 
 
 
 
 
 
G
i
v
e
n
 
@
c
 
n
a
m
e
 
d
o
e
s
 
n
o
t
 
c
o
r
r
e
s
p
o
n
d
 
t
o
 
a
n
y
 
U
S
B
 
d
e
v
i
c
e
.


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
v
i
c
e
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
f
i
n
d
U
S
B
D
e
v
i
c
e
B
y
A
d
d
r
e
s
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
n
a
m
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
I
H
o
s
t
U
S
B
D
e
v
i
c
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
n
e
r
a
t
e
_
m
a
c
_
a
d
d
r
e
s
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
n
e
r
a
t
e
s
 
a
 
v
a
l
i
d
 
E
t
h
e
r
n
e
t
 
M
A
C
 
a
d
d
r
e
s
s
,
 
1
2
 
h
e
x
a
d
e
c
i
m
a
l
 
c
h
a
r
a
c
t
e
r
s
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
d
d
r
e
s
s
 
o
f
 
t
y
p
e
 
s
t
r


 
 
 
 
 
 
 
 
 
 
 
 
N
e
w
 
E
t
h
e
r
n
e
t
 
M
A
C
 
a
d
d
r
e
s
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
a
d
d
r
e
s
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
n
e
r
a
t
e
M
A
C
A
d
d
r
e
s
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
s
t
r
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
d
d
r
e
s
s


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
 
i
n
t
e
r
f
a
c
e
 
r
e
p
r
e
s
e
n
t
s
 
g
l
o
b
a
l
 
p
r
o
p
e
r
t
i
e
s
 
o
f
 
t
h
e
 
g
i
v
e
n


 
 
 
 
 
 
V
i
r
t
u
a
l
B
o
x
 
i
n
s
t
a
l
l
a
t
i
o
n
.




 
 
 
 
 
 
T
h
e
s
e
 
p
r
o
p
e
r
t
i
e
s
 
d
e
f
i
n
e
 
l
i
m
i
t
s
 
a
n
d
 
d
e
f
a
u
l
t
 
v
a
l
u
e
s
 
f
o
r
 
v
a
r
i
o
u
s
 
a
t
t
r
i
b
u
t
e
s


 
 
 
 
 
 
a
n
d
 
p
a
r
a
m
e
t
e
r
s
.
 
M
o
s
t
 
o
f
 
t
h
e
 
p
r
o
p
e
r
t
i
e
s
 
a
r
e
 
r
e
a
d
-
o
n
l
y
,
 
b
u
t
 
s
o
m
e
 
c
a
n
 
b
e


 
 
 
 
 
 
c
h
a
n
g
e
d
 
b
y
 
a
 
u
s
e
r
.


 
 
 
 
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
4
1
3
e
a
9
4
c
-
e
f
d
9
-
4
9
1
e
-
8
1
f
c
-
5
d
f
0
c
4
d
8
6
4
b
b
'


 
 
 
 
w
s
m
a
p
 
=
 
'
m
a
n
a
g
e
d
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
i
n
_
g
u
e
s
t
_
r
a
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
i
n
G
u
e
s
t
R
A
M
'


 
 
 
 
 
 
 
 
M
i
n
i
m
u
m
 
g
u
e
s
t
 
s
y
s
t
e
m
 
m
e
m
o
r
y
 
i
n
 
M
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
i
n
G
u
e
s
t
R
A
M
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
x
_
g
u
e
s
t
_
r
a
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
a
x
G
u
e
s
t
R
A
M
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
g
u
e
s
t
 
s
y
s
t
e
m
 
m
e
m
o
r
y
 
i
n
 
M
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
x
G
u
e
s
t
R
A
M
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
i
n
_
g
u
e
s
t
_
v
r
a
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
i
n
G
u
e
s
t
V
R
A
M
'


 
 
 
 
 
 
 
 
M
i
n
i
m
u
m
 
g
u
e
s
t
 
v
i
d
e
o
 
m
e
m
o
r
y
 
i
n
 
M
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
i
n
G
u
e
s
t
V
R
A
M
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
x
_
g
u
e
s
t
_
v
r
a
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
a
x
G
u
e
s
t
V
R
A
M
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
g
u
e
s
t
 
v
i
d
e
o
 
m
e
m
o
r
y
 
i
n
 
M
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
x
G
u
e
s
t
V
R
A
M
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
i
n
_
g
u
e
s
t
_
c
p
u
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
i
n
G
u
e
s
t
C
P
U
C
o
u
n
t
'


 
 
 
 
 
 
 
 
M
i
n
i
m
u
m
 
C
P
U
 
c
o
u
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
i
n
G
u
e
s
t
C
P
U
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
x
_
g
u
e
s
t
_
c
p
u
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
a
x
G
u
e
s
t
C
P
U
C
o
u
n
t
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
C
P
U
 
c
o
u
n
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
x
G
u
e
s
t
C
P
U
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
x
_
g
u
e
s
t
_
m
o
n
i
t
o
r
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
a
x
G
u
e
s
t
M
o
n
i
t
o
r
s
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
o
f
 
m
o
n
i
t
o
r
s
 
w
h
i
c
h
 
c
o
u
l
d
 
b
e
 
c
o
n
n
e
c
t
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
x
G
u
e
s
t
M
o
n
i
t
o
r
s
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
n
f
o
_
v
d
_
s
i
z
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
i
n
f
o
V
D
S
i
z
e
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
s
i
z
e
 
o
f
 
a
 
v
i
r
t
u
a
l
 
d
i
s
k
 
i
m
a
g
e
 
i
n
 
b
y
t
e
s
.
 
I
n
f
o
r
m
a
t
i
o
n
a
l
 
v
a
l
u
e
,


 
 
 
 
 
 
d
o
e
s
 
n
o
t
 
r
e
f
l
e
c
t
 
t
h
e
 
l
i
m
i
t
s
 
o
f
 
a
n
y
 
v
i
r
t
u
a
l
 
d
i
s
k
 
i
m
a
g
e
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
n
f
o
V
D
S
i
z
e
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
s
e
r
i
a
l
_
p
o
r
t
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
s
e
r
i
a
l
P
o
r
t
C
o
u
n
t
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
s
e
r
i
a
l
 
p
o
r
t
s
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
e
v
e
r
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>
 
i
n
s
t
a
n
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
s
e
r
i
a
l
P
o
r
t
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
p
a
r
a
l
l
e
l
_
p
o
r
t
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
p
a
r
a
l
l
e
l
P
o
r
t
C
o
u
n
t
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
p
a
r
a
l
l
e
l
 
p
o
r
t
s
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
e
v
e
r
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>
 
i
n
s
t
a
n
c
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
p
a
r
a
l
l
e
l
P
o
r
t
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
a
x
_
b
o
o
t
_
p
o
s
i
t
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
m
a
x
B
o
o
t
P
o
s
i
t
i
o
n
'


 
 
 
 
 
 
 
 
M
a
x
i
m
u
m
 
d
e
v
i
c
e
 
p
o
s
i
t
i
o
n
 
i
n
 
t
h
e
 
b
o
o
t
 
o
r
d
e
r
.
 
T
h
i
s
 
v
a
l
u
e
 
c
o
r
r
e
s
p
o
n
d
s


 
 
 
 
 
 
 
 
t
o
 
t
h
e
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
d
e
v
i
c
e
s
 
a
 
m
a
c
h
i
n
e
 
c
a
n
 
b
o
o
t
 
f
r
o
m
,
 
t
o
 
m
a
k
e
 
i
t


 
 
 
 
 
 
 
 
p
o
s
s
i
b
l
e
 
t
o
 
i
n
c
l
u
d
e
 
a
l
l
 
p
o
s
s
i
b
l
e
 
d
e
v
i
c
e
s
 
t
o
 
t
h
e
 
b
o
o
t
 
l
i
s
t
.


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
s
e
t
B
o
o
t
O
r
d
e
r
"
/
>


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
a
x
B
o
o
t
P
o
s
i
t
i
o
n
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
m
a
c
h
i
n
e
_
f
o
l
d
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
f
a
u
l
t
M
a
c
h
i
n
e
F
o
l
d
e
r
'


 
 
 
 
 
 
 
 
F
u
l
l
 
p
a
t
h
 
t
o
 
t
h
e
 
d
e
f
a
u
l
t
 
d
i
r
e
c
t
o
r
y
 
u
s
e
d
 
t
o
 
c
r
e
a
t
e
 
n
e
w
 
o
r
 
o
p
e
n


 
 
 
 
 
 
 
 
e
x
i
s
t
i
n
g
 
m
a
c
h
i
n
e
s
 
w
h
e
n
 
a
 
m
a
c
h
i
n
e
 
s
e
t
t
i
n
g
s
 
f
i
l
e
 
n
a
m
e
 
c
o
n
t
a
i
n
s
 
n
o


 
 
 
 
 
 
 
 
p
a
t
h
.




 
 
 
 
 
 
 
 
S
t
a
r
t
i
n
g
 
w
i
t
h
 
V
i
r
t
u
a
l
B
o
x
 
4
.
0
,
 
b
y
 
d
e
f
a
u
l
t
,
 
t
h
i
s
 
a
t
t
r
i
b
u
t
e
 
c
o
n
t
a
i
n
s


 
 
 
 
 
 
 
 
t
h
e
 
f
u
l
l
 
p
a
t
h
 
o
f
 
f
o
l
d
e
r
 
n
a
m
e
d
 
"
V
i
r
t
u
a
l
B
o
x
 
V
M
s
"
 
i
n
 
t
h
e
 
u
s
e
r
'
s


 
 
 
 
 
 
 
 
h
o
m
e
 
d
i
r
e
c
t
o
r
y
,
 
w
h
i
c
h
 
d
e
p
e
n
d
s
 
o
n
 
t
h
e
 
h
o
s
t
 
p
l
a
t
f
o
r
m
.




 
 
 
 
 
 
 
 
W
h
e
n
 
s
e
t
t
i
n
g
 
t
h
i
s
 
a
t
t
r
i
b
u
t
e
,
 
a
 
f
u
l
l
 
p
a
t
h
 
m
u
s
t
 
b
e
 
s
p
e
c
i
f
i
e
d
.


 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
t
o
 
@
c
 
n
u
l
l
 
o
r
 
a
n
 
e
m
p
t
y
 
s
t
r
i
n
g
 
o
r
 
t
h
e


 
 
 
 
 
 
 
 
s
p
e
c
i
a
l
 
v
a
l
u
e
 
"
M
a
c
h
i
n
e
s
"
 
(
f
o
r
 
c
o
m
p
a
t
i
b
i
l
i
t
y
 
r
e
a
s
o
n
s
)
 
w
i
l
l
 
r
e
s
t
o
r
e


 
 
 
 
 
 
 
 
t
h
a
t
 
d
e
f
a
u
l
t
 
v
a
l
u
e
.




 
 
 
 
 
 
 
 
I
f
 
t
h
e
 
f
o
l
d
e
r
 
s
p
e
c
i
f
i
e
d
 
h
e
r
e
i
n
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
,
 
i
t
 
w
i
l
l
 
b
e
 
c
r
e
a
t
e
d


 
 
 
 
 
 
 
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
a
s
 
n
e
e
d
e
d
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
M
a
c
h
i
n
e
"
/
>
,


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
o
p
e
n
M
a
c
h
i
n
e
"
/
>


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
M
a
c
h
i
n
e
F
o
l
d
e
r
'
,
 
s
t
r
)




 
 
 
 
@
d
e
f
a
u
l
t
_
m
a
c
h
i
n
e
_
f
o
l
d
e
r
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
m
a
c
h
i
n
e
_
f
o
l
d
e
r
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
M
a
c
h
i
n
e
F
o
l
d
e
r
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
m
e
d
i
u
m
_
f
o
r
m
a
t
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
I
M
e
d
i
u
m
F
o
r
m
a
t
 
v
a
l
u
e
 
f
o
r
 
'
m
e
d
i
u
m
F
o
r
m
a
t
s
'


 
 
 
 
 
 
 
 
L
i
s
t
 
o
f
 
a
l
l
 
m
e
d
i
u
m
 
s
t
o
r
a
g
e
 
f
o
r
m
a
t
s
 
s
u
p
p
o
r
t
e
d
 
b
y
 
t
h
i
s
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
i
n
s
t
a
l
l
a
t
i
o
n
.




 
 
 
 
 
 
 
 
K
e
e
p
 
i
n
 
m
i
n
d
 
t
h
a
t
 
t
h
e
 
m
e
d
i
u
m
 
f
o
r
m
a
t
 
i
d
e
n
t
i
f
i
e
r


 
 
 
 
 
 
 
 
(
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
F
o
r
m
a
t
:
:
i
d
"
/
>
)
 
u
s
e
d
 
i
n
 
o
t
h
e
r
 
A
P
I
 
c
a
l
l
s
 
l
i
k
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
H
a
r
d
D
i
s
k
"
/
>
 
t
o
 
r
e
f
e
r
 
t
o
 
a
 
p
a
r
t
i
c
u
l
a
r


 
 
 
 
 
 
 
 
m
e
d
i
u
m
 
f
o
r
m
a
t
 
i
s
 
a
 
c
a
s
e
-
i
n
s
e
n
s
i
t
i
v
e
 
s
t
r
i
n
g
.
 
T
h
i
s
 
m
e
a
n
s
 
t
h
a
t
,
 
f
o
r


 
 
 
 
 
 
 
 
e
x
a
m
p
l
e
,
 
a
l
l
 
o
f
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
t
r
i
n
g
s
:


 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
"
V
D
I
"


 
 
 
 
 
 
 
 
 
 
"
v
d
i
"


 
 
 
 
 
 
 
 
 
 
"
V
d
I
"


 
 
 
 
 
 
 
 
r
e
f
e
r
 
t
o
 
t
h
e
 
s
a
m
e
 
m
e
d
i
u
m
 
f
o
r
m
a
t
.




 
 
 
 
 
 
 
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
v
i
r
t
u
a
l
 
m
e
d
i
u
m
 
f
r
a
m
e
w
o
r
k
 
i
s
 
b
a
c
k
e
n
d
-
b
a
s
e
d
,
 
t
h
e
r
e
f
o
r
e


 
 
 
 
 
 
 
 
t
h
e
 
l
i
s
t
 
o
f
 
s
u
p
p
o
r
t
e
d
 
f
o
r
m
a
t
s
 
d
e
p
e
n
d
s
 
o
n
 
w
h
a
t
 
b
a
c
k
e
n
d
s
 
a
r
e
 
c
u
r
r
e
n
t
l
y


 
 
 
 
 
 
 
 
i
n
s
t
a
l
l
e
d
.




 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
F
o
r
m
a
t
"
/
>


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
m
e
d
i
u
m
F
o
r
m
a
t
s
'
,
 
I
M
e
d
i
u
m
F
o
r
m
a
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
h
a
r
d
_
d
i
s
k
_
f
o
r
m
a
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
f
a
u
l
t
H
a
r
d
D
i
s
k
F
o
r
m
a
t
'


 
 
 
 
 
 
 
 
I
d
e
n
t
i
f
i
e
r
 
o
f
 
t
h
e
 
d
e
f
a
u
l
t
 
m
e
d
i
u
m
 
f
o
r
m
a
t
 
u
s
e
d
 
b
y
 
V
i
r
t
u
a
l
B
o
x
.




 
 
 
 
 
 
 
 
T
h
e
 
m
e
d
i
u
m
 
f
o
r
m
a
t
 
s
e
t
 
b
y
 
t
h
i
s
 
a
t
t
r
i
b
u
t
e
 
i
s
 
u
s
e
d
 
b
y
 
V
i
r
t
u
a
l
B
o
x


 
 
 
 
 
 
 
 
w
h
e
n
 
t
h
e
 
m
e
d
i
u
m
 
f
o
r
m
a
t
 
w
a
s
 
n
o
t
 
s
p
e
c
i
f
i
e
d
 
e
x
p
l
i
c
i
t
l
y
.
 
O
n
e
 
e
x
a
m
p
l
e
 
i
s


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
H
a
r
d
D
i
s
k
"
/
>
 
w
i
t
h
 
t
h
e
 
e
m
p
t
y


 
 
 
 
 
 
 
 
f
o
r
m
a
t
 
a
r
g
u
m
e
n
t
.
 
A
 
m
o
r
e
 
c
o
m
p
l
e
x
 
e
x
a
m
p
l
e
 
i
s
 
i
m
p
l
i
c
i
t
 
c
r
e
a
t
i
o
n
 
o
f


 
 
 
 
 
 
 
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
 
w
h
e
n
 
t
a
k
i
n
g
 
a
 
s
n
a
p
s
h
o
t
 
o
f
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
:


 
 
 
 
 
 
 
 
t
h
i
s
 
o
p
e
r
a
t
i
o
n
 
w
i
l
l
 
t
r
y
 
t
o
 
u
s
e
 
a
 
f
o
r
m
a
t
 
o
f
 
t
h
e
 
p
a
r
e
n
t
 
m
e
d
i
u
m
 
f
i
r
s
t


 
 
 
 
 
 
 
 
a
n
d
 
i
f
 
t
h
i
s
 
f
o
r
m
a
t
 
d
o
e
s
 
n
o
t
 
s
u
p
p
o
r
t
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
 
t
h
e
 
d
e
f
a
u
l
t


 
 
 
 
 
 
 
 
f
o
r
m
a
t
 
s
p
e
c
i
f
i
e
d
 
b
y
 
t
h
i
s
 
a
r
g
u
m
e
n
t
 
w
i
l
l
 
b
e
 
u
s
e
d
.




 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
o
f
 
s
u
p
p
o
r
t
e
d
 
m
e
d
i
u
m
 
f
o
r
m
a
t
s
 
m
a
y
 
b
e
 
o
b
t
a
i
n
e
d
 
b
y
 
t
h
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
m
e
d
i
u
m
F
o
r
m
a
t
s
"
/
>
 
c
a
l
l
.
 
N
o
t
e
 
t
h
a
t
 
t
h
e
 
d
e
f
a
u
l
t
 
m
e
d
i
u
m


 
 
 
 
 
 
 
 
f
o
r
m
a
t
 
m
u
s
t
 
h
a
v
e
 
a
 
c
a
p
a
b
i
l
i
t
y
 
t
o
 
c
r
e
a
t
e
 
d
i
f
f
e
r
e
n
c
i
n
g
 
m
e
d
i
a
;


 
 
 
 
 
 
 
 
o
t
h
e
r
w
i
s
e
 
o
p
e
r
a
t
i
o
n
s
 
t
h
a
t
 
c
r
e
a
t
e
 
m
e
d
i
a
 
i
m
p
l
i
c
i
t
l
y
 
m
a
y
 
f
a
i
l


 
 
 
 
 
 
 
 
u
n
e
x
p
e
c
t
e
d
l
y
.




 
 
 
 
 
 
 
 
T
h
e
 
i
n
i
t
i
a
l
 
v
a
l
u
e
 
o
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
"
V
D
I
"
 
i
n
 
t
h
e
 
c
u
r
r
e
n
t


 
 
 
 
 
 
 
 
v
e
r
s
i
o
n
 
o
f
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
p
r
o
d
u
c
t
,
 
b
u
t
 
m
a
y
 
c
h
a
n
g
e
 
i
n
 
t
h
e
 
f
u
t
u
r
e
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
t
o
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
 
s
t
r
i
n
g
 
w
i
l
l
 
r
e
s
t
o
r
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
i
n
i
t
i
a
l
 
v
a
l
u
e
.


 
 
 
 
 
 
 
 




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
#
m
e
d
i
u
m
F
o
r
m
a
t
s
"
/
>
,


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
e
d
i
u
m
F
o
r
m
a
t
:
:
i
d
"
/
>
,


 
 
 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
V
i
r
t
u
a
l
B
o
x
:
:
c
r
e
a
t
e
H
a
r
d
D
i
s
k
"
/
>


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
H
a
r
d
D
i
s
k
F
o
r
m
a
t
'
,
 
s
t
r
)




 
 
 
 
@
d
e
f
a
u
l
t
_
h
a
r
d
_
d
i
s
k
_
f
o
r
m
a
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
h
a
r
d
_
d
i
s
k
_
f
o
r
m
a
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
H
a
r
d
D
i
s
k
F
o
r
m
a
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
w
a
r
n
i
n
g
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
f
r
e
e
D
i
s
k
S
p
a
c
e
W
a
r
n
i
n
g
'


 
 
 
 
 
 
 
 
I
s
s
u
e
 
a
 
w
a
r
n
i
n
g
 
i
f
 
t
h
e
 
f
r
e
e
 
d
i
s
k
 
s
p
a
c
e
 
i
s
 
b
e
l
o
w
 
(
o
r
 
i
n
 
s
o
m
e
 
d
i
s
k


 
 
 
 
 
 
i
n
t
e
n
s
i
v
e
 
o
p
e
r
a
t
i
o
n
 
i
s
 
e
x
p
e
c
t
e
d
 
t
o
 
g
o
 
b
e
l
o
w
)
 
t
h
e
 
g
i
v
e
n
 
s
i
z
e
 
i
n


 
 
 
 
 
 
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
W
a
r
n
i
n
g
'
,
 
i
n
t
)




 
 
 
 
@
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
w
a
r
n
i
n
g
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
w
a
r
n
i
n
g
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
W
a
r
n
i
n
g
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
p
e
r
c
e
n
t
_
w
a
r
n
i
n
g
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
f
r
e
e
D
i
s
k
S
p
a
c
e
P
e
r
c
e
n
t
W
a
r
n
i
n
g
'


 
 
 
 
 
 
 
 
I
s
s
u
e
 
a
 
w
a
r
n
i
n
g
 
i
f
 
t
h
e
 
f
r
e
e
 
d
i
s
k
 
s
p
a
c
e
 
i
s
 
b
e
l
o
w
 
(
o
r
 
i
n
 
s
o
m
e
 
d
i
s
k


 
 
 
 
 
 
i
n
t
e
n
s
i
v
e
 
o
p
e
r
a
t
i
o
n
 
i
s
 
e
x
p
e
c
t
e
d
 
t
o
 
g
o
 
b
e
l
o
w
)
 
t
h
e
 
g
i
v
e
n
 
p
e
r
c
e
n
t
a
g
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
P
e
r
c
e
n
t
W
a
r
n
i
n
g
'
,
 
i
n
t
)




 
 
 
 
@
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
p
e
r
c
e
n
t
_
w
a
r
n
i
n
g
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
p
e
r
c
e
n
t
_
w
a
r
n
i
n
g
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
P
e
r
c
e
n
t
W
a
r
n
i
n
g
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
e
r
r
o
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
f
r
e
e
D
i
s
k
S
p
a
c
e
E
r
r
o
r
'


 
 
 
 
 
 
 
 
I
s
s
u
e
 
a
n
 
e
r
r
o
r
 
i
f
 
t
h
e
 
f
r
e
e
 
d
i
s
k
 
s
p
a
c
e
 
i
s
 
b
e
l
o
w
 
(
o
r
 
i
n
 
s
o
m
e
 
d
i
s
k


 
 
 
 
 
 
i
n
t
e
n
s
i
v
e
 
o
p
e
r
a
t
i
o
n
 
i
s
 
e
x
p
e
c
t
e
d
 
t
o
 
g
o
 
b
e
l
o
w
)
 
t
h
e
 
g
i
v
e
n
 
s
i
z
e
 
i
n


 
 
 
 
 
 
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
E
r
r
o
r
'
,
 
i
n
t
)




 
 
 
 
@
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
e
r
r
o
r
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
e
r
r
o
r
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
E
r
r
o
r
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
p
e
r
c
e
n
t
_
e
r
r
o
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
f
r
e
e
D
i
s
k
S
p
a
c
e
P
e
r
c
e
n
t
E
r
r
o
r
'


 
 
 
 
 
 
 
 
I
s
s
u
e
 
a
n
 
e
r
r
o
r
 
i
f
 
t
h
e
 
f
r
e
e
 
d
i
s
k
 
s
p
a
c
e
 
i
s
 
b
e
l
o
w
 
(
o
r
 
i
n
 
s
o
m
e
 
d
i
s
k


 
 
 
 
 
 
i
n
t
e
n
s
i
v
e
 
o
p
e
r
a
t
i
o
n
 
i
s
 
e
x
p
e
c
t
e
d
 
t
o
 
g
o
 
b
e
l
o
w
)
 
t
h
e
 
g
i
v
e
n
 
p
e
r
c
e
n
t
a
g
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
P
e
r
c
e
n
t
E
r
r
o
r
'
,
 
i
n
t
)




 
 
 
 
@
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
p
e
r
c
e
n
t
_
e
r
r
o
r
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
f
r
e
e
_
d
i
s
k
_
s
p
a
c
e
_
p
e
r
c
e
n
t
_
e
r
r
o
r
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
f
r
e
e
D
i
s
k
S
p
a
c
e
P
e
r
c
e
n
t
E
r
r
o
r
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
v
r
d
e
_
a
u
t
h
_
l
i
b
r
a
r
y
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
V
R
D
E
A
u
t
h
L
i
b
r
a
r
y
'


 
 
 
 
 
 
 
 
L
i
b
r
a
r
y
 
t
h
a
t
 
p
r
o
v
i
d
e
s
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
 
f
o
r
 
R
e
m
o
t
e
 
D
e
s
k
t
o
p
 
c
l
i
e
n
t
s
.
 
T
h
e
 
l
i
b
r
a
r
y


 
 
 
 
 
 
 
 
i
s
 
u
s
e
d
 
i
f
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
'
s
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
 
t
y
p
e
 
i
s
 
s
e
t
 
t
o
 
"
e
x
t
e
r
n
a
l
"


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
V
M
 
R
e
m
o
t
e
D
i
s
p
l
a
y
 
c
o
n
f
i
g
u
r
a
t
i
o
n
.




 
 
 
 
 
 
 
 
T
h
e
 
s
y
s
t
e
m
 
l
i
b
r
a
r
y
 
e
x
t
e
n
s
i
o
n
 
(
"
.
D
L
L
"
 
o
r
 
"
.
s
o
"
)
 
m
u
s
t
 
b
e
 
o
m
i
t
t
e
d
.


 
 
 
 
 
 
 
 
A
 
f
u
l
l
 
p
a
t
h
 
c
a
n
 
b
e
 
s
p
e
c
i
f
i
e
d
;
 
i
f
 
n
o
t
,
 
t
h
e
n
 
t
h
e
 
l
i
b
r
a
r
y
 
m
u
s
t
 
r
e
s
i
d
e
 
o
n
 
t
h
e


 
 
 
 
 
 
 
 
s
y
s
t
e
m
'
s
 
d
e
f
a
u
l
t
 
l
i
b
r
a
r
y
 
p
a
t
h
.




 
 
 
 
 
 
 
 
T
h
e
 
d
e
f
a
u
l
t
 
v
a
l
u
e
 
o
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
"
V
B
o
x
A
u
t
h
"
.
 
T
h
e
r
e
 
i
s
 
a
 
l
i
b
r
a
r
y


 
 
 
 
 
 
 
 
o
f
 
t
h
a
t
 
n
a
m
e
 
i
n
 
o
n
e
 
o
f
 
t
h
e
 
d
e
f
a
u
l
t
 
V
i
r
t
u
a
l
B
o
x
 
l
i
b
r
a
r
y
 
d
i
r
e
c
t
o
r
i
e
s
.




 
 
 
 
 
 
 
 
F
o
r
 
d
e
t
a
i
l
s
 
a
b
o
u
t
 
V
i
r
t
u
a
l
B
o
x
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
 
l
i
b
r
a
r
i
e
s
 
a
n
d
 
h
o
w
 
t
o
 
i
m
p
l
e
m
e
n
t


 
 
 
 
 
 
 
 
t
h
e
m
,
 
p
l
e
a
s
e
 
r
e
f
e
r
 
t
o
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
m
a
n
u
a
l
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
t
o
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
 
s
t
r
i
n
g
 
w
i
l
l
 
r
e
s
t
o
r
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
i
n
i
t
i
a
l
 
v
a
l
u
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
V
R
D
E
A
u
t
h
L
i
b
r
a
r
y
'
,
 
s
t
r
)




 
 
 
 
@
v
r
d
e
_
a
u
t
h
_
l
i
b
r
a
r
y
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
v
r
d
e
_
a
u
t
h
_
l
i
b
r
a
r
y
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
V
R
D
E
A
u
t
h
L
i
b
r
a
r
y
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
w
e
b
_
s
e
r
v
i
c
e
_
a
u
t
h
_
l
i
b
r
a
r
y
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
w
e
b
S
e
r
v
i
c
e
A
u
t
h
L
i
b
r
a
r
y
'


 
 
 
 
 
 
 
 
L
i
b
r
a
r
y
 
t
h
a
t
 
p
r
o
v
i
d
e
s
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
 
f
o
r
 
w
e
b
s
e
r
v
i
c
e
 
c
l
i
e
n
t
s
.
 
T
h
e
 
l
i
b
r
a
r
y


 
 
 
 
 
 
 
 
i
s
 
u
s
e
d
 
i
f
 
a
 
v
i
r
t
u
a
l
 
m
a
c
h
i
n
e
'
s
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
 
t
y
p
e
 
i
s
 
s
e
t
 
t
o
 
"
e
x
t
e
r
n
a
l
"


 
 
 
 
 
 
 
 
i
n
 
t
h
e
 
V
M
 
R
e
m
o
t
e
D
i
s
p
l
a
y
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
a
n
d
 
w
i
l
l
 
b
e
 
c
a
l
l
e
d
 
f
r
o
m


 
 
 
 
 
 
 
 
w
i
t
h
i
n
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
W
e
b
s
e
s
s
i
o
n
M
a
n
a
g
e
r
:
:
l
o
g
o
n
"
/
>
 
i
m
p
l
e
m
e
n
t
a
t
i
o
n
.




 
 
 
 
 
 
 
 
A
s
 
o
p
p
o
s
e
d
 
t
o
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
V
R
D
E
A
u
t
h
L
i
b
r
a
r
y
"
/
>
,


 
 
 
 
 
 
 
 
t
h
e
r
e
 
i
s
 
n
o
 
p
e
r
-
V
M
 
s
e
t
t
i
n
g
 
f
o
r
 
t
h
i
s
,
 
a
s
 
t
h
e
 
w
e
b
s
e
r
v
i
c
e
 
i
s
 
a
 
g
l
o
b
a
l


 
 
 
 
 
 
 
 
r
e
s
o
u
r
c
e
 
(
i
f
 
i
t
 
i
s
 
r
u
n
n
i
n
g
)
.
 
O
n
l
y
 
f
o
r
 
t
h
i
s
 
s
e
t
t
i
n
g
 
(
f
o
r
 
t
h
e
 
w
e
b
s
e
r
v
i
c
e
)
,


 
 
 
 
 
 
 
 
s
e
t
t
i
n
g
 
t
h
i
s
 
v
a
l
u
e
 
t
o
 
a
 
l
i
t
e
r
a
l
 
"
n
u
l
l
"
 
s
t
r
i
n
g
 
d
i
s
a
b
l
e
s
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
,


 
 
 
 
 
 
 
 
m
e
a
n
i
n
g
 
t
h
a
t
 
<
l
i
n
k
 
t
o
=
"
I
W
e
b
s
e
s
s
i
o
n
M
a
n
a
g
e
r
:
:
l
o
g
o
n
"
/
>
 
w
i
l
l
 
a
l
w
a
y
s
 
s
u
c
c
e
e
d
,


 
 
 
 
 
 
 
 
n
o
 
m
a
t
t
e
r
 
w
h
a
t
 
u
s
e
r
 
n
a
m
e
 
a
n
d
 
p
a
s
s
w
o
r
d
 
a
r
e
 
s
u
p
p
l
i
e
d
.




 
 
 
 
 
 
 
 
T
h
e
 
i
n
i
t
i
a
l
 
v
a
l
u
e
 
o
f
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
i
s
 
"
V
B
o
x
A
u
t
h
"
,


 
 
 
 
 
 
 
 
m
e
a
n
i
n
g
 
t
h
a
t
 
t
h
e
 
w
e
b
s
e
r
v
i
c
e
 
w
i
l
l
 
u
s
e
 
t
h
e
 
s
a
m
e
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n


 
 
 
 
 
 
 
 
l
i
b
r
a
r
y
 
t
h
a
t
 
i
s
 
u
s
e
d
 
b
y
 
d
e
f
a
u
l
t
 
f
o
r
 
V
R
D
E
 
(
a
g
a
i
n
,
 
s
e
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
S
y
s
t
e
m
P
r
o
p
e
r
t
i
e
s
:
:
V
R
D
E
A
u
t
h
L
i
b
r
a
r
y
"
/
>
)
.


 
 
 
 
 
 
 
 
T
h
e
 
f
o
r
m
a
t
 
a
n
d
 
c
a
l
l
i
n
g
 
c
o
n
v
e
n
t
i
o
n
 
o
f
 
a
u
t
h
e
n
t
i
c
a
t
i
o
n
 
l
i
b
r
a
r
i
e
s


 
 
 
 
 
 
 
 
i
s
 
t
h
e
 
s
a
m
e
 
f
o
r
 
t
h
e
 
w
e
b
s
e
r
v
i
c
e
 
a
s
 
i
t
 
i
s
 
f
o
r
 
V
R
D
E
.




 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
S
e
t
t
i
n
g
 
t
h
i
s
 
p
r
o
p
e
r
t
y
 
t
o
 
@
c
 
n
u
l
l
 
o
r
 
e
m
p
t
y
 
s
t
r
i
n
g
 
w
i
l
l
 
r
e
s
t
o
r
e
 
t
h
e


 
 
 
 
 
 
 
 
 
 
i
n
i
t
i
a
l
 
v
a
l
u
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
w
e
b
S
e
r
v
i
c
e
A
u
t
h
L
i
b
r
a
r
y
'
,
 
s
t
r
)




 
 
 
 
@
w
e
b
_
s
e
r
v
i
c
e
_
a
u
t
h
_
l
i
b
r
a
r
y
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
w
e
b
_
s
e
r
v
i
c
e
_
a
u
t
h
_
l
i
b
r
a
r
y
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
w
e
b
S
e
r
v
i
c
e
A
u
t
h
L
i
b
r
a
r
y
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
v
r
d
e
_
e
x
t
_
p
a
c
k
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
f
a
u
l
t
V
R
D
E
E
x
t
P
a
c
k
'


 
 
 
 
 
 
 
 
T
h
e
 
n
a
m
e
 
o
f
 
t
h
e
 
e
x
t
e
n
s
i
o
n
 
p
a
c
k
 
p
r
o
v
i
d
i
n
g
 
t
h
e
 
d
e
f
a
u
l
t
 
V
R
D
E
.




 
 
 
 
 
 
 
 
T
h
i
s
 
a
t
t
r
i
b
u
t
e
 
i
s
 
f
o
r
 
c
h
o
o
s
i
n
g
 
b
e
t
w
e
e
n
 
m
u
l
t
i
p
l
e
 
e
x
t
e
n
s
i
o
n
 
p
a
c
k
s


 
 
 
 
 
 
 
 
p
r
o
v
i
d
i
n
g
 
V
R
D
E
.
 
I
f
 
o
n
l
y
 
o
n
e
 
i
s
 
i
n
s
t
a
l
l
e
d
,
 
i
t
 
w
i
l
l
 
a
u
t
o
m
a
t
i
c
a
l
l
y
 
b
e
 
t
h
e


 
 
 
 
 
 
 
 
d
e
f
a
u
l
t
 
o
n
e
.
 
T
h
e
 
a
t
t
r
i
b
u
t
e
 
v
a
l
u
e
 
c
a
n
 
b
e
 
e
m
p
t
y
 
i
f
 
n
o
 
V
R
D
E
 
e
x
t
e
n
s
i
o
n


 
 
 
 
 
 
 
 
p
a
c
k
 
i
s
 
i
n
s
t
a
l
l
e
d
.




 
 
 
 
 
 
 
 
F
o
r
 
d
e
t
a
i
l
s
 
a
b
o
u
t
 
V
i
r
t
u
a
l
B
o
x
 
R
e
m
o
t
e
 
D
e
s
k
t
o
p
 
E
x
t
e
n
s
i
o
n
 
a
n
d
 
h
o
w
 
t
o


 
 
 
 
 
 
 
 
i
m
p
l
e
m
e
n
t
 
o
n
e
,
 
p
l
e
a
s
e
 
r
e
f
e
r
 
t
o
 
t
h
e
 
V
i
r
t
u
a
l
B
o
x
 
S
D
K
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
V
R
D
E
E
x
t
P
a
c
k
'
,
 
s
t
r
)




 
 
 
 
@
d
e
f
a
u
l
t
_
v
r
d
e
_
e
x
t
_
p
a
c
k
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
v
r
d
e
_
e
x
t
_
p
a
c
k
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
V
R
D
E
E
x
t
P
a
c
k
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
l
o
g
_
h
i
s
t
o
r
y
_
c
o
u
n
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
l
o
g
H
i
s
t
o
r
y
C
o
u
n
t
'


 
 
 
 
 
 
 
 
T
h
i
s
 
v
a
l
u
e
 
s
p
e
c
i
f
i
e
s
 
h
o
w
 
m
a
n
y
 
o
l
d
 
r
e
l
e
a
s
e
 
l
o
g
 
f
i
l
e
s
 
a
r
e
 
k
e
p
t
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
l
o
g
H
i
s
t
o
r
y
C
o
u
n
t
'
,
 
i
n
t
)




 
 
 
 
@
l
o
g
_
h
i
s
t
o
r
y
_
c
o
u
n
t
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
l
o
g
_
h
i
s
t
o
r
y
_
c
o
u
n
t
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
l
o
g
H
i
s
t
o
r
y
C
o
u
n
t
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
a
u
d
i
o
_
d
r
i
v
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
A
u
d
i
o
D
r
i
v
e
r
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
d
e
f
a
u
l
t
A
u
d
i
o
D
r
i
v
e
r
'


 
 
 
 
 
 
 
 
T
h
i
s
 
v
a
l
u
e
 
h
o
l
d
 
t
h
e
 
d
e
f
a
u
l
t
 
a
u
d
i
o
 
d
r
i
v
e
r
 
f
o
r
 
t
h
e
 
c
u
r
r
e
n
t


 
 
 
 
 
 
s
y
s
t
e
m
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
A
u
d
i
o
D
r
i
v
e
r
'
,
 
A
u
d
i
o
D
r
i
v
e
r
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
u
t
o
s
t
a
r
t
_
d
a
t
a
b
a
s
e
_
p
a
t
h
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
a
u
t
o
s
t
a
r
t
D
a
t
a
b
a
s
e
P
a
t
h
'


 
 
 
 
 
 
 
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
a
u
t
o
s
t
a
r
t
 
d
a
t
a
b
a
s
e
.
 
D
e
p
e
n
d
i
n
g
 
o
n
 
t
h
e
 
h
o
s
t
 
t
h
i
s
 
m
i
g
h
t


 
 
 
 
 
 
 
 
b
e
 
a
 
f
i
l
e
s
y
s
t
e
m
 
p
a
t
h
 
o
r
 
s
o
m
e
t
h
i
n
g
 
e
l
s
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
a
r
t
D
a
t
a
b
a
s
e
P
a
t
h
'
,
 
s
t
r
)




 
 
 
 
@
a
u
t
o
s
t
a
r
t
_
d
a
t
a
b
a
s
e
_
p
a
t
h
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
a
u
t
o
s
t
a
r
t
_
d
a
t
a
b
a
s
e
_
p
a
t
h
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
a
u
t
o
s
t
a
r
t
D
a
t
a
b
a
s
e
P
a
t
h
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
a
d
d
i
t
i
o
n
s
_
i
s
o
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
f
a
u
l
t
A
d
d
i
t
i
o
n
s
I
S
O
'


 
 
 
 
 
 
 
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
d
e
f
a
u
l
t
 
G
u
e
s
t
 
A
d
d
i
t
i
o
n
s
 
I
S
O
 
i
m
a
g
e
.
 
C
a
n
 
b
e
 
e
m
p
t
y
 
i
f


 
 
 
 
 
 
 
 
t
h
e
 
l
o
c
a
t
i
o
n
 
i
s
 
n
o
t
 
k
n
o
w
n
 
i
n
 
t
h
i
s
 
i
n
s
t
a
l
l
a
t
i
o
n
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
A
d
d
i
t
i
o
n
s
I
S
O
'
,
 
s
t
r
)




 
 
 
 
@
d
e
f
a
u
l
t
_
a
d
d
i
t
i
o
n
s
_
i
s
o
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
a
d
d
i
t
i
o
n
s
_
i
s
o
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
A
d
d
i
t
i
o
n
s
I
S
O
'
,
 
v
a
l
u
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
f
r
o
n
t
e
n
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
o
r
 
s
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
'


 
 
 
 
 
 
 
 
S
e
l
e
c
t
s
 
w
h
i
c
h
 
V
M
 
f
r
o
n
t
e
n
d
 
s
h
o
u
l
d
 
b
e
 
u
s
e
d
 
b
y
 
d
e
f
a
u
l
t
 
w
h
e
n
 
l
a
u
n
c
h
i
n
g


 
 
 
 
 
 
 
 
a
 
V
M
 
t
h
r
o
u
g
h
 
t
h
e
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
m
e
t
h
o
d
.


 
 
 
 
 
 
 
 
E
m
p
t
y
 
o
r
 
@
c
 
n
u
l
l
 
s
t
r
i
n
g
s
 
d
o
 
n
o
t
 
d
e
f
i
n
e
 
a
 
p
a
r
t
i
c
u
l
a
r
 
d
e
f
a
u
l
t
,
 
i
t
 
i
s
 
u
p


 
 
 
 
 
 
 
 
t
o
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
t
o
 
s
e
l
e
c
t
 
o
n
e
.
 
S
e
e
 
t
h
e


 
 
 
 
 
 
 
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
 
f
o
r
 
t
h
e
 
v
a
l
i
d


 
 
 
 
 
 
 
 
f
r
o
n
t
e
n
d
 
t
y
p
e
s
.




 
 
 
 
 
 
 
 
T
h
i
s
 
g
l
o
b
a
l
 
s
e
t
t
i
n
g
 
i
s
 
o
v
e
r
r
i
d
d
e
n
 
b
y
 
t
h
e
 
p
e
r
-
V
M
 
a
t
t
r
i
b
u
t
e


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
"
/
>
 
o
r
 
a
 
f
r
o
n
t
e
n
d
 
t
y
p
e


 
 
 
 
 
 
 
 
p
a
s
s
e
d
 
t
o
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
:
:
l
a
u
n
c
h
V
M
P
r
o
c
e
s
s
"
/
>
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
'
,
 
s
t
r
)




 
 
 
 
@
d
e
f
a
u
l
t
_
f
r
o
n
t
e
n
d
.
s
e
t
t
e
r


 
 
 
 
d
e
f
 
d
e
f
a
u
l
t
_
f
r
o
n
t
e
n
d
(
s
e
l
f
,
 
v
a
l
u
e
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
s
e
t
_
a
t
t
r
(
'
d
e
f
a
u
l
t
F
r
o
n
t
e
n
d
'
,
 
v
a
l
u
e
)




 
 
 
 
d
e
f
 
g
e
t
_
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s
(
s
e
l
f
,
 
c
h
i
p
s
e
t
)
:


 
 
 
 
 
 
 
 
"
"
"
M
a
x
i
m
u
m
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
s
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
e
v
e
r
y


 
 
 
 
 
 
 
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>
 
i
n
s
t
a
n
c
e
.




 
 
 
 
 
 
 
 
i
n
 
c
h
i
p
s
e
t
 
o
f
 
t
y
p
e
 
C
h
i
p
s
e
t
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
h
i
p
s
e
t
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
x
i
m
u
m
 
t
o
t
a
l
 
n
u
m
b
e
r
 
o
f
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
s
 
a
l
l
o
w
e
d
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
a
x
N
e
t
w
o
r
k
A
d
a
p
t
e
r
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
h
i
p
s
e
t
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s
_
o
f
_
t
y
p
e
(
s
e
l
f
,
 
c
h
i
p
s
e
t
,
 
t
y
p
e
_
p
)
:


 
 
 
 
 
 
 
 
"
"
"
M
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
s
 
o
f
 
a
 
g
i
v
e
n
 
a
t
t
a
c
h
m
e
n
t
 
t
y
p
e
,


 
 
 
 
 
 
 
 
a
s
s
o
c
i
a
t
e
d
 
w
i
t
h
 
e
v
e
r
y
 
<
l
i
n
k
 
t
o
=
"
I
M
a
c
h
i
n
e
"
/
>
 
i
n
s
t
a
n
c
e
.




 
 
 
 
 
 
 
 
i
n
 
c
h
i
p
s
e
t
 
o
f
 
t
y
p
e
 
C
h
i
p
s
e
t
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
h
i
p
s
e
t
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
i
n
 
t
y
p
e
_
p
 
o
f
 
t
y
p
e
 
N
e
t
w
o
r
k
A
t
t
a
c
h
m
e
n
t
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
y
p
e
 
o
f
 
a
t
t
a
c
h
m
e
n
t
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
s
 
a
l
l
o
w
e
d
 
f
o
r


 
 
 
 
 
 
 
 
 
 
p
a
r
t
i
c
u
l
a
r
 
c
h
i
p
s
e
t
 
a
n
d
 
a
t
t
a
c
h
m
e
n
t
 
t
y
p
e
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
a
x
N
e
t
w
o
r
k
A
d
a
p
t
e
r
s
O
f
T
y
p
e
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
h
i
p
s
e
t
,
 
t
y
p
e
_
p
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
n
e
t
w
o
r
k
_
a
d
a
p
t
e
r
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
a
x
_
d
e
v
i
c
e
s
_
p
e
r
_
p
o
r
t
_
f
o
r
_
s
t
o
r
a
g
e
_
b
u
s
(
s
e
l
f
,
 
b
u
s
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
d
e
v
i
c
e
s
 
w
h
i
c
h
 
c
a
n
 
b
e
 
a
t
t
a
c
h
e
d
 
t
o
 
a
 
p
o
r
t


 
 
 
 
 
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
b
u
s
.




 
 
 
 
 
 
 
 
i
n
 
b
u
s
 
o
f
 
t
y
p
e
 
S
t
o
r
a
g
e
B
u
s


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
o
r
a
g
e
 
b
u
s
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
d
e
v
i
c
e
s
_
p
e
r
_
p
o
r
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
d
e
v
i
c
e
s
 
w
h
i
c
h
 
c
a
n
 
b
e
 
a
t
t
a
c
h
e
d
 
t
o
 
t
h
e
 
p
o
r
t
 
f
o
r
 
t
h
e
 
g
i
v
e
n


 
 
 
 
 
 
 
 
s
t
o
r
a
g
e
 
b
u
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
x
_
d
e
v
i
c
e
s
_
p
e
r
_
p
o
r
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
a
x
D
e
v
i
c
e
s
P
e
r
P
o
r
t
F
o
r
S
t
o
r
a
g
e
B
u
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
b
u
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
d
e
v
i
c
e
s
_
p
e
r
_
p
o
r
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
i
n
_
p
o
r
t
_
c
o
u
n
t
_
f
o
r
_
s
t
o
r
a
g
e
_
b
u
s
(
s
e
l
f
,
 
b
u
s
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
m
i
n
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
p
o
r
t
s
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
b
u
s
 
s
u
p
p
o
r
t
s
.




 
 
 
 
 
 
 
 
i
n
 
b
u
s
 
o
f
 
t
y
p
e
 
S
t
o
r
a
g
e
B
u
s


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
o
r
a
g
e
 
b
u
s
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
i
n
_
p
o
r
t
_
c
o
u
n
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
i
n
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
p
o
r
t
s
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
b
u
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
i
n
_
p
o
r
t
_
c
o
u
n
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
i
n
P
o
r
t
C
o
u
n
t
F
o
r
S
t
o
r
a
g
e
B
u
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
b
u
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
i
n
_
p
o
r
t
_
c
o
u
n
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
a
x
_
p
o
r
t
_
c
o
u
n
t
_
f
o
r
_
s
t
o
r
a
g
e
_
b
u
s
(
s
e
l
f
,
 
b
u
s
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
p
o
r
t
s
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
b
u
s
 
s
u
p
p
o
r
t
s
.




 
 
 
 
 
 
 
 
i
n
 
b
u
s
 
o
f
 
t
y
p
e
 
S
t
o
r
a
g
e
B
u
s


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
o
r
a
g
e
 
b
u
s
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
p
o
r
t
_
c
o
u
n
t
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
p
o
r
t
s
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
b
u
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
x
_
p
o
r
t
_
c
o
u
n
t
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
a
x
P
o
r
t
C
o
u
n
t
F
o
r
S
t
o
r
a
g
e
B
u
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
b
u
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
p
o
r
t
_
c
o
u
n
t


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
m
a
x
_
i
n
s
t
a
n
c
e
s
_
o
f
_
s
t
o
r
a
g
e
_
b
u
s
(
s
e
l
f
,
 
c
h
i
p
s
e
t
,
 
b
u
s
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
s
t
o
r
a
g
e
 
b
u
s
 
i
n
s
t
a
n
c
e
s
 
w
h
i
c
h


 
 
 
 
 
 
 
 
c
a
n
 
b
e
 
c
o
n
f
i
g
u
r
e
d
 
f
o
r
 
e
a
c
h
 
V
M
.
 
T
h
i
s
 
c
o
r
r
e
s
p
o
n
d
s
 
t
o
 
t
h
e
 
n
u
m
b
e
r
 
o
f


 
 
 
 
 
 
 
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
s
 
o
n
e
 
c
a
n
 
h
a
v
e
.
 
V
a
l
u
e
 
m
a
y
 
d
e
p
e
n
d
 
o
n
 
c
h
i
p
s
e
t
 
t
y
p
e


 
 
 
 
 
 
 
 
u
s
e
d
.




 
 
 
 
 
 
 
 
i
n
 
c
h
i
p
s
e
t
 
o
f
 
t
y
p
e
 
C
h
i
p
s
e
t
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
c
h
i
p
s
e
t
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
i
n
 
b
u
s
 
o
f
 
t
y
p
e
 
S
t
o
r
a
g
e
B
u
s


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
o
r
a
g
e
 
b
u
s
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
i
n
s
t
a
n
c
e
s
 
o
f
 
t
y
p
e
 
i
n
t


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
m
a
x
i
m
u
m
 
n
u
m
b
e
r
 
o
f
 
i
n
s
t
a
n
c
e
s
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
b
u
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
m
a
x
_
i
n
s
t
a
n
c
e
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
M
a
x
I
n
s
t
a
n
c
e
s
O
f
S
t
o
r
a
g
e
B
u
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
h
i
p
s
e
t
,
 
b
u
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
i
n
t
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
x
_
i
n
s
t
a
n
c
e
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
d
e
v
i
c
e
_
t
y
p
e
s
_
f
o
r
_
s
t
o
r
a
g
e
_
b
u
s
(
s
e
l
f
,
 
b
u
s
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
l
i
s
t
 
o
f
 
a
l
l
 
t
h
e
 
s
u
p
p
o
r
t
e
d
 
d
e
v
i
c
e
 
t
y
p
e
s


 
 
 
 
 
 
 
 
(
<
l
i
n
k
 
t
o
=
"
D
e
v
i
c
e
T
y
p
e
"
/
>
)
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
t
y
p
e
 
o
f
 
s
t
o
r
a
g
e


 
 
 
 
 
 
 
 
b
u
s
.




 
 
 
 
 
 
 
 
i
n
 
b
u
s
 
o
f
 
t
y
p
e
 
S
t
o
r
a
g
e
B
u
s


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
o
r
a
g
e
 
b
u
s
 
t
y
p
e
 
t
o
 
g
e
t
 
t
h
e
 
v
a
l
u
e
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
_
t
y
p
e
s
 
o
f
 
t
y
p
e
 
D
e
v
i
c
e
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
l
i
s
t
 
o
f
 
a
l
l
 
s
u
p
p
o
r
t
e
d
 
d
e
v
i
c
e
 
t
y
p
e
s
 
f
o
r
 
t
h
e
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
b
u
s
.




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
d
e
v
i
c
e
_
t
y
p
e
s
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
D
e
v
i
c
e
T
y
p
e
s
F
o
r
S
t
o
r
a
g
e
B
u
s
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
b
u
s
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
D
e
v
i
c
e
T
y
p
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
e
v
i
c
e
_
t
y
p
e
s


 
 
 
 
 
 
 
 


 
 
 
 
d
e
f
 
g
e
t
_
d
e
f
a
u
l
t
_
i
o
_
c
a
c
h
e
_
s
e
t
t
i
n
g
_
f
o
r
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
,
 
c
o
n
t
r
o
l
l
e
r
_
t
y
p
e
)
:


 
 
 
 
 
 
 
 
"
"
"
R
e
t
u
r
n
s
 
t
h
e
 
d
e
f
a
u
l
t
 
I
/
O
 
c
a
c
h
e
 
s
e
t
t
i
n
g
 
f
o
r
 
t
h
e


 
 
 
 
 
 
 
 
g
i
v
e
n
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r




 
 
 
 
 
 
 
 
i
n
 
c
o
n
t
r
o
l
l
e
r
_
t
y
p
e
 
o
f
 
t
y
p
e
 
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
T
y
p
e


 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
o
 
t
h
e
 
s
e
t
t
i
n
g
 
f
o
r
.




 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
n
a
b
l
e
d
 
o
f
 
t
y
p
e
 
b
o
o
l


 
 
 
 
 
 
 
 
 
 
 
 
R
e
t
u
r
n
e
d
 
f
l
a
g
 
i
n
d
i
c
a
t
i
n
g
 
t
h
e
 
d
e
f
a
u
l
t
 
v
a
l
u
e




 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
e
n
a
b
l
e
d
 
=
 
s
e
l
f
.
c
a
l
l
_
m
e
t
h
o
d
(
'
g
e
t
D
e
f
a
u
l
t
I
o
C
a
c
h
e
S
e
t
t
i
n
g
F
o
r
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
_
p
=
[
c
o
n
t
r
o
l
l
e
r
_
t
y
p
e
]
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
t
y
p
e
=
b
o
o
l
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
n
a
b
l
e
d


 
 
 
 
 
 
 
 




c
l
a
s
s
 
I
G
u
e
s
t
O
S
T
y
p
e
(
I
n
t
e
r
f
a
c
e
)
:


 
 
 
 
"
"
"
"
"
"


 
 
 
 
u
u
i
d
 
=
 
'
6
d
9
6
8
f
9
a
-
8
5
8
b
-
4
c
5
0
-
b
f
1
7
-
2
4
1
f
0
6
9
e
9
4
c
2
'


 
 
 
 
w
s
m
a
p
 
=
 
'
s
t
r
u
c
t
'


 
 
 
 


 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
a
m
i
l
y
_
i
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
f
a
m
i
l
y
I
d
'


 
 
 
 
 
 
 
 
G
u
e
s
t
 
O
S
 
f
a
m
i
l
y
 
i
d
e
n
t
i
f
i
e
r
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
a
m
i
l
y
I
d
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
f
a
m
i
l
y
_
d
e
s
c
r
i
p
t
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
f
a
m
i
l
y
D
e
s
c
r
i
p
t
i
o
n
'


 
 
 
 
 
 
 
 
H
u
m
a
n
 
r
e
a
d
a
b
l
e
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
h
e
 
g
u
e
s
t
 
O
S
 
f
a
m
i
l
y
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
f
a
m
i
l
y
D
e
s
c
r
i
p
t
i
o
n
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
d
_
p
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
i
d
'


 
 
 
 
 
 
 
 
G
u
e
s
t
 
O
S
 
i
d
e
n
t
i
f
i
e
r
 
s
t
r
i
n
g
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
d
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
d
e
s
c
r
i
p
t
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
s
t
r
 
v
a
l
u
e
 
f
o
r
 
'
d
e
s
c
r
i
p
t
i
o
n
'


 
 
 
 
 
 
 
 
H
u
m
a
n
 
r
e
a
d
a
b
l
e
 
d
e
s
c
r
i
p
t
i
o
n
 
o
f
 
t
h
e
 
g
u
e
s
t
 
O
S
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
d
e
s
c
r
i
p
t
i
o
n
'
,
 
s
t
r
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
i
s
6
4
_
b
i
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
i
s
6
4
B
i
t
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
t
h
e
 
g
i
v
e
n
 
O
S
 
i
s
 
6
4
-
b
i
t


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
i
s
6
4
B
i
t
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
i
o
a
p
i
c
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
I
O
A
P
I
C
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
I
O
 
A
P
I
C
 
r
e
c
o
m
m
e
n
d
e
d
 
f
o
r
 
t
h
i
s
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
I
O
A
P
I
C
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
v
i
r
t
_
e
x
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
V
i
r
t
E
x
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
V
T
-
x
 
o
r
 
A
M
D
-
V
 
r
e
c
o
m
m
e
n
d
e
d
 
f
o
r
 
t
h
i
s
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
V
i
r
t
E
x
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
r
a
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
R
A
M
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
R
A
M
 
s
i
z
e
 
i
n
 
M
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
R
A
M
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
v
r
a
m
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
V
R
A
M
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
v
i
d
e
o
 
R
A
M
 
s
i
z
e
 
i
n
 
M
e
g
a
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
V
R
A
M
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
2
_
d
_
v
i
d
e
o
_
a
c
c
e
l
e
r
a
t
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
2
D
V
i
d
e
o
A
c
c
e
l
e
r
a
t
i
o
n
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
2
D
 
v
i
d
e
o
 
a
c
c
e
l
e
r
a
t
i
o
n
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
 
f
o
r
 
t
h
i
s
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
2
D
V
i
d
e
o
A
c
c
e
l
e
r
a
t
i
o
n
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
3
_
d
_
a
c
c
e
l
e
r
a
t
i
o
n
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
3
D
A
c
c
e
l
e
r
a
t
i
o
n
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
3
D
 
a
c
c
e
l
e
r
a
t
i
o
n
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
 
f
o
r
 
t
h
i
s
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
3
D
A
c
c
e
l
e
r
a
t
i
o
n
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
h
d
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
i
n
t
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
H
D
D
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
h
a
r
d
 
d
i
s
k
 
s
i
z
e
 
i
n
 
b
y
t
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
H
D
D
'
,
 
i
n
t
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
a
d
a
p
t
e
r
_
t
y
p
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
N
e
t
w
o
r
k
A
d
a
p
t
e
r
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
a
d
a
p
t
e
r
T
y
p
e
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
r
e
c
o
m
m
e
n
d
e
d
 
n
e
t
w
o
r
k
 
a
d
a
p
t
e
r
 
f
o
r
 
t
h
i
s
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
a
d
a
p
t
e
r
T
y
p
e
'
,
 
N
e
t
w
o
r
k
A
d
a
p
t
e
r
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
p
a
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
P
A
E
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
u
s
i
n
g
 
P
A
E
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
 
f
o
r
 
t
h
i
s
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
P
A
E
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
d
v
d
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
D
V
D
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
y
p
e
 
f
o
r
 
D
V
D
/
C
D
 
d
r
i
v
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
D
V
D
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
'
,
 
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
d
v
d
_
s
t
o
r
a
g
e
_
b
u
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
S
t
o
r
a
g
e
B
u
s
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
D
V
D
S
t
o
r
a
g
e
B
u
s
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
s
t
o
r
a
g
e
 
b
u
s
 
t
y
p
e
 
f
o
r
 
D
V
D
/
C
D
 
d
r
i
v
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
D
V
D
S
t
o
r
a
g
e
B
u
s
'
,
 
S
t
o
r
a
g
e
B
u
s
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
h
d
_
s
t
o
r
a
g
e
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
H
D
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
s
t
o
r
a
g
e
 
c
o
n
t
r
o
l
l
e
r
 
t
y
p
e
 
f
o
r
 
H
D
 
d
r
i
v
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
H
D
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
'
,
 
S
t
o
r
a
g
e
C
o
n
t
r
o
l
l
e
r
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
h
d
_
s
t
o
r
a
g
e
_
b
u
s
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
S
t
o
r
a
g
e
B
u
s
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
H
D
S
t
o
r
a
g
e
B
u
s
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
s
t
o
r
a
g
e
 
b
u
s
 
t
y
p
e
 
f
o
r
 
H
D
 
d
r
i
v
e
s
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
H
D
S
t
o
r
a
g
e
B
u
s
'
,
 
S
t
o
r
a
g
e
B
u
s
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
f
i
r
m
w
a
r
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
F
i
r
m
w
a
r
e
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
F
i
r
m
w
a
r
e
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
f
i
r
m
w
a
r
e
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
F
i
r
m
w
a
r
e
'
,
 
F
i
r
m
w
a
r
e
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
u
s
b
h
i
d
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
U
S
B
H
I
D
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
u
s
i
n
g
 
U
S
B
 
H
u
m
a
n
 
I
n
t
e
r
f
a
c
e
 
D
e
v
i
c
e
s
,
 
s
u
c
h
 
a
s
 
k
e
y
b
o
a
r
d
 
a
n
d
 
m
o
u
s
e
 
r
e
c
o
m
m
e
n
d
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
U
S
B
H
I
D
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
h
p
e
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
H
P
E
T
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
u
s
i
n
g
 
H
P
E
T
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
 
f
o
r
 
t
h
i
s
 
O
S
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
H
P
E
T
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
u
s
b
_
t
a
b
l
e
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
U
S
B
T
a
b
l
e
t
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
u
s
i
n
g
 
a
 
U
S
B
 
T
a
b
l
e
t
 
i
s
 
r
e
c
o
m
m
e
n
d
e
d
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
U
S
B
T
a
b
l
e
t
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
r
t
c
_
u
s
e
_
u
t
c
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
b
o
o
l
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
R
T
C
U
s
e
U
T
C
'


 
 
 
 
 
 
 
 
R
e
t
u
r
n
s
 
@
c
 
t
r
u
e
 
i
f
 
t
h
e
 
R
T
C
 
o
f
 
t
h
i
s
 
V
M
 
s
h
o
u
l
d
 
b
e
 
s
e
t
 
t
o
 
U
T
C


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
R
T
C
U
s
e
U
T
C
'
,
 
b
o
o
l
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
c
h
i
p
s
e
t
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
C
h
i
p
s
e
t
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n
d
e
d
C
h
i
p
s
e
t
'


 
 
 
 
 
 
 
 
R
e
c
o
m
m
e
n
d
e
d
 
c
h
i
p
s
e
t
 
t
y
p
e
.


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
e
l
f
.
g
e
t
_
a
t
t
r
(
'
r
e
c
o
m
m
e
n
d
e
d
C
h
i
p
s
e
t
'
,
 
C
h
i
p
s
e
t
T
y
p
e
)




 
 
 
 
@
p
r
o
p
e
r
t
y


 
 
 
 
d
e
f
 
r
e
c
o
m
m
e
n
d
e
d
_
a
u
d
i
o
_
c
o
n
t
r
o
l
l
e
r
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
G
e
t
 
A
u
d
i
o
C
o
n
t
r
o
l
l
e
r
T
y
p
e
 
v
a
l
u
e
 
f
o
r
 
'
r
e
c
o
m
m
e
n