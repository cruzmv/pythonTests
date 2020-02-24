import androidhelper, time
droid = androidhelper.Android()
droid.startLocating()
print('reading GPS ...')
event = droid.eventWaitFor('location',10000)
while 1:
   try:
      print(event)
      break
      
      #provider = event.result['data']['gps']['provider']
      #if provider == 'gps':
         #print(event)
         #lat = str(event['data']['gps']['latitude'])
         #lng = str(event['data']['gps']['longitude'])
         #print('lat:'+lat+' - long:'+lng)
         #break
      #else: continue
   except KeyError:
      continue
      