# DevOps laboratory demonstration

Student: Елдосұлы Сүлеймен, IT2-2310, Student ID 38320.

The repository is at https://github.com/Suleimen05/eldosuly-suleimen-devops. The project directory in the Linux demonstration is `/root/devops/eldosuly_suleimen`. The Linux environment is the container named `eldosuly-suleimen-linux` on this computer.

## Start and finish

Open PowerShell in the project folder. Docker Desktop must be running.

```powershell
docker start eldosuly-suleimen-linux
docker exec -it eldosuly-suleimen-linux bash
```

Inside the Linux shell:

```bash
cd /root/devops/eldosuly_suleimen
bash scripts/prepare_lab.sh
```

The preparation script recreates `logs/application.log` and `backup/`, which Git ignores. It sets `private.txt` to `600` and `public.txt` to `644`.

## A. Linux

Show the project and basic commands:

```bash
pwd
ls
ls -la
cd app && pwd && cd ..
mkdir -p backup/demo
touch backup/demo/first.txt
cp backup/demo/first.txt backup/demo/copy.txt
mv backup/demo/copy.txt backup/demo/renamed.txt
cat Eldosuly_Suleimen_info.txt
head -n 3 Eldosuly_Suleimen_info.txt
tail -n 2 Eldosuly_Suleimen_info.txt
rm backup/demo/renamed.txt
```

`pwd` shows the current directory, `ls` lists files, and `cd` changes directory. `mkdir` creates a directory and `touch` creates an empty file. `cp` copies, `mv` moves or renames, and `rm` deletes the selected file. `cat` prints the whole file; `head` and `tail` print the first and last lines.

Search and count messages:

```bash
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
tail -n 5 logs/application.log
```

The expected ERROR count is 2. These are sample messages for command practice, not real application failures.

Show permissions and the Bash script:

```bash
ls -l private.txt public.txt scripts/Eldosuly_Suleimen_system.sh
chmod 600 private.txt
chmod 644 public.txt
chmod +x scripts/Eldosuly_Suleimen_system.sh
./scripts/Eldosuly_Suleimen_system.sh
```

`r`, `w`, and `x` mean read, write, and execute. The first three permission characters describe the owner, the next three the group, and the last three other users. `600` gives only the owner read/write access. `644` lets everyone read the public file, while only the owner can edit it. `755` gives the owner read/write/execute and everyone else read/execute.

Show processes:

```bash
ps
ps aux | head
top -b -n 1 | head -n 12
```

A process is a running program; its PID is the process identifier. `ps` is a snapshot and `top` updates the view continuously (the command above captures one frame for the video). In `ps aux`, USER is the owner, PID is the identifier, `%CPU` is CPU use, and `%MEM` is memory use.

## B. Git and GitHub

Run these in the Linux shell or in the project folder on Windows:

```bash
git status
git log --oneline --graph --all
git branch -a
git remote -v
git check-ignore -v logs/application.log
```

The history shows more than five meaningful commits. The `development` branch added the Linux preparation script, and `main` contains a merge commit. `.gitignore` excludes logs, backup files, and `.env`, so generated or private local data does not enter the repository. `git pull` brings remote changes into a local branch; `git push` sends local commits to GitHub.

## C. Docker

On Windows PowerShell, show the Docker files and existing image/container:

```powershell
Get-Content Dockerfile
Get-Content docker-compose.yml
docker images eldosuly-suleimen-devops
docker ps -a --filter name=eldosuly-suleimen-container
docker logs eldosuly-suleimen-container
```

The image is the packaged application and its runtime. A container is one running instance of that image. `WORKDIR` sets the working directory inside the image. `EXPOSE` documents port 8000; `-p 8000:8000` publishes it to this computer.

To demonstrate environment variables and container lifecycle, run these commands only when the Jenkins build is not running:

```powershell
docker stop eldosuly-suleimen-container
docker start eldosuly-suleimen-container
docker exec eldosuly-suleimen-container python -c "import os; print(os.getenv('STUDENT_GROUP'))"
docker rm -f eldosuly-suleimen-container
docker run -d --name eldosuly-suleimen-container -p 8000:8000 -e STUDENT_NAME=Сүлеймен -e STUDENT_SURNAME=Елдосұлы -e STUDENT_GROUP=IT2-2310 -e STUDENT_ID=38320 eldosuly-suleimen-devops
docker logs eldosuly-suleimen-container
```

An environment variable supplies a value at container startup. This lets the same image run with different settings. Secrets should come from protected runtime configuration and must not be written into the image.

For Compose, first remove the standalone app container because Compose uses the same required name:

```powershell
docker rm -f eldosuly-suleimen-container
docker compose up -d --build
docker compose ps
Invoke-WebRequest http://localhost:8000/health -UseBasicParsing
docker compose down
```

Compose stores the container configuration in one file, so it is easier to start and stop the application with the same settings.

## D. Jenkins

Jenkins is available at http://localhost:8080 when the local container is running. The job name is `Eldosuly_Suleimen_DevOps`. The local admin password is in `jenkins/.env`; keep that file private and do not show it in the video or report. The job reads `Jenkinsfile` from the public GitHub repository.

```powershell
docker compose --env-file jenkins/.env -f jenkins/docker-compose.yml up -d
docker ps --filter name=eldosuly-suleimen-jenkins
```

Start a build from the job page. Show the five stages, the Git commit in Checkout, the three passing Python tests, Docker Build, Docker Run, student information in Console Output, and `Finished: SUCCESS`. The Docker Run stage removes the earlier app container of this project, starts the new one, checks `/health`, and prints its logs. Open http://localhost:8000 to show the result.

If a stage fails, Jenkins marks the build failed and stops the later stages. The console log gives the command and error to fix before running it again.

## E. Complete workflow and submission

Linux provides the shell, processes and file permissions. Git records changes. GitHub stores the repository and makes it available to Jenkins. Jenkins checks out a commit, checks Python syntax, runs tests, builds a Docker image, and starts a container. The container serves the student page. If any command returns an error, the pipeline stops before later stages.

Submit the GitHub link, the PDF report, and one continuous 10–20 minute screen recording with your own voice. At the beginning of the video, show your name, group and ID. Then show Linux, Git/GitHub, Docker, Jenkins and the final application. You can prepare the project beforehand; explain the commands and results in your own words.
