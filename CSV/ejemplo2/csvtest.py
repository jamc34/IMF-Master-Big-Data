import csv, os, sys

scdirectory='SinCabeceras';
def processFile(filename):
    scfile=open(scdirectory+'/'+filename, "w");
    ejemploEscritor=csv.writer(scfile);

    inputfile=open(filename)
    ejemploLector=csv.reader(inputfile)
    for linea in ejemploLector:
        print ("Linea #"+str(ejemploLector.line_num)+ " " + str(linea))
        ejemploEscritor.writerow(linea);
    print('finished ' +filename);

os.makedirs(scdirectory, exist_ok=True );
files = os.listdir(sys.argv[1])
for file in files:
    if file.endswith('.csv'):
        processFile(file)

