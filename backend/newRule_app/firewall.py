# import requests

# def create_security_rule(rule_name, source, destination, services):
#     url = "https://52.22.171.18/api/security-rules"
#     headers = {"Content-Type": "application/json",
#                "X-PAN-KEY":"LUFRPT1wZ2Z6VXFOOGYzUllkekE2YUVkWjFIK2J6cnc9YkdLOXRaSmNRZjZZcmFNSFc1TkpYUnZHTlNIUzkxZEVseGxZazQrWFF5RzNIY3N0VXpyeVJtY1JwRXQ5NkEwVA"
#                }
#     data = {
#         "rule_name": rule_name,
#         "source": source,
#         "destination": destination,
#         "services": services
#     }

#     try:
#         response = requests.post(url, json=data, headers=headers, verify=False)  # Disable SSL verification (for debugging)
#         print(f"Response Status: {response.status_code}")
#         print(f"Response Text: {response.text}")  # Debug the actual response

#         if response.status_code == 200:
#             return response.json()
#         else:
#             return {"error": f"Request failed with status {response.status_code}", "details": response.text}

#     except requests.exceptions.RequestException as e:
#         print(f"Request Exception: {e}")
#         return {"error": "Request failed", "details": str(e)}


import requests
import xml.etree.ElementTree as ET

from django.conf import settings



xpath = f"/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='{RULE_NAME}']"
element = f'''
<source><member>{SRC_IP}</member></source>
<destination><member>{DST_IP}</member></destination>
<service>{"".join([f"<member>{service}</member>" for service in SERVICES])}</service>
<application><member>web-browsing</member></application>
<action>{ACTION}</action>
<from><member>{SRC_ZONE}</member></from>
<to><member>{DST_ZONE}</member></to>
''' 

