import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as n

# Define Paramedian length and interpupillary breadth in mm
paramedian = 48.8
interpup = 54.5

# Set range of depths between 80 mm and 150 mm at 1 mm intervals
depth = n.arange(80,150)

# Calculate spot size as function of depth. Argument of tangent is half angle
# of sensor in question's FoV
phi = 2*depth*n.tan(n.deg2rad(6))

# Calculate linear tolerances v. depth
deltax = 0.5*(interpup-phi)
deltay = 0.5*(paramedian-phi)

# Calculate angular tolerances v. depth, covert to deg
alphax = n.degrees(n.arctan(deltax/depth))
alphay = n.degrees(n.arctan(deltay/depth))

# Plot angular tolerances
fig = plt.figure()
sub = fig.add_subplot(111)
sub.set_xlabel("Depth (mm)")
sub.set_ylabel("Angular tolerance (degrees)")
sub.set_title("MLX60914-DCH Angular Tolerance")
xline = sub.plot(depth, alphax)
yline = sub.plot(depth, alphay)
plt.show()