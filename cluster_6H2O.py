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
definition_CCSDT =['R(O1,H2)',  'R(O1,H3)',  'R(O1,H5)==>R(O--H)',  'R(O1,H9)==>R(O--H)',  'R(H2,O16)==>R(O--H)',  'R(O4,H5)',  'R(O4,H6)',  'R(O4,H11)', 'R(O7,H8) ', 'R(O7,H9) ', 'R(O7,H14)==>R(O--H)', 'R(O10,H11)', 'R(O10,H12)', 'R(O10,H15)==>R(O--H)', 'R(O10,H18)==>R(O--H)', 'R(O13,H14)', 'R(O13,H15)', 'R(O13,H17)==>R(O--H)', 'R(O16,H17)',      'R(O16,H18)',      'A(H2,O1,H3)',     'A(H2,O1,H5)',     'A(H2,O1,H9)',     'A(H3,O1,H5)',     'A(H3,O1,H9)',     'A(H5,O1,H9)',     'A(H5,O4,H6)',     'A(H5,O4,H11)',     'A(H6,O4,H11)',     'A(H1,H5,O4) ',     'A(H8,O7,H9) ',     'A(H8,O7,H14)',     'A(H9,O7,H14)',     'A(H1,H9,O7) ',     'A(H11,O10,H12)',     'A(H11,O10,H15)',     'A(H11,O10,H18)',     'A(H12,O10,H15)',     'A(H12,O10,H18)',     'A(H15,O10,H18)',     'A(H14,O13,H15)',   'A(H14,O13,H17)',   'A(H15,O13,H17)',   'A(O7,H14,O13) ',   'A(O10,H15,O13)',   'A(H2,O16,H17) ',   'A(H2,O16,H18) ',   'A(H17,O16,H18)',   'A(H13,H17,O16)',   'A(O10,H18,O16)',   'L(1,2,16,11,-1) ','L(4,11,10,2,-1) ','L(1,2,16,11,-2) ','L(4,11,10,2,-2) ','D(H3,O1,O16,H17)',    'D(H3,O1,O16,H18)',    'D(H5,O1,O16,H17)',    'D(H5,O1,O16,H18)',    'D(H9,O1,O16,H17)',    'D(H9,O1,O16,H18)',    'D(H2,O1,H5,O4)', 'D(H3,O1,H5,O4)',  'D(H9,O1,H5,O4)',  'D(H2,O1,H9,O7)',  'D(H3,O1,H9,O7)',  'D(H5,O1,H9,O7)',  'D(H6,O4,H5,O1)',  'D(H11,O4,H5,O1) ',  'D(H5,O4,O10,H12)',  'D(H5,O4,O10,H15)',  'D(H5,O4,O10,H18)',  'D(H6,O4,O10,H12)',  'D(H6,O4,O10,H15)',  'D(H6,O4,O10,H18)',  'D(H8,O7,H9,O1)  ',  'D(H14,O7,H9,O1) ',  'D(H8,O7,H14,O13)',  'D(H9,O7,H14,O13)',  'D(H11,O10,H15,O13)',  'D(H12,O10,H15,O13)',  'D(H18,O10,H15,O13)', 'D(H11,O10,H18,O16)', 'D(H12,O10,H18,O16)', 'D(H15,O10,H18,O16)', 'D(H15,O13,H14,O7) ', 'D(H17,O13,H14,O7) ', 'D(H14,O13,H15,O10)', 'D(H17,O13,H15,O10)', 'D(H14,O13,H17,O16)', 'D(H15,O13,H17,O16)',  'D(H2,O16,H17,O13) ', 'D(H18,O16,H17,O13)', 'D(H2,O16,H18,O10) ', 'D(H17,O16,H18,O10)', 'R(O1,O4)==>R(O--O)','R(O1,O7)==>R(O--O)', 'R(O4,O7)==>R(O--O)','R(O16,O1)==>R(O--O)','R(O7,O13)==>R(O--O)', 'R(O13,O10)==>R(O--O)', 'R(O16,O10)==>R(O--O)', 'R(O16,O13)==>R(O--O)'] 



param_CCSDT = ['0.9957', ' 0.9601', ' 2.0241', ' 1.8677', ' 1.6862', ' 0.9705', ' 0.967', ' 1.7903', ' 0.9604', ' 0.9769', ' 2.0022', ' 0.983', ' 0.9602', ' 2.0927', ' 2.1493', ' 0.9701', ' 0.9688', ' 1.8925', ' 0.9793', ' 0.9683', ' 107.2873', ' 100.2145', ' 103.5925', ' 132.285', ' 128.8807', '  78.711',  '102.7202', '103.2667', '105.6656', '148.2365', '107.0364', '122.3476', '101.322', '155.0121', ' 106.762', ' 100.7353', ' 100.1345', '130.5267', '134.4652', '77.2085', '104.6289', '102.4346', ' 89.5591', ' 160.9634', ' 147.5607', '101.7124', '105.5736', '101.818 ', '154.2138', '137.9762', '170.6486', '168.3087', '173.5927', '185.7844', '131.9453', '123.5708', '86.6575', '17.8264', '7.3822', '97.1017', '68.323 ',  ' 166.7857', '33.6553', '63.1579', '170.8482', '34.7614','41.5236', '68.2088', '135.3735', '85.5303', '8.1113', '118.8254', '20.2708', '97.6898', '170.1444', '60.6527', '149.4787', '30.7617', '70.8358', '165.9169', '27.2472', '68.9706', '165.1594', '29.8567', '66.7076', '26.1245', '78.3833', '24.3573', '72.8071', '32.0811', '70.7019', '38.173',  '71.1057', ' 34.774', '2.894639', '2.783838', '2.964834', '2.669891', '2.936282','2.956338', '2.940964', '2.806790'] 

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
            oo=comment[-2].split()[0]
            ROW.append(oo)
        if (row.find("  13  O    ") != -1)  :
            oo=comment[3].split()[0]
            ROW.append(oo)
            oo=comment[-1].split()[0]
            ROW.append(oo)
        if (row.find("  16  O    ") != -1)  :
            oo=comment[2].split()[0]
            ROW.append(oo)
            oo=comment[-1].split()[0]
            ROW.append(oo)
            oo=comment[-3].split()[0]
            ROW.append(oo)


for i ,j in enumerate(ROW):
    print "ROW",i,j


for i,j in enumerate(ROW):
    if i == 247:
#        print "the 247 element is", j #ok
        value.append(j)
    if i == 248:
#        print "the 248 element is", j #oK
        value.append(j)
    if i == 249:
#        print "the 249 element is", j #ok
        value.append(j)
    if i == 252:
#        print "the 252 element is", j #ok 
        value.append(j)
    if i == 257:
#        print "the 257 element is", j #ok
        value.append(j)
    if i == 258:
#        print "the 258 element is", j #ok
        value.append(j)
    if i == 260:
#        print "the 259 element is", j #ok
        value.append(j)
    if i == 266:
#        print "the 283 element is", j #ok
        value.append(j)


#for i in value: 
#    print i

#print "-------------------"

#for i ,j in enumerate(definition_CCSDT):
#    print i,j
         
for i,j in enumerate(definition_CCSDT ):
    if i == 94:
#        #print j
        definition.append(j)
    if i == 95:
##        #print j
        definition.append(j)
    if i == 96:
##        #print j
        definition.append(j)
    if i == 97:
#        #print j
        definition.append(j)
    if i == 98:
#        #print j
        definition.append(j)
    if i == 99:
#        print j
        definition.append(j)
    if i == 100:
##        #print j
        definition.append(j)
    if i == 101:
#        #print j
        definition.append(j)

#print 'the definition is:',definition, "\n"

#for i,j in enumerate(value):
#    print i,j

error=[ abs(float(j) -abs(float(i))) for i,j in zip(value,param_CCSDT)]

#print mad, '\n'



print "\n"
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
print "     geometrical parameters cluster (H2O)6, cluster number 1 of WATER27   ","\n"
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
    if i == 4:
       roh_mad.append(j)
    if i == 10:
       roh_mad.append(j)
    if i == 13:
       roh_mad.append(j)

    if i == 14:
       roh_mad.append(j)

    if i == 17:
       roh_mad.append(j)

#print roh_mad
ROH_mad=sum(roh_mad)/len(roh_mad)
#print R_mad

print "MAD R(O--H) = ", ROH_mad

roo_mad=[]
for i,j in enumerate(error):

   if i > 93  and i < 102 :
       roo_mad.append(j)

    #       roo_mad.append(j)
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
   if i > -1  and i < 20 :
       r_mad.append(j)
   if i > 93  and i < 102 :
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
   if (i > 19)  and (i < 50) :
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
   if (i > 53)  and (i < 94) :
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


