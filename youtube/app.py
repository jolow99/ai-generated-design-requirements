from code1 import code1
from code2 import code2
import pandas as pd

def main(): 
    products = [
    "Delonghi Dedica",
    "Delonghi Dinamica",
    "Delonghi Eletta",
    "Delonghi Icona",
    "Delonghi La Specialista",
    "Delonghi Lattissima",
    "Delonghi Magnifica",
    "Delonghi Perfecta",
    "Delonghi Prima Donna",
    "Delonghi Stilosa",
    ]

    for product in products: 
        max_result = 20
        code1(product, max_result)
        code2()

if __name__ == main():
    main()