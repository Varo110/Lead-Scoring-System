# 🎯 B2B Intelligent Lead Scoring System

### 🔗 [VER DEMO INTERACTIVA (Dashboard)](https://dashboard-lead-scoring.lovable.app)
*Nota: Subir en el dashboard interactivo el documento de scored_leads_final.csv para ver métricas.

---

## 💼 Resumen del Proyecto
Sistema diseñado para optimizar el tiempo de los equipos de ventas B2B. Utiliza un algoritmo de puntuación basado en datos para identificar qué leads tienen mayor probabilidad de compra, aumentando el **Revenue por Hora Comercial**.

## 🛠️ La Solución Técnica
He desarrollado un sistema *End-to-End* que simula, procesa y visualiza oportunidades de venta:

1.  **Data Engineering (Python):** Generación de datasets sintéticos estocásticos (librería `Faker`) simulando distribuciones reales del mercado B2B.
2.  **Scoring Engine (Python + Pandas):** Algoritmo de clasificación basado en reglas de negocio (Matriz de 100 puntos) que segmenta leads en Hot, Warm y Cold.
3.  **Frontend (React + Tailwind):** Dashboard interactivo desplegado en la nube para visualización en tiempo real por parte del equipo comercial.

## 🧠 Lógica de Puntuación (Business Logic)

El modelo se basa en una ponderación 50/50 entre perfil demográfico y comportamiento digital:

| Criterio | Peso Máximo | Racional de Negocio |
|----------|-------------|---------------------|
| **Cargo** | 20 pts | Los C-Level deciden presupuesto. Managers solo influyen. |
| **Intención**| 40 pts | Solicitar Demo es la señal de compra más fuerte (High Intent). |
| **Sector** | 15 pts | Prioridad a sectores Tech/Finanzas por ciclo de venta corto. |

*Para ver el desglose completo de la lógica, consulta la documentación en `/docs/LOGICA_NEGOCIO.md`.*

## 🚀 Cómo ejecutar este proyecto localmente

```bash
# 1. Clonar repositorio
git clone [https://github.com/tu-usuario/lead-scoring.git](https://github.com/tu-usuario/lead-scoring.git)

# 2. Instalar dependencias
pip install pandas faker

# 3. Ejecutar motor
python src/scoring_engine.py
---
*Proyecto creado por Álvaro Pérez.*
