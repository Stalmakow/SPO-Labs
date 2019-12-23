#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

 
import math


side  = {
    'left': 0,
    'front': 0,
    }

def calc_range(msg):
    global side
    side = {
        'left':  min(min(msg.ranges[0:143]), 0.9),
        'front':  min(min(msg.ranges[288:431]), 0.9),
    
    }
    
    

def state():
     global side
     dist=0.75
     if side['left'] <= dist  :
          return 0
     elif side['left'] > dist and side['front'] <= dist :
          return 1
     elif side['left'] > dist and side['front'] > dist :
          return 2

if __name__ == '__main__':
    global vel_msg

    rospy.init_node('base_node')

    vel_msg = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    sub = rospy.Subscriber('/base_scan', LaserScan, calc_range)

    rate = rospy.Rate(20)

    while not rospy.is_shutdown():

       msg = Twist()
       

       
       if state() == 0:
            msg.linear.x = 0
            msg.angular.z = 1.5
           
       elif state() == 1:
            msg.angular.z = -1.5
            msg.linear.x = 0.3
           
       elif state() == 2:
            msg.linear.x = 1
            msg.angular.z = -0.1
            pass

       vel_msg.publish(msg)

       rate.sleep()