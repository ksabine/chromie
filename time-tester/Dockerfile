FROM python:3-alpine
RUN pip install --no-cache-dir requests
COPY main.py /app/
ENV ENDPOINT http://time-keeper
ENV CALLS_PER_SECOND 10
CMD ["python", "/app/main.py"]
