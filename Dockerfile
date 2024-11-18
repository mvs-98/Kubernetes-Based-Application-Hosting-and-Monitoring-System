FROM python:3.9
2 WORKDIR /app
3 COPY Loadgenerator.py
4 Run pip install requests
5 CMD ["python", "loadgenerator.py"]