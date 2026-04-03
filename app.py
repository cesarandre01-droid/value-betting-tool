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

        # classificação visual
        if edge >= 4:
            status = "🟢 VALUE"
        elif edge >= 2:
            status = "🟡 QUASE"
        else:
            status = "🔴 NO VALUE"

        resultados.append({
            "Jogo": melhor["Jogo"],
            "Seleção": sel,
            "Casa": melhor["Casa"],
            "Odd PT": melhor["Odd"],
            "Benchmark": round(odd_bench, 2),
            "Edge %": round(edge, 2),
            "Status": status
        })

    return pd.DataFrame(resultados)
