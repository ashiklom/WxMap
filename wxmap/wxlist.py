#! /usr/bin/env python

import os
import sys
import copy

from .lib import wxservice
from .lib import interface

from .lib.request import Request
from .lib.taskmanager import TaskManager

if __name__ == "__main__":

    request = Request(interface.parse_args(sys.argv[1:]))

    wx = wxservice.WXService(request)
    #wx = wxservice.WXServiceLite(request)

    print("\n", 'default', ":\n")

    for k,v in wx.config('default',{}).items():
    print(k, ":", v)

    response = wx.get_capabilities()

    for key in response:

        result = response[key]
        print("\n", key, ":\n")

        if isinstance(result, list):
            print(result)
        else:
            for k,v in result.items():
                print(k, ":", v)

