import matplotlib.pyplot as plt                                     #importing the package
import pandas as pd                                                 #importing pandas to read given csv file 
plt.style.use('bmh')                                                #for styling the plot
df = pd.read_csv('FILE PATH.csv')                                   #'df' stands for dataframe which stores the csv file and reads it
x = df['x']                                                         #this stores the set of values given in the file
y = df['y']                                                         #this stores another set of values given in the file
plt.xlabel('')                                                      #this labels the x-axis of the plot
plt.ylabel('')                                                      #this labels the y-axis of the plot
plt.scatter(x,y)                                                    #this forms only the scatter plot
plt.plot(x,y)                                                       #this forms into a line plot
plt.title("LINE & SCATTER PLOT")                                    #title as per your requirement
plt.show()                                                          #displays the output
plt.savefig("mean_temp_line_scatter.png")                           #saves the output in 'png' format
                                              
