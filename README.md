Run Test Framework in Docker Container
---
1) Make sure you have docker on your machine
2) Download and unzip or clone this project 
3) Execute at root level `docker build -t rest-framework-image` to build your image
4) Execute at root level `docker run -d -t rest-framework-image` to run container from the image
5) Get the results from the container
    - `docker cp %contained_id%dd0b13f106309839324d:/rest-api-tests-action/results/latest %your_local_path%`
        You will have human readable HTML Report + XML report
    - mount a volume - this is not implemented on purpose - we use Jenkins and GitHub Actions to take care of the report

Run Tests locally - 2 way of doing it:
---
1) Just run `pytest` in the project root
2) Engage the testing framework by running `python runner.py --set smoke_test`

Note: The 2nd option will engage the REST API framework.

REST API Framework key features:
---
1) The framework has a custom wrapper on top of the requests library which provides friendly logging of the requests-respose, headers, body, content
2) Special reporting mechanism consists of human-readable HTML report and XML report for Jenkins integration.
You can explore and run the showcase test by simply executing
`python runner.py --set smoke_test`
Results can be easily found in timestamped `2023-02-07_00-38-42_smoke_test` folder in the `results` directory. 
There is also latest folder for easy integration - for example with Jenkins

Run Tests in Github Actions:
---
1) Simply visit [Actions tab](https://github.com/AssiNET/rest-api-tests-action/actions) in the repo
2) Open [Rest API Framework](https://github.com/AssiNET/rest-api-tests-action/actions/workflows/rest-api-tests.yml) workflow
3) Run workflow from the button against main branch
4) Open the last currently running RUN
5) Below you can explore
    - download test results area (contains HTML REPORT + XML REPORT)
    - build summary pass/fail tests
6) Open build box with green tick
7) You can Explore all steps of the build
8) Open HTML REPORT LINK and click the link -> You will be redirected to latest human readable HTML Report hosted on GitHub Pages

Run Tests in Jenkins main/node configuration in GCP on linux with docker:
---
1) Open Jenkins CI server instance - for security reasons link in the email
2) Credentials also could be found in the email
3) Open the link of the Jenkins job ICEYE_Smoke_REST_tests
4) Hit Build Now button
5) After build finish
6) Open HTML Report from the left menu
7) Use Test Results Analyzer to explore failures for any patterns 
