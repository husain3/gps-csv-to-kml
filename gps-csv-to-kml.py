import pandas as pd
import simplekml
import pprint

kml = simplekml.Kml()
df = pd.read_csv('gps_data.csv')

df.drop(4)

df.columns = ['latitude', 'longitude', 'altitude', 'hdop', 'ackReceived', 'datetime']
rearrange_columns = ['longitude', 'latitude', 'altitude', 'hdop', 'ackReceived', 'datetime']

df = df.drop(columns=['datetime'])
df = df.reindex(columns=rearrange_columns)

tuples = [tuple(x) for x in df.values]

extrude=1
altitudemode = simplekml.AltitudeMode.clamptoground

pol = kml.newpolygon(name="", description="", outerboundaryis=tuples, extrude=extrude, altitudemode=altitudemode)
pol.style.linestyle.color = simplekml.Color.red
pol.style.linestyle.width = 3
pol.style.polystyle.color = simplekml.Color.changealphaint(0, simplekml.Color.navy)


kml.save('gps_data.kml')

# for name, newdf in df.items():
# 	print(name)

# print(tuples[0])
