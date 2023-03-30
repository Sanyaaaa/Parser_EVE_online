import requests

# Ввод необходимых ID(Идентификаторы регионов и типов предметов можно найти на сайте https://evemarketer.com/)
item_id = input("Введите ID предмета: ")
region1_id = input("Введите ID первого региона: ")
region2_id = input("Введите ID второго региона: ")

# Формирование URL-адресов для запроса цены предмета на рынках
url1 = f"https://esi.evetech.net/latest/markets/{region1_id}/orders/?datasource=tranquility&type_id={item_id}"
url2 = f"https://esi.evetech.net/latest/markets/{region2_id}/orders/?datasource=tranquility&type_id={item_id}"

# Отправка запросов и получение ответов
response1 = requests.get(url1)
response2 = requests.get(url2)

# Обработка ответов
if response1.status_code == 200 and response2.status_code == 200:
    data1 = response1.json()
    data2 = response2.json()

    # Получение информации о предмете
    item_info_url = f"https://esi.evetech.net/latest/universe/types/{item_id}/?datasource=tranquility"
    item_info_response = requests.get(item_info_url)
    if item_info_response.status_code == 200:
        item_info = item_info_response.json()
        item_name = item_info['name']
    else:
        item_name = f"предмет с ID {item_id}"

    prices1 = [order['price'] for order in data1]
    prices2 = [order['price'] for order in data2]

    median_price1 = sum(prices1) / len(prices1)
    rounded_median_price1 = round(median_price1, 2)
    median_price2 = sum(prices2) / len(prices2)
    rounded_median_price2 = round(median_price2, 2)

    median_difference1 = rounded_median_price2 - rounded_median_price1
    median_difference2 = rounded_median_price1 - rounded_median_price2

    print(f"Средняя цена на '{item_name}' в регионе {region1_id} - {rounded_median_price1}")
    print(f"Средняя цена на '{item_name}' в регионе {region2_id} - {rounded_median_price2}")

    if median_price1 < median_price2:
        print(f"'{item_name}' дешевле в первом регионе на {median_difference1}")
    elif median_price1 > median_price2:
        print(f"'{item_name}' дешевле во втором регионе на {median_difference2}")
    else:
        print("У вещей одинаковые цены в обоих регионах")
else:
    print(f"Error: {response1.status_code} или {response2.status_code}")