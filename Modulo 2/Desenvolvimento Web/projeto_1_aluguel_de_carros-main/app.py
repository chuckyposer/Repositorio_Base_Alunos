import streamlit as st

#------------------------SIDEBAR
st.sidebar.image("logo.png")
st.sidebar.title("ALUCAR ☆ Aluguel de carros")

carros = ["OPALA-1","Mini cooper - LOROTA'S VERSION","Porsche"]

carro = st.sidebar.selectbox("Escolha seu carro:", carros)

#------------------------BODY
st.title("ALUCAR - Aluguel de carros")

st.image(f'{carro}.png')

st.write(f"Carro escolhido por você: {carro}")

if carro == "OPALA-1":
    diaria = 600

elif carro == "Mini cooper - LOROTA'S VERSION":
    diaria = 6000

elif carro == "Porsche":
    diaria = 1093

dias = st.text_input(f"Por quantos dias você deseja alugou o {carro}?")
km = st.text_input(f"Quantos quilômetros você rodou com o {carro}?")

if st.button("Calcular"):
    dias = float(dias)
    km = float(km)

    total = (diaria * dias) + (km*0.20)

    st.warning(f"Você alugou o {carro} por {dias} dias e rodou {km} km. O total a pagar é R${total}.")