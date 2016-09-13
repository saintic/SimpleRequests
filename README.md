# SimpleRequests
Simple Web Site(URL) Request Module


## Requirement
Requested URL returns JSON data

## Install
> pip install SimpleRequests

## Usage
*1.*
```
from SimpleReuqests import Requests
req=Requests()
req.get(YOUR_REQUEST_URL)
req.post(YOUR_REQUEST_URL, data=?)
```

*2.*
```
from SimpleRequests import Requests
req=Requests(YOUR_REQUEST_URL)
req.get()
req.post(data=?)
```

