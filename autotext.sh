for dir in $(ls .)
do
   if [ -d $dir ]; then 
      echo $dir
         ` cat $dir/*.txt |sed ':a ; N;s/\n//; t a ;' \$1 |sed 's/[,，,。,？]//g' $1|sed 's/\(.\{2000\}\)\(..\)/\1\n\2/g' \$1 >$dir.txt`
   fi
done  
