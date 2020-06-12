#!/bin/python3

import sys
import json

TOOLS_PATH = 'tools/'
tools = ['ffuf',
         'hakrawler',
         'eyewitness']

def dprint(tool_name):
    """
        PARAM:
            tool_name: str
        Default print.
    """
    with open(''.join([TOOLS_PATH, tool_name,".json"]),'r') as f:
        tool = json.loads(f.read())
    print(tool['example'])
    for example in tool['examples']:
        print('\n*{}\n {}'.format(example['desc'],example['command']))

def main():
    tools.sort()
    if len(sys.argv) == 1:
        print('\n'.join(tools))
    elif len(sys.argv) == 2:
        dprint(sys.argv[1])
    else:
        print("Wrong number of params.")


if __name__ == "__main__":
    main()
