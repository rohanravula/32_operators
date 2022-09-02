"ARTHMATIC OPERATORS"
# a,b=[int(x) for x in input("enter the values of a & b : ").split()] # a&b valures are : 10 5
# print(f"The value of {a}+{b} is {a+b}") #15
# print(f"The value of {a}-{b} is {a-b}") #5
# print(f"The value of {a}*{b} is {a*b}") #50
# print(f"The value of {a}/{b} is {a/b}") #2.0
# print(f"The value of {a}//{b} is {a//b}") #2
# print(f"The value of {a}%{b} is {a%b}")   #0
# print(f"The value of {a}**{b} is {a**b}") #100000  

"ASSIGMENT OPERATOR"
# a=int(input ("enter the vlaue of the a ")) #if we take a value as 6
# a+=3
# print("the value of a after the doing the a+=3 is {}".format(a)) #9
# a-=6
# print("the value of a after the doing the a-=6 is {}".format(a)) #3
# a*=3
# print("the value of a after the doing the a*=3 is {}".format(a)) #9
# a/=2
# print("the value of a after the doing the a/=3 is {}".format(a)) #4.5
# a//=2
# print("the value of a after the doing the a//=2 is {}".format(a)) #2.0
# a**=2
# print("the value of a after the doing the a**=2 is {}".format(a)) #4.0
# a%=3
# print("the value of a after the doing the a%=3 is {}".format(a)) #1.0

"RELATIONAL OPERATOR"
# a=input("enter the value of a :") # the value of a is 4
# b=input("enter the value of b :") # the value of b is 6
# print(f"the value of {a}<{b}is {a<b}") #True
# print(f"the value of {a}>{b}is {a>b}") #False
# print(f"the value of {a}<={b}is {a<=b}") #True
# print(f"the value of {a}>={b}is {a>=b}") #False
# print(f"the value of {a}=={b}is {a==b}") #False
# print(f"the value of {a}!={b}is {a!=b}") #True

"LOGICAL OPERATOR"
# a=int(input("enter the value of a: "))
# b=int(input("enter the vlaue of b: "))
# print("the vlaue of a<b and b>a is {}".format(a<b and b>a))
# print("the vlaue of a<b and a>b is {}".format(a<b and a>b))
# print("the vlaue of a==b and b==a is {}".format(a==b and b==a))
# print("the vlaue of a!=b and b=!a is {}".format(a!=b and b!=a))
# print("the vlaue of a==b or b!=a is {}".format(a==b or b!=a))

"BITWISE OPERATOR"

# a=int(input("enter the value of a :")) #7
# b=int(input("enter the value of b :")) #8
# print("the value of {} & {}is {}".format(a,b,a&b)) #7&8 is 0
# print("the value of {}|{}is {}".format(a,b,a|b)) #7|8 is 15
"note: the negotation formula is -(vlaue+1)"
# a=int(input("enter the value of a :")) #
# b=int(input("enter the value of b :")) #
# print("the vlaue of ~{} is {}".format(a,~a))
# print("the vlaue of ~{} is {}".format(b,~b))

"IDENTITY OPERATOR"
# a=20
# b=40
# if(a is b) :
#     print("a and b identy are same")
# else:
#     print("the value of a & b identiry are not same")

# x=8
# print(type(x) is int) # True 
# print(type(x) is  float) # False


"MEMBERSHIP OPERATOR"

# name=["rohan", "lokesh", "ram","sham", "mohan"]
# print('rohan' in name)
# print('ram'  not in name)
# print('sohan' in name)
# name.sort()
# print(name)  

"SHIFT OPERATOR"
"right shift means /2"
# a=20
# print(a>>1) #10
# print(a>>2) #5
# print(a>>3) #2.5
# print(a>>4) #1
# print(a>>5) #0
"left shift means *2 "
b=4
print(b<<1)
print(b<<2)
print(b<<3)
print(b<<4)