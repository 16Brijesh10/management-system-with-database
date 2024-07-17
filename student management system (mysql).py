import mysql.connector

# Establishing the connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    username='root',
    password='Brijesh@1610',
    database='student'
)
my_cursor = conn.cursor()

# Creating the student table if it does not exist
my_cursor.execute("CREATE TABLE IF NOT EXISTS student (Name VARCHAR(255), Roll INT, Branch VARCHAR(255), Dept VARCHAR(255))")

def search_stud():
    """
    Function to search for a student in the database by roll number.
    """
    rn = input("Enter the roll to find a particular student: ")
    qy = "SELECT * from student WHERE Roll = %s"
    rl = (rn,)
    try:
        my_cursor.execute(qy, rl)
        myresult = my_cursor.fetchall()
        for i in myresult:
            print(i)
        conn.commit()
    except TypeError:
        pass

def create_stud():
    """
    Function to add a new student to the database.
    """
    name = input("Enter the student name: ")
    rn = input("Enter the roll number: ")
    branch = input("Enter the branch: ")
    department = input("Enter the department: ")

    qy = "INSERT INTO student(Name, Roll, Branch, Dept) VALUES (%s, %s, %s, %s)"
    val = (name, rn, branch, department)
    
    try:
        my_cursor.execute(qy, val)
        conn.commit()
        print("\nValues inserted successfully.......")
    except TypeError:
        pass

def delete_stud():
    """
    Function to delete a student from the database by roll number.
    """
    rn = input("Enter the roll of student you need to delete: ")
    qy = "DELETE FROM student WHERE Roll = %s"
    rl = (rn,)
    try:
        my_cursor.execute(qy, rl)
        conn.commit()
        print("\nRecord deleted successfully............\n")
    except TypeError:
        pass

def update_stud():
    """
    Function to update student details in the database.
    Allows updating name, roll, branch, or department.
    """
    roll = input("Enter the roll of student for updation:\n")
    print("Update the student table, choose your option\n1. Name\n2. Roll\n3. Branch\n4. Department")
    
    choice = input("Enter your choice: ")
    
    try:
        if choice == 'name':
            name = input("Enter the new name: ")
            qy = "UPDATE student SET Name = %s WHERE Roll = %s"
            n = (name, roll)
            my_cursor.execute(qy, n)
            conn.commit()
        elif choice == 'roll':
            rn = input("Enter the new roll number: ")
            qy = "UPDATE student SET Roll = %s WHERE Roll = %s"
            rl = (rn, roll)
            my_cursor.execute(qy, rl)
            conn.commit()
        elif choice == 'branch':
            branch = input("Enter the new branch name: ")
            qy = "UPDATE student SET Branch = %s WHERE Roll = %s"
            br = (branch, roll)
            my_cursor.execute(qy, br)
            conn.commit()
        elif choice == 'department':
            department = input("Enter the new department name: ")
            qy = "UPDATE student SET Dept = %s WHERE Roll = %s"
            dep = (department, roll)
            my_cursor.execute(qy, dep)
            conn.commit()
    except TypeError:
        pass

def display_stud():
    """
    Function to display all student details from the database.
    """
    qy = "SELECT * FROM student"
    
    try:
        my_cursor.execute(qy)
        my_result = my_cursor.fetchall()
        print("____Record____")
        for i in my_result:
            print(i)
    except TypeError:
        pass

if __name__ == "__main__":
    while True:
        print("\n ------------WELCOME TO THE STUDENT MANAGEMENT SYSTEM------------\n ")
        print("\t\t=======================")
        print('''\nEnter the operation you want to perform
                1. Add new Student
                2. Search a Student
                3. Display all Student Details
                4. Update Details
                5. Delete a Student Detail
                6. Exit''')
        choice = int(input("\n\nEnter the choice [1/2/3/4/5/6]: "))
        
        while choice not in [1, 2, 3, 4, 5, 6]:
            print("\nOops, that seems to be an invalid choice!!")
            choice = int(input("\n\nEnter the choice [1/2/3/4/5/6]: "))
        
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
