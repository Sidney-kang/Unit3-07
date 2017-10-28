# Created by : Sidney Kang
# Created on : 18 Oct. 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-07
# This program displays a for loop program with range()

import ui

def calculate_factorial_touch_up_inside(sender):
	
    #variable
    counter = 1
    current_factorial_value = 1
    
    #input
    user_input = int(view['user_input_textbox'].text)
    
    #process 
    if user_input < 0:
    	 #output
       view['factorial_check_label'].text = "Please enter a non negative value."
       return
       
    for loop_counter in range(1,user_input + 1):
        current_factorial_value = counter * current_factorial_value      
        counter = counter + 1  
        #output          
        view['factorial_check_label'].text = "The factorial is: " + str(current_factorial_value)

view = ui.load_view()
view.present('sheet')
