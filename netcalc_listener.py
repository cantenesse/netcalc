import tornado.ioloop
import tornado.web
import json
import IPy
import sys

def calculate_network_info(net_input):
    net_input_json = json.loads(net_input)
    nc = netcalc.NetCalc(net_input_json)
    result = nc.calc()
    return json.dumps(result)
    
class APIHandler(tornado.web.RequestHandler):
    def post(self):
        self.write(calculate_network_info(self.request.body))


class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")
  
    def post(self):
        net_dict = {'ip': self.get_argument("ip"), 
                    'netmask': self.get_argument("subnet_mask")}
        net_dict = json.dumps(net_dict)
        blah = json.loads(calculate_network_info(net_dict))
        self.render("templates/output.html", title="Subnet Calc",
                    net_dict=blah)
        #self.write(calculate_network_info(net_dict))

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

         
application = tornado.web.Application([
    (r"/netcalc/api", APIHandler),
    (r"/netcalc", FormHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
