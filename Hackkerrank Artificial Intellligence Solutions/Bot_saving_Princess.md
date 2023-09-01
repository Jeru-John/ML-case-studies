### Problem: 
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

###### Sample input
```
3
---
-m-
p--
```
###### Sample output

```
DOWN
LEFT
```

### Task

Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid. The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0]. The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. The goal is to reach the princess in as few moves as possible.

### Solution:

[GitHub]([https://github.com](https://github.com/Jeru-John/ML-case-studies/blob/main/Hackkerrank%20Artificial%20Intellligence%20Solutions/Bot_Saving_Princess.py))

### Algorithm to Convert Grid into Data:

1. Initialize variables to store the positions of the bot and princess.

2. Iterate through each row and column of the grid.

3. For each cell in the grid, check its value:

4. step 4: 
* If the cell contains 'm', set the bot's position to the current row and column.
* If the cell contains 'p', set the princess's position to the current row and column.
* After processing all cells, you will have the positions of the bot and the princess.

5. Return or store these positions as data.


### Simple Understanding of the problem:

![WhatsApp Image 2023-09-01 at 11 46 08 PM](https://github.com/Jeru-John/ML-case-studies/assets/141055457/3290b5b4-e5b0-4e5e-ac24-2efb044347ec)

In the above image consider 1 to be the m position of the bot and 5 to be the p position of the princess.
bot_position = (1,1) => bot_col = 1, bot_row = 1
princess_position = (2,2) => princess_col = 2 , princess_row = 2
Let us get to the princess...
1. bot_col - 1 < princess_col - 2 --> so move RIGHT else move LEFT ( moves right => bot_col+1 , moves left => bot_col-1)  => makes the current bot col as 2
2. bot_row - 1 < princess_row - 2 --> so move DOWN else move UP ( moves down => bot_row+1 , moves up => bot_row-1) => makes the current bot row as 2

till... bot_row = princess_row and bot_col = princess_col (interation continues...)

### Solution steps: 

1. find_princess_position - function to get the current position of bot 'p'
2. find_bot_position - function to get the current position of bot 'm'
3. rescue_princess - function that gives the moves as a result

### Algorithm for Rescuing the Princess:

##### Find the Positions: 
First, the algorithm needs to find the positions of both the bot and the princess on the grid.

##### Navigate to the Princess: 
Using a loop or other control structure, continuously check the positions of the bot and the princess and make moves to get closer to the princess. The goal is to reduce the distance between the bot and the princess step by step.

##### Determine Moves: 
At each step of the loop, calculate the optimal move for the bot to get closer to the princess. The possible moves are typically UP, DOWN, LEFT, and RIGHT.

* If the bot's row position is greater than the princess's row position, move UP to decrease the row difference.
* If the bot's row position is less than the princess's row position, move DOWN to increase the row difference.
* If the bot's column position is greater than the princess's column position, move LEFT to decrease the column difference.
* If the bot's column position is less than the princess's column position, move RIGHT to increase the column difference.

##### Repeat Until Rescue: 
Keep looping and making moves until the bot reaches the same position as the princess. At this point, the bot has successfully rescued the princess.

##### Output Moves: 
After the rescue, the algorithm may generate a list of moves that the bot took to reach the princess. These moves can be returned or used for further processing.

##### Terminate: 
The algorithm terminates when the bot and the princess occupy the same cell, signifying a successful rescue.



