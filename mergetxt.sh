rm -rf all.dat
for fn in `ls *.txt`; do
    echo $fn
    f1=${fn%%.*}
    echo $f1
    cmd="sed 's/^/__label__$f1 /g' $fn >>all.dat"
    echo $cmd|sh
done
