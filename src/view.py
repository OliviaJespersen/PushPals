import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame, ScrolledText


class View:
    def __init__(self, window):
        self.window = window

    def build_gui(self):
        frm_send_center = ttk.Frame(master=self.window)
        frm_send_center.pack(fill=X, side=BOTTOM, padx=10, pady=10)

        self.btn_send = ttk.Button(master=frm_send_center, text="Send", bootstyle=SUCCESS)
        self.btn_send.pack(side=RIGHT)

        self.ent_message = ttk.Entry(master=frm_send_center)
        self.ent_message.pack(fill=X)

        self.frm_messages = ScrolledFrame(master=self.window, autohide=True)
        self.frm_messages.pack(fill=BOTH, expand=YES, padx=10, pady=(10,0))

    def load_messages(self, messages):
        for widget in self.frm_messages.winfo_children():
            widget.destroy()

        for message in messages:
            frm_info = ttk.Frame(master=self.frm_messages)
            frm_info.pack(fill=X)
            name = ttk.Label(frm_info, text=message[0], bootstyle=SUCCESS)
            name.pack(anchor=W, side=LEFT)
            time = ttk.Label(frm_info, text=message[1], bootstyle=SECONDARY)
            time.pack(anchor=E, side=RIGHT)
            text = ttk.Label(self.frm_messages, wraplength=460, text=message[2])
            text.pack(anchor=W, fill=X)
            separator = ttk.Separator(master=self.frm_messages)
            separator.pack(fill=X)

    def get_message(self):
        message = self.ent_message.get()
        self.ent_message.delete(0, END)
        return message

    def bind_send_button(self, command):
        self.btn_send.config(command=command)