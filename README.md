# LinkedIn_Data_Puller
## General
* Cert and Cred data in env vars
* Run `init.py` to pull profile data and et to Firebase.

## Run the following to Deploy
* Login first with 
    * `aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 832214191436.dkr.ecr.ap-south-1.amazonaws.com`
* One time 
    * `aws ecr create-repository --repository-name linkedindatapuller`
* Build docker image with 
    * `docker build -t linkedindatapuller .`
* `docker tag linkedindatapuller:latest 832214191436.dkr.ecr.ap-south-1.amazonaws.com/linkedindatapuller:latest`
* `docker push 832214191436.dkr.ecr.ap-south-1.amazonaws.com/linkedindatapuller:latest`