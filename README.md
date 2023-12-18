# Приложение для рассылок на Django

Приложение позволяет создавать рассылки для отправки их через электронную почту по расписанию
Пользователи разделены на роли:
user - обычный пользователь, который создает клиентов и рассылки для них, может писать статьи в блоге;
manager - менеджер, может блокировать пользователей и рассылки. Менеджер не имеет статус персонала. Необходимый функционал
обеспечен экранами.

Для приложения применено разделение прав доступа и кеширование данных. 

Команды:

- python manage.py mailing_start - ручная отправка активных рассылок, учитывая условия отправки (так же производится автоматически, каждые 10 минут);
- - python manage.py mailing_start_now - принудительная ручная отправка всех активных рассылок, игнорируя условия отправки;
- python manage.py csu - создать суперпользователя;      
- python manage.py runserver - запуск сервиса. 

ВАЖНО!!! Для запуска приложения необходимо загрузить приложенные фикстуры.