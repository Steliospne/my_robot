#!/usr/bin/env python3

import rospy
import RPi.GPIO as GPIO
import time
import math
from my_robot_driver.msg import Buttons, Odom_data
from my_robot_encoder.encoder import *
from my_robot_odom.odometry import *



def callback_button_command(data):
    if data.reset == 1:
        odo.resetPose()
        right_wheel_enc.reset()
        left_wheel_enc.reset()

def compute_callback(event=None):
    msg = Odom_data()
    msg.counter_r = right_wheel_enc.counter
    msg.counter_l = left_wheel_enc.counter
    msg.x = odo.x
    msg.y = odo.y
    msg.theta = odo.theta
    data_pub.publish(msg)

def wait_for_button_press():
    rospy.Subscriber("/button_command", Buttons, callback_button_command)
    rospy.spin()


if __name__ == "__main__":
    rospy.init_node("compute_controler")
    wheel_radius = 0.0325
    rw = 0.12293
    x = 0
    y = 0
    theta = 0
    right_wheel_enc = encoder(17, 20, wheel_radius)
    left_wheel_enc = encoder(27, 20, wheel_radius)
    odo = odometry(left_wheel_enc, right_wheel_enc, rw)
    data_pub = rospy.Publisher('/compute_data', Odom_data, queue_size=10)
    publish_encoder_data_freq = rospy.get_param("~publish_encoder_data_freq", 10.0)
    rospy.Timer(rospy.Duration(1.0/publish_encoder_data_freq), compute_callback)

    
    try:
        start_time = time.time_ns()
        while not rospy.is_shutdown():
            msg = Odom_data()
            
    
            t = time.time_ns()
            dt = t - start_time
            start_time = t
    
            odo.step()
    
            x, y ,theta = odo.getPose()

            theta_d = (theta - (2 * math.pi * math.floor((theta + math.pi)/(2*math.pi))))
            theta_d = theta * 180/math.pi
    
            #print('L/R:', left_wheel_enc.counter, right_wheel_enc.counter,
            #'x:', x, 'y:', y, 'theta:', theta_d)
    
    
    except rospy.ROSInterruptException:
        pass
