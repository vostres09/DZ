

 #Условие 1: Считать данные и вывести первые 5 строк, а также описание признаков.


import pandas as pd

# Считываем данные
data = pd.read_csv('kc_house_data.csv')

# Выводим первые 5 строк
print(data.head())

# Описание признаков
print(data.columns)

# Условие 2: Провести первичный анализ данных
# Типы данных
print(data.dtypes)

# Количество пропущенных ячеек
print(data.isnull().sum())

# Основные статистики
print(data.describe())

##Условие 3: Ответить на вопросы.


# 3.1 Диапазон стоимостей недвижимости
print(f"Минимальная стоимость: {data['price'].min()}")
print(f"Максимальная стоимость: {data['price'].max()}")

# 3.2 Доля жилой площади от всей площади
data['pct_living_area'] = data['sqft_living'] / data['sqft_lot'] * 100
print(f"Средняя доля жилой площади: {data['pct_living_area'].mean():.2f}%")

# 3.3 Количество домов с разными этажами
print(data['floors'].value_counts())

# 3.4 Состояние домов
print(data['condition'].value_counts())

# 3.5 Года постройки первого и последнего дома
print(f"Год постройки первого дома: {data['yr_built'].min()}")
print(f"Год постройки последнего дома: {data['yr_built'].max()}")

#Будут выведены ответы на вопросы 3.1-3.5.

#Условие 4: Ответить на вопросы.


# 4.1 Средняя стоимость домов с 2 спальнями
avg_price_2_bedrooms = data.loc[data['bedrooms'] == 2, 'price'].mean()
print(f"Средняя стоимость домов с 2 спальнями: {avg_price_2_bedrooms:.2f}")

# 4.2 Средняя общая площадь домов с ценой выше 600 000
avg_sqft_expensive = data.loc[data['price'] > 600000, 'sqft_living'].mean()
print(f"Средняя общая площадь дорогих домов: {avg_sqft_expensive:.2f}")

# 4.3 Количество домов, где был ремонт
renovation_count = data[data['yr_renovated'] > 0].shape[0]
print(f"Количество домов, где был ремонт: {renovation_count}")

# 4.4 Разница в стоимости домов с высокой и низкой оценкой grade
avg_price_high_grade = data.loc[data['grade'] > 10, 'price'].mean()
avg_price_low_grade = data.loc[data['grade'] < 4, 'price'].mean()
price_import pandas as pd

# заг   рузка данных
data = pd.read_csv('kc_house_data.csv')

# 5.1 Выберите дом клиенту
criteria_5_1 = (data['waterfront'] == 1) & (data['bathrooms'] >= 3) & (data['sqft_basement'] > 0)
houses_5_1 = data.loc[criteria_5_1]
print(f)
      #5.1 Количество подходящих домов: {len(houses_5_1)}")

# 5.2 Выберите дом клиенту
criteria_5_2 = ((data['view'] == 4) | (data['waterfront'] == 1)) & (data['condition'] == 5) & (data['yr_built'] >= 1980)
houses_5_2 = data.loc[criteria_5_2, 'price']
print(f"5.2 Ценовой диапазон: ${houses_5_2.min()} - ${houses_5_2.max()}")

# 5.3 Выберите дом клиенту
criteria_5_3 = (data['sqft_basement'] == 0) & (data['floors'] == 2) & (data['price'] <= 150000)
houses_5_3 = data.loc[criteria_5_3, 'condition']
print(f"5.3 Средняя оценка состояния: {houses_5_3.mean():.2f}")     