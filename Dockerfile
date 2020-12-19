FROM ubuntu:18.04
LABEL maintainer="João Dartora <joao.dartora@gmail.com>"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip
RUN pip3 install flask

EXPOSE 8080
WORKDIR /usr/src/app
COPY . .
CMD ["random_greetings.py"]
ENTRYPOINT ["python3"]