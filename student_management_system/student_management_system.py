import mysql.connector
from tkinter import *
from tkinter import messagebox

# Establishing the connection to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Brijesh@1610',
    database='student',
    auth_plugin='mysql_native_password'
)
my_cursor = conn.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS student (Name VARCHAR(255), Roll INT PRIMARY KEY, Branch VARCHAR(255), Dept VARCHAR(255))")


def create_stud():
    name = name_entry.get()
    rn = roll_entry.get()
    branch = branch_entry.get()
    department = dept_entry.get()

    qy = "INSERT INTO student (Name, Roll, Branch, Dept) VALUES (%s, %s, %s, %s)"
    val = (name, rn, branch, department)

    try:
        my_cursor.execute(qy, val)
        conn.commit()
        messagebox.showinfo("Success", "Values inserted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


def search_stud():
    rn = search_entry.get()
    qy = "SELECT * FROM student WHERE Roll = %s"
    rl = (rn,)
    try:
        my_cursor.execute(qy, rl)
        myresult = my_cursor.fetchall()
        result_text.delete('1.0', END)
        for i in myresult:
            result_text.insert(END, f"{i}\n")
        conn.commit()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


def delete_stud():
    rn = delete_entry.get()
    qy = "DELETE FROM student WHERE Roll = %s"
    rl = (rn,)
    try:
        my_cursor.execute(qy, rl)
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


def update_stud():
    roll = update_roll_entry.get()
    update_choice = update_choice_var.get()
    new_value = update_value_entry.get()

    try:
        if update_choice == 'Name':
            qy = "UPDATE student SET Name = %s WHERE Roll = %s"
        elif update_choice == 'Roll':
            qy = "UPDATE student SET Roll = %s WHERE Roll = %s"
        elif update_choice == 'Branch':
            qy = "UPDATE student SET Branch = %s WHERE Roll = %s"
        elif update_choice == 'Dept':
            qy = "UPDATE student SET Dept = %s WHERE Roll = %s"

        val = (new_value, roll)
        my_cursor.execute(qy, val)
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


def display_stud():
    qy = "SELECT * FROM student"
    try:
        my_cursor.execute(qy)
        my_result = my_cursor.fetchall()
        result_text.delete('1.0', END)
        for i in my_result:
            result_text.insert(END, f"{i}\n")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


# GUI setup
root = Tk()
root.title("Student Management System")

# Add new student
Label(root, text="Add New Student").grid(row=0, column=0, columnspan=2)

Label(root, text="Name:").grid(row=1, column=0)
name_entry = Entry(root)
name_entry.grid(row=1, column=1)

Label(root, text="Roll:").grid(row=2, column=0)
roll_entry = Entry(root)
roll_entry.grid(row=2, column=1)

Label(root, text="Branch:").grid(row=3, column=0)
branch_entry = Entry(root)
branch_entry.grid(row=3, column=1)

Label(root, text="Dept:").grid(row=4, column=0)
dept_entry = Entry(root)
dept_entry.grid(row=4, column=1)

Button(root, text="Add Student", command=create_stud).grid(row=5, column=0, columnspan=2)

# Search student
Label(root, text="Search Student by Roll").grid(row=6, column=0, columnspan=2)

search_entry = Entry(root)
search_entry.grid(row=7, column=0)

Button(root, text="Search", command=search_stud).grid(row=7, column=1)

# Display all students
Button(root, text="Display All Students", command=display_stud).grid(row=8, column=0, columnspan=2)

# Delete student
Label(root, text="Delete Student by Roll").grid(row=9, column=0, columnspan=2)

delete_entry = Entry(root)
delete_entry.grid(row=10, column=0)

Button(root, text="Delete", command=delete_stud).grid(row=10, column=1)

# Update student
Label(root, text="Update Student Details").grid(row=11, column=0, columnspan=2)

Label(root, text="Roll:").grid(row=12, column=0)
update_roll_entry = Entry(root)
update_roll_entry.grid(row=12, column=1)

update_choice_var = StringVar()
update_choice_var.set('Name')
update_choice_menu = OptionMenu(root, update_choice_var, 'Name', 'Roll', 'Branch', 'Dept')
update_choice_menu.grid(row=13, column=0)

update_value_entry = Entry(root)
update_value_entry.grid(row=13, column=1)

Button(root, text="Update", command=update_stud).grid(row=14, column=0, columnspan=2)

# Results display
result_text = Text(root, height=10, width=50)
result_text.grid(row=15, column=0, columnspan=2)

root.mainloop()
