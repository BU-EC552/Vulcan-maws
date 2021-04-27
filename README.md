# VulCan
README

VulcAn is a software tool that extracts information from input protein files, including:
	- trajectory and topology
 	- atom residue locations and information
The tool also performs the first steps of in-silico aptamer generation by:
	- generating a bounding box
	- performing random sampling 

The code is written in python.
To run: 
	Download our GitHub code
	In terminal:
		cd Code
		cd EC552Proj
		python3 test.py
User will be prompted to enter a file [input].pdb, and molecular information will be printed as an output.

Python modules pytraj and numpy must be installed prior to use.
The pdb file must be saved in the EC552Proj folder.
