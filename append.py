# file_object =open("append.txt", "w")
# file_object.write('hellohhhhhh')
# file_object.close()


# f=open("a.txt","w")
# f.write("gdhkjd")
# f.close()


# f=open("d.txt","a+")
# f.write("ikmnbg")
# f.close()


# f = open("demofile2.txt", "a")
# f.write("i hate u")
# f.close()


import os
if os.path.exists("rohini.txt"):
    os.remove("rohini.txt")
else:
  print("The file does not exist")

