# Manually Deploy Application to AWS App Runner and AWS ECR

## Prerequisites
- AWS CLI installed and configured. Refer [this](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html).
- IAM role with ECR and App Runner permissions. Refer [this](https://docs.aws.amazon.com/apprunner/latest/dg/security_iam_id-based-policy-examples.html).
- Docker installed. Refer [this](https://docs.docker.com/get-docker/).

## Steps
1. Create a repository in ECR. Refer [this](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html).
<img width="1253" alt="image" src="https://user-images.githubusercontent.com/57321948/198867205-68a9288a-23a0-438c-baf5-be48557b216f.png">

2. Build the docker image and push it to ECR. Refer [this](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html).
<img width="750" alt="image" src="https://user-images.githubusercontent.com/57321948/198867235-ef4c4dcc-c3cb-47e6-ab13-a1f88131e01b.png">
<img width="1219" alt="image" src="https://user-images.githubusercontent.com/57321948/198867240-03f44fad-ab12-4dd0-a61a-3ff23d73528d.png">

3. Create a service in App Runner. Refer [this](https://docs.aws.amazon.com/apprunner/latest/dg/getting-started-create-service.html).
4. Select the repository created in step 1.
5. Change deployment settings as per your requirements. Refer [this](https://docs.aws.amazon.com/apprunner/latest/dg/deployment-settings.html).
6. Change Service settings as per your requirements. Refer [this](https://docs.aws.amazon.com/apprunner/latest/dg/service-settings.html).
7. Give a Service Name.
8. Assign Virtual CPU and Memory and change the PORT.
9. Click on Create and deploy the service.
10.Wait for Your web application to be deployed.
<img width="1235" alt="image" src="https://user-images.githubusercontent.com/57321948/198867252-b12d4826-3001-440b-8b13-3e5d70c0b8d3.png">

You can also Deploy using GitHub Actions refer [this](https://aws.amazon.com/blogs/containers/deploy-applications-in-aws-app-runner-with-github-actions/).
