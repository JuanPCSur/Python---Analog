#!/usr/bin/env python
#-*- coding: utf-8 -*-

from datetime import datetime
		
		
def proc_ja():
	f= open ('auth.log', 'r')
	
	li = []
	for linea in f.readlines():
		if "authentication failure" in linea:
			cats = linea[:15]
			ano = datetime.now()
			cats = str(ano.year)+ ' ' + cats
			ts = datetime.strptime(cats, '%Y %b %d %H:%M:%S')
			ip = linea[129:143]
			li.append([ip,ts])
							
	f.close()
	
	print ('Hay ' + str(len(li)) +' intentos fallidos')
	li.sort(key=lambda fec: fec[1], reverse=True)	
	cu=0
	ip_A = ''	
	while cu < len(li):
		if ip_A <> li[cu][0]:
			print ('   La IP : ' + li[cu][0] + ' intento acceder sin exito : ')

		print (datetime.strftime(li[cu][1], 'El %d-%m-%Y a las %H:%M:%S'))
		ip_A = li[cu][0]
		cu+=1
	
proc_ja()


