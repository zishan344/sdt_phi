from ride import Ride,RideRequest,RideMatching,RideSharing
from user import Rider, Driver

from vehicles import Car, Bike


niya_jao = RideSharing("Niya Jao")

rahim = Rider("Rahim Uddin","rahim@gmail.com",1234,"mohakhali",1200)
niya_jao.add_rider(rahim)
kolimuddin = Driver("kolim Uddin", "Kolim@gmail.com",1234,"Gulshan")
niya_jao.add_driver(kolimuddin)

rahim.request_ride(niya_jao,'Uttara',"car")
kolimuddin.reach_destination(rahim.current_ride)
rahim.show_current_ride()





