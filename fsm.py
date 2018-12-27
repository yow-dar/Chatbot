from transitions.extensions import GraphMachine

from utils import send_text_message
import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def is_going_to_demo(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'demo'
        return False
    def is_going_to_eat(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'hungry'
        return False
    def is_going_to_search(self, update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'search'
        return False

    def is_going_to_google(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']        
            sender_id = update['sender']['id']
            send_text_message(sender_id,"https://www.google.com.tw/maps/search/"+text)
            return text.lower() == 'Bye Bye'
        return False
    def is_going_to_fastfood(self, update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'fast food'
        return False
    def is_going_to_fried(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'fried'
        return False
    def is_going_to_nonfried(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'non-fried'
        return False
    def is_going_to_food(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'normal food'
        return False
    def is_going_to_expensive(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'expensive'
        return False
    def is_going_to_cheap(self,update):
        if update.get("message") and update['message'].get("text"):
            text = update['message']['text']
            return text.lower() == 'cheap'
        return False
    def on_enter_eat(self, update):
        if update.get("message") and update['message'].get("text"):
            #print("I'm entering eat state.")
            sender_id = update['sender']['id']
            send_text_message(sender_id,"search for restaurant?Please type:search")
            send_text_message(sender_id,"want to eat fastfood? Please type:fast food")
            send_text_message(sender_id,"Want to eat normal food? Please type:normal food")
        return False
    def on_enter_demo(self,update):
        if update.get('message') and update['message'].get("text"):
            sender_id = update'[sender']['id']
            sender_text_message(sender_id,"Demo")
            self.go_back(update)
        return False
    def on_exit_eat(self, update):
        if update.get("message") and update['message'].get("text"):
            print('Leaving eat')
        return False
    def on_enter_search(self, update):
        if update.get("message") and update['message'].get("text"):
            sender_id = update['sender']['id']
            send_text_message(sender_id,"Please type where do you want to find?")
            send_text_message(sender_id,"輸入你想找的店")
        #self.go_back(update)
        return False
    def on_exit_search(self, update):
        if update.get("message") and update['message'].get("text"):
            print('Leaving search')
        return False
    def on_enter_google(self, update):
        if update.get("message") and update['message'].get("text"):
            sender_id = update['sender']['id']
            send_text_message(sender_id,"See you, guy.")
            self.go_back(update)
        return False
    def on_exit_google(self, update):
        return False
    def on_enter_fastfood(self, update):
        if update.get("message") and update['message'].get("text"):
            sender_id = update['sender']['id']
            send_text_message(sender_id,"fried or non-fried?")
        return False
    def on_exit_fastfood(self, update):
        if update.get("message") and update['message'].get("text"):
            print('Leaving fastfood')
        return False
    def on_enter_fried(self,update):
        i = random.randint(1,4)
        if update.get("message") and update['message'].get("text"):
            if i == 1:
                what="McDonald"
            elif i == 2:
                what="KFC"
            elif i == 3:
                what="Mos"
            elif i == 4:
                what="21Century"
            print(what,"Hello")
            sender_id = update['sender']['id']
            send_text_message(sender_id,what)
            self.go_back(update)
        return False
        j = random.randint(1,2)
        if update.get("message") and update['message'].get("text"):
            if j == 1:
                where="for here"
            elif j == 2:
                where="to go"
            sender_id = update['sender']['id']
            send_text_message(sender_id,where)
            send_text_message(sender_id,"See you,guy.")
            #self.go_back(update)
        return False
    def on_exit_fried(self,update):
        if update.get("message") and update['message'].get("text"):
            print("exit fried")
        return False
    def on_enter_nonfried(self,update):
        i = random.randint(1,3)
        if update.get("message") and update['message'].get("text"):
            if i == 1:
                what="PizzaHut"
            elif i == 2:
                what="Subway"
            elif i == 3:
                what="Dandan"
            sender_id = update['sender']['id']
            send_text_message(sender_id,what)
            self.go_back(update)
        return False
        j = random.randint(1,2)
        if update.get("message") and update['message'].get("text"):
            if j == 1:
                where="for here"
            elif j == 2:
                where="to go"
            sender_id = update['sender']['id']
            send_text_message(sender_id,where)
            send_text-message_text(sender_id,"See you, guy.")
        return False
    def on_exit_nonfried(self,update):
        if update.get("message") and update['message'].get("text"):
            print("leaving nonfried")
        return False
    def on_enter_food(self, update):
        if update.get("message") and update['message'].get("text"):
            sender_id = update['sender']['id']
            send_text_message(sender_id,"expensive or cheap?")
	    #self.go_back(update)
        return False
    def on_exit_food(self, update):
        if update.get("message") and update['message'].get("text"):
            print('Leaving food')
        return False
    def on_enter_expensive(self,update):
        i = random.randint(1,5)
        if update.get("message") and update['message'].get("text"):
            if i == 1:
                what="哞王"
            elif i == 2:
                what="澄花"
            elif i == 3:
                what="西提"
            elif i == 4:
                what="陶板屋"
            elif i == 5:
                what="覺丸拉麵"
            #print(what)
            sender_id = update['sender']['id']
            send_text_message(sender_id,what)
            self.go_back(update)
        return False
        j = random.randint(1,2)
        if update.get("message") and update['message'].get("text"):
            if j == 1:
                where="for here"
            elif j == 2:
                where="to go"
            send_text_message(sender_id,where)
            update.message.reply_text("See you, guy.")
            self.go_back(update)
        return False
    def on_exit_expensive(self,update):
        if update.get("message") and update['message'].get("text"):
            print("leaving expensive")
        return False
    def on_enter_cheap(self,update):
        i = random.randint(1,16)
        if update.get("message") and update['message'].get("text"):
            if i == 1:
                what="不倒翁"
            elif i == 2:
                what="7-11"
            elif i == 3:
                what="勝利早點"
            elif i == 4:
                what="四海遊龍"
            elif i == 5:
                what="甜麵屋"
            elif i == 6:
                what="煦悅"
            elif i == 7:
                what="活力小廚"
            elif i == 8:
                what="阿甘"
            elif i == 9:
                what="小妞"
            elif i == 10:
                what="原味屋"
            elif i == 11:
                what="甜麵屋"
            elif i == 12:
                what="阿閔"
            elif i == 13:
                what="紅樓小館"
            elif i == 14:
                what="雅味"
            elif i == 15:
                what="小廚師"
            elif i == 16:
                what="炒翻天"
            #print(what)
            sender_id = update['sender']['id']
            send_text_message(sender_id,what)
            self.go_back(update)
        return False
        j = random.randint(1,2)
        if update.get("message") and update['message'].get("text"):
            if j == 1:
                where="for here"
            elif j == 2:
                where="to go"  
            send_text_message(sender_id,where)
            send_text_message(sender_id,"See you, guy.")
            self.go_back(update)
        return False
    def on_exit_cheap(self,update):
        if update.get("message") and update['message'].get("text"):
            print("leaving cheap")
        return False
