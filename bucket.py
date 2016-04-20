from subprocess import call as s_call

import sys

ch=int()

while(ch!=5):
	print "menu"
	print "1.create bucket"
	print "2.view bucket"
	print "3.remove bucket"
	print "4.view bucket content"
	print "5.exit"
	
	while(1):
		try:
			ch=int(raw_input("enter choice\n"))
			break
		except ValueError:
			pass	
	if ch==1:
		bucket=raw_input("enter bucket name:")
		cmd="aws s3 mb s3://%s"%bucket
		s_call(cmd.split())
	elif ch==2:
		cmd="aws s3 ls"
		s_call(cmd.split())
	elif ch==3:
		bucket=raw_input("enter bucket name:")
		cmd="aws s3 rb s3://%s"%bucket
		s_call(cmd.split())
	elif ch==4:
		bucket=raw_input("enetr bucket name:")
		cmd="aws s3 ls S://%s"%bucket
		s_call(cmd.split())
	elif ch==5:
		sys.exit()
		
