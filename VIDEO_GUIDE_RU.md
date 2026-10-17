# Как записать видео по лабораторной DevOps

Это маршрут для **одной непрерывной записи экрана с вашим голосом**. По заданию рекомендована длительность 10–20 минут. Удобная цель — около 15 минут. Команды ниже рассчитаны на этот компьютер: проект находится в `C:\Users\PC\Desktop\девопстаск6\eldosuly_suleimen`, Linux, приложение и Jenkins запущены через Docker Desktop.

Говорите своими словами. Фразы в кавычках — подсказки, а не текст, который обязательно читать дословно.

## Подготовка до начала записи

1. Запустите Docker Desktop. Откройте проект в VS Code и терминал PowerShell.
2. Откройте в браузере GitHub-репозиторий, `http://localhost:8080` и `http://localhost:8000`. В Jenkins войдите **до начала записи**: логин `admin`, пароль находится в локальном `jenkins/.env`.
3. **Закройте вкладку `.env` перед записью.** Не показывайте пароль ни в терминале, ни в браузере, ни на видео.
4. Проверьте, что микрофон записывает голос, текст на экране читается, уведомления не перекрывают окно. Не останавливайте запись между разделами.
5. В PowerShell перейдите в папку проекта:

```powershell
Set-Location 'C:\Users\PC\Desktop\девопстаск6\eldosuly_suleimen'
docker ps --filter name=eldosuly-suleimen
```

Если Linux-контейнер остановлен, выполните `docker start eldosuly-suleimen-linux`. Если Jenkins остановлен, выполните `docker start eldosuly-suleimen-jenkins`. Это подготовка, её можно сделать до записи.

## 0:00–0:45 — представление

Начните запись. Покажите `Eldosuly_Suleimen_info.txt` в редакторе. Скажите: «Меня зовут Сүлеймен Елдосұлы, группа IT2-2310, Student ID 38320. Я покажу путь проекта от Linux и Git до Docker и Jenkins».

## 0:45–4:30 — Linux

В терминале PowerShell войдите в Linux-контейнер:

```powershell
docker exec -it eldosuly-suleimen-linux bash
```

Теперь приглашение терминала относится к Linux. Выполните команды:

```bash
cd /root/devops/eldosuly_suleimen
pwd
ls -la
cat Eldosuly_Suleimen_info.txt
```

Скажите: «`pwd` показывает текущий путь, `ls` — содержимое папки, `cat` — данные студента. Папки `app`, `scripts`, `config`, `logs` и `backup` находятся в моём проекте».

Покажите создание, копирование, переименование и удаление файла:

```bash
mkdir -p backup/demo
touch backup/demo/first.txt
cp backup/demo/first.txt backup/demo/copy.txt
mv backup/demo/copy.txt backup/demo/renamed.txt
ls backup/demo
rm backup/demo/renamed.txt
head -n 3 Eldosuly_Suleimen_info.txt
tail -n 2 Eldosuly_Suleimen_info.txt
```

Скажите коротко, что делают `mkdir`, `touch`, `cp`, `mv`, `rm`, `head` и `tail`. Папка `backup` игнорируется Git, поэтому пробные файлы не попадут в репозиторий.

Покажите поиск, права и скрипт:

```bash
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
tail -n 5 logs/application.log
ls -l private.txt public.txt
./scripts/Eldosuly_Suleimen_system.sh
ps
ps aux | head -n 5
top -b -n 1 | head -n 10
```

Ожидается **2 строки ERROR**. Скажите: «У `private.txt` права `600`: читать и менять файл может владелец. У `public.txt` права `644`: остальные могут его читать. `r`, `w`, `x` означают чтение, запись и выполнение. `ps` показывает список процессов на момент команды, `top` — использование ресурсов; PID — номер процесса». Скрипт выводит ваши данные и информацию о системе, затем проверяет наличие файла с данными студента.

Вернитесь в PowerShell:

```bash
exit
```

## 4:30–6:30 — Git и GitHub

В PowerShell, оставаясь в папке проекта, выполните:

```powershell
git status
git log --oneline --graph --all -10
git branch -a
git remote -v
git check-ignore -v logs/application.log
Get-Content .gitignore
```

Покажите в браузере `https://github.com/Suleimen05/eldosuly-suleimen-devops`. Укажите ветки `main` и `development`, осмысленные коммиты и merge-коммит.

Скажите: «Git сохраняет историю изменений. Ветка `development` позволила добавить подготовку Linux-файлов отдельно, затем я объединил её с `main`. GitHub хранит проект и отдаёт его Jenkins. `.gitignore` исключает логи, `backup/` и `.env`».

## 6:30–10:00 — Docker и Docker Compose

Покажите `Dockerfile` и `docker-compose.yml` в редакторе. Объясните `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`: базовый образ, рабочая папка, копирование файлов, команда при сборке, порт и команда запуска.

В PowerShell:

```powershell
docker images eldosuly-suleimen-devops
docker ps -a --filter name=eldosuly-suleimen-container
docker logs eldosuly-suleimen-container
docker exec eldosuly-suleimen-container printenv STUDENT_GROUP
docker stop eldosuly-suleimen-container
docker start eldosuly-suleimen-container
```

Скажите: «Образ — готовый пакет приложения. Контейнер — его запущенный экземпляр. Значение `STUDENT_GROUP` передано через переменную окружения; тот же образ можно запускать с другими данными». Команды `stop` и `start` на несколько секунд отключат только контейнер этого проекта.

Затем покажите удаление контейнера и Compose. **Выполняйте этот блок до нового запуска Jenkins**, чтобы pipeline снова поднял приложение в конце видео:

```powershell
docker rm -f eldosuly-suleimen-container
docker compose up -d --build
Start-Sleep -Seconds 2
docker compose ps
Invoke-WebRequest http://localhost:8000/health -UseBasicParsing
docker compose down
```

Для `/health` ожидается `200` и `OK`. Скажите: «Compose берёт настройки сборки, порта и переменных окружения из одного YAML-файла. `up` запускает сервис, `down` останавливает и удаляет его контейнер».

## 10:00–13:30 — Jenkins

Откройте вкладку `http://localhost:8080`. Покажите Job **`Eldosuly_Suleimen_DevOps`**. Откройте `Jenkinsfile` в редакторе и назовите пять этапов: `Checkout`, `Build`, `Test`, `Docker Build`, `Docker Run`.

В Jenkins нажмите **«Собрать сейчас» / Build Now**. Откройте новую сборку, затем **Console Output**. Дождитесь `Finished: SUCCESS` и покажите:

- GitHub URL и commit, который взял Jenkins;
- три прошедших теста;
- сборку Docker-образа и запуск контейнера;
- ваши имя, группу и Student ID в выводе;
- строку `Finished: SUCCESS`.

Скажите: «Jenkins получает код из GitHub, проверяет Python-файлы, запускает тесты, собирает Docker-образ и запускает контейнер. Если этап завершится ошибкой, следующие этапы не выполнятся; причину можно увидеть в Console Output».

## 13:30–15:00 — итоговый результат

Откройте `http://localhost:8000` и покажите страницу с вашими данными. В PowerShell выполните:

```powershell
docker ps --filter name=eldosuly-suleimen-container
docker images eldosuly-suleimen-devops
```

Завершите словами: «Весь путь выглядит так: Linux → Git → GitHub → Jenkins → сборка → тесты → Docker-образ → контейнер. Приложение работает, а Jenkins завершил pipeline успешно». Только после этого остановите запись.

## Перед отправкой

Проверьте, что получился **один видеофайл**, слышно ваш голос, видны экран и финальный `SUCCESS`. Для сдачи нужны три пункта: ссылка на GitHub, PDF-отчёт `DevOps_Lab_Report_Eldosuly_Suleimen.pdf` из папки `девопстаск6` и ваше видео. Если реальная запись займёт 12 или 18 минут, это укладывается в рекомендованные 10–20 минут.
