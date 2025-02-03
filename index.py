#student ditail are enter  and so  to though give roll number

dict1 ={}
student_number = int(input("how many student  ditail are inter :"))
for i in range(student_number):
    key = input("Enter student roll number  to give you = ")
    value = {}
    dict1[key] = value
    for a in range(2):
        student_key = input("enter the name,addres,mobile no.,class,mark = ")
        student_value = input("enter = ")
        #value[student_key] = student_value

        value.update({student_key:student_value})
        
    print("\n\n",value)
print("\n\n",dict1)

print("pradeep kumar sahu")
