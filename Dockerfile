FROM python:3.12-alpine

WORKDIR /project

COPY app/ ./app/
COPY scripts/ ./scripts/
COPY Eldosuly_Suleimen_info.txt ./

RUN python -m compileall -q app && chmod +x scripts/Eldosuly_Suleimen_system.sh

EXPOSE 8000

CMD ["python", "-u", "app/main.py"]
