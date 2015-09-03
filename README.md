## TI Api Python Wrapper

This project contains a class to communicate with the Amadeus Travel Intelligence Web Services

## Usage

The TIAPICommunicator needs to be initialized with a backend:

```python
communicator = TIAPICommunicator("https://api.travel-intelligence.com/")
```
Then we start a session with the user and password:

```python
communicator.start_Session("user@amadeus.com","XXX")
```

WE can then access to the different service in Travel Intelligence. See dev.travel-intelligence.com for more information:

```python
response = communicator.accessService("api/search_by_search_period",None,{"market":country,"ptype":"q","period":str(year)+"-"+str(quarter),"onds":ond})
```
