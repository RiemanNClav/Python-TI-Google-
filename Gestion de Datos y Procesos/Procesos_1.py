#STANDARD STREAMS 
#¿Como se conecta un programa de python a la pantalla y al teclado?, Usa flujos de E/S, mecanimos basicos para realizar operaciones de entrada
#y salida en sus programas, la mayoria de los sistemas operativos suministran tres flujos de E/S diferentes de forma 
#predeterminada. 
#La mayoria de sistemas operativos suministran tres flujos de E/S diferentes de forma predeterminada, cada uno con 
#proposito diferente, STDIN, STDOUT y STDERR. 
#Aplicacion de los tres flujos:

data = input('This will come from STDIN: ') 
print('Now we write it to STDOUT: ' + data) 
#print('Now we generate an error to STDERR: ' + data+1)

#ENVIROMENT VARIABLES

#Shell es un interfaz de linea de comandos que se utiliza para interactuar con el sistema operativo, el shell mas utilizado
#en Linux se llama Bash, otros shells populares son Zsh y Fish. 

#Los programa de python se ejecutan dentro de un entorno de linea de comandos shell, nos pueden ayudar a alterar
#rapidamente el comprotamiento de un programa 
#podemos leer las variables de entorno desde python usando el diccionario Environ proporcionado por el modulo del siste,a
import os
print('HOME: ' + os.environ.get('HOME', ''))
print('SHELL: ' + os.environ.get('SHELL', ''))
print('FRUIT: ' + os.environ.get('PATH', ''))


#COMMAND LINE ARGUMENT AND EXIT STATUS
#parametros que se pasan a un programa cuando se inicia, 
#para acceder a ellos usamos sys.
import sys 
print(sys.argv)
#return code: es un valor, en los sistemas operativos UNIX, es cero cuando 
# el proceso tiene exito, !=0 cuando tiene un error, para comprobar el 
# estado de salida de un programa, podemos utilizar una variable
#especial que nos dice cual fue el estado de salida del ultimo comando ejecutado. 



