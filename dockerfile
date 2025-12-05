FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requiremnts.txt
EXPOSE port 5005
CMD ["python", "app.py"]