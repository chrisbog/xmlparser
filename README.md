### xmlparser.py

#### Description
This code module is a code snippet to show a method of parsing through all the data, and summarizing the data.

This code is relevant because it demonstrates the following capabilities:
* Parsing through a XML
* Storing the data and the counts of each individual device serial number
* Leveraging a database to sort the output data in alphabetical order

The format of this xml is the following:

```buildoutcfg
<?xml version="1.0" encoding="UTF-8"?>
<Response requestId="12345">
    <ManagementResponse>
        <Get>
            <DeviceList>
                <Device>
                    <Id>1</Id>
                    .
                    . Device Details
                    .
                    
                </Device>
            </DeviceList>
        </Get>
    </ManagementResponse>
</Response>

```

The output data that is generated is the following:
```buildoutcfg
Model Type                               Count
======================================== =======
CISCO2901/K9                             8
N77-C7710                                1
WS-C2960X-48TS-L                         1

Total Device Count: 10
```