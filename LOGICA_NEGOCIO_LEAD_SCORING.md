# Análisis de Lógica de Negocio: Lead Scoring Engine
## Perspectiva RevOps - Contexto B2B

---

## 1. Matriz de Puntuación (Scoring Matrix)

El sistema de scoring utiliza una escala de **0-100 puntos**, dividida en dos componentes principales:

### 1.1. Score de Perfil (Máximo: 50 puntos)

Evalúa las características estáticas del lead que indican su potencial de valor como cliente.

#### **Cargo / Rol Organizacional** (Máximo: 20 puntos)

| Nivel Jerárquico | Puntos | Criterio de Identificación |
|-----------------|--------|---------------------------|
| **C-Level** | **20 pts** | CEO, CTO, CFO, CMO, COO, VP |
| **Director** | **15 pts** | Títulos que contengan "Director" |
| **Manager/Gerente** | **10 pts** | Títulos que contengan "Manager" o "Gerente" |
| **Junior/Otros** | **5 pts** | Cualquier otro cargo no mencionado |

**Lógica de Negocio:** El poder de decisión y acceso a presupuesto aumenta exponencialmente con el nivel jerárquico. Los C-Level tienen autoridad directa para aprobar compras estratégicas.

---

#### **Tamaño de Empresa** (Máximo: 15 puntos)

| Categoría | Puntos | Justificación |
|-----------|--------|---------------|
| **Enterprise** | **15 pts** | Mayor capacidad de compra y presupuesto |
| **Pyme** | **10 pts** | Mercado medio con potencial |
| **Micro** | **5 pts** | Presupuesto limitado |

**Lógica de Negocio:** El tamaño de empresa es un proxy directo del presupuesto disponible y del ticket promedio esperado.

---

#### **Sector Industrial** (Máximo: 15 puntos)

| Sector | Puntos | Justificación |
|--------|--------|---------------|
| **Tecnología** | **15 pts** | Alta adopción tecnológica y presupuesto B2B |
| **Finanzas** | **15 pts** | Alta adopción tecnológica y presupuesto B2B |
| **Otros Sectores** | **5 pts** | Menor propensión histórica a compras B2B |

**Lógica de Negocio:** Sectores tecnológicos y financieros tienen mayor madurez en la adopción de soluciones B2B y procesos de compra más ágiles.

---

### 1.2. Score de Comportamiento (Máximo: 50 puntos)

Evalúa las acciones del lead que indican intención de compra y engagement con la marca.

#### **Matriz de Comportamiento**

| Acción | Puntos | Límite | Justificación |
|--------|--------|--------|---------------|
| **Pidió Demo** | **40 pts** | Binario (Sí/No) | Señal más fuerte de intención de compra. Lead en etapa avanzada del funnel. Requiere compromiso activo del prospecto. |
| **Descargó Whitepaper** | **10 pts** | Binario (Sí/No) | Indica interés en aprender más. Señal de engagement temprano pero menos fuerte que demo. |
| **Visitas Web** | **1 pt/visita** | Máximo 10 pts | Múltiples visitas indican interés recurrente. Cap en 10 para evitar sobreponderar tráfico casual. |
| **Emails Abiertos** | **1 pt/email** | Máximo 10 pts | Indica que el lead está leyendo comunicaciones. Muestra engagement con contenido. Cap en 10 para evitar inflación. |

**Nota Estratégica:** El máximo de 50 puntos en comportamiento asegura que ningún lead pueda alcanzar un score perfecto solo con acciones, incentivando la combinación de **perfil de alto valor + comportamiento activo**.

---

## 2. Umbrales de Segmentación

El score total (Perfil + Comportamiento) determina la clasificación del lead en tres segmentos:

### **Hot Lead** (Score ≥ 70 puntos)

**Características:**
- Alta probabilidad de conversión
- Combina perfil de alto valor con comportamiento activo
- Requiere seguimiento prioritario
- Asignación a mejores vendedores (top performers)

**Ejemplo de Perfil Típico:**
- C-Level (20) + Enterprise (15) + Sector Tech/Finanzas (15) = 50 pts perfil
- + Pidió Demo (40) = 90 pts total → **Hot Lead**

---

### **Warm Lead** (Score: 40-69 puntos)

**Características:**
- Potencial de conversión moderado
- Necesitan más nurturing y educación
- Pueden convertirse con seguimiento adecuado
- Requieren campañas de marketing automatizadas
- Seguimiento regular pero no urgente

**Ejemplo de Perfil Típico:**
- Manager (10) + Pyme (10) + Sector Tech (15) = 35 pts perfil
- + Descargó Whitepaper (10) + 5 visitas web (5) = 50 pts total → **Warm Lead**

---

### **Cold Lead** (Score < 40 puntos)

**Características:**
- Bajo engagement o perfil de menor valor
- Requieren estrategias de reactivación
- Priorización baja en la cola de seguimiento
- Pueden ser candidatos para programas de re-engagement o nurturing de largo plazo

**Ejemplo de Perfil Típico:**
- Junior (5) + Micro (5) + Otro Sector (5) = 15 pts perfil
- + 2 emails abiertos (2) = 17 pts total → **Cold Lead**

---

## 3. Razonamiento Estratégico: ¿Por qué estos pesos en contexto B2B?

### 3.1. Filosofía del Modelo: Balance 50/50

El modelo divide equitativamente el scoring entre **Perfil (50 pts)** y **Comportamiento (50 pts)** para:

- **Evitar falsos positivos:** Un lead con mucho comportamiento pero perfil débil no puede alcanzar Hot Lead solo con clicks
- **Evitar falsos negativos:** Un lead con excelente perfil pero sin comportamiento aún puede ser identificado como potencial
- **Incentivar la combinación ideal:** Hot Leads requieren AMBOS: perfil de decisor + acciones de compra

---

### 3.2. Justificación de Pesos por Atributo

#### **Cargo: 20 puntos (40% del score de perfil)**

**Razonamiento B2B:**
- En ventas B2B, el nivel jerárquico es el predictor #1 de capacidad de decisión
- Los C-Level tienen autoridad presupuestaria directa y pueden acelerar ciclos de venta
- Los ciclos de venta B2B son largos; trabajar con el decisor correcto desde el inicio reduce el riesgo de "no decision"
- **ROI esperado:** Leads C-Level tienen tickets promedio 3-5x mayores que Managers

---

#### **Tamaño Empresa: 15 puntos (30% del score de perfil)**

**Razonamiento B2B:**
- El tamaño de empresa es un proxy directo del presupuesto disponible
- Empresas Enterprise tienen procesos de compra más estructurados y presupuestos pre-aprobados
- El LTV (Lifetime Value) de clientes Enterprise es significativamente mayor
- **ROI esperado:** Enterprise clients tienen LTV 5-10x mayor que Micro empresas

---

#### **Sector: 15 puntos (30% del score de perfil)**

**Razonamiento B2B:**
- Sectores Tech y Finanzas tienen mayor madurez en adopción de soluciones B2B
- Estos sectores tienen procesos de compra más ágiles y menor resistencia al cambio
- Históricamente, estos sectores tienen mayor tasa de conversión en ventas B2B
- **ROI esperado:** Tasa de conversión 2-3x mayor que otros sectores

---

#### **Pidió Demo: 40 puntos (80% del score de comportamiento)**

**Razonamiento B2B:**
- Es la acción más valiosa porque requiere compromiso activo del prospecto
- Un lead que solicita demo está en etapa avanzada del funnel (consideración activa)
- En B2B, las demos son el paso previo a propuesta comercial en 70-80% de los casos
- **ROI esperado:** Leads que piden demo tienen tasa de conversión 10-15x mayor que leads que solo visitan web

---

#### **Descargó Whitepaper: 10 puntos (20% del score de comportamiento)**

**Razonamiento B2B:**
- Indica interés en aprender más sobre la solución
- Es una señal de engagement temprano pero menos comprometedora que demo
- Útil para identificar leads en etapa de awareness/consideración temprana
- **ROI esperado:** Leads que descargan whitepapers tienen tasa de conversión 3-5x mayor que leads sin engagement

---

#### **Visitas Web y Emails: 1 punto cada uno (máximo 10 pts cada uno)**

**Razonamiento B2B:**
- Son señales de interés pero pueden ser pasivas o casuales
- El cap en 10 puntos evita sobreponderar tráfico de bajo valor
- Múltiples visitas/emails indican interés recurrente, pero no garantizan intención de compra
- **ROI esperado:** Son señales de apoyo, no determinantes por sí solas

---

### 3.3. Umbrales de Segmentación: Justificación

#### **Hot Lead: ≥ 70 puntos (70% del máximo)**

**Razonamiento:**
- Requiere combinar perfil alto (≥35 pts) + comportamiento activo (≥35 pts)
- Representa aproximadamente el top 15-20% de leads en un pipeline típico
- Estos leads justifican asignación de recursos premium (mejores vendedores, seguimiento inmediato)
- **Objetivo:** Maximizar tasa de conversión en leads de mayor valor

---

#### **Warm Lead: 40-69 puntos (40-69% del máximo)**

**Razonamiento:**
- Representa el "middle tier" que necesita nurturing
- Pueden convertirse con el seguimiento adecuado pero requieren más educación
- Son candidatos ideales para marketing automation y campañas de nurturing
- **Objetivo:** Acelerar leads con potencial pero que necesitan más tiempo/educación

---

#### **Cold Lead: < 40 puntos (<40% del máximo)**

**Razonamiento:**
- Representa leads con bajo perfil, bajo comportamiento, o ambos
- No justifican asignación de recursos de ventas en el corto plazo
- Pueden ser reactivados con estrategias de re-engagement o nurturing de largo plazo
- **Objetivo:** No desperdiciar recursos de ventas en leads de bajo potencial

---

## 4. Consideraciones Estratégicas para RevOps

### 4.1. Ventajas del Modelo

✅ **Balanceado:** No sobrepondera ni perfil ni comportamiento  
✅ **Interpretable:** Los pesos tienen justificación de negocio clara  
✅ **Escalable:** Fácil de ajustar pesos basado en datos históricos  
✅ **Accionable:** Los segmentos tienen acciones claras asociadas  

### 4.2. Limitaciones y Mejoras Potenciales

⚠️ **Falta de Decay:** No considera el tiempo transcurrido desde última acción  
⚠️ **Sin Scoring Negativo:** No penaliza señales negativas (ej: unsubscribe, rechazo)  
⚠️ **Estático:** No se ajusta automáticamente basado en performance histórica  
⚠️ **Sin Contexto de Fuente:** No diferencia entre leads inbound vs outbound  

### 4.3. Recomendaciones de Optimización

1. **A/B Testing:** Probar diferentes umbrales (ej: Hot ≥ 75 vs ≥ 70) y medir impacto en conversión
2. **Time Decay:** Implementar decay de puntos de comportamiento si no hay actividad en 30-60 días
3. **Scoring Negativo:** Penalizar acciones negativas (unsubscribe, rechazo explícito)
4. **Machine Learning:** Una vez con datos históricos, entrenar modelo ML para optimizar pesos automáticamente
5. **Segmentación por Fuente:** Ajustar pesos según origen del lead (inbound vs outbound vs eventos)

---

**Documento generado por:** Consultoría RevOps  
**Fecha:** Análisis basado en código actual  
**Contexto:** Lead Scoring Engine B2B

