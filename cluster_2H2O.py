#! /usr/bin/env python

"""
@author: bernardino.tirri@chimieparistech.psl.eu
"""



from sys import *
from math import pi,sqrt,exp,log
import os, string
from operator import itemgetter
import shutil
import os.path

############################## Starting      

param_CCSDT = ['0.95988','0.96872','1.9562','0.96172', '0.96172', '105.41977','109.63122', '109.63122','105.50831', '0.0', '0.0', '123.06345', '123.06345', '117.97929', '2.918782'  ]
definition_CCSDT  = ['r(O1-H2)', 'r(O1-H3)', 'r(H3-O4)==>r(O--H)', 'r(O4-H5)', 'r(O4-H6)', 'A(H2-O1-H3)',  'A(H3-O4-H5)', 'A(H3-O4-H6)', 'A(H5-O4-H6)', 'L(O1,H3,O4,H2,-H1)', 'L(O1,H3,O4,H2,-H2)', 'D(H2,O1,O4,H5)', 'D(H2,O1,O4,H6)', 'D(H3,O4,H5,H6)', 'r(O1-O4)==>r(O--O)']
name             = []
definition        = []
value             = []


##############################################################################################################


narg= 1 + 0
filename=argv[1:]


# read the command line
if (len(argv) <= narg) :
  print("Error in argument number")
  print("USAGE")
  print(argv[0]+" <g09_1.out> <g09_2.out> .... <g09_N.out>") 
  quit() 


info=[]
for file in filename :

  input=open(file,"r")	
  linee=input.readlines()
  
  for row in linee :
  
    #if some problem happend in the execution
    # of the g09 job under examination
    if (row.find("Error termination") != -1) :
      print("Error termination found in "+file)
      quit()
    
    # grep optimized structure in the output file
    #if (row.find("!   Optimized Parameters   !") != -1) :
    if (row.find("-DE/DX =    0.0                 !") != -1)  :
    #if (row.find("!   Optimized Parameters   !") != -1) :
      comment=row.split()
#      print row
            
      r_nam= comment[1].split()[0]
      r_def= comment[2].split()[0]
      #r_val=float(comment[3].split()[0])
      r_val=comment[3].split()[0]
      name.append(r_nam)
      definition.append(r_def)
      value.append(r_val)
                


      block=[ name, definition, value, param_CCSDT]
  input.close()



#print value
#print param_CCSDT 






ROW =[]

for file in filename :

  input=open(file,"r")	
  linee=input.readlines()
  
  for row in linee :

        comment=row.split()

        if (row.find("  4  O    ") != -1)  :
            oo=comment[2].split()[0]
            ROW.append(oo)

#for i,j in enumerate(ROW):
#    print i,j



#print ROW
for i,j in enumerate(ROW):
    if i == 6:
        value.append(j)

#print value
        
for i,j in enumerate(definition_CCSDT ):
    if i == 14:
        definition.append(j)
#print definition



error=[ abs(float(j) -abs(float(i))) for i,j in zip(value,param_CCSDT)]

#print mad, '\n'

print "\n"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "                       geometrical parameters cluster (H2O)2    ","\n"
print "               Definition                                 Err"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

for i,j in zip (definition_CCSDT,error):
#   print i, j
    print  ('{:^40}''{:^40}'.format (i, j ))

print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "\n"
print "R(O--H) = Hydrogen bond"
print "R(O--O) = Oxygen - Oxygen distances"
print "\n"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "\n"
print "Mean Absolute Deviation (MAD)","\n"

roh_mad=[]
for i,j in enumerate(error):
#   print i, j
   if i == 2:
       roh_mad.append(j)

#print roh_mad
ROH_mad=sum(roh_mad)/len(roh_mad)
#print R_mad


print "MAD R(O--H) = ", ROH_mad

roo_mad=[]
for i,j in enumerate(error):
#   print i, j
   if i == 14:
       roo_mad.append(j)

#print roo_mad
ROO_mad=sum(roo_mad)/len(roo_mad)
#print R_mad




print "MAD R(O--O) = ", ROO_mad

r_mad=[]
for i,j in enumerate(error):
#   print i, j
   if i > -1  and i < 5 :
       r_mad.append(j)
   if i == 14:
       r_mad.append(j)

#print r_mad
R_mad=sum(r_mad)/len(r_mad)
#print R_mad

print "MAD R(all bonds) = ", R_mad

a_mad=[]
for i,j in enumerate(error):
#   print i, j
   if (i > 4)  and (i < 9) :
#       print j
       a_mad.append(j)

#print a_mad
A_mad=sum(a_mad)/len(a_mad)
#print D_mad


print "MAD A(all angles) = ", A_mad


d_mad=[]
for i,j in enumerate(error):
#   print i, j
   if (i > 10)  and (i < 14) :
#       print j
       d_mad.append(j)

#print d_mad
D_mad=sum(d_mad)/len(d_mad)
#print D_mad


print "MAD D(all dihedral) = ", D_mad
print "\n"





            
