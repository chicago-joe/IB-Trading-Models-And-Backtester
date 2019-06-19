# --------------------------------------------------------
# Author: James Ma
# Email stuff here: jamesmawm@gmail.com
#
# Developed and updated by Joseph Loss on 6/19/2019
# MS Financial Engineering
# University of Illinois at Urbana-Champaign
#
# Inquiries: loss2@illinois.edu
# --------------------------------------------------------

class StockTick:
    def __init__(self):
        self.bid_price = 0
        self.ask_price = 0
        self.last_price = 0
        self.last_volume = 0
        self.volume = 0
        self.bid_volume = 0
        self.ask_volume = 0