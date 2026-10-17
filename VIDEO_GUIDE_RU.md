# Видеозащита: 6 пунктов, минимум действий

Цель — показать **готовый результат**, а не печатать всю лабораторную заново. Откройте один терминал в VS Code, пройдите в нём Linux → Git → Docker, затем покажите файлы и три вкладки браузера. Текст после **«Сказать»** можно читать дословно. Ориентир — **6–8 минут**; если Jenkins собирает дольше, дождитесь его. В задании 10–20 минут указаны как рекомендация, а не строгий минимум. Оценку длительности и полноты всё равно определяет преподаватель.

## До записи — сделать один раз

- Запустите Docker Desktop и VS Code. **Закройте вкладку jenkins/.env**, чтобы пароль не попал в видео.
- Войдите в Jenkins заранее: http://localhost:8080 . Откройте вкладки [GitHub](https://github.com/Suleimen05/eldosuly-suleimen-devops), [Jenkins Job](http://localhost:8080/job/Eldosuly_Suleimen_DevOps/) и http://localhost:8000 .
- Откройте **один встроенный терминал PowerShell**. До начала записи выполните:

~~~powershell
Set-Location 'C:\Users\PC\Desktop\девопстаск6\eldosuly_suleimen'
docker ps --filter name=eldosuly-suleimen
~~~

Должны работать три ваших контейнера: linux, jenkins и container. Если какой-то остановлен, запустите только его командой docker start ИМЯ_КОНТЕЙНЕРА. Проверьте микрофон. Теперь включайте запись. **Терминал дальше не закрывайте и повторно не открывайте.**

## 1. Мои данные — 0:00–0:15

**Показать:** Eldosuly_Suleimen_info.txt в VS Code.

**Сказать:** «Здравствуйте. Я Сүлеймен Елдосұлы, группа IT2-2310, Student ID 38320. Покажу шесть результатов лабораторной: Linux, Git и GitHub, Docker, Jenkins и работающий сайт».

## 2. Linux — 0:15–1:55

**В том же терминале войти в Linux:**

~~~powershell
docker exec -it eldosuly-suleimen-linux bash
~~~

**Вставить один блок команд Linux:**

~~~bash
cd /root/devops/eldosuly_suleimen
pwd
ls
cat Eldosuly_Suleimen_info.txt
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
tail -n 5 logs/application.log
ls -l private.txt public.txt
./scripts/Eldosuly_Suleimen_system.sh
ps aux | head -n 5
top -b -n 1 | head -n 8
exit
~~~

**Проверить на экране:** папки проекта, число ошибок 2, разные права файлов, вывод скрипта и список процессов. После exit вы опять в PowerShell. Это **единственный** переход между Linux и PowerShell.

**Сказать:** «Здесь структура проекта и файл с моими данными. find ищет лог, grep показывает ошибки и предупреждения — ошибок две. У закрытого файла права 600, у открытого 644: r — чтение, w — запись, x — выполнение. Bash-скрипт выводит мои данные и информацию о системе. ps и top показывают процессы, их PID и нагрузку».

*Если преподаватель отдельно попросит создать или изменить файл:* команды mkdir, touch, cp, mv, rm и head приведены в [LAB_GUIDE.md](LAB_GUIDE.md). Попробуйте выполнить их до защиты, чтобы суметь повторить самостоятельно.

## 3. Git и GitHub — 1:55–2:35

**Не уходя из PowerShell, вставить:**

~~~powershell
git log main --oneline --graph -10
git branch -a
git remote -v
git check-ignore -v logs/application.log
Get-Content .gitignore
~~~

**Проверить:** в истории виден merge ветки development, remote ведёт на ваш GitHub, лог игнорируется правилом *.log; файл .gitignore содержит также backup/ и .env.

**Сказать:** «Git сохранил больше пяти осмысленных коммитов. Отдельную ветку development я объединил с main. remote показывает мой GitHub. gitignore исключает логи, backup и локальный .env, поэтому эти файлы не отправляются в репозиторий».

*Текущая ветка может называться codex/video-guide-ru: это ветка инструкции. Jenkins берёт основной проект из main. Переключать ветку не нужно.*

## 4. Docker — 2:35–3:45

**В том же PowerShell показать образ, контейнер, логи и переменную:**

~~~powershell
docker images eldosuly-suleimen-devops
docker ps --filter name=eldosuly-suleimen-container
docker logs eldosuly-suleimen-container
docker exec eldosuly-suleimen-container printenv STUDENT_GROUP
~~~

**Сказать:** «Образ — пакет приложения, контейнер — его запущенная копия. Вот образ, контейнер и его логи. Переменная окружения STUDENT_GROUP равна IT2-2310; настройки передаются при запуске».

**Сразу после этого показать Compose четырьмя командами:**

~~~powershell
docker rm -f eldosuly-suleimen-container
docker compose up -d --build
docker compose ps
docker compose down
~~~

**Сказать:** «Docker Compose собрал и запустил приложение по одному файлу настроек. Команда ps показала работающий сервис. Я остановил его; сейчас Jenkins запустит приложение заново».

**Теперь терминал больше не нужен.** Оставьте его открытым и переходите к файлам.

## 5. Файлы и Jenkins — 3:45–5:50

**В VS Code быстро открыть по очереди:** Dockerfile → docker-compose.yml → Jenkinsfile. В Jenkinsfile показать пять строк stage.

**Сказать:** «Dockerfile описывает сборку образа. Compose задаёт порт 8000 и переменные окружения. Jenkinsfile задаёт этапы Checkout, Build, Test, Docker Build и Docker Run».

**В браузере открыть GitHub:** показать репозиторий, ветку main и файлы.

**Сказать:** «Это мой репозиторий GitHub; Jenkins берёт код отсюда».

**Открыть вкладку Jenkins Job:** показать имя Eldosuly_Suleimen_DevOps, нажать **Build Now**, открыть новую сборку → **Console Output**. Дождаться **Finished: SUCCESS**. Показать commit, который Jenkins взял из GitHub, строки **Ran 3 tests**, данные студента, запуск Docker и финальный статус.

**Сказать:** «Jenkins взял код из GitHub, выполнил три теста, собрал Docker-образ и запустил контейнер. Здесь мои данные и статус Finished: SUCCESS. Если этап завершится ошибкой, дальше сборка не пойдёт, а причина останется в консоли».

## 6. Работающий результат — 5:50–6:20

**Открыть и обновить** http://localhost:8000 . Показать свои данные. Если хотите дополнительно подтвердить ответ, открыть http://localhost:8000/health — должно быть OK.

**Сказать:** «Сайт снова работает после Jenkins. Полная цепочка такая: Linux — файлы проекта, Git — история, GitHub — репозиторий, Jenkins — автоматические тесты и сборка, Docker — запущенное приложение. Спасибо».

**Остановить запись.** Видео должно быть одним файлом, с вашим экраном и голосом. Для сдачи также нужны ссылка на GitHub и PDF-отчёт DevOps_Lab_Report_Eldosuly_Suleimen.pdf.

## Что должно точно попасть в кадр

- Ваши имя, группа и Student ID.
- В Linux: структура, grep/find, права, скрипт, процессы.
- В Git: история, ветка с merge, GitHub и игнорирование лога.
- В Docker: Dockerfile, образ, контейнер, переменная, логи и Compose.
- В Jenkins: Job, пять этапов, три теста, данные студента, Finished: SUCCESS.
- После Jenkins: открытый сайт с вашими данными.

Если команда выполняется дольше таймкода, просто ждите её результата. Не произносите таймкоды и не ускоряйте запись монтажом.
