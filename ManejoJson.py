import requests as rq
import json
import datetime as dt

def descargajson(url_webs, proyecto):
    commits = rq.get(url_webs)

    if commits.status_code == 200:
        info = commits.json()

        # Verificar la estructura de los datos
        for x in info:
            if 'days' not in x or 'total' not in x or 'week' not in x:
                print("El archivo JSON no es compatible con el tipo de estructura solicitada")
                return

        # Calcular el día de la semana con más commits
        dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        totalxdia = [sum(x['days'][y] for x in info) for y in range(7)]
        indice = totalxdia.index(max(totalxdia))

        # Calcular la semana con más commits
        mayor = max(info, key=lambda x: x['total'])
        semana = mayor['week']

        print(f"Proyecto {proyecto}")
        print("El día con más commits fue:", dias[indice])
        print("La semana con mayor número de commits fue:", dt.datetime.fromtimestamp(semana))
        print()

# URLs de los proyectos y llamadas a la función descargajson
url_proyectos = [
    ('https://api.github.com/repos/facebook/react/stats/commit_activity', 'React'),
    ('https://api.github.com/repos/d3/d3/stats/commit_activity', 'D3'),
    ('https://api.github.com/repos/tensorflow/tensorflow/stats/commit_activity', 'TensorFlow')
]

for url, proyecto in url_proyectos:
    descargajson(url, proyecto)
