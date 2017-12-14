
import dns.resolver
import domaincheck
import socket


def check(domain):
    absolute_domain = domaincheck.util.absolute_domain(domain)
    parent_domain = domaincheck.util.parent_domain(absolute_domain)
    # find domain nameservers
    ns_answer = dns.resolver.query(parent_domain, 'NS')
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [socket.gethostbyname(str(r.target)) for r in ns_answer]
    resolver.query(absolute_domain, 'NS')
