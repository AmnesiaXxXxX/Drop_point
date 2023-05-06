import math
import os
import pyperclip

# given coordinates
gps_target_data = str(input("Send the point from the clipboard: "))
gps_planet_data = str(input("Send the point of center planet from the clipboard: "))
height = float(input("Send height: "))
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
result = "GPS:Drop point:{}:{}:{}:#F17575:".format(drop_point[0], drop_point[1], drop_point[2])
print("The result was copied to the clipboard \n",result)
pyperclip.copy(result)
cnfr = input("Press any key to continue")
