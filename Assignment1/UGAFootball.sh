mkdir dawgs
cd dawgs
touch ZionBranch.txt CjAllen.txt JoshMcCray.txt NateFrazier.txt KjBolden.txt OscarDelp.txt 
NoahThomas.txt RaylenWilson.txt CjWiley.txt DanielHarris.txt ChrisCole.txt KirbySmart.txt 
MikeBobo.txt JoshCrawford.txt
mkdir players coaches
mv ZionBranch.txt CjAllen.txt JoshMcCray.txt NateFrazier.txt KjBolden.txt OscarDelp.txt
NoahThomas.txt RaylenWilson.txt CjWiley.txt DanielHarris.txt ChrisCole.txt players
mv KirbySmart.txt MikeBobo.txt JoshCrawford.txt coaches
mv coaches coachesAndStaff
ls -l
cd players
pwd
ls
cd ../coachesAndStaff
ls
cd ..
mkdir rivals
cd rivals
touch alabama.txt florida.txt tech.txt
cd ..
mkdir medals
cd medals
touch 2022.txt 2021.txt 1980.txt 1942.txt
cd ..
mkdir allFiles
cp players/* coachesAndStaff/* rivals/* medals/* allFiles/
rm -r rivals
cd ..

