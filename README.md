# Project-assignment
SDEV-Project
# Project Assignment - Management UI

This project contains a management user interface (UI) for an application. The main program, `login.py`, is located in the following folder:
`Project-assignment/UI-Design/combined/`

   

## Application Preview

![Application Preview](images/application-dashboard.jpg)
![Application Preview](images/application-cost.jpg)
![Application Preview](images/application-workOrders.jpg)
![Application Preview](images/application-inventory.jpg)

This screenshot provides a preview of the application's user interface.



<details>
<summary>Installation</summary>

To run the application, you'll need to ensure you have the required dependencies and Python packages installed. Below are instructions for installing Python 3.9 and the necessary packages on Ubuntu 22.04:

<details>
<summary>Step 1: Update System Packages</summary>

```bash
sudo apt update
sudo apt upgrade
```
</details>

<details>
<summary>Step 2: Install Prerequisites</summary>

```bash
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```
</details>

<details>
<summary>Step 3: Download Python 3.9</summary>

```bash
wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
```
</details>

<details>
<summary>Step 4: Extract and Change Directory</summary>

```bash
tar -xf Python-3.9.7.tgz
cd Python-3.9.7
```
</details>

<details>
<summary>Step 5: Configure, Compile, and Install Python 3.9</summary>

```bash
./configure --enable-optimizations
make -j 4
sudo make altinstall
```
</details>

<details>
<summary>Step 6: Verify Installation</summary>

```bash
python3.9 --version
```
</details>

<details>
<summary>Step 7: Install Required Python Packages</summary>

```bash
pip install bcrypt==4.0.1
pip install QtAwesome==1.2.3
pip install mysql-connector-python==8.0.33
pip install cryptography==41.0.1
pip install PyQt6==6.5.1
pip install PyQt6-Charts==6.5.0
pip install PyQt6-Charts-Qt6==6.5.1
pip install PyQt6-Qt6==6.5.1
pip install PyQt6-sip==13.4.0
```
</details>

</details>
