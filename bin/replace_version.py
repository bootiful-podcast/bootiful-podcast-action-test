#!/usr/bin/env python3

import os,sys, re

if __name__ == '__main__' :
    this_script_dir   = os.path.dirname(  sys.argv[ 0] )
    version = sys.argv[1]
    print (f'the version is {version}.')
    yml = os.path.abspath (  f'{this_script_dir}/../.github/workflows/deploy.yml' )
    contents = open(yml , 'r').read()
    new_content  = contents.replace('v%s' %  (int(version)  -1) , 'v%s' % version)
    with open ( yml, 'w') as fp :
        fp.write (new_content)
        # fp.write ( int(version) * ' ')


