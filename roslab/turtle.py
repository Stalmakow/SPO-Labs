#!/usr/bin/env python
import rospy
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist
import math
import time
import sys

rospy.init_node('robot_cleaner', anonymous=True)

def rotate(x,name=str):
    # Starts a new node
#    rospy.init_node('robot_cleaner', anonymous=True)
    name='/'+name+'/cmd_vel'
    velocity_publisher = rospy.Publisher(name, Twist, queue_size=10)

    rate = rospy.Rate(50)
    vel_msg = Twist()
    time.sleep(1)
    vel_msg.angular.z = x*math.pi/180

    t0=time.time()
    dt=0
    velocity_publisher.publish(vel_msg)
    while(dt <= 1):

            t1=time.time()
            dt=(t1-t0)
            rate.sleep()

    vel_msg.angular.z=0
    velocity_publisher.publish(vel_msg)
def circle(x,y,name =str):
   
#    rospy.init_node('robot_cleaner', anonymous=True)
    name='/'+name+'/cmd_vel'
    velocity_publisher = rospy.Publisher(name, Twist, queue_size=10)
    rate = rospy.Rate(50)
    vel_msg = Twist()
    time.sleep(1)
    vel_msg.angular.z = y*x*math.pi
    vel_msg.linear.x = x*math.pi/(1.5) 

    t0=time.time()
    dt=0
    velocity_publisher.publish(vel_msg)
    while(dt <= 1):
            t1=time.time()
            dt=(t1-t0)
            rate.sleep()

    t0=time.time()
    dt=0
    vel_msg.linear.x = 0
    vel_msg.angular.z=0
    velocity_publisher.publish(vel_msg)

def move(x,name=str):
    # Starts a new node
 #   rospy.init_node('robot_cleaner', anonymous=True)
    name='/'+name+'/cmd_vel'
    velocity_publisher = rospy.Publisher(name, Twist, queue_size=10)
    rate = rospy.Rate(50)
    vel_msg = Twist()
    time.sleep(1)    

    vel_msg.linear.x = x
    velocity_publisher.publish(vel_msg)
    dt = 0
    t0 = time.time()
    while(dt <= 1): 
           
            t1=time.time()
            dt=(t1-t0)
            rate.sleep()
 
    vel_msg.linear.x = 0
    vel_msg.angular.z=0
    velocity_publisher.publish(vel_msg)
def dva(number):
      name= 't' + str(number)
      rotate(90,name)
      circle(1,-1,name)
      rotate(-30,name)
      move(2,name)
      rotate(120,name)
      move(1.44,name)
def tri(number):
      name= 't' + str(number)
      circle(1,-1,name)
      rotate(180,name) 
      circle(1,-1,name)
def chetire(number):
      name= 't' + str(number)
      rotate(90,name)
      move(2.5,name)
      rotate(180,name)
      move(1.25,name)
      rotate(-90,name)
      move(1.25,name)
      rotate(-90,name)
      move(1.25,name)

def pyat(number):
      name= 't' + str(number)
      rotate(180,name)
      move(1,name)
      rotate(90,name)
      move(1,name)
      rotate(90,name)
      circle(1,-1,name)

def odin():
      name= rospy.ServiceProxy('/spawn',1,1,0)
      move(2,name)
      rotate(180,name)
      move(1,name)
      rotate(-90,name)
      move(4,name)
      rotate(135,name)
      move(1,name)
def deviat(number):
      #tmp = "x: 0.0 y: 0.0  theta: 0.0 name: 't'"
      name = 't' + str(number)
      rotate(60,name)
      move(2,name)
      rotate(30,name)
      circle(2,1,name)
      #rospy.ServiceProxy('/kill "name: 't1'"')

def spawn():
     spawn_turtle = rospy.ServiceProxy('spawn_turtle', Spawn)
     spawn_turtle(5,5,1,"turt")
     rospy.spin()

if __name__ == '__main__':
    try:
       
        dva(1)
	chetire(2)
	tri(3)
	deviat(4)
	dva(5)
	pyat(6)
        
       
    except rospy.ROSInterruptException: pas
