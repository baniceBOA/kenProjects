from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import os

#local import 
from func import maximum_height, horizontal_distance, flight_time



class MainApp(MDApp):
    def build(self):
        return Builder.load_file(os.path.join(os.path.dirname(__file__), "main.kv"))
    def calculate_output(self):
        try:
            launch_velocity = float(self.root.ids.launch_velocity.text)
            launch_angle = float(self.root.ids.launch_angle.text)
            
            max_height = maximum_height(launch_velocity, launch_angle)
            horiz_distance = horizontal_distance(launch_velocity, launch_angle)
            time_of_flight = flight_time(launch_velocity, launch_angle) * 2  # Total time of flight is double the time to reach max height
            
            self.root.ids.output_maximum_height.text = f"Maximum Height: {max_height:.2f} meters"
            self.root.ids.output_horizontal_distance.text = f"Horizontal Distance: {horiz_distance:.2f} meters"
            self.root.ids.output_time_taken.text = f"Time of Flight: {time_of_flight:.2f} seconds"
        except ValueError:
            self.root.ids.output_maximum_height.text = "Please enter valid numbers for velocity and angle."
            self.root.ids.output_horizontal_distance.text = ""
            self.root.ids.output_time_taken.text = ""

if __name__ == '__main__':
    MainApp().run()