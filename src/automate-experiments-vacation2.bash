#!/bin/bash

# last modified: 10/11/2021

# path to experiments folder:
# ~/Desktop/student-workSpace

# path to working git repository:
#  /home/messy/Workspace-boghos-youseef/

echo "Starting Automation Script..."


# this is the benchmark version with transacional actors
#lein run -- -vtxact -w 4 -s 8 -t 30 -n 300

# this is the original version of the benchmark
#
#lein run -- -v original -w 4 -s 8 -t 30 -n 300

# Paramteres defintion:
# -v either orginal or txact.
# -w the number of primary worker actors.
# -s the number of secondary worker actors. (this is only available for txact version)
# -t the numver of reservations.
# -n number of queries per relation per reservation.
# -r number of flights/rooms/cars.
# -p work factor for password generation.
# -d prnt debug information

Version=txact
#primary_worker_actors=1
#secondary_worker_actors=20
#num_reservations=50
#num_queries=10
addition_factor=4

primary_worker_actors=1
secondary_worker_actors=20
num_reservations=1000
num_queries=10
p=5
echo "currently running Bash ${BASH_VERSION}"
echo "Do you want to run the original version?(y/n)"
read answer

if [[ "$answer" == 'y' ]];
	then Version=original 
else version=txact

fi

#echo "How many points do you need?"
#read num_of_points

echo "write the name of the output file"
read output_name

if [[ "$output_name" == 0 ]];
	then
		echo "no output file will be produced for this run"
fi

#threads="1 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64"
threads="1 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64"

#threads="1 4"

echo "Running the script with the following options:  -v ${Version} -w ${primary_worker_actors} -s ${secondary_worker_actors} -t ${num_reservations} -n ${num_queries} -p ${p}"


for i in $threads
do

        cd  ~/Desktop/vacation2-automation/vacation2
        echo "now in loop number ${i}"
        output=$(lein run -- -v ${Version} -w ${i} -s ${secondary_worker_actors} -t ${num_reservations} -n ${num_queries} -p ${p})


	if [[ "$output_name" != '0' ]] ;

		then 
			
        		cd ~/Desktop/vacation2-automation/src/experiment-outputs
        		echo "Now writing the results to ${output_name}."
			echo ${output} >> ./"${output_name}".txt
	
	fi
	

	
	#echo ${output} | sed '[0-9]'

	if [[ $primary_worker_actors -eq $1 ]];
		then primary_worker_actors=4
	
	else

		primary_worker_actors=`expr $primary_worker_actors + $addition_factor`

	fi

done



gtimefile(){
  #echo "Please write the experiment output file name"
  #read output_name
  

  local outputfile_name=${output_name}
  echo "New time-stamps file: ${outputfile_name}"

  #echo "Please provide a name for the new file"
  #read new_file
  local new_file="${outputfile_name}-time-stamps"


  echo "Writing output file now..."
  cd ..
  touch time-stamps/"${new_file}.txt"


  mawk '/time/ {print $(NF - 1) ","}' ./experiment-outputs/${outputfile_name}.txt >> "time-stamps/${new_file}.txt"
  echo "Output file created!"
  echo "Program finished"
}

gtimefile

# echo ${output2} | sed -n "s/\([0-9]\{4\}\.[0-9]\{3\}\)/"

echo "shell program done!"
echo "-----------------------"
