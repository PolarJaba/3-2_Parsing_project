<b>Для запуска скрипта необходимо ввести в командную строку следующие команды:</b>

cd C:\путь к директории

docker build -t image .

docker run -d -p 6544:5432 --name python_code image

После успешного запуска контейнера произвести запуск скрипта с указанием текущих параметров подключения

В результате работы [скрипта](https://github.com/PolarJaba/3-2_Parsing_project/blob/dev/dockerfile_version/parsing_data.py) получена следующая таблица:
![](https://github.com/PolarJaba/3-2_Parsing_project/blob/dev/dockerfile_version/image.png)
