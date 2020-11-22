#!/usr/bin/env python3

import os
import re
import sys
import urllib.request

if __name__ == '__main__':

    version = 1
    try:
        with urllib.request.urlopen(
                'https://raw.githubusercontent.com/bootiful-podcast/bootiful-podcast-action/main/version') as f:
            c = f.read().decode('utf-8').strip()
            print('the value is ', c)
            version=int(c)
    except urllib.error.URLError as e:
        print(e.reason)
    assert version != 1, 'the version should be higher than 1'
    this_script_dir = os.path.dirname(sys.argv[0])

    yml = os.path.abspath(f'{this_script_dir}/../.github/workflows/deploy.yml')
    contents: str = open(yml, 'r').read()

    matches = []

    for result in re.findall(r'config-client-github-action@v\d+\w', contents):
        matches.append(result)

    assert len(matches) == 1, 'there should only be one match!'
    print('Going to update deploy.yml to use version %s of the bootiful-podcast-action. ' % version)
    new_content = contents.replace(matches[0], 'config-client-github-action@v%s' % version)
    with open(yml, 'w') as fp:
        fp.write(new_content)