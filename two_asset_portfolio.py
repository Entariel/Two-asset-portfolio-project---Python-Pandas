import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

## Pobieramy notowania dla 3 spółek gieldowych (interwał dzienny)
tickers = ['CDR.WA', 'BLO.WA', '11B.WA']
df = yf.download(tickers, start='2015-08-16', end='2025-08-15')

## Obliczmy stopę zwrotu
returns = df['Close'].pct_change().dropna()

## Obliczamy srednią stopę zwrotu, wariancję i odchylenie standardowe dla spółek
mean_returns = returns.mean()
variance = returns.var()
std_dev = returns.std()

## Obliczamy macież korelacji
correlation = returns.corr()

## Wybieramy spółki o najmniejszej korelacji
stacked = correlation.stack()
min_pair = stacked.idxmin()

## Wyznaczamy średnie stopy zwrotu, odchylenia standardowe i korelacje 
## dla wybranych dwóch spółek 
r1 = float(mean_returns[min_pair[0]])
r2 = float(mean_returns[min_pair[1]])
sigma1 = float(std_dev[min_pair[0]])
sigma2 = float(std_dev[min_pair[1]])
cor_pair = stacked.min()

## Tworzymy zakres wagi udziału jednego aktywa w portfelu
w = np.linspace(0, 1, 200)

## Obliczamy stopy zwrotu z portfela
r_p = w * r1 + (1 - w) * r2

## Obliczamy odchylenia standardowe stóp zwrotu z portfela (ryzyko)
sigma_p = np.sqrt((w**2)*(sigma1**2) + ((1-w)**2)*(sigma2**2) + 2*w*(1-w)*cor_pair*sigma1*sigma2)

## Wyznaczamy granice efektywną dla tego portfela
w_mv = (sigma2**2 - cor_pair*sigma1*sigma2) / (sigma1**2 + sigma2**2 - 2*cor_pair*sigma1*sigma2)
w_mv2 = 1 - w_mv
r_mv = w_mv*r1 + w_mv2*r2
sigma_mv = float(np.sqrt((w_mv**2)*sigma1**2 + (w_mv2**2)*sigma2**2 + 2*w_mv*w_mv2*cor_pair*sigma1*sigma2))

## Wykres możliwych portfeli z granicą efektywną
plt.plot(sigma_p, r_p, label=f"{min_pair[0]} & {min_pair[1]}")
plt.scatter(sigma_mv, r_mv, color='Orange', label='Granica efektywna', zorder=5)
plt.xlabel('Ryzyko')
plt.ylabel('Stopy zwrotu')
plt.title('Portfel akcji')
plt.legend()
plt.show()

## Drukujemy do konsoli wagi akcji w portfelu oraz jego ryzyko i stopę zwrotu
print()
print(f'Udział spółek w portfelu: {min_pair[0]} - {w_mv:.2f}; {min_pair[1]} - {w_mv2:.2f}' )
print(f'Ryzyko porfela wynosi: {sigma_mv:.4f}')
print(f'Stopa zwrotu z portfela wynosi: {r_mv:.4f}')
