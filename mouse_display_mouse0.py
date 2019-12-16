#!/usr/bin/python

import time
from threading import Thread, Lock

try:

	# Dictionaries/structures containing data for each 'SENSOR'
	mouse1 = {
		'Name': '1',
		'File': file('/dev/input/mouse0'),
		'dx': 0,
		'dy': 0}
	
	# Declare variables
	transmit_timer = None
	data_lock = Lock()
	serial_lock = Lock()

	transmit_delay = .01 #.01
	read_delay = .001 #0.01
	print('mouse_relay.py: \n\tMain thread initialized\n\tDefining I/O threads\n')


	# SENDOUTPUTTHREAD - class for sending data over serial port, subclass of Thread class
	class SendOutputThread(Thread):
		# Call parent (Thread) constructor with additional argument: SENSOR
		def __init__(self, sensor):
		        Thread.__init__(self)	        
		        self.sensor = sensor
		# Running code goes in 'run' method, called by obj.start() method
		def run(self):
			while True:
				# Convert and Reset dx/dy data
				data_lock.acquire()
				s = self.sensor['Name']
				dx = self.sensor['dx']
				self.sensor['dx'] = 0
				dy = self.sensor['dy']
				self.sensor['dy'] = 0
				data_lock.release()			
				serial_lock.acquire()
				serial_lock.release()
			
				# Delay for transmission period (100 msec)
				time.sleep(transmit_delay)		

	# READINPUTTHREAD - class to read raw input from linux /dev/mouseX files
	class ReadInputThread(Thread):
		# Call parent (Thread) constructor with additional argument: SENSOR
		def __init__(self, sensor):
		        Thread.__init__(self)	        
		        self.sensor = sensor
		# Running code goes in 'run' method, called by obj.start() method
		def run(self):
			while True:
				newdx = newdy = 0
				# Read raw values from mouse device file in linux filesystem
				dev_file = self.sensor['File']
				status, newdx, newdy = tuple(ord(c) for c in dev_file.read(3))
				# Define conversion to signed integer
				def to_signed(n):
					return n - ((0x80 & n) << 1)
				# Add accumulated readings
				if status:
					data_lock.acquire()
					self.sensor['dx'] += to_signed(newdx)
					self.sensor['dy'] += to_signed(newdy)
					data_lock.release()
				time.sleep(read_delay)
				print('dx' + str(self.sensor['dx']))
				print('dy' + str(self.sensor['dy']))
	print('\tI/O threads defined\n\t...initializing now\n')
			
	# Begin a transmitting thread for each mouse: SEND_OUTPUT
	serial_out_thread1 = SendOutputThread(mouse1)
#	serial_out_thread2 = SendOutputThread(mouse2)
	serial_out_thread1.setName('thread_out_mouse1')
#	serial_out_thread2.setName('thread_out_mouse2')
			
	# Begin the sensing thread for each mouse: READ_INPUT
	devread_in_thread1 = ReadInputThread(mouse1)
#	devread_in_thread2 = ReadInputThread(mouse2)
	devread_in_thread1.setName('thread_in_mouse1')
#	devread_in_thread2.setName('thread_in_mouse2')
	print('\tThreads initialized... starting all threads now\n')

	# Start all threads
	serial_out_thread1.start()
#	serial_out_thread2.start()
	devread_in_thread1.start()
#	devread_in_thread2.start()
			
	# Join all threads to prevent program exit
	serial_out_thread1.join()
#	serial_out_thread2.join()
	devread_in_thread1.join()
#	devread_in_thread2.join()

except KeyboardInterrupt:
        print(e) 

else:
	sr.close()
	print('\n\nShutting down safely...')
