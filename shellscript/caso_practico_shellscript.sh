#!/bin/bash

show_menu() {
echo Ver directorio actual...........[1]
echo Copiar archivos.................[2]
echo Editar archivos.................[3]
echo Imprimir archivo................[4]
echo Salir del menú..................[5]

}

copiar_archivos(){
    echo "Introduce archivo a copiar: "; read f;
    verificar_archivo $f;
    if [ $? -eq 1 ]; then
        echo "Introduce directorio destino: "; read d;
	verificar_directorio $d;
	if [ $? -eq 1 ]; then
           cp $f $d;
	fi
    fi
}

editar_archivo(){
    echo "Introduce archivo a editar: "; read f;
    verificar_archivo $f;
    if [ $? -eq 1 ]; then
       vi $f
    fi
}

imprimir_archivo(){
    echo "Introduce archivo a imprimir: "; read f;
    verificar_archivo $f;
    if [ $? -eq 1 ]; then
       lpr $f
    fi
}

verificar_archivo(){
    if [ ! -e $1 ]
    then 
       echo "El fichero $1 no existe";
       return 0;
    fi 
    return 1;
}


verificar_directorio(){
    if [ ! -d $1 ]
    then 
       echo "El directorio $1 no existe";
       return 0;
    fi 
    return 1;
}

while true
do
   show_menu
   read option 
   case $option in
      1) echo "El directorio actual es: " `pwd`
      ;;
      2) copiar_archivos
      ;;
      3) editar_archivo
      ;;
      4) imprimir_archivo
      ;;
      5) echo Hasta pronto; break;
      ;;
      *) echo "No te entiendo"
      ;;
      esac

done #while
