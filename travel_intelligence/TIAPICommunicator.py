import urllib2
import urllib
import json

class TIAPICommunicator(object):

    # constructor:
    def __init__(self, url):

        self.url = url # 'public' variable
        self.__baseURL = url # 'private' variable: can be accessed from child classes by using child._APICommunicator__baseURL

        # Set headers
        self.__headers = {} # set the headers
        self.__headers['Accept'] = 'application/json'
        self.__headers['Content-type'] = 'application/json' # set headers

    # method to start a session
    def start_Session(self,email,password):

        #Set credentials
        query = {}
        query['session'] = {'email' : email, 'password' : password} # set user and pass

         # call to acces the url with user and pass. authentication token is set
        data = self.accessService("api/v1/session", query,None)
        authToken = data['session']['auth_token']

        print authToken

        #Store the token and add the token to the  header of all the next calls
        self.__authToken = authToken
        self.__headers['Authorization'] = str('Token %s' % authToken)


    # method to stop the session
    def stop_Session(self):
        request = urllib2.Request(self.apiURL('api/v1/session'), None, self.__headers)
        request.get_method = lambda: 'DELETE'
        urllib2.urlopen(request).read()

    # method to open a url: it returns an urlopen object in json fromat
    def accessService(self, service, query, parameters):

        j = None
        if query:
            j = json.dumps(query)

        param = ""
        if parameters:
            param = "?" + urllib.urlencode(parameters)

        print self.url + service + param

        req = urllib2.Request(self.url + service + param, j, self.__headers)
        resp = urllib2.urlopen(req)

        return json.load(resp)
