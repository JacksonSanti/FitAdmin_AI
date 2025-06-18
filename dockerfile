FROM python:3.11-slim

WORKDIR /AI

COPY requirements.txt /AI/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "run.py"]
