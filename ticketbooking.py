# ONLINE TRAVEL TICKET BOOKING SYSTEM
import datetime
import random
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12340",
    database="batch_57"   
)
mycursor=mydb.cursor()
#**********************************************************************

# mycursor.execute("create database world_travel_agency_db")
# print("database created")

# mycursor.execute("create table tamilnadu(name varchar(25),age int,gender varchar(10),address varchar(50),destination varchar(20))")
# print("table created")

# mycursor.execute("create table india(name varchar(25),age int,gender varchar(10),address varchar(50),destination varchar(20))")
# print("table created")

# mycursor.execute("create table world(name varchar(25),age int,gender varchar(10),address varchar(50),destination varchar(20))")
# print("table created")

# mycursor.execute("create table cordilla_cruise(name varchar(25),age int,gender varchar(10),address varchar(50))")
# print("table created")

# mycursor.execute("create table train(name varchar(25),age int,gender varchar(10),address varchar(50),destination_from varchar(20),destination_to varchar(20))")
# print("table created")

def around_tamilnadu():
    sql="insert into tamilnadu(name,age,gender,address,destination) values(%s,%s,%s,%s,%s)"
    name=input("enter your name :")
    age=int(input("enter your age :"))
    gender=input("enter your gender :")
    address=input("enter your address :")
    destination=input("enter your destination :")
    val=(name,age,gender,address,destination)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your ticket booking sucessful reach chennai airport to get your ticket")

def around_india():
    sql="insert into india(name,age,gender,address,destination) values(%s,%s,%s,%s,%s)"
    name=input("enter your name :")
    age=int(input("enter your age :"))
    gender=input("enter your gender :")
    address=input("enter your address :")
    destination=input("enter your destination :")
    val=(name,age,gender,address,destination)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your ticket booking sucessful reach chennai airport to get your ticket")

def around_world():
    sql="insert into world(name,age,gender,address,destination) values(%s,%s,%s,%s,%s)"
    name=input("enter your name :")
    age=int(input("enter your age :"))
    gender=input("enter your gender :")
    address=input("enter your address :")
    destination=input("enter your destination :")
    val=(name,age,gender,address,destination)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your ticket booking sucessful reach chennai airport to get your ticket")

def cordilla_cruise():
    sql="insert into cordilla_cruise(name,age,gender,address) values(%s,%s,%s,%s)"
    name=input("enter your name :")
    age=int(input("enter your age :"))
    gender=input("enter your gender :")
    address=input("enter your address :")
    val=(name,age,gender,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your ticket booking sucessful reach chennai harbour to get your ticket")

def tamilnadu_data():
    mycursor.execute("select * from tamilnadu")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def india_data():
    mycursor.execute("select * from india")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def world_data():
    mycursor.execute("select * from world")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def cordilla_cruise_data():
    mycursor.execute("select * from cordilla_cruise")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def train():
    print('''train path :
            kanyakumari to chennai      price -- 350
            chennai to goa              price -- 500
            goa to rajasthan            price -- 600
            rajasthan to delhi          price -- 750
            delhi to jammu and kashmir  price -- 400''')
    sql="insert into train(name,age,gender,address,destination_from,destination_to) values(%s,%s,%s,%s,%s,%s)"
    name=input("enter your name :")
    age=int(input("enter your age :"))
    gender=input("enter your gender :")
    address=input("enter your address :")
    destination_from=input("enter your destination_from :")
    destination_to=input("enter your destination_to :")
    val=(name,age,gender,address,destination_from,destination_to)
    mycursor.execute(sql,val)
    mydb.commit()
    print("your ticket booking sucessful reach near train junction to get your ticket")

def train_data():
    mycursor.execute("select * from train")
    result=mycursor.fetchall()
    for i in result:
        print(i)

def exit():
    print("you are exited")

today=datetime.datetime.now()
print(f"Today Date and Time :{today}")

phone_number=input("verify your phone number here :")
otp=random.randint(1000,9999)
print(f"your OTP is :{otp}")

try:
    verify=int(input("enter your OTP :"))

    if otp==verify:
        print('''welcome to world_travel_agency
        1.by airplane
        2.by train
        3.exit''')

        try:
            transport=int(input("enter any one number :"))

            if transport==1:
                print('''by airplane
                1.ticket booking
                2.view old passengers details''')

                try:
                    data=int(input("enter any one number :"))

                    if data==1:
                        print('''ticket booking
                        1. around tamilnadu
                            chennai to salem        price -- 4,000
                            chennai to coimbathore  price -- 5,000
                            chennai to madhurai     price -- 6,000
                        2.around india
                            chennai to delhi        price -- 10,000
                            chennai to goa          price -- 8,000
                        3.around world
                            chennai to canada       price -- 1,00,000
                            chennai to london       price -- 60,000
                        4.cordilla cruise ship travel price -- 30,000
                        ''')

                        try:
                            data1=int(input("enter any one number :"))

                            if data1==1:
                                around_tamilnadu()
                            elif data1==2:
                                around_india()
                            elif data1==3:
                                around_world()
                            elif data1==4:
                                cordilla_cruise()
                            else:
                                print("you have entered an invalid number")

                        except:
                            print("enter only number")

                    elif data==2:
                        print('''view passengers details
                        1.around tmail nadu
                        2.around india
                        3.around world
                        4.cordilla cruise''')

                        try:
                            data2=int(input("enter any one number"))

                            if data2==1:
                                tamilnadu_data()
                            elif data2==2:
                                india_data()
                            elif data2==3:
                                world_data()
                            elif data2==4:
                                cordilla_cruise_data()
                            else:
                                print("you have entered an invalid number")

                        except:
                            print("enter only number")

                    else:
                        print("you have entered an invalid number")

                except:
                    print("enter only number")

            elif transport==2:
                print('''by train
                1.ticket booking
                2.view old passengers details''')

                try:
                    data3=int(input("enter any one number :"))

                    if data3==1:
                        train()

                    elif data3==2:
                        train_data()

                    else:
                        print("you have entered an invalid number")

                except:
                    print("enter only number")

            else:
                exit()

        except:
            print("enter only number")

    else:
        print("sorry your otp is wrong")

except:
    print("enter only number")
