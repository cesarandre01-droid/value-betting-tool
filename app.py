import streamlit as st
import pandas as pd
import re
import requests

st.title("⚡ Value Betting Finder (Correct Benchmark)")

API_KEY = "dd3f638fb38c7d3d8a500142243f5231"

input_text = st.text_area("Cole odds PT aqui:", height=200)

# -------- BENCHMARK POR SELEÇÃO --------
def get_benchmark():
    url = f"https://api.the-odds-api.com/v4/sports/soccer_spain_segunda_division/odds/?apiKey={API_KEY}&regions=eu&markets=h2h"

    response = requests.get(url)

    if response.status_code != 200:
        return {}

    data = response.json()
    benchmarks = {}

    for game in data:

        teams = game.get("teams", [])
        if len(teams) < 2:
            continue

        jogo = f"{teams[0]} vs {teams[1]}"

        sel_odds = {"1": [], "X": [], "2": []}

        for bookmaker in game.get("bookmakers", []):
            for market in bookmaker.get("markets", []):
                for outcome in market.get("outcomes", []):

                    name = outcome.get("name")
                    price = outcome.get("price")

                    if not name or not price:
                        continue

                    if name == teams[0]:
                        sel_odds["1"].append(price)
                    elif name == teams[1]:
                        sel_odds["2"].append(price)
                    elif name.lower() in ["draw", "tie"]:
                        sel_odds["X"].append(price)

        benchmarks[jogo] = {
            "1": max(sel_odds["1"]) if sel_odds["1"] else None,
            "X": max(sel_odds["X"]) if sel_odds["X"] else None,
            "2": max(sel_odds["2"]) if sel_odds["2"] else None
        }

    return benchmarks

# -------- PARSE PT --------
def parse(texto):
    linhas = [l.strip() for l in texto.split("\n") if l.strip()]
    dados = []

    for l in linhas:
        if "|" in l:
            partes = l.split("|")
            jogo = partes[0].strip()

            odds = re.findall(r"\d+[.,]\d+", partes[1])
            odds = [float(o.replace(",", ".")) for o in odds]

            for sel, odd in zip(["1", "X", "2"], odds):
                dados.append({
                    "Jogo": jogo,
                    "Selecao": sel,
                    "Odd": odd
                })

    return pd.DataFrame(dados)

# -------- CALCULAR VALUE --------
def calcular(df, benchmarks):
    resultados = []

    for _, row in df.iterrows():
        jogo = row["Jogo"]
        sel = row["Selecao"]
        odd = row["Odd"]

        if jogo not in benchmarks:
            continue

        odd_bench = benchmarks[jogo].get(sel)

        if not odd_bench:
            continue

        edge = (odd / odd_bench - 1) * 100

        if edge >= 4:
            resultados.append({
                "Jogo": jogo,
                "Seleção": sel,
                "Odd PT": odd,
                "Benchmark": round(odd_bench, 2),
                "Edge %": round(edge, 2)
            })

    return pd.DataFrame(resultados)

# -------- UI --------
if st.button("🔍 Procurar Value"):
    df = parse(input_text)

    if not df.empty:
        benchmarks = get_benchmark()

        res = calcular(df, benchmarks)

        if not res.empty:
            st.success("Oportunidades encontradas")
            st.dataframe(res)
        else:
            st.warning("Sem value")
    else:
        st.error("Erro a ler dados")
