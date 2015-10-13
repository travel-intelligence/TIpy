import TIAPICommunicator
import time

communicator = TIAPICommunicator.TIAPICommunicator("https://staging-api.travel-intelligence.com/")
communicator.start_Session("sandro.cuzzolin@amadeus.com", "madrid2015")

# Markets
markets = ["SPAIN", "FRANCE"]

# ONDs:
onds = ["*-ZAG", "*-DBV", "*-SPU"]

# Period type:
ptype = "y"

# Period: Be reminded that when choosing a period you are also served that equivalent from the previous year
# i.e. If you choose period 2015/09 you are given 2014/09 adn 2015/09
period = "2015"

file = open("output.csv","w")

header = "Market;Origin;Destinations;Average number of daily searches in "+ period +";Average number of daily searches last year"

file.write(header)
file.write("\n")

for market in markets:
    for ond in onds:

        response = communicator.accessService("api/search_by_search_period", None, {"market": market, "ptype":ptype, "period":period, "onds":ond})

        for item in response['search_by_search_period'][0]['top_destinations']:

            res = ""
            res = res+ market + ";" + ond.split("-")[0] +";"
            itemstring = map(lambda element: str(element), item)
            res = res + ";".join(itemstring)
            file.write(res)
            file.write("\n")

        time.sleep(0.1)

file.close()
