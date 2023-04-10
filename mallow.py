##s=int(input())          #factorial.
##e=int(input())
##for i in range(s,e+1):
##    fact=1
##    for j in range(i,0,-1):
##        if j==1:
##            print(j,end='=')
##        else:
##            print(j,end='*')
##        fact*=j
##    print(fact)
##    #print()

''''s=int(input())         #fibonacci        
e=int(input())
f1=-1
f2=1
for i in range(s,e+1):
    f3=f1+f2
    if f3>s and f3<e:
        print(f3,end='  ')
    f1=f2

    f2=f3'''

'''f=list(input())     #to eliminate same letters.
s=list(input())
print(f)
print(s)
for i in range(len(f)):
    for j in range(len(s)):
        if f[i]==s[j]:
            f[i]=''
            s[j]=''
print(f)
print(s)
f1="".join(f)
f2="".join(s)
total=len(f1)+len(f2)
print(total)'''

#min three low value.py
    
'''a="renganathan"
b=list(a)
print(b)
c=''.join(b)
print(c)'''

'''n=list(input())     #find index of character.
c=input()
print(n)
x=-1
A=[]
for i in range(len(n)):
    x+=1
    if n[i]==c:
        A.append(x)
        
print(c,'indexe are:',A)'''

'''x=list(input())     #to neglate the space.
print(x)
for i in range(len(x)):

    if x[i]==' ' and x[i+1]==' ':
        continue
    else:
        print(x[i],end='')'''


'''a=input()        #insert word inside the index.
b=input()
c=int(input())
x=list(a)
print(x)
y=len(x)
print(y)
if c<=y:
    x.insert(c,b)
    print(x)'''

'''a=input()
b=input()
c=int(input())
x=list(a)
print(x)
y=len(x)
if c<=y:
    x.append('')
    for i in range(y,c,-1):
        x[i]=x[i-1]      
    else:
        print('invalid index')
x[c]=b
print(x)
z=''.join(x)
print(z)'''

'''class sample:
    def fun(self,data,data1,n):
        print(data[:n]+data1+data[n:])
obj=sample()
print(obj.fun('renganathan','ajith',5))'''

'''a=input()
b=input()
c=int(input())'''






'''class direction:
    def data(self):
        dis=int(input())
        speed=int(input())
        dir=input()
n=int(input('laps:'))
A=[]
for i in range(n):
    obj=direction()
    obj.data()
    A.append(obj.data)
print(A)'''

'''n=int(input('number of labs:'))
for i in range(n):
    dis=int(input())
    speed=int(input())
    dir=input()
    time=(dis/speed)*3600
    if dir=='N':
        dir_y=dis*(+1)
    elif dir=='S':
        dir_y=dis*(-1)
    elif dir=="E":
        dir_x=dis*(+1)
    elif dir=='W':
        dir_x=dis*(-1)'''

'''class vowels:
    def data(self):
        n=input()
a=int(input('how mwny lwtters:'))
A=[]
for i in range(a):
    obj=vowels()
    obj.data()
    A.append(obj.data())
#n=input()
print(A)'''


'''a=[1,2,2,3,4,4,5,6,6,6,7,7,7]


b=len(a)
#print(b)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            a[i]=''
            if a[i]=="":
                a.remove(a)
print(a)

c=tuple(a)
print(c)
#x=str(a)
#print(x)
y=''.join(c)
print(y)'''


'''class slot:
    def slotdata(self):
        self.date=int(input())
        self.sid=int(input())
        self.nosheet=int(input())
class student:
    def studdata(self):
        self.studid=int(input())
        self.studcut=int(input())
        self.studage=int(input())
        self.studhsc=int(input())
        self.studsslc=int(input())
        self.cdate=0
        self.cslotid=0

n=int(input())
A=[]

for _ in range(n):
    s=slot()
    s.slotdata()
    A.append(s)
for j in range(len(A)):
    print(A[j].date)
    print(A[j].sid)
    print(A[j].nosheet)
a=int(input())
B=[]
for _ in range(a):
    st=student()
    st.studdata()
    B.append(st)
fsid=int(input())
for k in range(a):
    print(B[k].studid)
    print(B[k].studcut)
    print(B[k].studage)
    print(B[k].studhsc)
    print(B[k].studsslc)
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut < B[j].studcut:
            temp=B[j].studcut
            B[j].studcut=B[i].studcut
            B[i].studcut=temp
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut==B[j].studcut:
            if B[i].studage < B[j].studage:
                temp=B[j].studcut
                B[j].studcut=B[i].studcut
                B[i].studcut=temp
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut==B[j].studcut:
            if B[i].studage==B[j].studage:
                if B[i].studhsc < B[j].studhsc:
                    temp=B[j].studcut
                    B[j].studcut=B[i].studcut
                    B[i].studcut=temp
for i in range(a):
    for j in range(i+1,len(a)):
        if B[i].studcut==B[j].studcut:
            if B[i].studage==B[j].studage:
                if B[i].studhsc==B[j].studhsc:
                    if B[i].studsslc < B[j].studsslc:
                        temp=B[j].studcut
                        B[j].studcut=B[i].studcut
                        B[i].studcut=temp
noofsheet=0
for i in range(len(A)):
    noofsheet=noofsheet+A[i].nosheet
print('total no of sheet:',noofsheet)
a=0
if a<=noofsheet:
    for i in range(len(A)):
        for j in range(slot[i].nosheet):
            B[a].cdate=slot[j].date
            B[a].cslotid=slot[j].slotid
            a+=1
            if a==len(B):
                break
for i in range(a):
    if fsid==B[i].id:
        print(B[i].cdate,"|",fsid,"|",B[i].cslotid,sep=',')'''
    
        

'''class hotels:
    def hdata(self):
        self.hid=int(input('id:'))
        self.mindur=int(input('mindur:'))
        self.mdc=int(input('mdc:'))
        self.incd=int(input('incd:'))
        self.idc=int(input('idc:'))
        self.food=int(input('food:'))
n=int(input('nuber:'))
hot=[]
for i in range(n):
    hotel=hotels()
    hotel.hdata()
    hot.append(hotel)

for j in range(n):
    print(hot[i].hid)
    print(hot[i].mindur)
    print(hot[i].mdc)
    print(hot[i].incd)
    print(hot[i].idc)
hrcus=int(input())
budamt=int(input())
comamt=int(input())
predis=int(input())
premium=input()
tax=int(input())
food=input()
A=[]
B={}
for k in hot:
    cost=hot.mdc+((hot.hrcus-hot.mindur)//hot.incd)*hot.idc   #cost
    cost=(cost*hot.comamt)//100+cost           #comamt

    if premium=='Y' or premium=='y':     #premium
        cost=cost-((cost*predis)//100)
    else:
        pass

    cost=((cost*tax)//100)+cost     #tax


    if food=='Y' or food=='y':
        cost=cost+food
    else:
        pass
    print('total cost is:',cost)
    A.append(cost)
    B.append({K.id:cost})
A.sort()
for i in A:
    if i<butamt:
        final_amount=i
key=B.keys()
for a in key:
    if B(a)==final_amount:
        print(a,"|",final_amount,sep='')'''
    




##n1=int(input('enter your first number:'))    #biggest number.
##n2=int(input('enter your second number:'))
##n3=int(input('enter your third number:'))
##if n1>n2:
##    if n1>n3:
##        print('n1 is biggest number')
##    else:
##        print('n3 is biggest number')
##elif n2>n3:
##    print('n2 is biggest number')
##else:
##    print('n3 is biggest number')

'''a=[23,65,88,54,33,8,864,65,23]      ####biggest number
b=a[0]
d=a[0]
e=a[0]
c=[]
for i in a:
    if i>b:
        b=i            
c.append(b)

for i in a:
    if (i>d and i!=b):
        d=i
c.append(d)

for i in a:
    if i>e and i!=b and i!=d:
        e=i
c.append(e)
print(c)'''

'''x=int(input('enter your number:'))      ###fact with range.
y=int(input('enter your number:'))
for i in range(x,y):
    fact=1
    print(i,end=':')
    for j in range(i,0,-1):
        
        if j==1:
            print(j,end='=')
        else:
            print(j,end='*')
        fact*=j
    print(fact)'''


##while 1:                                  ###leap year.
##    n=int(input('enter the year:'))
##    if n%4==0:
##        print('%d is leap year'%(n))
##    elif n%40==0:
##         print('%d is leap year'%(n))
##    elif n%400==0:
##         print('%d is leap year'%(n))
##    else:
##        print('%d is not leap year'%(n))

'''a='renganathan'      ###assending with name.
b=list(a)
print(b)
for i in range(len(b)):
    for j in range(i,len(b)):
        if b[i]>b[j]:
            temp=b[j]
            #print(temp)
            b[j]=b[i]
            #print(b[j])
            b[i]=temp
            #print(b[i])
print(b)
k="".join(b)
print(k)'''

        
        

##n=input()
##print(n)
##a=n.split(' ')
##print(a)
##b=len(a)
##for i in range(len(a)):
##	A=a[i]
##	#print(A)
##	B=list(A)
##	#print(B)
##	for j in range(len(B)):
##		for k in range(len(B)):
##			pass
##		print(B[k],end='')
##		B.pop()
##	print(end=' ')


'''n=int(input('enter your number:'))       #pattern.
k=1
for i in range(n):
    for j in range(1,i+2):
        print(k,end=' ')
    print()
    k+=1'''

'''n=int(input('enter your number:'))      #pattern.
for i in range(n):
    k=0
    for j in range(i+1):
        k+=1
        print(k,end=' ')
    print()'''
'''k=1
n=int(input('enter your number:'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(k,end=' ')
    print()
    k+=1'''

##n=int(input('enter your number:'))
##k=n
##
##for i in range(n):
##    for j in range(n,0,-1):
##        print(k,end='')
##    print()


'''class emp:
    def getinfo(self):
        self.emp_no=int(input("enter emp no:"))
        self.emp_name=input("enter emp name:")
        self.emp_sal=int(input("enter emp salary:"))
    def display(self):
        print("employe number:",self.emp_no)
        print("employe name:",self.emp_name)
        print("employe salary:",self.emp_sal)
list=[]
n=int(input("enter no.of employee:"))
for i in range(n):
    student=emp()
    list.append(student)
    student.getinfo()
for i in range(n):
    print(list[i].emp_no,list[i].emp_name,list[i].emp_sal)
c=0
for i in range(n):
    if list[i].emp_sal > c:
        c=list[i].emp_sal
        name=list[i].emp_name
        id=list[i].emp_no
print(c,"||",name,"||",id)'''

##n=int(input("enter your number:"))
##space=n-1
##for i in range(0,n):
##    for j in range(0,space):
##        print("",end=" ")
##    for k in range(0,i+1):
##        print("*",end=" ")
##    print()
##    space-=1
##'''for A in range(0,n):
##    space+=1
###print(space)'''
##space=n-1
##for x in range(n-1):
##    for y in range(0,n-space):
##        print("",end=" ")
##    for z in range(space,0,-1):
##        print("*",end=" ")
##    space-=1
##    print()

"""
n=int(input("enter your number:"))     ###pattern   A
for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i==1 and 1<j<n) or (j==1 and i>1)  or (j==n and i>1) or i==5):
            print("*",end="")
        else :
            print(" ",end="")
    print()"""




##while True:
##    n=int(input("enter your number:"))
##    A=n//2
##    for i in range(1,n+1):
##        for j in range(1,n+1):
##            if ((i==1 and j>2) or (i==n and j<n) or (i==A and (1<j<n)) or (1<i<A and j==1) or (A<i<n) and j==n)):
##                print("*",end="")
##            else:
##                print(" ",end="")
##        print()



##def renga(R,T):
##    for k in range(R,T):
##        if k==R or k==T-1:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()
##n=int(input("enter your number:"))
##space=n-1
##for i in range(0,n):
##    for j in range(0,space):
##        print("",end=" ")
##    renga(R=0,T=i+1)
##    space-=1
##space=n-1
##for x in range(n-1):
##    for y in range(0,space):
##        print("",end=" ")
        


##n=int(input(" "))
##i=1
##
##while(i<=n):
##    j=1
##    while(j<=n):
##        if (i==j or i+j==8):
##            print("@",end=" ")
##        else:
##            print("  ",end="")
##        j=j+1
##    i=i+1
##    print()  

##n1=input("first name:")
##n2=input("second name:")
##X=list(n1)
##Y=list(n2)
##A=len(n1)
###R=print(X[A-1])
##B=len(n2)
###T=print(Y[B-1])
##for i in range(A):
##    print(X[i],end=" ")
##    for j in range(B):
##        pass 
##    print(Y[j],end=" ")
##    B=B-1

##id=input("enter amail id:")
##n=int(input("enter min char:"))
##A=print(len(id))
##spe_char=0
##alpha=0
##num=0
##if n <= len(id):
##    for i in id:
##        if i.isalpha()==True:
##            alpha=alpha+1
##        elif i.isnumeric()==True:
##            num=num+1
##        else:
##            spe_char=spe_char+1
##print("alpha in id is:",alpha)
##print("num in id is:",num)
##print("spe_char in id is:",spe_char)
##else:
##    print("please enter min 8 char")

##import threading
##def fun(name):
##    for i in name:
##        print(i,end="")
##def fun1(name):
##    B=list(name)
##    #print(B)
##    A=len(name)
##    #print(A)
##    for j in range((A-1),-1,-1):
##        print(B[j],end="")
##n1=input("name:")
##n2=input("names:")
##t1=threading.Thread(target=fun,args=(n1,))
##t2=threading.Thread(target=fun1,args=(n2,))
##t1.start()
##t2.start()



##a=["1223python8786","345jango878","1342jdfkrjf78434"]
##q=[]
##w=[]
##R=[]
##T=[]
##for i in a:
##    #print(i)
##    A=i
##    #print(A)
##    for j in range(len(A)):
##        if A[j].isalpha()==True:
##            R.append(A[j])
##        else:
##            T.append(A[j])
##    C=" ".join(T)
##    w.append(C)
##    T.clear()
##    B=" ".join(R)
##    q.append(B)
##    R.clear()
##print(q)
##print(w)

##name=input("name:")
##n=int(input("number:"))
##print((name*n))


"""id=input("enter your e mail id:")
#min=int(input("min:"))
#max=int(input("max:"))
a=len(id)
upp_case=0
low_case=0
num=0
spl_char=0
if 8<=len(id):
    for i in id:
        if i.isalpha()==True:
            if i.isupper()==True:
                upp_case+=1
            else:
                low_case+=1
        elif i.isnumeric()==True:
            num+=1
        else:
            spl_char+=1
    #print(upp_case)
    #print(low_case)
    #print(num)
    print(spl_char)
    if (0==upp_case and 1<=low_case and 1<=num and 1<=spl_char):
        print("valid E-mail id")
    else:
        print("invalid E-mail id")
    
else:
    print("please enter min 8 charactor")"""


##n=['e','r','d','a','q','e','t','g','f','d','w','w','f','d','w','q','w','e','t','e']
##A=[]
##for i in range(len(n)):
##    A_i_i=[]
##    if n[i] in n:
##        A_i_i=A.copy()
##        if n[i].islist==True:
##            #A_i=A.copy()
##            A_i_i.append(n[i])
##            #print(A_i)
##        else:
##            A_i_i=A.copy()
##            A_i_i.append(n[i])
##            #print(A_i)
##    
##for i in range(len(n)):
##    print("count is:",A_i_i)
##        
##        
##    

'''n=int(input("enter your number:"))
a=1
b=1
while b<=10:
    for i in range(1,n+1):
        print(i,"*",a,"=",(i*a))
        print()
    a+=1
    b+=1'''

##n=[[4,6,3],[2,3,4],[6,8,4],[2,1,3]]
##print(len(n))
##for i in range(len(n)):
##    for j in range(i+1,len(n)):
##        if n[i][1]>n[j][1]:
##            temp=n[i]
##            n[i]=n[j]
##            n[j]=temp
##print(n)

##n=[[4,6,3],[2,3,4],[6,8,4],[2,1,3]]
##A={}
##A.update({n[0][0]:n[1]})
##A.update({n[0][1]:n[2]})
##A.update({n[0][2]:n[3]})
##print(A)

##data="can run mon sun bun gun can run can son"
##a=input("enter your choice:")
##A=data.split(" ")
###print(A)
##B=print(len(A))
##C=set(A)
###print(C)
##T=list(C)
###print(T)
##Q={}
##for i in range(len(T)):
##    count=0
##    for j in range(len(A)):
##        if T[i]==A[j]:
##           count+=1
##        else:
##            pass
##    Q.update({T[i]:count})
##print(Q)
##W=Q.keys()
##print(W)
##for k in W:
##    if a==k:
##        print(a,":",Q[k])
##
##
##A=[35,86,12,56,2,34,68,23,75,98,21,63,74]
##B=len(A)
##R=[]
##for i in range(len(A)):
##    for j in range(len(A)):
##        if A[i]==A[j]:
##            pass
##        else:
##            C=A[i]-A[j]
##            if C<0:
##                C=-C
##            R.append(C)
###print(R)
####T=R.sort()
####print(T)
##for k in range(len(R)):
##    for T in range(k+1,len(R)):
##        if R[k]<R[T]:
##            temp=R[k]
##            R[k]=R[T]
##            R[T]=temp
##print(R[0])

##A=[35,86,12,56,2,34,68,23,75,98,21,63,74]
##B=[]
##for i in range(len(A)):
##    for j in range(i+1,len(A)):
##        if A[i]>A[j]:
##            temp=A[i]
##            A[i]=A[j]
##            A[j]=temp
##
##print(A)
##u=0
##for i in range(A[u]):
##    if i==len(A)-2:
##        pass
##    else:
##        for j in range(A[i+1]):
##            C=A[i]-A[j]
##            if C<0:
##                C=-C
##        B.append(C)
##    
##print(B)


##A="renga ajith"
##data=[A[::-1] for i in A]
##print(data)
#================================================
##a='whdkjsahd'
##b=''
##for i in a:
##    b=i+b
##print(b)


#==================================================
##A="entertainment"
##B=list(A)
##q=print(len(B))
##C=['a','e','i','o','u']
##D={}
##print(B)
##for i in range(len(B)):
##    #print(i)
##    if B[i] in C:
##        print(B[i])        
##        D.update({i:B[i]}) 
##
##print(B)
##print(D)
##w=D.keys()
##print(w)
##a=list(w)
##print(a)
##for k in a[::-1]:
##    print(k)
##    B.pop(k)
##print(B)
##T=[]
##for i in B[::-1]:
##    B=""+i
##    T.append(B)
##print(T)
##R=tuple(D)
##print(R)
##for i in R:
##    T.insert(i,D[i])
##print(T)
###=======================================================================
##
##A={'prem':[98,22,2002],'renga':[99,20,2003],'ajith':[87,18,2003],'surya':[67,24,2001]}
##B=A.keys()
##print(B)
##C=list(B)
##print(C)
##T=[]
##R={}
##for i in C:
##    A[i].append(i)
##    T.append(A[i])
##print(T)
##for i in range(len(T)):
##    for j in range(i+1,len(T)):
##        if T[i][1]>T[j][1]:
##            temp=T[i]
##            T[i]=T[j]
##            T[j]=temp
##print(T)
##for i in range(len(T)):
##    Z=T[i][-1]
##    print(Z)
##    Y=T[i].pop()
##    print(T[i])
##    R.update({Z:T[i]})
##print(R)

#####============ ====================================================================


##a='renganathan * & @'
##b=a.split(" ")
##print(b)
##b=""
##for i in a:
##    b=b+i
##print(b)

##=========================================================

##a=["one","two","three","four","five","six","seven","eight","nine","ten"]
##A=[]
##b=''
##for i in range(len(a)):
##    if i%2!=0:
##        for j in a[i]:
##            b=j+b
##        A.append(b)
##        b=''
##    else:
##        A.append(a[i])
##print(A)'''

##==============================================================
##A=input("enter first name:")
##B=input("enter first name:")
##C=input("enter first name:")
###A="abcedjsej"
##a=len(A)
###B="qwer"
##b=len(B)
###C="123456789"
##c=len(C)
##r=0
##Q=[]
##R=""
##E=[]
##Q.append(a)
##Q.append(b)
##Q.append(c)
##print(Q)
##Q.sort()
##prit(Q)
##W=Q[-1]
##for i in range(Q[-1]):
##    if r<a:
##        R=R+A[r]
##    else:
##        pass
##    if r<b:
##        R=R+B[r]
##    else:
##        pass
##    if r<c:
##        R=R+C[r]
##    T=str(R)
##    E.append(T)
##    R=""
##    r+=1
##print(E)
#####=======================================================================

##A=5
##B="flames"
##C=list(B)
###print(C)
##Q=C
###print(Q)
##for i in range(len(C)):
##    if len(Q)<A:
##        if len(Q)<A:
##            Q=
####            print(Q)




##        else:
##            Q.pop(A-1)
####            print(Q)
##            
##        
##    else:
##        Q.pop(A-1)
##print(Q)

#==========================================================================
##Q=[34673764,46736,356,13,6564,66786,4534]
##for i in range(len(Q)):
##    A=Q[i]
##    C=0
##    while A>0:
##        B=A%10
##        C=C+B
##        A=A//10
##    D=C
##    E=0
##    while D>0:
##        F=D%10
##        E=E+F
##        D=D//10
##    print(E)
#============================================================================
##C=4
##A=['f','l','a','m','e','s']
###R=A.split("")
##print(A)
###print(R)
##a=len(A)
##B=[]
##for i in range(a):
##    if C>len(A):
##        R=A[a:]+A[:a-1]
##        B.append(R[C])
##    else:  
##        B.append(A[C-2])
##        #R=A[a:]+A[:a-1]
##        A.pop(C-1)
##
##print(B)

#================================================================
##a=["ajith","renga","bala","malini","vaathiyar"]
##b=[]
##r=""
##for k in range(len(a[-1])):
##    for i in a:
##        A=i
##        for j in range(k,len(A)):
##            B=A[j]
##            r=r+B
##            break
##    
##    b.append(r)
##    r=""
##print(b)
#===================================================================
##n=int(input("enter:"))
##a=n
##b=n
##for i in range(a):
##    for j in range(n-i):
##        print(j,end=" ")
##    print()
#===================================================================
##n=int(input("enter your number:"))
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=" ")
##    print()
#==================================================================
##n=int(input("enter your nunber:"))
##a=n
##b=5
##for i in range(a):
##    for j in range(n-i):
##        print(b,end=" ")
##    print()
#===================================================================
##n=int(input("enter your number:"))
##a=n
##b=n
##
##for i in range(a):
##    for j in range(n-i):
##        print(b,end=" ")
##    print()
##    b=b-1
#====================================================================
##n=int(input("enter number:"))
##for i in range(n):
##    for j in range(i+1,0,-1):
##        print(j,end=" ")
##    print()
#======================================================================
##n=int(input("enter number:"))
##sum=0
##for i in range(n):
##    if i==0:
##        A=(2*i)+1
##        #print(sum)
##        for j in range(i+1):
##            print(A,end="  ")
##        print()
##        print()
##    else:
##        A=A*2
##        sum=A
##        #print(sum)
##        for j in range(1,i+2):
##            print(sum,end="  ")
##            sum=sum-(sum//2)
##        print()
##        print()
#================================================================
##n=int(input("enter your number:"))
##
##k=1
##for i in range(n):
##    for j in range(i+1+i):
##        print(k,end=" ")
##        k=k+1
##    print()
#=================================================================
##n=int(input("enter your number:"))
##k=1
##for i in range(1,n+1):
##    x=k
##    for j in range(i):
##        print(x,end=" ")
##        x=x-1
##    k=k+(2*i-j)
##    print()
#===========================================================
##n=int(input("enter your number:"))
##k=1
##for i in range(n):
##    x=k
##    for j in range(i+1):
##        print(x,end=" ")
##        x=x-1
##    print()
#================================================================
'''n=int(input("enter your number:"))
x=1
y=1
k=1
for i in range(1,n+1):
    y=1
    for j in range(1,i+i):
        if x>=j:
            print(y,end=" ")
            if x>j:
                y=y*2
        else:
            A=y//2
            y=y-A
            print(y,end=" ")
    x+=1
    k+=1
    print()'''
#====================================================================
##n=int(input("enter your number:"))
##for i in range(n):
##    N=10
##    for j in range(i+1):
##        if N<=0:
##            break
##        else:
##            print(N,end=" ")
##        N=N-2
##        
##    print()
#=======================================================================
##n=int(input("enter your number:"))
##A=5
##for i in range(n):
##    A=5
##    for j in range(A-i):
##        print(A,end=" ")
##        A=A-1
##    print()
#=========================================================================
##n=int(input("enter your number:"))
##A=1
##for i in range(n):
##    A=1
##    if i==0:
##        print("0")
##    else:
##        print("0",end=" ")
##        B=A*i
##        C=B
##        for j in range(i):            
##            print(B,end=" ")
##            B=C*(j+2)
##        print()
#===================================================
##n=int(input("enter your number:"))
##A=n
##for i in range(n):
##    B=0
##    if i==B:
##        for k in range(n,0,-1):
##            print(k,end=" ")
##        for j in range(1,n+1):
##            print(j,end=" ")

#===============================================================================================
n=int(input("enter your number:"))
for k in range(10,n+1):
    t=k
    a=str(t)
    b=list(a)
    #print(b)
    count=1
    A=[]
    for i in b:
        #print(i)
        c=int(i)
        #A.append(c)
        if c not in A:
            A.append(c)
        else:
            A.append(c)

            count=count+1
    sum=0
    if count>=2:
        for r in range(len(A)):
            sum=sum+A[r]
        if sum<=5:
            print(t)
##    print(A)
##    sum=0
##    print("%d is :%d"%(c,count))
    
    
    
            
        
        

    
    
    

    
    

    
      
      

    
        

    





            






      
      
    





























            






                    



















