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
from sensirion_shdlc_driver.errors import ShdlcDeviceError

import logging
log = logging.getLogger(__name__)


class Svm41CommandNotAllowedInCurrentState(ShdlcDeviceError):
    """
    Command is not allowed in the current state.
    """
    def __init__(self):
        super(Svm41CommandNotAllowedInCurrentState, self).__init__(
            0x43,
            "Command is not allowed in the current state."
        )


class Svm41FatalError(ShdlcDeviceError):
    """
    An error without specific error code occurred.
    """
    def __init__(self):
        super(Svm41FatalError, self).__init__(
            0x7F,
            "An error without specific error code occurred."
        )


"""
List containing all device errors specified in this file.
"""
SVM41_DEVICE_ERROR_LIST = [
    Svm41CommandNotAllowedInCurrentState(),
    Svm41FatalError(),
]
