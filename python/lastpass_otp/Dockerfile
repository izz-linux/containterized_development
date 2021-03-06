# use python 3.7.4
FROM python:3.7.4

# set our working directory in the container
WORKDIR /develop

# copy up our requirements.txt to the container
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy up our scripts to the working directory in our container
COPY src/ .

#docker build -t pythonimage .
#docker run -it pythonimage bash
#docker rm 291f2550af70
#docker images
#docker rmi 141cbf796302
