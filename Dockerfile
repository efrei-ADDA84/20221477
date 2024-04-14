FROM python:3.9-slim

WORKDIR /app
 
COPY tp1_devops.py .

RUN pip install requests

CMD ["python", "tp_devops.py"]
