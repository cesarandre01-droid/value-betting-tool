Last login: Wed Apr  1 11:41:14 on console
cesarandre@Cesars-Air ~ % python3 --version
Python 3.14.3
cesarandre@Cesars-Air ~ % python3 --version
Python 3.14.3
cesarandre@Cesars-Air ~ % pip3 --version
pip 25.3 from /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/pip (python 3.14)
cesarandre@Cesars-Air ~ % pip3 install streamlit pandas numpy
Collecting streamlit
  Downloading streamlit-1.56.0-py3-none-any.whl.metadata (9.8 kB)
Collecting pandas
  Downloading pandas-3.0.2-cp314-cp314-macosx_11_0_arm64.whl.metadata (79 kB)
Collecting numpy
  Downloading numpy-2.4.4-cp314-cp314-macosx_14_0_arm64.whl.metadata (6.6 kB)
Collecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit)
  Downloading altair-6.0.0-py3-none-any.whl.metadata (11 kB)
Collecting blinker<2,>=1.5.0 (from streamlit)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cachetools<8,>=5.5 (from streamlit)
  Downloading cachetools-7.0.5-py3-none-any.whl.metadata (5.6 kB)
Collecting click<9,>=7.0 (from streamlit)
  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)
  Downloading gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)
Collecting packaging>=20 (from streamlit)
  Downloading packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pillow<13,>=7.1.0 (from streamlit)
  Downloading pillow-12.1.1-cp314-cp314-macosx_11_0_arm64.whl.metadata (8.8 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Collecting protobuf<8,>=3.20 (from streamlit)
  Downloading protobuf-7.34.1-cp310-abi3-macosx_10_9_universal2.whl.metadata (595 bytes)
Collecting pyarrow>=7.0 (from streamlit)
  Downloading pyarrow-23.0.1-cp314-cp314-macosx_12_0_arm64.whl.metadata (3.1 kB)
Collecting requests<3,>=2.27 (from streamlit)
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting tenacity<10,>=8.1.0 (from streamlit)
  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting toml<2,>=0.10.1 (from streamlit)
  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit)
  Downloading tornado-6.5.5-cp39-abi3-macosx_10_9_universal2.whl.metadata (2.8 kB)
Collecting typing-extensions<5,>=4.10.0 (from streamlit)
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting narwhals>=1.27.1 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading narwhals-2.18.1-py3-none-any.whl.metadata (14 kB)
Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Downloading smmap-5.0.3-py3-none-any.whl.metadata (4.6 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->streamlit)
  Downloading charset_normalizer-3.4.6-cp314-cp314-macosx_10_15_universal2.whl.metadata (40 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.27->streamlit)
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.26 (from requests<3,>=2.27->streamlit)
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2023.5.7 (from requests<3,>=2.27->streamlit)
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading streamlit-1.56.0-py3-none-any.whl (9.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.1/9.1 MB 80.3 MB/s  0:00:00
Downloading pandas-3.0.2-cp314-cp314-macosx_11_0_arm64.whl (9.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 96.1 MB/s  0:00:00
Downloading numpy-2.4.4-cp314-cp314-macosx_14_0_arm64.whl (5.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 95.0 MB/s  0:00:00
Downloading altair-6.0.0-py3-none-any.whl (795 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 795.4/795.4 kB 40.1 MB/s  0:00:00
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading cachetools-7.0.5-py3-none-any.whl (13 kB)
Downloading click-8.3.1-py3-none-any.whl (108 kB)
Downloading gitpython-3.1.46-py3-none-any.whl (208 kB)
Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
Downloading pillow-12.1.1-cp314-cp314-macosx_11_0_arm64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 80.7 MB/s  0:00:00
Downloading protobuf-7.34.1-cp310-abi3-macosx_10_9_universal2.whl (429 kB)
Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 16.6 MB/s  0:00:00
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.6-cp314-cp314-macosx_10_15_universal2.whl (294 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading smmap-5.0.3-py3-none-any.whl (24 kB)
Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Downloading tornado-6.5.5-cp39-abi3-macosx_10_9_universal2.whl (445 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl (12 kB)
Downloading narwhals-2.18.1-py3-none-any.whl (444 kB)
Downloading packaging-26.0-py3-none-any.whl (74 kB)
Downloading pyarrow-23.0.1-cp314-cp314-macosx_12_0_arm64.whl (34.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 34.2/34.2 MB 78.9 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl (353 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: urllib3, typing-extensions, tornado, toml, tenacity, smmap, six, rpds-py, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, idna, click, charset_normalizer, certifi, cachetools, blinker, attrs, requests, referencing, python-dateutil, jinja2, gitdb, pydeck, pandas, jsonschema-specifications, gitpython, jsonschema, altair, streamlit
Successfully installed MarkupSafe-3.0.3 altair-6.0.0 attrs-26.1.0 blinker-1.9.0 cachetools-7.0.5 certifi-2026.2.25 charset_normalizer-3.4.6 click-8.3.1 gitdb-4.0.12 gitpython-3.1.46 idna-3.11 jinja2-3.1.6 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 narwhals-2.18.1 numpy-2.4.4 packaging-26.0 pandas-3.0.2 pillow-12.1.1 protobuf-7.34.1 pyarrow-23.0.1 pydeck-0.9.1 python-dateutil-2.9.0.post0 referencing-0.37.0 requests-2.33.1 rpds-py-0.30.0 six-1.17.0 smmap-5.0.3 streamlit-1.56.0 tenacity-9.1.4 toml-0.10.2 tornado-6.5.5 typing-extensions-4.15.0 urllib3-2.6.3

[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: pip3 install --upgrade pip
cesarandre@Cesars-Air ~ % touch app.py
cesarandre@Cesars-Air ~ % open -e app.py
cesarandre@Cesars-Air ~ % streamlit run app.py

      👋 Welcome to Streamlit!

      If you'd like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email:                     

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.64:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
open -e app.py
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")
st.title("📊 Value Betting Dashboard")

THRESHOLDS = {
    "Betano": 0.035,
    "Placard": 0.04,
    "Bwin": 0.05,
    "Betclic": 0.05,
    "Solverde": 0.05,
    "ESC": 0.05
}

input_text = st.text_area(
    "Inserir odds (formato):\nJogo | Hora | Liga | Mercado | Selecao | Casa | Odd",
    height=200
)

def calcular(df):
    resultados = []

    grupos = df.groupby(["Jogo", "Hora", "Liga", "Mercado"])

    for info, grupo in grupos:

        selecoes = grupo.groupby("Selecao")

        for sel, g in selecoes:

            if len(g) < 2:
                continue

            odds = g["Odd"].tolist()

            preco_justo = sum(odds) / len(odds) / 0.95

            melhor_row = g.loc[g["Odd"].idxmax()]
            melhor_odd = melhor_row["Odd"]
            casa_top = melhor_row["Casa"]

            threshold = THRESHOLDS.get(casa_top, 0.05)

            m
