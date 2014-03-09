import tornado.ioloop
import tornado.web
import json
import IPy
import sys

sys.path.append('lib')
import netcalc

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
         
application = tornado.web.Application([
    (r"/netcalc/api", APIHandler),
    (r"/netcalc", FormHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
