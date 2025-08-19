# Stock Portfolio Optimization (Python + yFinance)

## 📌 Project description
This project demonstrates how to build a simple investment portfolio model consisting of two stocks with the **lowest historical correlation of returns**. The project uses Warsaw Stock Exchange data (tickers in Yahoo Finance format: `CDR.WA`, `BLO.WA`, `11B.WA`).

The script:
- Downloads historical stock price data from **Yahoo Finance**.
- Calculates **returns, variance, standard deviation** and the **correlation matrix**.
- Selects the pair of stocks with the **lowest correlation**.
- Builds an investment portfolio with different asset weights.
- Determines the **efficient frontier (minimum variance portfolio)**.
- Visualizes the results (risk vs. return).

---

## 🛠️ Technologies
- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://matplotlib.org/)

---

## ▶️ How to run
1. Clone the repository:
   ```bash
   git clone https://github.com/Entariel/Two-asset-portfolio-project---Python-Pandas.git
   cd Two-asset-portfolio-project---Python-Pandas
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python portfolio.py
   ```

---

## 📊 Results
The script generates:
- **Portfolio chart** (curve of possible stock combinations and the minimum variance portfolio point).
- Information about **portfolio weights, risk, and expected return**:

Example console output:
```
Portfolio composition: CDR.WA - 0.42; BLO.WA - 0.58
Portfolio risk: 0.0184
Portfolio return: 0.0009
```

---

## 📌 Interpretation
- **Portfolio risk** = standard deviation of returns.
- **Portfolio return** = weighted average of stock returns.
- **Efficient frontier** shows the most optimal portfolio for selected assets.

---

# Optymalizacja portfela akcji (Python + yFinance)

## 📌 Opis projektu
Projekt demonstruje, w jaki sposób można zbudować prosty model portfela inwestycyjnego złożonego z dwóch spółek giełdowych o **najmniejszej korelacji historycznych stóp zwrotu**. W projekcie wykorzystano dane z GPW (tickery w formacie Yahoo Finance: `CDR.WA`, `BLO.WA`, `11B.WA`).

Skrypt:
- Pobiera dane historyczne notowań z **Yahoo Finance**.
- Oblicza **stopy zwrotu, wariancję, odchylenia standardowe** oraz **macierz korelacji**.
- Wybiera parę spółek o **najmniejszej korelacji**.
- Buduje portfel inwestycyjny z różnych wag aktywów.
- Wyznacza **granice efektywną (minimum variance portfolio)**.
- Wizualizuje wyniki na wykresie (ryzyko vs. stopa zwrotu).

---

## 🛠️ Technologie
- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://matplotlib.org/)

---

## ▶️ Uruchomienie
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/Entariel/Two-asset-portfolio-project---Python-Pandas.git
   cd Two-asset-portfolio-project---Python-Pandas
   ```

2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install -r requirements.txt
   ```

3. Uruchom skrypt:
   ```bash
   python portfolio.py
   ```

---

## 📊 Wyniki
Skrypt generuje:
- **Wykres portfela** (krzywa możliwych kombinacji spółek oraz punkt portfela o minimalnej wariancji).
- Informacje o **udziale spółek w portfelu, ryzyku oraz oczekiwanej stopie zwrotu**:

Przykład wyjścia w konsoli:
```
Udział spółek w portfelu: CDR.WA - 0.42; BLO.WA - 0.58
Ryzyko portfela wynosi: 0.0184
Stopa zwrotu z portfela wynosi: 0.0009
```

---

## 📌 Interpretacja
- **Ryzyko portfela** = odchylenie standardowe stóp zwrotu.
- **Stopa zwrotu portfela** = średnia ważona stóp zwrotu spółek.
- **Granica efektywna** wskazuje najbardziej optymalny portfel dla wybranych aktywów.

