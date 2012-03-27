#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Author: posativ <info@posativ.org>
Date  : 20. July 2010
Revision: 1

This software can be redistributed and modified under the following restricitons:
1. name the author
2. no commercial use
3. publish any modification

Requirements: python>=2.4 <http://python.org/>, wuala <http://wuala.com/>, root-permissions
Optional    : dtach <http://dtach.sourceforge.net/>
'''

import re
from os import popen
from sys import argv
from time import time, localtime, strftime, sleep

cmd = 'cd ~/wuala; ./wuala > /dev/null &'
#cmd = 'cd ~/wuala; dtach -n ~/dtach ./wuala' #  if you want to use dtach

def ps(user):
    '''returns pid of wuala'''
    s = popen('ps -Fu %s | grep loader[0-9].jar | grep -v grep' % user)
    for line in s:
        m = re.match('%s +(\d+)' % user, line.strip())
        if m:
            return int(m.group(1))
    return None

def kill(user):
    '''kill -9 pid'''
    pid = ps(user)
    killseq = 'kill -9 %s' % pid
    if pid:
        popen("su %s -c '%s'" % (user, killseq))
        sleep(1)

def start(user, cmd):
    '''launch wuala using dtach'''
    popen("su %s -c '%s'" % (user, cmd))

def loop(user):
    '''main loop: checks every 60 seconds, if wuala is running. If not, it will launch wuala'''
    while True:
        if not ps(user):
            print '%s:: restart' % strftime('%Y.%m.%d-%H:%M', localtime(time()))
            start(user, cmd)
        sleep(60*1)

if __name__ == '__main__':

    if len(argv) == 2:
        loop(argv[1])
    elif len(argv) > 2:
        if argv[1] == 'status' and len(argv) == 3:
            print ps(argv[2])
        elif argv[1] == 'kill' and len(argv) == 3:
            kill(argv[2])
    else: print 'usage: %s user' % argv[0]