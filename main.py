import tkinter as tk
from tkinter import messagebox

from weather_fetcher import WeatherFetcher
from database import Database


class WeatherApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Weather Dashboard")

        self.root.geometry("500x500")

        self.fetcher = WeatherFetcher()
        self.db = Database()

        self.create_ui()

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="Weather Dashboard",
            font=("Arial", 20)
        )

        title.pack(pady=10)

        self.city_entry = tk.Entry(
            self.root,
            font=("Arial", 14)
        )

        self.city_entry.pack(pady=10)

        search_btn = tk.Button(
            self.root,
            text="Get Weather",
            command=self.search_weather
        )

        search_btn.pack()

        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14)
        )

        self.result_label.pack(pady=20)

        history_btn = tk.Button(
            self.root,
            text="View History",
            command=self.show_history
        )

        history_btn.pack(pady=10)

    def search_weather(self):

        city = self.city_entry.get()

        try:

            weather = self.fetcher.get_weather(city)

            temp = weather["temperature"]
            wind = weather["windspeed"]

            self.result_label.config(
                text=
                f"City: {city}\n"
                f"Temperature: {temp}°C\n"
                f"Wind Speed: {wind} km/h"
            )

            self.db.save_weather(
                city,
                temp,
                wind
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def show_history(self):

        history_window = tk.Toplevel(self.root)

        history_window.title("History")

        text = tk.Text(history_window)

        text.pack(
            fill="both",
            expand=True
        )

        rows = self.db.get_history()

        for row in rows:

            city, temp, wind, time = row

            text.insert(
                tk.END,
                f"{time}\n"
                f"{city}\n"
                f"Temp: {temp}°C\n"
                f"Wind: {wind} km/h\n\n"
            )


root = tk.Tk()

app = WeatherApp(root)

root.mainloop()