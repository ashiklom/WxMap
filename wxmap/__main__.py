#! /usr/bin/env python

import matplotlib
matplotlib.use('Agg')

import os
import sys
from .lib import wxservice
from .lib import interface
from .lib import gradsdataservice as dataservice
from .lib import gradsmapservice as mapservice

from .lib.request import Request

if __name__ == "__main__":

    request = Request(interface.parse_args(sys.argv[1:]))

    wx = wxservice.WXService(request)
    #wx = wxservice.WXServiceLite(request)

    ds = dataservice.Service()
    ms = mapservice.Service()

    wx.register(dataservice = ds)
    wx.register(mapservice  = ms)

    playlist = wx.playlist()

    for play in playlist:

        for request in play:

            for r in request:
                opath = os.path.dirname(r['oname'])
                try:
                    os.makedirs(opath, 0o755)
                except Exception:
                    pass

                ds  = wx.renew(10)
                map = wx.get_map(r)
                print(map)
