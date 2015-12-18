import xmlrpclib

server = xmlrpclib.Server("http://localhost:8000")

#Need to resolve I.O warnings ... and perhaps better format for o, d input.."
rttime = server.GetRouteTime(o, d, validtrips, getstopid) 
print rttime

rtdetail = server.GetRouteDetail(o, d) 
print rtdetail 

server.Quit()
