# Kubernetes

- Container orchestration tool, which helps in managing containerized applications in different deployment environments.

## Need for container orchestration

- Increased popularity of microservices and each microservice running as a container caused a problem in managing a large number of containers, hence the need of a tool to help with this.

## What features do orchestration tools offer?

- High availability or no downtime
- Scalability or high performance
- Disaster recovery - backup and restore

## Kubernetes Components

### Node and Pod
- **Pod**:-
  - Smallest unit of kubernetes
  - Abstraction over container
  - This abstraction is created to abstract away the container technology
  - A pod contains a running container inside it.
  - Usually one container per pod, but it is possible to run multiple containers inside one pod.
  - Kubernetes proviedes a virtual network, and each pod (not the container) gets its own IP address.
  - K8s pods can communicate with each other using the IP addresses.
  - Pod components are ephemeral (they can die very easily) and a new pod is created to take its place. When that happens, a new IP address is assigned to it on recreation.

- **Node**:-
  - The physical or virtual machine on which pods are created

- **Service**:-
  - has a permanent IP address
  - lifecycle of Pod and Service are not connected, so even if the Pod dies, the Service stays the same and hence, the IP address remains the same for the service.
  - Types:-
    - External Service -- accessible from outside the kubernetes environment
    - Internal Service

- **Ingress**:-
  - Request from outside world first comes to Ingress, and it forwards it to the service
  - Routes traffic into the K8s cluster

### ConfigMap and Secret

- **ConfigMap**:-
  - stores configuration for the applications external to the pods

- **Secret**:-
  - just like configmap, but used to store secrets like db credentials, etc.
  - not stored in plain text, stored as base64 encoded

### Volumes

- persistent storage on local or remote storage for stateful services like db to retain data

### Deployment and Stateful Set

- **Deployment**:-
  - defines blueprint for pods of a service
  - usually people work with deployments; not at the pod level
  - abstraction over Pods

- **Stateful Set**:-
  - meant for stateful apps like databases to provide replication functionalities without creating inconsistencies
  - similar to deployment, but for stateful services like databases
  - deploying database applications using Stateful Set can be tedious compared to deployments
  - common practice is to host databases outside of the kubernetes cluster (like a managed cloud service)

## Kubernetes Architecture

### Node
- Two types of Nodes:-
  - Master Node
  - Worker Node / Slave Node

  **Worker Node / Node**:-
    - Each Worker Node has multiple Pods on it
    - Worker Nodes do the actual work. Sometimes, Worker Nodes are just called Nodes.
    - 3 processes must be installed on every Worker Node
      - **container runtime** (e.g. docker)
      - **kubelet** -- interacts with container runtime and the node; it starts the pod with a container inside
      - **kube proxy** -- forwards requests from services to pods; we send requests to services, kube proxy forwards them from the service to the actual pod

  - **Master Node**
    - Master Node is responsible for managing the cluster by taking care of operations like:-
      - Scheduling pods
      - Monitoring pod health and state changes of the cluster
      - Restarting pods if they die
    - Every master node has 4 processes running on it:-
      - **api server** -- This is the interface using which any client (UI, kubectl, etc.) interacts with the kubernetes cluster. It also authenticates and validates the incoming requests before forwarding them forward.
      - **scheduler** -- Its job is to schedule pods on worker nodes (on which node this pod should run). Note that it just decides the node on which the pod should be started, the actual work of starting the pod is done by kubelet process running inside the worker node.
      - **controller manager** -- It monitors the cluster for state changes like pods dying, pods restarting, etc. If a pod has to be restarted, it calls the scheduler.
      - **etcd** -- It is a key-value store which stores the state of the cluster. Other master processes (api server, scheduler, controller manager) use the data stored here to make their decisions.
    - Since master node is a critical component of the cluster, multiple master nodes are run in the cluster by kubernetes. The api servers are load-balanced, and the etcd store forms a distributed storage across all the master nodes.
    - Master nodes require less resources than worker nodes as master nodes don't have to do the actual work (running the applications).

## Minikube and Kubectl

- **Minikube**:-
  - It is an open source tool to create a single node cluster on a local development environment
  - This is used to test kubernetes locally without creating a full-blown cluster of nodes
  - It creates a node inside a virtual box, and installs all the master processes and worker processes inside it.

- **Kubectl**:-
  - kubectl is a CLI tool used to interact with and manage a kubernetes cluster

### Basic kubectl commands

- `kubectl get <component>`, where `<component>` can be any kubenetes component like nodes, pod, deployment, service, replicaset, etc.
- `kubectl create deployment <deployment_name> --image=<image>` -- create deployments, which is a blueprint for creating pods. When we create a deployment, it creates a replicaset, which manages replicas of our pods.
  - The hierarchy of abstraction is:-
    - Deployment
    - ReplicaSet
    - Pod
    - Container
  - We only deal with deployments using kubernetes. kubernetes internally handles everything below the deployment level.
- `kubectl edit deployment` -- to edit deployment configuration file. On saving it, a new replicaset is created and new pods are created inside it. Old pods are terminated and deleted.
- `kubectl logs <pod_name>` - show pod logs
- `kubectl describe pod <pod_name>` -- Shows details about the pod, along with the state changes happening. Useful to debug a pod.
- `kubectl exec -ti <pod_name> -- /bin/sh` -- To get an interactive terminal inside the pod. Also useful in debugging a pod.
- `kubectl delete deployment <deployment_name>` -- Delete a deployment
- `kubectl apply -f <filepath>` -- Applies a kubernetes configuration file. A configuration file is used to create and manage components inside kubernetes. It is impractical to create components using the command line options, so a configuration file is used to configure all kubernetes components. For example, `kubectl apply -f 01-nginx-deployment.yaml`.
- `kubectl delete -f <filepath>` -- Delete kubernetes components using configuration file.

## Kubernetes Configuration Files

- Every k8s configuration file has 3 sections:-
  1. metadata
  2. spec
  3. status
- Every configuration file defines an apiVersion and a Kind, which is specific to each component and needs to be looked up in docs.
- metadata defines the name, labels, etc. of the component.
- spec defines the desired state of the component and differs for each component.
- status is added automatically by kubernetes when the component is created, and is automatically updated to keep track of the current status.
- kubernetes uses the status and compares it with the spec to know if there is something to do. In case there is a mismatch between the desired state and the actual state, kubernetes tries to fix it.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.24
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
        ports:
        - containerPort: 8080

```

- Above is an example of configuration file for a deployment. We can see that it has the 2 sections, `metadata` and `spec`. Inside the spec of a deployment, there's a `template` section, which defines the configuration for a pod. It also has the metadata and spec sections. It is like a configuration file inside of a configuration file.

- The metadata defines labels. These are key value pairs used to annotate components, which are used by other components to find their relevant components using selectors.
- For example, the deployment defines a label `app: nginx`, which can be used in the selector of a service to match this label. Similarly, inside the template section, we see that the label `app: nginx` is defined for each pod, and the selector in spec of the deployment specifies to match label `app: nginx`. This is how the deployment will know which pods belong to it.

## MongoDB and Mongo Express Application deployment

- The configuration files are [here](/kubernetes/demo-mongodb-and-mongoexpress/).
- The architecture of the application is as follows:-
  - We create a `mongodb-deployment` which has mongodb pod running inside it.
  - We create an internal service (by default all services are internal) called `mongodb-service`. This service forwards requests from mongoexpress pod to mongodb pod.
  - We create a secret to hold mongodb credentials. This secret is used in the mongodb deployment configuration file.
  - We create a deployment, `mongoexpress-deployment`, which deploys the mongo-express pods.
  - We create a configmap, `mongoexpress-config`, which holds the mongodb url, to which mongo-express will connect. This configmap is also referenced in the mongoexpress-deployment configuration file.
  - We create an external service (a service of type LoadBalancer), `mongoexpress-service`. This service is assigned a node IP address and a node port, through which this service can be accessed from outside the kubernetes cluster. Since minikube works a bit differently, we have to run `minikube service mongoexpress-service` in our example to access it from the browser. This creates a tunnel between localhost and the node (the virtual node which minikube has created, because the external IP assigned to the service is of the node, so we need this tunnelling). In other cases, when the cluster is on the cloud, we'll get an actual external IP and this tunnel won't be required.