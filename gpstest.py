import androidhelper, time
droid = androidhelper.Android()
droid.startLocating()

n = 0
while 1:
   try:
       n+=1
       print('reading GPS ...'+str(n))
       event = droid.eventWaitFor('location',10000)
       rst = event.result
       if rst != None:
           dt = rst['data']
           nt = dt['network']
           pv = nt['provider']
           lt = nt['latitude']
           lg = nt['longitude']
           print('Provider: '+str(pv))
           print('Lat: '+str(lt))
           print('Long: '+str(lg))
           print('-')
       else:
           continue
      
   except KeyError:
      print(str(KeyError))
      break
      
      


"""
/data/user/0/org.qpython.qpy3/files/bin/qpython3-android5.sh  /storage/emulated/0/qpython/.last_tmp.py  && exit
/0/qpython/.last_tmp.py  && exit        <
reading GPS ...
Result(id=2, result={'name': 'location', 'data': {'network': {'altitude': 0, 'latitude': 40.1131461, 'longitude': -8.498351, 'time': 1582481120465, 'accuracy': 23.29800033569336, 'speed': 0, 'provider': 'network', 'bearing': 0}}, 'time': 1582481120683000}, error=None)

#[QPython] Press enter to exit ...
"""


