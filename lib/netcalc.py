import IPy

class NetCalc:
    def __init__(self, network_struct):
        self.ip = network_struct['ip']
        self.netmask = network_struct['netmask']
        
    def calc(self):
        network = IPy.IP(self.ip).make_net(self.netmask)
        network_id = network.strNormal(0)
        network_cidr = network.strNormal(1)
        network_range = network.strNormal(3)
       
        network_dict = {'net_cidr': network_cidr, 'network_id': network_id,
                        'network_range': network_range}

        return network_dict
