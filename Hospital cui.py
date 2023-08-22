# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:54:09 2023

@author: User
"""

import pymysql
mydb=pymysql.connect(host="localhost", user="root",passwd="malika")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists hospital")
mycursor.execute("use hospital")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(30))")

while True:
    print("1: SIGNUP")
    print("2: LOGNIN")
    
    ch=int(input("SINGUP / LOGIN: "))
    
    if ch==1:
        username=input("ENTER USSERNAME: ")
        pw=input("ENTER PASSWORD: ")
        
        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        mydb.commit()
        
    elif ch==2:
        username=input("ENTER YOUR USERNAME: ")
        
        mycursor.execute("select username from signup where username='"+username+"'")
        pot=mycursor.fetchone()
        
        if pot is None:
            print("""
<<<<<<   SINGUP TO COUNTINOUE   >>>>>>""")

                
        else:
            print("""
!!!!!!!!!!!!!!!<<<<<  VALIDE USERNAME  >>>>>!!!!!!!!!!!!!!!!!!!""")
            
            pw=input("ENTER YOUR PASSWORD: ")
            
            mycursor.execute("select password from signup where password='"+pw+"'")
            a=mycursor.fetchone()
            
            if a is None:
                print("""
                      
!!!!!!!!!!!!!!!!!!!!! INCORRECT PASSWORD !!!!!!!!!!!!!!!!!!!!!""")


            else:
                
                print("""
+++++++++++++++++++++++++++++ LOGIN SUCCESSFULL ++++++++++++++++++++++++++++++++++""") 
                
                print("""
                      
                
==================================================================================

======++++++++++++++++++++++      TMH HOSPITAL      ++++++++++++++++++++++++======

==================================================================================""")
                
                mycursor.execute("create table if not exists birth(Child_id varchar(34)primary key,Child_name varchar(56),Addrass varchar(30),Birth_date varchar(25),Sex varchar(6),Father_name varchar(20),Mother_name varchar(20))")
                mycursor.execute("create table if not exists doctor(Doctor_id varchar(89)primary key,Doctor_name varchar(56),Addrass varchar(30),Age int(80),Department varchar(45))")
                mycursor.execute("create table if not exists patient(Patient_id varchar(47)primary key,Patient_name varchar(50),Addrass varchar(30),Age varchar(80),Addmited_date varchar(67),Department varchar(76),Doctor_id varchar(89),sex varchar(56))")
                mycursor.execute("create table if not exists nurse(Nurse_id varchar(34)primary key,Nurse_name varchar(56),Addrass varchar(30),Age int(30))")
                mycursor.execute("create table if not exists other_worker(Worker_id varchar(34)primary key,Worker_name varchar(56),Address varchar(30),Age int(30),Job varchar(56))")
                mycursor.execute("create table if not exists appointment(appointment_no varchar(47)primary key,patient_Name varchar(50),Age int(19),Department varchar(60),Doctor_id varchar(89)references doctor(doctor_id),Time varchar(20))")
                mycursor.execute("create table if not exists discharged(Patient_name varchar(50),Addrass varchar(30),Age int(80),Addmited_date varchar(67),Department varchar(76),Doctor_id varchar(89),discharged_date varchar(50))")
                mydb.commit()
                
                while (True):
                    print(
                        
"""
1: <<< Search >>>
2: <<< Birth record >>>
3: <<< Patient registeration >>>
4: <<< Patient information >>>
5: <<< Staff registration >>>
6: <<< Staff information >>>
7: <<< Appointments >>>
8: <<< Discharged record >>>
9: <<< Exit >>>""")

                    
                
                
                    c=int(input("Enter your choice: "))         
                    
                    if c==1:
                        print("""
1: >> Birth taken
2: >> Patient
3: >> Staff
4: >> Exit""")
                        s=int(input("enter your choice: "))
                        if s==1:
                            br=input("Enter child_id: ")
                         
                            mycursor.execute("select * from birth where Child_id='"+br+"'")
                            pot3=mycursor.fetchone()
                            if pot3 is not None:
                                print(pot3)
                            else:
                                print("""     
  !!! Incorrect child_id !!!""")
                        elif s==2:
                            pr=input("Enter patient_id: ")
                            
                            mycursor.execute("select * from patient where Patient_id='"+pr+"'")
                            pot3=mycursor.fetchone()
                            if pot3 is not None:
                                print(pot3)
                            else:
                                print("""  
  !!! Incorrect patient_id !!!""")
                                    
                        elif s==3:
                            
                            print("""
1: >>>Doctor<<<
2: >>Nurse<<<
3: >>Other_worker<<<
4: >>Exit<<<""")
                             
                            ss=int(input("Enter your choice: "))
                            if ss==1:
                                
                                
                                dr=input("Enter doctor_id: ")
                            
                            
                                mycursor.execute("select * from doctor where Doctor_id='"+dr+"'")
                                pot3=mycursor.fetchone()
                                if pot3 is not None:
                                     print(pot3)
                                else:
                                    print("""
  !!!invalide doctor_id!!!""")
                                
                                
                                    
  
                            elif ss==2:
                                 
                                 nr=input("Enter nurse_id: ")
                        
                                 mycursor.execute("select * from nurse where Nurse_id='"+nr+"'")
                                 pot3=mycursor.fetchone()
                                 if pot3 is not None:
                                      print(pot3)
                                 else:
                                     print("""
  !!!invalid nurse_id!!!""")
                                         
                        
                
  
                            
                            elif ss==3:
                                 nr=input("Enter worker_id: ")
                            
                                 
                                 mycursor.execute("select * from other_worker where Worker_id='"+nr+"'")
                                 pot3=mycursor.fetchone()
                                 if pot3 is not None:
                                      print(pot3)
                                 else:
                                     print("""
  !!!invalid worker_id!!!""")

                            elif ss==4:
                                
                                break
                            else:
                                print("plz choose a valide input")
                            
                        
                        elif s==4:
                            break
                        else:
                            print("plz choose a valid input")
                            
                    
                    
                    elif c==2:
                        print("""
1: >>Add record
2: >>Update record
3: >>Show records
4: >>Exit""")
                        br=int(input("enter your choose: "))
                        
                        if br==1:
                            print("""
 Fill the details""")
                            
                            cd=input("enter child_id: "  )
                            mycursor.execute("select * from birth where Child_id='"+cd+"'")
                            row=mycursor.fetchone()
                            if row is None:
                                cn=input ("Enter child_name: ")
                                ad=input("Enter address of parents: ")
                                bd=input("Enter date of bith: ")
                                s=input("Enter sex: ")
                                fn=input("Enter father's name: ")
                                mn=input("Enter mother's name: ")
                            
                            
                            
                                mycursor.execute("insert into birth values('"+cd+"','"+cn+"','"+ad+"','"+bd+"','"+s+"','"+fn+"','"+mn+"')")
                                mydb.commit()
                                print("""
      +++++++++++SUCCESSFULLY ADDED+++++++++++++   """)
   
                            else:
                                print("""
                                      *** Duplicate id ***""")
   
                        elif br==2:
                            print("""
1: ~Update name
2: ~Update address
3: ~Update date of birth
4: ~Update sex
5: ~Update father's name
6: ~Update mother's name
7: ~Exit """)
                            u=int(input("Enter your choice: "))
                            
                            
                            if u==1:
                                cd=input("Enter child_id: " )
                                mycursor.execute("select * from birth where Child_id='"+cd+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    cn=input("Enter new name: ")
                                    mycursor.execute("update birth set Child_name='"+cn+"'where Child_id='"+cd+"'")
                                    mydb.commit()
                                    print("""
        +++++++++++ SUCCESSFULLY UPDATE ++++++++++ """)
                   
                                else:
                                    print("""
             > !!! invalid child_id !!! <   """)
             
                        
                            elif u==2:
                                 cd=input("Enter child_id: " )
                                 mycursor.execute("select * from birth where Child_id='"+cd+"'")
                                 row=mycursor.fetchone()
                                 if row is not None:
                                    ad=input("Enter new addrass: ")
                                    mycursor.execute("update birth set Child_name='"+cn+"'where Addrass='"+ad+"'")
                                    mydb.commit()
                                    print("""
        +++++++++++ SUCCESSFULLY UPDATE ++++++++++ """)
                   
                                 else:
                                    print("""
             >>> !!! invalid child_id !!! <<<  """)
             
                            elif u==3:
                                cd=input("Enter child_id: " )
                                mycursor.execute("select * from birth where Child_id='"+cd+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    d=input("Enter date of birth: ")
                                    mycursor.execute("update birth set Birth_date='"+d+"'where Child_id='"+cd+"'")
                                    mydb.commit()
                                    print("""
        +++++++++++ SUCCESSFULLY UPDATE ++++++++++ """)
                   
                                else:
                                    print("""
             > !!! invalid child_id !!! <   """)                   

                            elif u==4:
                                cd=input("Enter child_id: " )
                                mycursor.execute("select * from birth where Child_id='"+cd+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    s=input("Enter gender: ")
                                    mycursor.execute("update birth set Sex='"+s+"'where Child_id='"+cd+"'")
                                    mydb.commit()
                                    print("""
        +++++++++++ SUCCESSFULLY UPDATE ++++++++++ """)
                   
                                else:
                                    print("""
             > !!! invalid child_id !!! <   """)
             
                            elif u==5:
                                cd=input("Enter child_id: " )
                                mycursor.execute("select * from birth where Child_id='"+cd+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    fn=input("Enter father name: ")
                                    mycursor.execute("update birth set Child_name='"+fn+"'where Child_id='"+cd+"'")
                                    mydb.commit()
                                    print("""
        +++++++++++ SUCCESSFULLY UPDATE ++++++++++ """)
                   
                                else:
                                    print("""
             > !!! invalid child_id !!! <   """)
             
             
                            elif u==6:
                                cd=input("Enter child_id: " )
                                mycursor.execute("select * from birth where Child_id='"+cd+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    mn=input("Enter mother name: ")
                                    mycursor.execute("update birth set Child_name='"+mn+"'where Child_id='"+cd+"'")
                                    mydb.commit()
                                    print("""
        +++++++++++ SUCCESSFULLY UPDATE ++++++++++ """)
                   
                                else:
                                    print("""
             > !!! Invalid child_id !!! <   """)
  
                            elif u==7:
                                break
                            else:
                                print("""
       @ @ @ Plz choose valid input @ @ @ """)
       
                        elif br==3:
                            
                            db=mycursor.execute("select * from birth")
                            row=mycursor.fetchall()
                            for i in row:
                                print(i)
                        
                        elif br==4:
                            break
                        else:
                            print(""""
                ---- Plz enter valid input ----""")
                
                
                
                    elif c==3:
                        
                         pr=input("Enter patient_id: ")
                         mycursor.execute("select * from patient where Patient_id ='"+pr+"'")
                         row=mycursor.fetchone()
                         if row is None:
                             d=input("Enter department: ")
                             mycursor.execute("select Doctor_id,Doctor_name from doctor where Department='"+d+"'") 
                             row1=mycursor.fetchone()
                             if row1 is not None:   
                                 print(" +++++  Doctors of '"+d+"' department  +++++ " )
                                 print(row1)
                                 for i in mycursor:
                                     print(i)
                                 di=input("Enter doctor_id: ")
                                 p=input("Enter patient name: ")
                                 a=input("Enter patient address: ")
                                 ag=input("Enter age of patient: ")
                                 ad=input("Enter addmited date: ")
                             
                                 s=input("Enter sex: ")
                                        
                                 mycursor.execute("insert into patient values('"+pr+"','"+p+"','"+a+"','"+str(ag)+"','"+ad+"','"+d+"','"+di+"','"+s+"')")
                                 mydb.commit()
                                 print("""
    +++++++++++ SUCCESSFULLY ADDED ++++++++++""")
                             else:
                                 print("""
      ???  INVAID DEPARTMENT ???  """)   
     
                         else:
                             print("""
        *****  DUPLICATE PATIENT ID  *****""")
            
                     
                    elif c==4:
                        print("""
1: >> Update record 
2: >> Show record
3: >> Delete record / Discharge a patient
4: >> Exit""")

                        pr=int(input("Enter your choice: "))
                        if pr==1:
                            print("""
1: >>> Update name
2: >>> Update age
3: >>> Update address
4: >>> Update sex
5: >>> Exit""")

                            u=int(input("Enter your choice"))
                            if u==1:
                                pi=input("Enter patient id")
                                mycursor.execute("select * from patient where patient_id='"+pi+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    nm=input("Enter a new name")
                                    mycursor.execute("update patient set Patient_name='"+nm+"' where patient_id='"+pi+"'")
                                    mydb.commit()
                                    print("""
    +++++++++++ SUCCESSFULLY UPDATED ++++++++++""")
                                else:
                                    print("""
    ----------  INVALID PATIENT_ID  -----------""")
    
    
                            elif u==2:
                                pi=input("Enter patient id: ")
                                mycursor.execute("select * from patient where patient_id='"+pi+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    ag=input("Enter new age: ")
                                    mycursor.execute("update patient set age='"+ag+"'where patient_id='"+pi+"'")
                                    mydb.commit()
                                    print("""
    +++++++++++ SUCCESSFULLY UPDATED ++++++++++""")
                                else:
                                    print("""
    ----------  INVALID PATIENT_ID  -----------""")
    
                                
                            elif u==3:
                                pi=input("Enter patient id: ")
                                mycursor.execute("select * from patient where patient_id='"+pi+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    ad=input("Enter new addrass: ")
                                    mycursor.execute("update patient set addrass ='"+ad+"'where patient_id='"+pi+"'")
                                    mydb.commit()
                                    print("""
    +++++++++++ SUCCESSFULLY UPDATED ++++++++++""")
                                else:
                                    print("""
    ----------  INVALID PATIENT_ID  -----------""")
      
    
                            elif u==4:
                                pi=input("Enter patient id: ")
                                mycursor.execute("select * from patient where patient_id='"+pi+"'")
                                row=mycursor.fetchone()
                                if row is not None:
                                    s=input("Enter sex: ")
                                    mycursor.execute("update patient set sex='"+s+"'where patient_id='"+pi+"'")
                                    mydb.commit()
                                    print("""
    +++++++++++ SUCCESSFULLY UPDATED ++++++++++""")
                                else:
                                    print("""
    ----------  INVALID PATIENT_ID  -----------""")
    
                    
                            elif u==5:
                                break
                            else:
                                print("""
                ---- Plz enter valid input ----""")
                
                                
                        elif pr==2:
                            mycursor.execute("select * from patient")
                            row=mycursor.fetchall()
                            for i in row:
                                print(i)
                    
                
                        elif pr==3:
                            pi=input("Enter patient_id")
                            mycursor.execute("select * from patient where patient_id='"+pi+"'")
                            row=mycursor.fetchone()
                            if row is not None:
                                d=input("enter discharged date")
                                mycursor.execute("insert into discharged select patient_name,addrass,age,addmited_date,department,doctor_id,'"+d+"' as 'discharged_date' from patient where patient_id='"+pi+"'")
                                mycursor.execute("delete from patient where patient_id='"+pi+"'")
                                mydb.commit()
                                print("""
   <<++++++++++>> PATIENT DISCHARGED <<++++++++++>>""")
                            else:
                                print("""
      >>>>>>  INVAID PATIENT ID  <<<<<<""")
                                
                                
                        elif pr==4:
                            break
                        else:
                            print("""
                ---- Plz enter valid input ----""")
                
                    elif c==5:
                        print("""
1. <<<>>> Add Doctor<<<>>>
2. <<<>>> Add Nurse <<<>>>
3. <<<>>> Add Other_worker <<<>>>
4. <<<>>> Exit <<<>>>""")

                        sr=int(input("Enter your choice: "))
                        if sr==1:
                            di=input("Enter a doctor_id: ")
                            mycursor.execute("select * from doctor where doctor_id='"+di+"'")
                            row=mycursor.fetchone()
                            if row is None:
                                print("""
        >>>>> FILL THE DETAILS <<<<<""")
                                dn=input("Enter doctor name: ")
                                ad=input("Enter address: ")
                                ag=int(input("Enter age: "))
                                d=input("Enter doctor department: ")
                                mycursor.execute("insert into doctor values('"+di+"','"+dn+"','"+ad+"','"+str(ag)+"','"+d+"')")
                                mydb.commit()
                                print("""
        >>>>>> SUCCSESSFULLY ADDAED <<<<<<""")
                            else:
                                print("""
       >>>>>> duplicate id <<<<<<<""")
       
       
                        elif sr==2:
                            ni=input("Enter nurse id: ")
                            mycursor.execute("select * from nurse where nurse_id='"+ni+"'")
                            row=mycursor.fetchone()
                            if row is None:
                                print("""
        >>>>> FILL THE DETAILS <<<<<""")
                                nn=input("Enter your name: ")
                                ad=input("Enter your address: ")
                                ag=int(input("Enter your ages: "))
    
                                mycursor.execute("insert into nurse values('"+ni+"','"+nn+"','"+ad+"','"+str(ag)+"')")
                                mydb.commit()
                                print("""
        >>>>>> SUCCSESSFULLY ADDAED <<<<<<""")
                            else:
                                print("""
       >>>>>> duplicate id <<<<<<<""")
       
                        elif sr==3:
                           wi=input("Enter worker id: ")
                           mycursor.execute("select * from other_worker where worker_id='"+wi+"'")
                           row=mycursor.fetchone()
                           if row is None:
                               print("""
        >>>>> FILL THE DETAILS <<<<<""")
                               wn=input("Enter your name: ")
                               ad=input("Enter your address: ")
                               ag=int(input("Enter your age: "))
                               j=input("Enter job: ")
                               mycursor.execute("insert into other_worker values('"+wi+"','"+wn+"','"+ad+"','"+str(ag)+"','"+j+"')")
                               mydb.commit()
                               print("""
        >>>>>> SUCCSESSFULLY ADDAED <<<<<<""")
                           else:
                               print("""
       >>>>>> duplicate id <<<<<<<""")
       
                        elif sr==4:
                            break
                        else:
                         print("""
    >>>>>>>>>>> plz enter valid input <<<<<<<<<<<<<<<<<<""")
    
     
    
                    elif c==6:
                        print("""
1. <> Doctor information <>
2. <> Nurse information <>
3. <> Other_worker <>
4. <> Exit <>""")

                        si=int(input("Enter your choice: "))
                        if si==1:
                           print("""
1. >>>> Upadate record
2. >>>> Show record
3. >>>> Delete record
4. >>>> Exit""")

                           du=int(input("Enter your choice: "))
                           if du==1:
                               di=input("Enter doctor id: ")
                               mycursor.execute("select * from doctor where doctor_id='"+di+"'")
                               row=mycursor.fetchone()
                               if row is not None:
                                   print("""
1. {{{ Update name }}}
2. {{{ Update Address }}}
3. {{{ Update age }}}
4. {{{ Update departmenet }}}
5. {{{ Exit }}}""")

                                   u=int(input("Enter your choice: "))
                                   if u==1:
                                       un=input("Enter updated name; ")
                                       mycursor.execute("update doctor set doctor_name='"+un+"' where doctor_id='"+di+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==2:
                                       ua=input("Enter updated address: ")
                                       mycursor.execute("update doctor set addrass='"+ua+"' where doctor_id='"+di+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==3:
                                       uag=input("Enter updated age: ")
                                       mycursor.execute("update doctor set age='"+uag+"' where doctor_id='"+di+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==4:
                                       ud=input("Enter updated departmented: ")
                                       mycursor.execute("update doctor set department='"+ud+"' where doctor_id='"+di+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==5:
                                      break
                                   else:
                                       print("""
    ---plz enter valid input---""")
    
                               else:
                                   print("""
    !!!! INVALID DOCTOR_ID !!!!""" )
                                       
                                               
                           elif du==2:  
                               mycursor.execute("select * from doctor")
                               row=mycursor.fetchall()
                               for i in row:
                                   print(i)
                                   
                           elif du==3:
                               di=input("Enter doctor id: ")
                               mycursor.execute("select * from doctor where doctor_id='"+di+"'")
                               row=mycursor.fetchone()
                               if row is not None:    
                                  mycursor.execute("delete from doctor where doctor_id='"+di+"'")
                                  mydb.commit()
                                  print("""
   ++++++++ SUCCSESSFULLY DELETED ++++++++""")
                               else:
                                   print("""
    !!!! INVALID DOCTOR_ID !!!!""" )
                                   
   
                           elif du==4:
                               break
                           else:
                               print("""
        ---- plz choose valid input ----""")
                
####################################################################################################################################3
                        elif si==2:
                           print("""
1. >>>> Upadate record
2. >>>> Show record
3. >>>> Delete record
4. >>>> Exit""")

                           nu=int(input("Enter your choice: "))
                           if nu==1:
                               ni=input("Enter nurse id: ")
                               mycursor.execute("select * from nurse where nurse_id='"+ni+"'")
                               row=mycursor.fetchone()
                               if row is not None:
                                   print("""
1. {{{ Update name }}}
2. {{{ Update Address }}}
3. {{{ Update age }}}
4. {{{ Exit }}}""")

                                   u=int(input("Enter your choice: "))
                                   if u==1:
                                       nn=input("Enter updated name: ")
                                       mycursor.execute("update nurse set nurse_name='"+nn+"' where nurse_id='"+ni+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==2:
                                       ua=input("Enter updated address: ")
                                       mycursor.execute("update nurse set addrass='"+ua+"' where nurse_id='"+ni+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==3:
                                       uag=input("Enter updated age: ")
                                       mycursor.execute("update nurse set age='"+uag+"' where nurse_id='"+ni+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==4:
                                      break
                                   else:
                                       print("""
    ---Plz enter valid input---""")
    
                               else:
                                   print("""
    !!!! INVALID NURSE_ID !!!!""" )
                                       
                                               
                           elif nu==2:  
                               mycursor.execute("select * from nurse")
                               row=mycursor.fetchall()
                               for i in row:
                                   print(i)
                                   
                           elif nu==3:
                               ni=input("Enter nurse id: ")
                               mycursor.execute("select * from nurse where nurse_id='"+ni+"'")
                               row=mycursor.fetchone()
                               if row is not None:    
                                  mycursor.execute("delete from nurse where nurse_id='"+ni+"'")
                                  mydb.commit()
                                  print("""
   ++++++++ SUCCSESSFULLY DELETED ++++++++""")
                               else:
                                   print("""
    !!!! INVALID NURSE_ID !!!!""" )
                                   
   
                           elif nu==4:
                               break
                           else:
                               print("""
        ---- Plz choose valid input ----""")
        
                        
        
                
                        elif si==3:
                           print("""
1. >>>> Upadate record
2. >>>> Show record
3. >>>> Delete record
4. >>>> Exit""")

                           wu=int(input("Enter your choice: "))
                           if wu==1:
                               wi=input("Enter Worker id: ")
                               mycursor.execute("select * from other_worker where worker_id='"+wi+"'")
                               row=mycursor.fetchone()
                               if row is not None:
                                   print("""
1. {{{ Update name }}}
2. {{{ Update Address }}}
3. {{{ Update age }}}
4. {{{ Update job }}}
5. {{{ Exit }}}""")

                                   u=int(input("Enter your choice: "))
                                   if u==1:
                                       nn=input("Enter updated name: ")
                                       mycursor.execute("update other_worker set worker_name='"+nn+"' where worker_id='"+wi+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==2:
                                       ua=input("Enter updated address: ")
                                       mycursor.execute("update other_worker set address='"+ua+"' where worker_id='"+wi+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==3:
                                       uag=input("Enter updated age: ")
                                       mycursor.execute("update other_worker set age='"+uag+"' where worker_id='"+wi+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==4:
                                       uj=input("Enter update job: ")
                                       mycursor.execute("update other_worker set job='"+uj+"' where worker_id='"+wi+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                                   elif u==5:
                                      break
                                   else:
                                       print("""
    ---plz enter valid input---""")
    
                               else:
                                   print("""
    !!!! INVALID WORKER_ID !!!!""" )
                                       
                                               
                           elif wu==2:  
                               mycursor.execute("select * from other_worker")
                               row=mycursor.fetchall()
                               for i in row:
                                   print(i)
                                   
                           elif wu==3:
                               wi=input("Enter worker id: ")
                               mycursor.execute("select * from other_worker where worker_id='"+wi+"'")
                               row=mycursor.fetchone()
                               if row is not None:    
                                  mycursor.execute("delete from other_worker where worker_id='"+wi+"'")
                                  mydb.commit()
                                  print("""
   ++++++++ SUCCSESSFULLY DELETED ++++++++""")
                               else:
                                   print("""
    !!!! INVALID WORKER_ID !!!!""" )
                                   
   
                           elif wu==4:
                               break
                           else:
                               print("""
        ---- plz choose valid input ----""")
        
                        
        
                        elif si==4:
                            break
                        else:
                            print("""
        ---- plz choose valid input ----""")
        






                    elif c==7:
                        print("""
1. >>> Add Appointment >>>
2. >>> Update Appointment >>>
3. >>> Delete Appointment >>>
4. >>> Show Appointment >>>
5. >>> Exit >>> """)

                        ap=int(input("Enter your choice: "))
                        if ap==1:
                            ai=input("Enter appointment no: ")
                            mycursor.execute("Select * from appointment where appointment_no='"+ai+"' ")
                            row=mycursor.fetchone()
                            if row is None:
                                d=input("Enter department: ")
                                mycursor.execute("select Doctor_id,Doctor_name from doctor where Department='"+d+"'") 
                                row1=mycursor.fetchone()
                                if row1 is not None:   
                                   print(" +++++  Doctors of '"+d+"' department  +++++ " )
                                   print(row1)
                                   for i in mycursor:
                                     print(i)
                                   di=input("Enter doctor_id: ")
                                   p=input("Enter patient name: ")
                                   ag=input("Enter age of patient: ")
                                   t=input("Enter appointment time: ")
                                   mycursor.execute("insert into appointment values('"+ai+"','"+p+"','"+str(ag)+"','"+d+"','"+di+"','"+t+"')")
                                   mydb.commit()
                                   print("""
   +++++++++++++++++ APPOINTMENT ADDED ++++++++++++++++""")
                                else:
                                   print("""
   ---------------- INVALID DEPARTMENT ---------------""")
                            else:
                                print("""
   ---------------- INVALID APPOINTMENT.NO -------------""")
   
                                
                                 
                             
                        elif ap==2:
                            ai=input("Enter appointment no: ")
                            mycursor.execute("Select * from appointment where appointment_no='"+ai+"' ")
                            row=mycursor.fetchone()
                            if row is not None:
                               print("""
1. >>> Update name
2. >>> Update age
3. >>> Update time
4. >>> Exit""")
                               u=int(input("Enter your choice: "))
                               if u==1:
                                       un=input("Enter updated name: ")
                                       mycursor.execute("update appointment set patient_name='"+un+"' where appointment_no='"+ai+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                               
                               elif u==2:
                                       uag=input("Enter updated age: ")
                                       mycursor.execute("update appointment set age='"+uag+"' where appointment_no='"+ai+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                               elif u==3:
                                       ua=input("Enter updated address: ")
                                       mycursor.execute("update appointment set time='"+t+"' where appointment_no='"+ai+"'")
                                       mydb.commit()
                                       print("""
    +++++ SUCCSESSFULLY UPDATED +++++""")
                               elif u==4:
                                     break
                               else:
                                       print("""
    ---Plz enter valid input---""")
                        elif ap==3:
                            ai=input("Enter Appointment_no:  ")
                            mycursor.execute("select * from appointment where appointment_no='"+ai+"' ")
                            row=mycursor.fetchone()
                            if row is not None:
                                mycursor.execute("delete from appointment where appointment_no='"+ai+"'")
                                mydb.commit()
                                print("""
    +++++++ APPOINTMENT DELETED +++++++""")
                            else:
                                print("""
   !!!!!!  INVALID APPOINTMENT NO.  !!!!!!""")

                        elif ap==4:
                            mycursor.execute("select * from appointment")
                            row=mycursor.fetchall()
                            for i in row:
                                print(i)
                                
                        elif ap==5:
                            break
                        else:
                             print("""
       ~~~PLZ CHOOSE VALID INPUT~~~     """)
                    
                    elif c==8:
                        mycursor.execute("select * from discharged")
                        row=mycursor.fetchall()
                        for i in row:
                            print(i)
                    elif c==9:
                        break
                    
###################################################################################
        
                    else:
                        print("""
       ~~~PLZ CHOOSE VALID INPUT~~~     """)

                       
    else:
        print("""
       ~~~PLZ CHOOSE VALID INPUT~~~""")