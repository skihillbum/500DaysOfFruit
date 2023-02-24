"""
Program: Dustin_Smith_Stats.py
Author: Dustin Smith
Date: February 17, 2023

This program creates two functions to calculate the mean and median of fruit data from the fruit data file (500DayFruitData.txt).
The text file should contain three columns: days, fruit, and number of fruits eaten.
This program should be in the same directory as (Dustin_Smith_MyProgram.py) (Dustin_Smith_Output.txt) and (500DayFruitData.txt).
"""

#This function calculates the mean for individual fruit types and all fruits eaten.
def Mean (fruit_data_file):
	
	#Opens the fruit_data_file for reading.
	fruit_txt= open(fruit_data_file, "r")
		
	#Reads the lines of fruit data.
	fruit_data = fruit_txt.readlines()
	
	#Initializes variables for each type of fruit and all fruit.
	apple_days = 0
	apples_eaten = 0
	apples_eaten_list = []
	
	banana_days = 0
	bananas_eaten = 0
	bananas_eaten_list = []
	
	strawberry_days = 0
	strawberrys_eaten = 0
	strawberrys_eaten_list = []
	
	fruit_days = 0
	fruits_eaten = 0
	fruits_eaten_list = []
	
	#Loops through the fruit data to calculate the mean of apples eaten.
	for i in fruit_data:
		
		#Splits the line into a list strings.
	    line = i.split()
	    
	    #Extracts the fruit name from element two.
	    if line[1] == "apple":
			
	        apple_days += 1
	        
	        apples_eaten += int(line[2])
	        
	        apples_eaten_list += [int(line[2])]
	
	#Calculates and defines the mean of apples eaten.       
	mean_apples = apples_eaten / apple_days
	
	#Loops through the fruit data to calculate the mean of bananas eaten.
	for i in fruit_data:
		
	    line = i.split()
	    
	    if line[1] == "banana":
			
	        banana_days += 1
	        
	        bananas_eaten += int(line[2])
	        
	        bananas_eaten_list += [int(line[2])]
	        
	#Calculates and defines the mean of bananas eaten.
	mean_bananas = bananas_eaten / banana_days
	
	#Loops through the fruit data to calculate the mean of strawberries eaten.
	for i in fruit_data:
		
	    line = i.split()
	    
	    if line[1] == "strawberry":
			
	        strawberry_days += 1
	        
	        strawberrys_eaten += int(line[2])
	        
	        strawberrys_eaten_list += [int(line[2])]
	        
	#Calculates and defines the mean of strawberries eaten.
	mean_strawberrys = strawberrys_eaten / strawberry_days
	
	#Creates a list of fruit names.
	all_fruit_names = ["apple","banana","strawberry"]
	
	#Loops through the fruit data to calculate the mean of all fruits eaten.
	for i in fruit_data:
		
	    line = i.split()
	    
	    fruit_name = line[1]
	    
	    if fruit_name in all_fruit_names:
			
	        fruit_days += 1
	        
	        fruits_eaten += int(line[2])
	        
	        fruits_eaten_list += [int(line[2])]
	        
	#Calculates and defines the mean of all fruits eaten.       
	mean_fruits = fruits_eaten / fruit_days
	
	#Formats the mean values to two decimal places and returns them as strings.
	return "{:.2f}".format(mean_apples),"{:.2f}".format(mean_bananas),"{:.2f}".format(mean_strawberrys),"{:.2f}".format(mean_fruits),
	
#This function calculates the medians for each fruit type and all fruits.
def Median (fruit_data_file):
	
	#Opens the fruit_data_file for reading.
	fruit_txt= open(fruit_data_file, "r")
	
	#Reads the lines of fruit data.
	fruit_data = fruit_txt.readlines()
	
	#Intializes a list for apples eaten.	
	apples_eaten_list = []
	
    #Loops through the fruit data to fill the list of apples eaten.
	for i in fruit_data:
		
		#Splits the lines into a list of strings.
		line = i.split()
		
		#Extracts the fruit name from element two.
		if line[1] == "apple":
			
			#Extracts the number of fruit eaten from element three.
			apples_eaten_list += [int(line[2])]
			
	#Sorts the list in ascending order.
	apples_eaten_list.sort()
	
	#Initialize the n variable to calculate length of the list (even or odd)
	n = len(apples_eaten_list)
	
	#If the length of the list is odd, the median is set to the middle value.
	if n % 2 != 0:
		
	    median_apples = apples_eaten_list[n // 2]
	
	#If the length of the list is even, the median is set to the average of the two middle elements.    
	else:
		
	    median_apples_1 = apples_eaten_list[n // 2 - 1]
	    
	    median_apples_2 = apples_eaten_list[n // 2]
	    
	    median_apples = (median_apples_1 + median_apples_2) / 2
	
	#Intializes a list for bananas eaten.  
	bananas_eaten_list = []
	
	#Loops through the fruit data to fill the list of bananas eaten.
	for i in fruit_data:
				
		line = i.split()
		
		if line[1] == "banana":
			
			bananas_eaten_list += [int(line[2])]
			
	bananas_eaten_list.sort()
	
	n = len(bananas_eaten_list)
	
	if n % 2 != 0:
		
	    median_bananas = bananas_eaten_list[n // 2]
	    
	else:
		
	    median_bananas_1 = bananas_eaten_list[n // 2 - 1]
	    
	    median_bananas_2 = bananas_eaten_list[n // 2]
	    
	    median_bananas = (median_bananas_1 + median_bananas_2) / 2
	
	#Intializes a list for strawberries eaten.    
	strawberrys_eaten_list = []
	
	#Loops through the fruit data to fill the list of strawberries eaten.
	for i in fruit_data:
		
		line = i.split()
		
		if line[1] == "strawberry":
			strawberrys_eaten_list += [int(line[2])]
			
	strawberrys_eaten_list.sort()
	
	n = len(strawberrys_eaten_list)
	
	if n % 2 != 0:
		
	    median_strawberrys = strawberrys_eaten_list[n // 2]
	    
	else:
		
	    median_strawberrys_1 = strawberrys_eaten_list[n // 2 - 1]
	    
	    median_strawberrys_2 = strawberrys_eaten_list[n // 2]
	    
	    median_strawberrys = (median_strawberrys_1 + median_strawberrys_2) / 2
	
	#Creates a list of all fruit names.
	all_fruit_names = ["apple","banana","strawberry"]
	
	#Intializes a list for all fruit eaten.
	fruits_eaten_list =[]
	
	#Loops through the fruit data to fill the list of all fruits eaten.
	for i in fruit_data:
		 
		line = i.split()
		
		fruit_name = line[1]
		
		#Checks if the fruit name is in the list of all_fruit_names
		if fruit_name in all_fruit_names:
			
			fruits_eaten_list += [int(line[2])]
			
	fruits_eaten_list.sort()
	
	n = len(fruits_eaten_list)
	
	if n % 2 != 0:
		
	    median_fruits = fruits_eaten_list[n // 2]
	 
	else:
		
	    median_fruits_1 = fruits_eaten_list[n // 2 - 1]
	    
	    median_fruits_2 = fruits_eaten_list[n // 2]
	    
	    median_fruits = (median_fruits_1 + median_fruits_2) / 2
	
	#Formats the median values to two decimal places and returns them as strings.
	return "{:.2f}".format(median_apples),"{:.2f}".format(median_bananas),"{:.2f}".format(median_strawberrys),"{:.2f}".format(median_fruits),
	
