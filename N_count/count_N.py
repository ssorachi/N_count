#!/usr/bin/env python
# coding: utf-8
# In[11]:


import sys
args = sys.argv
read_file = args[1]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = open(read_file, 'r')
b = open('count.txt',mode='w')

count = ''
while True:
    line1 = a.readline()
    if line1:
        if ">" in line1:
            pass
        else:
            count = count + line1
    else:
        break

count_N_count = count.count('N')
count_A_count = count.count('A')
count_T_count = count.count('T')
count_G_count = count.count('G')
count_C_count = count.count('C')
all_count = count_N_count+count_A_count+count_T_count+count_G_count+count_C_count
N_percent = count_N_count/all_count*100
A_percent = count_A_count/all_count*100
T_percent = count_T_count/all_count*100
G_percent = count_G_count/all_count*100
C_percent = count_C_count/all_count*100
final_N_percent = round(N_percent,1)
final_A_percent = round(A_percent,1)
final_T_percent = round(T_percent,1)
final_G_percent = round(G_percent,1)
final_C_percent = round(C_percent,1)
b.write('>all chr'+'\n''The percent of N is '+str(final_N_percent)+'\n')
b.write('The percent of A is '+str(final_A_percent)+'\n')
b.write('The percent of T is '+str(final_T_percent)+'\n')
b.write('The percent of G is '+str(final_G_percent)+'\n')
b.write('The percent of C is '+str(final_C_percent)+'\n')

a.close()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = open(read_file, 'r')

c = open('chr_N_count.txt',mode='w')
count = 0
ATGCN_count = ''
while True:
    line1 = a.readline()
    if line1:
        if ">" in line1 and count == 0:
            c.write('The percent of N is '+str(final_N_percent)+'\n')
            c.write('The percent of A is '+str(final_A_percent)+'\n')
            c.write('The percent of T is '+str(final_T_percent)+'\n')
            c.write('The percent of G is '+str(final_G_percent)+'\n')
            c.write('The percent of C is '+str(final_C_percent)+'\n')
            ATGCN_count = ''
            c.write(line1)
            count += 1
        else:
            ATGCN_count = ATGCN_count + line1
            count_N_count = ATGCN_count.count('N')
            count_A_count = ATGCN_count.count('A')
            count_T_count = ATGCN_count.count('T')
            count_G_count = ATGCN_count.count('G')
            count_C_count = ATGCN_count.count('C')
            all_count = count_N_count+count_A_count+count_T_count+count_G_count+count_C_count
            N_percent = count_N_count/all_count*100
            A_percent = count_A_count/all_count*100
            T_percent = count_T_count/all_count*100
            G_percent = count_G_count/all_count*100
            C_percent = count_C_count/all_count*100
            final_N_percent = round(N_percent,1)
            final_A_percent = round(A_percent,1)
            final_T_percent = round(T_percent,1)
            final_G_percent = round(G_percent,1)
            final_C_percent = round(C_percent,1)
            count = 0
    else:
        break

count_N_count = ATGCN_count.count('N')
count_A_count = ATGCN_count.count('A')
count_T_count = ATGCN_count.count('T')
count_G_count = ATGCN_count.count('G')
count_C_count = ATGCN_count.count('C')
all_count = count_N_count+count_A_count+count_T_count+count_G_count+count_C_count
N_percent = count_N_count/all_count*100
A_percent = count_A_count/all_count*100
T_percent = count_T_count/all_count*100
G_percent = count_G_count/all_count*100
C_percent = count_C_count/all_count*100
final_N_percent = round(N_percent,1)
final_A_percent = round(A_percent,1)
final_T_percent = round(T_percent,1)
final_G_percent = round(G_percent,1)
final_C_percent = round(C_percent,1)
c.write('The percent of N is '+str(final_N_percent)+'\n')
c.write('The percent of A is '+str(final_A_percent)+'\n')
c.write('The percent of T is '+str(final_T_percent)+'\n')
c.write('The percent of G is '+str(final_G_percent)+'\n')
c.write('The percent of C is '+str(final_C_percent)+'\n')

a.close()
