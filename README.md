## Dockerization
1. **Clone the repository**
 git clone https://github.com/nyrahul/wisecow  

2. **Write Dockerfile**:
    ```Dockerfile
    # Use a base image that matches your application's needs (e.g., Node.js, Python)
    FROM node:14

    # Set the working directory
    WORKDIR /usr/src/app

   # Copy package.json and install dependencies
   COPY package*.json ./
   RUN npm install

   # Copy the rest of the application code
   COPY . .

   # Expose the port the app runs on
   EXPOSE 3000

   # Command to run the application
   CMD ["npm", "start"]

3. **Build the Docker image**:
    ```bash
    docker build -t wisecow-app .
    ```
4. **Test the Docker image locally**:
    ```bash
    docker run -p 3000:3000 wisecow-app
    ```

## Kubernetes Deployment

1. **Create Deployment YAML (`wisecow_app-deployment.yaml`)**:
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: wisecow-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: wisecow
      template:
        metadata:
          labels:
            app: wisecow
        spec:
          containers:
          - name: wisecow-container
            image: wisecow-app:latest
            ports:
            - containerPort: 3000    
    ```
2. **Create Service YAML (`wisecow_app-service.yaml`)**:
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: wisecow-service
    spec:
      TYPE: NodePort
      ports:
      - port: 3000
        targetPort: 3000
        nodeport: 30001
      selector:
        app: wisecow
    ```
3. **Apply the manifest files**:
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

## Continuous Integration and Deployment (CI/CD)

1. **GitHub Actions Workflow**:
   - Create `.github/workflows/ci-cd.yml`:
     ```yaml
     name: CI/CD Pipeline

     on:
       push:
         branches:
           - main

     jobs:
       build-and-deploy:
         runs-on: ubuntu-latest
         steps:
         - name: Checkout code
           uses: actions/checkout@v2
     
         - name: Set up Docker Buildx
           uses: docker/setuo-login-action@v1
          
         - name: Build and push Docker image
           uses: docker/build-push-action@v2
           with:
             context: .
             push: true
             tags: your-dockerhub-username/wisecow-app:latest
     
         - name: Deploy to kubernates
           uses: imranismail/setup-kubectl@v1
           with:
             kubectl_version: 'latest'
             kubeconfig: ${{ secrets.KUBE_CONGIG }}
     
           run |
             kubectl apply -f deployment.yaml
             kubectl apply -f service.yaml
     ```
   - Configure Docker and Kubernetes secrets in the GitHub repository settings.

## TLS Implementation

1. **Generate TLS Certificates**:
   - Use a Kubernetes Ingress Controller (like NGINX) for managing TLS.
   - Set up a certificate using Let's Encrypt or self-signed certificates.
   - Update the Ingress resource to route traffic and enable TLS.
2. **Configure TLS in Kubernetes Ingress**:
   - git add .
   - git commit -m "Initial setup"
   - git push origin main

