# Описание
В этом проекте я решил сделать микросервис из модели классификации жалоб, которую я делал в одном из прошлых проектов. Для этого я написал простое приложение на Flask и запустил его внутри Docker-контейнера.

Обучение модели описано в файле [Обучение_модели_классификации_жалоб.ipynb](https://github.com/Popov-SS/Portfolio/blob/master/Complaint%20classification%20(deployment)/%D0%9E%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8_%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%B8_%D0%B6%D0%B0%D0%BB%D0%BE%D0%B1.ipynb). 
Из этого файла получается пайплайн обработки текста, пайплайн модели, и тестовый набор данных. 

Серверное приложение находится в файле [docker_components/server.py](https://github.com/Popov-SS/Portfolio/blob/master/Complaint%20classification%20(deployment)/docker_components/server.py)
В нём описана логика получения данных и формирования ответа. Входящие и исходящие файлы имеют формат JSON. Формат ответа сервера:
```
{'predict': результат метода .predict() для отправленного объекта,
 'proba': результат метода .predict_proba() для отправленного объекта,
 'success': Bool - статус ответа; 
 }
```

Процесс взаимодействия клиента и сервера описан в файле [Client_notebook.ipynb](https://github.com/Popov-SS/Portfolio/blob/master/Complaint%20classification%20(deployment)/Client_notebook.ipynb)
В нём я отправлял уже обработанный текст, полученный из файла обучения модели. Очищать текст лучше на стороне клиента, так как это занимает достаточно много времени.

Папка [docker_components](https://github.com/Popov-SS/Portfolio/tree/master/Complaint%20classification%20(deployment)/docker_components) 
содержит все необходимые файлы для создания образа контейнера:
* Сам Dockerfile;
* Файл requirements.txt с необходимыми для работы проекта библиотеками;
* Файл пайплайна модели;
* Файл серверного приложения.

# Скачивание файлов для создания образа:
```
svn checkout https://github.com/Popov-SS/Portfolio/trunk/'Complaint%20classification%20(deployment)'/docker_components
cd docker_components
docker build -t <image_name> .
```
# Запуск контейнера:
```
docker run -d -p 8180:8180 <image_name>
```
