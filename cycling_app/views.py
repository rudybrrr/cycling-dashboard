from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from . import app
from .database import insert_ride, get_rides, get_stats

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST": 
        distance = request.form.get('distance')
        duration = request.form.get('duration')
        date = request.form.get('date')
        insert_ride(distance, duration, date)
        flash(f"Ride logged! Distance: {distance}km, Duration: {duration}mins, Date: {date}")
        return redirect(url_for('home'))
    else:
        stats = get_stats()
        rides = get_rides()
        return render_template(
            "home.html", 
            stats=stats, 
            rides=rides
        )