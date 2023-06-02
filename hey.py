#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


def main():
    if len(sys.argv) != 2 or sys.argv[1] != 'helloworld':
        print("Invalid input. Please type 'helloworld'")
        return
    
    print("Hello, World!")

if __name__ == '__main__':
    main()
