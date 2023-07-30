# Machine-Learning-Project-with-MLflow-for-Wine-Quality-Prediction



## workflow

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src 
6. update the components 
7. update the pipeline 
8. update the main.py
9. update the app.py

## How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Gaurang140/Machine-Learning-Project-with-MLflow-for-Wine-Quality-Prediction.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.8 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Gaurang140/Machine-Learning-Project-with-MLflow-for-Wine-Quality-Prediction.mlflow \
MLFLOW_TRACKING_USERNAME= yourusername \
MLFLOW_TRACKING_PASSWORD= yourpassword \
python script.py

Run this to export as env variables:

```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/Gaurang140/Machine-Learning-Project-with-MLflow-for-Wine-Quality-Prediction.mlflow 

set MLFLOW_TRACKING_USERNAME= your-username 

set MLFLOW_TRACKING_PASSWORD= your-password 

```

# Azure Deployment Steps

Follow the steps outlined below to successfully deploy your application using Azure.

1. **Login to Azure**
   - Start by logging in to your Azure account with your credentials.

2. **Search for Container Registry**
   - Type "Container Registry" in the search bar. This will appear in the marketplace.

3. **Create a Container**
   - Next, create a new container. Here, you will need to create a new resource group named for example `mlflowapp` and use the same name for the registry. Choose a location near your region and click on 'Review + create', then 'Create'.

4. **Go to Resource**
   - After the creation process (which may take a few moments), you will see a button labeled 'Go to resource'. Click on it.

5. **Copy Login Server**
   - Now, goto the Access keys , copy the login server (e.g., `mlflowapp.azurecr.io`) and enable Admin User. After this, copy the password (e.g., `XUAztbIBEiAWgqLzzD/mJNNNJ7dGQ7hPbo/feR8iw3+ACRAPv68B`). Remember to safely store this password as it is important for later steps.


6. **Install Docker Desktop**
   - If Docker Desktop isn't installed on your system, make sure to install it now.

7. **Build the Docker Image**
   - Use the following command in your terminal to build your Docker image: `docker build -t mlflowapp.azurecr.io/mlflow:latest .`. After the process is complete, you can see your built image in Docker Desktop.

8. **Login**
   - Use the following command to login to Docker using your Azure credentials: `docker login mlflowapp.azurecr.io`. It will ask for a username and password. Here , The username is `mlflowapp` and the password is the one you copied from Azure in Step 5.

9. **Push the Docker Image**
   - Next, push the Docker image using this command: `docker push mlflowapp.azurecr.io/mlflow:latest`.

10.**Search for the Web App for Containers**
   - Look for the 'Web App for Containers' service and select the resource group you created earlier ('mlflowapp'). The instance should be a Docker container. Name your web app and keep the other fields as default. Click 'Next' and move to the Docker section. Select 'Single container' as an option and 'Azure Container Registry' as the image source. At this point, you need an image, which you will create in the next steps.

11. **Configure the Deployment Center**
   - In your resource, navigate to the 'Deployment Center' on the left-hand side of the screen. You will need to:
     - Select 'GitHub Actions' (Connect your GitHub if it is not already connected to Azure and choose the repository to deploy your application)
     - Select your organization
     - Choose your repository
     - Select the correct branch
     - Click on 'Preview file' to view the `workflow.yml` file for CI/CD deployment
     - Save your settings and navigate to the repository to see the `workflow.yml` file
   - On GitHub, go to the 'Actions' tab to monitor the deployment process.

12. **Launch the Application**
   - Go back to the Azure portal, click on 'Overview', and then click on the default domain link to access your application. Note that the first launch may take a while.

13. **Clean up Resources (if necessary)**
   - If you're deploying this for educational purposes, remember to delete the resources group afterward to avoid unnecessary charges.

By following these steps, you will be able to deploy your application on Azure successfully.

