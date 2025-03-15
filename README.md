# Palo Alto Firewall Rule Automation  

This project automates the creation of security rules in a **Palo Alto Next-Gen Firewall** using its API. The script allows HTTP (TCP 80) and HTTPS (TCP 443) traffic from `192.168.1.0/24` to `8.8.8.8/32` and commits the changes automatically. Additionally, a basic web UI is provided for input and configuration validation.

## Features  

✅ Adds a new security rule to the **Palo Alto Firewall** via API.  
✅ The rule allows **HTTP and HTTPS** traffic based on specified source and destination.  
✅ The rule is named after the user and placed **at the top of the rule base**.  
✅ Automatic **commit** after rule creation.  
✅ Simple **web UI** for input and validation.  

---

## Installation  

Ensure you have Python installed on your system. Then, run the following command to install dependencies:  

```bash
pip install -r requirements.txt

python manage.py runserver
