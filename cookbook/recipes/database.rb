#
# Cookbook Name:: netcalc
# Recipe:: app
#
# Copyright (C) 2014 Chris Antenesse
#
#

include_recipe 'mysql::server'
include_recipe 'database::mysql'

mysql_connection_info = {
  :host     => 'localhost',
  :username => 'root',
  :password => node['mysql']['server_root_password']
}

mysql_database 'networks' do
  connection mysql_connection_info
  action :create
end