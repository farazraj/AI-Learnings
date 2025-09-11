To start the application -

1. Start the redis server using docker
2. Start the celery in a powersehell terminal using: celery -A employee worker -l info -P solo
3. Start the daphne in another powershell termincal using: daphne -p 8000 employee.asgi:application