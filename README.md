<h1> Создаение первого приложения на Django по документации </h1>

https://docs.djangoproject.com/en/3.2/intro/tutorial01/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial02/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial03/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial04/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial05/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial06/<br>
https://docs.djangoproject.com/en/3.2/intro/tutorial07/<br>

<strong>Homework 5. queryset filter, managment commands:</strong><br>

Написать кастомную менеджент комманду которая будет генеритовать случайных пользователей ( https://docs.djangoproject.com/en/3.1/ref/models/querysets/#create ) c username, email и password. Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей. Значения меньше 1 и больше 10 - должны вызывать ошибку.
https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/

<strong>Homework 6. Django forms:</strong><br>

Добавить вью по пути /triangle
На этой вью необходимо использовать форму которая будет принимать значения двух катетов треугольника (положительные, больше нуля, для простоты используйте int значения если хотите). После отправки формы, если значения были валидными - на этой же странице вывести значение гипотенузы.
Это должна быть одна view
Можете использовать 1 или 2 темплейта при необходимости для рендера формы и результата.
Если один темплейт - значение гипотенузы по умолчанию None - проверяйте его в темплейте, и на основании того None или "значение" рендерите форму или значение гипотенузы


<strong>Homework 7. Django model form:</strong><br>

Создать новую модель с несколькими полями. Создать миграцию и мигрировать.<br>
<li>Person:<br>
<ol>
<li>first_name - charfield<br></li>
<li>last_name - charfield<br></li>
<li>email - emailfield<br>
</ol>

Создать modelform, view, template для - создания новой записи, и для редактирования существующей записи.<br>
<br>
/person - GET - получить форму<br>
/person - POST - отвалидировать и сохранить новый объект Person в базу<br>