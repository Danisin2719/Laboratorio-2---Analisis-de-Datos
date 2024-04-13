import requests
import json
from datetime import datetime

def descargajson(url):
    # Hacer la solicitud GET
    response = requests.get(url)
    
    # Verificar si la petición fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido JSON
        data = response.json()
        
        # Verificar la estructura de las entradas
        if "days" in data and "total" in data and "week" in data:
            # Analizar los datos
            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            max_commits_dia = max(range(len(data["days"])), key=lambda x: data["days"][x])
            dia_max_commits = dias_semana[max_commits_dia]
            
            max_commits_semana = max(data["week"], key=lambda x: x[1])
            semana_max_commits = datetime.fromtimestamp(max_commits_semana[0]).strftime("%Y-%m-%d")
            
            return dia_max_commits, semana_max_commits
        else:
            print("La estructura de los datos no coincide con la esperada.")
            return None, None
    else:
        print(f"Error al hacer la solicitud: {response.status_code}")
        return None, None

# Ejemplos de uso
repos = [
    ("Node.js", "https://api.github.com/repos/nodejs/node/stats/commit_activity"),
    ("React.js", "https://api.github.com/repos/facebook/react/stats/commit_activity"),
    ("Angular", "https://api.github.com/repos/angular/angular/stats/commit_activity")
]

# Modifica el bucle for para imprimir los datos devueltos por la API
for repo_name, repo_url in repos:
    print(f"Repositorio: {repo_name}")
    data = requests.get(repo_url).json()
    print(data)
    print()

