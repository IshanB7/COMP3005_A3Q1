import psycopg

# connecting to postgres, change connection parameters if needed
with psycopg.connect("dbname=COMP3005 user=postgres password=student host=localhost port=5433") as connection:
    with connection.cursor() as cursor:

        # querying for all students in database
        def getAllStudents():
            cursor.execute("SELECT * FROM students")
            for record in cursor:
                print(record)

        # adding a student
        def addStudent():
            try:
                fname = input("First name: ")
                lname = input("Last name: ")
                email = input("Email: ")
                enroll_date = input("Enrollment Date (YYYY-MM-DD): ")

                if (fname == "" or lname == "" or email == ""):
                    raise ValueError("CANNOT HAVE EMPTY STRING")

                # executing the query based on user input
                cursor.execute("""
                    INSERT INTO students (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s)
                """, (fname, lname, email, enroll_date))
                connection.commit()
            except Exception as e:
                print("Error: ", e)

        # updating the email for an existing student
        def updateStudentEmail():
            try:
                id = input("Student id: ")
                new_email = input("New email: ")

                if (id == "" or new_email == ""):
                    raise ValueError("CANNOT HAVE EMPTY STRING")

                # executing the query based on user input
                cursor.execute("UPDATE students SET email=%s WHERE student_id=%s", (new_email, id))
                connection.commit()
            except Exception as e:
                print("Error: ", e)

        # deleting an existing student
        def deleteStudent():
            try:
                id = input("Student id: ")
                
                if (id == ""):
                    raise ValueError("CANNOT HAVE EMPTY STRING")
                
                # executing the query based on user input
                cursor.execute("DELETE FROM students WHERE student_id=%s", (id,))
                connection.commit()
            except Exception as e:
                print("Error: ", e)

        flag = True
        # ask user for input and call corresponding function
        while flag:
            print("\n1. getAllStudent()")
            print("2. addStudent(first_name, last_name, email, enrollment_date)")
            print("3. updateStudentEmail(student_id, new_email)")
            print("4. deleteStudent(student_id)")
            print("5. exit")

            choice = input("\nEnter a number: ")
            if len(choice) > 1:
                choice = choice[0]

            match choice:
                case '1':
                    getAllStudents()
                case '2':
                    addStudent()
                case '3':
                    updateStudentEmail()
                case '4':
                    deleteStudent()
                case '5':
                    flag = False