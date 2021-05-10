FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app

# run unit tests
RUN python -m pytest tests/bdd/step_definitions
RUN python -m pytest tests/unit_tests

# start app server
CMD ["python", "app.py"]
