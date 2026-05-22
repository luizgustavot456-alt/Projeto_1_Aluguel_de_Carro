import streamlit as st

#---------------------------------- SIDEBAR
st.sidebar.title("Mate Aluguel de carro")
st.sidebar.title("Mate Aluguel de carro")

carros = ["Porche", "Chevete", "Opala", "Mercedes"]

carro = st.sidebar.selectbox("escolha seu carro", carros)

#----------------------------- BODY
st.title("Mate Aluguel de carro")

st.image(f"{carro}.png")
st.write(f"Voce escolheu o {carro}")

if carros == "Porche":
    diaria = 3500
elif carros == "Chevete":
    diaria = 450
elif carros == "Opala":
    diaria = 1000
elif carros == "Mercedes":
    diaria = 3000

dias = st.text_input(f"Por quantos dias vc alugou o {carro}?")
km = st.text_input(f"Quantos vc rodou com o {carro}?")

if st.button("Calcular"):
    dias = float(dias)
    km = float(dias)

    total = (diaria * dias) + (km*0.15)
    st.warning(f"Vc alugou o {carro} por {dias} dias e rodou {km}km. ")