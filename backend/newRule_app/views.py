from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from xml.etree.ElementTree import Element, SubElement, tostring

# def add_rule(request):
#     data = request.data
#     rule_name = data.get("rule_name")
#     source = data.get("source")
#     destination = data.get("destination")
#     services = data.get("services", ["tcp-80", "tcp-443"])

#     if not rule_name or not source or not destination:
#         return Response({"error": "Missing required parameters"}, status=400)

#     result = create_security_rule(rule_name, source, destination, services)
#     return Response(result)


class RuleView(APIView):
    def get(self,request):
        attributes = {}
        return render(request, 'home.html', attributes)

    def post(self,request):
        attributes = {}
        secret_key = settings.FIREWALL_IP
        print(secret_key)

        if request.method == 'POST':
            data = request.POST
            rule_name = data.get("rule_name")
            source = data.get("source")
            destination = data.get("destination")
            print(rule_name, source, destination)
            try:
                self.create_security_rule(rule_name, source, destination)
                return render(request, 'home.html', attributes)
            except Exception as e:
                print("An error occurred:", e)
                return render(request, 'home.html', attributes)


    
    def create_security_rule(self,rule_name, source, destination):
        BASE_URL = f"https://{settings.FIREWALL_IP}/api"
        api_key = settings.API_KEY
        SERVICES = ["service-http", "service-https"]
        APPLICATIONS = ["web-browsing"]
        ACTION = "allow"
        SRC_ZONE = "trust"
        DST_ZONE = "untrust"
        DESCRIPTION = "This is a test rule"
        device_name = 'Palo Alto Next Gen Firewall V10.1' 
        vsys_name = 'vsys1'
        # XPath for Security Rules
        xpath = f"/config/devices/entry[@name='{device_name}']/vsys/entry[@name='{vsys_name}']/rulebase/security/rules"

        # XML Payload
        element = f"""
        <entry name="{rule_name}">
            <source><member>{source}</member></source>
            <destination><member>{destination}</member></destination>
            <service>{"".join([f"<member>{service}</member>" for service in SERVICES])}</service>
            <application>{"".join([f"<member>{app}</member>" for app in APPLICATIONS])}</application>
            <action>{ACTION}</action>
            <from><member>{SRC_ZONE}</member></from>
            <to><member>{DST_ZONE}</member></to>
            <log-start>yes</log-start>
            <log-end>yes</log-end>
            <description>{DESCRIPTION}</description>
        </entry>
"""
        set_url = f"{BASE_URL}?type=config&action=set&xpath={xpath}&element={element}&key={api_key}"


        try:
            print(BASE_URL,"gggggggggggggggg", set_url)
            response = requests.post(set_url, verify=True)
            print(response,"aaaaaaa")
            print("Add Rule Response:", response.text)
            commit_url = f"{BASE_URL}/?type=commit&key={api_key}"
            commit_response = requests.post(commit_url, verify=False)
            print(commit_response,"bbbbbbbbb")
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)

