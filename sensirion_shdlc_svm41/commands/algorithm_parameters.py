# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

##############################################################################
##############################################################################
#                 _____         _    _ _______ _____ ____  _   _
#                / ____|   /\  | |  | |__   __|_   _/ __ \| \ | |
#               | |       /  \ | |  | |  | |    | || |  | |  \| |
#               | |      / /\ \| |  | |  | |    | || |  | | . ` |
#               | |____ / ____ \ |__| |  | |   _| || |__| | |\  |
#                \_____/_/    \_\____/   |_|  |_____\____/|_| \_|
#
#     THIS FILE IS AUTOMATICALLY GENERATED AND MUST NOT BE EDITED MANUALLY!
#
# Generator:    sensirion-shdlc-interface-generator 0.9.0
# Product:      SVM41
# Version:      0.8.4
#
##############################################################################
##############################################################################

# flake8: noqa

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver.command import ShdlcCommand
from struct import pack, unpack

import logging
log = logging.getLogger(__name__)


class Svm41CmdAlgorithmParametersBase(ShdlcCommand):
    """
    SHDLC command 0x60: "Algorithm Parameters".
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super(Svm41CmdAlgorithmParametersBase, self).__init__(
            0x60, *args, **kwargs)


class Svm41CmdGetTemperatureOffsetForRhtMeasurements(Svm41CmdAlgorithmParametersBase):
    """
    Get Temperature Offset For Rht Measurements Command

    Gets the T-Offset for the temperature compensation of the RHT algorithm.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Svm41CmdGetTemperatureOffsetForRhtMeasurements, self).__init__(
            data=b"".join([bytes(bytearray([0x01]))]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=2,
            max_response_length=2
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: Temperature offset which is used for the RHT measurements.
                 Values are in degrees celsius with a scaling of 200. Thus the
                 received value must be divided by 200.
        :rtype: int
        """
        t_offset = int(unpack(">h", data[0:2])[0])  # int16
        return t_offset


class Svm41CmdGetVocTuningParameters(Svm41CmdAlgorithmParametersBase):
    """
    Get Voc Tuning Parameters Command

    Gets the currently set parameters for customizing the VOC algorithm.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Svm41CmdGetVocTuningParameters, self).__init__(
            data=b"".join([bytes(bytearray([0x0D]))]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=12,
            max_response_length=12
        )

    @staticmethod
    def interpret_response(data):
        """
        :return:
            - voc_index_offset (int) -
              VOC index representing typical (average) conditions.
            - learning_time_offset_hours (int) -
              Time constant to estimate the VOC algorithm offset from the
              history in hours. Past events will be forgotten after about twice
              the learning time.
            - learning_time_gain_hours (int) -
              Time constant to estimate the VOC algorithm gain from the history
              in hours. Past events will be forgotten after about twice the
              learning time.
            - gating_max_duration_minutes (int) -
              Maximum duration of gating in minutes (freeze of estimator during
              high VOC index signal). Set to zero to disable the gating.
            - std_initial (int) -
              Initial estimate for standard deviation. Lower value boosts
              events during initial learning period, but may result in larger
              device-to-device variations.
            - gain_factor (int) -
              Gain factor to amplify or to attenuate the VOC index output.
        :rtype: tuple
        """
        voc_index_offset = int(unpack(">h", data[0:2])[0])  # int16
        learning_time_offset_hours = int(unpack(">h", data[2:4])[0])  # int16
        learning_time_gain_hours = int(unpack(">h", data[4:6])[0])  # int16
        gating_max_duration_minutes = int(unpack(">h", data[6:8])[0])  # int16
        std_initial = int(unpack(">h", data[8:10])[0])  # int16
        gain_factor = int(unpack(">h", data[10:12])[0])  # int16
        return voc_index_offset,\
            learning_time_offset_hours,\
            learning_time_gain_hours,\
            gating_max_duration_minutes,\
            std_initial,\
            gain_factor


class Svm41CmdGetNoxTuningParameters(Svm41CmdAlgorithmParametersBase):
    """
    Get Nox Tuning Parameters Command

    Gets the currently set parameters for customizing the NOx algorithm.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Svm41CmdGetNoxTuningParameters, self).__init__(
            data=b"".join([bytes(bytearray([0x0E]))]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=12,
            max_response_length=12
        )

    @staticmethod
    def interpret_response(data):
        """
        :return:
            - nox_index_offset (int) -
              NOx index representing typical (average) conditions.
            - learning_time_offset_hours (int) -
              Time constant to estimate the NOx algorithm offset from the
              history in hours. Past events will be forgotten after about twice
              the learning time.
            - learning_time_gain_hours (int) -
              The time constant to estimate the NOx algorithm gain from the
              history has no impact for NOx. This parameter is still in place
              for consistency reasons with the VOC tuning parameters command.
              This getter will always return the default value.
            - gating_max_duration_minutes (int) -
              Maximum duration of gating in minutes (freeze of estimator during
              high NOx index signal). Set to zero to disable the gating.
            - std_initial (int) -
              The initial estimate for standard deviation has no impact for
              NOx. This parameter is still in place for consistency reasons
              with the VOC tuning parameters command. This getter will always
              return the default value.
            - gain_factor (int) -
              Gain factor to amplify or to attenuate the NOx index output.
        :rtype: tuple
        """
        nox_index_offset = int(unpack(">h", data[0:2])[0])  # int16
        learning_time_offset_hours = int(unpack(">h", data[2:4])[0])  # int16
        learning_time_gain_hours = int(unpack(">h", data[4:6])[0])  # int16
        gating_max_duration_minutes = int(unpack(">h", data[6:8])[0])  # int16
        std_initial = int(unpack(">h", data[8:10])[0])  # int16
        gain_factor = int(unpack(">h", data[10:12])[0])  # int16
        return nox_index_offset,\
            learning_time_offset_hours,\
            learning_time_gain_hours,\
            gating_max_duration_minutes,\
            std_initial,\
            gain_factor


class Svm41CmdStoreNvData(Svm41CmdAlgorithmParametersBase):
    """
    Store Nv Data Command

    Stores all algorithm parameters to the non-volatile memory.
    """

    def __init__(self):
        """
        Constructor.
        """
        super(Svm41CmdStoreNvData, self).__init__(
            data=b"".join([bytes(bytearray([0x80]))]),
            max_response_time=0.5,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Svm41CmdSetTemperatureOffsetForRhtMeasurements(Svm41CmdAlgorithmParametersBase):
    """
    Set Temperature Offset For Rht Measurements Command

    Sets the T-Offset for the temperature compensation of the RHT algorithm.

    .. note:: Execute the store command after writing the parameter to store it
              in the non-volatile memory of the device otherwise the parameter
              will be reset upton a device reset.
    """

    def __init__(self, t_offset):
        """
        Constructor.

        :param int t_offset:
            Temperature offset in degrees celsius. Accepted data formats is a
            int16 value (2 bytes). Values are in degrees celsius with a scaling
            of 200. Thus the provided value must be multiplied by 200.
        """
        super(Svm41CmdSetTemperatureOffsetForRhtMeasurements, self).__init__(
            data=b"".join([bytes(bytearray([0x81])),
                           pack(">h", t_offset)]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Svm41CmdSetVocTuningParameters(Svm41CmdAlgorithmParametersBase):
    """
    Set Voc Tuning Parameters Command

    Sets parameters to customize the VOC algorithm. This command is only
    available in idle mode.

    .. note:: Execute the store command after writing the parameter to store it
              in the non-volatile memory of the device otherwise the parameter
              will be reset upton a device reset.
    """

    def __init__(self, voc_index_offset, learning_time_offset_hours, learning_time_gain_hours, gating_max_duration_minutes, std_initial, gain_factor):
        """
        Constructor.

        :param int voc_index_offset:
            VOC index representing typical (average) conditions. Allowed values
            are in range 1..250. The default value is 100.
        :param int learning_time_offset_hours:
            Time constant to estimate the VOC algorithm offset from the history
            in hours. Past events will be forgotten after about twice the
            learning time. Allowed values are in range 1..1000. The default
            value is 12 hours.
        :param int learning_time_gain_hours:
            Time constant to estimate the VOC algorithm gain from the history
            in hours. Past events will be forgotten after about twice the
            learning time. Allowed values are in range 1..1000. The default
            value is 12 hours.
        :param int gating_max_duration_minutes:
            Maximum duration of gating in minutes (freeze of estimator during
            high VOC index signal). Set to zero to disable the gating. Allowed
            values are in range 0..3000. The default value is 180 minutes.
        :param int std_initial:
            Initial estimate for standard deviation. Lower value boosts events
            during initial learning period, but may result in larger
            device-to-device variations. Allowed values are in range 10..5000.
            The default value is 50.
        :param int gain_factor:
            Gain factor to amplify or to attenuate the VOC index output.
            Allowed values are in range 1..1000. The default value is 230.
        """
        super(Svm41CmdSetVocTuningParameters, self).__init__(
            data=b"".join([bytes(bytearray([0x8D])),
                           pack(">h", voc_index_offset),
                           pack(">h", learning_time_offset_hours),
                           pack(">h", learning_time_gain_hours),
                           pack(">h", gating_max_duration_minutes),
                           pack(">h", std_initial),
                           pack(">h", gain_factor)]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class Svm41CmdSetNoxTuningParameters(Svm41CmdAlgorithmParametersBase):
    """
    Set Nox Tuning Parameters Command

    Sets parameters to customize the NOx algorithm. This command is only
    available in idle mode.

    .. note:: Execute the store command after writing the parameter to store it
              in the non-volatile memory of the device otherwise the parameter
              will be reset upton a device reset.
    """

    def __init__(self, nox_index_offset, learning_time_offset_hours, learning_time_gain_hours, gating_max_duration_minutes, std_initial, gain_factor):
        """
        Constructor.

        :param int nox_index_offset:
            NOx index representing typical (average) conditions. Allowed values
            are in range 1..250. The default value is 1.
        :param int learning_time_offset_hours:
            Time constant to estimate the NOx algorithm offset from the history
            in hours. Past events will be forgotten after about twice the
            learning time. Allowed values are in range 1..1000. The default
            value is 12 hours.
        :param int learning_time_gain_hours:
            The time constant to estimate the NOx algorithm gain from the
            history has no impact for the NOx algorithm. This parameter is
            still in place for consistency reasons with the VOC tuning
            parameters command. This parameter must always be set to 12 hours.
        :param int gating_max_duration_minutes:
            Maximum duration of gating in minutes (freeze of estimator during
            high NOx index signal). Set to zero to disable the gating. Allowed
            values are in range 0..3000. The default value is 720 minutes.
        :param int std_initial:
            The initial estimate for standard deviation parameter has no impact
            for the NOx algorithm. This parameter is still in place for
            consistency reasons with the VOC tuning parameters command. This
            parameter must always be set to 50.
        :param int gain_factor:
            Gain factor to amplify or to attenuate the NOx index output.
            Allowed values are in range 1..1000. The default value is 230.
        """
        super(Svm41CmdSetNoxTuningParameters, self).__init__(
            data=b"".join([bytes(bytearray([0x8E])),
                           pack(">h", nox_index_offset),
                           pack(">h", learning_time_offset_hours),
                           pack(">h", learning_time_gain_hours),
                           pack(">h", gating_max_duration_minutes),
                           pack(">h", std_initial),
                           pack(">h", gain_factor)]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )
