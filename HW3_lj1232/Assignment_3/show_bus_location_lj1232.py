from __future__ import print_function
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv)==3:
    print ('Invalid number of arguments. Run as: show_bus_location_lj1232.py MTAKEY BUSLINE')
    sys.exit()
    

url='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s'%(sys.argv[1], sys.argv[2])

#print(url)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

VA=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print ('Bus Line : ' + sys.argv[2])
print ('Number of Active Buses : ' + str(len(VA)))

       
for i in VA:
    BusNo=VA.index(i)
    lat=i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long=i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus ' + str(BusNo) + ' is at latitude ' + str(lat) + ' and longitude ' + str(long))
     

                