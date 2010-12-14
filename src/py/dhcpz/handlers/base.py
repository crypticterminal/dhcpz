"""
dhcpz.handlers.base
"""

import dpkt.dhcp as dhcp

class DhcpHandler(object):
    """
    Handlers are the work-horse classes of dhcpz. All logic for handling
    the flow of DHCP packets happens in a handler.
    """

    def __init__(self, logger=None):
        """
        @param logger: Logger to use for all logging in this class
        """
        self.logger = logger or logging.getLogger(self.__class__.__name__)

    def handle_packet(self, listener, packet):
        """
        @param listener: The class handling all communications
        @param packet: The incoming packet
        """ 
        try:
            return self._dispatch[packet["msgtype"]](self, listener, packet)
        except KeyError:
            self.logger.debug("Unknown message type encountered: %d" % packet['msgtype'])

    def handle_discover(self, listener, packet):
        """
        @param listener: The listener that got the packet
        @param packet: The incoming packet from a client
        """
        pass

    def handle_request(self, listener, packet):
        """
        @param listener: The listener that got the packet
        @param packet: The incoming packet from a client
        """
        pass

    def handle_decline(self, listener, packet):
        """
        @param listener: The listener that got the packet
        @param packet: The incoming packet from a client
        """
        pass

    def handle_release(self, listener, packet):
        """
        @param listener: The listener that got the packet
        @param packet: The incoming packet from a client
        """
        pass
    
    _dispatch = {
            dhcp.DHCPDISCOVER : handle_discover,
            dhcp.DHCPDECLINE : handle_decline,
            dhcp.DHCPREQUEST : handle_request,
            dhcp.DHCPRELEASE : handle_release,
            }



