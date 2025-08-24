import requests
import os

VT_API = os.getenv("VIRUSTOTAL_API_KEY")
ABUSE_API = os.getenv("ABUSEIPDB_API_KEY")

def query_virustotal(ip_or_domain):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_or_domain}"
    headers = {"x-apikey": VT_API}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def query_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    headers = {"Key": ABUSE_API, "Accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None

