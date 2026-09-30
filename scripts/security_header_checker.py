import requests

def check_security_headers(url):
    try:
        # Send a GET request to the target URL
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        print(f"[*] Checking security headers for: {url}\n")
        
        # List of critical security headers to look for
        security_headers = [
            'Strict-Transport-Security',
            'Content-Security-Policy',
            'X-Frame-Options',
            'X-Content-Type-Options',
            'X-XSS-Protection'
        ]
        
        for header in security_headers:
            if header in headers:
                print(f"[+] [PRESENT] {header}")
            else:
                print(f"[-] [MISSING] {header} is not set.")
                
    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to {url}: {e}")

if __name__ == "__main__":
    target = input("Enter target URL (e.g., https://example.com): ")
    check_security_headers(target)
