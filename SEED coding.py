a = 0
# while a < 5:
#   a = a+1
#   x_1 = input("Welcome, which teacher are you?")
#   b = 0 
#   while b < 1:
#     b = b+1
#     x = input("Please put in your assignment. If there is none, type 'none' ")
#     if x == "none":
#       break
#     t = int(input("Please put in how long the assignment will take to complete in minutes, please keep in mind that there is a maximum time for all teachers of 180 minutes."))
#     if t < 180:
#       print("Okay there is a total of",int(180-t), "minutes left")
#     c = 0  
  
#     assignmentlist = [ ]

#     d = 0
#     while d < 4:
#       d = d + 1  
     
    
#       x_2 = input("Please put in another assignment. If there is none, type 'none' ")
      
#       if x_2 == "none":
#         break 
#       t_2 = int(input("Please put in how long the assignment will take to complete in minutes, please keep in mind that there is a maximum time for all teachers of 180 minutes."))
#       assignmentlist.append(t_2)
#       total = sum(assignmentlist)
      
#       if total + t < 180:
#         print("Okay there is a total of",int(180-total-t), "minutes left")

x_1 = input("Welcome, which teacher are you?")
z = {}
end = False
for day in ['monday','tuesday','Wednesday','Thursday','Friday']: 
  total = 0
  assignmentlist = []
  c = 0
  
  
  if end == True:
    break
  while c < 1000000:
    c = c+1
    x_2 = input("Put in another assignment. Please put no assignments above 180 minutes. If there is none, type 'none'. If there is none or no more for the day, type 'noday'")
    if x_2 == "none":
        end = True
        z[day] = assignmentlist
        break
    if x_2 == "noday":
        z[day] = assignmentlist
        break
    
    t = int(input("Please put in how long the assignment will take to complete in minutes, please keep in mind that there is a maximum time for all teachers of 180 minutes."))
    if t > 180:
        print("Don't do this")
        continue
    total += t
    print("Okay there is a total of",int(180-total), "minutes left")
    if (total) >= 180:
      print("You have exceeded the time limit for students. Please change the assignment or the time.")
      z[day] = assignmentlist
      break
      if t_error < 180:
        print("Okay there is a total of",int(180-total-t_error), "minutes left")
        break
    
    assignmentlist.append((x_2,t))
  print(z)

import csv

with open('TeacherApplication.csv', 'w') as f:
    for key in z.keys():
        f.write("%s,%s\n"%(key,z[key]))


##predictions_file = open("myfirstforest.csv", "w", newline="")
##
##with open("myfirstforest.csv", "w", newline="") as predictions_file:
##    predictions_file = csv.DictWriter(f, z.keys()
##    predictions_file.writeheader()
##    predictions_file.writerow(z)
##

##plaintext = input("Please enter the text you want to compress")
##filename = input("Please enter the desired filename")
##with gzip.open(filename + ".gz", "wb") as outfile:
##    outfile.write(bytes(plaintext, 'UTF-8'))
##    
##      
##      
##      
