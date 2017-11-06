def checkio(text):
    text = text.lower()
    ascii_alphabet= "".join([chr(x) for x in range(ord('a'), ord('z')+1)])
    cuenta = [(text.count(letra)* -1,letra) for letra in ascii_alphabet] 
    #el orden es #, letra porque min() revisa primero el primer elemento y si hay mas de una coincidencia 
    # evalua el segundo elemento, si se pusiera primero la letra, simepre devolveria la letra 'a'
    return min(cuenta)[1]
checkio("aaabbbccccddddde opef")