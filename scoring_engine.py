"""
Script de Lead Scoring Engine
Procesa leads y calcula un score de 0-100 basado en perfil y comportamiento
para segmentar leads en Hot, Warm y Cold.
"""

import pandas as pd

# Cargar el dataset de leads
print("Cargando dataset de leads...")
df_leads = pd.read_csv('leads_mock_data.csv', encoding='utf-8-sig')

print(f"Total de leads cargados: {len(df_leads)}")

# ============================================================================
# LÓGICA DE SCORING - BUSINESS RULES
# ============================================================================

def calcular_score_perfil(cargo, tamaño_empresa, sector):
    """
    Calcula el Score de Perfil (máximo 50 puntos).
    
    Business Logic:
    - Cargo: Los C-Level tienen mayor poder de decisión y presupuesto, 
      por lo que se les asigna el mayor peso (20 pts). Los Directores 
      también tienen influencia significativa (15 pts). Managers tienen 
      influencia moderada (10 pts) y Juniors suelen ser investigadores 
      iniciales (5 pts).
    
    - Tamaño Empresa: Las empresas Enterprise tienen mayor capacidad 
      de compra y presupuesto (15 pts). Las Pymes son un mercado medio 
      con potencial (10 pts). Las Micro empresas tienen presupuestos 
      limitados (5 pts).
    
    - Sector: Tecnología y Finanzas son sectores con alta adopción 
      tecnológica y presupuestos para soluciones B2B (15 pts). Los demás 
      sectores tienen menor propensión histórica (5 pts).
    """
    score_perfil = 0
    
    # Scoring por Cargo
    # Identificamos el nivel de cargo basado en títulos comunes
    cargo_str = str(cargo).lower()
    
    if any(title in cargo_str for title in ['ceo', 'cto', 'cfo', 'cmo', 'coo', 'vp']):
        score_perfil += 20  # C-Level: Máximo poder de decisión
    elif 'director' in cargo_str:
        score_perfil += 15  # Director: Alta influencia en decisiones
    elif any(title in cargo_str for title in ['gerente', 'manager']):
        score_perfil += 10  # Manager: Influencia moderada
    else:
        score_perfil += 5   # Junior: Rol investigativo, menor poder decisión
    
    # Scoring por Tamaño de Empresa
    if tamaño_empresa == 'Enterprise':
        score_perfil += 15  # Mayor presupuesto y capacidad de compra
    elif tamaño_empresa == 'Pyme':
        score_perfil += 10  # Mercado medio con potencial
    else:  # Micro
        score_perfil += 5   # Presupuesto limitado
    
    # Scoring por Sector
    if sector in ['Tecnología', 'Finanzas']:
        score_perfil += 15  # Alta adopción tecnológica y presupuesto B2B
    else:
        score_perfil += 5   # Menor propensión histórica a compras B2B
    
    return min(score_perfil, 50)  # Cap máximo de 50 puntos


def calcular_score_comportamiento(pidio_demo, descargo_whitepaper, visitas_web, emails_abiertos):
    """
    Calcula el Score de Comportamiento (máximo 50 puntos).
    
    Business Logic:
    - Pidio Demo: Es la señal más fuerte de intención de compra. Un lead 
      que solicita demo está en etapa avanzada del funnel (40 pts). Esta 
      es la acción más valiosa porque requiere compromiso del prospecto.
    
    - Descargo Whitepaper: Indica interés en aprender más sobre la solución 
      y es una señal de engagement temprano (10 pts). Es menos fuerte que 
      una demo pero muestra intención.
    
    - Visitas Web: Múltiples visitas indican interés recurrente. Se otorga 
      1 punto por visita hasta máximo 10 pts para evitar sobreponderar 
      tráfico casual.
    
    - Emails Abiertos: Indica que el lead está leyendo nuestras comunicaciones. 
      1 punto por email abierto hasta máximo 10 pts. Muestra engagement 
      con el contenido.
    
    Nota: El máximo de 50 puntos asegura que ningún lead pueda alcanzar 
    un score perfecto solo con comportamiento, incentivando la combinación 
    de perfil + comportamiento.
    """
    score_comportamiento = 0
    
    # Señal crítica: Pedido de Demo
    if pidio_demo:
        score_comportamiento += 40  # Mayor señal de intención de compra
    
    # Engagement con contenido
    if descargo_whitepaper:
        score_comportamiento += 10  # Interés en aprender más
    
    # Visitas web (máximo 10 puntos)
    score_comportamiento += min(visitas_web, 10)  # 1 punto por visita, cap en 10
    
    # Emails abiertos (máximo 10 puntos)
    score_comportamiento += min(emails_abiertos, 10)  # 1 punto por email, cap en 10
    
    return min(score_comportamiento, 50)  # Cap máximo de 50 puntos


def asignar_segmento(score_total):
    """
    Asigna segmento basado en el score total.
    
    Business Logic:
    - Hot Lead (>=70): Leads con alta probabilidad de conversión. 
      Combinan perfil de alto valor con comportamiento activo. Requieren 
      seguimiento prioritario y asignación a mejores vendedores.
    
    - Warm Lead (40-69): Leads con potencial pero necesitan más nurturing. 
      Pueden convertirse con el seguimiento adecuado. Requieren campañas 
      de marketing automatizadas y seguimiento regular.
    
    - Cold Lead (<40): Leads con bajo engagement o perfil de menor valor. 
      Requieren estrategias de reactivación o pueden ser priorizados más 
      bajo en la cola de seguimiento.
    """
    if score_total >= 70:
        return 'Hot Lead'
    elif score_total >= 40:
        return 'Warm Lead'
    else:
        return 'Cold Lead'


# ============================================================================
# APLICAR SCORING A TODOS LOS LEADS
# ============================================================================

print("\nCalculando scores para cada lead...")

# Calcular Score de Perfil
df_leads['score_perfil'] = df_leads.apply(
    lambda row: calcular_score_perfil(
        row['cargo'], 
        row['tamaño_empresa'], 
        row['sector']
    ), 
    axis=1
)

# Calcular Score de Comportamiento
df_leads['score_comportamiento'] = df_leads.apply(
    lambda row: calcular_score_comportamiento(
        row['pidio_demo'],
        row['descargo_whitepaper'],
        row['visitas_web'],
        row['emails_abiertos']
    ),
    axis=1
)

# Calcular Score Total
df_leads['lead_score'] = df_leads['score_perfil'] + df_leads['score_comportamiento']

# Asignar Segmento
df_leads['segmento'] = df_leads['lead_score'].apply(asignar_segmento)

# ============================================================================
# GUARDAR RESULTADOS
# ============================================================================

output_file = 'scored_leads_final.csv'
df_leads.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"\n[OK] Dataset con scores guardado en: {output_file}")

# ============================================================================
# RESUMEN Y ESTADÍSTICAS
# ============================================================================

print("\n" + "="*60)
print("RESUMEN DE LEAD SCORING")
print("="*60)

# Contar leads por segmento
hot_leads = len(df_leads[df_leads['segmento'] == 'Hot Lead'])
warm_leads = len(df_leads[df_leads['segmento'] == 'Warm Lead'])
cold_leads = len(df_leads[df_leads['segmento'] == 'Cold Lead'])

print(f"\n[INFO] Distribucion por Segmento:")
print(f"   - Hot Leads:  {hot_leads:3d} ({hot_leads/len(df_leads)*100:.1f}%)")
print(f"   - Warm Leads: {warm_leads:3d} ({warm_leads/len(df_leads)*100:.1f}%)")
print(f"   - Cold Leads: {cold_leads:3d} ({cold_leads/len(df_leads)*100:.1f}%)")

# Score promedio de leads convertidos
leads_convertidos = df_leads[df_leads['status_final'] == 'Convertido']
if len(leads_convertidos) > 0:
    score_promedio_convertidos = leads_convertidos['lead_score'].mean()
    print(f"\n[OK] Score Promedio de Leads Convertidos: {score_promedio_convertidos:.2f} puntos")
    print(f"   Total de Convertidos: {len(leads_convertidos)}")
    
    # Distribución de convertidos por segmento
    convertidos_hot = len(leads_convertidos[leads_convertidos['segmento'] == 'Hot Lead'])
    convertidos_warm = len(leads_convertidos[leads_convertidos['segmento'] == 'Warm Lead'])
    convertidos_cold = len(leads_convertidos[leads_convertidos['segmento'] == 'Cold Lead'])
    
    print(f"\n[INFO] Convertidos por Segmento:")
    print(f"   - Hot Leads convertidos:  {convertidos_hot:3d} ({convertidos_hot/hot_leads*100:.1f}% de Hot Leads)" if hot_leads > 0 else "   - Hot Leads convertidos:  0")
    print(f"   - Warm Leads convertidos: {convertidos_warm:3d} ({convertidos_warm/warm_leads*100:.1f}% de Warm Leads)" if warm_leads > 0 else "   - Warm Leads convertidos: 0")
    print(f"   - Cold Leads convertidos: {convertidos_cold:3d} ({convertidos_cold/cold_leads*100:.1f}% de Cold Leads)" if cold_leads > 0 else "   - Cold Leads convertidos: 0")
else:
    print("\n[WARNING] No se encontraron leads convertidos en el dataset")

# Estadísticas adicionales
print(f"\n[INFO] Estadisticas Generales:")
print(f"   - Score Promedio Total: {df_leads['lead_score'].mean():.2f} puntos")
print(f"   - Score Minimo: {df_leads['lead_score'].min():.2f} puntos")
print(f"   - Score Maximo: {df_leads['lead_score'].max():.2f} puntos")
print(f"   - Score Mediano: {df_leads['lead_score'].median():.2f} puntos")

print("\n" + "="*60)
print("Procesamiento completado exitosamente!")
print("="*60)

