"""
El Teorema del mono infinito afirma que un mono pulsando teclas al azar sobre un teclado durante un periodo de tiempo infinito casi seguramente podrá escribir un texto determinado, como los trabakos completos de John Wallis, o más probablemente, una novela de Dan Brown .
Supongamos que nuestros monos están tecleando, tecleando y tecleando, y han producido una amplia variedad de segmentos cortos de texto. Intentemos revisarlos en busca de la inclusión de palabras legibles.
Se te da algún texto que potencialmente incluye palabras legibles. Debes contar cuantas palabras están incluidas en el texto proporcionado. Una palabra debería estar completa y podría ser parte de otra palabra. Mayúsculas o mínusculas en el texto no importan. Las palabras son dadas en mminúsculas y no se repiten. Si una palabra aparece varias veces en el texto, sólo debe ser contada una vez.
Por ejemplo, texto - "How aresjfhdskfhskd you?", palabras - ("how", "are", "you", "hello"). El resultado sería 3.
Entrada: Dos argumentos. Un texto como caracter (unicode para py2) y palabras como un set de caracteres (unicode para py2).
Salida: El numero de palabras en el texto como un entero.
count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1
Precondicion:
0 < len(text) ≤ 256
all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
"""

def count_words(text, words):
    contadas = set()
    text = text.lower().split(" ")
    for cadena in text:
        for palabra in words:
            if palabra in cadena:
                contadas.add(palabra)

    return len(contadas)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")