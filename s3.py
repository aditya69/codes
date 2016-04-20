from subprocess import call as s_call
import sys
ch=int()
while(ch!=8):
	print "\n Menu"
	print "1.Create Bucket"
	print "2.Delete Bucket"
	print "3.Upload File"
	print "4.Download File"
	print "5.Delete File"
	print "6.Show Bucket"
	print "7.Show Bucket Contents"
	print "8.Exit"
	ch=int(raw_input("Enter your Choice : \n"))
	if ch==1:
		b=raw_input("Enter Bucket Name : \n")
		r=raw_input("Enter Region Name : \n")
		cmd="aws s3api create-bucket --bucket %s --region %s"%(b,r)
		print "commamd : ",cmd
		s_call(cmd.split())
	elif ch==2:
		b=raw_input("Enter Bucket Name : \n")
		r=raw_input("Enter Region Name : \n")
		cmd="aws s3api delete-bucket --bucket %s --region %s"%(b,r)
		print "commamd : ",cmd
		s_call(cmd.split())
	elif ch==3:
		s=raw_input("Enter Source : \n")
		d=raw_input("Enter Destination : \n")
		cmd="aws s3 cp %s s3:/%s"%(s,d)
		print "commamd : ",cmd
		s_call(cmd.split())

	elif ch==4:
		s=raw_input("Enter Source : \n")
		d=raw_input("Enter Destination : \n")
		cmd="aws s3 cp s3:/%s %s"%(s,d)
		print "commamd : ",cmd
		s_call(cmd.split())
	elif ch==5:
		f=raw_input("Enter File path to be deleted: \n")
		cmd="aws s3 rm s3:/%s"%(f)
		print "commamd : ",cmd
		s_call(cmd.split())
	elif ch==6:
		cmd="aws s3 ls"
		print "commamd : ",cmd
		s_call(cmd.split())
	elif ch==7:
		b=raw_input("Enter Bucket name: \n")
		cmd="aws s3 ls %s"%(b)
		print "commamd : ",cmd
		s_call(cmd.split())
	elif ch==8:
		print "Exited "
		sys.exit()
	else:
		print "Enter Correct Choice "
