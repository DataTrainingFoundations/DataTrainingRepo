## Unit

# AWS Fundamentals

* **How would you describe AWS?**
  * Keywords, concepts, or topics that should be in the response:
    * AWS is leading cloud platform, they manage many physical data centers
    * Provides computing resources, services, infrastructure on demand through remote access
  * Possible follow-up questions
    * **What are the advantages to using AWS?**
      * No need to manage infrastructure
      * Useful tooling
      * Worldwide distribution/deployment
    * **What are some downsides to using AWS?**
      * Locked into the AWS ecosystem

* **What is "the cloud" or "cloud computing" and why is it so popular now?**
  * The cloud is a server farm where all of our data is being kept
  * Cloud computing is popular because it enables us to keep our data off-site so in the event there are any outages in a certain region it will not effect our operations as heavily

* **What are the 3 types of cloud service models?**
  * Keywords, concepts, or topics that should be in the response:
    * Infrastructure, Platform, and Software as a Service
    * IaaS: direct access to hardware; most control
    * PaaS: hardware abstracted; developer provides the software to run
    * SaaS: software abstracted
  * Possible follow-up questions
    * **Alternative phrasing: What is the difference between IaaS, PaaS, and SaaS?**
    * **What AWS services fall in these categories? Can you name some?**

* **What are the configuration options for EC2?**
  * Keywords, concepts, or topics that should be in the response:
    * AMI
    * EBS
    * Security group
    * Instance size
    * Tagging
    * Possible follow-up questions
      * What are the different EC2 instance sizes/types?
        * General purpose
        * Compute optimized (more CPU)
        * Memory optimized (more RAM)
        * Storage optimized (more I/O)
        * Sizes: nano, micro, small, medium, large, xlarge

* **Once you create an EC2, how to connect to it?**
  * Keywords, concepts, or topics that should be in the response:
    * Need `.pem` key and IP / domain; connect over `ssh`
    * Also ensure in the security group that the port is open for SSH access and your IP is whitelisted

* **What are Security Groups? When defining a rule for a security group, what 3 things do you need to specify?**
  * Keywords, concepts, or topics that should be in the response:
    * Control access to a particular resource
    * IP address (or range), port, protocol
    * Possible follow-up questions
      * Can you attach more than one security group to an EC2 instance? Ans: yes
      * Can you attach a security group to > 1 EC2 instance? Ans: yes

* **What is EC2 Instance Store?**
  * The EC2 Instance Store is temporary block storage for EC2 instances, providing high-performance storage that is directly attached to the instance.
  * Instance store volumes are ephemeral, meaning they are temporary and data is lost if the instance is stopped, terminated, or fails.
  * *Use Cases*:
    * Suitable for temporary data that doesn’t need to persist (e.g., scratch data, caches, or buffers).
    * Workloads that require high-speed, low-latency access to data, such as batch processing, and data logging.

* **What's an RDS?**
  * Keywords, concepts, or topics that should be in the response:
    * Relational database service - a PaaS offering that loads RDBMS software based on your configuration

* **What security configurations are available for AWS RDS?**
  * AWS RDS provides several security features and configurations to protect your managed database instances and data:
    * Network Security
    * Encryption
    * Authentication and Access Control
    * Database Auditing
    * Parameter Groups and Options

* **What is the S3 service?**
  * Keywords, concepts, or topics that should be in the response:
    * Simple storage service - cloud storage for static files and assets
    * Very scalable and can hold large amounts of data

* **What kind of data would you store on S3 vs a database?**
  * Keywords, concepts, or topics that should be in the response:
    * Database: relational data, application-specific, not static assets
    * S3: object storage (files); static assets like images, videos, text documents, etc.
    * Example: for an application, store username, password, address, and URL link to profile pic in database; actual profile pic stored in S3

* **What is AWS CLI?**
  * Keywords, concepts, or topics that should be in the response:
    * It's a tool to manage all AWS services from a single command based interface just like the terminal in our computers

* **What's the difference between a Region and an Availability Zone (AZ)?**
  * Keywords, concepts, or topics that should be in the response:
    * Regions cover a geographic area, all over the world
    * AZs are individual data centers; 3 AZs per region for redundancy and fault tolerance

* **How are you charged for using AWS services? Does it vary by service?**
  * Keywords, concepts, or topics that should be in the response:
    * By uptime, data stored, data exchanged

* **Different ways to interact with AWS services?**
  * Keywords, concepts, or topics that should be in the response:
    * Web console / UI
    * AWS CLI / REST API
    * AWS SDK

* **What are some features of the AWS CLI?**
  * Keywords, concepts, or topics that should be in the response:
    * Launch AWS services
    * Run scripts
    * Access AWS Services
    * Manage AWS Cloud Infrastructure

* **What are some benefits of AWS CLI?**
  * Keywords, concepts, or topics that should be in the response:
    * Very simple
      * Nothing complex, simply download AWS CLI and then install and configure
    * Saves time
      * If we want to check all of our S3 buckets then we don't have to login to AWS through a browser, simply type in a command and get the list
    * Run scripts
      * We can run powerful scripts to automate the cloud infrastructure however we want, either partially or fully
    * Access all of AWS Services
      * We can manage every service on AWS through the AWS CLI

## Challenge Questions

* **What's the difference between scalability, elasticity, and resiliency?**
  * Keywords, concepts, or topics that should be in the response:
    * Scalability is a characteristic of cloud computing through which increasing workload can be handled by increasing in proportion the amount of resource capacity. It allows the architecture to provide on demand resources if the requirement is being raised by the traffic.
    * Elasticity is the concept of commissioning and decommissioning of large amount of resource capacity dynamically. It is measured by the speed by which the resources are coming on demand and the usage of the resources.
    * Resiliency refers to the ability to recover from a disaster or outage

* **What is autoscaling?**
  * Keywords, concepts, or topics that should be in the response:
    * Autoscaling is a feature of AWS which allows you to configure and automatically provision and spin up new instances without the need for your intervention.
    * You do this by setting thresholds and metrics to monitor. When those thresholds are crossed a new instance of your choosing will be spun up, configured, and rolled into the load balancer pool.
    * You can scaled horizontally without any operator intervention.

* **What is the difference between a bucket and an object for AWS S3?**
  * Keywords, concepts, or topics that should be in the response:
    * Objects are stored inside buckets

* **What are the different storage tiers?**
  * Keywords, concepts, or topics that should be in the response:
    * `Standard`
      * Frequently used objects
    * `Standard-IA`
      * Infrequently used objects
    * `Intelligent-tiering`
      * Designed to optimize storage costs by choosing Standard and Standard-IA for objects
    * `One Zone-IA`
      * Infrequently used objects and non-mission-critical data
    * `Glacier`
      * Long-term data archiving with retrieval times ranging from minutes to hours
    * `Deep Archive`
      * Archiving and rarely accessing with retrieval times averaging 12 hours

* **Can you use S3 to host a front-end or back-end of an application?**
  * Keywords, concepts, or topics that should be in the response:
    * Front-end (static site hosting)

* **What is AWS ECR?**
  * Keywords, concepts, or topics that should be in the response:
    * Elastic Container Registry
    * Amazon's place to keep docker images
  * Possible follow-up questions:
    * **What is it used for?**
      * We can deploy application images and artifacts anywhere
