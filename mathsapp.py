from tkinter import *
from tkinter import messagebox
import mysql.connector
from operator import itemgetter
import random

tk = Tk()

def User_Profile():
    
    global con, cur, c1,username

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)
    
    c3.destroy()

    c1 = Canvas(tk, width=400, height=600,bg="light blue")
    c1.pack()

    sql = "select username from progress where username=%s"
    sql1 = "select score_percentage from progress where username=%s and topic=%s"
    val=[username]
    val1=[username,'Expanding Brackets']
    val2=[username,'Linear Equations']
    val3=[username,'Factorising']
    val4=[username,'Completing the Square']
    val5=[username,'Algebra']
    val6=[username,'Differentiation']
    val7=[username,'Integration']
    val8=[username,'Exponentials and Logarithms']
    val9=[username,'Decimals']
    val10=[username,'Multiplication']
    val11=[username,'Division']
    val12=[username,'Rounding']
    cur.execute(sql,val)
    row=cur.fetchone()
    cur.execute(sql1,val1)
    row1=cur.fetchone()
    cur.execute(sql1,val2)
    row2=cur.fetchone()
    cur.execute(sql1,val3)
    row3=cur.fetchone()
    cur.execute(sql1,val4)
    row4=cur.fetchone()
    cur.execute(sql1,val5)
    row5=cur.fetchone()
    cur.execute(sql1,val6)
    row6=cur.fetchone()
    cur.execute(sql1,val7)
    row7=cur.fetchone()
    cur.execute(sql1,val8)
    row8=cur.fetchone()
    cur.execute(sql1,val9)
    row9=cur.fetchone()
    cur.execute(sql1,val10)
    row10=cur.fetchone()
    cur.execute(sql1,val11)
    row11=cur.fetchone()
    cur.execute(sql1,val12)
    row12=cur.fetchone()
    
    c1.create_text(140,50, text='%s'%(row), font=('arial',19,'bold'))
    c1.create_text(260,50, text='progress', font=('arial',19,'bold'))
    c1.create_text(50,120, text='Topic', font=('arial',19,'bold'))
    c1.create_text(185,120, text='Level', font=('arial',19,'bold'))
    c1.create_text(330,120, text='progress(%)', font=('arial',19,'bold'))

    c1.create_text(70,160, text='''Expanding
Brackets''', font=('arial',15,'bold'))
    c1.create_text(70,210, text='''Linear
Equations''', font=('arial',15,'bold'))
    c1.create_text(70,250, text='Factorising', font=('arial',15,'bold'))
    c1.create_text(70,275, text='Completing', font=('arial',15,'bold'))
    c1.create_text(70,295, text='The Square', font=('arial',15,'bold'))
    c1.create_text(70,320, text='Algebra', font=('arial',15,'bold'))
    c1.create_text(70,350, text='Differentiation', font=('arial',15,'bold'))
    c1.create_text(70,380, text='Integration', font=('arial',15,'bold'))
    c1.create_text(70,410, text='Exponentials,', font=('arial',15,'bold'))
    c1.create_text(70,430, text='Logarithms', font=('arial',15,'bold'))
    c1.create_text(70,460, text='Decimals', font=('arial',15,'bold'))
    c1.create_text(70,490, text='Multiplication', font=('arial',15,'bold'))
    c1.create_text(70,520, text='Division', font=('arial',15,'bold'))
    c1.create_text(70,550, text='Rounding', font=('arial',15,'bold'))
    c1.create_text(185,160, text='GCSE', font=('arial',15,'bold'))
    c1.create_text(185,210, text='GCSE', font=('arial',15,'bold'))
    c1.create_text(185,250, text='GCSE', font=('arial',15,'bold'))
    c1.create_text(185,275, text='GCSE', font=('arial',15,'bold'))
    c1.create_text(185,320, text='A_Level', font=('arial',15,'bold'))
    c1.create_text(185,350, text='A_Level', font=('arial',15,'bold'))
    c1.create_text(185,380, text='A_Level', font=('arial',15,'bold'))
    c1.create_text(185,410, text='A_Level', font=('arial',15,'bold'))
    c1.create_text(185,460, text='KS3', font=('arial',15,'bold'))
    c1.create_text(185,490, text='KS3', font=('arial',15,'bold'))
    c1.create_text(185,520, text='KS3', font=('arial',15,'bold'))
    c1.create_text(185,550, text='KS3', font=('arial',15,'bold'))
    c1.create_text(330,160, text='%s'%(row1), font=('arial',15,'bold'))
    c1.create_text(330,210, text='%s'%(row2), font=('arial',15,'bold'))
    c1.create_text(330,250, text='%s'%(row3), font=('arial',15,'bold'))
    c1.create_text(330,275, text='%s'%(row4), font=('arial',15,'bold'))
    c1.create_text(330,320, text='%s'%(row5), font=('arial',15,'bold'))
    c1.create_text(330,350, text='%s'%(row6), font=('arial',15,'bold'))
    c1.create_text(330,380, text='%s'%(row7), font=('arial',15,'bold'))
    c1.create_text(330,410, text='%s'%(row8), font=('arial',15,'bold'))
    c1.create_text(330,460, text='%s'%(row9), font=('arial',15,'bold'))
    c1.create_text(330,490, text='%s'%(row10), font=('arial',15,'bold'))
    c1.create_text(330,520, text='%s'%(row11), font=('arial',15,'bold'))
    c1.create_text(330,550, text='%s'%(row12), font=('arial',15,'bold'))

    btn = Button(tk, text="Back", font=("bold", 10, "bold"), width=5, height=1, bd=1, command=main_menu)
    btn.place(x=40,y=50)
    
    
def ER():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Expanding_Brackets()
    elif x[0] == '2':
        Expanding_Brackets_2()
    elif x[0] == '3':
        Expanding_Brackets_3()

def LR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0]=='1':
        Linear_Equations()
    if x[0]=='2':
        Linear_Equations_2()
    if x[0]=='3':
        Linear_Equations_3()

def FR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Factorising()
    elif x[0] == '2':
        Factorising_2()
    elif x[0] == '3':
        Factorising_3()

def CR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Complete_Square()
    elif x[0] == '2':
        Complete_Square_2()
    elif x[0] == '3':
        Complete_Square_3()

def AR():
    x = ['1','2']
    random.shuffle(x)
    if x[0] == '1':
        Algebra()
    elif x[0] == '2':
        Algebra_2()
        
def DR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Differentiation()
    elif x[0] == '2':
        Differentiation_2()
    elif x[0] == '3':
        Differentiation_3()

def IR():
    x = ['1','2']
    random.shuffle(x)
    if x[0] == '1':
        Integration()
    elif x[0] == '2':
        Integration_2()

def ELR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        EXP()
    elif x[0] == '2':
        EXP_2()
    elif x[0] == '3':
        EXP_3()

def DER():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Decimal()
    elif x[0] == '2':
        Decimal_2()
    elif x[0] == '3':
        Decimal_3()

def MR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Multiplication()
    elif x[0] == '2':
        Multiplication_2()
    elif x[0] == '3':
        Multiplication_3()
        
def DIR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Division()
    elif x[0] == '2':
        Division_2()
    elif x[0] == '3':
        Division_3()
        
def RR():
    x = ['1','2','3']
    random.shuffle(x)
    if x[0] == '1':
        Rounding()
    elif x[0] == '2':
        Rounding_2()
    elif x[0] == '3':
        Rounding_3()

def Rounding_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 490 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 490 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Rounding_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 481:
            canvas.destroy()
            Rounding_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [481,490]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Rounding']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=481 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Rounding_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Rounding_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 471:
            canvas.destroy()
            Rounding_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [471,480]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Rounding']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 480 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 480 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=471 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def Rounding():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Rounding()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 461:
            canvas.destroy()
            Rounding()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct" %(ans))
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [461,470]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Rounding']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 470 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 470 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=461 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)
    

def Division_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 460 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 460 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Division_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 451:
            canvas.destroy()
            Division_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [451,460]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Division']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=451 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Division_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Division_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 441:
            canvas.destroy()
            Division_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [441,450]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Division']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 450 and entry.get() == ans:
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 450 and entry.get() != ans:
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=441 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def Division():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Division()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 431:
            canvas.destroy()
            Division()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [431,440]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Division']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correc","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        if i == 440 and entry.get() == ans:
            messagebox.showinfo("Correc","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 440 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=431 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Multiplication_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 430 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 430 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Multiplication_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 421:
            canvas.destroy()
            Multiplication_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [421,430]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Multiplication']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=421 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Multiplication_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Multiplication_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 411:
            canvas.destroy()
            Multiplication_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showerror("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [411,420]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Multiplication']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 420 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 420 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=411 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def Multiplication():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Multiplication()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 401:
            canvas.destroy()
            Multiplication()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [401,410]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Multiplication']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        if i == 410 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 410 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=401 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Decimal_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 400 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 400 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Decimal_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 391:
            canvas.destroy()
            Decimal_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [391,400]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Decimals']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=391 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Decimal_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Decimal_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 381:
            canvas.destroy()
            Decimal_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [381,390]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Decimals']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 390 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 390 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=381 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def Decimal():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        KS3()

    def EP_2():
        canvas.destroy()
        Decimal()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 371:
            canvas.destroy()
            Decimal()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [371,380]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Decimals']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 380 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 380 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=371 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def EXP_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 370 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 370 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        EXP_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 361:
            canvas.destroy()
            EXP_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [361,370]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Exponentials and logarithms']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=361 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def EXP_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        EXP_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 351:
            canvas.destroy()
            EXP_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [351,360]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Exponentials and logarithms']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 360 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 360 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=351 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def EXP():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        EXP()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 341:
            canvas.destroy()
            EXP()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [341,350]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Exponentials and logarithms']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        print(ans)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 350 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 350 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=341 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Integration_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        Integration_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 331:
            canvas.destroy()
            Integration_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Wrong","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [331,340]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Integration']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 340 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 340 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=331 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def Integration():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        Integration()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 321:
            canvas.destroy()
            Integration()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [321,330]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Integration']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

                    
        if i == 330 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 330 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=321 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Differentiation_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 320 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 320 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        Differentiation_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 311:
            canvas.destroy()
            Differentiation_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [311,320]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Differentiation']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=311 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Differentiation_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        Differentiation_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 301:
            canvas.destroy()
            Differentiation_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [271,280]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Differentiation']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 310 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 310 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=301 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def Differentiation():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        Differentiation()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 291:
            canvas.destroy()
            Differentiation()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [291,300]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Differentiation']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 300 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 300 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=291 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Algebra_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 290 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 290 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        Algebra_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 281:
            canvas.destroy()
            Algebra_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [281,290]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Algebra']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=281 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Algebra():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        A_Level()

    def EP_2():
        canvas.destroy()
        Algebra()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 271:
            canvas.destroy()
            Algebra()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [271,280]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Algebra']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 280 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 280 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=271 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)


def Complete_Square_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Complete_Square_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 261:
            canvas.destroy()
            Complete_Square_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [261,270]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Completing the square']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 270 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 270 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=261 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Complete_Square_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 260 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 260 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Complete_Square_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 251:
            canvas.destroy()
            Complete_Square_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [251,260]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Completing the square']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=251 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Complete_Square():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Complete_Square()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 241:
            canvas.destroy()
            Complete_Square()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [241,250]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Completing the square']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 250 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 250 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=241 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

    
def Linear_Equations_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Linear_Equations_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 201:
            canvas.destroy()
            Linear_Equations_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [201,210]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Linear Equations']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

             
        if i == 210 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 210 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=201 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Linear_Equations_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 200 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 200 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Linear_Equations_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 191:
            canvas.destroy()
            Linear_Equations_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [191,200]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Linear Equations']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=191 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Linear_Equations():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Linear_Equations()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 181:
            canvas.destroy()
            Linear_Equations()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [181,190]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Linear Equations']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 190 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 190 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=181 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)
        
        
def Factorising_3():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Factorising_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 231:
            canvas.destroy()
            Factorising_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [231,240]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Factorising']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        print(ans)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            print(entry.get())
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 240 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 240 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=231 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Factorising_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,cur,cur2,cur3,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 230 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 230 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Factorising_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 221:
            canvas.destroy()
            Factorising_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [221,230]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Factorising']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=221 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Factorising():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Factorising()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 211:
            canvas.destroy()
            Factorising()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [211,220]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Factorising']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 220 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 220 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=211 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Expanding_Brackets_3(): 
    
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Expanding_Brackets_3()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 171:
            canvas.destroy()
            Expanding_Brackets_3()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [150,160]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Expanding Brackets']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")    
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
            
        if i == 180 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 180 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Finish", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
        
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=171 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Expanding_Brackets_2():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username

    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1) 
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        canvas.delete('all')

        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        

        if i == 170 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        if i == 170 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Expanding_Brackets_2()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 161:
            canvas.destroy()
            Expanding_Brackets_2()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [150,160]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Expanding Brackets']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            
        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=161 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)

def Expanding_Brackets():
    
    global con,cur,cur2,con2,cur3,con3,i,canvas,row,btn,btn1,entry,username


    def Exit():
        canvas.destroy()
        GCSE()

    def EP_2():
        canvas.destroy()
        Expanding_Brackets()
        
    def Back():
        
        global i, sql5, row5, val5, entry,btn, btn1,canvas
        i-= 1
        
        sql5 = "select questions from score where scoreID = %s"
        val5 = [i]
        cur.execute(sql5,val5)
        row5 = cur.fetchone()

        canvas.delete('all')
        
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)

        canvas.create_text(250, 50, text='%s' %(row5), font=('bold',15,'bold'))

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)

        if i == 151:
            canvas.destroy()
            Expanding_brackets()
            
    def Final_Score():
        
        global i,sql1,val1,sql2,val2,sql3,val3,sql6,val6,sql7,val7,canvas,btn,btn1,score,entry,ans,row6,username
        
        i+= 1        
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        else:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)

        sql6 = "select sum(score) from score where ScoreID between %s and %s"
        val6 = [151,160]
        cur.execute(sql6,val6)
        row6 = cur.fetchone()
        ans = '%s' %(row6)
        ans = int(ans)
        ans = int((ans/20) * 100)

        sql7 = "update progress set score_percentage = %s where username = %s and topic=%s"
        val7 = [ans,username,'Expanding Brackets']
        cur2.execute(sql7,val7)
                
        canvas.delete('all')
        
        canvas.create_text(250, 50, text="Your Score: %s/20" %(row6),font=('arial',19,'bold'))

        btn = Button(tk, text="Replay", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=EP_2)
        btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
        
    def Next():
        global i,sql1,val1,row1,sql2,val2,sql3,val3,sql4,val4,row2,entry,btn, btn1,canvas,btn2
        
        i+= 1
    
        sql1 = "Select answers from score where scoreID = %s"
        val1 = [i-1]
        cur2.execute(sql1,val1)
        row1 = cur2.fetchone()
        ans = '%s'%(row1)

        canvas.delete('all')
        
        if entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)

        if entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            
        entry = Entry(tk, font=('Arial',10))
        canvas.create_window(250,120, window=entry)
    
        sql4 = "select questions from score where scoreID =%s"
        val4 = [i]
        cur.execute(sql4,val4)
        row2 = cur.fetchone()

        canvas.create_text(250, 50, text='%s' %(row2), font=('bold',15,'bold')) 

        btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
        btn1 = Button(tk, text="Back", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Back)
        btn.place(x=170, y=160)
        btn1.place(x=265,y=160)
        
        if i == 160 and entry.get() == ans:
            messagebox.showinfo("Correct","Your Answer is Correct")
            sql2 = "update score set score = %s where scoreID = %s"
            val2 = [2, i-1]
            cur3.execute(sql2, val2)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)

        if i == 160 and entry.get() != ans:
            messagebox.showerror("Wrong","The correct Answer is %s" %(ans))
            sql3 = "update score set score = %s where scoreID = %s"
            val3 = [0,i-1]
            cur3.execute(sql3,val3)
            btn.destroy()
            btn2 = Button(tk, text="Confirm", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Final_Score)
            btn2.place(x=170, y=160)
            
        
    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur2 = con.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp",autocommit=True)
    cur3 = con.cursor(buffered=True)
    
    i=151 
    sql = "select questions from score where scoreID =%s"
    val = [i]
    cur.execute(sql, val) 
    row = cur.fetchone()
    
    c1.destroy()
    
    canvas = Canvas(tk, width=600, height=200, bg="light blue")
    canvas.pack()
    
    entry = Entry(tk, font=('Arial',10))
    canvas.create_window(250,120, window=entry)

    canvas.create_text(250, 50, text='%s' %(row), font=('bold',15,'bold'))

    btn = Button(tk, text="Next", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=Next)
    btn1 = Button(tk, text="Exit", font=("bold", 11, "bold"), width=7, height=1, bd=1,command=Exit)
    btn.place(x=170, y=160)
    btn1.place(x=265,y=160)
    
def GCSE():
    global c1
    
    c3.destroy() 

    c1 = Canvas(tk, width=400, height=300, bg="light blue")
    c1.pack()

    btn = Button(tk, text="Expanding brackets", font=("bold", 11, "bold"), width=16, height=3, bd=1, command=ER)
    btn1 = Button(tk, text="Linear Equations", font=("bold", 11, "bold"), width=18, height=3, bd=1,command=LR)
    btn2 = Button(tk, text='Factorising', font=("bold", 11, "bold"), width=16, height=3, bd=1,command=FR)
    btn3 = Button(tk, text='Exit', font=("bold", 11, "bold"), width=15, height=3, bd=1,command=main_menu)
    btn4 = Button(tk, text="Completing the square", font=("bold", 11, "bold"), width=18, height=3, bd=1,command=CR)
    
    btn.place(x=18,y=30)
    btn1.place(x=200,y=30)
    btn2.place(x=15,y=130)
    btn3.place(x=100,y=230)
    btn4.place(x=200,y=130)

def A_Level(): 
    c3.destroy()
    global c1

    c1 = Canvas(tk, width=400, height=300, bg="light blue")
    c1.pack()
    
    btn = Button(tk, text="Algebra", font=("bold", 11, "bold"), width=15, height=3, bd=1,command=AR)
    btn1 = Button(tk, text="Differentiation", font=("bold", 11, "bold"), width=15, height=3, bd=1,command=DR)
    btn2 = Button(tk, text='Integration', font=("bold", 11, "bold"), width=16, height=3, bd=1,command=IR)
    btn3 = Button(tk, text='Exit', font=("bold", 11, "bold"), width=15, height=3, bd=1,command=main_menu)
    btn4 = Button(tk, text="exponentials,logarithms", font=("bold", 11, "bold"), width=15, height=3, bd=1,command=ELR)
    
    btn.place(x=18,y=30)
    btn1.place(x=200,y=30)
    btn2.place(x=15,y=130)
    btn3.place(x=18,y=230)
    btn4.place(x=200,y=130)

def KS3():
    global c1
    
    c3.destroy()

    c1 = Canvas(tk, width=400, height=300, bg="light blue")
    c1.pack()

    btn = Button(tk, text="Decimals", font=("bold", 11, "bold"), width=15, height=3, bd=1,command=DER)
    btn1 = Button(tk, text="Mutiplication", font=("bold", 11, "bold"), width=15, height=3, bd=1,command=MR)
    btn2 = Button(tk, text='Division', font=("bold", 11, "bold"), width=16, height=3, bd=1,command=DIR)
    btn3 = Button(tk, text='Exit', font=("bold", 11, "bold"), width=15, height=3, bd=1,command=main_menu)
    btn4 = Button(tk, text="Rounding", font=("bold", 11, "bold"), width=15, height=3, bd=1,command=RR)
    
    btn.place(x=18,y=30)
    btn1.place(x=200,y=30)
    btn2.place(x=15,y=130)
    btn3.place(x=130,y=230)
    btn4.place(x=200,y=130)

def restart():
    c3.destroy()
    start()

def main():
    c1.destroy()
    sign_up()

def login2():
    c1.destroy()
    login()

def login():
    global c1, entry, entry1, con, con2, cur3, con3

    c.destroy()

    c1 = Canvas(tk, width=300, height=210, bg="light blue")
    c1.pack()

    c1.create_text(50, 50, text="Username", font=("calibri", 15, "bold"))
    c1.create_text(50, 100, text="Password", font=("calibri", 15, "bold"))

    con = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp")
    cur = con.cursor(buffered=True)

    con2 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp")
    cur2 = con2.cursor(buffered=True)

    con3 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp")
    cur3 = con.cursor(buffered=True)
    
    def confirmlogin():

        global username, userpassword
        
        username = entry.get()
        userpassword = entry1.get()

        if (username == "" or userpassword == ""):
            messagebox.showerror("Oops!", "Your information can't be empty!")
            return
 
        sql = "select username, password from register where username=%s and password=%s"
        
        val = (username, userpassword)
        cur.execute(sql, val)
        result = cur.fetchone()

        sql1 = "select username from register"
        sql2 = "select password from register"

        cur2.execute(sql1)
        cur3.execute(sql2)

        u = []
        p = []

        for i in cur2:
            u.append(i)
        for i in cur3:
            p.append(i)

        res = list(map(itemgetter(0),u))
        res2 = list(map(itemgetter(0),p))
        
        entry.delete(0, END)
        entry1.delete(0, END)
        
        if result and username in res and userpassword in res2:
            main_menu()
        else:
            messagebox.showerror("Failed", "You've entered wrong credentials! .Try again")

    entry = Entry(tk)
    entry1 = Entry(tk)

    c1.create_window(160, 50, window=entry)
    c1.create_window(160, 100, window=entry1)

    btn2 = Button(tk, text='Proceed', font=("bold", 11, "bold"), width=7, height=1, bd=1, command=confirmlogin)
    btn2.place(x=120, y=130)

    btn3 = Button(tk, text='''Haven't joined yet? click here!''', activebackground="light blue", bg='light blue', font=("arial", 10, "bold"), width=30, height=1, bd=0, command=main)
    btn3.place(x=50, y=180)


def sign_up():
    global c1, entry2, entry3, entry4, entry5, con4, cur4

    c.destroy()

    c1 = Canvas(tk, width=300, height=300, bg="light blue")
    c1.pack()

    c1.create_text(50, 50, text="First Name", font=("calibri", 15, "bold"))
    c1.create_text(50, 100, text="Last Name", font=("calibri", 15, "bold"))
    c1.create_text(50, 150, text="Username", font=("calibri", 15, "bold"))
    c1.create_text(50, 200, text="Password", font=("calibri", 15, "bold"))

    con4 = mysql.connector.connect(host="localhost", user="root", password="User", database="MathsApp")
    cur4 = con4.cursor(buffered=True)

    def confirmsignup():
        global username

        username = entry4.get()

        sql = 'select * from Register where Username=%s'
        val = [username,]

        cur4.execute(sql, val)
        row = cur4.fetchone()

        if entry2.get() == "" or entry3.get() == "" or username == "" or entry5.get() == "":

            messagebox.showerror("Error", "All Fields Are Required")

        elif row != None:

            messagebox.showerror("Error", "Username already Exists,Please try a different Username")

        else:

            sql = "insert into Register(Forename,Surname,Username,Password) values(%s,%s,%s,%s)"
            sql1="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql2="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql3="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql4="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql5="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql6="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql7="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql8="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql9="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql10="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql11="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"
            sql12="insert into progress(Username,Topic,Score_percentage) values(%s, %s, %s)"

            val=[entry2.get(), entry3.get(), username, entry5.get(), ]
            val1=[username, 'Expanding Brackets',0]
            val2=[username, 'Linear Equations',0]
            val3=[username, 'Factorising',0]
            val4=[username, 'Completing the square', 0]
            val5=[username, 'Algebra', 0]
            val6=[username, 'Differentiation', 0]
            val7=[username, 'Integration', 0]
            val8=[username, 'Exponentials and logarithms', 0]
            val9=[username, 'Decimals', 0]
            val10=[username, 'Multiplication', 0]
            val11=[username, 'Division', 0]
            val12=[username, 'Rounding', 0]
            
            cur4.execute(sql, val)
            cur4.execute(sql1, val1)
            cur4.execute(sql2, val2)
            cur4.execute(sql3, val3)
            cur4.execute(sql4, val4)
            cur4.execute(sql5, val5)
            cur4.execute(sql6, val6)
            cur4.execute(sql7, val7)
            cur4.execute(sql8, val8)
            cur4.execute(sql9, val9)
            cur4.execute(sql10, val10)
            cur4.execute(sql11, val11)
            cur4.execute(sql12, val12)
            
            con4.commit()
            con4.close()

            main_menu()

            messagebox.showinfo("Congratulations", "Your Sign-up was successful")
            

            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

    entry2 = Entry(tk)
    entry3 = Entry(tk)
    entry4 = Entry(tk)
    entry5 = Entry(tk)

    c1.create_window(160, 50, window=entry2)
    c1.create_window(160, 100, window=entry3)
    c1.create_window(160, 150, window=entry4)
    c1.create_window(160, 200, window=entry5)

    btn6 = Button(tk, text="Home", font=("bold", 11, "bold"), width=7, height=1, bd=1, command=main_menu)
    btn6.place(x=150, y=230)

    btn4 = Button(tk, text='Proceed', font=("bold", 11, "bold"), width=7, height=1, bd=1, command=confirmsignup)
    btn4.place(x=60, y=230)

    btn5 = Button(tk, text='Already a member? click here!', activebackground="light blue", bg='light blue',
                  font=("arial", 10, "bold"), width=30, height=1, bd=0, command=login2)
    btn5.place(x=40, y=270)

def main_menu():
    global c3, btn6, btn7, btn, btn9, btn10

    c1.destroy()

    c3 = Canvas(tk, width=400, height=300, bg="light blue")
    c3.pack()

    btn7 = Button(tk, text="User Profile", font=("bold", 11, "bold"), width=15, height=3, bd=1,command=User_Profile)
    btn8 = Button(tk, text="KS3", font=("bold", 11, "bold"), width=15, height=3, bd=1, command=KS3)
    btn9 = Button(tk, text="A-Level", font=("bold", 11, "bold"), width=15, height=3, bd=1, command=A_Level)
    btn10 = Button(tk, text="GCSE", font=("bold", 11, "bold"), width=15, height=3, bd=1, command=GCSE)
    btn11 = Button(tk, text="Home", font=("bold", 11, "bold"), width=15, height=3, bd=1, command=restart)

    btn7.place(x=50, y=50)
    btn8.place(x=50, y=200)
    btn9.place(x=200, y=50)
    btn10.place(x=200, y=200)
    btn11.place(x=135, y=125)

def start():
    global c, img

    c = Canvas(tk, width=530, height=500, bg="light blue")
    c.pack()

    c.create_text(250, 100, text="MATHS", font=("calibri", 20, "bold"))
    c.create_text(50, 160, text='Login', font=("calibri", 20, "bold"))
    c.create_text(50, 220, text='''If You're''', font=("calibri", 20, "bold"))
    c.create_text(50, 270, text='A', font=("calibri", 20, "bold"))
    c.create_text(50, 310, text='Member', font=("calibri", 20, "bold"))
    c.create_text(450, 160, text='Sign Up', font=("calibri", 20, "bold"))
    c.create_text(450, 220, text='To experience', font=("calibri", 20, "bold"))
    c.create_text(450, 270, text='First', font=("calibri", 20, "bold"))
    c.create_text(450, 310, text='Time', font=("calibri", 20, "bold"))

    img = PhotoImage(file="maths.gif")
    c.create_image(255, 250, anchor=CENTER, image=img)

    btn = Button(tk, text='Login', font=("bold", 11, "bold"), width=15, height=3, bd=1, command=login)
    btn1 = Button(tk, text='Sign Up', font=("bold", 11, "bold"), width=15, height=3, bd=1, command=sign_up)
    btn1.place(x=300, y=400)
    btn.place(x=100, y=400)

start()

tk.mainloop() 
