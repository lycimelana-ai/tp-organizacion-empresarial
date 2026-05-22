
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Convertir fecha
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Ventas totales
ventas_totales = df["sales_amount"].sum()

# Crear columna mes
df["mes"] = df["sales_date"].dt.to_period("M")

# Ventas por mes
ventas_mes = df.groupby("mes")["sales_amount"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)

print("\nVentas por mes:")
print(ventas_mes)

# Crear gráfico
ventas_mes.plot(kind="line")

plt.title("Evolución de ventas")
plt.xlabel("Mes")
plt.ylabel("Ventas")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("\nGráfico guardado en resultados/")
