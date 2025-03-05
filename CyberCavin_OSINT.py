# CYBERCAVIN OSINT Kit 💀
# Top-Notch Dangerous OSINT Framework without API Keys
# Purely Custom & Crisp by CYBERCAVIN

import requests
import socket
import json
import whois
import dns.resolver
import re
from bs4 import BeautifulSoup
import hashlib
from waybackpy import WaybackMachineSaveAPI as WaybackMachineSearch

# Banner
def banner():
    print("""
    ██████╗ ██╗   ██╗██████╗ ███████╗██╗ ██████╗ ██╗   ██╗
    ██╔══██╗██║   ██║██╔══██╗██╔════╝██║██╔════╝ ██║   ██║
    ██║  ██║██║   ██║██████╔╝█████╗  ██║██║  ███╗██║   ██║
    ██║  ██║██║   ██║██╔══██╗██╔══╝  ██║██║   ██║██║   ██║
    ██████╔╝╚██████╔╝██║  ██║███████╗██║╚██████╔╝╚██████╔╝
    CYBERCAVIN OSINT KIT 💀 - Topnotch VINOD
    """)

# WHOIS Lookup
def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        print(f"[+] WHOIS Data for {domain}:")
        print(info)
    except:
        print("[-] WHOIS Lookup Failed")

# Subdomain Finder
def subdomain_finder(domain):
    print(f"[+] Subdomains for {domain}:")
    subdomains = ["www", "mail", "ftp", "dev", "test"]
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"[+] Found: {url}")
        except:
            pass

# DNS Lookup
def dns_lookup(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        print(f"[+] DNS Records for {domain}:")
        for ip in result:
            print(ip)
    except:
        print("[-] DNS Lookup Failed")

# IP Lookup
def ip_lookup(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = json.loads(response.text)
        print(f"[+] IP Info for {ip}:")
        for key, value in data.items():
            print(f"{key}: {value}")
    except:
        print("[-] IP Lookup Failed")

# Google Dork Search
def google_dork(dork):
    print(f"[+] Google Dork: {dork}")
    print("https://www.google.com/search?q=" + dork)

# Hash Cracking (MD5)
def hash_crack(hash):
    try:
        url = f"https://hashes.com/en/decrypt/hash?hash={hash}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find("td", {"class": "decrypted"})
        if result:
            print(f"[+] Hash Cracked: {result.text}")
        else:
            print("[-] Hash Not Found")
    except:
        print("[-] Hash Cracking Failed")

# Wayback Machine Lookup
def wayback_lookup(domain):
    try:
        search = WaybackMachineSearch(domain)
        urls = search.search_urls()[:10]
        print(f"[+] Wayback Machine URLs for {domain}:")
        for url in urls:
            print(url)
    except:
        print("[-] Wayback Lookup Failed")

# Main Function
def main():
    banner()
    target = input("[+] Enter Target Domain: ")
    whois_lookup(target)
    subdomain_finder(target)
    dns_lookup(target)
    try:
        ip = socket.gethostbyname(target)
        ip_lookup(ip)
    except:
        print("[-] IP Lookup Failed")
    google_dork(f"site:{target}")
    hash = input("[+] Enter Hash (MD5) for Cracking: ")
    if hash:
        hash_crack(hash)
    wayback_lookup(target)

if __name__ == '__main__':
    main()
