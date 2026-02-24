FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
<<<<<<< HEAD
RUN pip install pytest pytest-cov
=======
>>>>>>> c0b70c8a3a8ec317e248fdce5463bffa3cd1cac8
COPY . .
EXPOSE 8443
CMD ["python","server.py"]