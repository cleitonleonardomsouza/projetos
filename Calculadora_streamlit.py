import streamlit as st
import math

# Função para realizar as operações
def calcular(num1, num2, operador):
    if operador == 'Soma':
        return round(num1 + num2, 2)
    elif operador == 'Subtração':
        return round(num1 - num2, 2)
    elif operador == 'Multiplicação':
        return round(num1 * num2, 2)
    elif operador == 'Divisão':
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return round(num1 / num2, 2)
    elif operador == 'Seno':
        return round(math.sin(math.radians(num1)), 2)
    elif operador == 'Cosseno':
        return round(math.cos(math.radians(num1)), 2)
    elif operador == 'Tangente':
        return round(math.tan(math.radians(num1)), 2)
    elif operador == 'Exponencial':
        return round(math.exp(num1), 2)
    elif operador == 'Logaritmo':
        return round(math.log(num1), 2) if num1 > 0 else "Erro: Logaritmo não definido para zero ou números negativos."
    elif operador == 'Raiz Quadrada':
        return round(math.sqrt(num1), 2) if num1 >= 0 else "Erro: Raiz quadrada de número negativo."

# Interface do Streamlit
st.title("Calculadora Científica")
st.header("Realize operações matemáticas e científicas")

# Entrada da forma básica
num1 = st.text_input("Digite um número:")

# Verifica se o usuário inseriu um valor numérico
if num1 != "":
    num1 = float(num1)
else:
    num1 = None

# Adiciona botões para operações
if st.button("Soma"):
    if num1 is not None:
        num2 = st.text_input("Digite outro número:")
        if num2:
            resultado = calcular(num1, float(num2), 'Soma')
            st.success(f'Resultado: {num1} + {num2} = {resultado}')

if st.button("Subtração"):
    if num1 is not None:
        num2 = st.text_input("Digite outro número:")
        if num2:
            resultado = calcular(num1, float(num2), 'Subtração')
            st.success(f'Resultado: {num1} - {num2} = {resultado}')

if st.button("Multiplicação"):
    if num1 is not None:
        num2 = st.text_input("Digite outro número:")
        if num2:
            resultado = calcular(num1, float(num2), 'Multiplicação')
            st.success(f'Resultado: {num1} * {num2} = {resultado}')

if st.button("Divisão"):
    if num1 is not None:
        num2 = st.text_input("Digite outro número:")
        if num2:
            resultado = calcular(num1, float(num2), 'Divisão')
            st.success(f'Resultado: {num1} ÷ {num2} = {resultado}')

# Adiciona botões para funções científicas
if st.button("Seno"):
    if num1 is not None:
        resultado = calcular(num1, 0, 'Seno')
        st.success(f'Seno de {num1}° = {resultado}')

if st.button("Cosseno"):
    if num1 is not None:
        resultado = calcular(num1, 0, 'Cosseno')
        st.success(f'Cosseno de {num1}° = {resultado}')

if st.button("Tangente"):
    if num1 is not None:
        resultado = calcular(num1, 0, 'Tangente')
        st.success(f'Tangente de {num1}° = {resultado}')

if st.button("Exponencial"):
    if num1 is not None:
        resultado = calcular(num1, 0, 'Exponencial')
        st.success(f'e^{num1} = {resultado}')

if st.button("Logaritmo"):
    if num1 is not None:
        resultado = calcular(num1, 0, 'Logaritmo')
        st.success(f'ln({num1}) = {resultado}')

if st.button("Raiz Quadrada"):
    if num1 is not None:
        resultado = calcular(num1, 0, 'Raiz Quadrada')
        st.success(f'Raiz quadrada de {num1} = {resultado}')
