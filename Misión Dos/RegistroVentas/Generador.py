import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sales_data(start_date, end_date, output_file):
    """
    Genera datos de ventas diarias y los guarda en un archivo CSV.

    :param start_date: Fecha de inicio (YYYY-MM-DD)
    :param end_date: Fecha de fin (YYYY-MM-DD)
    :param output_file: Nombre del archivo CSV de salida
    """
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    sales = [random.randint(100, 3000) for _ in range(len(dates))]
    
    sales_data = pd.DataFrame({
        'Date': dates,
        'Sales': sales
    })
    
    sales_data.to_csv(output_file, index=False)
    print(f"Datos de ventas generados y guardados en {output_file}")

# Configurar las fechas de inicio y fin para los datos simulados
# formato de fecha ISO 8601
start_date = '2023-01-01'
end_date = '2023-12-31'
output_file = 'D:\Shadow\GitHub\Curso-Explorador\Misión Dos\RegistroVentas\sales_data.csv'

# Generar los datos de ventas
generate_sales_data(start_date, end_date, output_file)
