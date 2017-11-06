"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in 
the sequence.

Input: a list of strings.
Output: a string.

Example:

most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""
def most_frequent(datat):
    temporal = list(set(data))
    frecuencia= dict.fromkeys(temporal)
    for elemento in frecuencia:
        frecuencia[str(elemento)]=data.count(elemento)
    return sorted(frecuencia.keys(), key=frecuencia.__getitem__)[-1]

a = most_frequent(['ca', 'ca', 'ca', 'ca','a', 'a', 'bi', 'bi', 'bi'])