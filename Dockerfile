FROM python:latest
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY main.py /code/main.py
COPY static/ /code/static
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
