FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /api_stripe
WORKDIR /api_stripe
COPY requirements.txt /api_stripe/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /api_stripe/