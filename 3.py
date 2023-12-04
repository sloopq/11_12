import csv
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
passenger_data = {'Year': [], 'Month': [], 'Passengers': []}
with open('file.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        year, month = row['Month'].split('-')
        passenger_data['Year'].append(int(year))
        passenger_data['Month'].append(int(month))
        passenger_data['Passengers'].append(int(row['#Passengers']))

# График пассажиропотока за все время (линейный график)
plt.figure(figsize=(10, 5))
plt.plot(range(len(passenger_data['Passengers'])), passenger_data['Passengers'])
plt.xlabel('Месяцы с начала записей')
plt.ylabel('Количество пассажиров')
plt.title('Пассажиропоток за все время')
plt.show()

# Распределение пассажиров по месяцам в 1951-1955 годах (гистограмма)
years_51_to_55 = range(1951, 1956)
for year in years_51_to_55:
    year_passengers = [
        passenger_data['Passengers'][i] for i in range(len(passenger_data['Passengers']))
        if passenger_data['Year'][i] == year
    ]
    plt.hist(year_passengers, bins=10, alpha=0.5, label=str(year))

plt.xlabel('Количество пассажиров')
plt.ylabel('Частота')
plt.title('Распределение пассажиров по месяцам (1951-1955)')
plt.legend()
plt.show()
