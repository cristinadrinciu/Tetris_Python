## Tetris_Python

* This is a repository for a Tetris game implemented in Python.      
* It contains the necessary code and files to run the game.    

The main purpose of this project is to showcase the implementation    
of the classic Tetris game using Python programming language with OOP concepts.

## Features & Technologies
- Classic Tetris gameplay with block movement and rotation.
- Collision detection to ensure blocks fit within the game grid.
- Sound effects when blocks are rotated.
- Programming Language : Python with **pygame** library api.

## Run instructions & Usage
To run the game, make sure you have Python installed on your system.         
Then, simply execute the main Python file to start playing the game (command: python3 ./main.py).

## Details about implementation

<img align="right" src="https://i.imgur.com/DBwAukX.png" width="250">

Implemented in OOP manner, the program contains the following classes:
* `block.py` - Contains implementation for general blocks, pieces of the game.
    * `blocks.py` - Contains all the classes that inherit the super class block.
* `grid.py` - Class that implements the grid of the game, the main stage of the gameplay 
              using a 20x10 matrix and the display methods.
* `game.py` - Class that directs the flow of the gameplay, making the connection between 
              the UserInteface and the logic of the game.
* `position.py` - Class that handles the coordinates of the game pieces.
* `colors.py` - Class that contains all the colors that appear in the UserInteface.
* `main.py` - Entry point of the program : handles the action of the user and translated them
              into gameplay.

* `Sounds/` - Directory that contains 3 audio files for the game features (background music,
              block rotation sound, row clear sound).

## Each member's contribution for the TEAM

**Drinciu Cristina**
* Created screen and set background color.
* Randomize the spawned piece and added controls of the pieces from the keyboard.
* Added the new function of clearing the full rows.
* Added the score, based on the cleared lines in game.

**Stefan Miruna - Andreea**
* Created grid, the rectangular guide and the list of colors.
* Implemented block rotation.
* Added game over and restart game implementations.
* Added display next block functionality and made sure that each type of block is centred in the user interface.
* Added sounds.

**Vasile Alexandru - Gabriel**
* Created general class of blocks and subclasses for the specific game pieces.
* Created slower movement for game pieces and solved collision problem for blocks.
* Added the UserInterface : score, next_block, switchBackGround button.
* Finished last details and created README.

**NOTE : Each member of the team has worked remotely, pushed their own**         
**contribution on github(https://github.com/cristinadrinciu/Tetris_Python) and then merged solution.**

**Difficulties & Solutions**
* We changed our approach for game pieces, initially being considered just the      
colored part by itself. Latter we figured it out that for an easier implementation          
we considered each block as a generic 4x4 square block, that incorporates the particular    
game piece in itself completed with "invisible" elements.

* We encountered some difficulities during the implementation of block rotation  
because their were getting out of the grid. To solve the problem, we came up     
with a new rotation condition that checks if the blocks still fit in the grid during rotation.

Feel free to explore the code and make any modifications or improvements as needed. Contributions are welcome!     

**NOTE: For more details about implementation check files.**
