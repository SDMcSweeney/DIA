# DIA -Investigating desirability of boid like behaviours in a predator/prey simulation


## Behaviour videos


random movement.mp4  
Demonstrates the first behaviour state in the chromosome  


boid movement.mp4  
Demonstrates the second behaviour state in the chromosome  


Return movement.mp4  
Demonstrates the third behaviour state in the chromosome  


Wolf hunting behaviour.mp4  
Demonstrates the behaviour of the wolf  

## Graphs and figures

Visualised_ranges.png  
Demonstrates visually the unit ranges talked about in my paper   

Sheepflow.drawio.png
Additional flowchart for prey behaviour

The follwing are the graphs showing the results from their respective simulations  
Prey with 4 range 7 predators.png  
Prey with 6 range 5 predators.png  
Prey with 6 range 6 predators.png  
Prey with 6 range 7 predators.png  
Prey with 6 vision range no predators.png  
Prey with 8 range 7 predators.png  

## Unity Project  
The project should be opened through unity (made with version 2021.3.18f1) , and is not exported as an executable, hyperparameters need to be set in the engine.  
The majority of hyperparameters are found in the scripts labelled "behaviour_controller" and "spawner".  
Prey and predator vision is controlled through the prefab for the respective agent.

## Paper submission
DIA-Boid-Evolution.pdf contains the full paper as submitted through the university moodle

## Raw results data
The raw data of results csvs are included in /results_raw . The simple python script I used to generate graphs is also included.
