# Программа для поиска плагиата загружаемых файлов
## Работает с docx, pdf, txt
Загружаемый файл в эндпоинт "/database/" обрабатывается разбивается на шинглы, а затем шинглы загружаюся в базу данных, а если загрузить файл в "/uploadfile/", то текст будет сравниваться с шинглами из базы данных.
Для работы программы потребуется загрузить базу данных из репазитория и активировать её с помощью pgAdmin4
