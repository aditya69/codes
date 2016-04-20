import json

f=open('s.json','r')
s=f.read()
print s

cnt=int(raw_input("enter size of board"))
a=[0 for i in range(cnt)]


x=json.loads(s).get("x")
y=json.loads(s).get("y")



def check(a,i):
	for j in range(i):
		if a[j]==a[i]:
			return False
		if abs(a[j]-a[i])==abs(j-i):
			return False
	return True




def solve(a,i):
	if i==cnt:
		if a[x-1]==y:
			print a
		return 

	for it in range(1,cnt+1):
		a[i]=it
		if check(a,i):
			solve(a,i+1)



solve(a,0)




