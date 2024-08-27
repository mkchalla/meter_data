FROM python:3.10.14-bookworm

WORKDIR /opt/app

RUN pip3 install pdm

COPY . .

RUN pdm install

WORKDIR /opt/app/src

CMD ["/opt/app/.venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]



