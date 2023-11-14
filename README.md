# Лабораторная работа 3.  
## Цель работы  
Настроить автоматическую сборку образа и сохранение его на DockerHub после пуша в репозиторий.  
## Ход работы  
Для начала необходимо сохранить логин и пароль для входа в DockerHub:  

![Снимок экрана (2375)](https://github.com/KirillMisilin/Clouds-lab3/assets/88585791/01c8a00c-e64f-4fc9-b0aa-648727fd1d6f)

Далее был написан файл main.yml:  
```
name: Push_To_DockerHub

on:
  push:
    branches: "main"
    
jobs:
  build-and-push:
    runs-on: ubuntu-22.04

    defaults:
      run:
        working-directory: "/"

    steps:
      - name: checkout_repository
        uses: actions/checkout@v4

      - name: docker_login
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: docker_build_and_push
        uses: docker/build-push-action@v5
        with:
          context: "./"
          push: true
          tags: kirillmisilin/auto-docker:latest
```

В первой строке задается имя сценария.
```
name: Push_To_DockerHub
```
Далее указывается, что сценарий должен запускаться при пуше в ветку main:  
```
on:
  push:
    branches: "main"
```
Далее указывается, что нужно сделать при активации сценария. Для начала указывается, на чем нужно выполнять команды.  
```
jobs:
  build-and-push:
    runs-on: ubuntu-22.04
```

Далее задается рабочая директория по умолчанию:  
```
    defaults:
      run:
        working-directory: "/"
```
Далее указаны шаги, необходимые для выполнения сценария.

На первом шаге используется готовый сценарий actions/checkout@v4  
```
    steps:
      - name: checkout_repository
        uses: actions/checkout@v4
```
Далее выполняется вход в DockerHub:
```
      - name: docker_login
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
```
Далее образ собирается и пушится на DockerHub:
```
      - name: docker_build_and_push
        uses: docker/build-push-action@v5
        with:
          context: "./"
          push: true
          tags: kirillmisilin/auto-docker:latest
```

## Результаты  
Образ успешно запушился на DockerHub:  
![Снимок экрана (2371)](https://github.com/KirillMisilin/Clouds-lab3/assets/88585791/c540601d-e3dc-43c1-86be-3a44664fa3e4)

Сценарий срабатывает после каждого пуша в репозиторий:  
![Снимок экрана (2374)](https://github.com/KirillMisilin/Clouds-lab3/assets/88585791/50792857-f877-4551-a5f8-3ffd87d593f2)


## Вывод
В результате выполнения работы была настроена автоматическая сборка и сохранение образа на DockerHub после каждого пуша в репозиторий.
