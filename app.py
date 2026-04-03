import streamlit as st
import pandas as pd
import re
import requests
import unicodedata

st.title("⚡ Value Betting Finder (Multi-Market)")

API_KEY = "dd3f638fb38c7d3d8a500142243f5231"

input_text = st.text_area("Cole odds PT aqui:", height=250)

# -------- NORMALIZAR --------
def normalize(text):
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    return text

# -------- BENCHMARK --------
def get_benchmark():
    url = f"https://api.the-odds-api.com/v4/sports/soccer_spain_segunda_division/odds/?apiKey={API_KEY}&regions=eu&markets=h2h,totals,btts"

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
        jogo_norm = normalize(jogo)

        markets = {
            "1X2": {"1": [], "X": [], "2": []},
            "BTTS": {"YES": [], "NO": []},
            "OU": {"OVER": [], "UNDER": []}
        }

        for bookmaker in game.get("bookmakers", []):
            for market in bookmaker.get("markets", []):

                key = market.get("key")

                for outcome in market.get("outcomes", []):
                    name = outcome.get("name")
                    price = outcome.get("price")

                    if not name or not price:
                        continue

                    # 1X2
                    if key == "h2h":
                        if name == teams[0]:
                            markets["1X2"]["1"].append(price)
                        elif name == teams[1]:
                            markets["1X2"]["2"].append(price)
                        elif name.lower() in ["draw", "tie"]:
                            markets["1X2"]["X"].append(price)

                    # BTTS
                    elif key == "btts":
                        if name.lower() == "yes":
                            markets["BTTS"]["YES"].append(price)
                        elif name.lower() == "no":
                            markets["BTTS"]["NO"].append(price)

                    # Over/Under 2.5
                    elif key == "totals" and outcome.get("point") == 2.5:
                        if name.lower() == "over":
                            markets["OU"]["OVER"].append(price)
                        elif name.lower() == "under":
                            markets["OU"]["UNDER"].append(price)

        benchmarks[jogo_norm] = {
            m: {k: max(v) if v else None for k, v in sel.items()}
            for m, sel in markets.items()
        }

    return benchmarks

# -------- PARSE --------
def parse(texto):
    linhas = [l.strip() for l in texto.split("\n") if l.strip()]
    dados = []

    for l in linhas:
        if "|" in l:
            partes = l.split("|")

            jogo = partes[0].strip()
            jogo_norm = normalize(jogo)

            mercado = partes[1].strip().upper()

            odds = re.findall(r"\d+[.,]\d+", partes[2])
            odds = [float(o.replace(",", ".")) for o in odds]

            selecoes_map = {
                "1X2": ["1", "X", "2"],
                "BTTS": ["YES", "NO"],
                "OU": ["OVER", "UNDER"]
            }

            for sel, odd in zip(selecoes_map[mercado], odds):
                dados.append({
                    "Jogo": jogo,
                    "Jogo_norm": jogo_norm,
                    "Mercado": mercado,
                    "Selecao": sel,
                    "Odd": odd
                })

    return pd.DataFrame(dados)

# -------- CALCULAR --------
def calcular(df, benchmarks):
    resultados = []

    for _, row in df.iterrows():
        jogo = row["Jogo_norm"]
        mercado = row["Mercado"]
        sel = row["Selecao"]
        odd = row["Odd"]

        if jogo not in benchmarks:
            continue

        odd_bench = benchmarks[jogo].get(mercado, {}).get(sel)

        if not odd_bench:
            continue

        edge = (odd / odd_bench - 1) * 100

        if edge >= 4:
            resultados.append({
                "Jogo": row["Jogo"],
                "Mercado": mercado,
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
