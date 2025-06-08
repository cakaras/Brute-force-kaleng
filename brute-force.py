#!/usr/bin/env python3
"""
Brute Force Hidden Path Finder - Pentest Tool
Usage:
    python3 bruteforce_path_finder.py -u https://example.com -w wordlist.txt -t 10

Description:
This tool attempts to find hidden directories or files on a target website by trying
paths listed in a wordlist file. It supports multithreading to speed up scanning.
"""

import argparse
import requests
import sys
import threading
import queue
from urllib.parse import urljoin
from time import sleep

# Disable SSL warnings for HTTPS sites with invalid certs
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def worker(base_url, q, results, verbose):
    while True:
        path = q.get()
        if path is None:
            break
        url = urljoin(base_url, path.strip())
        try:
            response = requests.get(url, verify=False, timeout=8, allow_redirects=True)
            status = response.status_code
            if status < 400:
                results.append((url, status))
                if verbose:
                    print(f"[+] Found: {url} (Status: {status})")
            else:
                if verbose:
                    print(f"[-] {url} (Status: {status})")
        except requests.RequestException as e:
            if verbose:
                print(f"[!] Error accessing {url}: {e}")
        q.task_done()

def main():
    parser = argparse.ArgumentParser(description="Brute Force Hidden Path Finder - Pentest Tool")
    parser.add_argument("-u", "--url", required=True, help="Base target URL (e.g. https://example.com/)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file with paths to test")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads (default: 10)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show all attempts including failed")
    args = parser.parse_args()

    base_url = args.url
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        print("[-] Please specify the URL with http:// or https://")
        sys.exit(1)

    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            paths = f.read().splitlines()
    except Exception as e:
        print(f"[-] Failed to open wordlist file: {e}")
        sys.exit(1)

    q = queue.Queue()
    results = []
    num_threads = args.threads

    print(f"[+] Starting scan on {base_url} with {num_threads} threads...")
    print(f"[+] Loaded {len(paths)} paths from wordlist")

    for path in paths:
        if path.strip():
            # Ensure path always starts without a leading slash so urljoin works cleanly
            q.put(path.lstrip("/"))

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(base_url, q, results, args.verbose), daemon=True)
        t.start()
        threads.append(t)

    try:
        # Wait for queue empty
        q.join()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user, terminating...")
        sys.exit(1)

    # Stop threads
    for _ in range(num_threads):
        q.put(None)
    for t in threads:
        t.join()

    print("\n[+] Scan completed.")
    if results:
        print("[+] Valid paths found:")
        for url, status in sorted(results, key=lambda x: x[1]):
            print(f"  {url} (Status: {status})")
    else:
        print("[-] No valid paths found.")

if __name__ == "__main__":
    main()

