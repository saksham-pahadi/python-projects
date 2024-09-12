# # data in x
# x=[32,33,34,35,36,37,38,39,40,41]

# # frequency in f
# f=[7,14,30,28,35,34,16,14,36,16]
x=[]
f=[]
x1="DATA"
f1="Frequency"

def takevalue(x,x1):
    x=[]
    k=1
    print(f"Enter the values of {x1}\nEnter 0 when complete")
    while(k!=0):
        k=int(input("Enter:"))
        if(k!=0):
            x.append(k)
    return(x)




while True:
    x=takevalue(x,x1)
    f=takevalue(f,f1)
    if(len(f)!=len(x)):
        print(f"\nThe quqntity of {x1} and {f1} is not equal.\nKindly! re-enter the values.")
    else:
        break
    
# variable for group pair
gp=[0]
g1p=[0,0]
g2p=[0,0]
g3p=[0,0,0]
g4p=[0,0,0]
g5p=[0,0,0]

# group paired data
gd=[0]
g1d=[0,0]
g2d=[0,0]
g3d=[0,0,0]
g4d=[0,0,0]
g5d=[0,0,0]

# variable for group
g1=[]
g2=[]
g3=[]
g4=[]
g5=[]
print("Data(x):",x)
print("Frequency(f):",f)

# loop for first group pair
j=0
while(j<len(f)):
    if(gp[0]<f[j]):
        gp[0]=f[j]
        gd[0]=x[j]
    j=j+1
print("highest:",gp)
print("first group pair:",gp,"\n") 
           
#loop for second group 
i=0
while(i<len(f) and i+1<len(f)):
        g1.append(f[i]+f[i+1]) 
        i=i+2    
print("Second group :",g1) 

#loop for second group pair 
j=0
temp=0
while(j<len(g1)):
    if(temp<g1[j]):
        temp=g1[j]
        g1p[0]=f[j*2]
        g1p[1]=f[(j*2)+1]
        g1d[0]=x[j*2]
        g1d[1]=x[(j*2)+1]
    j=j+1
print("highest:",temp)
print("Second group pair:",g1p,"\n")

# loop for third group
i=1
while(i<len(f) and i+1<len(f)):
        g2.append(f[i]+f[1+i])
        i=i+2
        
# loop for third group pair
j=0
temp=0
while(j<len(g2)):
    if(temp<g2[j]):
        temp=g2[j]
        g2p[0]=f[(j*2)+1]
        g2p[1]=f[(j*2)+2]
        g2d[0]=x[(j*2)+1]
        g2d[1]=x[(j*2)+2]
    j=j+1
print("third group :",g2)
print("highest:",temp)
print("third group pair:",g2p,"\n")

# loop for fourth group 
i=0
while(i<len(f)-1 and i+2<len(f)):
        g3.append(f[i]+f[1+i]+f[2+i])
        i=i+3
print("fourth group :",g3)

# loop for fourth group pair
j=0
temp=0
while(j<len(g3)):
    if(temp<g3[j]):
        temp=g3[j]
        g3p[0]=f[(j*3)]
        g3p[1]=f[(j*3)+1]
        g3p[2]=f[(j*3)+2]
        g3d[0]=x[(j*3)]
        g3d[1]=x[(j*3)+1]
        g3d[2]=x[(j*3)+2]
    j=j+1
print("highest:",temp)
print("fourth group pair:",g3p,"\n")

# loop for fifth group 
i=1
while(i<len(f) and i+2<len(f)):
        g4.append(f[i]+f[1+i]+f[2+i])
        i=i+3
        
# loop for fifth group pair
j=1
temp=0
while(j<len(g4)):
    if(temp<g4[j]):
        temp=g4[j]
        g4p[0]=f[(j*3)+1]
        g4p[1]=f[(j*3)+2]
        g4p[2]=f[(j*3)+3]
        g4d[0]=x[(j*3)+1]
        g4d[1]=x[(j*3)+2]
        g4d[2]=x[(j*3)+3]
    j=j+1
print("fifth group :",g4)
print("highest:",temp)
print("fifth group pair:",g4p,"\n")

# loop for sixth group
i=2
while(i<len(f) and i+2<len(f)):
        g5.append(f[i]+f[1+i]+f[2+i])
        i=i+3
        
# loop for sixth group pair
j=0
temp=0
while(j<len(g5)):
    if(temp<g5[j]):
        temp=g5[j]
        g5p[0]=f[(j*3)+2]
        g5p[1]=f[(j*3)+3]
        g5p[2]=f[(j*3)+4]
        g5d[0]=x[(j*3)+2]
        g5d[1]=x[(j*3)+3]
        g5d[2]=x[(j*3)+4]
    j=j+1
print("sixth group :",g5)
print("highest:",temp)
print("sixth group pair:",g5p,"\n")

# creating a new list and append all paired group to mapping
m=gd+g1d+g2d+g2d+g4d+g5d

# creat new list for which index element present  how many times
rm=[0,0,0,0,0,0,0]

i = 0 
j = 0
while i <= 6:
    while j <= 12:
        if x[i] == m[j]:
            rm[i]+=1
        
        j += 1
    i += 1
    j = 1  # Reset j for the next iteration of the outer loop
print(m)
j=0
temp=0
while(j<=6):
    if(temp<rm[j]):
        temp=rm[j]  
    j=j+1
j=0
while(j<=6):
    if(temp==rm[j]):
        print("THE MODAL VALUE IS :",x[j],)
        print("------------------------")
    j=j+1