# EC 552 Project

"""
Authors: Antoine Baize, Hannah Collins,
            Mariafernanda Hernandez, Nick Simone

"""

import pytraj as pt
import numpy as np


# MAWS math functions
def sum_a(nested_array):

    output = list(nested_array[0])
    n_a = list(nested_array)
    for i in range(1, len(n_a)):
        for j in range(len(n_a[0])):
            output[j] += n_a[i][j]

    return output


def power(array, a):
    output = [elem**a for elem in array]
    return output


def power2(array_nested, a):
    output = [power(elem, a) for elem in array_nested]
    return output


# asking user to load in a file
file_name = str(input("Which .pdb file would you like to load?\n"))

# import the pdb file
traj = pt.iterload(file_name)
top = traj.topology

print("\nInitial:", traj, "\n")


# data = pt.energy_decomposition(traj, igb=8)
# print("data:", data)

count1 = 0
print("The first five residues:")
for b in traj.topology.residues:
    print(b)
    count1 = count1+1
    if count1 == 5:
        break
print("\n")

# Accessing the atom's general information
count = 0
print("The first five atoms:")
for b in traj.topology.atoms:
    print(b)
    count = count+1
    if count == 5:
        break
print("\n")

# accessing the atom coordinates
xyz_raw = []
count2 = 0
print("Coordinates of the first 5 atoms")
for i in traj[0]:
    if count2 < 5:
        print("Atom #", count2+1 ,"Coordinates:", i)
        count2 = count2+1
    xyz_raw.append(i)


print("\n---------------------------------------------------------------\n")


# generating the box
longest_distance = max(power(sum_a(power2(list(xyz_raw), 2)), 0.5)) + 10
box_x = max([abs(xyz_raw[i][0]) for i in range(len(xyz_raw))]) + 10
box_y = max([abs(xyz_raw[i][1]) for i in range(len(xyz_raw))]) + 10
box_z = max([abs(xyz_raw[i][2]) for i in range(len(xyz_raw))]) + 10
print("Generating the bounding box.....\n")


# generating X random locations on the box
x_loc = 5
randX = np.random.uniform(low=0.0, high=box_x, size=(x_loc,))
randY = np.random.uniform(low=0.0, high=box_y, size=(x_loc,))
randZ = np.random.uniform(low=0.0, high=box_z, size=(x_loc,))

print("Generating the random locations on the box.....\n")

# adding the random locations to their respective arrays
t1_arr = np.array([[[randX[0], randY[0], randZ[0]]]])
t1_xyz = traj.xyz
t1_xyz = np.column_stack((t1_xyz, t1_arr))

# same for t2
t2_arr = np.array([[[randX[1], randY[1], randZ[1]]]])
t2_xyz = traj.xyz
t2_xyz = np.column_stack((t2_xyz, t2_arr))

# t3
t3_arr = np.array([[[randX[2], randY[2], randZ[2]]]])
t3_xyz = traj.xyz
t3_xyz = np.column_stack((t3_xyz, t3_arr))

# t4
t4_arr = np.array([[[randX[3], randY[3], randZ[3]]]])
t4_xyz = traj.xyz
t4_xyz = np.column_stack((t4_xyz, t4_arr))

# t5
t5_arr = np.array([[[randX[4], randY[4], randZ[4]]]])
t5_xyz = traj.xyz
t5_xyz = np.column_stack((t5_xyz, t5_arr))

print("Appending each random location to a new array containing atom coordinates\n")
print("At these locations we would have tested different nucleotides")
print(" and would have calculated the entropy at each location\n")


# data = amb.esander(traj, igb=8)
# print(data)
# print("gb:", data['gb'])
# print("bond:", data['bond'])


# saving the changes onto a new pdb file
# basename = "copyTest.pdb"
# traj.save(basename, overwrite=True)
