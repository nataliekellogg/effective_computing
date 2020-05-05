"""
OCEAN506 Effective Computing code practice

Unimaginative code for using argparse, making arrays, 
trying methods, and saving output as a pickle file. 
"""
# imports
import sys, os
import numpy as np
import pickle

# determine file
filename = sys.argv[1]


## make arrays
aa = np.array(np.arange(16)).reshape((4,4))
bb = np.array(np.arange(16)).reshape((4,4))

#reshape arrays
arraa = np.reshape(aa,(2,8))
arrbb = np.reshape(bb,(8,2))

#print arrays
print ("Array aa:", arraa)
print ("Array bb:", arrbb)
 
##Find out attributes of array aa 

#number of axes
print ("Number of axes:", arraa.ndim)
#shape of array
print("Shape:", arraa.shape)
#total number of elements
print ("Total number of elements:", arraa.size)


## Some extra methods to try out 

#concatenate arrays
print("Concatenate arrays aa and bb:" ,np.concatenate((arraa,arrbb), axis=1))

#maximum along a given axis
print ("Maximum of axis 1:", np.amax(arraa, axis=1)

#minimum along a given axis
#print ("Minimum of axis 1:", np.amin(arraa, axis=1)

#standard deviation of the array elements along given axis
#print ("Standard deviation of axis 1:", np.std(arraa, axis=1)

#open file for writing
#outfile = open(filename,'wb')

#make pickle file of array aa
#pickle.dump(arraa,outfile)

#load pickle file back
#infile = open(filename,'rb')
#new_arraa = pickle.load(infile)


#What does the array look like now 
#print("Shape:", new_arraa.shape)