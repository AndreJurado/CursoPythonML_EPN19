"""
Esta es al libreria de areas de  figuras geometricas
autor
fecha
obsevaciones
version
"""
#%%
from math import pow, pi

#%%


def circulo(radio):
    """
    Esta funcion devuelve el area de un circulo de radio r
    :param radio: es un numero real
    :return: area como numero real
    """
    area = pi*pow(radio,2)
    print('Area de un circulo de radio {} es {:.3f}'.format(radio, area))

    return area
#%%


def rectangulo(lado1, lado2):
    """
    Esta funcion devuelve el area de un circulo de radio r
    :param radio: es un numero real
    :return: area como numero real
    """
    area = lado1*lado2
    print('Area de un rectagulo de lado1 {} y lado2 {} es {}'.format(lado1, lado2, area))


    return area
#%%


def triangulo(base, altura):
    """
    Esta funcion devuelve el area de un circulo de radio r
    :param radio: es un numero real
    :return: area como numero real
    """
    area = base*altura/2
    print('Area de un triangulo de base{} y altura {} es {}'.format(base, altura, area))
    return area

if __name__ == '__main__':
    circulo(radio=5)
    rectangulo(lado1=5, lado2=5)
    triangulo(base=3, altura=5)

