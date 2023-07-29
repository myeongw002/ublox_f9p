#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import NavSatFix
import simplekml

kml = simplekml.Kml()

def callback(msg):
    global kml
    # Ensure the GPS fix is valid
    if msg.status.status != -1:
        lon = msg.longitude
        lat = msg.latitude
        # altitude is optional, but can be included if your GPS provides it
        # alt = msg.altitude
        kml.newpoint(coords=[(lon,lat)])  # Creates a new point in the KML file

rospy.init_node('gps_to_kml')
rospy.Subscriber('/ublox_gps/fix', NavSatFix, callback)  # Substitute '/gps/fix' with your GPS topic
rospy.spin()

kml.save("gps_track.kml")

