## Unit

# Azure

* **What are the primary benefits of using cloud computing over traditional on-premises infrastructure?**
  * The cloud provides scalability, flexibility, and cost-efficiency. It allows businesses to pay only for what they use, scale resources up or down quickly, and reduce the overhead of maintaining physical hardware. It also enhances reliability through redundancy and offers access to global infrastructure.

* **What are the 3 types of cloud service models?**
    * IaaS (Infrastructure as a Service): Provides virtualized computing resources over the internet. Example: Azure VMs.

    * PaaS (Platform as a Service): Provides a platform allowing customers to develop, run, and manage applications. Example: Azure App Service.

    * SaaS (Software as a Service): Delivers software applications over the internet on a subscription basis. Example: Microsoft 365.

    * **Alternative phrasing: What is the difference between IaaS, PaaS, and SaaS?**

* **What is Azure SQL Database?**
  * Azure SQL Database is a fully managed relational database service provided by Microsoft Azure. It allows you to deploy, manage, and scale relational databases in the cloud.

* **Why would you choose Azure SQL over setting up your own database on a virtual machine?**
  * Azure SQL is a fully managed PaaS offering that handles backups, patching, scaling, and high availability, reducing the need for manual maintenance. It also provides built-in security features and better performance tuning.

* **What is autoscaling in cloud environments, and why is it beneficial?**
  * Autoscaling automatically adjusts the number of compute resources based on current demand. It helps optimize cost and performance by ensuring enough resources are available during traffic spikes and scaling down during low usage.

* **What is serverless computing, and how does Azure Automation offer advantages over traditional VMs?**
  * Serverless computing allows you to run code without provisioning or managing servers. Azure Automation simplifies task automation by running scripts on demand or on a schedule, reducing the need for maintaining persistent VM infrastructure and improving cost-efficiency.

* **Why are logging, monitoring, and alerting important in cloud applications?**
  * They provide visibility into application health, performance, and potential issues. Logging helps in debugging, monitoring helps in performance analysis, and alerting ensures that incidents are detected and responded to quickly.

* **What types of data can Azure Monitor collect from applications?**
  * Azure Monitor can collect metrics (e.g., CPU usage), logs (e.g., application traces), diagnostic data, and telemetry from Azure resources, applications, and the operating system. It helps in gaining insights into system behavior and performance.

* **What is Infrastructure as Code, and how does Azure Resource Manager (ARM) support it?**
  * Infrastructure as Code (IaC) is the practice of managing infrastructure through code instead of manual processes. ARM templates allow users to define Azure infrastructure declaratively in JSON or Bicep files, enabling consistent, repeatable deployments.

* **What are the benefits of using Azure Resource Manager to manage cloud infrastructure?**
  * ARM provides a centralized management layer, supports role-based access control, enables template-based deployment, and allows grouping resources logically for easier management and cost tracking.


## Challenge Questions

* **What’s the difference between Azure’s Hot and Cool storage tiers, and when would you use each?**
  * Hot tier is optimized for frequent access with higher storage cost and lower access cost. Cool tier is for infrequent access, with lower storage cost and higher access cost. Use hot for active data and cool for archived or rarely accessed data.

* **What is a container registry, and why is it useful in a DevOps pipeline?**
  * A container registry stores and manages container images. It allows version control, secure access, and integration into CI/CD pipelines. Azure Container Registry (ACR) enables easy deployment of containerized applications across environments.

* **What are the advantages of using Azure Kubernetes Service (AKS) instead of managing Kubernetes on VMs manually?**
  * AKS is a managed Kubernetes service that handles tasks like cluster upgrades, patching, and scaling. It simplifies setup and operations, enhances security, and integrates with Azure’s ecosystem, reducing administrative overhead.

* **How can Azure Pipelines be used to implement CI/CD for a software project?**
  * Azure Pipelines automate the build, test, and deployment processes. They support multiple languages and platforms, integrate with GitHub or Azure Repos, and allow defining pipelines as code (YAML), facilitating consistent and repeatable deployments.

