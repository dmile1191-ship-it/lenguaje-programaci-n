# Portafolio Multi-Sectorial Global

Dashboard para inversionistas construido con Python y Streamlit
(curso Lenguajes de Programación · Ingeniería Financiera · ITM).

**Integrantes:** Deisy Milena Garro Rueda · Yovani Caez

## Portafolio
Activos: MSFT, JPM, JNJ, PG, XOM · Benchmark: SPY · Período: 2022-01-01 a 2025-01-01

## Ejecución local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Fuente de datos
Yahoo Finance mediante yfinance. Si la descarga falla, la app usa `precios_respaldo.csv` y lo indica en pantalla.

> Rendimientos pasados no garantizan rendimientos futuros. Uso académico; no es una recomendación de inversión.
