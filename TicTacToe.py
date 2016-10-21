import tkinter as tk
from tkinter import messagebox
class Game(object):
	def __init__(self):
		#global variables for count, turn, buttons and values
		global turn
		global count
		global buttons
		global values
		turn = True
		count = 1
		buttons = []
		values = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}
	
	def draw_interface(self):
		#create and draw the root window
		root = tk.Tk()
		#root windows title
		root.title("Tic-Tac-Toe")
		#size of the root window
		root.geometry("550x800")
		#create label to push buttons down the root window
		lbl = tk.Label(root, height="2")
		lbl.pack()
		#create the three frames to house the buttons
		frame1 = tk.Frame(root, height="50", width="50")
		frame1.pack()
		frame2 = tk.Frame(root, height="50", width="50")
		frame2.pack()
		frame3 = tk.Frame(root, height="50", width="50")
		frame3.pack()
		#list to store button config to allow the program to change the button config later on
		self.buttons = []
		#loop to create three buttons in each frame each with the value from i
		for i in range(1,10):
			if i <= 3:
				btn = tk.Button(frame1, height="10", width="16", text=" ", \
				command=lambda n=i: self.btn_pressed(n))
				btn.pack(side="left")
			elif i > 3 and i <=6:
				btn = tk.Button(frame2, height="10", width="16", text=" ", \
				command=lambda n=i: self.btn_pressed(n))
				btn.pack(side="left")
			else:
				btn = tk.Button(frame3, height="10", width="16", text=" ", \
				command=lambda n=i: self.btn_pressed(n))
				btn.pack(side="left")
			#frame to house the reset button 
			frame4 = tk.Frame(root, height="0", width="200")
			frame4.pack()
			#add the last button created to the buttons list to allow the program to change its config in the button pressed function
			self.buttons.append(btn)
		#creation of the reset button
		resetButton = tk.Button(frame4, width="16", height="3", text="Reset", command=self.reset_game)
		#packing the reset button
		resetButton.pack(side="right", padx=(310,0))

	#function to check if there is a winner
	#this function check 3 times accross 
	#3 times down
	#and in each direction diagonally
	def check_if_solved(self, n):
		if n == "X":
			if values["1"] == "X" and values["2"] == "X" and values["3"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif values["4"] == "X" and values["5"] == "X" and values["6"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif values["6"] == "X" and values["7"] == "X" and values["8"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif values["1"] == "X" and values["4"] == "X" and values["7"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif values["2"] == "X" and values["5"] == "X" and values["8"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif values["3"] == "X" and values["7"] == "6" and values["9"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif values["1"] == "X" and values["5"] == "X" and values["9"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif values["7"] == "X" and values["5"] == "X" and values["3"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
		if n == "O":
			if values["1"] == "O" and values["2"] == "O" and values["3"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif values["4"] == "O" and values["5"] == "O" and values["6"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif values["6"] == "O" and values["7"] == "O" and values["8"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif values["1"] == "O" and values["4"] == "O" and values["7"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif values["2"] == "O" and values["5"] == "O" and values["8"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif values["3"] == "O" and values["7"] == "6" and values["9"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif values["1"] == "O" and values["5"] == "O" and values["9"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif values["7"] == "O" and values["5"] == "O" and values["3"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
	#function to handle what happens when there is a button which is pressed
	def btn_pressed(self, n):
		#references the global variables for use
		global turn
		global count
		# print(count)
		if turn == True:
			for key in values:
				if key == str(n):
					values[key] = "X"
			#change the config for the buttons to show who has taken there turn and where
			self.buttons[n-1].config(text="X")
			self.buttons[n-1].config(state="disabled")
			turn = False
			count += 1
			#the check if solved function is called to see if there is a winner when the button is pressed
			self.check_if_solved("X")
		else:
			for key in values:
				if key == str(n):
					values[key] = "O"
			self.buttons[n-1].config(text="O")
			self.buttons[n-1].config(state="disabled")
			turn = True
			count += 1
			self.check_if_solved("O")
			# print(values)
	#function to reset the game so the user can play the game several times without having to reopen the game
	def reset_game(self):
		global values
		#reset the values dictionary to default
		values = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}
		global count
		count = 1
		#loop to reset the buttons values to default
		for num in range(0, 9):
			self.buttons[num].config(text="", state="normal")
game = Game()
game.draw_interface()