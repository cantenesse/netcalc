#
# Cookbook Name:: netcalc
# Recipe:: app
#
# Copyright (C) 2014 Chris Antenesse
#
#
include_recipe 'apt'

package 'python-tornado' do 
    action :install
end

package 'python-IPy' do
    action :install
end

package 'python-yaml' do
    action :install
end