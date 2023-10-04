FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000
CMD cd source && python db_init.py && uvicorn app:app --reload --host 0.0.0.0