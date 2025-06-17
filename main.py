# For Loop :

str = 'Hello'
#type 1
for i in str: #here --> for i in str <--  mean --> i=0; i<len(str) ; i++
    print(i) #here--> print(i)  mean print(str[i])

#type 2
for i in range(0,len(str),1):
    print(str[i])

# here type 1 and type 2 will give smae output

for i in range(1,5,1):
    print(i)


# ***Here ---> for i in range(1,5,1) mean i=1;i<5; i=i+1
# ***Here ---> for i in range(0,7,2) mean i=0;i<7; i=i+2 







# Go To Loop

def Again(): #Again :
    while True:
     #Your Code Here  
      print("Doing Again")  
      

if 1==2 : #I used this to prenevnt unlimited looping
     Again()  #goto Again










# While Loop
print("While Loop")
i=0
while i<5:
    print(i)
    i+=1
