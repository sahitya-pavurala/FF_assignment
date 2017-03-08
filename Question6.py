import Tkinter as tk
from collections import defaultdict
import json


class CityInfoMap:

    def __init__(self, master):
        """
        Initializer for the class
        :param master: Tkinter master
        """
        self.master = master
        self.frame = tk.Frame(self.master, width=300, height=200)
        self.master.title('City Information')
        self.city_dict = defaultdict(list)
        with open('ca.json') as data_file:
            json_data = json.load(data_file)
        for city in json_data:
            if city["name"] not in self.city_dict and city["full_county_name"] is not None \
                    and city["primary_latitude"] is not None and city["primary_longitude"] is not None:
                self.city_dict[city["name"]] = [city["full_county_name"], city["primary_latitude"],
                                               city["primary_longitude"]]
        self.create_ui(master)

    def display(self, master):
        """
        Method to set parameters for the diplay
        :param master: Tkinter master
        :return: None
        """
        self.county_entry.delete(0, 'end')
        self.lat_entry.delete(0, 'end')
        self.lng_entry.delete(0, 'end')
        self.county_entry.insert(0, self.city_dict[self.city_menu_str.get()][0])
        self.lat_entry.insert(0, self.city_dict[self.city_menu_str.get()][1])
        self.lng_entry.insert(0, self.city_dict[self.city_menu_str.get()][2])

    def create_ui(self, master):
        """
        Method to create the UI
        :param master: Tkinter master
        :return: None
        """
        self.city_menu_str = tk.StringVar()
        self.city_menu = tk.OptionMenu(master,
                                       self.city_menu_str,
                                       *self.city_dict.keys(), command=self.display)
        self.city_menu.configure(width=20)
        self.county_entry_var = tk.StringVar()
        self.county_entry = tk.Entry(master, width=20)
        self.lat_entry_var = tk.StringVar()
        self.lat_entry = tk.Entry(master, width=20)
        self.lng_entry_var = tk.StringVar()
        self.lng_entry = tk.Entry(master, width=20)

        self.city_label = tk.Label(master, text="City", justify='left').grid(sticky='W', pady=20, row=0, column=0)
        self.city_menu.grid(padx=50, row=0, column=1)
        self.county_label = tk.Label(master, text="County", justify='left').grid(sticky='W', pady=20, row=1, column=0)
        self.county_entry.grid(padx=50, row=1, column=1)
        self.lat_label = tk.Label(master, text="Latitude", justify='left').grid(sticky='W', pady=20, row=2,
                                                                                    column=0)
        self.lat_entry.grid(padx=50, row=2, column=1)
        self.lng_label = tk.Label(master, text="Longitude", justify='left').grid(sticky='W', pady=20, row=3,
                                                                                      column=0)
        self.lng_entry.grid(padx=50, row=3, column=1)

    def run_app(self, root):
        """
        Method to run the app
        :param root: tk object
        :return: None
        """
        root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = CityInfoMap(root)
    app.run_app(root)
