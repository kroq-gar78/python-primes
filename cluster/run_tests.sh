#!/bin/bash

# Run all of the tests with a certain amount of bases, ranges, and trials

#ranges=( 1000 10000 1000000 10000000 100000000 1000000000 )
ranges=( 1000 10000 1000000 10000000 )

#mkdir "trialdiv"
for (( i=1; i<$((${#ranges[*]})); i++ )) # iterate through array 'ranges' at the top of the file
do
	#time python trialdiv_pp.py ${ranges[$i-1]} ${ranges[$i]}
	#mv *.accuracy trialdiv/
	for j in 1 2 3 4 5 6 7 8 # num. of bases
	do
		#echo "Base(s): $i"
		dir_bases="bases_$j"
		for k in 1 2 3 4 5 # multiple trials
		do
			dir_trial="trial$k"
			mkdir -p "$dir_bases/$dir_trial/"
			echo "${ranges[$i-1]} ${ranges[$i]}"
			time python fermat_pp.py ${ranges[$i-1]} ${ranges[$i]} $j
			time python solovaystrassen_pp.py ${ranges[$i-1]} ${ranges[$i]} $j
			time python millerrabin_pp.py ${ranges[$i-1]} ${ranges[$i]} $j
			mv *.accuracy "$dir_bases/$dir_trial/" # move data to their respective directories
		done
	done
done
