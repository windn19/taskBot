# Бот по работе с заданиями.

Данный бот сделать в качестве тестового задания.

## Запуск

Проект предполагает наличие установленного Python. 

1. Установить зависимости

```commandline
pip install -r requirements.txt
```

2. Создать базы данных с именем tasks в PostgreSQL

```commandline
sudo -u postgres psql
postgres=# createbase tasks;
```

3. Запуск файла

```commandline
python bot.py
```
 - по командам "help" и "start" - бот вернет сообщение начало работы
 - по команде "add" - бот ожидает, что после текста команды через пробел - названия задачи, а затем через пробел текст
описания задачи. В случае успеха он выведет сообщение о создании сообщения, иначе вывод сообщения об отказе.
 - по команде 'tsk' - выводится каждое задание в отдельном сообщении.
