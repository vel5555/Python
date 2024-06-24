##initial setting (database)
import mysql.connector
con_o=mysql.connector.connect(host="localhost",user="root",password="",database="placement_details")
cur_o=con_o.cursor()



###actual code (querying)
op=0
while op!=5:
    print("Enter the numbers to perform their corresponding operation:\n 1 - For printing the description of the table \n 2 - For Inserting details in table \n 3 - For showing contents in table \n 4 - For empting the table \n 5 - Closing the application\n")
    print("\t\t############################")
    print("Enter your option :-\noption : ",end="")
    try:
        op=int(input())
    except ValueError:
        print("op can only be numbers str is not accepted\n")
    ##description of table
    else:
        if(op==1):
            q1="desc students"
            cur_o.execute(q1)
            table=cur_o.fetchall()
            print("\n\tTable Description")
            for atr in table:
                print(atr)
            print("\n\t---------------------end----------------\n")

        #detail for insertion
        elif op==2:
            print("\tEnter details:-")
            name=input("Name: ")
            gender=input("gender: ")
            depart=input("Department: ")
            cgp=float(input("CGPA: "))
            attend=float(input("attendence: "))

            #insert code
            q2=f"INSERT INTO `s_details`(`name`, `department`, `CGPA`, `gender`, `attendence`) VALUES ('{name}','{depart}',{cgp},'{gender}',{attend})"
            cur_o.execute(q2)
            con_o.commit()
            #
            
        #showing content
        elif op==3:
            print("\n\tRecords in the table")
            q3="SELECT * from s_details"
            cur_o.execute(q3)
            rows=cur_o.fetchall()
            print(*rows,sep="\n")
            print("\n\t---------------------end----------------\n")
            
        elif op==4:
            #code for deleting all the rows to get a new table
            truncate_query = "TRUNCATE TABLE s_details"
            cur_o.execute(truncate_query)
            con_o.commit()
            #end

##ending steps
cur_o.close()
con_o.close()