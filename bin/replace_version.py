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
            version = int(f.read().decode('utf-8').strip())
    except urllib.error.URLError as e:
        print(e.reason)
    assert version != 1, 'the version should be higher than 1'
    this_script_dir = os.path.dirname(sys.argv[0])

    yml = os.path.abspath(f'{this_script_dir}/../.github/workflows/deploy.yml')
    contents: str = open(yml, 'r').read()

    matches = []

    for result in re.findall(r'bootiful-podcast-action@v.*?\w', contents):
        print('----')
        print(result)
        print(type(result))
        matches.append(result)

    assert len(matches) == 1, 'there should only be one match!'

    new_content = contents.replace(matches[0], 'bootiful-podcast-action@v%s' % version)
    with open(yml, 'w') as fp:
        fp.write(new_content)
        # fp.write ( int(version) * ' ')
