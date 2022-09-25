import math
import matplotlib.pyplot as pt
import numpy as np
from tkinter import*                                      #GO TO LINE 636 TO CONTINUE
from tabulate import tabulate
real_name=""
import mysql.connector as sqltor

mycon=sqltor.connect( host="localhost", database="calculator", user="root", password="yashtarush")
if mycon.is_connected()==False:
    print("Error connecting to mysql database")
    
cursor = mycon.cursor(buffered=True)
    
print("Welcome to Calculator. ")
print("Enter 'NEW' if you are a new user and 'OLD' if u are an existing user")
j=input()
if (j.upper().strip()) == "NEW":
    ty=0
    print("Enter a username ")
    while(ty==0):
        username=input().strip()
        query=("SELECT count(*) FROM cal_hist WHERE NAME='%s'")
        cursor.execute("SELECT count(*) FROM cal_hist WHERE NAME='%s'"%username)
        l=cursor.fetchall()
        print(l)

        if l[0][0] == 0:
            ty=1
            real_name = username
        else:
            print("This username already exists ")
            print("Enter a different username")
            
elif (j.upper().strip())=="OLD":
    ty2=0 
    print("Enter a username")
    while (ty2==0):
        
        username1=input().strip()
        cursor.execute("SELECT count(*) FROM cal_hist WHERE NAME='%s'"%username1)
        l=cursor.fetchall()
        if l[0][0]==0:
            print("Account does not exist")
            print("Enter '1' if you want to enter a different username or '2' to create a new account")
            kip=int(input())
            if kip==1:
                print("Enter a username ")
                continue
            elif kip==2:
                ty=0
                print("Enter a username ")
                while(ty==0):
                    username=input().strip()
                    cursor.execute("SELECT count(*) FROM cal_hist WHERE NAME='%s'"%username)
                    l2=cursor.fetchall()

                    if l2[0][0] != 0:
                        print("This username already exists ")
                        print("Enter a different username")
                    else:
                        ty=1
                        real_name = username
                
                ty2=1
                continue
            else:
                print("How dumb can u be")
                print("Enter a username")
                continue

        else:
            print("Account Found")
            real_name=username1
            ty2=1
            continue
else:
    print("U HAVE MADE A MISTAKE ")
quit_var = 0

while (quit_var != 1 and real_name!=""):
    result = 0.0

    print("As you know our calculator has many features. To choose the function you want to do. Write the index number given beside the operation. Enter the operation you want to do?")
    print("1. BASIC Calculator")
    print("2. Calculator for MATHEMATICAL FUNCTION operations")
    print("3. Co-ordinate Geometry related equation solving")
    print("4. Vector Algebra")
    print("5. Graphing Calculator")
    print("6. Find Derivatives of function")
    print("7. Temperature Converter")
    print("8. CURRENCY convertor")
    print("9. Check your previous history")

    main_choice = int(input())
    if main_choice ==1:
        myWindow=Tk()
        myWindow['bg']="white"
        myWindow.title("Basic Calculator")
        myWindow.geometry('900x450')
        print("Your BASIC CALCULATOR GUI has opened")

        def findSum():
            a=int(No1.get())
            b=int(No2.get())
            c=a+b
            ans.delete(0,END)
            ans.insert(0,str(c))
            str1=str(a)+" and "+str(b)
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"ADDITION",str(c)))
            mycon.commit()
           
        def findDifference():
            a=int(No1.get())
            b=int(No2.get())
            c=a-b
            ans.delete(0,END)
            ans.insert(0,str(c))
            str1=str(a)+" and "+str(b)
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"SUBTRACTION",str(c)))
            mycon.commit()

        def findProduct():
            a=int(No1.get())
            b=int(No2.get())
            c=a*b
            ans.delete(0,END)
            ans.insert(0,str(c))
            str1=str(a)+" and "+str(b)
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"MULTIPLICATION",str(c)))
            mycon.commit()
            
        def finddivision():
            a=int(No1.get())
            b=int(No2.get())
            c=a/b
            ans.delete(0,END)
            ans.insert(0,str(c))
            str1=str(a)+" and "+str(b)
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"DIVISION",str(c)))
            mycon.commit()

        Label(myWindow,text="Basic Operations", padx=100, pady=25, bg='red', fg='blue', bd=5, relief='raised', font='system').grid(row=0,column=1)

        Label(myWindow,text="Enter Your First Number", padx=50, pady=15, bg='white').grid(row=1,column=0)
        No1=Entry(myWindow,width=15)
        No1.grid(row=1,column=1)

        Label(myWindow,text="Enter Your Second Number", padx=42, pady=15, bg='white').grid(row=2,column=0)

        No2=Entry(myWindow,width=15)
        No2.grid(row=2,column=1)

        Label(myWindow,text="Here Is Your Answer", padx=65, pady=15, bg='white').grid(row=3,column=0)
        Label(myWindow,text="Which operation do you need to perform? Click on that.", padx=10, pady=15, bg='white', fg="blue").grid(row=5,column=0)
        ans=Entry(myWindow,width=15)
        ans.grid(row=3,column=1)


        Button(myWindow,text="Sum",padx=35,pady=13, command=findSum, bg='light green').grid(row=4,column=1)
        Button(myWindow,text="Difference",padx=20,pady=13, command=findDifference, bg='light green').grid(row=5,column=1)
        Button(myWindow,text="Product",padx=26,pady=13, command=findProduct, bg='light green').grid(row=6,column=1)
        Button(myWindow,text="Division",padx=26,pady=13, command=finddivision, bg='light green').grid(row=7,column=1)


        mainloop()

    elif main_choice == 2:
        def Addition(a):
            sum1 = 0
            str1=""
            for i in range(0,a):
                b = int(input("Enter the number to be added"))
                str1=str(b)+" and "+str1
                sum1 = sum1 + b
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"ADDITION",str(sum1)))
            mycon.commit()   
            return sum1    

        def Multiplication(a):
            prod = 1
            str1=""
            for i in range(0,a):
                b = int(input("Enter the number to be multiplied"))
                str1=str1+" and "+str(b)
                prod = prod * b
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"MULTIPLICATION",str(prod)))
            mycon.commit()
            return prod

        quit_var = 0

        while (quit_var != 1):
            result = 0.0
            
            print("Enter the operation you want to do?")
            print("1. X raised to Y")
            print("2. Square Root")
            print("3. Natural Lograthim(base = e)")
            print("4. Lograthim of any base")
            print("5. Factorial")
            print("6. Greatest Integer Function [x]")
            print("7. Fractional Part of X {x}")
            print("8. Radian to Degree")
            print("9. Degree to Radians")
            print("10. Sine of angle ")
            print("11. Cosine of angle ")
            print("12. Tangent of angle ")
            print("13. Arc Sine of angle ")
            print("14. Arc Cosine of angle ")
            print("15. Arc Tangent of angle ")
            
            choice = int(input())

            if choice == 1 :
                a = float(input("Enter the 1st number"))
                b = float(input("Enter the second number"))
                result = a**b
                print (result)
                str1=str(a)+" and "+str(b)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"X RAISED TO Y",str(result)))
                mycon.commit()
                

            elif choice == 2 :
                a = float(input("Enter the number"))
                result = math.sqrt(a)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"SQUARE ROOT",str(result)))
                mycon.commit()
                
            elif choice == 3 :
                a = float(input("Enter the number"))
                result = math.log1p(a)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"NATURAL LOGARITHM",str(result))) 
                mycon.commit() 

            elif choice == 4 :
                a = float(input("Enter the number"))
                b = float(input("Enter the base number"))
                result = math.log(a, b)
                print (result)
                str1=str(a)+" and "+str(b)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"LOGARITHM WITH BASE",str(result)))  
                mycon.commit()
            elif choice == 5 :
                a = float(input("Enter the number"))
                result = math.factorial(a)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"FACTORIAL",str(result))) 
                mycon.commit()
            elif choice == 6 :
                a = float(input("Enter the number"))
                result = math.floor(a)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"GREATEST INT FUNC",str(result))) 
                mycon.commit()
            elif choice == 7 :
                a = float(input("Enter the number"))
                result = abs(math.floor(a)-a)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"FRACTIONAL PART ",str(result))) 
                mycon.commit()
            elif choice == 8 :
                a = float(input("Enter the angle in radian"))
                result = math.degrees(a)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"RADIANS TO DEGREE",str(result))) 
                mycon.commit()
            elif choice ==9 :
                a = float(input("Enter the angle in degree"))
                result = math.radians(a)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"DEGREE TO RADIANS",str(result))) 
                mycon.commit()
            elif choice == 10 :
                a = float(input("Enter the angle in degree"))
                b= a/(57.2958)
                result = math.sin(b)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"SINE OF ANGLE",str(result))) 
                mycon.commit()
            elif choice == 11 :
                a = float(input("Enter the angle in degree"))
                b= a/(57.2958)
                result = math.cos(b)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"COSINE OF ANGLE",str(result))) 
                mycon.commit()
            elif choice == 12 :
                a = float(input("Enter the angle in degree"))
                b= a/(57.2958)
                result = math.tan(b)
                print (result)
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"TAN OF ANGLE",str(result)))  
                mycon.commit()

            elif choice == 13 :
                a = float(input("Enter the number "))
                result = math.asin(a) * (180/ math.pi)
                print (result," degree")
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"ARC SINE OF ANGLE",str(result))) 
                mycon.commit()
            elif choice == 14 :
                a = float(input("Enter the number"))
                result = math.acos(a) * (180 / math.pi)
                print (result," degree")
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"ARC COSINE OF ANGLE",str(result))) 
                mycon.commit()
            elif choice == 15 :
                a = float(input("Enter the number"))
                result = math.atan(a) * (180/math.pi)
                print (result," degree")
                str1=str(a)
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"ARC TAN OF ANGLE",str(result))) 
                mycon.commit()
                
            else:
                print("Please choose from the list above")

            print("THE Calculator for scientific operations IS OVER")
            quit_var = int(input("Enter 1 to quit, any other digit to continue"))

    elif main_choice == 3:
        print("Welcome to Co-ordinate Geometry equation calculator!")
            

        quit_var = 0

        while (quit_var != 1):
            result = 0.0

            print("Enter the shape you want to operate on:")
            print("1. Parabola")
            print("2. Ellipse")
            print("3. Hyperbola")
            print("4. Circle")

            scd_choice = int(input())

            if scd_choice == 1:
                def eqnparabola():
                    print("Enter 1 if ur major axis is x and 2 if ur major axis is y :  ")
                    maxis=int(input())
                    a=eval(input("Enter the coordinates of the focus eg- '(5,0)': "))
                    if maxis==1:
                        print("The equation is : y^2=",4*a[0],"x")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axis,focus","EQN OF PARABOLA","The equation is : y^2="+str(4*a[0])+"x"))
                        mycon.commit()
                    elif maxis==2:
                        print("The equation is : x^2=",4*a[0],"y")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axis,focus","EQN OF PARABOLA","The equation is : x^2="+str(4*a[0])+"y"))
                        mycon.commit()
                    else :
                        print("No such axis is present")
        
                   
                    
    

                def paradirectrix():
                    print("enter 1 if ur major axis is x and 2 if ur major axis is y ")
                    maxis=int(input())
                    a=eval(input("Enter the coordiantes of the focus eg- '(5,0)': "))
                    if maxis==1:
                        print("The equation of directrix is : x=",-a[0])
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axis,focus","EQN OF DIRECTRIX","The equation is : x^="+str(-a[0])))
                        mycon.commit()
                    elif maxis==2:
                        print("The equation of directrix is : y=",-a[1])
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axis,focus","EQN OF DIRECTRIX","The equation is : y="+str(-a[1])))
                        mycon.commit()
                    else :
                        print("No such axis is present")
                    

                def LRparabola():
                    a=float(input("Enter the lenght of the focus from the vertex"))
                    print ("The lenght of the latus rectum is : ",4*a)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"lenght of focus from vertex","LEN OF LATUS RECTUM","lenght of latus rectum is :"+str(4*a)))
                    mycon.commit()

                def ptcheckparabola():
                    print("Enter 1 if ur major axis is x and 2 if ur major axis is y :  ")
                    maxis=int(input())
                    a=eval(input("Enter the coordinates of the focus eg- '(5,0)': "))
                    pt=eval(input("Enter the coordinates of the point to be checked : "))
                    lhs=0
                    rhs=0
                    if maxis==1:
                        lhs=pt[1]**2
                        rhs=4*a[0]*pt[0]
                    elif axis==2:
                        lhs=pt[0]**2
                        rhs=4*a[1]*pt[1]
                    else:
                        print("no such axis is present ")
                        
                    if lhs-rhs==0:
                        print("the point lies on the parabola")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axes,focus,pt to be checked","POSITION OF PT","LIES ON THE PARABOLA"))
                        mycon.commit()

                    elif lhs-rhs<0:
                        print("the point lies inside the parabola")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axes,focus,pt to be checked","POSITION OF PT","LIES IN THE PARABOLA"))
                        mycon.commit()

                    else:
                        print("the point lies outside the parabola")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axes,focus,pt to be checked","POSITION OF PT","LIES OUTSIDE THE PARABOLA"))
                        mycon.commit()



                def shiftparabola():
                    print("Enter 1 if ur major axis is x and 2 if ur major axis is y :  ")
                    maxis=int(input())
                    a=eval(input("Enter the coordinates of the focus eg- '(5,0)': "))
                    v=eval(input("Enter the new vertex of the parabola : "))
                    if maxis==1 :
                        print("The shifted equation of the parabola is : y^2 + (",(-1*4*a[0]),"x) + (",v[1]**2+4*a[0]*v[0],") + (",(-1*2*v[1]),"y) = 0")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axes,focus,new vertex","shifted parabola eqn","The shifted equation of the parabola is : y^2 + ("+str(-1*4*a[0])+"x) + ("+str(v[1]**2+4*a[0]*v[0])+") + ("+str(-1*2*v[1])+"y) = 0"))
                        mycon.commit()           
                    elif axis==2 :
                        print("The shifted equation of the parabola is : x^2 + (",(-1*4*a[1]),"y) + (",v[0]**2+4*a[1]*v[1],") + (",(-1*2*v[0]),"x) = 0")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"axes,focus,new vertex","shifted parabola eqn","The shifted equation of the parabola is : x^2 + ("+str(-1*4*a[1])+"y) + ("+str(v[0]**2+4*a[1]*v[1])+") + ("+str(-1*2*v[0])+"x) = 0"))
                        mycon.commit()
                    else:
                        print("No such axis is present ")
                quit_var = 0

                while (quit_var != 1):
                    result = 0.0
                    print(" Enter the operation you want to do :")
                    print("1: Calculate the standard equation of a parabola")
                    print("2: Calculate the equation of the directrix of the standard parabola")
                    print("3: Calculate the the lenght of the Latus Rectum")
                    print("4: Check the position of the point with respect to the parabola ")
                    print("5: Calculate the equation of a parabola after shifting its vertex")
                    choice=int(input())

                    if choice==1:
                        eqnparabola()
                        
                    elif choice ==2:
                        paradirectrix()
                        
                        
                    elif choice==3:
                        LRparabola()
                        
                        

                    elif choice==4:
                        ptcheckparabola()
                    

                    elif choice==5:
                        shiftparabola()
                        

                    else:
                        print("Please choose from the list above")

                    print("THE Calculator for PARABOLA IS OVER")
                    quit_var = int(input("Enter 1 to quit, any other digit to continue"))


            elif scd_choice == 2:
                def eqnellipse():
                        print("Enter 1 if ur major axis is x and 2 if ur major axis is y")
                        maxis = int(input())
                        a = int(input("Enter the length of the major axis"))
                        b = int(input("Enter the lenght of the minor axis"))
                        if maxis == 1:
                            print("The equation is: x^2/",(a/2)**2, " + y^2/",  (b/2)**2 , "= 1")
                            S= "x^2/"+str((a/2)**2)+ " + y^2/"+  str((b/2)**2) + "= 1"
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"LENGHT OF MAJOR AND MINOR AXIS","EQN OF ELLIPSE",S))
                            mycon.commit()
                        elif maxis == 2:
                            print("The equation is: y^2/", (a/2)**2, "+ x^2/" ,(b/2)**2, "= 1")
                            S= "y^2/"+str( (a/2)**2)+ "+ x^2/" +str((b/2)**2)+ "= 1"
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"LENGHT OF MAJOR AND MINOR AXIS","EQN OF ELLIPSE",S))
                            mycon.commit()
                        else:
                            print("No such axis is present")    
                                
                def eccentricity():
                        print("Enter 1 f u know focus and length of major axis and 2 if u know length of minor axis and lenght of major axis")
                        option = int(input())
                        if option ==1:
                            print("Enter value of focus eg - '(O,5)'")
                            focus = eval(input())
                            print("Enter lenght of the major axis")
                            lmaxis = (int(input()))/2
                            ecc = 0.0
                            if focus [0] == 0:
                                ecc=(focus[1]/lmaxis)
                            else:
                                ecc = (focus[0]/lmaxis)
                            print("Eccentricity is:",ecc)
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"AXIS,LENGHT OF MAJOR AXIS","ECCENTRICITY",str(ecc)))
                            mycon.commit()
                            
                        elif option==2:
                            lmaxis=(int(input("Enter lenght of major axis")))/2
                            lmiaxis=(int(input("Enter lenght of minor axis")))/2
                            c=math.sqrt((lmaxis)**2-(lmiaxis)**2)
                            ecc=float(c/lmaxis)
                            print("Eccentricity is:",ecc)
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"LENGHT OF MAJOR AND MINOR AXIS","ECCENTRICITY",str(ecc)))
                            mycon.commit()
                        else:
                            print("No such option present")
                            
                def LRellipse():
                    
                    lmaxis=(int(input("Enter lenght of major axis")))/2
                    lmiaxis=(int(input("Enter lenght of minor axis")))/2
                    LR=2*(lmiaxis)**2/(lmaxis)
                    print("The lenght of latus rectum is:",LR)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"lenght of major and minor axis","LENGHT OF LATUS RECTUM",str(LR)))
                    mycon.commit()

                    
                quit_var=0
                while(quit_var!=1):
                    print("Enter the operation you want to do :")
                    print("1.Calculate the standard equation of an ellipse")
                    print("2.Calculate the eccentricity of an ellipse")
                    print("3.Calculate the lenght of latus rectum")
                    choice=int(input())
                    if choice==1:
                        eqnellipse()
                        
                    elif choice==2:
                        eccentricity()
                        
                    elif choice==3:
                        LRellipse()
                        
                            
                    else:
                        print("Please choose from the list above")
                    print("THE Calculator for ELLIPSE IS OVER")        
                    quit_var=int(input("Enter 1 to quit, any other digit to continue"))


            elif scd_choice == 3:
                def eqnhyperbola():
                    print("If x-axis is major axis enter 1 and if y-axis is major axis then enter 2")
                    maxis = int(input())
                    print("If you want to enter the lenght of major axis and eccentricity then enter 1, else if you want to enter the length of major and minor axis enter 2 ")
                    option = int(input())
                    if option == 1:
                        print("Enter length of major axis")
                        a = (float(input()))/2
                        print("Enter the eccentricity")
                        e = float(input())
                        b = a**2*(e**2-1)
                        if maxis == 1:
                            print("The equation is x^2/",(a**2),"-y^2/",(b**2))
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"AXIS,ECCENTRICITY,LEN OF MAJOR AXIS","EQN OF HYPERBOLA","x^2/"+str(a**2)+"-y^2/"+str(b**2)))
                            mycon.commit()
                        elif maxis == 2:
                            print("The equation is y^2/",(a**2),"-x^2/",(b**2))
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"AXIS,ECCENTRICITY,LEN OF MAJOR AXIS","EQN OF HYPERBOLA","y^2/"+str(a**2)+"-x^2/"+str(b**2)))
                            mycon.commit()
                        else:
                            print("Invalid axis")
                    elif option == 2:
                        print("Enter length of major axis")
                        a = (float(input()))/2
                        print("Enter length of minor axis")
                        b = (float(input()))/2
                        if maxis == 1:
                            print("The equation is x^2/",(a**2),"-y^2/",(b**2))
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"AXIS,LEN OF MAJOR and minor AXIS","EQN OF HYPERBOLA","x^2/"+str(a**2)+"-y^2/"+str(b**2)))
                            mycon.commit()
                        elif maxis == 2:
                            print("The equation is y^2/",(a**2),"-x^2/",(b**2))
                            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"AXIS,LEN OF MAJOR and minor AXIS","EQN OF HYPERBOLA","y^2/"+str(a**2)+"-x^2/"+str(b**2)))
                            mycon.commit()
                        else:
                            print("Invalid axis")
                    else:
                        print("Your choice was invalid")

                def ecchyperbola():
                    print("To calculate the eccentricity using focus and length of major axis, enter 1 else if you want to calculate using length off major axis and minor axis, enter 2")
                    option = int(input())
                    if option == 1:
                        print("Enter the focus, eg:- (0,5)")
                        f = eval(input())
                        print("Enter the length of the major axis:")
                        a = float(input())
                        e=0
                        if f[0] != 0:
                            e = (f[0]/a)*2
                        else:
                            e = (f[1]/a)*2 
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"FOCUS,LEN OF MAJOR AXIS","ECCENTRICITY",str(e)))
                        mycon.commit()
                    elif option == 2:
                        print("Enter the length of major axis:")
                        a = (float(input()))/2
                        b = (float(input()))/2
                        e = math.sqrt (1 + (b**2)/(a**2))
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"LEN OF MAJOR AND MINOR AXIS","ECCENTRICITY",str(e)))
                        mycon.commit()
                    else:
                        print("Incorrect option")
                def LRhyperbola():
                    print("Enter length of major axis:")
                    a = float(input())
                    print("Enter length of minor axis:")
                    b = float(input())
                    LR = (2*(b**2))/a
                    print("The length of Latus Rectum:",LR)
                    #U WERE HERE
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"lenght of major AND minor axis","LEN OF LATUS RECTUM",str(LR)))
                    mycon.commit()    


                quit_var = 0
                while(quit_var != 1):
                    print("Enter the operation you want to do:")
                    print("1.Calculate the standard equation of hyperbola")
                    print("2.Calculate the eccentricity of hyperbola")
                    print("3.Calculate the length of Latus Rectum of hyperbola")
                    choice = int(input())
                    if choice == 1:
                        eqnhyperbola()

                        
                    elif choice == 2:
                        ecchyperbola()
                        
                    elif choice == 3:
                        LRhyperbola()
                        
                    else:
                        print("Please choose from the list above")
                    print("THE Calculator for HYPERBOLA IS OVER")
                    quit_var = int(input("Enter 1 to quit, any other digit to continue"))


            elif scd_choice == 4:
                def area():
                    r=float(input("Enter radius"))
                    print(3.14*r*r)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius","Area of circle",str(3.14*r*r)))
                    mycon.commit()
                def perimeter():
                    r=float(input("Enter radius"))
                    print(2*3.14*r)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius","Perimeter of circle",str(2*3.14*r)))
                    mycon.commit()

                def pointloc():
                    p=float(input("Enter x coordinate of centre of circle:"))
                    q=float(input("Enter y coordinate of centre of circle:"))
                    s=float(input("Enter x coordinate of point:"))
                    t=float(input("Enter y coordinate of point:"))
                    r=float(input("Enter radius of circle:"))
                    c=(s-p)*(s-p) + (t-q)*(t-q)
                    if c<r*r:
                        print("Point inside circle")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius,coordinate of point,coordinate of center of circle","The point is inside circle"))
                        mycon.commit()
                    elif c==r*r:
                        print("Point on circle")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius,coordinate of point,coordinate of center of circle","The point is on the circle"))
                        mycon.commit()
                    elif c>r*r:
                        print("Point lies outside circle")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius,coordinate of point,coordinate of center of circle","The point is outside the circle"))
                        mycon.commit()
                def circleradiuscheck():
                    g=float(input("Enter x coordinate of centre of circle:"))
                    f=float(input("Enter y coordinate of centre of circle:"))
                    c=float(input("Enter constant in equation of circle:"))
                    r=float(input("Enter radius of circle:"))
                    if ((g*g+f*f-c)>0):
                        print("The radius of the circle is real and hence the circle is also real.")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius,coordinate of point,coordinate of center of circle","Radius Check","The radius is real"))
                        mycon.commit()
                    elif ((g*g+f*f-c)==0):
                        print("The radius of the circle is 0 and the circle is known as point circle.")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius,coordinate of point,coordinate of center of circle","Radius Check","The radius is 0"))
                        mycon.commit()
                    elif ((g*g+f*f-c)<0):
                        print("The radius of the circle is imaginary. Such a circle is imaginary, which is not possible to draw.")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius,coordinate of point,coordinate of center of circle","Radius Check","The radius is imaginary"))
                        mycon.commit()
                    

                def eqnofcircle():
                    p=float(input("Enter x coordinate of centre of circle:"))
                    q=float(input("Enter y coordinate of centre of circle:"))
                    r=float(input("Enter radius of circle:"))
                    print("Equation of circle is:", "(x-",p,")^2 + (y-",q,")^2 =", r*r)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"radius,coordinate of center of circle","EQN of Circle","x-"+str(p)+")^2 + (y-"+str(q)+")^2 ="+str( r*r)))
                    mycon.commit()

                def diametriceqnofcircle():
                    p=float(input("Enter x coordinate of point 1:"))
                    q=float(input("Enter y coordinate of point 1:"))
                    s=float(input("Enter x coordinate of point 2:"))
                    t=float(input("Enter y coordinate of point 2:"))
                    print("(x-",p,")(x-",s,")+(y-",q,")(y-",t,") = 0")
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Coordinates of two points","Dimetric EQN of Circle","(x-"+str(p)+")(x-"+str(s)+")+(y-"+str(q)+")(y-"+str(t)+") = 0"))
                    mycon.commit()

                def findradius():
                    p=float(input("Enter x coordinate of centre of circle:"))
                    q=float(input("Enter y coordinate of centre of circle:"))
                    c=float(input("Enter constant in equation of circle"))
                    r=math.sqrt(p*p+q*q -c)
                    print(r)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Centre of circle,Constant","Finding Radius",str(r)))
                    mycon.commit()

                def xinterc():
                    g=float(input("Enter x coordinate of centre of circle:"))
                    c=float(input("Enter constant in equation of circle:"))
                    z=2*(math.sqrt(g*g-c))
                    print(z)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Centre of circle,Constant","X intercept of Circle",str(z)))
                    mycon.commit()
                    

                def yinterc():
                    f=float(input("Enter y coordinate of centre of circle:"))
                    c=float(input("Enter constant in equation of circle"))
                    z=2*(math.sqrt(f*f-c))
                    print(z)
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Centre of circle,Constant","Y intercept of Circle",str(z)))
                    mycon.commit()
                    

                def eqnoftangents():
                    g=float(input("Enter x coordinate of centre of circle:"))
                    f=float(input("Enter y coordinate of centre of circle:"))
                    c=float(input("Enter constant in equation of circle:"))
                    m=float(input("Enter slope to circle:"))
                    print("y-",f,"=",m,"(x-",g,")+",math.sqrt((g*g+f*f-c)*(1+m*m)))
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Centre of circle,Constant,slope of tangent","EQN of tangent to Circle","y-"+str(f)+"="+str(m)+"(x-"+str(g)+")+"+str(math.sqrt((g*g+f*f-c)*(1+m*m)))))
                    mycon.commit()

                def eqnofnormal():
                    g=float(input("Enter x coordinate of centre of circle:"))
                    f=float(input("Enter y coordinate of centre of circle:"))
                    s=float(input("Enter x coordinate of point:"))
                    t=float(input("Enter y coordinate of point:"))
                    print("y-",t,"=[(",t-f,")(x-",s,")]/(",s-g,")(",t-f,")x-(",s-g,")y+(",g*t-f*s,") = 0")
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Centre of circle,Coordinates of point","EQN of normal to Circle","y-"+str(f)+"="+str(m)+"(x-"+str(g)+")+"+str(math.sqrt((g*g+f*f-c)*(1+m*m)))))
                    mycon.commit()

                def eqnofpot():
                    p=float(input("Enter x coordinate of point"))
                    q=float(input("Enter y coordinate of point"))
                    r=float(input("Enter radius of circle:"))
                    print("(x^2+y^2-",r*r,")(",p*p+q*q-r*r,")=(x",p,"+y",q,"-",r*r,")^2")
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Radius,Coordinates of point","Pair of tangents","(x^2+y^2-"+str(r*r)+")("+str(p*p+q*q-r*r)+")=(x"+str(p)+"+y"+str(q)+"-"+str(r*r)+")^2"))
                    mycon.commit()

                def angintersection():
                    k=float(input("Enter radius of circle 1:"))
                    j=float(input("Enter radius of circle 2:"))
                    d=float(input("Enter distance between centres of circles:"))
                    print(math.acos((k*k+j*j-d*d)/(2*k*j)))
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Radius of circles,Distances between centres of circles","Angle of intersection",str(math.acos((k*k+j*j-d*d)/(2*k*j)))))
                    mycon.commit()
                    

                def checkortho():
                    g=float(input("Enter x coordinate of centre of circle 1:"))
                    f=float(input("Enter y coordinate of centre of circle 1:"))
                    c=float(input("Enter constant in equation of circle 1:"))
                    j=float(input("Enter x coordinate of centre of circle 2:"))
                    k=float(input("Enter y coordinate of centre of circle 2:"))
                    h=float(input("Enter constant in equation of circle 2:"))
                    if (2*g*j+2*f*k==c+h):
                        print("Orthogonal circles")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Coordinates od Circle 1,coordinates of circle 2,constant1,constan2","Checking for orthogonal","Orthogonal Circles"))
                        mycon.commit()
                    else:
                        print("Not orthogonal circles")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Coordinates od Circle 1,coordinates of circle 2,constant1,constant2","Checking for orthogonal","not Orthogonal Circles"))
                        mycon.commit()

                def famcircles():
                    a=int(input("Enter 1 for circle and line, enter 2 for circle and point, enter 3 for two circles"))
                    if a==1:
                        c=input("Enter equation of Circle")
                        l=input("Enter equation of Line")
                        print(c,"+ LAMBDA(", l,") =0")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"EQN of circle and line","Family of circles",c+"+ LAMBDA("+ l+") =0"))
                        mycon.commit()
                        
                    elif a==2:
                        n=input("Enter equation of Circle")
                        m=input("Enter equation of Tangent at required point to circle")
                        print(n,"+ LAMBDA(", m,") =0")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"EQN of circle and tangent","Family of circles",n+"+ LAMBDA("+ m+") =0"))
                        mycon.commit()
                        
                    elif a==3:
                        v=input("Enter equation of Circle 1")
                        b=input("Enter equation of Circle 2")
                        print(v,"+ LAMBDA (",v,"-",b,") =0")
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"EQN of circles","Family of circles",v+"+ LAMBDA ("+v+"-"+b+") =0"))
                        mycon.commit()
                        
                    

                quit_var = 0
                while ( quit_var != 1):
                    result = 0.0

                    print("what operation do you want to d0 on circles?")
                    print("1. Area of circle")
                    print("2. Circumference of circle")
                    print("3. Locus of Point")
                    print("4. How is the circle? Real, Imaginary or Point?")
                    print("5. Equation of Circle")
                    print("6. Diametric Circle")
                    print("7. Radius of Circle")
                    print("8. X intercept")
                    print("9. Y intercept")
                    print("10. Equation of Tangents from a point")
                    print("11. Equation of Normal on a point")
                    print("12. Equation of POT of circle")
                    print("13. Angle of intersection of 2 circles")
                    print("14. Check if 2 circles are orthogonals")
                    print("15. Family of circles")

                    choice = int(input())

                    if choice == 1:
                        area()
                        
                        
                    elif choice == 2:
                        perimeter()
                        
                        
                    elif choice == 3:
                        pointloc()
                        

                    elif choice == 4:
                        circleradiuscheck()
                        

                    elif choice == 5:
                        eqnofcircle()
                        

                    elif choice == 6:
                        diametriceqnofcircle()
                        

                    elif choice == 7:
                        findradius()
                        

                    elif choice == 8:
                        xinterc()
                        

                    elif choice == 9:
                        yinterc()
                        

                    elif choice == 10:
                        eqnoftangents()
                        

                    elif choice == 11:
                        eqnofnormal()
                        

                    elif choice == 12:
                        eqnofpot()
                        

                    elif choice == 13:
                        angintersection()
                        

                    elif choice == 14:
                        checkortho()
                        

                    elif choice == 15:
                        famcircles()
                        

                    else:
                        print("Invalid selection. enter from the list above")
                        
                    print("THE Calculator for CIRCLES IS OVER")
                    quit_var = int(input("Enter 1 to quit, any other digit to continue"))


            else:
                print("Invalid choice. choose from the list")
            
            print("THE Calculator for COORDINATE GEOMETRY IS OVER")
            quit_var = int(input("Enter 1 to quit, any other digit to continue"))



    elif main_choice == 4:
                def addorsubtract():
                    a=[]
                    b=[]
                    e1=int(input("Enter x coordinate of first vector"))
                    a.append(e1)
                    e2=int(input("Enter y coordinate of first vector"))
                    a.append(e2)
                    e3=int(input("Enter z coordinate of first vector"))
                    a.append(e3)
                    e4=int(input("Enter x coordinate of second vector"))
                    b.append(e4)
                    e5=int(input("Enter y coordinate of second vector"))
                    b.append(e5)
                    e6=int(input("Enter z coordinate of second vector"))
                    b.append(e6)
                    p=input("Do you want to add or subtract? Type add or subtract")
                    if (p.lower()).strip()=="add":
                        for j in range (0,3):
                            print("x,y,z coordinates of resultant vector are", a[j]+b[j])
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"x,y,z coordinates of vectors","Adding vectors","ANSWER CANNOT BE STORED"))
                        mycon.commit()
                    elif (p.lower()).strip()=="subtract":
                        for z in range (0,3):
                            print("x,y,z coordinates of resultant vector are", a[z]-b[z])
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"x,y,z coordinates of vectors","Subtracting vectors","ANSWER CANNOT BE STORED"))
                        mycon.commit()
                    else:
                        print("Type add or subtract")
                #addorsubtract()


                def multiply():
                    a=[]
                    b=[]
                    e1=int(input("Enter x coordinate of first vector"))
                    a.append(e1)
                    e2=int(input("Enter y coordinate of first vector"))
                    a.append(e2)
                    e3=int(input("Enter z coordinate of first vector"))
                    a.append(e3)
                    e4=int(input("Enter x coordinate of second vector"))
                    b.append(e4)
                    e5=int(input("Enter y coordinate of second vector"))
                    b.append(e5)
                    e6=int(input("Enter z coordinate of second vector"))
                    b.append(e6)
                    p=input("Do you want dot product or cross product? Type dot or cross")
                    
                    if p=="dot":
                        for j in range (0,3):
                            print("x,y,z coordinates of resultant vector are", a[j]*b[j])
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"x,y,z coordinates of vectors","Dot product of vectors","ANSWER CANNOT BE STORED"))
                        mycon.commit()
                    elif p=="cross":
                        print("x,y,z coordinates of resultant vector are:", e2*e6-e5*e3, e4*e3-e1*e6, e1*e5-e4*e2)
                        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"x,y,z coordinates of vectors","Cross product of vectors","ANSWER CANNOT BE STORED"))
                        mycon.commit()
                    else:
                        print("Type dot or cross")
                #multiply()


                def posvec():
                    a=[]
                    b=[]
                    e1=int(input("Enter x coordinate of first point"))
                    a.append(e1)
                    e2=int(input("Enter y coordinate of first point"))
                    a.append(e2)
                    e3=int(input("Enter z coordinate of first point"))
                    a.append(e3)
                    e4=int(input("Enter x coordinate of second point"))
                    b.append(e4)
                    e5=int(input("Enter y coordinate of second point"))
                    b.append(e5)
                    e6=int(input("Enter z coordinate of second point"))
                    b.append(e6)
                    for z in range (0,3):
                        print("coordinates of position vector are", a[z]-b[z])
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"x,y,z coordinates of vectors","Finding position vector","ANSWER CANNOT BE STORED"))
                    mycon.commit()
                #posvec()

                            

                quit_var = 0
                while (quit_var !=1 ):
                    result = 0.0

                    print("What operation do you want to do on vectors?")
                    print("1. Add or Subtract two vectors")
                    print("2. Multiply two vectors")
                    print("3. Postion Vector")

                    choice= int(input())

                    if choice == 1:
                        addorsubtract()

                    elif choice ==2:
                        multiply()

                    elif choice == 3:
                        posvec()

                    else:
                        print("Invalid choice. choose from the list")
                    
                    priNT("THE CALCULATOR FOR VECTORS IS OVER")
                    quit_var = int(input("Enter 1 to quit, any other digit to continue"))


    elif main_choice == 5:
        def graphfromsingledataset():
            a= []
            b=[]
            n = int(input("Enter number of elements  of x coordinates: "))
            m= int(input("Enter number of elements  of y coordinates(must be equal to the number of x coordinates): "))
            if n!=m:
                print("Number of elements  of x coordinates must be equal to number of elements  of y coordinates, restart program")
            else:
                for i in range(0, n): 
                    ele1 = int(input("Enter the x coordinates"))
                    a.append(ele1)
                for i in range(0, m): 
                    ele2 = int(input("Enter the y coordinates"))
                    b.append(ele2) 
                pt.plot(a,b, color='blue', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='green', markersize=12)
                pt.xlabel("x coordinates")
                pt.ylabel("y coordinates")
                pt.show()
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"x coordinates,ycoordinates","SINGLE DATA GRAPH","**GRAPH CANNOT BE SAVED**"))
                mycon.commit()

    #graphfromdata()
                    

        def comparisonoftwodatasets():
            a=[]
            b=[]
            c=[]
            d=[]
            n1 = int(input("Enter number of elements  of x coordinates of first dataset: "))
            m1= int(input("Enter number of elements  of y coordinates(must be equal to the number of x coordinates of first dataset): "))
            if n1!=m1:
                print("Number of elements  of x coordinates must be equal to number of elements  of y coordinates, restart program")
            else:
                for i in range(0, n1): 
                    ele1 = int(input("Enter the x coordinates"))
                    a.append(ele1)
                for i in range(0, m1): 
                    ele2 = int(input("Enter the y coordinates"))
                    b.append(ele2)
                n2 = int(input("Enter number of elements  of x coordinates of second dataset: "))
                m2= int(input("Enter number of elements  of y coordinates(must be equal to the number of x coordinates of second dataset): "))
                if n2!=m2:
                    print("Number of elements  of x coordinates must be equal to number of elements  of y coordinates, restart program")
                else:
                    for i in range(0, n2): 
                        ele3 = int(input("Enter the x coordinates"))
                        c.append(ele3)
                    for i in range(0, m2): 
                        ele4 = int(input("Enter the y coordinates"))
                        d.append(ele4)       
                pt.plot(a,b,color='blue', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='green', markersize=12)
                pt.plot(c,d,color='red', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='green', markersize=12)
                pt.xlabel("x coordinates")
                pt.ylabel("y coordinates")
                pt.show()
                cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Coordinates of two data sets","COMPARISON OF TWO DATASETS","**GRAPH CANNOT BE SAVED**"))
                mycon.commit()
    
    #comparisonoftwodatasets()
            

        def singlebargraph():
            a=[]
            n = int(input("Enter number of elements "))
            for i in range(0, n): 
                ele = int(input("Enter the values"))
                a.append(ele)
            x=np.arange(n)
            pt.bar(x,a,color='r',label='bar')
            pt.title("single bar graph")
            pt.xlabel("elements")
            pt.ylabel("values")
            pt.legend(loc="upper left")
            pt.grid(True)
            pt.show()
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Values of graph elements","SINGLE BAR GRAPH","**GRAPH CANNOT BE SAVED**"))
            mycon.commit()
	 
    #singlebargraph()
            
            
        def multiplebargraphs():
            t=int(input("Enter number of datasets you want to compare, 2 or 3 or 4 only"))
            if t==2:
                    a=[]
                    b=[]
                    n=int(input("Enter number of  values"))
                    for i in  range(0,n):
                            x = int(input("Enter the value of first data"))
                            y = int(input("Enter the value of second data"))
                            a.append(x)
                            b.append(y)
                    w=0.3
                    x=np.arange(len(a))
                    pt.bar(x,a, width=w, color='blue', edgecolor='green')
                    pt.bar(x+w, b,width=w, color='pink',edgecolor='blue')
                    pt.show()
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Values of first and second dataset","MULTIPLE BAR GRAPHS","**GRAPH CANNOT BE SAVED**"))
                    mycon.commit()
            elif t==3:
                    a=[]
                    b=[]
                    c=[]
                    n=int(input("enter number of  values"))
                    for i in  range(0,n):
                            x = int(input("Enter the value of first data"))
                            y = int(input("Enter the value of second data"))
                            z = int(input("Enter the value of third data"))
                            a.append(x)
                            b.append(y)
                            c.append(z)
                    w=0.3
                    x=np.arange(len(a))
                    pt.bar(x,a, width=w, color='blue', edgecolor='green')
                    pt.bar(x+w, b,width=w, color='pink',edgecolor='blue')
                    pt.bar(x+w*2, c,width=w,color='green', edgecolor='red')
                    pt.show()
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Values of first,second and third dataset","MULTIPLE BAR GRAPHS","**GRAPH CANNOT BE SAVED**"))
                    mycon.commit()
                    
            elif t==4:
                    a=[]
                    b=[]
                    c=[]
                    d=[]
                    n=int(input("Enter number of  values"))
                    for i in  range(0,n):
                            x = int(input("Enter the value of first data"))
                            y = int(input("Enter the value of second data"))
                            z = int(input("Enter the value of third data"))
                            w= int(input("Enter the value of fourth data"))
                            a.append(x)
                            b.append(y)
                            c.append(z)
                            d.append(w)
                    w=0.15
                    x=np.arange(len(a))
                    pt.bar(x,a, width=w, color='blue', edgecolor='green')
                    pt.bar(x+w, b,width=w, color='pink',edgecolor='blue')
                    pt.bar(x+w*2, c,width=w,color='green', edgecolor='red')
                    pt.bar(x+w*3, d,width=w,color='red', edgecolor='black')
                    pt.show()
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Values of first,second,third and fourth dataset","MULTIPLE BAR GRAPHS","**GRAPH CANNOT BE SAVED**"))
                    mycon.commit()
    #multiplebargraphs()


        def  piechart():
            a=[]
            b=[]
            c=[]
            n=int(input("Enter number of  values"))
            for i in  range(0,n):
                name= input("Enter the dataname")
                value = int(input("Enter the value of the dataname"))
                mycolor= input("Enter color name of the dataname")
                a.append(name)
                b.append(value)
                c.append(mycolor)
            pt.pie(b, labels = a, colors=c, startangle=90, shadow = True, radius = 1.2, autopct = '%5.2f%%')
            pt.legend(loc="upper right")
            pt.show()
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"Dataname, value and color of dataname","PIE CHART","**GRAPH CANNOT BE SAVED**"))
            mycon.commit()
            
    #piechart()


        def scatterchart():
            a= []
            b=[]
            n = int(input("Enter number of elements  of x coordinates: "))
            m= int(input("Enter number of elements  of y coordinates(must be equal to the number of x coordinates): "))
            if n!=m:
                    print("Number of elements  of x coordinates must be equal to number of elements  of y coordinates, restart program")
            else:
                    for i in range(0, n): 
                        ele1 = int(input("Enter the x coordinates"))
                        a.append(ele1)
                    for i in range(0, m): 
                        ele2 = int(input("Enter the y coordinates"))
                        b.append(ele2)
                    pt.scatter(a, b, label= "stars", color= "green", marker= "*", s=30) 
                      
                    # x-axis label 
                    pt.xlabel('x - axis') 
                    # frequency label 
                    pt.ylabel('y - axis') 
                    # plot title 
                    pt.title('My scatter plot!') 
                    # showing legend 
                    pt.legend(loc="best")  
                    # function to show the plot 
                    pt.show()
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"x and y coordinates","SCATTER CHART",))
                    mycon.commit()
                    
    #scatterchart()


        def trigonometricfunctions():
            gr=input("Enter triginometric name of function required(from sin,cos,tan):")
            if gr=="sin":
                    n = int(input("Enter a multiple of pi"))
                    x = np.linspace(-n*np.pi, n*np.pi, n*256, endpoint=True)
                    y = np.cos(x)
                    pt.plot(x,y)
                    pt.show()
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"trignometric name='sin',mutiple of pi="+str(n),"DISPLAYING TRIGONOMETRIC FUNCTIONS","**GRAPH CANNOT BE SAVED**"))
                    mycon.commit()
            elif gr=="cos":
                    n = int(input("Enter a multiple of pi"))
                    x = np.linspace(-n*np.pi, n*np.pi, n*256, endpoint=True)
                    y = np.sin(x)
                    pt.plot(x,y)
                    pt.show()
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"trignometric name='cos',mutiple of pi="+str(n),"DISPLAYING TRIGONOMETRIC FUNCTIONS","**GRAPH CANNOT BE SAVED**"))
                    mycon.commit()
                    
            elif gr=="tan":
                    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
                    pt.plot(x, np.tan(x))
                    pt.ylim(-5, 5)
                    pt.show()
                    cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"trignometric name='tan',mutiple of pi="+str(n),"DISPLAYING TRIGONOMETRIC FUNCTIONS","**GRAPH CANNOT BE SAVED**"))
                    mycon.commit()
            else:
                    print("Enter from sin,cos,tan")
    #trigonometricfunctions()
                    

        def typesofgraph():
            def create_plot(ptype): 
                
                x = np.arange(-10, 10, 0.01) 
                  
                if ptype == 'linear': 
                    y = x 
                elif ptype == 'quadratic': 
                    y = x**2
                elif ptype == 'cubic': 
                    y = x**3
                elif ptype == 'quartic': 
                    y = x**4
                          
                return(x, y) 
              
            pt.style.use('fivethirtyeight') 
              
            fig = pt.figure() 
               
            pt1 = fig.add_subplot(221) 
            pt2 = fig.add_subplot(222) 
            pt3 = fig.add_subplot(223) 
            pt4 = fig.add_subplot(224) 
               
            x, y = create_plot('linear') 
            pt1.plot(x, y, color ='r') 
            pt1.set_title('$y_1 = x$') 
              
            x, y = create_plot('quadratic') 
            pt2.plot(x, y, color ='b') 
            pt2.set_title('$y_2 = x^2$') 
              
            x, y = create_plot('cubic') 
            pt3.plot(x, y, color ='g') 
            pt3.set_title('$y_3 = x^3$') 
              
            x, y = create_plot('quartic') 
            pt4.plot(x, y, color ='k') 
            pt4.set_title('$y_4 = x^4$') 
              
            fig.subplots_adjust(hspace=.5,wspace=0.5) 
              
            pt.show()
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"NO SUCH INPUTS","DISPLAYING COMMON TYPES OF GRAPHS","**GRAPH CANNOT BE SAVED**"))
            mycon.commit()
            
    #typesofgraph()


        def graphfromequation(formula, x_range): 
            x = np.array(x_range)  
            y = eval(formula)
            pt.plot(x, y)  
            pt.show()
            cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,"NO INPUT","DISPLAYING GRAPH OF AN EQUATION","**GRAPH CANNOT BE SAVED**"))
            mycon.commit()
    #graphfromequation('x**4+x**2-5*x-4', range(-500, 500))


        quit_var = 0
        while ( quit_var != 1):
            result = 0.0

            print("What kind of graph do you want to sketch ")
            print("1. Graph from given data")
            print("2. Comparison between 2 given datas")
            print("3. Single Bar graph")
            print("4. Multiple Bar Graph")
            print("5. Pie Chart")
            print("6. Scatter Chart")
            print("7. Trignometric graphs")
            print("8. Types of graph")
            print("9. Graph of a given equation")

            choice = int(input())

            if choice == 1:
                    graphfromsingledataset()
		    

            elif choice == 2:
                    comparisonoftwodatasets()
                    

            elif choice == 3:
                    singlebargraph()

            elif choice == 4:
                    multiplebargraphs()

            elif choice == 5:
                    piechart()

            elif choice == 6:
                    scatterchart()

            elif choice == 7:
                    trigonometricfunctions()
    
            elif choice == 8:
                    typesofgraph()

            elif choice == 9:
                    
                    graphfromequation('x**4+x**2-5*x-4', range(-500, 500))
                    

            else:
                    print("Invalid choice. enter from the above list")
            print("THE Calculator GRAPHS IS OVER")
            quit_var = int(input("Enter 1 to quit, any other number to continue"))


    elif main_choice == 6:
        from sympy import *
        x, y = symbols('x y') 
        expr = eval(input("enter an expression"))
        print("Expression : {} ".format(expr)) 
   
        # Use sympy.Derivative() method  
        expr_diff = Derivative(expr, x)   
      
        print("Derivative of expression with respect to x : {}".format(expr_diff))   
        print("Value of the derivative : {} ".format(expr_diff.doit()))
        result=str(expr_diff.doit())  
        str1=str(expr)
        cursor.execute("INSERT INTO cal_hist(name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str1,"DIFFERENCIATION",result))

        

    elif main_choice ==7:
        mywin=Tk()
        mywin.title("TEMPERATURE CONVERTER")
        mywin.geometry('1500x300')
        print("THE GUI FOR TEMPERATURE HAS OPENED ")
        def CtoF():
            a=float(input_value.get())
            b=(a*9/5)+ 32
            ans.delete(0,END)
            ans.insert(0,str(b))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"C TO F",str(b)))
            
        def FtoC():
            a=float(input_value.get())
            b=(a-32)*5/9
            ans.delete(0,END)
            ans.insert(0,str(b))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"F TO C",str(b))) 
            mycon.commit()
            
        def CtoK():
            a=float(input_value.get())
            b=a+273
            ans.delete(0,END)
            ans.insert(0,str(b))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"C TO K",str(b)))
            mycon.commit()
            
        def FtoK():
            a=float(input_value.get())
            b=(a-32)*5/9 +273
            ans.delete(0,END)
            ans.insert(0,str(b))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"F TO K",str(b)))
            mycon.commit()
            
        Label(mywin,text="CONVERT THE TEMPERATURE", padx=100, pady=25, bg='light green', fg='white', bd=5, relief='raised', font='system').grid(row=0,column=2)
        Label(mywin,text="Input the temperature", padx=50, pady=15).grid(row=1,column=1)
        input_value=Entry(mywin,width=15)
        input_value.grid(row=1,column=2)

        Label(mywin,text="Answer", padx=50, pady=15).grid(row=3,column=1)
        ans=Entry(mywin,width=15)
        ans.grid(row=3,column=2)

        Button(mywin,text="Convert from Celcius to Fahrenheit ",padx=25,pady=10, command=CtoF).grid(row=4,column=0)
        Button(mywin,text="Convert from Fahrenheit to Celcius ",padx=25,pady=10, command=FtoC).grid(row=4,column=1)
        Button(mywin,text="Convert from Celcius to Kelvin ",padx=25,pady=10, command=CtoK).grid(row=4,column=2)
        Button(mywin,text="Convert from Fahrenheit to Kelvin ",padx=25,pady=10, command=FtoK).grid(row=4,column=3)
        mainloop()


    elif main_choice==8:
        #currencyconverter
        print("YOUR CURRENCY CONVERTER GUI HAS OPENED")

        from tkinter import *
        mywin=Tk()
        mywin['bg']="red"
        mywin.title("CURRENCY CONVERTER")
        mywin.geometry('840x450')

        def dollarTOr():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='us_dollar'")
            s= float(cursor.fetchall()[0][0])
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"US Dollar to Rupee",str(c)))
            mycon.commit()
        def rTOdollar():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='dollar'")
            s= float(cursor.fetchall()[0][0])
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Rupee to US Dollar",str(c)))
            mycon.commit()

        def yenTOr():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='yen'")
            s= float(cursor.fetchall()[0][0])
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Yen to Rupee",str(c)))
            mycon.commit()

        def rTOyen():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='yen'")
            s= float(cursor.fetchall()[0][0])
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Rupee to Yen",str(c)))
            mycon.commit()

        def euroTOr():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='euro'")
            s= float(cursor.fetchall()[0][0])
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Euro to Rupee",str(c)))
            mycon.commit()


        def rTOeuro():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='euro'")
            s= float(cursor.fetchall()[0][0])
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Rupee to Euro",str(c)))
            mycon.commit()

        def poundTOr():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='pound'")
            s= float(cursor.fetchall()[0][0])
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Pound to Rupee",str(c)))
            mycon.commit()

        def rTOpound():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='pound'")
            s= float(cursor.fetchall()[0][0])
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Rupee to Pound",str(c)))
            mycon.commit()

        def swiss_francTOr():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='swiss_franc'")
            s= float(cursor.fetchall()[0][0])
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Swiss Franc to Rupee",str(c)))
            mycon.commit()

        def rTOswiss_franc():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='swiss_franc'")
            s= float(cursor.fetchall()[0][0])
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Rupee to Swiss Franc",str(c)))
            mycon.commit()

        def singapore_dollarTOr():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='singapore_dollar'")
            s= float(cursor.fetchall()[0][0])
            c= a*s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Singapore Dollar to Rupee",str(c)))
            mycon.commit()

        def rTOsingapore_dollar():
            a= int(input_value.get())
            cursor.execute("SELECT IN_RUPEE FROM CURRENCIES WHERE 1_UNIT_OF_CURRENCY='singapore_dollar'")
            s= float(cursor.fetchall()[0][0])
            c= a/s
            ans.delete(0,END)
            ans.insert(0,str(c))
            cursor.execute("INSERT INTO cal_hist (name,input,operation,output) VALUES('{}','{}','{}','{}')".format(real_name,str(a),"Rupee to Singapore Dollar",str(c)))
            mycon.commit()


                           

        Label(mywin,text="~~~WIDGET TO CONVERT THE CURRENCY~~~", padx=100, pady=25, bg='red', fg='Black', bd=7, font='system').grid(row=0,column=1)
        Label(mywin,text="Input the Currency you want to convert:", padx=50, pady=15, fg='blue', bg='red').grid(row=1,column=1)
        input_value=Entry(mywin,width=15)
        input_value.grid(row=1,column=2)

        Label(mywin,text="Required Currency:", padx=50, pady=15, fg='blue', bg='red').grid(row=3,column=1)
        ans=Entry(mywin,width=15)
        ans.grid(row=3,column=2)

        Button(mywin,text="Convert from Rupee to U.S Dollar ",padx=34,pady=10, command=rTOdollar, bg='yellow').grid(row=4,column=1)
        Button(mywin,text="Convert from U.S Dollar to Rupee ",padx=34,pady=10, command=dollarTOr, bg='yellow').grid(row=4,column=2)
        Button(mywin,text="Convert from Rupee to Japanese Yen ",padx=25,pady=10, command=rTOyen, bg='yellow').grid(row=5,column=1)
        Button(mywin,text="Convert from Japanese Yen to Rupee ",padx=25,pady=10, command=yenTOr, bg='yellow').grid(row=5,column=2)
        Button(mywin,text="Convert from Rupee to Euro ",padx=48,pady=10, command=rTOeuro, bg='yellow').grid(row=6,column=1)
        Button(mywin,text="Convert from Euro to Rupee ",padx=48,pady=10, command=euroTOr, bg='yellow').grid(row=6,column=2)
        Button(mywin,text="Convert from Rupee to British Pound ",padx=24,pady=10, command=rTOpound, bg='yellow').grid(row=7,column=1)
        Button(mywin,text="Convert from British Pound to Rupee ",padx=24,pady=10, command=poundTOr, bg='yellow').grid(row=7,column=2)
        Button(mywin,text="Convert from Rupee to Swiss Franc ",padx=30,pady=10, command=rTOswiss_franc, bg='yellow').grid(row=8,column=1)
        Button(mywin,text="Convert from Swiss Franc to Rupee ",padx=30,pady=10, command=swiss_francTOr, bg='yellow').grid(row=8,column=2)
        Button(mywin,text="Convert from Rupee to Singapore Dollar ",padx=16,pady=10, command=rTOsingapore_dollar, bg='yellow').grid(row=9,column=1)
        Button(mywin,text="Convert from Singapore Dollar to Rupee ",padx=16,pady=10, command=singapore_dollarTOr, bg='yellow').grid(row=9,column=2)


        mainloop()


        
        
    elif main_choice == 9:
        cursor.execute(" SELECT INPUT,OPERATION,OUTPUT FROM cal_hist WHERE NAME='%s'"%real_name)
        rows = cursor.fetchall()
        print(tabulate(rows, headers=['INPUT', 'OPERATION','OUTPUT'], tablefmt='psql'))
    else: 
        print(" Please choose from the list above")
    print("YOU ARE NOW ON THE MAIN CALCULATOR MENU ")
    quit_var = int(input("Enter 1 to quit, any other number to continue"))
mycon.commit()               
mycon.close()




















        



                    
                    


                    
                    


        


             
