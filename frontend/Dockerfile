FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install streamlit requests
CMD ["streamlit", "run", "app.py", "--server.port=3000"]
