
#! /bin/bash

# assn03-1

for val in {808..8008..1}
  do
    echo "TR-${val}"
  done

# assn03-2
alias hm="cd ~"
alias ll="ls -al"

#assn03-3
ls -l .| egrep -c '*.fasta'  # ans:15085

#assn03-4
ls -l .| egrep -c '*.tre' # ans: 14640

#assn03-5
ls -l .| egrep -c '*.sched'

#assn03-6
ls | egrep '*.fasta'| awk -F'[_]' '{print $1}'|sort > fasta.txt
ls | egrep '*.tre'| awk -F'[_]' '{print $1}'|sort > tre.txt
comm -23 fasta.txt tre.txt |wc -l  #ans: 445

#assn03-7
awk '/Program Return Code:/ {print FILENAME, " " $4}' *.sched| uniq|awk ' {if ($2 == '0') {count++; }} END {print count}'
awk '/Program Return Code:/ {print FILENAME, " " $4}' *.sched| uniq|awk ' {if ($2 != '0') {count++; }} END {print count}'

#assn03-8
comm -23 fasta.txt tre.txt > notree.txt

for word in $(cat notree.txt)
 do 
  command="write_raxml_job_script.py ${word}_alignment.fasta > ${word}_alignment.pbs"
 echo $command
 done
