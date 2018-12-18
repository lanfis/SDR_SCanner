#!/usr/bin/env python
# license removed for brevity
from __future__ import division

import os
import sys
current_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_folder)
main_folder = os.path.join(current_folder, "..")
sys.path.append(main_folder)

import numpy as np
import time
from rtlsdr import *
from utils.console_formatter import Console_Formatter

class SDR_CONTROLER:
    version_ = "1.0"
    console = Console_Formatter(__name__)
    
    sdr_serial_numbers = []
    sdr_controler = None
    
    sample_rate = None
    center_freq = None
    gain = None
    
    samples = None    
    is_plot = False
    
    def __init__(self):
        #print(self.console.INFO("Initializing ..."))
        self.sdr_serial_numbers = RtlSdr.get_device_serial_addresses()
        
    def __del__(self):
        if self.sdr_controler != None:
            self.sdr_controler.close()
            
    def __call__(self, interface_number=None, sample_rate=2.4e6, center_freq=98.9e6, gain=2):
        return self.init(interface_number, sample_rate, center_freq, gain)
        
    def run(self, sample_size=256*1024):
        if self.sdr_controler == None:
            return None
        self.samples = self.sdr_controler.read_samples(sample_size)
        return self.samples
    
    def get_device_serial_numbers(self):
        return self.sdr_serial_numbers
        
    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.sdr_controler.sample_rate = self.sample_rate
        
    def set_center_freq(self, freq):
        self.center_freq = freq
        self.sdr_controler.center_freq = self.center_freq
        
    def set_gain(self, gain):
        self.gain = gain
        self.sdr_controler.gain = self.gain
        
    def init(self, interface_number=None, sample_rate=2.4e6, center_freq=98.9e6, gain=2):
        interface_number = 0 if interface_number == None else interface_number
        #print(self.console.INFO("Using device : {} ...".format(self.sdr_serial_numbers[interface_number])))     

        #print(self.console.INFO("Starting ..."))
        self.sdr_controler = RtlSdr(serial_number=self.sdr_serial_numbers[interface_number])
        self.set_sample_rate(sample_rate)
        self.set_center_freq(center_freq)
        self.set_gain(gain)
        return
        
def main(**kwargs):
    sdr = SDR_CONTROLER()

    sdr.init()
    for i in range(10):
        print(sdr.run())

if __name__ == "__main__":
    args = sys.argv[1:]
    kwargs = {}
    for i in range(0, len(args),2):
        kwargs[args[i]] = args[i+1]
    main(**kwargs)

