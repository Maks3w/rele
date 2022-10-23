FROM python:3.10-buster

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /rele
LABEL python_version=python

COPY requirements requirements/
RUN pip install -r requirements/django.txt -r requirements/test.txt

COPY Makefile setup.py README.md ./
COPY rele/__init__.py rele/
RUN make install-requirements

CMD ["make", "clean", "lint-fix", "test"]
