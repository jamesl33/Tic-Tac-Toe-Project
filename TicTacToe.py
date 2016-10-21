import tkinter as tk

class Game(object):
	def __init__(self):
		#turn counter to determine if player places X or O
		global turn
		turn = True
		global count
		count = 1
		global buttons
		buttons = []
	def draw_interface(self):
		#create and draw the root window
		root = tk.Tk()
		#root windows title
		root.title("Tic-Tac-Toe")
		#size of the root window
		root.geometry("550x800")
		#create label to push buttons down the root window
		root.config()
		lbl = tk.Label(root, height="2")
		lbl.pack()
		#create the three frames for the buttons
		frame1 = tk.Frame(root, height="50", width="50")
		frame1.pack()
		frame2 = tk.Frame(root, height="50", width="50")
		frame2.pack()
		frame3 = tk.Frame(root, height="50", width="50")
		frame3.pack()

		self.buttons = []

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

			frame4 = tk.Frame(root, height="0", width="200")
			frame4.pack()

			self.buttons.append(btn)

		resetButton = tk.Button(frame4, width="16", height="3", text="Reset", command=self.reset_game)
		resetButton.pack(side="right", padx=(310,0))

	
	def check_if_solved(self):
		pass



	def btn_pressed(self, n):
		global turn
		global count
		print(count)
		if turn == True:			
			self.buttons[n-1].config(text="X")
			self.buttons[n-1].config(state="disabled")
			turn = False
			count += 1
			self.check_if_solved()
		else:
			self.buttons[n-1].config(text="O")
			self.buttons[n-1].config(state="disabled")
			turn = True
			count += 1

	def reset_game(self):
		global count
		count = 1
		for num in range(0, 9):
			self.buttons[num].config(text="", state="normal")



game = Game()
game.draw_interface()