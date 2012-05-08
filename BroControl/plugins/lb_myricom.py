# This plugin sets necessary environment variables to run Bro with
# myricom load balancing.

import BroControl.plugin

class LBMyricom(BroControl.plugin.Plugin):
    def __init__(self):
        super(LBMyricom, self).__init__(apiversion=1)

    def name(self):
        return "lb_myricom"

    def pluginVersion(self):
        return 1

    def cmd_install_pre(self):
        for nn in self.nodes():
            if nn.lb_method == "myricom":
                nn.env_vars += ["SNF_NUM_RINGS=10"]
                nn.env_vars += ["SNF_FLAGS=0x101"]

