#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-w", "--website", dest="website", help="website you want to check")
    (options, arguments) = parser.parse_args()
    if not options.website:
        #code to handle error
        parser.error("[-] need a website to check against, use --help for more info")
    return options

def check_site(website):
    command = "openssl s_client -connect " + website + ":443 2>/dev/null | openssl x509 -noout -dates"
    output = subprocess.check_output(command, shell=True)
    output = output.decode('utf-8')
    print(output)

options = get_arguments()
check_site(options.website)
