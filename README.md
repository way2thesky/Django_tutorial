<h1> Курс молодого Бойца! </h1>

https://docs.djangoproject.com/en/3.2/intro/tutorial01/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial02/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial03/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial04/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial05/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial06/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial07/<br>

<h2> <strong>Homework 5. queryset filter, managment commands:</strong><br></h2>
<li>
Написать кастомную менеджент комманду которая будет генеритовать случайных пользователей ( https://docs.djangoproject.com/en/3.1/ref/models/querysets/#create ) c username, email и password. Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей. Значения меньше 1 и больше 10 - должны вызывать ошибку.
https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/
</li>

<h2><strong>Homework 6. Django forms:</strong><br></h2>
<li>
Добавить вью по пути /triangle
На этой вью необходимо использовать форму которая будет принимать значения двух катетов треугольника (положительные, больше нуля, для простоты используйте int значения если хотите). После отправки формы, если значения были валидными - на этой же странице вывести значение гипотенузы.
Это должна быть одна view
Можете использовать 1 или 2 темплейта при необходимости для рендера формы и результата.
Если один темплейт - значение гипотенузы по умолчанию None - проверяйте его в темплейте, и на основании того None или "значение" рендерите форму или значение гипотенузы
</li>

<h2><strong>Homework 7. Django model form:</strong><br></h2>
<li>
Создать новую модель с несколькими полями. Создать миграцию и мигрировать.<br>
<li>Person:<br>
<ol>
<li>first_name - charfield<br></li>
<li>last_name - charfield<br></li>
<li>email - emailfield<br>
</ol>
</li>
Создать modelform, view, template для - создания новой записи, и для редактирования существующей записи.<br>
<br>
/person - GET - получить форму<br>
/person - POST - отвалидировать и сохранить новый объект Person в базу<br>

<h2><strong>Homework 8. OneToOneField, ForeignKey, ManyToManyField::</strong><br></h2>
<li>
Реализовать в приложении модели использующие поля OneToOneField, ForeignKey, ManyToManyField.

Использовать graph_models из django-extensions что бы отобразить структуру моделей ТОЛЬКО этого приложения.

Пример:

Город Клиент (MTM на товар, FK на город)
Товар Поставщик (OTO на город)
Написать по запросу из инстанса одной модели в другую по каждой из связей (всего 3 запроса).

Для создания запроса используйте shell_plus --print-sql что бы ваш SQL отобразился в консоли.
</li>

<h2><strong>Homework 9. Middleware, ModelAdmin:</strong><br></h2>

<li>
Добавить модель для логов. В ней должны быть поля - path (путь), method (GET, POST etc), timestamp. Добавить мидлвар LogMiddleware который будет обрабатывать каждый реквест (кроме реквестов в админку) и сохранять соответствующие значения в базу.
Добавить ModelAdmin для этой модели что бы вывести соответствующие данные в админке.ть модель для логов. В ней должны быть поля - path (путь), method (GET, POST etc), timestamp. Добавить мидлвар LogMiddleware который будет обрабатывать каждый реквест (кроме реквестов в админку) и сохранять соответствующие значения в базу. Добавить ModelAdmin для этой модели что бы вывести соответствующие данные в админке.
</li>