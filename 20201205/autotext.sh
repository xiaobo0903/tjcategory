for dir in $(ls .)
do
   if [ -d $dir ]; then 
      echo $dir
         ` cat $dir/*.txt |sed ':a ; N;s/\n//; t a ;' \$1 |sed 's/[
   fi
done  