# -------------------------------
# Sección 1: Imports y Carga de Datos
# -------------------------------
import pandas as pd

# URL del archivo CSV en GitHub (raw)
url = "https://raw.githubusercontent.com/daobaa/M14Datasets/master/mxmh_survey_results.csv"

# Leer el archivo CSV desde la URL
df = pd.read_csv(url)