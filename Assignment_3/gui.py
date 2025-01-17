# Course: 		    CS 3642
# Assignment #: 	3
# Due Date: 		11/22/24

import tkinter as tk
from tkinter import ttk
import random

############### General Functions ###############

# Increase the number of epochs by 1 
def increase_num_epochs_one(current_label): 
    current_num_epochs = int(current_label["text"]) 
    if current_num_epochs < 1000: 
        current_label.config(text=str(current_num_epochs + 1))

# Increase the number of epochs by 10
def increase_num_epochs_ten(current_label): 
    current_num_epochs = int(current_label["text"]) 
    if current_num_epochs < 991: 
        current_label.config(text=str(current_num_epochs + 10))

# Decrease the number of epochs by 1
def decrease_num_epochs_one(current_label): 
    current_num_epochs = int(current_label["text"]) 
    if current_num_epochs > 1: 
        current_label.config(text=str(current_num_epochs - 1)) 
        
# Decrease the number of epochs by 10
def decrease_num_epochs_ten(current_label): 
    current_num_epochs = int(current_label["text"]) 
    if current_num_epochs > 10: 
        current_label.config(text=str(current_num_epochs - 10)) 

############### Pixel Perceptron Functions ###############

# Update initial weights pixel label 
def update_initial_weights_pixel(initial_weights): 
    initial_weights_pixel.config(text=str(initial_weights))

# Update final weights pixel label 
def update_final_weights_pixel(final_weights): 
    final_weights_pixel.config(text=str(final_weights))

def update_train_results_pixel(epoch, results): 
    results_str = "Epoch #" + epoch + "\nCorrectly classified " + results
    training_results_pixel.config(text=results_str)

# Update labels when pixel testing is complete 
def update_test_labels_pixel(results): 
    test_label_pixel.config(text=results)

bias_val = 1

pixel_weights = []

pixel_training_inputs = [

        [-1, -1, -1, 1, -1],
        [-1, -1, 1, -1, -1],
        [-1, -1, 1, 1, 1],
        [-1, 1, -1, -1, -1],
        [-1, 1, 1, -1, 1],
        [1, 1, 1, -1, 1],
        [-1, 1, -1, 1, 1],
        [1, -1, 1, -1, 1],
        [1, 1, 1, 1, 1], 
        [1, 1, -1, -1, 1],

    ]

pixel_testing_inputs = [
        
        [-1, -1, -1, -1, -1],
        [-1, 1, 1, 1, 1],
        [1, -1, -1, -1, -1],
        [1, -1, -1, 1, 1],
        [1, -1, 1, 1, 1],
        [1, 1, -1, 1, 1],

    ]

def pixel_training(target_epochs): 
    # Set initial values for weights, learning rate, target epochs

    global pixel_weights
    
    pixel_weights = [round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2)]

    update_initial_weights_pixel(pixel_weights)

    learning_rate = 0.1

    # Epoch count to keep track of completed epochs, initialized to zero 
    epoch_count = 0

    # Repeat until the target number of epochs has been completed 
    for epoch in range(target_epochs): 

        epoch_count += 1

        num_wrong = 0

        # Repeat for each pixel in the training inputs list 
        for pixel_input in pixel_training_inputs: 

            # Get the pixel values and expected output 
            pixel = pixel_input[:4]
            expected = pixel_input[-1]

            # Calculate the weighted sum for the bias neuron and the four pixels 
            weighted_sum_bias = bias_val * pixel_weights[0]
            weighted_sum_1 = pixel[0] * pixel_weights[1]
            weighted_sum_2 = pixel[1] * pixel_weights[2]
            weighted_sum_3 = pixel[2] * pixel_weights[3]
            weighted_sum_4 = pixel[3] * pixel_weights[4]

            # Calculate the total weighted sum 
            total_weighted_sum = weighted_sum_bias + weighted_sum_1 + weighted_sum_2 + weighted_sum_3 + weighted_sum_4
            output = -999

            # Determine the observed output 
            if (total_weighted_sum > -0.1): 
                output = 1
            else: 
                output = -1

            # Check if the observed output equals the expected output 
            if (output != expected): 

                # Increment the variable that tracks the number of incorrectly observed outputs per epoch 
                num_wrong += 1

                # Calculate the first part of the weight change calculation 
                partial_weight_change = learning_rate * (expected - output)

                # Calculate the weight change for each input 
                weight_change_bias = partial_weight_change * bias_val
                weight_change_1 = partial_weight_change * pixel[0]
                weight_change_2 = partial_weight_change * pixel[1]
                weight_change_3 = partial_weight_change * pixel[2]
                weight_change_4 = partial_weight_change * pixel[3]

                # Calculate the new weights 
                pixel_weights[0] += weight_change_bias
                pixel_weights[1] += weight_change_1
                pixel_weights[2] += weight_change_2
                pixel_weights[3] += weight_change_3
                pixel_weights[4] += weight_change_4

                # Round the weights 
                pixel_weights[0] = round(pixel_weights[0], 4)
                pixel_weights[1] = round(pixel_weights[1], 4)
                pixel_weights[2] = round(pixel_weights[2], 4)
                pixel_weights[3] = round(pixel_weights[3], 4)
                pixel_weights[4] = round(pixel_weights[4], 4)

    # Update the final weights label 
    update_final_weights_pixel(pixel_weights)

    # Update the training results label 
    results = str(len(pixel_training_inputs) - num_wrong) + "/" + str(len(pixel_training_inputs))
    update_train_results_pixel(str(epoch + 1), results)

    # Clear test results 
    update_test_labels_pixel("0 / 0")

def pixel_testing(): 
    global pixel_weights

    # Initialize the variables to track the number of correct tests 
    num_correct = 0

    # Repeat for each input in the testing inputs list 
    for pixel_input in pixel_testing_inputs: 

        # Get the pixel values and expected output 
        pixel = pixel_input[:4]
        expected = pixel_input[-1]

        # Calculate the weighted sum for the bias neuron and the four pixels 
        weighted_sum_bias = bias_val * pixel_weights[0]
        weighted_sum_1 = pixel[0] * pixel_weights[1]
        weighted_sum_2 = pixel[1] * pixel_weights[2]
        weighted_sum_3 = pixel[2] * pixel_weights[3]
        weighted_sum_4 = pixel[3] * pixel_weights[4]

        # Calculate the total weighted sum 
        total_weighted_sum = weighted_sum_bias + weighted_sum_1 + weighted_sum_2 + weighted_sum_3 + weighted_sum_4
        output = -999

        # Determine the observed output 
        if (total_weighted_sum > -0.1): 
            output = 1
        else: 
            output = -1

        # Check if the correct output was observed 
        if (output == expected): 
            # Increment the number of correct tests 
            num_correct += 1

    # Update the test results labels
    results = num_correct, "/", len(pixel_testing_inputs)
    update_test_labels_pixel(results)

############### Plant Perceptron Functions ###############

# Plant checker 
# If more than three attributes are "on", the plant does not need to be watered, otherwise it does need to 
# be watered

# Outputs:
#     (1)     Don't water the plant
#     (-1)    Water the plant 

# Attributes: 
#     (1) soil_mouisture -- good/bad
#     (2) healthy_leaves -- yes/no
#     (3) low_temperature -- yes/no
#     (4) high_humidity -- yes/no
#     (5) rainy_weather -- yes/no

# Update initial weights plant label 
def update_initial_weights_plant(initial_weights): 
    initial_weights_plant.config(text=str(initial_weights))

# Update final weights plant label 
def update_final_weights_plant(final_weights): 
    final_weights_plant.config(text=str(final_weights))

def update_train_results_plant(epoch, results): 
    results_str = "Epoch #" + epoch + "\nCorrectly classified " + results
    training_results_plant.config(text=results_str)

# Update labels when plant testing is complete 
def update_test_labels_plant(results): 
    test_label_plant.config(text=results)

plant_weights = []

plant_training_inputs = [

    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 1, -1],
    [-1, -1, 1, -1, -1, -1],
    [-1, -1, 1, -1, 1, -1],
    [-1, -1, 1, 1, -1, -1],
    [-1, 1, -1, -1, 1, -1],
    [-1, 1, -1, 1, -1, -1],
    [-1, 1, -1, 1, 1, 1],
    [-1, 1, 1, -1, -1, -1],
    [-1, 1, 1, 1, 1, 1],
    [1, -1, -1, -1, -1, -1],
    [1, -1, -1, -1, 1, -1],
    [1, -1, 1, -1, -1, -1],
    [1, -1, 1, -1, 1, 1],
    [1, -1, 1, 1, -1, 1],
    [1, -1, 1, 1, 1, 1],
    [1, 1, -1, 1, -1, 1],
    [1, 1, 1, -1, -1, 1],
    [1, 1, 1, -1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

plant_testing_inputs = [
    
    [-1, -1, -1, 1, -1, -1],
    [-1, -1, -1, 1, 1, -1],
    [-1, -1, 1, 1, 1, 1],
    [-1, 1, -1, -1, -1, -1],
    [-1, 1, 1, -1, 1, 1],
    [-1, 1, 1, 1, -1, 1],
    [1, -1, -1, 1, -1, -1],
    [1, -1, -1, 1, 1, 1],
    [1, 1, -1, -1, -1, -1],
    [1, 1, -1, -1, 1, 1],
    [1, 1, -1, 1, 1, 1],
    [1, 1, 1, 1, -1, 1]

]

def plant_training(target_epochs): 
    global plant_weights

    # Set initial values for weights, learning rate, target epochs

    global plant_weights
    
    plant_weights = [round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2)]
    update_initial_weights_plant(plant_weights)
    
    learning_rate = 0.1

    # Epoch count to keep track of completed epochs, initialized to zero 
    epoch_count = 0

    # Repeat until the target number of epochs has been completed 
    for epoch in range(target_epochs): 

        epoch_count += 1

        num_wrong = 0

        # Repeat for each plant_info input in the training inputs list 
        for plant_info_input in plant_training_inputs: 

            # Get the plant_info values and expected output 
            plant_info = plant_info_input[:5]
            expected = plant_info_input[-1]

            # Calculate the weighted sum for the bias neuron and the five plant_info attributes
            weighted_sum_bias = bias_val * plant_weights[0]
            weighted_sum_1 = plant_info[0] * plant_weights[1]
            weighted_sum_2 = plant_info[1] * plant_weights[2]
            weighted_sum_3 = plant_info[2] * plant_weights[3]
            weighted_sum_4 = plant_info[3] * plant_weights[4]
            weighted_sum_5 = plant_info[4] * plant_weights[5]

            # Calculate the total weighted sum 
            total_weighted_sum = weighted_sum_bias + weighted_sum_1 + weighted_sum_2 + weighted_sum_3 + weighted_sum_4 + weighted_sum_5
            output = -999

            # Determine the observed output 
            if (total_weighted_sum > -0.1): 
                output = 1
            else: 
                output = -1

            # Check if the observed output equals the expected output 
            if (output != expected): 

                # Increment the variable that tracks the number of incorrectly observed outputs per epoch 
                num_wrong += 1

                # Calculate the first part of the weight change calculation 
                partial_weight_change = learning_rate * (expected - output)

                # Calculate the weight change for each input 
                weight_change_bias = partial_weight_change * bias_val
                weight_change_1 = partial_weight_change * plant_info[0]
                weight_change_2 = partial_weight_change * plant_info[1]
                weight_change_3 = partial_weight_change * plant_info[2]
                weight_change_4 = partial_weight_change * plant_info[3]
                weight_change_5 = partial_weight_change * plant_info[4]

                # Calculate the new plant_weights 
                plant_weights[0] += weight_change_bias
                plant_weights[1] += weight_change_1
                plant_weights[2] += weight_change_2
                plant_weights[3] += weight_change_3
                plant_weights[4] += weight_change_4
                plant_weights[5] += weight_change_5

                # Round the weights 
                plant_weights[0] = round(plant_weights[0], 4)
                plant_weights[1] = round(plant_weights[1], 4)
                plant_weights[2] = round(plant_weights[2], 4)
                plant_weights[3] = round(plant_weights[3], 4)
                plant_weights[4] = round(plant_weights[4], 4)
                plant_weights[5] = round(plant_weights[5], 4)

    # Update the final weights label 
    update_final_weights_plant(plant_weights)

    # Update the training results label 
    results = str(len(plant_training_inputs) - num_wrong) + "/" + str(len(plant_training_inputs))
    update_train_results_plant(str(epoch + 1), results)

    # Clear test results 
    update_test_labels_plant("0 / 0")

def plant_testing(): 

    global plant_weights

    # Initialize the variables to track the number of correct tests 
    num_correct = 0

    # Repeat for each input in the testing inputs list 
    for plant_info_input in plant_testing_inputs: 

        # Get the plant_info values and expected output 
        plant_info = plant_info_input[:5]
        expected = plant_info_input[-1]

        # Calculate the weighted sum for the bias neuron and the five plant_info attributes
        weighted_sum_bias = bias_val * plant_weights[0]
        weighted_sum_1 = plant_info[0] * plant_weights[1]
        weighted_sum_2 = plant_info[1] * plant_weights[2]
        weighted_sum_3 = plant_info[2] * plant_weights[3]
        weighted_sum_4 = plant_info[3] * plant_weights[4]
        weighted_sum_5 = plant_info[4] * plant_weights[5]

        # Calculate the total weighted sum 
        total_weighted_sum = weighted_sum_bias + weighted_sum_1 + weighted_sum_2 + weighted_sum_3 + weighted_sum_4 + weighted_sum_5
        output = -999

        # Determine the observed output 
        if (total_weighted_sum > -0.1): 
            output = 1
        else: 
            output = -1

        # Check if the correct output was observed 
        if (output == expected): 
            # Increment the number of correct tests 
            num_correct += 1

    # Update the test results labels
    results = num_correct, "/", len(plant_testing_inputs)
    update_test_labels_plant(results)

############### Tkinter GUI setup ############### 

# Set up the window 
root = tk.Tk()
root.title("Assignment #3 - Perceptrons")

# Create a notebook for the tabs 
notebook = ttk.Notebook(root)

# Create a frame for each tab 
pixel_tab = ttk.Frame(notebook)
plant_tab = ttk.Frame(notebook)

# Create the tabs in the notebook 
notebook.add(pixel_tab, text="Image Perceptron")
notebook.add(plant_tab, text="Real World Perceptron")
notebook.pack(expand=True, fill='both')

############### Pixel Perceptron Tab ############### 

### Epoch Control ### 

# Label for the num epochs
epochs_label_pixel = tk.Label(pixel_tab, text="Number of Epochs", width=5, font=("Helvetica", 16))
epochs_label_pixel.grid(row=1, column=1, columnspan=5, padx=10, pady=5, sticky="ew")

# Label to display the number of epochs 
num_epochs_label_pixel = tk.Label(pixel_tab, text="10", width=5, font=("Helvetica", 16))
num_epochs_label_pixel.grid(row=2, column=3, padx=10, pady=5)

# Button to decrease the number of epochs by 1
decrease_epochs_button_pixel = tk.Button(pixel_tab, text="<", command=lambda: decrease_num_epochs_one(num_epochs_label_pixel), width=3)
decrease_epochs_button_pixel.grid(row=2, column=2, padx=10, pady=5)

# Button to decrease the number of epochs by 10
decrease_epochs_button_pixel = tk.Button(pixel_tab, text="<<", command=lambda: decrease_num_epochs_ten(num_epochs_label_pixel), width=3)
decrease_epochs_button_pixel.grid(row=2, column=1, padx=10, pady=5)

# Button to increase the number of epochs by 1
increase_epochs_button_pixel = tk.Button(pixel_tab, text=">", command=lambda: increase_num_epochs_one(num_epochs_label_pixel), width=3)
increase_epochs_button_pixel.grid(row=2, column=4, padx=10, pady=5)

# Button to increase the number of epochs by 10
increase_epochs_button_pixel = tk.Button(pixel_tab, text=">>", command=lambda: increase_num_epochs_ten(num_epochs_label_pixel), width=3)
increase_epochs_button_pixel.grid(row=2, column=5, padx=10, pady=5)

### Training and Testing ### 

# Button to train 
train_button_pixel = tk.Button(pixel_tab, text="Train", command=lambda: pixel_training(int(num_epochs_label_pixel["text"])), width=10)
train_button_pixel.grid(row=4, column=3, padx=10, pady=5)

# Button to test 
train_button_pixel = tk.Button(pixel_tab, text="Test", command=pixel_testing, width=10)
train_button_pixel.grid(row=5, column=3, padx=10, pady=5)

### Results Labels ### 

# Initial weights labels 
initial_weights_header_pixel = tk.Label(pixel_tab, text="Initial weights:", width=20, font=("Helvetica", 16))
initial_weights_header_pixel.grid(row=1, column=6, padx=10, pady=5)

initial_weights_pixel = tk.Label(pixel_tab, text="n/a", width=30, font=("Helvetica", 16))
initial_weights_pixel.grid(row=2, column=6, padx=10, pady=5)

# Final weights labels 
final_weights_header_pixel = tk.Label(pixel_tab, text="Final weights:", width=20, font=("Helvetica", 16))
final_weights_header_pixel.grid(row=4, column=6, padx=10, pady=5)

final_weights_pixel = tk.Label(pixel_tab, text="n/a", width=30, font=("Helvetica", 16))
final_weights_pixel.grid(row=5, column=6, padx=10, pady=5)

# Training results labels 
training_results_header_pixel = tk.Label(pixel_tab, text="Training results:", width=20, font=("Helvetica", 16))
training_results_header_pixel.grid(row=6, column=6, padx=10, pady=5)

training_results_pixel = tk.Label(pixel_tab, text="n/a", width=30, font=("Helvetica", 16))
training_results_pixel.grid(row=7, column=6, padx=10, pady=5)

# Test results labels 
test_header_label_pixel = tk.Label(pixel_tab, text="Test results:", width=20, font=("Helvetica", 16))
test_header_label_pixel.grid(row=1, column=7, padx=10, pady=5)

test_label_pixel = tk.Label(pixel_tab, text="0 / 0", width=20, font=("Helvetica", 16))
test_label_pixel.grid(row=2, column=7, padx=10, pady=5)

############### Plant Perceptron Tab ############### 

### Epoch Control ### 

# Label for the num epochs
epochs_label_plant = tk.Label(plant_tab, text="Number of Epochs", width=5, font=("Helvetica", 16))
epochs_label_plant.grid(row=1, column=1, columnspan=5, padx=10, pady=5, sticky="ew")

# Label to display the number of epochs 
num_epochs_label_plant = tk.Label(plant_tab, text="10", width=5, font=("Helvetica", 16))
num_epochs_label_plant.grid(row=2, column=3, padx=10, pady=5)

# Button to decrease the number of epochs by 1
decrease_epochs_button_plant = tk.Button(plant_tab, text="<", command=lambda: decrease_num_epochs_one(num_epochs_label_plant), width=3)
decrease_epochs_button_plant.grid(row=2, column=2, padx=10, pady=5)

# Button to decrease the number of epochs by 10
decrease_epochs_button_plant = tk.Button(plant_tab, text="<<", command=lambda: decrease_num_epochs_ten(num_epochs_label_plant), width=3)
decrease_epochs_button_plant.grid(row=2, column=1, padx=10, pady=5)

# Button to increase the number of epochs by 1
increase_epochs_button_plant = tk.Button(plant_tab, text=">", command=lambda: increase_num_epochs_one(num_epochs_label_plant), width=3)
increase_epochs_button_plant.grid(row=2, column=4, padx=10, pady=5)

# Button to increase the number of epochs by 10
increase_epochs_button_plant = tk.Button(plant_tab, text=">>", command=lambda: increase_num_epochs_ten(num_epochs_label_plant), width=3)
increase_epochs_button_plant.grid(row=2, column=5, padx=10, pady=5)

### Training and Testing ### 

# Button to train 
train_button_plant = tk.Button(plant_tab, text="Train", command=lambda: plant_training(int(num_epochs_label_plant["text"])), width=10)
train_button_plant.grid(row=4, column=3, padx=10, pady=5)

# Button to test 
train_button_plant = tk.Button(plant_tab, text="Test", command=plant_testing, width=10)
train_button_plant.grid(row=5, column=3, padx=10, pady=5)

### Results Labels ### 

# Initial weights labels 
initial_weights_header_plant = tk.Label(plant_tab, text="Initial weights:", width=20, font=("Helvetica", 16))
initial_weights_header_plant.grid(row=1, column=6, padx=10, pady=5)

initial_weights_plant = tk.Label(plant_tab, text="n/a", width=30, font=("Helvetica", 16))
initial_weights_plant.grid(row=2, column=6, padx=10, pady=5)

# Final weights labels 
final_weights_header_plant = tk.Label(plant_tab, text="Final weights:", width=20, font=("Helvetica", 16))
final_weights_header_plant.grid(row=4, column=6, padx=10, pady=5)

final_weights_plant = tk.Label(plant_tab, text="n/a", width=30, font=("Helvetica", 16))
final_weights_plant.grid(row=5, column=6, padx=10, pady=5)

# Training results labels 
training_results_header_plant = tk.Label(plant_tab, text="Training results:", width=20, font=("Helvetica", 16))
training_results_header_plant.grid(row=6, column=6, padx=10, pady=5)

training_results_plant = tk.Label(plant_tab, text="n/a", width=30, font=("Helvetica", 16))
training_results_plant.grid(row=7, column=6, padx=10, pady=5)

# Test results labels 
test_header_label_plant = tk.Label(plant_tab, text="Test results:", width=20, font=("Helvetica", 16))
test_header_label_plant.grid(row=1, column=7, padx=10, pady=5)

test_label_plant = tk.Label(plant_tab, text="0 / 0", width=20, font=("Helvetica", 16))
test_label_plant.grid(row=2, column=7, padx=10, pady=5)

root.mainloop()