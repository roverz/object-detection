import matplotlib.pyplot as plt                                   #importing the package
import pandas as pd                                               #importing pandas to read given csv file 
plt.style.use('bmh')                                              #for styling the plot
df = pd.read_csv('FILE PATH.csv')                                 #'df' stands for dataframe which stores the csv file and reads it
x = df['x']                                                       #this stores the given set of values
plt.boxplot(x)                                                    #this forms the box plot of the x values
plt.ylabel('')                                                    #this labels the y-axis as the boxplot will be read form y-axis only
plt.title("BOX PLOT of MEAN values")                              #title for the plot
plt.savefig("boxplot.png")                                        #saves the output in 'png' format
plt.show()                                                        #displays the ouput
