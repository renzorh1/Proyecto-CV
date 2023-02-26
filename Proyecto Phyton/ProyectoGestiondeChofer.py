"""
THE LAST PROYECT
INTEGRANTES
-
-
-
-
"""
"""
Imaginemos que somos los encargados de soporte del área de TI en la empresa 
de transportes “VIAJE SEGURO SAC”, Entre nuestras responsabilidades se 
encuentra la administración y organización de los choferes y vehículo, 
así como la asignación de rutas y destinos para cada uno. Por el momento, 
la empresa solo cuenta con una única ruta que es de LIMA->TRUJILLO, 
TRUJILLO->LIMA. Se desea gestionar que choferes se encuentran disponibles 
según su horario y en qué ciudad están ubicados para poder asignarlos. 
Igualmente, se desea gestionar la información de los ómnibus con los que 
cuenta la empresa, su última fecha de mantenimiento y si están aptos para 
salir, capacidad de combustible y nivel actual, tipo de combustible, estado 
de las llantas, capacidad de pasajeros.  Por motivos de la pandemia, la 
capacidad se ha reducido a solo 1 pasajero cada par de asientos; entonces, 
se debe tener el registro del número de asientos pares para asignar solo 1 
asiento disponible. Para esta labor, se pretende desarrollar un software 
que cumpla con los siguientes requerimientos:
"""

#1.	Registrar todos los choferes:


"""
1.1	Código, nombre y apellidos, dirección, ubicación actual (LIMA O TRUJILLO),
horario de trabajo (L-M-X-J-V-S-D), salario, número de brevete, estado 
(ACTIVO, VACACIONES, INACTIVO), años en la empresa.
"""
def datos(n):
    lista=[]
    
    for i in range(n):
        c=input("Ingrese el codigo:")
        o=input("Ingrese el nombre:")
        a=input("Ingrese el apellido:")
        d=input("Ingrese su direccion:")
        print("Seleccion su ubicación actual")
        print("[1] LIMA\n[2] TRUJILLO\n")
        n1=int(input("Ingrese la opción: "))
        if n1==1:
            u="LIMA"
        elif n1==2:
            u="TRUJILLO"
        s=""
        bre=input("Ingrese el numero de brevete:")
        print("Seleccione su estado")
        print("[1] ACTIVO\n[2] VACACIONES\n[3] RETIRADO")
        n=int(input("Seleccione una opción: "))
        if n==1:
            est="ACTIVO"
        elif n==2:
            est="VACACIONES"
        elif n==3:
            est="RETIRADO"
            
        year=int(input("Ingrese los años de la empresa:"))
        t=int(input("¿Cuantos días a la semana trabaja?: "))
        dias=[]
        print("Ingrese las iniciales de los dias que trabaja")
        print("[L] LUNES\n[M] MARTES\n[X] MIERCOLES\n[J] JUEVES\n[V] VIERNES\n[S] SABADO\n[D] DOMINGO")
        for i in range(t):
            z=str(input(f"Ingrese el dia {i+1} de trabajo: "))
            dias.append(z)
        diccionario={"Codigo":c,"Nombre":o,"Apellido":a,"Direccion":d,"Ubicacion actual":u,"Horario de trabajo":dias,"Salario":s,"Brevete":bre,"Estado":est,"Años en la empresa":year}
        lista.append(diccionario)
    return lista



"""

1.2	El salario de un chofer se calcula: (1 + (años en la empresa/10)) * 2000. 
Si los años superan a 10, el salario es 4500.
"""
def recarcular(lista):
    salarios=[]
    resultados=[]
    lista_oficial=[]
    for i in range(len(lista)):
        
        tra=lista[i]
        a=tra["Años en la empresa"]
        salarios.append(a)
    
        
    for j in range(len(salarios)):
        if salarios[j]<10:
           re=((1+(salarios[j]/10))*2000)
           
               
        else:
            re=4500
            
        
        resultados.append(re)
    
    for k in range(len(lista)):
        lista[k]["Salario"]=resultados[k]
        lista_oficial.append(lista[k])
        
    return lista_oficial
    

"""
1.3	Indicar los choferes que se encuentran en cada ciudad y quienes 
tienen horario disponible.
"""
#cambiar esto
def mostrarChoferes(lista):
  horarios = ["L", "M", "X", "J", "V", "S", "D"]
  print("\nChoferes en Lima:")
  for dic in lista:
    if(dic["Ubicacion actual"] == "Lima"):
      print(dic["Nombre"],dic["Apellido"])
  print("\nChoferes en Trujillo:")
  for dic in lista:
    if(dic["Ubicacion actual"] == "Trujillo"):
      print(dic["Nombre"],dic["Apellido"])
  dia = ""
  while dia not in horarios:
    dia = input("Ingrese el dia actual :")
  print("\nChoferes disponibles el dia de hoy",dia,":")     
  for dic in lista:
    z=len(dic["Horario de trabajo"])
    for i in range(z):
        if(dic["Horario de trabajo"][i] == dia):
            print(dic["Nombre"],dic["Apellido"])    


"""
1.4	Reportar choferes con un salario superior a un valor X de búsqueda. 
"""
def salario_superior(lista): 
    l_salario=[]
    x=int(input("Ingrese un valor para hallar los choferes con un salario superior al ingresado: "))
    for i in range(len(lista)):
        if x<lista[i]["Años en la empresa"]:
            l_salario.append(lista[i])
    return l_salario

"""
1.5	Reportar choferes con tiempo de servicio superior a un valor X de búsqueda.
"""
def tiempo_superior(lista): 
    y=int(input("Ingrese un valor para hallar los choferes con un tiempo de servicio superior al ingresado: "))
    l_tiempo=[]
    for i in range(len(lista)):
        if y<lista[i]["Salario"]:
            l_tiempo.append(lista[i])
    return l_tiempo

"""
1.6	Actualizar el horario, estado, años en la empresa (recalcular el salario), 
ubicación, etc.
"""
def actualizar(lista):
    ard=int(input("De cuantos choferes desea actualizar sus datos: "))
    if ard != 0:
        for i in range(ard):
            for diccionario in lista:
                name=input("Ingrese el nombre: ")
                if diccionario["Nombre"]==name:
                    apellido=input("Ingrese el apellido: ")
                    if diccionario["Apellido"]==apellido:
                        Actual_horario=input("Ingrese el horario de trabajo: ")
                        Estado=input("Ingrese su estado:")
                        Ubicacion=input("Ingrese la ubicacion: ")
                        Años=input("Ingrese los años en la empresa:")
                        diccionario["Horario de trabajo"]=Actual_horario
                        diccionario["Estado"]=Estado
                        diccionario["Ubicacion actual"]=Ubicacion
                        diccionario["Años en la empresa"]=Años
    return lista

"""
1.7	Registrar nuevos choferes
"""
def nuevos(lista):
    nuevos=int(input("Cuantos nuevos choferes contratamos: "))
    if nuevos!=0:
        b=datos(nuevos)
        lista.append(b)
        return lista



#2.	Registrar todos los ómnibus:
"""
2.1	Código, Modelo, capacidad total, capacidad reducida (por COVID), 
asientos disponibles (según van vendiéndose los pasajes), meses transcurridos 
desde su mantenimiento, determinar si está apto o no para salir 
(si supera los 6 meses), chofer asignado, ubicación, hora de salida 
(existen tres horarios: 9, 12 y 20 horas)
"""
def registro_ómnibus():
    n=int(input("Ingrese el número de ómnibus: "))
    ómnibus=[]
    for i in range(n):
        Código=int(input("Ingrese el código: "))
        Modelo=input("Ingrese el modelo: ")
        Capacidad_total=int(input("Ingrese la capacidad total: "))
        Capacidad_reducida=int(input("Ingrese la capacidad reducida: "))
        Asientos_disponibles=disponibles(Capacidad_reducida)
        Mantenimiento_transcurido=int(input("Ingrese los meses transcurridos desde su mantenimiento: "))
        Estado_ómnibus=Estado(Mantenimiento_transcurido)
        Chofer=input("Ingrese el chofer asignado al ómnibus: ")
        Ubicacion=input("Ingrese su ubicacion actual: ")
        salida=int(input("Ingrese la hora de salida del ómnibus: "))
        dato_ómnibus={"Código":Código,"Modelo":Modelo,"Capacidad_total":Capacidad_total,"Capacidad_reducida":Capacidad_reducida,"Asientos_disponibles":Asientos_disponibles,"Mantenimiento_transcurido":Mantenimiento_transcurido,"Estado_ómnibus":Estado_ómnibus,"Chofer":Chofer,"Ubicacion":Ubicacion,"salida_ómnibus":salida}
        ómnibus.append(dato_ómnibus)
    return ómnibus
def disponibles(Capacidad_reducida):
    a=Capacidad_reducida
    b=int(input("Cuantos asientos se vendieron: "))
    if b != 0 :
        disponibles=a-b
    else:
        disponibles=a
    return disponibles
def Estado(Mantenimiento_transcurido):
    c=Mantenimiento_transcurido
    if c>6:
        b="No está apto"
    else:
        b="Sí está apto"
    return b
"""
2.2	Actualizar los meses de mantenimiento, la capacidad del ómnibus, 
chofer asignado, ubicación, etc.
"""
def actualizar_ómnibus(lista):
    ar=int(input("De cuantos ómnibus desea actualizar sus datos: "))
    if ar != 0:
        for i in range(ar):
            for diccionario in lista:
                Cód=int(input("Ingrese el Código: "))
                if diccionario["Código"]==Cód:
                    Mod=input("Ingrese el modelo: ")
                    if diccionario["Modelo"]==Mod:
                        mes=int(input("Ingrese los meses transcurridos desde su mantenimiento: "))
                        est=Estado(mes)
                        Cap_total=int(input("Ingrese la capacidad total: "))
                        Chof=input("Ingrese el chofer asignado al ómnibus: ")
                        ubica=input("Ingrese la ubicacion: ")
                        diccionario["Mantenimiento_transcurido"]=mes
                        diccionario["Estado_ómnibus"]=est
                        diccionario["Ubicacion"]=ubica
                        diccionario["Chofer"]=Chof
                        diccionario["Capacidad_total"]=Cap_total
    return lista

"""
2.3	Registrar nuevos ómnibus.
"""
def new_omni(lista):
    nuevos=int(input("Cuantos nuevos ómnibus alquilamos: "))
    if nuevos!=0:
        b=datos(nuevos)
        lista.append(b)
        return lista




#3-CONSULTAS
"""
3.1	Reportar el código y la cantidad de ómnibus que se encuentran en cada ciudad.
"""
def monstrar_Omnibus(lista):
    l=0
    t=0
    print("Omnibus en Lima:")
    for dic in lista:
        if(dic["Ubicacion"]=="LIMA"):
            print(dic["Código"])
            l=l+1
    print("\nOmnibus en Trujillo:")
    for dic in lista:
        if (dic["Ubicación"]=="TRUJILLO"):
            print(dic["Código"])
            t=t+1
    print(f"Hay {l} omnibus disponibles en Lima.")
    print(f"Hay {t} omnibus disponibles en Trujillo.")



"""
3.2	Reportar el número de choferes aptos dado un día específico de consulta.
"""
def choferesaptos(listas):
    horarios = ["L", "M", "X", "J", "V", "S", "D"]

    dia= ""
    while dia not in horarios:
        dia = input("Ingrese el dia actual: ")
        print("\nChoferes disponibles el dia de hoy",dia,":")
        aptos=0
        for dic in listas:
            if(dic["Horario de trabajo"] == dia):
                if (dic["Estado"]) == "ACTIVO":
                    aptos = aptos + 1
        print("Los choferes aptos son", aptos)
    
    
"""
3.3	Reportar en un determinado día cuantos ómnibus poseen asientos libres
 cuando se requiere comprar un pasaje para una hora de salida indicada.
"""
def boleto_final(listas):
    horarios = ["L", "M", "X", "J", "V", "S", "D"]

    dia= ""
    while dia not in horarios:
        dia = input("Ingrese el dia actual: ")
        libre=0
        horario=int(input("Ingrese el horario de salida: "))
        for dic in listas:
            if dic["Asientos_disponibles"] != 0 and dic["salida_ómnibus"]== horario:
                libre+=1
        print("Los Ómnibus con asientos libres son", libre)
                  

def crear_archivoChofer(lista,nombre): #leer archivo: "r" para arreglar las salidas al .txt (eliminar la ultima ",")(con .split) y poner todo en mayuscula y quitar la coma despues del nombre
    archivo=open(nombre,"w")
    for i in range(len(lista)):
        c=0
        while c<10:
            for clave, valor in lista[i].items():
                valor= str(valor)
                archivo.write(valor+" ")
                c=c+1
            archivo.write("\n")
    archivo.close()
    print("Creando archivo choferes...")
"""
CABECERA
"""

def main():
    print("BIENVENIDOS A VIAJE SEGURO SAC")
    nombre="Chofer.txt"
    print("Elije una de las opciones")
    print("[1] Registro de Choferes\n[2] Registro de Ómnibus\n[3] Reportes\n[4] Cerrar Menú")
    num=int(input("Ingrese la opción: "))
    while num!=4:
        if num==1:
            n=int(input("Ingrese el numero total de choferes:"))
            z=datos(n)
            a=recarcular(z)
            print(f" Lista Oficial de choferes es: {a}")
            print("[1] Reportar Ciudad y horario\n[2] Salario Superior a un valor\n[3] Tiempo superior a un valor \n[4] Actualizar datos \n[5] Nuevos choferes \n[6] Menu Principal")    
            num2=int(input("Ingrese la opción: "))
            while num2!= 6:
                if num2==1:
                    mostrarChoferes(a)
                elif num2==2:
                    k=salario_superior(a)
                    print("Los choferes con un salario superior son: ", k)
                elif num2==3:
                    p=tiempo_superior(a)
                    print("Los choferes con tiempos de servicio superior son: ", p)
                elif num2==4:
                    a=actualizar(a)
                    print("La lista actualizada sería: ", a)
                elif num2==5:
                    a=nuevos(a)
                    print("Lista oficial de los choferes son: ", a)
                    
                print("[1] Reportar Ciudad y horario\n[2] Salario Superior a un valor\n[3] Tiempo superior a un valor \n[4] Actualizar datos \n[5] Nuevos choferes \n[6] Menu Principal")
                num2=int(input("Ingrese la opción: ")) 
        elif num==2:
            n=registro_ómnibus()
            print("Los Ómnibus en total son: ", n)
            print("[1] Actualizar Datos\n[2] Registrar nuevos Ómnibus\n[3] Menú Principal") 
            num3= int(input("Ingrese la opción: "))
            while num3 != 3:
                if num3==1:
                   n=actualizar_ómnibus(n)
                   print("La lista actualizada es: ", n)
                elif num3==2:
                   n=new_omni(n)
                   print("La lista oficial de los Ómnibus son: ", n)
                print("[1] Actualizar Datos\n[2] Registrar nuevos Ómnibus\n[3] Menú Principal") 
                num3= int(input("Ingrese la opción: "))
                    
        elif num==3:
           print("[1] Codigo y cantidad de Ómnibus\n[2] Choferes aptos en un día específico\n[3] Comprar pasaje\n[4] Menú Principal")
           num4=int(input("Ingrese la opción: "))
           while num4 != 4:
               if num4==1:
                   monstrar_Omnibus(n)
               elif num4==2:
                   choferesaptos(a)
               elif num4==3:
                   boleto_final(n)
           print("[1] Codigo y cantidad de Ómnibus\n[2] Choferes aptos en un día específico\n[3] Comprar pasaje\n[4] Menú Principal")
           num4=int(input("Ingrese la opción: "))

        print("[1] Registro de Choferes\n[2] Registro de Ómnibus\n[3] Reportes\n[4] Cerrar Menú")
        num=int(input("Ingrese la opción: "))
    print("Saliendo del sistema...")        
    crear_archivoChofer(a, nombre)
if __name__=="__main__":
    main()

