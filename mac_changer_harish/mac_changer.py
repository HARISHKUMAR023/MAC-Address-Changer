import pyfiglet
import subprocess
import optparse


ascii__banner= pyfiglet.figlet_format("    MAC CHANNER-Hari")
print(ascii__banner)

interface= input("Enter the interface name :>")
new_mac = input("enter the new mac address :> ")
print('[+] Change Mac address for '+interface+" to "+new_mac)

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether", new_mac])
subprocess.call(["ifconfig",interface,"up"])
