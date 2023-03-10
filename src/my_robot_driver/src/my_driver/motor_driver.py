#!/usr/bin/env python3

import RPi.GPIO as GPIO

class MotorDriver:

	def __init__(self, max_speed = 75):
		#Pin setup
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM) 

		#Pin assignment
		self.forward_right=22 #IN4
		self.backward_right=23 #IN3
		self.forward_left=20 #IN2
		self.backward_left=26 #IN1

		#Motor setup.
		GPIO.setup(self.forward_right, GPIO.OUT)
		GPIO.setup(self.backward_right, GPIO.OUT)
		GPIO.setup(self.forward_left, GPIO.OUT)
		GPIO.setup(self.backward_left, GPIO.OUT)

		#PWM frequency and assignment.
		self.pwm_freq = 100

		self.pwm_fr = GPIO.PWM(self.forward_right,self.pwm_freq)
		self.pwm_br = GPIO.PWM(self.backward_right, self.pwm_freq)
		self.pwm_fl = GPIO.PWM(self.forward_left, self.pwm_freq)
		self.pwm_bl = GPIO.PWM(self.backward_left, self.pwm_freq)
		
		#Initialization of software pwm.
		self.pwm_fr.start(0)
		self.pwm_br.start(0)
		self.pwm_fl.start(0)
		self.pwm_bl.start(0)

		#Motor var
		self.max_speed = max_speed
		self.current_speed_r = 0
		self.current_speed_l = 0

		self.state = 'fw'
		


	def move_command(self, speed_x, speed_z, mode=1):
		if mode == 1:	
			#if speed_x >= self.max_speed or speed_z >= self.max_speed:
			#	speed_x = self.max_speed
			#	speed_z = self.max_speed

			if -9 < speed_x < 9:
				speed_x = 0

			if -9 < speed_z < 9:
				speed_z = 0

			if speed_z == 0:
				self.current_speed_r = speed_x
				self.current_speed_l = speed_x

				if speed_x > 0:
					self.pwm_fr.ChangeDutyCycle(self.current_speed_r)
					self.pwm_fl.ChangeDutyCycle(self.current_speed_l)
					self.pwm_br.ChangeDutyCycle(0)
					self.pwm_bl.ChangeDutyCycle(0)
					self.state = 'fw'
				else:
					self.pwm_fr.ChangeDutyCycle(0)
					self.pwm_fl.ChangeDutyCycle(0)
					self.pwm_br.ChangeDutyCycle(abs(self.current_speed_r))
					self.pwm_bl.ChangeDutyCycle(abs(self.current_speed_l))
					self.state = 'bw'

			elif speed_x == 0:
				if speed_z > 0:
					self.current_speed_r = self.current_speed_l = speed_z
					self.pwm_fr.ChangeDutyCycle(self.current_speed_r)
					self.pwm_bl.ChangeDutyCycle(self.current_speed_l)
					self.state = 'l'
				else:
					self.current_speed_r = self.current_speed_l = speed_z
					self.pwm_br.ChangeDutyCycle(abs(self.current_speed_r))
					self.pwm_fl.ChangeDutyCycle(abs(self.current_speed_l))
					self.state = 'r'

			else:
				if speed_z > 0:
					self.current_speed_r = speed_x
					self.current_speed_l = speed_x - speed_z
					self.pwm_fr.ChangeDutyCycle(abs(self.current_speed_r))
					self.pwm_fl.ChangeDutyCycle(abs(self.current_speed_l))
				else:
					self.current_speed_r = speed_x - abs(speed_z)
					self.current_speed_l = speed_x
					self.pwm_fr.ChangeDutyCycle(abs(self.current_speed_r))
					self.pwm_fl.ChangeDutyCycle(abs(self.current_speed_l))
		else:
			self.state = 'fw'
			self.current_speed_r = speed_x
			self.current_speed_l = speed_z
			self.pwm_fr.ChangeDutyCycle(self.current_speed_r)
			self.pwm_fl.ChangeDutyCycle(self.current_speed_l)

	def get_current_speed(self):
		return self.current_speed_r, self.current_speed_l

	def get_state(self):
		return self.state
		
	def stop(self):
		self.pwm_fr.ChangeDutyCycle(0)
		self.pwm_fl.ChangeDutyCycle(0)
		self.pwm_br.ChangeDutyCycle(0)
		self.pwm_bl.ChangeDutyCycle(0)