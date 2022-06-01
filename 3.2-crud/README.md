# Сборка контейнера

``docker build -t my-django ./``

# Запуск приложения в контейнере

``docker run --name my-django-server -d -p 8000:8000 my-django``
