import names
import random
file = open('./student_names.txt','r')
read_file = file.read()
file.close()
nb = random.randint(7,20)
file = open('./student_names.txt','a')
for i in range(nb):
 file.write((names.get_first_name() + '\n'))
file.close()
n1 = int(input('Please enter the number of the first lines that you want to read : '))
file = open('./student_names.txt')
list = file.readlines()
for j in range(n1) : 
  print(list[j])
file.close()
n2 = int(input('Please enter the number of the last lines that you want to read : '))
file = open('./student_names.txt')
list2 = file.readlines()
file.close()
ind = len(list2) - 1
for k in range(n2) : 
  print(list2[ind])
  ind = ind - 1
str = input ('Enter the name that you want to check in the file : ')
found = False
for cpp in list2 :
    if ( cpp == str + '\n') :
      found = True 
if (found == True) :
  print(str,"is in the file",sep=' ')
elif (found == False )  :
  print(str,"doesn't exist in the file",sep =' ')
