import os
import subprocess
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

#pathing donde encontraremos todas las carpetas, cambiando el nombre particular por CHANGE 
str_directorios_dsds = "C:/StruvalChecker/struval_checker-main/struval_checker-main/DSD/CHANGE/*.xml"
str_directorios_cubos = "C:/StruvalChecker/struval_checker-main/struval_checker-main/datos/CHANGE/*.xml"


#pathing donde tenemos todas las carpetas a recorrer
for _,dirs,_ in os.walk("C:/StruvalChecker/struval_checker-main/struval_checker-main/DSD"):
    for certificacion in dirs:
        print(certificacion)
        str_directorios_dsds_aux = str_directorios_dsds.replace("CHANGE",certificacion)
        str_directorios_cubos_aux = str_directorios_cubos.replace("CHANGE",certificacion)
        dsds_directorios = glob.glob(str_directorios_dsds_aux)
        cubos_directorios = glob.glob(str_directorios_cubos_aux)
        dsds_directorios = [directorio_dsd.replace('\\', '/') for directorio_dsd in dsds_directorios]
        cubos_directorios = [directorio_cubo.replace('\\', '/') for directorio_cubo in cubos_directorios]
        dsd = dsds_directorios[0]
        cubo = cubos_directorios

        for cubo in  cubos_directorios:
            #print(cubo)
            #print(dsd)
            result = []
            win_cmd = f'cd C:/StruvalChecker/struval_v3_externalaccesstutorial/ExternalAccessTutorial/ & runClient.cmd {cubo} {dsd} SDMX_ML '
            

            process = subprocess.Popen(win_cmd,
                                       shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                                       
            process.wait()
            directorio = os.path.join("validation",cubo.split('/')[-2])
            if not os.path.exists(directorio):
                os.makedirs(directorio)
            fichero_dir = os.path.join(directorio,cubo.split('/')[-1].split('+')[0])
           
            with open(fichero_dir+'.txt', 'w') as file:
                for line in process.stdout:
                    # print(line)
                    file.write(line.decode("latin-1"))


