# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#
import urllib.request # this provides the classes and codes so we can http requests

web_url = urllib.request.urlopen("http://www.example.com") # will return an http response objects
print("Result code:", web_url.getcode())
# result code was 200 which is good and succesful connection
data = web_url.read()
print(data)

