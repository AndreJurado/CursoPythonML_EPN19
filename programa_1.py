"""
Este script hace ........
Autor: LGFE
Fecha: 06/06/06
"""


from Geometry import area_figuras

# def hipotenusa(cateto_1, cateto_2):
#     """
#     Esta funcion calcula la hipo de un triag rect
#     :param cateto_1:
#     :param cateto_2:
#     :return:
#     """
#     hip = sqrt(cateto_1**2+cateto_2**2)
#     return hip

def main():

    area_circulo1 = area_figuras.circulo(radio=5)
    area_rectangulo1 = area_figuras.rectangulo(lado1=5,lado2=5)
    area_triangulo = area_figuras.triangulo(base=3,altura=5)



if __name__ == '__main__':
    main()


