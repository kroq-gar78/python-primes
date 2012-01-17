#!/bin/bash

# Run all of the tests with a certain amount of bases, ranges, and trials

#ranges=( 1000 10000 1000000 10000000 100000000 1000000000 )
ranges=( 1000 10000 1000000 10000000 )
	
for i in 1 2 3 # num. of bases
do
	#echo "Base(s): $i"
	dir_bases="bases_$i"
	for (( j=1; j<$((${#ranges[*]})); j++ )) # iterate through array 'ranges' at the top of the file
	do
		time python trialdiv_pp.py ${ranges[$j-1]} ${ranges[$j]}
		for k in 1 2 3 4 5 # multiple trials
		do
			dir_trial="trial$k"
			mkdir -p "$dir_bases/$dir_trial/"
			echo "${ranges[$j-1]} ${ranges[$j]}"
			time python fermat_pp.py ${ranges[$j-1]} ${ranges[$j]} $i
			time python solovaystrassen_pp.py ${ranges[$j-1]} ${ranges[$j]} $i
			time python millerrabin_pp.py ${ranges[$j-1]} ${ranges[$j]} $i
			mv *.accuracy "$dir_bases/$dir_trial/" # move data to their respective directories
		done
	done
done
