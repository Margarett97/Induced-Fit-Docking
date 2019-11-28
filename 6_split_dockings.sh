#!/usr/bin/bash


echo please input filename dlg
read FILENAME
echo insert receptor
read RFILENAME

grep '^DOCKED' $FILENAME | cut -c9- > my_docking.pdbqt 


cut -c-66 my_docking.pdbqt > my_docking.pdb 

cat $RFILENAME my_docking.pdb | grep -v '^END   ' | grep -v '^END$' > complex.pdb 



a=`grep ENDMDL my_docking.pdb | wc -l`
b=`expr $a - 2`
echo $b
csplit -k -s -n 3 -f my_docking. my_docking.pdb '/^ENDMDL/+1' '{'$b'}'
for f in my_docking.[0-9][0-9][0-9]
do
  mv $f $f.pdb
done
