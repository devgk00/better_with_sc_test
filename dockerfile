FROM python:3
WORKDIR /usr/src/
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "main.py"]