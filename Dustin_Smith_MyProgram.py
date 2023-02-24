"""
Program: Dustin_Smith_MyProgram.py
Author: Dustin Smith
Date: February 18, 2023

This programs calls the input file 500DayFruitData.txt then imports the Mean and Median functions from Dustin_Smith_Stats.py.
The program writes all of the output data in the text file Dustin_Smith_Output.txt.
This program should be in the same directory as (Dustin_Smith_Stats.py) (Dustin_Smith_Output.txt) and (500DayFruitData.txt).
"""

#Assigns fruit_data_file to the text file containing the fruit data.
fruit_data_file = ("500DayFruitData.txt")

#Imports the Mean and Median functions from the Dustin_Smith_Stats.py module.	
from Dustin_Smith_Stats import Mean, Median

#The Mean function is used to calculate the mean of apples, bananas, strawberries, and all fruit eaten.
mean_apples, mean_bananas, mean_strawberrys, mean_fruits =  Mean(fruit_data_file)

#The Median function is used to calculate the median of apples, bananas, strawberries, and all fruit
median_apples, median_bananas, median_strawberrys, median_fruits = Median(fruit_data_file)

#Defines and opens the Dustin_Smith_Output text file in write mode to accept the output data.
output_file= open("Dustin_Smith_Output.txt", "w")

#Writes mean and median values of apples eaten in the output file. 
output_file.write("The mean number of apples eaten is " + str(mean_apples) + "\n")	
output_file.write("The median number of apples eaten is " + str(median_apples) + "\n\n")

#Writes the mean and median values of bananas eaten in the output file.
output_file.write("The mean number of bananas eaten is " + str(mean_bananas) + "\n")
output_file.write("The median number of bananas eaten is " + str(median_bananas) + "\n\n")

#Writes the mean and median values of strawberries eaten in the output file.
output_file.write("The mean number of strawberries eaten is " + str(mean_strawberrys) + "\n")
output_file.write("The median number of strawberries eaten is " + str(median_strawberrys) + "\n\n")

#Writes the the mean and median values of all fruit eaten in the output file.
output_file.write("The mean number of all fruit eaten is " + str(mean_fruits) + "\n")
output_file.write("The median number of all fruit eaten is " + str(median_fruits))
