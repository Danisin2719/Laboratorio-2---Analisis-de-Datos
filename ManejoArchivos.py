import csv

# Inicializar variables
sum_ratings = 0
num_rated_dresses = 0
recommended_dress_ids = []
animal_pattern_count = 0
sexy_summer_dresses = []
price_dict = {"Low": [], "High": [], "Average": [], "Medium": []}

# Abrir el archivo CSV
with open('Dresses.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterar sobre cada fila del archivo CSV
    for row in reader:
        # a. Obtener todos los vestidos con una puntuación > 0 y calcular el promedio
        rating = float(row['Rating'])
        if rating > 0:
            sum_ratings += rating
            num_rated_dresses += 1
        
        # b. Obtener el Dress_ID recomendado y contar los vestidos con patrón de animales
        recommendation = int(row['Recommendation'])
        if recommendation == 1:
            recommended_dress_ids.append(row['Dress_ID'])
        elif recommendation == 0 and row['Pattern Type'] == 'animal':
            animal_pattern_count += 1
        
        # c. Obtener los vestidos de verano con estilo "sexy"
        if row['Season'] == 'Summer' and row['Style'] == 'Sexy':
            sexy_summer_dresses.append(row)
        
        # d. Crear el diccionario de Dress_ID por precio
        price = row['Price']
        dress_id = row['Dress_ID']
        if price == 'Low':
            price_dict['Low'].append(dress_id)
        elif price == 'High':
            price_dict['High'].append(dress_id)
        elif price == 'Average':
            price_dict['Average'].append(dress_id)
        elif price == 'Medium':
            price_dict['Medium'].append(dress_id)

# Imprimir los resultados
if num_rated_dresses > 0:
    avg_rating = sum_ratings / num_rated_dresses
    print(f"La calificación promedio de los vestidos con puntuación > 0 es: {avg_rating:.2f}")
else:
    print("No hay vestidos con puntuación > 0.")

print("Los vestidos recomendados (Recomendación = 1) tienen los siguientes Dress_ID:")
for dress_id in recommended_dress_ids:
    print(dress_id)

print(f"Número de vestidos no recomendados (Recomendación = 0) con patrón de animales: {animal_pattern_count}")

print("Información de los vestidos de verano con estilo 'sexy':")
for dress in sexy_summer_dresses:
    print(dress)

print("\nDress_ID por precio:")
for price, dress_ids in price_dict.items():
    print(f"{price}: {', '.join(dress_ids)} (Total: {len(dress_ids)})")