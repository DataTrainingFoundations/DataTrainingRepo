# Spark Installation Instructions

## Pre-Installation Steps:
```
sudo apt-get update
sudo apt-get install python3-pip
sudo apt install openjdk-17-jdk
```

## 1) Download and untar Spark binaries

```
wget https://dlcdn.apache.org/spark/spark-4.0.2/spark-4.0.2-bin-hadoop3.tgz

tar -xvzf spark-4.0.2-bin-hadoop3.tgz
```

## 2) Move spark directory

```
cd ~

sudo mv spark-4.0.2-bin-hadoop3 /opt/spark
```

## 3) Setup environment variables

```
sudo vim ~/.bashrc
```

Place theses exports at the bottom of the file:

```
export SPARK_HOME=/opt/spark
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin:$JAVA_HOME
```

Save and exit, then source the bashrc file:

```
source ~/.bashrc
```

## 4) Install python (if not installed)
Install pip3 as well.

```
sudo apt install python3 -y
sudo apt install python3-pip -y

sudo apt install python3.12-venv
```

## 5) Install pySpark using pip

```
python3 -m venv ./pysparkFun
cd pysparkFun/bin
source activate
pip3 install pyspark
```