from model import Model
from view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.old_messages = []

        self.view.bind_send_button(self.send_message)
        
        self.update_view()


    def send_message(self):
        message = self.view.get_message()
        self.model.send_message(message)
        self.update_view()

    def update_view(self):
        messages = self.model.get_messages()
        if messages != self.old_messages:
            self.old_messages = messages
            self.view.load_messages(messages)
