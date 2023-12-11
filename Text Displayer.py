import tkinter as tk
import time

def generate_live_data():
    with open('data_file.txt', 'r') as file:
        data = list(map(float,file.read().split(' ')))
        print(data)
    time.sleep(1)
    return data

def update_data():
    all_values = generate_live_data()
    thumbSensor = all_values[0]
    indexSensor = all_values[1]
    middleSensor = all_values[2]
    ringSensor = all_values[3]
    pinkySensor = all_values[4]
    wristSensor = all_values[5]
    thumbCurl = thumbSensor < 500
    wristCurl = wristSensor < 1000
    pinkyCurl = pinkySensor < 1000
    indexCurl = indexSensor < 200
    middleCurl = middleSensor < 420

    if  middleCurl == False and indexCurl == False and thumbCurl == True and pinkyCurl == True  :
        canvas.itemconfig(text_item, text="PEACE", fill="red")
    elif middleCurl == True and indexCurl == True and thumbCurl == False and pinkyCurl == False :
        canvas.itemconfig(text_item, text="CALL", fill="red")
    # elif middleCurl == False and indexCurl == True and thumbCurl == True and pinkyCurl == True :
    #     canvas.itemconfig(text_item, text="F U", fill="red")
    elif middleCurl == True and indexCurl == True and thumbCurl == False and pinkyCurl == True :
        canvas.itemconfig(text_item, text="HELP", fill="red")
    elif middleCurl == True and indexCurl == False and thumbCurl == False and pinkyCurl == False :
        canvas.itemconfig(text_item, text="YO!", fill="red")
    else:
        canvas.itemconfig(text_item, text="R U READY!?", fill="red")

    # Schedule the next update after 1000 milliseconds (1 second)
    root.after(1000, update_data)


# Create the main window
root = tk.Tk()
root.title("The Fun Part")

# Create a canvas widget
canvas = tk.Canvas(root, width=1500, height=800, bg="black")
canvas.pack()

# Create text directly on the canvas
text_item = canvas.create_text(375, 200, text="", font=("Arial", 75))

# Schedule the initial update and subsequent updates
update_data()

# Run the main loop
root.mainloop()
