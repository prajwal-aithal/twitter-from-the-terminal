import httplib
import urllib
import json
import sys

def error_mess() :
    print "The expected format is - "
    print "$ python twitterbot.py <action> <attributes>"
    print "<action> - search, trend, user"
    print "<attributes> - "
    print "search - <query> <rpp_number> <result_type>"

 
class TwitterBot :
    def __init__(self) :
        self.searchconn = httplib.HTTPConnection('search.twitter.com')

    def search(self,argarr) :
        keyword = argarr[2]
        rppnum = 20
        restype = "mixed"
        if len(argarr) == 4:
            rppnum = argarr[3]
        elif len(argarr) == 5:
            rppnum = argarr[3]
            restype = argarr[4]
        elif len(argarr) > 5 :
            error_mess()
            return 1
        
        self.searchconn.connect()
        searchkeyword = urllib.urlencode({"q": keyword, "rpp" : rppnum, "result_type": restype})
        self.searchconn.request("GET", "/search.json?"+searchkeyword)
        searchres = self.searchconn.getresponse()
        searchdata = searchres.read()
        searchjsondata =  json.loads(searchdata)['results']

        print "\n \n"
        print "-----------------------",
        print "You asked for around "+str(rppnum)+" "+restype+" public tweets about - "+keyword,
        print "-----------------------"
        print "\n \n"
        
        for a in searchjsondata :
            print a["from_user"], "(www.twitter.com/"+str(a["from_user"])+")", a["created_at"]
            print a["text"]
            print "____________________________________________"

    def trending(self) :
        print "Hello, welcome to the trend function"
        

def main() :
    Bot = TwitterBot()
    if len(sys.argv) == 1 or len(sys.argv) == 2 :
        error_mess()
        return 1
    if(sys.argv[1] == "search") :
        Bot.search(sys.argv)


   
main()


