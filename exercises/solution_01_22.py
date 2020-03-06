import pandas as pd

# The database 

hockey_players = pd.read_csv('data/canucks.csv', , index_col=0)


# Plots x as `Age` and y as `Salary`. using a scatterplot 
# Set color to `Darkblue`, opacity to 0.4 and don't forget to assign a title as "Canuck players Age vs. Salary" 

hockey_players.plot.scatter(x="Age", y = "Salary", alpha = 0.4, color = "Darkblue", title = "Canuck players Age vs. Salary");