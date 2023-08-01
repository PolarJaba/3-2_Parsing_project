# 3-2_Parsing_project

Средствами языка python ([скрипт](https://github.com/PolarJaba/3-2_Parsing_project/blob/dev/app/parsing_data.py)) создана база данных postgres и выполнен парсинг сайта Exchange.host, в резальтате чего получена таблица: ![таблица](https://github.com/PolarJaba/3-2_Parsing_project/blob/dev/parced_data.PNG)

Посредствам запросов к созданной БД получена витрина данных ввиде отдельной таблицы БД:
![витрина](https://github.com/PolarJaba/3-2_Parsing_project/blob/dev/data_mart.PNG)

Развертывание СУБД postgres и контейнера python реализовано через [docker compose](https://github.com/PolarJaba/3-2_Parsing_project/blob/dev/docker-compose.yml).
