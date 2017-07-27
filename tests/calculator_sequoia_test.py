from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from unittest import TestCase

from sequoia_calculator.sequoia import SEQUOIA


class TestCalculatorSEQUOIA(TestCase):
    VERSION = '0.1.0'
    DEFAULT_MODE = 1
    MODES = [1, 2]
    NAME = 'SEQUOIA'

    def setUp(self):
        self.calculator = SEQUOIA(self.DEFAULT_MODE)

    def tearDown(self):
        self.calculator = None

    def test_version(self):
        self.assertEqual(self.calculator.get_version(), self.VERSION)

    def test_name(self):
        self.assertEqual(self.calculator.get_name(), self.NAME)

    def test_calculator_mk(self):
        central_frequency = 100  # GHz (85 - 115)
        spectral_mode = {'b': 200, 'ch': 8192}  # 8192 chanels
        mapx = 1800  # arcsec
        mapy = 1800  # arcsec
        scan_speed = 60  # arcsec/sec
        time = 90  # min
        units = 'mK'
        result = [1, 43.12, 272.98], [2, 86.25, 193.03], [3, 129.37, 157.61]
        self.calculator.set_mode(1)
        self.assertEqual(self.calculator.calculate(
            central_frequency=central_frequency,
            spectral_mode=spectral_mode,
            mapx=mapx, mapy=mapy,
            scan_speed=scan_speed,
            time=time,
            units=units
        ), result)

    def test_calculator_mjy(self):
        central_frequency = 100  # GHz (85 - 115)
        spectral_mode = {'b': 200, 'ch': 8192}  # 8192 chanels
        mapx = 1800  # arcsec
        mapy = 1800  # arcsec
        scan_speed = 60  # arcsec/sec
        time = 90  # min
        units = 'mJy'
        result = [1, 43.12, 873.54], [2, 86.25, 617.69], [3, 129.37, 504.34]
        self.calculator.set_mode(1)
        self.assertEqual(self.calculator.calculate(
            central_frequency=central_frequency,
            spectral_mode=spectral_mode,
            mapx=mapx, mapy=mapy,
            scan_speed=scan_speed,
            time=time,
            units=units
        ), result)

    def test_calculator_temperature(self):
        spectral_mode = {'b': 200, 'ch': 8192}  # 8192 chanels
        central_frequency = 100  # GHz
        mapx = 1800  # arcsec
        mapy = 1800  # arcsec
        scan_speed = 60  # arcsec/sec
        rms = 193.03  # mK
        units = 'Temperature'
        result = [1, 43.12, 272.98], [2, 86.25, 193.03]
        self.calculator.set_mode(2)
        self.assertEqual(self.calculator.calculate(
            central_frequency=central_frequency,
            spectral_mode=spectral_mode,
            mapx=mapx, mapy=mapy,
            scan_speed=scan_speed,
            rms=rms,
            units=units
        ), result)

    def test_calculator_flux(self):
        spectral_mode = {'b': 200, 'ch': 8192}  # 8192 chanels
        central_frequency = 100  # GHz
        mapx = 1800  # arcsec
        mapy = 1800  # arcsec
        scan_speed = 60  # arcsec/sec
        rms = 617.69  # mJy
        units = 'Flux'
        result = [1, 43.12, 873.54], [2, 86.25, 617.69]
        self.calculator.set_mode(2)
        self.assertEqual(self.calculator.calculate(
            central_frequency=central_frequency,
            spectral_mode=spectral_mode,
            mapx=mapx, mapy=mapy,
            scan_speed=scan_speed,
            rms=rms,
            units=units
        ), result)
