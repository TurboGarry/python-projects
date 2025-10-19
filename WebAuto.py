import subprocess

def webauto():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    urls = [
        "https://x.com/home",
        "https://youtube.com"
    ]
    for url in urls:
        print(f"Opening {url}...")
        subprocess.Popen([chrome_path, url])

webauto()
