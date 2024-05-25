import pandas as pd
import matplotlib.pyplot as plt

def load_sales_data(file_path):
    """Carga datos de ventas desde un archivo CSV."""
    return pd.read_csv(file_path)
"""La función pd.to_datetime se encarga de la conversión, 
asegurando que cualquier formato de fecha en la columna Date se interprete 
correctamente como un objeto de fecha y hora.
"""
def calculate_monthly_sales(data):
    """Calcula las ventas mensuales agregadas."""
    data['Date'] = pd.to_datetime(data['Date'])
    monthly_sales = data.resample('M', on='Date').sum()
    return monthly_sales

def plot_monthly_sales(monthly_sales):
    """Genera un gráfico de las ventas mensuales."""
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales.index, monthly_sales['Sales'], marker='o')
    plt.title('Monthly Sales Analysis')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()
