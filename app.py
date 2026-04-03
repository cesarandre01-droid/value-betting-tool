import streamlit as st
import pandas as pd
import re
import requests
import unicodedata

st.title("⚡ Value Finder PT vs Market")

API_KEY = "dd3f638fb38c7d3d8a500142243f5231"

input_text = st.text_area("Cole odds das casas PT:", height=300)

# -------- NORMALIZAR --------
def normalize(text):
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    return text

# -------- BENCHMARK --------
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

        jogo_norm = normalize(f"{teams[0]} vs {teams[1]}")

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

        benchmarks[jogo_norm] = {
            k: max(v) if v else None for k, v in sel_odds.items()
        }

    return benchmarks

# -------- PARSE PT --------
def parse(text):
    linhas = [l.strip() for l in text.split("\n") if l.strip()]
    dados = []

    casa = None
    jogo = None

    casas_validas = ["betano", "solverde", "placard", "bwin", "betclic", "esc"]

    for l in linhas:

        l_norm = normalize(l)

        if any(c in l_norm for c in casas_validas):
            casa = l.strip()
            continue

        if "vs" in l.lower():
            jogo = l.strip()
            continue

        odds = re.findall(r"\d+[.,]\d+", l)

        if odds and casa and jogo:
            odds = [float(o.replace(",", ".")) for o in odds]

            for sel, odd in zip(["1", "X", "2"], odds):
                dados.append({
                    "Jogo": jogo,
                    "Jogo_norm": normalize(jogo),
                    "Casa": casa,
                    "Selecao": sel,
                    "Odd": odd
                })

    return pd.DataFrame(dados)

# -------- CALCULAR --------
def calcular(df, benchmarks):
    resultados = []

    grupos = df.groupby(["Jogo_norm", "Selecao"])

    for (jogo, sel), g in grupos:

        if jogo not in benchmarks:
            continue

        odd_bench = benchmarks[jogo].get(sel)
        if not odd_bench:
            continue

        melhor = g.loc[g["Odd"].idxmax()]

        edge = (melhor["Odd"] / odd_bench - 1) * 100

        if edge >= 4:
            resultados.append({
                "Jogo": melhor["Jogo"],
                "Seleção": sel,
                "Casa": melhor["Casa"],
                "Odd PT": melhor["Odd"],
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
            st.success("🔥 Oportunidades encontradas")
            st.dataframe(res)
        else:
            st.warning("Sem value")
    else:
        st.error("Erro a ler dados")
