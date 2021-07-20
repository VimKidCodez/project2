"""


def #compute_lcm(num1, num2):

   # choose the greater number
   if num1 > num2:
       greater = num1
   else:
       greater = num2

   while(True):
       if((greater % num1 == 0) and (greater % num2 == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# num1 = str(input("enter the first number "))
# num2 = str(input("enter the second number"))

print("The L.C.M. is", compute_lcm(num1, num2))

"""
# Python Program to find LCM of Two Numbers using Functions
def findlcm(a, b):   # Function definition
    if(a > b):
        maximum = a
    else:
        maximum = b
    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            lcm = maximum;
            break;
        maximum = maximum + 1
    return lcm
# Taking inputs from the user
num1 = int(input("enter the first number that you want to find the lcm: "))
num2 = int(input("enter the second number that you want to find the lcm: "))
lcm = findlcm(num1, num2)   # Function call
print("the lcm is ", lcm)