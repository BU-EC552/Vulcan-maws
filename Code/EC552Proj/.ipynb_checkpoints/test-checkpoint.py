# EC 552 Project
# Test File

"""
    Skeleton Code:

    1. Download and open pdb file
    2. Do the operations (math) on the pdb file
    3.
    4.

"""
import pytraj as pt  # pytraj stuff
from pytraj.utils.progress import ProgressBarTrajectory

# using pdb file
# traj4 = pt.load("1gwd.v5.cif")

# print("Traj4:")
# print(traj4)

#loading in with iter
traj2 = pt.iterload("heat1.mdcrd", "1gwd.v5.cif")
print("Traj2:")
print(traj2)


#prog = ProgressBarTrajectory(traj2, style='circle')
pt.molsurf(traj2, '@C')



# make changes to file (MATH STUFF HAPPENS!??)
# traj3 = traj2[2:8:2, '!@C=']


# print(traj3.topology())


# print("Changed:")
# print(traj3)

# # saving to new file
# basename = "nickysims.pdb"
# traj3.save(basename, overwrite=True)

#opening the file
# traj = pt.iterload("nickysims.pdb")
# print("nick:")
# print(traj)

# #testing time
# basename = "copyTest.pdb"
# traj.save(basename, overwrite=True)



#_________________________

# loading other files 
# traj3 = pt.load("1gwd.v5.cif")
# print(traj3)



# testing Github link from Jackson


# print("hello")

# traj = pt.iterload("heat1.mdcrd", "1gwd.v5.cif") # loads in the files
# pt.rmsd(traj, mask='@CA', ref=0)
# pt.dssp(traj, mask=':2-16')
# # pt.pca(traj, mask='!@H=', n_vecs=2)

# print("bye")
