#crear un programa de un cajero, en el cual se pueda
#ver saldo disponible 
#ingresar dinero a la cuenta
#sacar dinero de la cuenta 
#transferir a otra cuenta
#pedir un credito con tasa anual al %6
#hacer un plazo fijo con tasa anual %4

import funciones_cajero as funciones
import re 
import pandas as pd 
class programa():
    saldo = 0
    print('bienvenidos al banco FED bank® ')
    usuario, pin = funciones.cargar_usuario()
    print('')
    print(f'hola {usuario} su pin es {pin}')
    
    def menu (self):
        while True:
            print('-----------------')
            print('1_consultar saldo')
            print('2_ingresar dinero')
            print('3_retirar dinero')
            print('4_transferir')
            print('5_creditos')
            print('6_plazos fijos')
            print('7_salir')
            
            opcion = input('ingrese la opcion: ')
            while opcion not in ('1','2','3','4','5','6','7'):
                opcion = input('ingrese un valor correcto: ')
                
            if opcion == '1':
               consultar = consultar_saldo()
               print(consultar)
               
            
            if opcion == '2':
                while True:
                    try:
                        ingresar = int(input('cargue la cantidad de dinero a ingresar: '))
                        break
                    except:
                        print('valor incorrecto')
                        
                total = funciones.ingresar_dinero(ingresar,saldo())
                programa.saldo = total
                print(f'su nuevo saldo es {programa.saldo}')
                        
                        
            if opcion == '3':
                while True:
                    try:
                        retirar = int(input('ingrese la cantidad a retirar: '))
                        break
                    except:
                        print('ingrese un valor correcto')
                        
                while retirar > programa.saldo:
                    print('el retiro no puede ser mayor a su saldo')
                    while True:
                        try:
                            retirar = int(input('ingrese un valor nuevamente: '))
                            break
                        except:
                            print('ingrese un numero')
                total = funciones.retirar_dinero(saldo(), retirar)
                programa.saldo = total
                print(f'su nuevo saldo es {programa.saldo}')
                

            if opcion == '4':
                while True:
                    try:
                        nombre_destinatario = str(input('ingrese el nombre del destinatario: '))
                        print('comprobando nombre...')
                        funciones.comprobar_nombre(nombre_destinatario)
                        print('nombre correcto')
                        cbu = input('ingrese el numero de cuenta del destinatario: ')
                        str(cbu)
                        break
                    except:
                        print('error a cargar el usuario')
                        print('intente nuevamente')
                        
                while len(cbu) > 22:
                    print('el cbu tiene demasiados numeros')
                    cbu = str(input('ingrese nuevamente el cbu: '))
                    
                while True:
                    try:
                        print(f'saldo: {programa.saldo}')
                        transferencia = int(input('ingrese el monto que desea transferir: '))  
                        break
                    except:
                        print('escriba un numero')
                        
                while transferencia > programa.saldo:
                    print(f'maximo monto para transferir: {programa.saldo}')
                    print('monto no disponible')
                    while True:
                        try:
                            transferencia = int(input('ingrese un monto valido: '))
                            break
                        except:
                            print('escriba un numero')
                print('')
                print(f'nombre del destinatario: {nombre_destinatario}\ncbu: {cbu}\nimporte: {transferencia}')
    
                total = funciones.retirar_dinero(saldo(), transferencia)
                programa.saldo = total
                
                print(f'su saldo actual es {programa.saldo}')
                              
            
            if opcion == '5':
                max_credito = funciones.consultar_credito(saldo())
                print(f'maximo credito a pedir: {max_credito}')
               
                while True:
                    try:
                       credito = int(input('ingrese el monto del credito: '))
                       break
                    except:
                       print('ponga un numero')
                
                while credito > max_credito:
                    print('monto no disponible')
                    while True:
                        try:
                            credito = int(input('ingrese un valor correcto: '))
                            break
                        except:
                            print('ingrese un numero')    
                print('selecione la tasa')                                
                plazo = funciones.tasas_credito(credito)
                print(plazo)
                
                
            if opcion == '6':
                print('ingrese el monto que desea poner a plazo fijo')
                print(f'monto maximo: {programa.saldo}' )
                while True:
                    try:
                        plazo_fijo = int(input('ingrese el monto: '))
                        break
                    except:
                        print('ingrese un numero')
                        
                while plazo_fijo > programa.saldo:
                    print('monto no disponible')
                    while True:
                        try:
                            plazo_fijo = int(input('ingrese un valor correcto: '))
                            break
                        except:
                            print('ingrese un numero')
                            
                plazo = funciones.plazo_fijo(plazo_fijo)
                print(plazo)
                
                        
            if opcion == '7':
                print('saliendo...')
                break
            
def consultar_saldo():
  return f'su saldo es {programa.saldo}'         
                                                        
def saldo():
    return programa.saldo


banco = programa()
banco.menu()