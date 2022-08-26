# f=open("question3.txt","r")
# for i in open(f):
#     if "delhi" in "question3.txt":
#         f=open("question3.txt","a")
#         f=write(i)
#         f=write("\n")
#         f=close()
#     elif "shimla" in i:
#         f=open("shimla.txt","a")
#         f=write(i)
#         f=write("\n")
#         f.close()
#     else:
#         f=open("others.txt","a")
#         f=write(i)
#         f=write("\n")
#         f=close()
# print("succesfull!!!")




for i in open("question3.txt","r"):
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
    elif "shimla" in i :
        f=open("shimla.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
    else:
        f=open("other.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
print("succussfull !!!")