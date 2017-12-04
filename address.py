import os

def get_address(tld):
    command = "host " + tld
    execute = os.popen(command)
    results = str(execute.read())
    i = results.find("address")
    return results[i+8:].splitlines()[0]
