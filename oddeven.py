import threading
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
	return "hello world"

class FlagObj():
	def __init__(self):
		self.f=True

def sort(x,s,f):
	for i in range(s,len(x)-1,2):	
		if x[i]>x[i+1]:
			x[i],x[i+1]=x[i+1],x[i]
			f.f &=False


@app.route('/<f>')
def oddevensort(f):
	x=open(f,'r').read().split()
	x=map(int,x)
	l=[]
	sorted=FlagObj()
	sorted.f=False
	while not sorted.f:
		sorted.f=True
		t1=threading.Thread(target=sort,args=(x,0,sorted),group=None)
		t2=threading.Thread(target=sort,args=(x,1,sorted),group=None)
		l.append((t1.name,t2.name))		
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		print sorted.f
	return (str(x)+"<br>"+str(l)) 	

def hello():
	return "hello world"

if __name__=="__main__":
	app.run(debug=True,port=5012)

