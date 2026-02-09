q=91 
alpha=11 
xa=int(input("Enter private key of A: ")) 
xb=int(input("Enter Private Key of B: ")) 
ya=pow(alpha, xa)%q 
print("Public Key of A:", ya) 
yb=pow(alpha, xb)%q 
print("Public Key of B:",yb) 
if pow(yb, xa)%q == pow(ya, xb)%q: 
    print("equal") 
else: 
    print("no") 
# 56,71

 
  
