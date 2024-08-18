import pandas as pd

def load_and_label_csv(filename, label):
    data = pd.read_csv(filename)
    data['label'] = label
    return data

# Cargar y etiquetar los datos
circulo_data = load_and_label_csv('datos_circulo.csv', 'circulo')
cuadrado_data = load_and_label_csv('datos_cuadrado.csv', 'cuadrado')
reposo_data = load_and_label_csv('datos_reposo.csv', 'reposo')
signo_data = load_and_label_csv('datos_signo.csv', 'signo')
linea_data = load_and_label_csv('datos_linea.csv', 'linea')
hechizo1_data = load_and_label_csv('datos_hechizo1.csv', 'hechizo1')
#hechizo2_data = load_and_label_csv('datos_hechizo2.csv', 'hechizo2')
ele_data = load_and_label_csv('datos_ele.csv', 'ele')


# Unir todos los datasets
#all_data = pd.concat([circulo_data, cuadrado_data, triangulo_data, garabato_data], ignore_index=True)

all_data = pd.concat([circulo_data, cuadrado_data,reposo_data,linea_data,hechizo1_data,signo_data,ele_data], ignore_index=True)

# Guardar el dataset unificado
all_data.to_csv('figuras.csv', index=False)
