from flask import Flask, render_template,request
import requests
app=Flask(__name__)
api_key="32204b77b4288b74b754520d0d54558a"
@app.route("/", methods=["GET", "POST"])


def home():
    weather_data=None
    error_message=None

    if request.method=="POST":
        city=request.form.get("city").strip()
        base_url="https://api.openweathermap.org/data/2.5/weather"

        param={
            "q":city,
            "appid":api_key,
            "units":"metric"
        }
        try:
            response=requests.get(base_url,params=param)
            response.raise_for_status()
            data=response.json()
            weather_data={
                "city":data["name"],
                "country":data["sys"]["country"],
                "temp":data["main"]["temp"],
                "feels_like":data["main"]["feels_like"],
                "humidity":data["main"]["humidity"],
                "condition":data["weather"][0]["description"],
                "wind_speed":data["wind"]["speed"]
            }
        except:
            error_message="error"

    return render_template("report.html", weather=weather_data, error=error_message)

if __name__=="__main__":
    app.run(debug=True)