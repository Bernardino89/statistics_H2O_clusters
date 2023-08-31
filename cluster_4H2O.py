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
import numpy as np

############################## Starting      

definition_CCSDT  =['R(O1,H2)  ',  'R(O1,H3)  ',  'R(O1,H5)==>R(O--H)  ',  'R(H2,O10) ==>R(O--H)',  'R(O4,H5)  ',  'R(O4,H6)  ',  'R(O4,H8)==>R(O--H)  ',  'R(O7,H8)  ',  'R(O7,H9)  ',  'R(O7,H11)==>R(O--H) ',  'R(O10,H11)',  'R(O10,H12)',  'A(H2,O1,H3)  ',  'A(H2,O1,H5)  ',  'A(H3,O1,H5)  ',  'A(H5,O4,H6)  ',  'A(H5,O4,H8)  ',  'A(H6,O4,H8)  ',  'A(H8,O7,H9)  ',  'A(H8,O7,H11) ',  'A(H9,O7,H11) ',  'A(H2,O10,H11)',  'A(H2,O10,H12)',  'A(H11,O10,H12)',  'L(H1,2,10,8,-1) ',  'L(H1,5,4,11,-1) ',  'L(H4,8,7,2,-1)  ',  'L(o7,11,10,5,-1)',  'L(O1,2,10,8,-2) ',  'L(O1,5,4,11,-2) ',  'L(O4,8,7,2,-2)  ',  'L(H7,11,10,5,-2)',  'D(H2,O1,O4,H6)   ',  'D(H2,O1,O4,H8)   ',  'D(H3,O1,O4,H6)   ',  'D(H3,O1,O4,H8)   ',  'D(H3,O1,O10,H11) ',  'D(H3,O1,O10,H12) ',  'D(H5,O1,O10,H11) ',  'D(H5,O1,O10,H12) ',  'D(H5,O4,O7,H9)   ',  'D(H5,O4,O7,H11)  ',  'D(H6,O4,O7,H9)   ',  'D(H6,O4,O7,H11)  ',  ' D(H8,O7,O10,H2', 'D(H8,O7,O10,H12)', 'D(H9,O7,O10,H2)', 'D(H9,O7,O10,H12)', 'R(O1,O4)==>R(O--O)  ', 'R(O1,O10)==>R(O--O)', 'R(O7,O4)==>R(O--O)', 'R(O7,O10)==>R(O--O)'] 



param_CCSDT = ['0.9737    ','0.9518    ','1.7504    ','1.7504    ','0.9737    ','0.9518    ','1.7504    ','0.9737    ','0.9518    ','1.7504    ','0.9737    ','0.9518    ','106.0371  ','102.5525  ','120.315   ','106.0371  ','102.5525  ','120.315   ','106.0371  ','102.5525  ','120.315   ','102.5525  ','120.315   ','106.0371  ','167.4397  ','167.4397  ','167.4397  ','167.4397  ','180.9892  ','180.9892  ','179.0108  ','180.9892  ','123.1549  ','1.4833    ','121.9313  ','113.4305  ','123.1549  ','121.9313  ','1.4833    ','113.4305  ','123.1549  ','1.4833    ','121.9313  ','113.4305  ','1.4833    ','123.1549  ','113.4305  ','121.9313  ',  '2.748959 ', '2.748959', '2.748959', '2.748959' ]




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
    if (row.find("-DE/DX =    0.0") != -1) or (row.find("-DE/DX =   -0.000") != -1)  :
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
        if (row.find("    10  O    ") != -1)  :
            oo=comment[2].split()[0]
            ROW.append(oo)
        if (row.find("  7  O    ") != -1)  :
            oo=comment[-2].split()[0]
            ROW.append(oo)

O7x=[]
O7y=[]
O7z=[]
O10x=[]
O10y=[]
O10z=[]


for file in filename :

  input=open(file,"r")	
  linee=input.readlines()
  
  for row in linee :

        comment=row.split()

        if (row.find(" 7          8           0 ") != -1)  :
            O7X=comment[-3].split()[0]
            O7Y=comment[-2].split()[0]
            O7Z=comment[-1].split()[0]
            O7x.append(O7X)
            O7y.append(O7Y)
            O7z.append(O7Z)
        if (row.find("10          8           0") != -1)  :
            O10X=comment[-3].split()[0]
            O10Y=comment[-2].split()[0]
            O10Z=comment[-1].split()[0]
            O10x.append(O10X)
            O10y.append(O10Y)
            O10z.append(O10Z)

O7O10=[(np.sqrt(((float(x2)-float(x1))**2) + ((float(y2)-float(y1))**2) + ((float(z2)-float(z1))**2))) for x1,x2, y1,y2, z1, z2 in zip(O7x, O10x,O7y, O10y,O7z, O10z)]


#for i,g in enumerate(ROW):
#    
#        print i,g
for i,j in enumerate(ROW):
    if i == 0: 
        #O1---O4
#        print "the 0 element is", j 
        value.append(j)
    if i == 1: 
        #O1--O10
#        print "the 1 element is", j 
        value.append(j)
    if i == 2:
        # O7---O4
#        print "the value 2 is", j
        value.append(j)


for i,j in enumerate(O7O10):
    if i==1:
        value.append(j)

#for i,j in enumerate(value):
#    print i,j


#print value

#print 'the value is :', value, "\n"
        
#for i,j in enumerate(definition_CCSDT ):
#    if i == 33:
#        #print j
#        definition.append(j)
#    if i == 34:
#        #print j
#        definition.append(j)
#    if i == 35:
#        #print j
#        definition.append(j)

#print 'the definition is:',definition, "\n"

error=[ abs(float(j) -abs(float(i))) for i,j in zip(value,param_CCSDT)]

#print mad, '\n'


print "\n"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "                       geometrical parameters cluster (H2O)4    ","\n"
print "               Definition                                 Err"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

for i,j in zip (definition_CCSDT,error):
#   print i, j
   print  ('{:^40}''{:^40}'.format (i, j ))

print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

print "R(O--H) = Hydrogen bond"
print "R(O--O) = Oxygen - Oxygen distances"
print "\n"

print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

print "\n"
print "Mean Absolute Deviation (MAD)","\n"

roh_mad=[]

#for i,j in enumerate(definition_CCSDT):
#   print i, j

for i,j in enumerate(error):
#   print i, j
    if i == 2:
       roh_mad.append(j)
    if i == 3:
       roh_mad.append(j)
    if i == 6:
       roh_mad.append(j)
    if i == 9:
       roh_mad.append(j)

#print roh_mad
ROH_mad=sum(roh_mad)/len(roh_mad)
#print R_mad

print "MAD R(O--H) = ", ROH_mad

roo_mad=[]
for i,j in enumerate(error):
    if i == 48:
       roo_mad.append(j)
    if i == 49:
       roo_mad.append(j)
    if i == 50:
       roo_mad.append(j)
    if i == 51:
       roo_mad.append(j)
#
#
#print roo_mad
ROO_mad=sum(roo_mad)/len(roo_mad)
#print R_mad

print "MAD R(O--O) = ", ROO_mad
#
r_mad=[]
for i,j in enumerate(error):
##   print i, j
   if i > -1  and i < 12 :
       r_mad.append(j)
   if i > 47  and i < 52 :
       r_mad.append(j)
#
#print r_mad
R_mad=sum(r_mad)/len(r_mad)
#print R_mad
#
print "MAD R(all bonds) = ", R_mad
#
a_mad=[]
for i,j in enumerate(error):
##   print i, j
   if (i > 11)  and (i < 24) :
##       print j
       a_mad.append(j)
#
#print a_mad
A_mad=sum(a_mad)/len(a_mad)
##print D_mad
#
#
print "MAD A(all angles) = ", A_mad
#
#
d_mad=[]
for i,j in enumerate(error):
#   print i, j
   if (i > 31)  and (i < 48) :
#       print j
       d_mad.append(j)
#
#
#print d_mad
D_mad=sum(d_mad)/len(d_mad)
#print D_mad
#
#
print "MAD D(all dihedral) = ", D_mad
print "\n"
#










