import ttkbootstrap as ttk
import json
import os
import sys
from model import Model
from view import View
from controller import Controller


def read_config_file(file_path):
    with open(file_path, "r") as config_file:
        config_data = json.load(config_file)
    return config_data


def pull_data():
    controller.update_view()
    window.after(1000, pull_data)

config_data = read_config_file(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json'))

model = Model(config_data["auth_token"], config_data["repo"], time_zone=config_data["time_zone"])

window = ttk.Window(title="PushPals", themename=config_data["theme"], resizable=(False, False))
window.geometry("500x800")
view = View(window)
view.build_gui()

controller = Controller(model, view)

pull_data()

window.mainloop()
