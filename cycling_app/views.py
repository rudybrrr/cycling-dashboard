from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from . import app
from .database import insert_ride, get_rides, get_stats
import calendar

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST": 
        distance = request.form.get('distance')
        duration = request.form.get('duration')
        date = request.form.get('date')
        if float(distance) > 0 and float(duration) > 0: 
            insert_ride(distance, duration, date)
            flash(f"Ride logged! Distance: {distance}km, Duration: {duration}mins, Date: {date}")
        else: 
            flash("Invalid values. Distance and duration must be greater than 0.")
        return redirect(url_for('home'))
    else:
        stats = get_stats()
        rides = get_rides()
        return render_template(
            "home.html", 
            stats=stats, 
            rides=rides
        )

@app.route("/stats/")
def stats(): 
    stats = get_stats()
    rides = get_rides()
    ride_dates = {ride[3] for ride in rides}
    today = datetime.now()
    month_name = today.strftime("%B")
    cal = calendar.monthcalendar(today.year, today.month)
    print(ride_dates)
    return render_template(
        "stats.html",
        stats=stats,  
        rides=rides, 
        ride_dates=ride_dates,
        month = today.month,
        year = today.year, 
        month_name=month_name,
        cal=cal
    )