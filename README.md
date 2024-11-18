# Kubernetes-Based Application Hosting and Monitoring System  

## Overview  
This project demonstrates the deployment and monitoring of containerized applications using Kubernetes, showcasing skills in container orchestration, monitoring, and performance benchmarking. The workflow involves deploying applications, simulating load, and visualizing performance metrics using tools like Grafana and Prometheus.  

## Features  
- **Kubernetes Dashboard Deployment**: Configure and access the Kubernetes dashboard for managing cluster resources.  
- **Application Hosting**: Deploy a Java-based benchmarking application using Kubernetes resources such as Deployments and Services.  
- **Load Simulation**: Generate workload using a Python-based load generator to simulate real-world traffic.  
- **Monitoring and Observability**: Integrate Kubernetes monitoring stack with Prometheus, Grafana, and Metrics Server for real-time insights into resource usage.  
- **Performance Visualization**: Use Grafana to create dashboards for CPU and memory usage metrics and evaluate application performance under load.  

## Technologies Used  
- **Kubernetes**: For container orchestration and resource management.  
- **Docker**: For containerization of applications and load generator.  
- **Prometheus and Grafana**: For monitoring and visualization of system performance.  
- **Python**: For building a load generator.  
- **MicroK8s**: For setting up a lightweight Kubernetes cluster.  

## Project Structure  
- `deployment.yaml`: Kubernetes deployment file for the Java-based benchmarking application.  
- `loadgeneratorservice.yaml`: Kubernetes manifest file for deploying the load generator.  
- `load_generator.py`: Python script for simulating application load.  
- `dockerfile`: Dockerfile for containerizing the load generator script.  
- `grafana-dashboard.json`: Configuration file for setting up Grafana dashboards.  

## Getting Started  

### Prerequisites  
- Kubernetes cluster (MicroK8s or any Kubernetes distribution)  
- Docker installed on the local machine  
- Python 3.6+  
- Prometheus and Grafana installed on the cluster  

### Steps to Run the Project  

1. **Set Up Kubernetes Dashboard**:  
   - Deploy the dashboard using the following command:  
     ```bash
     kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
     ```  
   - Create a service account and cluster role binding as per the included YAML files.  
   - Access the dashboard using the token generated.  

2. **Deploy Java Application**:  
   - Apply the `deployment.yaml` file to deploy the Java benchmarking application:  
     ```bash
     kubectl apply -f deployment.yaml
     ```  
   - Expose the application using a NodePort service for external access.  

3. **Set Up Monitoring Tools**:  
   - Enable observability add-ons in MicroK8s:  
     ```bash
     microk8s enable observability
     ```  
   - Edit the Grafana service to use a NodePort and access it via `localhost:31000`.  

4. **Load Simulation**:  
   - Build the load generator Docker image:  
     ```bash
     docker build -t load-generator .
     ```  
   - Push the image to a local registry:  
     ```bash
     docker tag load-generator localhost:32000/load-generator
     docker push localhost:32000/load-generator
     ```  
   - Deploy the load generator service:  
     ```bash
     kubectl apply -f loadgeneratorservice.yaml
     ```  

5. **Visualize Metrics**:  
   - Access Grafana at `localhost:31000` and configure dashboards using `grafana-dashboard.json`.  
   - View CPU and memory usage metrics for the deployed application and load generator.  

## Results  
- The Grafana dashboard displays real-time metrics for CPU and memory usage of the deployed application under load.  
- Benchmarking results include response times and failure counts from the load generator.  

## Future Enhancements  
- Integrate auto-scaling for applications based on resource utilization.  
- Experiment with additional workloads and monitoring tools.  
- Add support for multi-cluster deployments.  
