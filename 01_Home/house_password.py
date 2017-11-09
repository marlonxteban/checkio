"""
Stephan y Sophia no se preocupan por la seguridad y usan contraseñas sencillas para todo. Ayuda a a Nikola a desarrollar un módulo para verificar la seguridad de la contraseña o password. 
La contraseña será considerada suficientemente fuerte si 
el largo es mayor o igual a 10 caracteres, 
tiene por lo menos un dígito, 
así como una letra en mayúscula y una letra en minúscula. 
La contraseña contiene solo letras latinas o dígitos ASCII.
Entrada: La contraseña como una cadena o string (Unicode para python 2.7).
Salida: Si la contraseña es segura o no representada mediante un booleano o cualquier otro tipo de dato que pueda ser convertido y procesado como un booleano. En los resultados finales podrás ver los resultados convertidos.
checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

Pre-condición:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""
import string
def checkio(data):
    if len(data)<10:
        return False

    minuscula = False
    mayuscula = False
    numero = False
    minusculas=string.ascii_lowercase
    mayusculas=string.ascii_uppercase
    numeros=string.digits
    for ch in data:
        if ch in minusculas:
            minuscula = True
        if ch in mayusculas:
            mayuscula=True
        if ch in numeros:
            numero = True
         
    return minuscula and mayuscula and numero

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")