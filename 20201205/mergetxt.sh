rm -rf all.txt
for fn in `ls *.txt`; do
    echo $fn
    f1=${fn%%.*}
    echo $f1
    sed 's/^/__label__$f1 /g' $fn >>all.txt
done
