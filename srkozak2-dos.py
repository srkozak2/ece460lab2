#!/usr/bin/python

import socket

TCP_IP = '192.168.100.196'
TCP_PORT = 31337
MESSAGE = "srkozak2"

for i in range(1,10000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)