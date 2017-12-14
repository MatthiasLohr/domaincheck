# Domain Check Tool

This script is a small tool to check the status of a domain.
It finds out whether a domain is available for registration
or has already been assigned.

## Usage Example

```bash
$ domaincheck google.com
INFO:root:google.com is used
$ domaincheck example-random-number.com                                                                                                                                                   [15:16:00]
INFO:root:example-random-number.com is available for registration

```

You can also limit the output for showing only domains available for
registration. The ```--hide-used``` flag will only show domains which
are available for registration:

```bash
$ domaincheck --hide-used google.com example-random-number.com
INFO:root:example-random-number.com is available for registration
```


## Usage Manual

```
usage: domaincheck [-h] [-i [INPUT_FILE [INPUT_FILE ...]]] [--hide-used]
                   [--hide-for-sale]
                   [domain [domain ...]]

positional arguments:
  domain                Domain name to check

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT_FILE [INPUT_FILE ...]], --input-file [INPUT_FILE [INPUT_FILE ...]]
                        File with domain names, one domain per line
  --hide-used
  --hide-for-sale
```


## Future Ideas

 * Check if a domain is for sale (eg. at SEDO, some first lines of
   code already there).
