"""Como Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Viviane Araujo Vieira
Enunciado: Convertendo expressões matematicas para python"""

# Recebe dados numericos do usuario
 
from traceback import print_last


base = int(input("Digite a base:"))

expoente = int(input("Digite o expoente: "))
 
divisor = int(input("digite o divisor: "))


resultado = (base**expoente) / divisor

print(f"resultado da operação é: {resultado:.2f}" )



 