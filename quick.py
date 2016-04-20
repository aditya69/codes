import json
import threading
a=open('s.json','r')
s=[]
s=map(int,a.read().split())

j=0
for i in s:
	j=j+1

def part(arr,low,high):
	p,i=arr[high],low
	for j in range(low,high):
		if arr[j]<=p:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1
	arr[high],arr[i]=arr[i],arr[high]
	return i


def qsort(arr,low,high):
	if low<high:
		p=part(s,low,high)
		t1=threading.Thread(target=qsort,args=(s,p+1,high))
		t2=threading.Thread(target=qsort,args=(s,low,p-1))
		t1.start()
		t2.start()
		t1.join()
		t2.join()



qsort(s,0,j-1)

for i in s:
	print i

