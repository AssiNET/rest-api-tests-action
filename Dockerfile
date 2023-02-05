FROM python:latest

RUN git clone https://github.com/AssiNET/rest-api-tests-action.git

WORKDIR /rest-api-tests-action

RUN pip install pytest pytest-html requests

CMD ["python", "runner.py", "--set", "smoke_test"]

#docker build -t python-script
#docker run -d -t python-script
#cp dd0b13f106309839324d:/rest-api-tests-action/results/latest C:\rest-api-tests-action\dock_poc