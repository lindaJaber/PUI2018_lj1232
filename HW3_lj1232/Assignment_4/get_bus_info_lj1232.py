from __future__ import print_function
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import json

if not len(sys.argv) == 4:
    print('Invalid number of arguments. Run as: pyhton get_bus_info_lj1232 MTAKEY BUSLINE BUS_LINE.csv')
    
    
url='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s'%(sys.argv[1], sys.argv[2])

response=urllib.urlopen(url)
data=response.read().decode('utf-8')
data=json.loads(data)


fout = open(sys.argv[3], 'w')
fout.write('Latitude,Longitude,Stop Name,Stop Status\n')

VA=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
for i in VA:
    lat=i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long=i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    name=i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    status=i['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
    if status == '':
        fout.write (str(lat) + ',' + str(long) + ',' + 'N/A' + ',' + 'N/A' + ','  + '\n')
    else:
        fout.write(str(lat) + ',' + str(long) + ',' + name + ',' + status + '\n')

