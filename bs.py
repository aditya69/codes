import threading
import xml.etree.ElementTree as X

def part(arr,low,high):
	p,i=arr[high],low	
	for j in range(low,high):
		if arr[j]<=p:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1
	arr[i],arr[high]=arr[high],arr[i]
	return i

def qsort(arr,low,high):
	if low<high:
		p=part(arr,low,high)
		t1=threading.Thread(target=qsort,args=(arr,p+1,high))
		t2=threading.Thread(target=qsort,args=(arr,low,p-1))
		t1.start()	
		t2.start()
		t1.join()
		t2.join()


def bs(arr,n,key):
	low=0
	high=n-1
	mid=(low+high)/2
	while low<=high:
		
		mid=(low+high)/2
		if arr[mid]==key:
			return mid
		elif arr[mid]<key:
			low=mid+1
		elif arr[mid]>key:
			high=mid-1
		
	return -1




r=X.parse('sample.xml').getroot()
arr=map(int,r.text.split())
#arr=r.text.split()
ch=[]
while ch!=4:
	print("1.sort2.search3.display")
	ch=int(raw_input("enter ch u want"))

	if ch==1:
		qsort(arr,0,len(arr)-1)
	elif ch==2:
		key=(int(raw_input("enter element u want to search")))

		ans =bs(arr,len(arr),key)
		if ans==-1:
			print("key not found")
		else:
			print("key found at",ans+1)
	elif ch==3:


			for i in arr:
				print i

	
 
