#! /usr/bin/env python

import os
import sys
import json

from .lib import wxservice
from .lib import interface

from .lib.request import Request

def main():

    request  = Request(interface.parse_args(sys.argv[1:]))
    wx       = wxservice.WXService(request)

    bin_name = request.get_key()
    bin_path = wx.config('bin_path', './')
    bin_path = os.path.join(bin_path, bin_name)

    print(bin_path)

    try:
        os.makedirs(bin_path, 0o755)
    except Exception:
        pass

    playlist = wx.playlist()

    i = 0
    for play in playlist:

        file = 'wx%03d.json'%(i) 
        file = os.path.join(bin_path, file)
        print(file)

    #   wx.config['plotservice_'] = wx.ps
    #   wx.config['theme_'] = wx.ps.name
        wx.config.serialize(wx.config)
        with open(file, 'w') as outfile:
            json.dump(wx.config, outfile)

        i += 1

if __name__ == "__main__":
    main()
