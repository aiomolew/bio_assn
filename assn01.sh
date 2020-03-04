#! /bin/bash

#assn01-1

find . -name "*nad*"

#assn01-2
ps aux

#CPU percentage for the command is 0.0%

#Output below
#USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
#yomolewu 15389  0.0  0.0 155360  1832 pts/1    R+   00:23   0:00 ps aux

sudo top

#Total memory available is 1882300 + 2097148 KiB
#Total used is 1109440 + 520
#Available memory is 536600

#Output below
#%Cpu(s):  4.0 us,  1.0 sy,  0.0 ni, 94.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
#KiB Mem :  1882300 total,   169924 free,  1109440 used,   602936 buff/cache
#KiB Swap:  2097148 total,  2096628 free,      520 used.   536600 avail Mem 


#assn01-3
grep "misc_feature" watermelon.gff |sort -k7nr >IR_regions.gff


#assn01-4
grep "misc_feature" watermelon.gff | wc -l
grep -v "misc_feature" watermelon.gff | wc -l

# 37 line with IR feature
# 107 line with non-IR feature

# No, the IR region do not outnumber the non-IR fragment
# More fragment from outside the IR sequence


#assn01-5
grep  "BamHI" watermelon.gff | wc -l
# I am not sure which file to use for this. There is not line with BamHI
# in watermelon.gff

#assn01-6
head -n 1000 shaver_etal.csv | tail -n 500
sed -n '500,1000p' shaver_etal.csv
 
#assn01-7

sort -k3,3 -k2r,2  fruit.txt

