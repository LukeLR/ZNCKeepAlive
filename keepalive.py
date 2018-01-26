import znc

class pingtimer(znc.Timer):
    def RunJob(self):
        self.GetModule().PutStatus('foo {0}'.format(self.msg))

class keepalive(znc.Module):
    description = "Keep connections through NAT to idle IRC networks alive."
    module_types = [znc.CModInfo.GlobalModule,znc.CModInfo.UserModule,znc.CModInfo.NetworkModule]
    def OnIRCConnected(self):
        timer = self.CreateTimer(pingtimer, interval=4, cycles=2, description='Says "foo bar" twice after 4 seconds')
        timer.msg = 'bar'
        return znc.CONTINUE
    def OnChanMsg(self, nick, channel, message):
        self.PutModule("Hey, {0} said {1} on {2}".format(nick.GetNick(), message.s, channel.GetName()))
        timer = self.CreateTimer(pingtimer, interval=4, cycles=2, description='Says "foo bar" twice after 4 seconds')
        timer.msg = 'chan'
        return znc.CONTINUE
