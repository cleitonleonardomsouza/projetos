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
    elif operador == 'potência':
        return round(num1 ** num2, 2)
    elif operador == 'raiz quadrada':
        if num1 < 0:
            return "Erro: Raiz de número negativo!"
        return round(math.sqrt(num1), 2)
    elif operador == 'seno':
        return round(math.sin(math.radians(num1)), 2)
    elif operador == 'cosseno':
        return round(math.cos(math.radians(num1)), 2)
    elif operador == 'tangente':
        return round(math.tan(math.radians(num1)), 2)
    elif operador == 'logaritmo':
        if num1 <= 0:
            return "Erro: Logaritmo de número não positivo!"
        return round(math.log(num1), 2)
    else:
        return "Operador inválido!"

# Interface do Streamlit
st.title("Calculadora Científica")
st.header("Realize operações matemáticas e científicas facilmente")

# Opções de operação
operacao = st.selectbox("Escolha uma operação:", [
    '+', '-', '*', '/', 'potência', 'raiz quadrada',
    'seno', 'cosseno', 'tangente', 'logaritmo'
])

numero_1 = st.text_input("Digite um número:")
numero_2 = st.text_input("Digite outro número (se necessário):")

# Lista para armazenar histórico de cálculos
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Botão para calcular
if st.button("Calcular"):
    numeros_validos = True
    
    try:
        num_1_float = float(numero_1)
        if operacao in ['+', '-', '*', '/', 'potência', 'logaritmo']:
            num_2_float = float(numero_2)
        else:
            num_2_float = None  # Não necessário para funções como raiz, seno, etc.
    except ValueError:
        st.error('Um ou ambos os números são inválidos.')
        numeros_validos = False

    if numeros_validos:
        resultado = calcular(num_1_float, num_2_float, operacao)
        
        # Armazenar resultado no histórico
        if isinstance(resultado, float) or isinstance(resultado, str) and "Erro" not in resultado:
            st.success(f'Resultado: {num_1_float} {operacao} {num_2_float if num_2_float is not None else ""} = {resultado}')
            st.session_state.historico.append(f'{num_1_float} {operacao} {num_2_float if num_2_float is not None else ""} = {resultado}')
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
