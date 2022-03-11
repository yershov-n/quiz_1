FROM python:3.10

RUN apt update \
    && apt install -y mc \
    && apt install -y vim

RUN mkdir /opt/src
WORKDIR /opt/src

RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./accounts accounts
COPY ./app app
COPY ./core core
COPY ./media media
COPY ./quiz quiz
COPY ./static static
COPY ./templates templates
COPY ./db.sqlite3 .
COPY ./manage.py .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]