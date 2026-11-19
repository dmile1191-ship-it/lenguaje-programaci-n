# =====================================================================
# mi_portafolio.py · LA FICHA DE TU PORTAFOLIO
# =====================================================================

# ---------- 1. Identificación ----------------------------------------
nombre_portafolio = "Portafolio Multi-Sectorial Global"
integrantes = "Deisy Milena Garro Rueda · Yovani Caez"

# ---------- 2. Composición (igual que en el taller) ------------------
activos = ["MSFT", "JPM", "JNJ", "PG", "XOM"]

info_activos = {
    "MSFT": ("Microsoft", "Tecnología"),
    "JPM":  ("JPMorgan Chase", "Financiero"),
    "XOM":  ("ExxonMobil", "Energía"),
    "JNJ":  ("Johnson & Johnson", "Salud"),
    "PG":   ("Procter & Gamble", "Consumo Básico")
}

# Pesos en el MISMO orden de `activos`. Deben sumar 1.
pesos = [0.25, 0.20, 0.20, 0.20, 0.15]

benchmark = "SPY"
fecha_inicio = "2022-01-01"
fecha_fin = "2025-01-01"
monto_inicial = 10_000
tasa_libre_riesgo = 0.045    # 4.5% anual de referencia usado en tu taller

# ---------- 3. Mensaje para el inversionista (sección 13 del taller) --
justificacion = (
    "Se seleccionaron 5 empresas líderes en sectores clave y poco correlacionados "
    "(Tecnología, Financiero, Salud, Consumo Básico y Energía) para equilibrar "
    "crecimiento y estabilidad defensiva frente a la volatilidad del mercado."
)

resumen_ejecutivo = (
    "Este portafolio multi-sectorial global (MSFT, JPM, JNJ, PG, XOM) logró un "
    "rendimiento total de 36.20% (10.35% anualizado) entre 2022 y 2024, superando "
    "al benchmark SPY (28.19% / 8.32%). Presenta un perfil de riesgo defensivo con "
    "volatilidad reducida de 14.19% y máxima caída de -15.26%, logrando un Sharpe de 0.41."
)

hallazgos = [
    "Rendimiento: El portafolio creció hasta $13,620.14 USD desde $10,000 USD iniciales, superando los $12,819.41 USD del SPY.",
    "Riesgo y diversificación: Con una correlación promedio baja de 0.22, la volatilidad del portafolio (14.19%) fue 38% menor al promedio de sus activos individuales (22.76%).",
    "Eventos extremos: La máxima caída histórica fue de -15.26% (vs. -24.50% del SPY) y el VaR histórico diario al 95% se situó en -1.40% ($189.98 USD)."
]

riesgos = (
    "Principales riesgos: exposición sectorial, volatilidad macroeconómica global y "
    "presencia de colas pesadas (exceso de curtosis de 1.89), lo que implica caídas "
    "extremas más frecuentes de lo que predice la distribución normal."
)

limitaciones = (
    "Limitaciones: análisis basado en un periodo histórico específico (2022-2025), "
    "rendimientos pasados no garantizan resultados futuros, asume rebalanceo diario ideal "
    "y no contempla costos de transacción, comisiones ni impacto de tipo de cambio."
)

perfil_inversionista = "Moderado"
