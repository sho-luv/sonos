#! /usr/bin/python3
# PYTHON_ARGCOMPLETE_OK

############################################
# by Leon Johnson
# 
# This is a template to start programs
# by using the argparse as a starting point
#
# Debuging: 
#       python -m pdb program.py
#

import sys # Used by len, exit, etc
import soco # Sonos api 
import readline
import argparse # Parser for command-line options, arguments and sub-commands

banner = """
 .oooo.o  .ooooo.  ooo. .oo.    .ooooo.   .oooo.o 
d88(  "8 d88' `88b `888P"Y88b  d88' `88b d88(  "8 
`"Y88b.  888   888  888   888  888   888 `"Y88b.  
o.  )88b 888   888  888   888  888   888 o.  )88b 
8""888P' `Y8bod8P' o888o o888o `Y8bod8P' 8""888P' 
"""

parser = argparse.ArgumentParser(description='Program to control Sonos systems. Sonos Amp has a left and right speaker. The amp is powerful enough to set up a room on each This script makes it easy to play left and right speakers as if they were zones. ')
parser.add_argument('-l','--list', action='store_true', help='list sonos definded rooms')
parser.add_argument('-f','--family', action='store', metavar = '{on/off}', help='play music in family room')
parser.add_argument('-k','--kitchen', action='store', metavar = '{on/off}', help='play music in kitchen room')
parser.add_argument('-b', '--bath', action='store', metavar = '{on/off}', help='play music in bath room')
parser.add_argument('-m', '--master', action='store', metavar = '{on/off}', help='play music in master room')
parser.add_argument('-g', '--guest', action='store', metavar = '{on/off}', help='play music in guest room')

if len(sys.argv)==1:
        print(banner)
        parser.print_help()
        sys.exit(1)

options = parser.parse_args()

def get_rooms():
	for device in soco.discover():
		print(device.player_name+" ("+device.ip_address+")")

def family_room(switch):
	room = "192.168.1.104"
	if switch == "on":
		soco.SoCo(room).balance = (0,100)
		soco.SoCo(room).play()
		print("family room should be playing music now...")
		return True
	elif switch == "off":
		soco.SoCo(room).stop()
		print("family room turned off...")
		return True
	else:
		print("Error in option choice")
		return False

def kitchen(switch):
	if switch == "on":
		soco.SoCo("192.168.1.134").balance = (0,100)
		soco.SoCo("192.168.1.134").play()
		print("family room should be playing music now...")
		return True
	elif switch == "off":
		soco.SoCo("192.168.1.134").stop()
		print("family room turned off...")
		return True
	else:
		print("Error in option choice")
		return False

def guest_room(switch):
	if switch == "on":
		soco.SoCo("192.168.1.134").balance = (100,0)
		soco.SoCo("192.168.1.134").play()
		print("guest room should be playing music now...")
		return True
	elif switch == "off":
		soco.SoCo("192.168.1.134").stop()
		print("guest room turned off...")
		return True
	else:
		print("Error in option choice")
		return False

def bath_room():
	if switch == "on":
		soco.SoCo("192.168.1.127").balance = (100,0)
		soco.SoCo("192.168.1.127").play()
		print("guest room should be playing music now...")
		return True
	elif switch == "off":
		soco.SoCo("192.168.1.127").stop()
		print("guest room turned off...")
		return True
	else:
		print("Error in option choice")
		return False

def master_bedroom():
	if switch == "on":
		soco.SoCo("192.168.1.127").balance = (100,0)
		soco.SoCo("192.168.1.127").play()
		print("guest room should be playing music now...")
		return True
	elif switch == "off":
		soco.SoCo("192.168.1.127").stop()
		print("guest room turned off...")
		return True
	else:
		print("Error in option choice")
		return False

if options.list:
	get_rooms()	
if options.family is not None:
	family_room(options.family)
if options.guest is not None:
	guest_room(options.guest)
