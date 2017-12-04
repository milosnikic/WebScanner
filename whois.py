import os

def get_whois(tld):
    command = "whois " + tld
    execute = os.popen(command)
    results = str(execute.read())
    return results