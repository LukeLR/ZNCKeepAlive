import znc

class pingtimer(znc.Timer):
    def RunJob(self):
        self.GetModule().PutModule('Sending version number {0} to IRC network...'.format(self.counter))
        self.GetModule().PutIRC('version')
        self.counter = self.counter + 1

class keepalive(znc.Module):
    description = "Keep connections through NAT to idle IRC networks alive."
    module_types = [znc.CModInfo.NetworkModule,znc.CModInfo.GlobalModule,znc.CModInfo.UserModule]
    def OnIRCConnected(self):
        timer = self.CreateTimer(pingtimer, interval=5, cycles=0, description='Sends version command to IRC network.')
        timer.counter=0
        return znc.CONTINUE
