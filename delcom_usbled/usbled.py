__author__ = 'Torsten Braun'


class UsbLed:
    def __init__(self):
        pass

    @staticmethod
    def set(red=False, yellow=False, green=False, off=False):
        import usb.core
        import usb.util

        dev = usb.core.find(idVendor=0x0fc5, idProduct=0x1223)

        if dev is None:
            raise ValueError('Devise not found.')

        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)

        dev.set_configuration()
        usb.util.claim_interface(dev, 0)

        if off:
            color = 0x0
        else:
            color = (0x01 if green else 0x0) + \
                    (0x02 if yellow else 0x0) + \
                    (0x4 if red else 0x0)

        try:
            dev.ctrl_transfer(
                bmRequestType=0x000000c8,
                bRequest=0x00000012,
                wValue=(0x02 * 0x100) + 0x0a,
                wIndex=0xff & (~color),
                data_or_wLength=0x00000008
            )
        except usb.core.USBError:
            pass

        usb.util.release_interface(dev, 0)
        dev.attach_kernel_driver(0)
