files=(
	"IMG_0545.JPG"  
	"IMG_0546.JPG"  
	"IMG_0547.JPG"  
	"IMG_0548.JPG"  
	"IMG_0552.JPG"  
	"IMG_0553.JPG"
      )

for i in ${files[@]}; do
	keepass2john -k $i ./MyPasswords.kdbx > ./hash/$i-hash.txt
done
