FROM ubuntu:18.04
LABEL maintainer="João Dartora <joao.dartora@gmail.com>"

# Update Ubuntu
RUN apt-get update

# Install Python Utils
RUN apt-get install -y python3 python3-dev python3-pip locales
RUN pip3 install flask

# Configure encoding
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8   

EXPOSE 8080
WORKDIR /usr/src/app
COPY . .
CMD ["random_greetings.py"]
ENTRYPOINT ["python3"]