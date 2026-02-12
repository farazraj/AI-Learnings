To start the application -

1. Start the redis server using docker/Download Memurai and install on your windows system and run as a windows service
2. Start the celery in a powersehell terminal using: celery -A employee worker -l info -P solo
3. Start celery in a powershell terminal for autonomous task like auto delete using: celery -A employee beat -l info
4. Start the daphne in another powershell termincal using: daphne -p 8000 employee.asgi:application


PS: Here Procfile is used to start all on single terminal. Using Honcho library.