import znc

class pingtimer(znc.Timer):
    def RunJob(self):
        self.GetModule().PutStatus('foo {0}'.format(self.msg))

class keepalive(znc.Module):
    description = "Keep connections through NAT to idle IRC networks alive."
    module_types = [znc.CModInfo.GlobalModule,znc.CModInfo.UserModule,znc.CModInfo.NetworkModule]
    def OnIRCConnected(self):
        timer = self.CreateTimer(testtimer, interval=4, cycles=1, description='Says "foo bar" after 4 seconds')
        timer.msg = 'bar'
