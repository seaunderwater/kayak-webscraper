webscraper for kayak that bypasses kayak's bot filters. Change the following variables at the top of the file as desired. Here is an example: 

origin_code = 'WAS'
origin_location = 'WASHINGTON'
destination_code = 'AMD'
destination_location = 'Ahmedabad'
depart_date = '2018-04-20'
return_date = '2018-04-27'

The script will return a lot of content. This content has not been filtered because there is a lot of useful and relevant metadata that shows how Kayak works on the backend. If you are only interested in the prices returned, search for "price" within the returned content. Often there are about 100 prices returned for a given flight. 

In the near future, I will provide an additional script that will only return prices. 



