import streamlit as st

# Função para realizar a operação
def calcular(num1, num2, operador):
    if operador == '+':
        return round(num1 + num2, 2)
    elif operador == '-':
        return round(num1 - num2, 2)
    elif operador == '/':
        return round(num1 / num2, 2)
    elif operador == '*':
        return round(num1 * num2, 2)

# Interface do Streamlit
st.title("Calculadora Simples")

# Entrada do usuário
numero_1 = st.text_input("Digite um número:")
numero_2 = st.text_input("Digite outro número:")
operador = st.selectbox("Escolha um operador:", ['+', '-', '*', '/'])

# Botão para calcular
if st.button("Calcular"):
    numeros_validos = True

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except ValueError:
        st.error('Um ou ambos dos números são inválidos.')
        numeros_validos = False

    if numeros_validos:
        if operador not in ['+', '-', '*', '/']:
            st.error('Operador inválido.')
        else:
            resultado = calcular(num_1_float, num_2_float, operador)
            st.success(f'Resultado: {num_1_float} {operador} {num_2_float} = {resultado}')

# Opção para sair
if st.button("Sair"):
    st.stop()  # Para encerrar o aplicativo
