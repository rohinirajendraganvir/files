# f=open("klm.txt","r")
# import os
# os.path.exist("klm.txt")
# # for i in "klm.txt":
# os.remove("klm.txt","ing")
# f=f.read()
# print(f)
# # print("the file does not exist")
# f.close()

# counting_ing
# f=open("ksr.txt","a")
# m=f.write("is")
# # m=f.read().split()
# c=0
# for i in m:
#     if "ing" in i:
#         c=c+1
#         # remove.f("ing")
# print(c)
# f.close()


# f=open("ksr123.txt","r") 
# a=f.read()
# print(a)
# f.close()

# line="dancing,running ,walking"
# for i in line:
#     f=open("ksr123.txt",'r')
#     a=line.replace("ing",'')
# print(a)
# f.close()
 


# line="dancing running walking"
# f=open("ksr123.txt","r")
# # for i in line:
# a=line.split()
# c=""
# for i in a:
#     b=i+"is "
#     c+=b
#     print(b)
# f.close()










# file = open('geek.txt','w')
# file.write("hi this is rohini")
# file.close()
# file=open('geek.txt','a')
# file.write(' m from maharstra')
# file.close()
# file=open('geek.txt','r')
# file.read()
# file.close()


# file = open("kkk.bin","wb")
# sentence = bytearray("This is good".encode("ASCII"))
# file.write(sentence)
# file.close()


# file=open("array.bin","wb")
# num=[64,32,11,2,12,67,150,56,43]
# array=bytearray(num)
# # print(file.read())
# file.write(array)
# file.close()


# file = open("sonu.bin", "rb")
# byte = file.read(3)
# while byte:
#     print(byte)
#     byte = file.read(3)




# comma-separated value
# import csv
# f = open("lock.bin", "w")
# writer = csv.writer(f)
# writer.writerows([["aditya", 1], ["baby", 2], ["ciya", 3], ["dash",4]])
# f.close()


# f = open("ksr123.txt", 'r')
# variable1= f.readlines()
# print(variable1)
# count=0
# i=0
# while i<len(variable):
#     j=0
#     while j<len(variable1[i]):
#         if variable1[0][j]=="ing":
#             count+=1
#         j+=1
#     i+=1
# print(count)

# fi = open('ksr123.text','r')
# l = fi.read()
# s = ''
# l1 = []
# for i in l:
#     if i !=',':
#         s+=i
#     else:
#         l1.append(s)
#         s=""
# c = 0 
# for i in l1:
#     if i[-3:] == 'ing':
#         c+=1
# print(c)


# z=open("ksr123.txt","r")
# m=z.read().split()
# c=0
# for i in m:
#     if "ing" in i:
#         c=c+1
# print(c)
# z.close()


f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
f.close()

