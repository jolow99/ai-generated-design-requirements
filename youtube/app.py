from code1 import code1
from code2 import code2
import pandas as pd

def main(): 
    products = [
    "Delonghi All-In-One Combination coffee maker", 
    "Delonghi Clessidra", 
    "Delonghi Dedica",
    "Delonghi Dinamica",
    "Delonghi Eletta",
    "Delonghi Icona",
    "Delonghi La Specialista",
    "Delonghi Lattissima",
    "Delonghi Maestosa",
    "Delonghi Magnifica",
    "Delonghi Perfecta",
    "Delonghi Prima Donn",
    "Delonghi Stilosa",
    "Delonghi Vertuo Next"
    ]

    for product in products: 
        max_result = 5
        code1(product, max_result)
        code2()

if __name__ == main():
    main()