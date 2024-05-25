import tkinter as tk
from tkinter import filedialog, messagebox
import sales_analysis as sa

class SalesAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Analysis App")

        self.label = tk.Label(root, text="Seleccione un archivo CSV de ventas:")
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="Cargar Archivo", command=self.load_file)
        self.button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            try:
                sales_data = sa.load_sales_data(file_path)
                monthly_sales = sa.calculate_monthly_sales(sales_data)
                sa.plot_monthly_sales(monthly_sales)
            except Exception as e:
                messagebox.showerror("Error", f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SalesAnalysisApp(root)
    root.mainloop()
