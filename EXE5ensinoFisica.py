#EXE 5
import streamlit as st #Parte grafica
import pandas as pd #Dados
import numpy as np #Variaveis para
import matplotlib.pyplot as plt
import math


st.title('Auxilio no ensino de Física')
Aba1, Aba2, Aba3, Aba4, Aba5, Aba6 = st.tabs(['Reflexão da luz', 'Evaporação', 'Eletricidade',
                                        'Propagação do Som', 'Magnetismo', 'Formulas Aplicadas'])
with Aba1:
    st.markdown('***Reflexão da luz*** :rainbow:')
    st.subheader('É a mudança de direção que a luz sofre ao bater em uma superfície,como um espelho. Graças a esse fenômeno, podemos ver nosso reflexo.')
    st.text('Sobre sua formula e lei')
    st.image('reflexaodaluz.png')

    
with Aba2:
    st.markdown('***Evaporação***:droplet:')
    st.subheader('É o processo pelo qual um líquido (como a água) se transforma em vapor devido ao aumento da temperatura.')
    st.text('Sobre sua formula e lei')
    st.image('evaporacao.png')
    
with Aba3:
    st.markdown('***Eletricidade***:zap:')
    st.subheader('É o movimento dos elétrons através de um condutor. Manifesta-se em fenômenos como os raios ou no funcionamento de aparelhos elétricos.')
    st.text('Sobre sua formula e lei')
    st.image('eletricidade.png')
    
with Aba4:
    st.markdown('***Propagação do Som***:musical_note::soon:')
    st.subheader('É a transmissão das ondas sonoras através de um meio (ar, água ou sólidos). Por exemplo, quando ouvimos música ou uma voz.')
    st.text('Sobre sua formula e lei')
    st.image('propagacaodosom.png')

with Aba5:
    st.markdown('***Magnetismo***:magnet:')
    st.subheader('É a força de atração ou repulsão exercida por ímãs ou materiais magnéticos. É usada em motores, bússolas e alto-falantes.')
    st.text('Sobre sua formula e lei')
    st.image('magnetismo.png')

with Aba6:
    st.title("🌍  5 Fenômenos Físicos ")
    st.subheader('Escolha um fenômeno físico e o app calcula o resultado com base nas fórmulas que vimos')
    # Menu de seleção
    fenomeno = st.selectbox(
        "Escolha um fenômeno físico:",
        ["Reflexão da Luz", "Evaporação", "Eletricidade", "Propagação do Som", "Magnetismo"]
    )

    if fenomeno == "Reflexão da Luz":
        st.subheader("🌈 Lei da Reflexão: θi = θr")
        ang_inc = st.number_input("Ângulo de incidência (em graus):", min_value=0.0, max_value=90.0)
        st.write(f"➡️ Ângulo de reflexão: **{ang_inc:.2f}°**")

    elif fenomeno == "Evaporação":
        st.subheader("💧 Calor de Vaporização: Q = m * L")
        m = st.number_input("Massa (kg):", min_value=0.0)
        Lv = st.number_input("Calor latente de vaporização (J/kg):", min_value=0.0)
        Q = m * Lv
        st.write(f"➡️ Quantidade de calor necessária: **{Q:.2f} J**")

    elif fenomeno == "Eletricidade":
        st.subheader("⚡ Lei de Ohm: V = R * I")
        R = st.number_input("Resistência (Ω):", min_value=0.0)
        I = st.number_input("Corrente elétrica (A):", min_value=0.0)
        V = R * I
        st.write(f"➡️ Tensão elétrica: **{V:.2f} V**")

    elif fenomeno == "Propagação do Som":
        st.subheader("🔊 v = λ * f")
        lamb = st.number_input("Comprimento de onda (m):", min_value=0.0)
        f = st.number_input("Frequência (Hz):", min_value=0.0)
        v = lamb * f
        st.write(f"➡️ Velocidade do som: **{v:.2f} m/s**")

    elif fenomeno == "Magnetismo":
        st.subheader("🧲 F = q * v * B * sen(θ)")
        q = st.number_input("Carga elétrica (C):", min_value=0.0)
        v = st.number_input("Velocidade da partícula (m/s):", min_value=0.0)
        B = st.number_input("Campo magnético (T):", min_value=0.0)
        theta = st.number_input("Ângulo entre v e B (graus):", min_value=0.0, max_value=180.0)
        F = q * v * B * math.sin(math.radians(theta))
        st.write(f"➡️ Força magnética: **{F:.4f} N**")

    st.markdown("---")
    st.caption("Desenvolvido💻 por Dayse Passos com a ajuda do CHAT nas formulas rs'")





    
