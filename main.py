from tkinter import *
import random
from tkinter import  messagebox
root =Tk()
root.geometry('800x600+300+50')

root.title('Typing Speed Game')
root.iconbitmap('icon.ico')
root.configure(bg='black')
words =  ['Sister','Iceland', 'Germany', 'Bangladesh', 'lorem','testing','Software','Web','industry','software','Game','Good','AIUB','Got','Gamil','hello','Next', 'You']
random.shuffle(words)
######### funtion section
def welcomeLabel():
    global count,sliderWord
    text = 'Welcome To Typing Speed Testing Game'
    if(count >= len(text)):
        count=0
        sliderWord=''
    sliderWord += text[count]
    count += 1
    titleLabel.configure(text=sliderWord)
    titleLabel.after(150,welcomeLabel)

def startGame(event):
    global score, miss
    if(timeLeft == 60):
        time()
        gamePlayDetailLabel.configure(text='Enjoy!!!')

    if(wordEntry.get() == wordLabel['text']):
        score +=1

        scoreCountLabel.configure(text=score)
        random.shuffle(words)
        wordLabel.configure(text=words[0])
        wordEntry.delete(0, END)
    else:
        miss +=1
        random.shuffle(words)

        wordLabel.configure(text=words[0])

        wordEntry.delete(0,END)

def time():
    global timeLeft,score,miss
    if(timeLeft >=11):
        pass
    else:
        timeCountLabel.configure(fg='red')
    if(timeLeft >0):
        timeLeft -= 1
        timeCountLabel.configure(text=timeLeft)
        timeCountLabel.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        notific = messagebox.askretrycancel('Notification','For Play Again Please Hit The Retry Button!')
        if(notific==True):
            score=0
            timeLeft=60
            miss=0
            timeCountLabel.configure(text=timeLeft)
            wordLabel.configure(text=words[0])
            scoreCountLabel.configure(text=score)



######### variables
score = 0
miss = 0
timeLeft=60
count =0
sliderWord = ''

###### label section
titleLabel = Label(root,text='', bg='black', fg='green', font=('arial',30, 'italic bold'), width=34)
titleLabel.place(x=10, y=10)
welcomeLabel()


scoreLabel = Label(root, text='Your Score', bg='black', fg='white', font=('arial',25, 'italic bold'))
scoreLabel.place(x=10, y=100)
scoreCountLabel = Label(root,text=score, bg='black', fg='white', font=('arial',25, 'italic bold'))
scoreCountLabel.place(x=80, y=180)

timeLabel=Label(root,text='Time Left', bg='black', fg='white', font=('arial',25, 'italic bold'))
timeLabel.place(x=600,y=100)

timeCountLabel=Label(root,text=timeLeft, bg='black', fg='white', font=('arial',25, 'italic bold'))
timeCountLabel.place(x=680,y=180)

wordLabel=Label(root,text=words[0], bg='black', fg='blue', font=('arial',25, 'italic bold'))
wordLabel.place(x=320,y=200)

######## Entry Section
wordEntry = Entry(root,font=('arial',25, 'italic bold'), bd=10, justify='center')
wordEntry.place(x=200, y=300)




######## Game Play detail label
gamePlayDetailLabel = Label(root,text='Type Word and Hit Enter Button', bg='black', fg='skyblue', font=('arial',30, 'italic bold'))
gamePlayDetailLabel.place(x=100, y=450)




root.bind('<Return>',startGame)
root.mainloop()