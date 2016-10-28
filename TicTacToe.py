import tkinter as tk
from tkinter import messagebox

class Game(object):
	def __init__(self):
		#this turn variable is declared to allow the program to alternate between placing "X" or "O"
		self.turn = True
		#count variable to check if the game has ended
		self.count = 1
		#values list which allows me to apply the check if solved function. each number represents a place on the board
		self.values = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}
		#list to store button config to allow the program to change the button config later on
		self.buttons = []
		#when the Game object has been called draw the user interface using the draw_interface class
		self.draw_interface()
	
	def draw_interface(self):
		"""This is the function to draw the initial interface. This includes packing the buttons on the screen inside three frames"""
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

	def check_if_solved(self, n):
		"""This check function checks to see if there is a winner of the current game depending on wether its argument is "X" or "Y" This function will check the array and see who
		if anybody has won the game. If there is a winner then it will pop up with a message box displaying who has won the game"""
		if n == "X":
			if self.values["1"] == "X" and self.values["2"] == "X" and self.values["3"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif self.values["4"] == "X" and self.values["5"] == "X" and self.values["6"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif self.values["6"] == "X" and self.values["7"] == "X" and self.values["8"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif self.values["1"] == "X" and self.values["4"] == "X" and self.values["7"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif self.values["2"] == "X" and self.values["5"] == "X" and self.values["8"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif self.values["3"] == "X" and self.values["7"] == "6" and self.values["9"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif self.values["1"] == "X" and self.values["5"] == "X" and self.values["9"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
			elif self.values["7"] == "X" and self.values["5"] == "X" and self.values["3"] == "X":
				messagebox.showinfo("We have a winner", "X Wins Well Done!")
		if n == "O":
			if self.values["1"] == "O" and self.values["2"] == "O" and self.values["3"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif self.values["4"] == "O" and self.values["5"] == "O" and self.values["6"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif self.values["6"] == "O" and self.values["7"] == "O" and self.values["8"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif self.values["1"] == "O" and self.values["4"] == "O" and self.values["7"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif self.values["2"] == "O" and self.values["5"] == "O" and self.values["8"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif self.values["3"] == "O" and self.values["7"] == "6" and self.values["9"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif self.values["1"] == "O" and self.values["5"] == "O" and self.values["9"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
			elif self.values["7"] == "O" and self.values["5"] == "O" and self.values["3"] == "O":
				messagebox.showinfo("We have a winner", "O Wins Well Done!")
	#function to handle what happens when there is a button which is pressed
	def btn_pressed(self, n):
		"""Button pressed function. This function handles what happens to the buttons on the gui when they are pressed. This includes what text will be place on the button when it is pressed
		This function in turn calls the check if solved function. It passes which player pressed a button last as an argument to allow the program to check who won."""
		#references the global variables for use
		# print(count)
		if self.turn == True:
			for key in self.values:
				if key == str(n):
					self.values[key] = "X"
			#change the config for the buttons to show who has taken there turn and where
			self.buttons[n-1].config(text="X")
			self.buttons[n-1].config(state="disabled")
			self.turn = False
			self.count += 1
			#the check if solved function is called to see if there is a winner when the button is pressed
			self.check_if_solved("X")
		else:
			for key in self.values:
				if key == str(n):
					self.values[key] = "O"
			self.buttons[n-1].config(text="O")
			self.buttons[n-1].config(state="disabled")
			self.turn = True
			self.count += 1
			self.check_if_solved("O")
			# print(values)

	def reset_game(self):
		"""Function to reset the game back to the state that it opens up in. This means if the user wants to restart playing the game they can.
		This allows the user to restart playing the game without haing to reopen the game"""
		self.turn = True
		#reset the values dictionary to default
		self.values = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}
		self.count = 1
		#loop to reset the buttons values to default
		for num in range(0, 9):
			self.buttons[num].config(text="", state="normal")
game = Game()