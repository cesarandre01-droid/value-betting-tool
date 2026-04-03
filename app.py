import streamlit as st
import pandas as pd
import re

st.title("⚡ Value Betting Finder")

input_text = st.text_area("Cole odds aqui:", height=250)

def parse(texto):
    linhas = [l.strip() for l in texto.split("\n") if l.strip()]
    dados = []

    casa = None

    for l in linhas:
        if l in ["Betano", "Solverde", "Placard", "Bwin", "Betclic", "Benchmark"]:
            casa = l
            continue

        if "|" in l:
            partes = l.split("|")

            jogo = partes[0].strip()
            tempo = partes[1].strip()
            liga = partes[2].strip()
            mercado = partes[3].strip()

            odds = re.findall(r"\d+[.,]\d+", partes[4])
            odds = [float(o.replace(",", ".")) for o in odds]

            for sel, odd in zip(["1", "X", "2"], odds):
                dados.append({
                    "Jogo": jogo,
                    "Hora": tempo,
                    "Liga": liga,
                    "Mercado": mercado,
                    "Selecao": sel,
                    "Casa": casa,
                    "Odd": odd
                })

    return pd.DataFrame(dados)

def calcular(df):
    resultados = []

    grupos = df.groupby(["Jogo", "Selecao", "Mercado"])

    for (jogo, sel, mercado), g in grupos:

        bench = g[g["Casa"] == "Benchmark"]
        pt = g[g["Casa"] != "Benchmark"]

        if bench.empty or pt.empty:
            continue

        odd_bench = max(bench["Odd"])
        melhor = pt.loc[pt["Odd"].idxmax()]

        edge = (melhor["Odd"] / odd_bench - 1) * 100

        if edge >= 4:
            resultados.append({
                "Jogo": jogo,
                "Hora": melhor["Hora"],
                "Mercado": mercado,
                "Seleção": sel,
                "Casa": melhor["Casa"],
                "Odd": melhor["Odd"],
                "Edge %": round(edge, 2)
            })

    return pd.DataFrame(resultados)

if st.button("🔍 Procurar Value"):
    df = parse(input_text)

    if not df.empty:
        res = calcular(df)

        if not res.empty:
            st.success("Oportunidades encontradas")
            st.dataframe(res)
        else:
            st.warning("Sem value")
    else:
        st.error("Erro a ler dados")
