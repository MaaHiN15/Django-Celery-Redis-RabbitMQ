FROM python:3.11.4-alpine

ARG HOME_DIR=/usr/src/app

WORKDIR $HOME_DIR

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

COPY req.txt $HOME_DIR/req.txt

RUN pip install -r $HOME_DIR/req.txt

COPY ./entrypoint.sh $HOME_DIR/entrypoint.sh

COPY . $HOME_DIR

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

