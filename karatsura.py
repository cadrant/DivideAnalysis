


#Compute 1234*4321
 #a1=12*43
 #d1=34*21
 #e1=(12+34)*(43+21)-a1-d1

def multiply(x, y):

    #CAD print("x: " + str(x) + " len x: " + str(len(str(x))))
    #CAD print("y: " + str(y) + " len y: " + str(len(str(y))))
    #Base Case
    if len(str(x)) <= 1 or len(str(y)) <= 1:
        return x * y

    #Split numbers into a, b, c, d  
    n = max(len(str(x)),len(str(y)))//2
    
    a = x // 10**(n)
    b = x % 10**(n)
    c = y // 10**(n)
    d = y % 10**(n)

    #step 1
    z2 = multiply(a,c)
    #step 2
    z0 = multiply(b,d)
    #step 3
    z1 = multiply((a + b),(c + d)) - z2 - z0

    #CAD print ("z2 " + str(z2))
    #CAD print ("z0 " + str(z0))
    #CAD print ("z1 " + str(z1))

    #print(n)
    return z2 * (10**n)**2 + z1 * (10**n) + z0

#should be 408
#print (multiply(12,34))
#Should be 7006652
#print (multiply(1234,5678))

#Should
#x = 1234123412341234123412341234123
#y = 5678567856785678567856785678567
#print (multiply(x,y))

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

#Wolfram Output
z = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
my_z = multiply(x,y)
print ("z: " + str(z))
print ("my_z: " + str(my_z))

if z == my_z:
    print ("We're done.  The answers match")
else:
    print ("We are not done.  The answers do not match")

   


