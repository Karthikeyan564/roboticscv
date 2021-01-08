FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install libgl1-mesa-glx -y
EXPOSE 5555:5555
COPY . .

CMD [ "python", "detect.py" ]
