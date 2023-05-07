import math
import os
from py_compile import PyCompileError
import pyperclip
import tkinter as tk



def calculate():
    gps_target_get = target_coordinates_entry.get()
    gps_planet_get = planet_coordinates_entry.get()
    gps_target_data = str(gps_target_get)
    gps_planet_data = str(gps_planet_get)

    height_get = height_entry.get()
    height = int(height_get)

    coordinates = gps_target_data.split(':')
    planet_coordinates = gps_planet_data.split(':')

    x = float(coordinates[2])
    y = float(coordinates[3])
    z = float(coordinates[4])

    x_p = float(planet_coordinates[2])
    y_p = float(planet_coordinates[3])
    z_p = float(planet_coordinates[4])

    print("x=",x ,"\n", "y=",y,"\n","z=",z)
    print("x=",x_p ,"\n", "y=",y_p,"\n","z=",z_p)
    target = [x, y, z]
    planet_center = [x_p, y_p, z_p]

    # calculating the vertical vector
    vertical_vector = [target[i] - planet_center[i] for i in range(3)]

    # calculating the normalized vertical vector
    vector_length = math.sqrt(sum([component**2 for component in vertical_vector]))
    normalized_vector = [component / vector_length for component in vertical_vector]

    # calculating the drop point
    drop_point = [target[i] + normalized_vector[i]*height for i in range(3)]

    # formatting the result
    global result
    result = "GPS:Drop point:{}:{}:{}:#F17575:".format(drop_point[0], drop_point[1], drop_point[2])
    print("The result was copied to the clipboard \n",result)
    pyperclip.copy(result)
    cnfr = input("Press any key to continue")
    root.destroy()


root = tk.Tk()
root.title("Drop point calculator")
root.geometry("600x400")

# Create labels
planet_coordinates_label = tk.Label(root, text=f"Field for entering the coordinates of the center of the planet:")
target_coordinates_label = tk.Label(root, text=f"Target coordinates entry field:")
height_label = tk.Label(root, text=f"Height entry field:")

# Create input fields
planet_coordinates_entry = tk.Entry(root)
target_coordinates_entry = tk.Entry(root)

height_entry = tk.Entry(root)

# Associate labels with input fields
planet_coordinates_label['anchor'] = 'w'
planet_coordinates_label['width'] = 50
planet_coordinates_label['height'] = 2
planet_coordinates_label['font'] = ('Arial', 14)
planet_coordinates_label.pack()
planet_coordinates_entry.pack()

target_coordinates_label['anchor'] = 'w'
target_coordinates_label['width'] = 30
target_coordinates_label['height'] = 2
target_coordinates_label['font'] = ('Arial', 14)
target_coordinates_label.pack()
target_coordinates_entry.pack()

height_label['anchor'] = 'w'
height_label['width'] = 30
height_label['height'] = 2
height_label['font'] = ('Arial', 14)
height_label.pack()
height_entry.pack()

pce = tk.Button(root,command) 
pce.pack()

tce = tk.Button(root)
pce.pack()

sumbit_button = tk.Button(command=calculate)
sumbit_button.pack()

root.mainloop()
