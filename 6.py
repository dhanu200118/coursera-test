import urllib.request, urllib.parse, urllib.error
import json
import ssl
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	address = input("Enter location:")

    url = serviceurl+ urllib.parse.urlencode ({"sensor": "false,", "address":address})

    print ("retrieving", url)
	uh = urllib.request.urlopen(url)
	data = uh.read()
	print ("retrieved", len(data), "characters")
	try:
        js=json.loads(str(data))
	except:
        js= None
	if not js or "status" not in js or js['status'] != "OK":
		print ("=== failure to retrieve ===")
		print (data)
		continue

	print (json.dumps(js, indent = 4))

	lat = js["results"] [0] ["geometry"] ["location"]["lat"]
	lng = js["results"] [0] ["geometry"] ["location"]["lng"]
	print ("lat", lat, "lng", lng)
	location = js["results"][0]["formatted_address"]
	print ("placeid",location)
