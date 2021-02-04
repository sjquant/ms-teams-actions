FROM python:3.8.6-slim
RUN pip install --upgrade pip && pip install pymsteams==0.1.14
COPY main.py /main.py
ENTRYPOINT ["python", "/main.py"]