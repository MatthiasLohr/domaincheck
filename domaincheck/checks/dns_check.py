
import dns.resolver
import domaincheck
import socket


def check(domain):
    absolute_domain = domaincheck.util.absolute_domain(domain)
    parent_domain = domaincheck.util.parent_domain(absolute_domain)
    # find domain nameservers
    ns_answer = dns.resolver.query(parent_domain, 'NS')
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [socket.gethostbyname(str(r.target)) for r in ns_answer]
    try:
        resolver.query(absolute_domain, 'NS', raise_on_no_answer=False)
        return domaincheck.CheckResult.USED
    except dns.resolver.NXDOMAIN:
        return domaincheck.CheckResult.AVAILABLE
