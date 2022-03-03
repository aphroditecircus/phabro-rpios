import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

pins = {
    27: {'name': 'GPIO27', 'state': GPIO.LOW},
    22: {'name': 'GPIO22', 'state': GPIO.LOW},
    17: {'name': 'GPIO17', 'state': GPIO.LOW},
    4:  {'name': 'GPIO4' , 'state': GPIO.LOW},
}

