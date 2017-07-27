# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pdb
from math import ceil, floor, sqrt

from .version import version


class SEQUOIA(object):
    T_SYS = 100  # k
    FR = 0.9
    TTF = 3.2
    NAME = 'SEQUOIA'

    def __init__(self, mode=None):

        self.__mode = mode
        self.__name = self.NAME
        self.__kwargs = None

    def get_version(self):
        return version

    def get_name(self):
        return self.__name

    def set_mode(self, mode):
        self.__mode = mode

    def __calculations(self):
        barion_lambda = 299.793 / self.__kwargs['central_frequency']
        spectral_mode = self.__kwargs['spectral_mode']
        band = spectral_mode['b'] / spectral_mode['ch']
        # deltanu = (band / self.__kwargs['central_frequency']) * (2.99793 * 10 ** 5)
        n_y_cs = 2.06265 * barion_lambda
        n_map = (self.__kwargs['mapx'] + 120) * (self.__kwargs['mapy']) / (n_y_cs ** 2)
        map_time = (n_map * n_y_cs) / (self.FR * self.__kwargs['scan_speed'] * 14400)
        map_rms = (self.T_SYS / (8.3138 * (10 ** 5))) * sqrt(n_map / (band * map_time))
        return map_time, map_rms

    def __calculate_mk(self):
        map_time, map_rms = self.__calculations()
        n_maps_up = ceil(self.__kwargs['time'] / (60 * map_time))
        n_maps_down = floor(self.__kwargs['time'] / (60 * map_time))
        rms_up = (1000 * map_rms) / sqrt(n_maps_up)
        rms_down = (1000 * map_rms) / sqrt(n_maps_down)
        time_up = map_time * n_maps_up * 60
        time_down = map_time * n_maps_down * 60
        a = [1, round(map_time * 60, 2), round(map_rms * 1000, 2)]
        b = [n_maps_down, round(time_down, 2), round(rms_down, 2)]
        c = [n_maps_up, round(time_up, 2), round(rms_up, 2)]
        # return [1, 43.12, 272.98], [2, 86.25, 193.03], [3, 129.37, 157.61]

        return a, b, c

    def __calculate_mjy(self):
        map_time, map_rms = self.__calculations()
        n_maps_up = ceil(self.__kwargs['time'] / (60 * map_time))
        n_maps_down = floor(self.__kwargs['time'] / (60 * map_time))
        rms_up = self.TTF * ((1000 * map_rms) / sqrt(n_maps_up))
        rms_down = self.TTF * ((1000 * map_rms) / sqrt(n_maps_down))
        time_up = map_time * n_maps_up * 60
        time_down = map_time * n_maps_down * 60

        a = [1, round(map_time * 60, 2), round(map_rms * 1000 * self.TTF, 2)]
        b = [n_maps_down, round(time_down, 2), round(rms_down, 2)]
        c = [n_maps_up, round(time_up, 2), round(rms_up, 2)]
        return a, b, c
        # return [1, 43.12, 873.54], [2, 86.25, 617.69], [3, 129.37, 504.34]

    def __calculate_temperature(self):
        map_time, map_rms = self.__calculations()
        n_maps_up = ceil(((1000 * map_rms) / self.__kwargs['rms']) ** 2)
        n_maps_down = floor(((1000 * map_rms) / self.__kwargs['rms']) ** 2)
        rms_up = map_rms * 1000 / sqrt(n_maps_up)
        rms_down = map_rms * 1000 / sqrt(n_maps_down)
        time_up = map_time * n_maps_up * 60
        time_down = map_time * n_maps_down * 60

        a = [1, round(map_time * 60, 2), round(map_rms * 1000, 2)]
        b = [n_maps_down, round(time_down, 2), round(rms_down, 2)]
        c = [n_maps_up, round(time_up, 2), round(rms_up, 2)]
        # danger: Exceptions not implemented
        return a, c
        # return [1, 43.12, 272.98], [2, 86.25, 193.03]

    def __calculate_flux(self):
        map_time, map_rms = self.__calculations()
        n_maps_up = ceil(((1000 * map_rms * self.TTF) / self.__kwargs['rms']) ** 2)
        n_maps_down = floor(((1000 * map_rms * self.TTF) / self.__kwargs['rms']) ** 2)
        rms_up = map_rms * 1000 * self.TTF / sqrt(n_maps_up)
        rms_down = map_rms * 1000 * self.TTF / sqrt(n_maps_down)
        time_up = map_time * n_maps_up * 60
        time_down = map_time * n_maps_down * 60

        a = [1, round(map_time * 60, 2), round(map_rms * 1000 * self.TTF, 2)]
        b = [n_maps_down, round(time_down, 2), round(rms_down, 2)]
        c = [n_maps_up, round(time_up, 2), round(rms_up, 2)]

        # danger: Exceptions not implemented
        return a, c

        # return [1, 43.12, 873.536], [2, 86.25, 617.69]

    def calculate(self, **kwargs):
        # result = {}
        self.__kwargs = kwargs
        if self.__mode == 1:
            if self.__kwargs['units'] == 'mK':
                result = self.__calculate_mk()
            elif self.__kwargs['units'] == 'mJy':
                result = self.__calculate_mjy()
        elif self.__mode == 2:
            if self.__kwargs['units'] == 'Temperature':
                result = self.__calculate_temperature()
            elif self.__kwargs['units'] == 'Flux':
                result = self.__calculate_flux()
        return result


if __name__ == '__main__':
    example = SEQUOIA(mode=2)
    central_frequency = 100  # GHz (85 - 115)
    spectral_mode = {'b': 200, 'ch': 8192}  # 8192 chanels
    mapx = 1800  # arcsec
    mapy = 1800  # arcsec
    scan_speed = 60  # arcsec/sec
    time = 90  # min
    rms = 617.69
    units = 'Flux'
    pdb.set_trace()
    example.calculate(
        central_frequency=central_frequency,
        spectral_mode=spectral_mode,
        mapx=mapx, mapy=mapy,
        scan_speed=scan_speed,
        rms=rms,
        units=units)
