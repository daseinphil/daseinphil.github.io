import csv
 
# Read in raw data from csv
rawData = csv.reader(open('311_clean.csv', 'rb'))
 
template = """L.marker([%s, %s]).bindPopup('<table border=0><tr><td>Address</td><td>%s</td></tr><tr><td>Date</td><td>%s</td> </tr></table>').addTo(%s);"""

print "var group2009 = new L.LayerGroup();\n"

for row in rawData:
	date = row[0]
	ticket = row[1]
	address = row[2]
	lat = row[4]
	lng = row[5]
	if "2009" in date:
		group = "group2009"
	elif "2010" in date:
		group = "group2010" 
	elif "2011" in date:
		group = "group2011" 
	elif "2012" in date:
		group = "group2012" 
	else:
		group = ""
	if "2009" in date:
		print template % (lat, lng, date, address, group)
	


