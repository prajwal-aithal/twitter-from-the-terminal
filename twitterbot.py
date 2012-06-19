import httplib
import urllib
import json
import sys

def error_mess() :
    print "The expected format is - "
    print "$ python twitterbot.py <action> <attributes>"
    print "<action> - search, trending"
    print "<attributes> - "
    print "search - <query> <rpp_number> <result_type>"
    print "trending - <daily/ weekly/ nothing>"


def GETTER(connection,url) :
    connection.request("GET", url)
    res = connection.getresponse()
    data = res.read()
    jsondata =  json.loads(data)
    return jsondata


def def_printer(printstr) :
    print "\n \n"
    print "----------------------- "+printstr+" -----------------------"
    print "\n \n"

class TwitterBot :
    def __init__(self) :
        self.searchconn = httplib.HTTPConnection('search.twitter.com')
        self.trendconn = httplib.HTTPConnection('api.twitter.com')
    
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
        searchjsondata =  GETTER(self.searchconn, "/search.json?"+searchkeyword)['results']

        def_printer("You asked for around "+str(rppnum)+" "+restype+" public tweets about - "+keyword)
        
        for a in searchjsondata :
            print a["from_user"], "(www.twitter.com/"+str(a["from_user"])+")", a["created_at"]
            print a["text"]
            print "____________________________________________"


    def trending(self,argarr) :
        if len(argarr) > 3 :
            error_mess()
            return 1
        else :
            self.trendconn.connect()
            if len(argarr) == 2 :
                trendjson =  GETTER(self.trendconn,"/1/trends/1.json")[0]
                trendjsondata = trendjson['trends']

                def_printer("Trending topics as of "+trendjson["as_of"][0:10]+" are")

                for a in trendjsondata :
                    print a["name"], "(https://twitter.com/search/"+str(a["query"])+")"
                    print "____________________________________________"
            else :
                timeframe = argarr[2]
                if timeframe == "daily" :
                    trendjson =  GETTER(self.trendconn,"/1/trends/daily.json")
                    trendjsondata = trendjson['trends']
                    for a in trendjsondata :
                        date = a.split(' ')[0]
                        break
                    
                    def_printer("Trending topics for "+date+" are")

                    for a in trendjsondata :
                        print "----- "+ a + " -----"+"\n"
                        for x in trendjsondata[a] :
                            print x["name"]
                            print "____________________________________________"
                else :
                    trendjson =  GETTER(self.trendconn,"/1/trends/weekly.json")
                    trendjsondata = trendjson['trends']
                    for a in trendjsondata :
                        date = a.split(' ')[0]
                        break
                    
                    def_printer("Trending topics for the week starting from "+date+" are")

                    for a in trendjsondata :
                        print "----- "+ a + " -----" + "\n"
                        for x in trendjsondata[a] :
                            print x["name"]
                            print "____________________________________________"
                
        

def main() :
    Bot = TwitterBot()
    if len(sys.argv) == 1 :
        error_mess()
        return 1
    if sys.argv[1] == "search" :
        if len(sys.argv) == 2 :
            error_mess()
            return 1
        Bot.search(sys.argv)
    elif sys.argv[1] == "trending" :
        Bot.trending(sys.argv)
    else :
        error_mess()
        return 1
        


   
main()


