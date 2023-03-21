import mysql.connector

conn= mysql.connector.connect(host='localhost',username='root',password='Brijesh@1610',database='student')
my_cursor = conn.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS student (Name VARCHAR(255), Roll INT , Branch VARCHAR(255), Dept VARCHAR(255))")

    
def search_stud():
    #Write code to SEARCH student from database.
    rn=input("enter the roll to find a particular student:")
    qy="SELECT * from student WHERE Roll= %s"
    print(qy)
    rl=(rn)
    try:
        my_cursor.execute(qy,tuple(rl))
        myresult = my_cursor.fetchall()
        print("name   roll  branch dept")
        for i in myresult:
            for j in i:
                print(j,end="  ")
        conn.commit()
    except TypeError:
        pass

def create_stud():
    #Write code to ADD student to database.
    name=input("enter the student name:")
    rn=input("enter the roll number:")
    branch=input("enter the branch :")
    department=input("enter the department:")
    
    qy="INSERT into student(Name,Roll,Branch,Dept)VALUES(%s,%s,%s,%s)"
    val=(name,rn,branch,department)
    
    try:
        my_cursor.execute(qy,val)
        conn.commit()
        print("\nvalues inserted succefully.......")
    except TypeError:
        pass

def delete_stud():
    #Write code to DELETE student from database.
    rn=input("enter the roll of student u need to delete:")
    qy="DELETE from student WHERE Roll=%s"
    rl=(rn)
    try:
        my_cursor.execute(qy,tuple(rl))
        conn.commit()
        print("\nrecord deleted successfully............\n")
    except TypeError:
        pass


def update_stud():
    
    #Write code to UPDATE student in database. 1.name 2.roll 3.branch 4.department
    roll=input("enter the roll of student for updation:\n")
    print("update the student table choose your optiopn\n1.name\n2.roll\n3.branch\n4.department")
    
    choice=input("enter your choice:")
    
    try:
        if choice=='name':
            
            name=input("enter the new name:")
            qy= "UPDATE student SET Name= %s where Roll =%s"
            n=(name,roll)
            my_cursor.execute(qy,tuple(n))
            conn.commit()
        elif choice=='roll':
             
             rn=input("enter the new roll number:")
             qy= "UPDATE student SET Roll= %s where Roll=%s"
             rl=(rn,roll)
             my_cursor.execute(qy,tuple(rl))
             conn.commit()
        elif choice=='branch':
              
              branch=input("enter the new branch name:")
              qy= "UPDATE student SET Branch= %s where Roll= %s"
              br=(branch,roll)
              my_cursor.execute(qy,tuple(br))
              conn.commit()
        elif choice=='department':
              department=input("enter the new department name:")
              qy="UPDATE student SET Dept = %s where Roll= %s"
              dep=(department,roll)
              my_cursor.execute(qy,tuple(dep))
              conn.commit()
    except TypeError:
       pass

def display_stud():
    #write code display all values from database
    qy="SELECT*FROM student"
    
    try:
        my_cursor.execute(qy)
        my_result = my_cursor.fetchall()
        print("____record____")
        for i in my_result:
            print(i)
    
    except TypeError:
        pass
if __name__=="__main__":
    
    while True:
        print("\n ------------WELOCME TO THE STUDENT MANAGEMENT SYSTEM------------\n ")
        print("\t\t=======================")
        print('''\nEnter the operation you want to perform
                1.Add new Student
                2.Search a Student
                3.Display all Student Details
                4.Update Details
                5.Delete a Student Detail
                6.Exit''')
        choice=int(input("\n\nEnter the choice[1/2/3/4/5/6]:"))
        while choice not in  [1,2,3,4,5,6]:
            print("\nOops that seems to be  an  invlaid Choice!!")
            choice=int(input("\n\nEnter the choice[1/2/3/4/5/6]:"))
        
        if choice == 1:
            create_stud()
        elif choice == 2:
            search_stud()
        elif choice == 3:
            display_stud()
        elif choice == 4:
            update_stud()
        elif choice == 5:
            delete_stud()
        elif choice == 6:
            print("\n\texiting.........")
            break
            
            
            
            
        
        
        
    
    