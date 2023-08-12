# Game of Life

## What is the Game of Life?
The Game of Life is a cellular automaton devised by the british mathematician John Horton Conway in 1970. It was popularised by Martin Gardner in his October 1970 column of "Mathematical Games" in the "Scientific American" magazine.

A notable property of the special rule set used by Conway's "Game of Life" is it's Turing completeness. The Turing completeness is a property that describes that a programming language, a simulation or a logical system is in principle suitable to solve every computing problem. The programming of the "Game of Life" would be done with patterns, which then interact with each other in the simulation.

Because of the simplicity of the rule set, implementing Game of Life is a popular task for novice programmers.

## What is a Cellular Automaton?
A Cellular automaton is a discrete model that consists of a regular grid of cells wherein each cell is in a finite state. The inital state of the cellular automate is selected by assigning a state to each cell. The simulation then progresses in discreet time steps. The state of a cell at timestep t depends only on the state of nearby cells at timestep t-1 and a set of rules specific to the automate.

## Cell Neighborhoods
The cells which have an influence on the state of the automate are called neighborhood. There are two commonly used types of neighborhoods: The Moore Neighborhood and the Van Neumann Neighborhood. The Moore neighborhood contains all neighboring cells even if they share only a cornerpoint with a cell whilst the Van Neumann Neighborhood contains only cells that share an edge with a cell.

## Rules of the Game of Life
In the Game of Life each grid cell can have either one of two states: dead or alive. The Game of Life is controlled by four simple rules which are applied to each grid cell in the simulation domain:

* A live cell dies if it has fewer than two live neighbors.
* A live cell with two or three live neighbors lives on to the next generation.
* A live cell with more than three live neighbors dies.
* A dead cell will be brought back to live if it has exactly three live neighbors.

## Pattern Examples
Patterns will appear in a typical run of the Game of Life. Some patterns are static, others are oscillating or are moving across the screen. Some Patterns may even produce other patterns. The following tables give an overview on commonly appearing patterns in the Game of Life.

### Still Lifes
Still lifes are static structures that do not change over time.

> #### Block:
> The block is the most common "still life". It consists of four cells that form a 2x2 block. A block is a so-called "eater". This means that it can destroy other patterns without being structurally damaged.

> #### Beehive:
> A "still life" consisting of 6 cells. The second most common still life.

> #### Loaf:
> A still life consisting of 7 cells. The third most common still life.

### Oscillators
Oscillators are structures that repeat periodically over time, but maintain their position.

> #### Blinker:
> The smallest and most common oscillator.

> #### Toad:
> The Toad is a period 2 oscillator. It is the second most common naturally occuring oscillator

> #### Beacon:
> The third most common naturally occuring oscillator. It is composed of two diagonally touching blocks.

### Spaceships
Spaceships are structures that move across the playing field of the "Game of Life".

> #### The Glider:
> The glider is a pattern that is moving diagonally across the screen. It is the smallest, most common, and first-discovered spaceship.

> #### Lightweight spaceship (LWSS):
> This is an oscillating object that is moving orthogonally across the screen. It is the smallest orthogonally moving spaceship.

> #### Weekender:
> This is an orthogonal spaceship that is slightly larger than the previous patterns.