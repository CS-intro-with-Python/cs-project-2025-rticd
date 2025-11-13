FROM python:3.11-slim

WORKDIR /app
COPY . .


RUN pip install -r p_requirements.txt

CMD ["python", "src/server.py"]