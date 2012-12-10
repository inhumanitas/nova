# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import fixtures

from nova import config
from nova.openstack.common import cfg

CONF = cfg.CONF
CONF.import_opt('state_path', 'nova.config')
CONF.import_opt('scheduler_driver', 'nova.scheduler.manager')
CONF.import_opt('fake_network', 'nova.network.manager')
CONF.import_opt('network_size', 'nova.network.manager')
CONF.import_opt('num_networks', 'nova.network.manager')
CONF.import_opt('policy_file', 'nova.policy')
CONF.import_opt('compute_driver', 'nova.virt.driver')


class ConfFixture(fixtures.Fixture):
    """Fixture to manage global conf settings."""

    def __init__(self, conf):
        self.conf = conf

    def setUp(self):
        super(ConfFixture, self).setUp()

        self.conf.set_default('api_paste_config',
                              '$state_path/etc/nova/api-paste.ini')
        self.conf.set_default('compute_driver', 'nova.virt.fake.FakeDriver')
        self.conf.set_default('fake_network', True)
        self.conf.set_default('fake_rabbit', True)
        self.conf.set_default('flat_network_bridge', 'br100')
        self.conf.set_default('floating_ip_dns_manager',
                              'nova.tests.utils.dns_manager')
        self.conf.set_default('instance_dns_manager',
                              'nova.tests.utils.dns_manager')
        self.conf.set_default('lock_path', None)
        self.conf.set_default('network_size', 8)
        self.conf.set_default('num_networks', 2)
        self.conf.set_default('rpc_backend',
                              'nova.openstack.common.rpc.impl_fake')
        self.conf.set_default('rpc_cast_timeout', 5)
        self.conf.set_default('rpc_response_timeout', 5)
        self.conf.set_default('sql_connection', "sqlite://")
        self.conf.set_default('sqlite_synchronous', False)
        self.conf.set_default('use_ipv6', True)
        self.conf.set_default('verbose', True)
        self.conf.set_default('vlan_interface', 'eth0')
        config.parse_args([], default_config_files=[])
        self.addCleanup(self.conf.reset)
