import streamlit as st
import math

# Função para realizar a operação
def calcular(num1, num2, operador):
    if operador == '+':
        return round(num1 + num2, 2)
    elif operador == '-':
        return round(num1 - num2, 2)
    elif operador == '/':
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return round(num1 / num2, 2)
    elif operador == '*':
        return round(num1 * num2, 2)
    elif operador == 'sin':
        return round(math.sin(math.radians(num1)), 2)
    elif operador == 'cos':
        return round(math.cos(math.radians(num1)), 2)
    elif operador == 'tan':
        return round(math.tan(math.radians(num1)), 2)
    elif operador == 'exp':
        return round(math.exp(num1), 2)
    else:
        return "Operador inválido!"

# Interface do Streamlit
st.title("Calculadora Científica Simples")
st.header("Realize operações matemáticas facilmente")

# Entrada do usuário
numero_1 = st.text_input("Digite um número:")
numero_2 = st.text_input("Digite outro número (não usado em funções científicas):")
operador = None

# Botões para operações
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("+"):
        operador = '+'
with col2:
    if st.button("-"):
        operador = '-'
with col3:
    if st.button("*"):
        operador = '*'
with col4:
    if st.button("/"):
        operador = '/'
with col5:
    if st.button("sin"):
        operador = 'sin'
with col1:
    if st.button("cos"):
        operador = 'cos'
with col2:
    if st.button("tan"):
        operador = 'tan'
with col3:
    if st.button("exp"):
        operador = 'exp'

# Lista para armazenar histórico de cálculos
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Botão para calcular
if operador and st.button("Calcular"):
    numeros_validos = True
    
    try:
        num_1_float = float(numero_1)
        if operador in ['+', '-', '*', '/']:
            num_2_float = float(numero_2)  # O segundo número é necessário apenas para algumas operações
    except ValueError:
        st.error('Um ou ambos os números são inválidos.')
        numeros_validos = False

    if numeros_validos:
        resultado = calcular(num_1_float, num_2_float if operador in ['+', '-', '*', '/'] else None, operador)
        
        # Armazenar resultado no histórico
        if isinstance(resultado, float) or isinstance(resultado, str):
            st.success(f'Resultado: {num_1_float} {operador} {num_2_float if operador in ["+", "-", "*", "/"] else ""} = {resultado}')
            st.session_state.historico.append(f'{num_1_float} {operador} {num_2_float if operador in ["+", "-", "*", "/"] else ""} = {resultado}')

# Mostrar histórico
if st.session_state.historico:
    st.subheader("Histórico de Cálculos")
    for item in st.session_state.historico:
        st.write(item)

# Botão para limpar entradas
if st.button("Limpar"):
    st.session_state.historico = []
    st.experimental_rerun()  # Redefine o estado da página

# Opção para sair
if st.button("Sair"):
    st.stop()  # Para encerrar o aplicativo
