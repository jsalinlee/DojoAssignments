students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for count in range(len(students)):
    print students[count].get("first_name") + " " + students[count].get("last_name")
users = {

 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}
print "***************************************"
print "Students"
temp = users.get("Students")        #temporary array to get dict values easier

'''Loop through Students array and Instructors array
then print desired values with get functions'''

for count2 in range(len(users.get("Students"))):
    charCount = len(temp[count2].get("first_name")) + len(temp[count2].get("last_name"))
    print str(count2 + 1) + " - " + temp[count2].get("first_name") + " " + temp[count2].get("last_name") + " - " + str(charCount)
print "\nInstructors"
temp = users.get("Instructors")
for count in range(len(users.get("Instructors"))):
    charCount = len(temp[count].get("first_name")) + len(temp[count].get("last_name"))
    print str(count + 1) + " - " + temp[count].get("first_name") + " " + temp[count].get("last_name") + " - " + str(charCount)
