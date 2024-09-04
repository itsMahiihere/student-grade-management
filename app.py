
student_grade={ }

# add a new student 
def add_student(name,grade):
    student_grade[name]=grade
    print(f"Added {name} with a {grade}")
    
# update a student

def update_student(name,grade):
    if name is student_grade:
        student_grade[name]=grade
        print(f"{name} marks are updated with {grade}")
    else:
        print(f"{name} is not found!")
        
# delete a student

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been sussessfully deleted")
        
# view all student

def view_all_student():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name}:{grade}" )
    else:
        print("No student founded")
        
def main():
    while True:
        print('\n Student Grade Management Student')
        print("1. Add Student")
        print("2. Update Student")   
        print("3. Delete Student")           
        print("4. view Student")
        print("5. exit")
        
        choice=int(input("Enter your choice="))
        if choice==1:
            name=input("Enter student name= ")   
            grade=int(input("Enter student grade= "))
            add_student(name,grade)     
            
        elif choice==2:
            name=input("Enter student name= ")
            grade=int(input("Enter student grade= "))
            update_student(name,grade)    
            
        elif choice==3:
            name=input("Enter student name= ")
            delete_student(name)
            
        elif choice==4:
            view_all_student()
            
        elif choice==5:
            print("closing the program...")
            break
        else:
            print("Invalid choice")
            
if __name__== '__main__':
    main()            
                
                    
          
                  
               
        

