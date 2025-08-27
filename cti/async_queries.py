'import aiohttp
import asyncio

async def fetch_vt(session, ip, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": api_key}
    async with session.get(url, headers=headers) as resp:
        return await resp.json()

async def fetch_abuse(session, ip, api_key):
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
    headers = {"Key": api_key, "Accept": "application/json"}
    async with session.get(url, headers=headers) as resp:
        return await resp.json()

async def query_ip(ip, vt_key, abuse_key):
    async with aiohttp.ClientSession() as session:
        vt_task = fetch_vt(session, ip, vt_key)
        abuse_task = fetch_abuse(session, ip, abuse_key)
        vt_data, abuse_data = await asyncio.gather(vt_task, abuse_task)
        return vt_data, abuse_data

