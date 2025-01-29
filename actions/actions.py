from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionOpenTicket(Action):
    def name(self) -> str:
        return "action_open_ticket"

    def run(self, dispatcher, tracker, domain):
        # Simulamos la apertura de un ticket
        dispatcher.utter_message(text="He creado un ticket para ti. El equipo de soporte se pondrá en contacto pronto.")
        return []
