name             'netcalc'
maintainer       'Chris Antenesse'
maintainer_email 'chris@antenesse.net'
license          'All rights reserved'
description      'Installs/Configures netcalc'
long_description 'Installs/Configures netcalc'
version File.read(File.join(File.dirname(__FILE__), "..", "VERSION"))

depends 'apt'

recipe 'netcalc::default', 'Installs a full stack netcalc server'
recipe 'netcalc::app', 'Installs a netcalc application server'

attribute 'netcalc/app/port'
    display_name: 'App Server Port',
    description: 'Listen port for application server',
    type: 'integer'
    default: 8888
    