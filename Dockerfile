FROM python:3-alpine
WORKDIR /home/app
ADD requirements.txt /home/app
RUN pip3 install --no-cache-dir -r requirements.txt
ADD . /home/app
CMD python3 dev_run.py
EXPOSE 3001
