FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#docker-compose downCOPY ../best_yield_model.pkl /app/best_yield_model.pkl
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# FROM python:3.10-slim
# WORKDIR /app
# COPY . .
# RUN pip install --no-cache-dir -r requirements.txt
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]