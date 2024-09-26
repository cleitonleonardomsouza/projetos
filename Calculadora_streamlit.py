import streamlit as st

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

# Interface do Streamlit
st.title("Calculadora Simples")
st.header("Realize operações matemáticas facilmente")

# Entrada do usuário
numero_1 = st.text_input("Digite um número:")
numero_2 = st.text_input("Digite outro número:")
operador = st.selectbox("Escolha um operador:", ['+', '-', '*', '/'])

# Lista para armazenar histórico de cálculos
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Botão para calcular
if st.button("Calcular"):
    numeros_validos = True
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except ValueError:
        st.error('Um ou ambos os números são inválidos.')
        numeros_validos = False

    if numeros_validos:
        resultado = calcular(num_1_float, num_2_float, operador)
        
        # Armazenar resultado no histórico
        if isinstance(resultado, float):
            st.success(f'Resultado: {num_1_float} {operador} {num_2_float} = {resultado}')
            st.session_state.historico.append(f'{num_1_float} {operador} {num_2_float} = {resultado}')
        else:
            st.error(resultado)

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
