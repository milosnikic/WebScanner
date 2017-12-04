from tld import get_tld


def get_domain(url):
    tld = get_tld(url)
    return tld
