import requests
import time

url = 'https://www.kayak.com'
r = requests.get(url)
layer1Cookies = r.cookies

url2 = url + '/s/horizon/flights/results/FlightSearchPoll'

origin_code = 'WAS'
origin_location = 'WASHINGTON'
destination_code = 'AMD'
destination_location = 'Ahmedabad'
depart_date = '2018-04-20'
return_date = '2018-04-27'

referer = 'https://www.kayak.com/flights/'+origin_code+'-'+destination_code+'/'+depart_date+'/'+return_date
headers = {
    'Host': 'www.kayak.com',
    'User-Agent': 'Chrome/63 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': referer,
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-CSRF': 'kAqI1NgGh$DJnEUpiSDOWpdQXzlgAwG8EVOCd$gXO08-hpumC4oNpaOjz15GO_q9a5FdZPonpC2kF4CBYjEPh14',
    'X-RequestId': 'flights#frontdoor#Ag$s9g',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '1094'
}
params = {
    'searchId':'',
    'poll':'true',
    'pollNumber':'0',
    'applyFilters':'true',
    'filterState':'',
    'useViewStateFilterState':'false',
    'pageNumber':'1',
    'append':'false',
    'pollingId':'593606',  #interesting. explore further
    'requestReason':'POLL',
    'isSecondPhase':'false',
    'textAndPageLocations':'bottom,right',
    'displayAdPageLocations':'none',
    'existingAds':'false',
    'activeLeg':'-1',
    'view':'list',
    'renderPlusMinusThreeFlex':'false',
    'renderAirlineStopsMatrix':'false',
    'renderFlexHeader':'true',
    'tab':'flights',
    'pageOrigin':'F..FD..M0',
    'src':'',
    'searchingAgain':'',
    'c2s':'',
    'po':'',
    'personality':'',
    'provider':'',
    'isMulticity':'false',
    'flex_category':'exact',
    'depart_date':'12/30/2017',
    'return_date':'01/31/2018',
    'oneway':'false',
    'origincode':'WAS',  #change accordingly
    'origin':'WAS', #change accordingly
    'origin_location':'Washington+(WAS)', #change accordingly
    'origin_code':'WAS/2279', #change accordingly
    'nearby_origin':'false',
    'destination':'LIM', #change accordingly
    'destination_location':'Lima', #change accordingly
    'destination_code':'LIM/2270', #change accordingly
    'nearby_destination':'false',
    'countrySearch':'false',
    'depart_date_canon':'2017-12-30', #change accordingly
    'return_date_canon':'2018-01-31', #change accordingly
    'travelers':'1',
    'adults':'1',
    'seniors':'0',
    'youth':'0',
    'child':'0',
    'seatInfant':'0',
    'lapInfant':'0',
    'cabin':'e',
    'cabinDisplayType':'Economy',
    'vertical':'flights',
    'url':'flights/WAS-LIM/2017-12-30/2018-01-31',
    'id':'',
    'navigateToResults':'false',
    'ajaxts':'',
    'scriptsMetadata':'',
    'stylesMetadata':'',
}


url3 = 'flights/'+origin_code+'-'+destination_code+'/'+depart_date+'/'+return_date

params1 = {
    'searchId':'',
    'poll':'true',
    'pollNumber':'0',
    'applyFilters':'true',
    'filterState':'',
    'useViewStateFilterState':'false',
    'pageNumber':'1',
    'append':'false',
    'pollingId':'593601',  #interesting. explore further
    'requestReason':'POLL',
    'isSecondPhase':'false',
    'textAndPageLocations':'bottom,right',
    'displayAdPageLocations':'none',
    'existingAds':'false',
    'activeLeg':'-1',
    'view':'list',
    'renderPlusMinusThreeFlex':'false',
    'renderAirlineStopsMatrix':'false',
    'renderFlexHeader':'true',
    'tab':'flights',
    'pageOrigin':'F..FD..M0',
    'src':'',
    'searchingAgain':'',
    'c2s':'',
    'po':'',
    'personality':'',
    'provider':'',
    'isMulticity':'false',
    'flex_category':'exact',
    'depart_date':depart_date,
    'return_date':return_date,
    'oneway':'false',
    'origincode':origin_code,  #change accordingly
    'origin':origin_code, #change accordingly
    'origin_location':origin_location, #change accordingly
    'origin_code':'', #change accordingly
    'nearby_origin':'false',
    'destination':destination_code, #change accordingly
    'destination_location':destination_location, #change accordingly
    'destination_code':'', #change accordingly
    'nearby_destination':'false',
    'countrySearch':'false',
    'depart_date_canon':depart_date, #change accordingly
    'return_date_canon':return_date, #change accordingly
    'travelers':'1',
    'adults':'1',
    'seniors':'0',
    'youth':'0',
    'child':'0',
    'seatInfant':'0',
    'lapInfant':'0',
    'cabin':'e',
    'cabinDisplayType':'Economy',
    'vertical':'flights',
    'url':url3,
    'id':'',
    'navigateToResults':'false',
    'ajaxts':'',
    'scriptsMetadata':'',
    'stylesMetadata':'',
}

next = requests.post(url2, headers = headers, data = params1, cookies = layer1Cookies)
print(next.json())

