FROM python:3.7-buster

# prevents writing pyc files and writting errors to standard out 
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
ENTRYPOINT ["tail", "-f", "/dev/null"]
COPY . /code/
