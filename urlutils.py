#! /usr/bin/python

import urlparse
import urllib
import sys

# List of supported channels
supported_channels = ("P1","P2")

class UrlBuilder:
    def __init__(self, scheme='http', netloc='www.nrk.no', path='/programoversikt/avansert/', params='', query='', url=''):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.params = params
        self.query = query
        self.fragment = ''

    def __str__(self):
        return urlparse.urlunparse((self.scheme, self.netloc, self.path, self.params, self.query, self.fragment))

    def setQuery(self, plist_params):
        self.query = plist_params.asQuery()

class ProgramListParams:
    def __init__(self, p_format='HTML', p_type='prog', p_fom_dag='11', p_fom_mnd='9', p_fom_ar='2012', p_periode='dennedagen', channel='MPETRE'):
        self.p_format=p_format
        self.p_type = p_type
        self.p_fom_dag = p_fom_dag
        self.p_fom_mnd = p_fom_mnd
        self.p_fom_ar = p_fom_ar
        self.p_periode = p_periode
        self.channel = channel

    def setFormat(self, p_format):
        self.p_format = p_format

    def setFomDag(self, fom_dag):
        self.p_fom_dag = fom_dag

    def setFomMnd(self, p_fom_mnd):
        self.p_fom_mnd = p_fom_mnd

    def setFomAr(self, p_fom_ar):
        self.p_fom_ar = p_fom_ar

    def setPeriode(self, p_periode):
        self.p_periode = p_periode
        
    def setPtype(self, p_type):
        self.p_type = p_type

    def setChannel(self, channel):
        self.channel = channel

    def channelAsQueryParam(self):
        name = "&p_"
        low = self.channel.lower()
        upper = self.channel
        return name + low + "=" + upper

    def asQuery(self):
        return "p_artikkel_id=&p_format={p_format}&p_type={p_type}&p_fom_dag={p_fom_dag}&p_fom_mnd={p_fom_mnd}&p_fom_ar={p_fom_ar}&p_periode={p_periode}".format(p_format=self.p_format, p_type=self.p_type, p_fom_dag=self.p_fom_dag,p_fom_mnd=self.p_fom_mnd, p_fom_ar=self.p_fom_ar, p_periode=self.p_periode) + self.channelAsQueryParam()
#return 'p_artikkel_id=&p_format=HTML&p_type=prog&p_fom_dag=11&p_fom_mnd=9&p_fom_ar=2012&p_periode=dennedagen&p_mpetre=MPETRE'

def printListofSupportedChannels():
    print "Supported channels:\nP1\nP2"

def validateArgs(args):
    if args.channel.upper() in supported_channels:
        pass
    else:
        print args.channel + " is not a supported channel"
        printListofSupportedChannels()
        sys.exit(0)

if __name__ == '__main__':
    urlbuild = UrlBuilder(query='p_format=HTML')
    plist = ProgramListParams()
    plist.setChannel("P1")
    urlbuild.setQuery(plist)
    print urlbuild
