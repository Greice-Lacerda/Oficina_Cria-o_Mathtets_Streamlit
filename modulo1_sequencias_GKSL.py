import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# TÍTULO PEDAGÓGICO
st.title("Explorador de Sequências Reais $x_n$")
st.markdown("Uma sequência é uma função com domínio nos Naturais ($\mathbb{N}$).")

# 1. ESCOPO DA SEQUÊNCIA (O que o usuário pode escolher)
# Oferecemos 5 modelos para análise de diferentes comportamentos de limite
opcoes = {
    "1/n (Convergente a zero)": lambda n: 1/n,
    "(-1)^n / n (Oscilante convergente)": lambda n: ((-1)**n) / n,
    "n / (n + 1) (Convergente a 1)": lambda n: n / (n + 1),
    "(-1)^n (Divergente/Oscilante)": lambda n: ((-1.0)**n),
    "log(n) (Divergente ao infinito)": lambda n: np.log(n)
}

selecao = st.selectbox("Escolha a sequência matemática:", list(opcoes.keys()))

# 2. CONTROLE DO N (O 'Infinito' computacional)
# O slider representa o crescimento do índice n da definição formal
n_max = st.slider("Visualizar até o termo n =", 5, 100, 20)

# 3. TRADUÇÃO DO DOMÍNIO DISCRETO
# np.arange(1, n_max + 1) garante que n seja apenas números inteiros (1, 2, 3...)
# Isso respeita a definição de sequência f: N -> R
n_valores = np.arange(1, n_max + 1)
x_n = opcoes[selecao](n_valores)

# 4. CONSTRUÇÃO DO GRÁFICO (REPRESENTAÇÃO GRÁFICA)
fig, ax = plt.subplots()

# Usamos 'scatter' (dispersão) em vez de 'plot' para enfatizar a natureza discreta
# No cálculo, os termos são pontos isolados, não uma curva contínua
ax.scatter(n_valores, x_n, color='blue', s=30, label=f"Termos $x_n$")

# Estética e Rigor: Linha de referência no zero para sequências convergentes
ax.axhline(0, color='black', linestyle='--', alpha=0.5)

# 5. LABELS QUE REFORÇAM A NOTAÇÃO MATEMÁTICA
ax.set_xlabel("Índice (n $\in \mathbb{N}$)")
ax.set_ylabel("Valor do Termo ($x_n$)")
ax.set_title(f"Visualização de {selecao}")
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()

# EXIBIÇÃO
st.pyplot(fig)

# 6. FEEDBACK NUMÉRICO
st.write(f"Último termo calculado: $x_{{{n_max}}} = {x_n[-1]:.4f}$")