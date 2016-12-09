# Tic-Tac-Toe-Project
A.L.L Tic-Tac-Toe Game in python

This game was created for the activity lead learning as Coventry University and we had a group of four people who were assigned to create
the game. The game is written in Python using the Pygame module.

How do i run the game?
Simply running the Main.py file will allow you to play the game. You should be able to find your way around from here using the in game menus. To play local two player simply open the Main.py file and then press the play game button. If you would like to play the game online with two people first of all you must run the Server.py file. Then you will need to start two instances of the Main.py file and go into the setting menu and select the online mode. The game will assign one play as "X" and one person of "O".
If you would like to play the game in single player game you will have to run the Main.py and then enter the setting menu and select single player against AI. This will allow you to play the game against offine AI's. 

How do i play against an AI?
After running the Main.py file go into the settings menu from the main menu and click the box until it says that you will play against AI.
There will be another option which will appear to change the AI difficulity however currently there is only an easy Ai.

How do i play the networked version of the game?
First of all you will need to run the Server.py file which will start the server so it is ready for two players to connect. The server 
will not do anything untill two people have connected. 
Next you will need to run the Main.py file twice to create two instances of the game.
You will then need to go into the settings menu and choose player vs player(online) this will connect you to the server.
When two people have connected to the server player 1 will be able to take thier turn. 


Known Bugs:
1. When playing the game in multiplayer mode if there is moves on the display when you press the back button it will still display the "X" and "O" counters on the screen.
2. When playing the game in multiplayer mode you must press the reset button twice if the win line is drawn on the screen.
3. When you close the game from the terminal or from a text editor such as sublime you will get a Pygame Error: Video system not initialised. This bug has been ignored so far as it does not
effect how the game plays.
4. Harder Ai in not implimented as this was set on the side while the networking was created. The menu option has been left in so that later on the new AI can be added very easilly.