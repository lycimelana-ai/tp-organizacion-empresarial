# -*- coding: utf-8 -*-
"""
Cátedra: Organización Empresarial - UTN
Script de Análisis de Ventas de una Pequeña Empresa (Escenario B)
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def ejecutar_analisis():
    # 1. Definición de rutas relativas según la estructura obligatoria de la rúbrica
    ruta_datos = os.path.join('datos', 'dataset.csv')
    ruta_resultados = 'resultados'
    os.makedirs(ruta_resultados, exist_ok=True)
    
    # Cargar los datos descargados
    df = pd.read_csv(ruta_datos)
    
    # Limpieza de nombres de columnas por si tienen espacios ocultos
    df.columns = df.columns.str.strip()
    
    # Formatear la columna de fechas y agrupar por periodo mensual
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    df['mes'] = df['sales_date'].dt.to_period('M')
    
    # 2. Procesamiento Matemático e Indicadores Requeridos
    ventas_totales = df['sales_amount'].sum()
    ventas_por_mes = df.groupby('mes')['sales_amount'].sum()
    
    print("=== RESULTADOS DEL ANÁLISIS DE VENTAS (CÉLULA ÁGIL) ===")
    print(f"Monto de Ventas Totales: ${ventas_totales:,.2f}")
    
    # Si el archivo CSV tiene columna de productos individuales, calcula el más vendido
    if 'product' in df.columns:
        prod_mas_vendido = df.groupby('product')['quantity'].sum().idxmax()
        cant_prod = df.groupby('product')['quantity'].sum().max()
        print(f"Producto Estrella (Más vendido): {prod_mas_vendido} ({cant_prod} unidades)")
    elif 'producto' in df.columns:
        prod_mas_vendido = df.groupby('producto')['cantidad_vendida'].sum().idxmax()
        cant_prod = df.groupby('producto')['cantidad_vendida'].sum().max()
        print(f"Producto Estrella (Más vendido): {prod_mas_vendido} ({cant_prod} unidades)")
        
    print("\nEvolución de Ventas por Mes:")
    print(ventas_por_mes.to_string())
    
    # 3. Generación y Exportación del Gráfico Temporal (Criterio de Reproducibilidad)
    plt.figure(figsize=(10, 5))
    ventas_por_mes.plot(kind='line', marker='o', color='darkblue', linewidth=2, markersize=6)
    plt.title('Evolución Temporal de Ventas Mensuales', fontsize=14, fontweight='bold')
    plt.xlabel('Periodo Mensual', fontsize=12)
    plt.ylabel('Monto Total Facturado ($)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    # Guardar en la carpeta de resultados para el informe final
    ruta_grafico = os.path.join(ruta_resultados, 'grafico_resultados.png')
    plt.savefig(ruta_grafico)
    plt.close()
    print(f"\n¡Proceso Exitoso! Gráfico estadístico exportado en: {ruta_grafico}")

if __name__ == '__main__':
    ejecutar_analisis()
