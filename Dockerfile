FROM python:3.12

RUN mkdir /task_manager_api

WORKDIR /task_manager_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
