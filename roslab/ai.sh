rosservice call /kill "name: 't1'"
rosservice call /kill "name: 't2'"
rosservice call /kill "name: 't3'"
rosservice call /kill "name: 't4'"
rosservice call /kill "name: 't5'"
rosservice call /kill "name: 't6'"
rosservice call /clear

rosservice call /spawn "x: 0.5
y: 4.0
theta: 0.0
name: 't1'"

rosservice call /spawn "x: 3.8
y: 2.5
theta: 0.0
name: 't2'"

rosservice call /spawn "x: 4.3
y: 5.0
theta: 0.0
name: 't3'"

rosservice call /spawn "x: 5.5
y: 2.5
theta: 0.0
name: 't4'"

rosservice call /spawn "x: 7
y: 4.0
theta: 0.0
name: 't5'"

rosservice call /spawn "x: 9.5
y: 5.0
theta: 0.0
name: 't6'"

./turtle.py

rosservice call /kill "name: 't1'"
rosservice call /kill "name: 't2'"
rosservice call /kill "name: 't3'"
rosservice call /kill "name: 't4'"
rosservice call /kill "name: 't5'"
rosservice call /kill "name: 't6'"
