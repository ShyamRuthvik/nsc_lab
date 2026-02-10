import hashlib 
import sys 
def hash(a): 
    result = hashlib.sha1(a.encode()) 
    a=result.hexdigest() 
    res = int(a, 16) 
    return res 
p=int(input("Enter p value : ")) 
q=int(input("Enter q value as prime divisor of p-1 : ")) 
h=int(input("Enter h value in range of 1 t0 p-1 : ")) 
g=pow(h,(p-1)//q,p) 
print("The value of g is : ",g) 
x=int(input("Enter user private key :")) 
y=pow(g,x,p) 
k=int(input("Enter k value in range of o to q : ")) 
r=pow(pow(g,k,p),1,q) 
x1=1 
while (k*x1)%q!=1: 
    x1+=1 
h=input("Enter message :")   
h1=hash(h) 
print("The h1 value is ",h1 ) 
s=pow(x1*(h1+x*r),1,q) 
print("The value of r and s is : ",r ,s) 
if s==0 or r==0: 
    print("invalid") 
    sys.exit(0) 
s1=1 
while (s1*s)%q!=1: 
    s1+=1 
w=pow(s1,1,q) 
ha=input("Enter msg after transmission :") 
h2=hash(ha) 
print("the value of h2 ",h2) 
u1=(h2*w)%q 
u2=(r*w)%q 
v=((pow(g,u1)*pow(y,u2))%q)%p 
print(u1,u2,y,v,r) 
if v==r: 
    print("valid") 
else: 
    print("Not valid")
#Enter q value as prime divisor of p-1 : 5
# Enter h value in range of 1 t0 p-1 : 10
# The value of g is :  1
# Enter user private key :10
# Enter k value in range of o to q : 3
# Enter message :hello welcome to nsc lab
# The h1 value is  1103894014913676640963277234425932413600103189928
# The value of r and s is :  1 1
# Enter msg after transmission :hello welocme to nsc lab
# the value of h2  228056070146739718221074259857506724331317833209
# 4 1 1 1 1
# valid
#2nd method
import hashlib

# 1. Setup & Key Gen
p, q = 23, 11  # Example primes where q divides p-1
g = 2          # Generator
x = 7          # Private key
y = pow(g, x, p) # Public key

# 2. Signing
msg = "hello"
h_val = int(hashlib.sha1(msg.encode()).hexdigest(), 16)
k = 3          # Random per-message secret
r = pow(g, k, p) % q
s = (pow(k, -1, q) * (h_val + x * r)) % q

print(f"Signature (r, s): ({r}, {s})")

# 3. Verification
w = pow(s, -1, q)
u1 = (h_val * w) % q
u2 = (r * w) % q
v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

print("Valid!" if v == r else "Invalid!")