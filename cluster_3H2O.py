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

#param_CCSDT = ['0.9743','0.9601','1.9089','1.9343', '0.9601', '0.9751','1.9096', '0.975','0.9604', '106.3925', '89.7073', '123.7461', '149.1012', '127.2891', '88.7886','106.3134', '151.6023', '88.6509', '121.0746', '106.1425', '151.5579' , '-136.1102', '-10.8313', '3.1749', '112.8079', '120.9425', '11.246', '-1.2729', '-129.9701', '-1.149', '-109.2388', '1.041', '123.0919', '2.81517', '2.80496', '2.80594'  ]
definition_CCSDT  = ['r(O1-H2)', 'r(O1-H3)', 'r(O1-H8)==>R(O--H)','r(H2-O4)==>R(O--H)' , 'r(O4-H5)', 'r(O4-H6)', 'r(H6-O7)==>R(O--H)', 'r(O7-H8)', 'r(O7-H9)', 'A(H2-O1-H3)','A(H2-O1-H8)' , 'A(H3-O1-H8)', 'A(O1-H2-O4)' , 'A(H2-O4-H5)', 'A(H2-O4-H6)', 'A(H5-O4-H6)', 'A(O4-H6-O7)'  , 'A(H6-O7-H8)', 'A(H6-O7-H9)', 'A(H8-O7-H9)', 'A(O1-H8-O7)', 'D(H3,O1,H2,O4)', 'D(H8,O1,H2,O4)', 'D(H2,O1,H8,O7)', 'D(H3,O1,H8,O7)', 'D(O1,H2,O4,H5)', 'D(O1,H2,O4,H6)', 'D(H2,O4,H6,O7)', 'D(H5,O4,H6,O7)', 'D(O4,H6,O7,H8)', 'D(O4,H6,O7,H9)', 'D(H6,O7,H8,O1)', 'D(H9,O7,H8,O1)', 'r(O1-O4)==>R(O--O)', 'r(O1-O7)==>R(O--O)', 'r(O4-O7)==>R(O--O)']



param_CCSDT = ['0.9743','0.9601','1.9089','1.9343', '0.9601', '0.9751','1.9096', '0.975','0.9604', '106.3925', '89.7073', '123.7461', '149.1012', '127.2891', '88.7886','106.3134', '151.6023', '88.6509', '121.0746', '106.1425', '151.5579' , '136.1102', '10.8313', '3.1749', '112.8079', '120.9425', '11.246', '1.2729', '129.9701', '1.149', '109.2388', '1.041', '123.0919', '2.81517', '2.80496', '2.80594'  ]






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
        if (row.find("  7  O    ") != -1)  :
            oo=comment[2].split()[0]
            ROW.append(oo)


#print ROW
for i,j in enumerate(ROW):
    if i == 5:
        #print "the 5 element is", j 
        value.append(j)
    if i == 18:
        #print "the value 18 is", j
        value.append(j)

#print value
a= 2.76608
value.append(a)

#print value

#print 'the value is :', value, "\n"
        
for i,j in enumerate(definition_CCSDT ):
    if i == 33:
        #print j
        definition.append(j)
    if i == 34:
        #print j
        definition.append(j)
    if i == 35:
        #print j
        definition.append(j)

#print 'the definition is:',definition, "\n"

error=[ abs(float(j) -abs(float(i))) for i,j in zip(value,param_CCSDT)]

#print mad, '\n'


print "\n"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "                       geometrical parameters cluster (H2O)3    ","\n"
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

#print roh_mad
ROH_mad=sum(roh_mad)/len(roh_mad)
#print R_mad


print "MAD R(O--H) = ", ROH_mad

roo_mad=[]
for i,j in enumerate(error):
    if i == 33:
       roo_mad.append(j)
    if i == 34:
       roo_mad.append(j)
    if i == 35:
       roo_mad.append(j)

#
##print roo_mad
ROO_mad=sum(roo_mad)/len(roo_mad)
#print R_mad

print "MAD R(O--O) = ", ROO_mad

r_mad=[]
for i,j in enumerate(error):
#   print i, j
   if i > -1  and i < 9 :
       r_mad.append(j)
   if i > 32  and i < 36 :
       r_mad.append(j)

#print r_mad
R_mad=sum(r_mad)/len(r_mad)
#print R_mad

print "MAD R(all bonds) = ", R_mad
#
a_mad=[]
for i,j in enumerate(error):
#   print i, j
   if (i > 8)  and (i < 21) :
#       print j
       a_mad.append(j)

#print a_mad
A_mad=sum(a_mad)/len(a_mad)
#print D_mad


print "MAD A(all angles) = ", A_mad


d_mad=[]
for i,j in enumerate(error):
#   print i, j
   if (i > 20)  and (i < 33) :
#       print j
       d_mad.append(j)
#
#print d_mad
D_mad=sum(d_mad)/len(d_mad)
##print D_mad


print "MAD D(all dihedral) = ", D_mad
print "\n"











