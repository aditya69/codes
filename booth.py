from bitstring import BitArray
from flask import Flask
app = Flask(__name__)

def booth(m, r, x, y):
	# Initialize
	totalLength = x + y + 1
	mA = BitArray(int = m, length = totalLength)
	rA = BitArray(int = r, length = totalLength)
	A = mA << (y+1)
	S = BitArray(int = -m, length = totalLength)  << (y+1)
	P = BitArray(int = r, length = y)
	P.prepend(BitArray(int = 0, length = x))
	P = P << 1
	print "Initial values"
	print "A", A.bin
	print "S", S.bin
	print "P", P.bin
	print "Starting calculation"
	for i in range(1,y+1):
		if P[-2:] == '0b01':
			P = BitArray(int = P.int + A.int, length = totalLength)
			print "P +  A:", P.bin
		elif P[-2:] == '0b10':
			P = BitArray(int = P.int +S.int, length = totalLength)
			print "P +  S:", P.bin
		P = arith_shift_right(P, 1)
		print "P >> 1:", P.bin
	P = arith_shift_right(P, 1)
	print "P >> 1:", P.bin
	print "Integer:",P.int
	return P.bin,P.int

def arith_shift_right(x, amt):
	l = x.len
	x = BitArray(int = (x.int >> amt), length = l)
	return x


@app.route('/')
def f():
    return "hello wolrd"

@app.route('/<f>')
def g(f):
	x=open(f,'r').read().split()
	x=map(int,x)


	ans=booth(x[0],x[1],x[2],x[3])
	return "multiplication of no   "+str(x[0])+"    and    "+str(x[1])+"     is    "+'<br>'+str(ans)
    
if __name__ == '__main__':
    app.run(debug=True,port=5003)

