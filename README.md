В данном репозитории находится итоговый проект по автоматизации тестирования: 

test_auth.py       - тесты авторизации,
test_register.py   - тесты регистрации,
test_ui.py         - тесты UI.

Кроме того, в папке есть файл settings.py, содержащий переменные, необходимые для тестов, а так же conftest.py, содержащий фикстуры.

Из-за невозможности отключить капчу при превышении порогового значения попыток авторизации, соответствующие тесты могут быть нестабильны. Без капчи они работают верно.

Тестов авторизации всего 15 штук:

 1. позитивный тест на авторизацию по телефону
 2. негативный тест на авторизацию по телефону
 3. позитивный тест на авторизацию по почте
 4. негативный тест на авторизацию по почте
 5. позитивный тест на авторизацию по логину
 6. негативный тест на авторизацию по логину
 7. позитивный тест на авторизацию по лицевому счету
 8. негативный тест на авторизацию по лицевому счету
 9. Негативный тест с неверным паролем
 10. Негативный тест во всеми пустыми значениями
 11. авторизация через ВКонтакте работает
 12. авторизация через Одноклассники работает
 13. авторизация через mail.ru работает
 14. авторизация через google.com работает
 15. авторизация через ya.ru работает

Тестов Регистрации всего 7 штук.
 1. ссылка на страницу регистрации в блоке авторизации работает
 2. позитивный тест на регистрацию
 3. негативный тест на регистрацию с невалидными именем/фамилией
 4. негативные тесты на регистрацию по неверному телефону
 5. негативные тесты на регистрацию по неверному email
 6. негативный тест на регистрацию по уже существующему телефону
 7. негативный тест на регистрацию по уже существующему email

Тестов UI всего 8 штук.
 1. стартовая страница открывается, обязательные элементы присутствуют
 2. При вводе неверного пароля цвет ссылки "забыл пароль" меняется на оранжевый
 3. Ссылка "Забыл пароль" ведёт на страницу восстановления пароля
 4. На странице восстановления пароля присутствуют все необходимые поля
 5. На странице восстановления обновляется капча.
 6. Ссылка на пользовательское соглашение в блоке авторизации работает
 7. Ссылка на политику конфиденциальности и пользовательское соглашение в футере работает
 8. Ссылка Cookies в футере открывает окно с подсказкой.