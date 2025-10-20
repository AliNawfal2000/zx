import hashlib
import urllib.request
import getpass

def check_password(password):
    s = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = s[:5], s[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    req = urllib.request.Request(url, headers={"User-Agent": "pw-check"})
    with urllib.request.urlopen(req, timeout=10) as r:
        data = r.read().decode('utf-8')
    for line in data.splitlines():
        h, count = line.split(':')
        if h == suffix:
            return int(count)
    return 0

if name == "__main__":
    pw = getpass.getpass("Enter password to check: ")
    c = check_password(pw)
    if c:
        print(f"Compromised! Found {c} times.")
    else:
        print("Not found in dumps. (Likely safe)")