#!/usr/bin/env python
# license removed for brevity
from __future__ import division

import os
import sys
current_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_folder)
main_folder = os.path.join(current_folder, "..")
sys.path.append(main_folder)

from modules import *

import numpy as np
import time
from rtlsdr import *
from utils.console_formatter import Console_Formatter

from scipy import signal
import seaborn as sns
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.mlab import psd

class VIEWER:
    version_ = "1.0"
    console = Console_Formatter(__name__)
    
    sdr_controlers = []
    
    sdr_controler_ptr_ = None
    
    is_plot = False
    
    def __init__(self):
        print(self.console.INFO("Detecting ..."))
        self.sdr_controler_ptr_ = SDR_CONTROLER()
        print(self.console.INFO("Found {} devices ...".format(len(self.sdr_controler_ptr_.get_device_serial_numbers()))))
        
        print(self.console.INFO("Initializing ..."))
        for i in range(len(self.sdr_controler_ptr_.get_device_serial_numbers())):
            sdr = SDR_CONTROLER()
            sdr.init(interface_number=int(i))
            self.sdr_controlers.append(sdr) 
        
    def __del__(self):
        pass
        
    def run(self, sample_size=256*1024):
        if len(self.sdr_controlers) == 0:
            return None
        for i in range(len(self.sdr_controlers)):
            samples = self.sdr_controlers[int(i)].run(sample_size)
        self.plot(samples)
        return samples
    
    def plot(self, samples):
        if not self.is_plot:
            psd_scan, f = psd(samples, NFFT=1024)#, Fs=self.sdr_controlers[0].sample_rate/1e6)#, Fc=self.sdr_controlers[0].center_freq/1e6)
            #sns.xlabel('Frequency (MHz)')
            #sns.ylabel('Relative power (dB)')
            #power = np.real(self.samples * np.conj(self.samples))
            psd_scan = 10*np.log10(psd_scan)
            #sns.distplot(psd_scan, hist=False, color="g", kde_kws={"shade": False})
            sns.lineplot(data=psd_scan, palette="tab10", linewidth=2.5)
            #f, Pxx_den = signal.welch(self.samples, self.sdr_controler.sample_rate/1e6, nperseg=1024)
            #plt.semilogy(f, Pxx_den)
            #plt.ylim([-90, -50])
            self.is_plot = True
        else:           
            #power = np.real(self.samples * np.conj(self.samples))
            psd_scan, f = psd(samples, NFFT=1024)#, Fs=self.sdr_controlers[0].sample_rate/1e6)#, Fc=self.sdr_controlers[0].center_freq/1e6)
            psd_scan = 10*np.log10(psd_scan)
            #sns.distplot(psd_scan, hist=False, color="g", kde_kws={"shade": False})#, ax=axes[1, 0])
            sns.lineplot(data=psd_scan, palette="tab10", linewidth=2.5)
            #f, Pxx_den = signal.welch(self.samples, self.sdr_controler.sample_rate/1e6, nperseg=1024)
            #plt.semilogy(f, Pxx_den)
        
        plt.ion()
        #plt.pause(refresh_time)
        plt.pause(0.1)
        plt.cla()
        #plt.show()
    
        
def main(**kwargs):
    viewer = VIEWER()

    for i in range(10):
        viewer.run()

if __name__ == "__main__":
    args = sys.argv[1:]
    kwargs = {}
    for i in range(0, len(args),2):
        kwargs[args[i]] = args[i+1]
    main(**kwargs)

