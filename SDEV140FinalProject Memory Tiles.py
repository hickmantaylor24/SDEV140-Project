from tkinter import *
import random


#Create window
root = Tk()
root.title('Memory Tiles Game')
root.geometry("650x650")
root.configure(background='lightblue')

global winner
winner = 0


#Create matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6] #6 pairs
#Shuffle matches
random.shuffle(matches)

#Button frame
my_frame = Frame(root)
my_frame.pack(pady=15)


#Variables
count = 0
answer_list = []
answer_dict = {}




#Function for buttons
def button_click(button, number):
    global count, answer_list, answer_dict, winner

    if button["text"] == " " and count < 2 : #if button has not been clicked and if clicks are less than 2
        button["text"] = matches[number]
        answer_list.append(number)            #adds button
        answer_dict[button] = matches[number] #adds number

        #increase counter
        count += 1




#If numbers match
    if len(answer_list) == 2: #clicked on 2 tiles
        if matches[answer_list[0]] == matches[answer_list[1]]:
            footer.config(text= "MATCH!", fg = "black", background = "lightblue")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0               #reset count
            answer_list = []        #reset list
            answer_dict = {}        #reset dictionary
            winner += 1             #increase win number
            if winner == 6:         #user has won if 6 tiles have been clicked
                footer.config(text= " ", background = "lightblue")
#Window for if user has won
                win = Toplevel()
                win.title("Memory Tiles: Winner")
                win.geometry("450x450")
                win.configure(background= "green")
                win_label = Label(win, text = "YOU WON!", font= ("Arial", 50), background = "green").pack()
                
                
                
                
#If numbers do NOT match
        else: 
            footer.config(text= "Not a match",fg = "black", background = "lightblue")
            count = 0
            answer_list = []

        #reset buttons   
        for key in answer_dict:
            key["text"] = " "

            answer_dict = {}
            


#Define buttons
button0 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button0,0))
button1 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button1,1))
button2 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button2,2))
button3 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button3,3))
button4 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button4,4))
button5 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button5,5))
button6 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button6,6))
button7 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button7,7))
button8 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button8,8)) 
button9 = Button(my_frame, text = " ", font=("Arial", 30),height=5, width=6, command = lambda: button_click(button9,9)) 
button10 = Button(my_frame, text = " ", font=("Arial", 30), height=5, width=6,command = lambda: button_click(button10,10)) 
button11 = Button(my_frame, text = " ", font=("Arial", 30),height=5, width=6,command = lambda: button_click(button11,11)) 



#Grid for buttons
button0.grid(row=0,column= 0)
button1.grid(row=0,column= 1)
button2.grid(row=0,column= 2)
button3.grid(row=0,column= 3)

button4.grid(row=1,column= 0)
button5.grid(row=1,column= 1)
button6.grid(row=1,column= 2)
button7.grid(row=1,column= 3)

button8.grid(row=2, column= 0)
button9.grid(row=2,column= 1)
button10.grid(row=2,column= 2)
button11.grid(row=2,column= 3)


#Text at bottom of window
footer = Label(root, text= "Select two tiles to start", font=("Arial", 35), fg = "black", background = "lightblue")
footer.pack(pady=10)




root.mainloop()

