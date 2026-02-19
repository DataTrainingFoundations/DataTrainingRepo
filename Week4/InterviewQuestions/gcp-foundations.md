## Unit

# GCP Foundations

## Links

## Required Questions

* **What is "the cloud" or "cloud computing" and why is it so popular now?**
    * The cloud is a server farm where all of our data is being kept
    * Cloud computing is popular because it enables us to keep our data off-site so in the event there are any outages in a certain region it will not effect our operations as heavily

* **What are the 3 types of cloud service models?/ What is the difference between IaaS, PaaS, and SaaS?**
    * Infrastructure, Platform, and Software as a Service
    * *IaaS*: direct access to hardware; most control
    * *PaaS*: hardware abstracted; developer provides the software to run
    * *SaaS*: software abstracted

* **What are the different ways of interacting with GCP?**
  * Web console (GUI)
  * SDK
  * Command line tool (`gcloud` CLI)
  * Cloud Shell

* **What is the difference between a GCP region and a zone?**
  * A GCP **region** is a specific geographical location where you can host your resources. 
  * Each **region consists of multiple zones**, which are isolated locations within that region. 
  * **Zones** are designed to be independent of each other so that any single failure event affects only a single zone. 
  * This allows you to distribute applications and storage across multiple zones to ensure redundancy and availability.


* **What is IAM in GCP and why is it important?**
  * **Identity and Access Management (IAM)** in GCP is a framework that helps you manage:
    * who has access to your GCP resources
    * what they can do with those resources
    * and what areas they have access to
  * IAM is important because it provides fine-grained control over permissions and roles, helping to enforce the principle of least privilege, which minimizes security risks by ensuring users and services have only the permissions they need to perform their tasks.


* **What are the different types of roles available in GCP IAM?**
  * GCP IAM offers three types of roles:
  * **Basic Roles**: Broad roles that existed before IAM, such as Owner, Editor, and Viewer.
  * **Predefined Roles**: Roles created and maintained by Google that provide granular permissions for specific GCP services.
  * **Custom Roles**: User-defined roles that allow you to bundle specific permissions tailored to your needs.

* **What are some features of GCP Compute Engine?**
    * On demand, scalable computing resource that follows the IaaS compute model
    * Generally used to host applications when the customer needs more control over the computing environment

* **What is Google Cloud SQL, and what are its primary use cases?**
  * Google Cloud SQL is a fully managed relational database service provided by Google Cloud. It supports popular database engines such as MySQL, PostgreSQL, and SQL Server. Primary use cases include application development, testing, and production deployments where a managed and scalable relational database is required.

* **What is the difference between the storage classes?**
  * **Standard**: for frequently accessed, "hot" data; most expensive
  * **Nearline**: less frequently accessed, ~once a month or less
  * **Coldline**: infrequently accessed, ~once per quarter or less
  * **Archival**: for data archiving, backup; least expensive.

* **What are some key requirements or limitations regarding the naming of Google Cloud Storage buckets?**
    *   GCS bucket names must be globally unique across all of Google Cloud, must contain only lowercase letters, numbers, dashes (-), underscores (_), and dots (.). They must start and end with a letter or number, be between 3 and 63 characters long (dots can extend this to 222), and cannot contain consecutive dots or dots next to dashes/underscores.

* **What is a Persistent Disk in Google Cloud, and why would you attach one to a Compute Engine instance instead of just using the instance's local SSD or boot disk for storing application data?**
    *   A Persistent Disk is a durable, block-level storage device that can be attached to Compute Engine instances. It's independent of the VM's lifecycle. You would use a Persistent Disk for application data because it provides durable storage that persists even if the VM is stopped or deleted, unlike local SSDs or boot disks (unless configured carefully). Persistent Disks can also be detached from one VM and attached to another, offer snapshots for backup, and can be resized. Local SSDs are volatile (data is lost when the VM stops) but offer very high performance, while boot disks are primarily for the operating system.

* **How does Compute Engine integrate with other GCP services for data storage and networking?**
  * Compute Engine instances seamlessly integrate with GCP services for data storage, including Cloud Storage, Cloud SQL, and Cloud Bigtable. 
  * Networking services such as Cloud VPN, Cloud Interconnect, and Cloud DNS are also available for seamless connectivity.

*   **Explain the concept of autoscaling in Google Cloud Compute Engine. What are the primary benefits of using autoscaling for a web application hosted on Compute Engine VMs?**
    *   Autoscaling automatically adjusts the number of virtual machine instances in a managed instance group (MIG) based on load. It adds instances when demand increases (scaling out) and removes them when demand decreases (scaling in). The primary benefits for a web application include: 1. Cost Optimization: You only pay for the resources you use, scaling down during low traffic periods. 2. High Availability & Performance: The application can handle spikes in traffic by scaling out, maintaining responsiveness and availability during peak loads. 3. Reduced Operational Overhead: You don't need to manually monitor load and provision/deprovision instances.

*   **When provisioning a new Compute Engine instance, what is the significance of specifying the 'machine type' and the 'OS image'? How do network settings typically tie into the instance configuration?**
    *   The 'machine type' defines the virtual hardware resources allocated to the instance, including the number of virtual CPUs, the amount of memory, and available persistent disk limits. Choosing the right machine type is crucial for performance and cost. The 'OS image' specifies the operating system that will run on the VM (e.g., Debian, Ubuntu, Windows Server) and often includes pre-installed software. Network settings involve assigning the instance to a Virtual Private Cloud (VPC) network, configuring its internal and external IP addresses, and applying network tags that can be used by firewall rules or load balancers to control traffic flow.

## Challenge Questions


*   **You are designing a storage strategy for two types of data in Google Cloud Storage: user-uploaded profile pictures that are viewed frequently, and archived financial records that must be retained for compliance but are accessed very rarely (perhaps once a year). Explain why you would choose different GCS storage classes for these two use cases, specifically comparing Standard and Coldline storage.**
    *   For user-uploaded profile pictures, which are accessed frequently and require low latency, you would choose Standard storage. Standard storage is optimized for high performance, high frequency access, and doesn't have retrieval fees or minimum storage durations, making it cost-effective for active data despite having the highest per-GB storage cost. For archived financial records, which are accessed very rarely, you would choose Coldline storage (or even Archive storage). Coldline storage has a much lower per-GB storage cost than Standard. While it has retrieval fees and a minimum storage duration (90 days for Coldline), the infrequent access means these costs are negligible compared to the storage savings over time, making it the cost-effective choice for data primarily intended for long-term retention rather than frequent access.

