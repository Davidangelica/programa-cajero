import re
def ingresar_dinero(ingresar,saldo):
    total = ingresar + saldo
    return total
                              

def retirar_dinero(saldo,retirar):
    total = saldo - retirar
    return total
    

def transferir_dinero(saldo,transferir):
    total = saldo - transferir
    return total


class error_nombre(Exception):
    def __init__(self,err):
        print(f'error: {err}')

def comprobar_nombre(nombre_destinatario):
   resultado = re.findall(r'\d', nombre_destinatario)
   if len(resultado) >= 1: raise error_nombre('no se permiten numeros en el nombre')
   else: return 'nombre correcto'

def consultar_credito(saldo):
    total = saldo*1.20
    return total

def tasas_credito(credito):
    print('1_ 3 meses: %2\n2_ 6 meses: %4.5\n3_ 12 meses: %9.5')
    
    while True:
        try:
            opc = int(input('ingrese la opcion: '))
            break
        except:
            print('escriba un numero')
            
    while opc not in (1,2,3):   
        while True:  
            try:    
                opc = int(input('ingrese un valor correcto: '))
                break
            except:
                print('escriba un numero')
    
    if opc == 1:
        credito = (credito*0.02) + credito
        print(f'credito a 3 meses\ntotal a pagar: {credito}')
        
    if opc == 2:
        credito = (credito*0.045) + credito
        print(f'credito a 6 meses\ntotal a pagar: {credito}')
        
    if opc == 3:
        credito = (credito*0.095) + credito
        print(f'credito a 12 meses\ntotal a pagar: {credito}')
        
    return credito


def plazo_fijo(saldo):
    print('selecione el plazo:\n1_ 3 meses\n2_ 6 meses\n3_ 12 meses')
    
    opc = input('ingrese una opcion: ')
    
    while opc not in ('1','2','3'):
        opc = input('ingrese una opcion correcta: ')
    
    if opc == '1':
        saldo = (saldo*0.025) * 3 + saldo
        return f'recibira {saldo} en 90 dias'
    
    if opc == '2':
        saldo = (saldo*0.025) * 6 + saldo
        return f'recibira {saldo} en 180 dias'
    
    if opc == '3':
        saldo = (saldo*0.025) * 12 + saldo
        return f'recibira {saldo} en 365 dias'

def cargar_usuario():
    while True:
        try:
            nombre_usuario = input('ingrese un nombre de usuario: ')
            comprobar_nombre(nombre_usuario)
            break
        except:
            print('cargue un usuario valido')
            
    while True:
        try:
            pin = int(input('cargue un pin de 4 numeros: '))
            break
        except:
            print('ingrese un numero')    
    
    while pin > 9999:
        while True:
            try:
                print('demaciados numeros')
                pin = int(input('ingrese el pin nuevamente: '))
                break
            except:
                print('escriba un numero')
        
    return nombre_usuario, pin
