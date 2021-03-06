Quick Start
===========

Following example code shows how the driver is intended to be used:

.. sourcecode:: python

    import time
    from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
    from sensirion_shdlc_svm41 import Svm41ShdlcDevice

    # Connect to the device with default settings:
    #  - baudrate:      115200
    #  - slave address: 0
    with ShdlcSerialPort(port='COM1', baudrate=115200) as port:
        device = Svm41ShdlcDevice(ShdlcConnection(port), slave_address=0)
        device.device_reset()

        # Print some device information
        print("Version: {}".format(device.get_version()))
        print("Product Name: {}".format(device.get_product_name()))
        print("Serial Number: {}".format(device.get_serial_number()))

        # Start measurement
        device.start_measurement()
        print("Measurement started... ")
        while True:
            time.sleep(10.)
            humidity, temperature, air_quality_voc, air_quality_nox = \
                device.read_measured_values()

            # use default formatting for printing output:
            print("{}, {}, {}, {}".format(humidity,
                                          temperature,
                                          air_quality_voc,
                                          air_quality_nox))

