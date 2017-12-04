import os


def get_nmap(tld,option="-F"):
    command = "nmap " + option +" " + tld
    execute = os.popen(command)
    results = str(execute.read())
    return results

