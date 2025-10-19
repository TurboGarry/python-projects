import webbrowser as wb

def webauto():
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'  #add chrome path
    
    for url in URL:
        wb.get(chrome_path).open(url)

webauto()