import matplotlib.pyplot as plt                                          #importing the package 
import pandas as pd                                                      #importing pandas to read given csv file 
plt.style.use('bmh')                                                     #for styling the plot
df = pd.read_csv('FILE PATH.csv')                                        #'df' stands for dataframe which stores the csv file and reads it
x = df['']                                                               #here x stores the set of values given in the file
y = df['']                                                               #here y stores another set of values given in the file
plt.xlabel('')                                                           #this labels the x-axis of the plot 
plt.ylabel('')                                                           #this labels the y-axis of the plot
plt.scatter(x,y, color = "purple", alpha = 0.3)                          #this forms the customised bubble chart
plt.title("BUBBLE CHART")                                                #sets title according to your requirement
plt.show()                                                               #displays the output
plt.savefig("FILE NAME.png")                                             #saves your output in 'png' format
plt.tight_layout()                                                       #structures everything and saves frome overlapping value plots
