from domain import get_domain
from address import get_address
from nmap import get_nmap
from robots import get_robots
from whois import get_whois
from write import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_information(name,url):
    domain = get_domain(url)
    ipaddress = get_address(domain)
    nmap = get_nmap(domain,'-F')
    robots = get_robots(url)
    whois = get_whois(domain)
    create_report(name, url, domain, ipaddress, nmap, robots, whois)

def create_report(name, url, domain, ipaddress, nmap, robots, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt',url)
    write_file(project_dir + '/domain.txt', domain)
    write_file(project_dir + '/ipaddress.txt', ipaddress)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots)
    write_file(project_dir + '/whois.txt', whois)

gather_information('kupindo', 'https://www.kupindo.com/')