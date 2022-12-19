<p id="p7">
<h3>Оглавление:</h3>
<a href="#p1">Обзор</a></br>
<br><a href="#p2">Команды запуска через Terminal</a></br>
<br><a href="#p3">Тесты на странице авторизации</a></br>
<br><a href="#p4">Тесты на странице авторизации с временным кодом</a></br>
<br><a href="#p5">Тесты на странице восстановления пароля</a></br>
<br><a href="#p6">Тесты на странице регистрации</a></br></p>

<p id="p1">
<h3>Обзор:</h3>

Проект содержит автотесты для UI тестирования сервисов:
<br> | [ЕЛК Web](https://lk.rt.ru) | 
[Онлайм Web](https://my.rt.ru) | 
[Старт Web](https://start.rt.ru) | 
[Умный дом Web](https://lk.smarthome.rt.ru) | 
[Ключ Web](https://key.rt.ru) | 
</br>
<br>Chromedriver добавлен в файлы проекта</br>
<br>Наборы тестовых данных хранятся в файле test_data.py</br>
<br>Фикстуры открытия веб-страниц расположены в conftest.py</br></p>

<p id="p2"><h3>Команды запуска через Terminal:</h3>

Создание виртуального окружения:
>python -m venv venv

Активация скриптов виртуального окружения:
>venv\scripts\activate

Вывод отчетов в allure:
>allure serve allureres

Запуск тестов на странице авторизации auth_tests.py:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/auth_tests.py

Запуск тестов на странице авторизации по временному коду get_code_tests.py:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/get_code_tests.py

Запуск тестов на странице восставновления пароля recovery_tests.py:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/recovery_tests.py

Запуск тестов на странице восставновления пароля recovery_tests.py с подготовкой отчетов в allure:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/recovery_tests.py --alluredir=allureres

Запуск тестов на странице регистрации reg_tests.py:
>python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/reg_tests.py</p>

<p id="p3">
<h3>Тесты на странице авторизации</h3>
<p>
<b>test_elk_default_tab</b>
<br>позволяет удостовериться, что Телефон выбран в качестве таба по умолчанию</br>
</p>

<p>
<b>test_elk_switch_to_email_tab</b>
<br>автоматическое переключение на таб Почта при вводе email</br>
</p>

<p>
<b>test_elk_switch_to_login_tab</b>
<br>автоматическое переключение на таб Логин при вводе логин:</br>
</p>

<p>
<b>test_elk_switch_to_phone_tab</b>
<br>автоматическое переключение на таб Телефон при вводе номера телефона, если предварительно был выбран другой таб</br>
</p>

<p>
<b>test_elk_phone_authorization_no_such_user</b>
<br>попытка входа с учетными данными незарегистрированного пользователя<br>
<p>

<p>
<b>test_elk_invalid_username_authorization</b>
<br>попытка ввода названия учетной записи в невалидном формате</br>
</p>

<p>
<b>test_elk_invalid_password_authorization</b>
<br>попытка ввода пароля в невалидном формате</br>
</p></p>

<p id="p4">
<h3>Тесты на странице авторизации с временным кодом</h3>

<p>
<b>test_key_web_invalid_one_time_code</b>
<br>попытка авторизации по имейл, либо номеру мобильного телефона с вводом неверного временного кода</br>
</p>

<p>
<b>test_key_web_go_to_pswd_auth_page</b>
<br>переход на страницу обычной авторизации со страницы авторизации по временному коду</br>
</p>

<p>
<b>test_key_web_return_to_one_time_code</b>
<br>возврат на страницу авторизации по временному коду со страницы обычной авторизации</br>
</p>

<p>
<b>test_onlime_get_one_time_code_by_email</b>
<br>отправка формы запроса временного кода на имейл зарегистрированного пользователя</br>
</p>

<p>
<b>test_smarthome_get_code_positive</b>
<br>отправка формы запроса временного кода по номеру телефона</br>
</p>

<p>
<b>test_start_web_invalid_phone_or_email</b>
<br>попытка ввода номера мобильного телефона, либо имейл в невалидном формате</br>
</p></p>

<p id="p5">
</p><h3>Тесты на странице восстановления пароля</h3>

<p>
<b>test_elk_pswd_recovery_captcha</b>
<br>попытка восстановления пароля по номеру телефона/почте/логину/лицевому счету без ввода капчи, либо с вводом неверного значения в поле капчи</br>
</p></p>

<p id="p6">
</p><h3>Тесты на странице регистрации</h3>

<p>
<b>test_elk_sign_up_diverse_regions</b>
<br>отправка формы регистрации с валидным данными для разных регионов</br>
</p>

<p>
<b>test_elk_sign_up_invalid_first_name</b>
<br>ввод имени в невалидном формате</br>
</p>

<p>
<b>test_elk_sign_up_invalid_surname</b>
<br>ввод фамилии в невалидном формате</br>
</p>

<p>
<b>test_elk_sign_up_invalid_phone_or_email</b>
<br>ввод мобильного телефона/имейла в невалидном формате</br>
</p>

<p>
<b>test_elk_sign_up_invalid_password</b>
<br>попытка создания невалидного пароля</br>
</p>

<p>
<b>test_elk_unconfirmed_password</b>
<br>попытка отправки формы регистрации без подтверждения пароля, либо при несовпадающих паролях</br>
</p></p>

<a href="#p7">Вверх</a>