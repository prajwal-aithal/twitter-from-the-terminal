import httplib
import urllib
import json
import sys

class TwitterBot :
    def __init__(self) :
        self.searchconn = httplib.HTTPConnection('search.twitter.com')

    def search(self,keyword) :
        self.searchconn.connect()
        searchkeyword = urllib.urlencode({"q": keyword})
        self.searchconn.request("GET", "/search.json?"+searchkeyword)
        searchres = self.searchconn.getresponse()
        searchdata = searchres.read()
        searchjsondata =  json.loads(searchdata)['results']

        print
        print

        print "-------------------------------------------",
        print "You asked for all public tweets about - "+keyword,
        print "-------------------------------------------"

        print
        print

        for a in searchjsondata :
            print a["from_user"], "(www.twitter.com/"+str(a["from_user"])+")"
            print a["text"]
            print "____________________________________________"


def main() :
    Bot = TwitterBot()
    if(sys.argv[1] == "search") :
        Bot.search(sys.argv[2])

    
main()


