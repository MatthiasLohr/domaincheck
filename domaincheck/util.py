
def parent_domain(domain):
    return '.'.join(domain.split('.')[1:])


def absolute_domain(domain):
    return domain.rstrip('.') + '.'
