def highrank(names,marks,updates):
    list2=sorted(marks)
    list3=list2[::-1]
    print("Before Updates, Ranks are:-")
    for i in range(0,d):
        for j in range(0,d):
            if list3[i]==marks[j]:
                print("Rank:",(i+1),"---->",names[j])
    newlist=[]
    for i in range(0,d):
        newlist.append(marks[i]+updates[i])
    list1=sorted(newlist)
    list5=list1[::-1]
    print("After Updates student with highest marks:")
    for i in range(0,d):
        if list5[0]==newlist[i]:
            print("Rank:","1","---->",names[i],"[Final Marks:",list5[0],"]")
            k=i
    for i in range(0,d):
        if marks[k]==list3[i]:
            l=i+1
    Jump=abs(l-1)
    print("Jump of rank:",Jump)

a=input("Please Enter the list of Student's Names: ")
names=a.split(",")

b=input("Please Enter the list of marks obtained by students: ")
marks=b.split(",")

c=input("Please Enter the list of Updation of numbers: ")
updates=c.split(",")

d=len(names)
e=len(marks)
f=len(updates)
if d==e and d==f:
    for i in range(0,e):
      marks[i]=float(marks[i])

    for i in range(0,f):
      updates[i]=float(updates[i])

    highrank(names,marks,updates)
else:
    print("Sorry, Lists are of different lengths")