

The Locked Chest

mkdir secret_chamber/
cd secret_chamber
echo "treasure" > chest
chmod 000 chest
cd ..
mv secret_chamber .secret_chamber
less .secret_chamber/chest


Spices

mkdir fruit/
touch apple banana melon lemon orange strawberry pineapple
ls > text.txt
ls | grep a > text_a.txt
diff text.txt text_a.txt


Scripting

#!/bin/bash
echo "hello world"


#!/bin/bash
echo $1

source hello.sh "hello world"

#!/bin/bash
for i in $@
do
        source hello.sh $i
done
