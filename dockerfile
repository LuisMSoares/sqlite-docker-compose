FROM python:3.6
ADD ./code /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python run.py