```.py


import hashlib, binascii, os
import sys

from kivy.lang import Builder
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

from kivy.uix.behaviors import ButtonBehavior
from sqlalchemy.sql.functions import current_user

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.label import Label
from datetime import date
from kivymd.uix.list import OneLineListItem

Base = declarative_base()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ScreenManagement(ScreenManager):
    pass


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(256), unique=True)
    password = Column(String)


    # relationship "has in the ER diagram" one-to-many
    trading_partners = relationship("TradingPartner", backref="user")




class TradingPartner(Base):
    __tablename__ = "trading_partner"
    id = Column(Integer, primary_key=True, autoincrement=True)
    trading_partner_name = Column(String)
    supplier_name = Column(String)
    sector = Column(String)
    contract_days = Column(Integer)
    priority_rank = Column(Integer)
    remit_to_bank_account_name = Column(String)
    remit_to_bank_account_number = Column(Integer)

    trading_partner_added_by_user = Column(String, ForeignKey("user.username"))
####PROBLEM STARTS FROM BELOW HERE:

    # invoices = relationship("Invoice", backref="trading_partner")

##problem is with these two below:
    # trading_partner_id = relationship("Invoice", primaryjoin="trading_partner.id == Invoice.trading_partner_id")
    # trading_partner = relationship("Invoice", backref="trading_partner",
    #                                   primaryjoin="trading_partner.trading_partner_name == Invoice.trading_partner")


class Invoice(Base):
    __tablename__ = "invoice"
    id = Column(Integer, primary_key=True, autoincrement=True)

    trading_partner_id = Column(Integer, ForeignKey("trading_partner.id"))
    trading_partner_name = Column(String, ForeignKey("trading_partner.trading_partner_name"))

    id_relationship = relationship('TradingPartner', backref='tradingid', foreign_keys=[trading_partner_id])
    name_relationship = relationship('TradingPartner', backref='tradingname', foreign_keys=[trading_partner_name])

    invoice_date = Column(String)
    invoice_amount = Column(String)
    invoice_currency = Column(String)
    invoice_added_date = Column(String)
    tax = Column(Integer)
    description = Column(String)
    expired_contract_date = Column(String)
    actual_payment_date = Column(String)
    actual_payment_accepted_by = Column(String)
    overdue_period = Column(Integer)
    notes_for_penalty_overdue = Column(String)
    paid = Column(Float)
    paid_amount = Column(Integer)
    payment_unpaid_amount = Column(Integer)
    payment_date1 = Column(String)
    payment_date2 = Column(String)

    invoice_added_by_user = Column(String, ForeignKey("user.username"))




# create the database and the connection
from sqlalchemy import create_engine

engine = create_engine('sqlite:///financiaz.db')

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
##########

# class TestingScreen(MDScreen):
#
#     def on_pre_enter(self, *args):
#         self.test()
#
#     def test(self):
#         s = session()
#         date1 = s.query(Test).filter_by(id=1).first()
#
#         print(date1.invoice_date)
#         print(date1.trading_partner_name)

# class TableScreen(MDScreen):
#
#     # Function that prints all activity data on the screen
#     def print_data(self):
#         # Clearing all the widgets(in this case text) on the page
#         # to prevent redundancy of the data
#         self.ids.container.clear_widgets()
#         # Getting data from the database
#         s = session()
#         order_check = s.query(Snack).filter_by(user_id=LoginScreen.current_user).all()
#
#         # Creating labels - Headings for the columns
#         snack_name = MDLabel(text="Snack name", font_style="H4", halign="center")
#         self.ids.container.add_widget(snack_name)
#         amount = MDLabel(text="Amount", font_style="H4", halign="center")
#         self.ids.container.add_widget(amount)
#         price = MDLabel(text="Price", font_style="H4", halign="center")
#         self.ids.container.add_widget(price)
#
#         # display the data such as type of the activity, distance, date
#         for data in order_check:
#             snack_name = MDLabel(text=str(data.name), halign="center")
#             self.ids.container.add_widget(snack_name)
#             amount = MDLabel(text=str(data.amount), halign="center")
#             self.ids.container.add_widget(amount)
#             price = MDLabel(text=str(data.price), halign="center")
#             self.ids.container.add_widget(price)


# class ImageScreen(MDScreen):
#
#     def go_back_to_order(self):
#         self.parent.current = "SnackScreen"


# class MyAccountScreen(MDScreen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.delivery_location = LoginScreen.delivery_location
#         self.email = LoginScreen.email
#
#     def on_pre_enter(self, *args):
#         self.my_account()
#
#     def my_account(self):
#         self.ids.delivery_location.text = f"Your delivery location: {LoginScreen.delivery_location}"
#         self.ids.email.text = f"Your email: {LoginScreen.email}"
#
#     def home_page(self):
#         self.parent.current = "HomeScreen"


# class ThankyouScreen(MDScreen):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.delivery_location = LoginScreen.delivery_location
#
#     def on_pre_enter(self, *args):
#         self.thankyou()
#
#     def thankyou(self):
#         LoginScreen.delivery_location.strip()
#         self.ids.location_thankyou.text = f"Your order will arrived to your delivery location ( {LoginScreen.delivery_location}) in under 30 minutes."
#
#     def home_page(self):
#         self.parent.current = "HomeScreen"
#
#
# class CheckoutScreen(MDScreen):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.id = LoginScreen.current_user
#         self.delivery_location = LoginScreen.delivery_location
#
#     def on_pre_enter(self, *args):
#         self.checkout()
#
#     def checkout(self):
#         order_list = ""
#         price = 0
#         s = session()
#         order_check = s.query(Snack).filter_by(user_id=LoginScreen.current_user).all()
#
#         print(f"Delivery location is at {LoginScreen.delivery_location}")
#         print(f"Total order of user with id {LoginScreen.delivery_location}:")
#         for i in range(len(order_check)):
#             order_list += '\n' + "| No." + str(i + 1) + " | " + "Name: " + str(
#                 order_check[i].name).capitalize() + "| Amount: " + str(order_check[i].amount) + " | Price: " + str(
#                 order_check[i].price) + "¥ |"
#             price += order_check[i].price
#         print(order_list)
#
#         self.ids.my_orders.text = order_list
#
#         self.ids.delivery_location.text = f"Delivery location: {LoginScreen.delivery_location}"
#
#         self.ids.total_price.text = f"Total cost: {price}¥"
#
#     def confirm_order(self):
#         print("Confirm button was clicked")
#         self.parent.current = "ThankyouScreen"
#
#     def go_back_to_order(self):
#         self.parent.current = "SnackScreen"
#
#
# class SnackScreen(MDScreen):
#
#     # string123 = StringProperty("")
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.id = LoginScreen.current_user
#
#     def see_snacks(self):
#         self.parent.current = "ImageScreen"
#
#     def check_out(self):
#         print("Checkout button was pressed")
#         self.parent.current = "CheckoutScreen"
#
#     def add_to_cart(self):
#         price_per_product = 0
#         print("Add to cart button was pressed")
#         # print(LoginScreen.current_user) #LoginScreen.current_user is the id of the user
#         user_id = LoginScreen.current_user
#         snack_name = self.ids.snack_name.text
#         amount = self.ids.snack_amount.text
#
#         if snack_name != "Hamburger" and snack_name != "hamburger" and snack_name != "Coke" and snack_name != "coke" and snack_name != "Popcorn" \
#                 and snack_name != "popcorn":
#
#             print("Invalid food order")
#
#         elif amount.isnumeric() == False:
#             print("Invalid amount")
#
#         else:
#
#             if int(amount) > 50 or int(amount) < 1:
#                 print("The ordering amount is too much or too little.")
#             else:
#                 if (snack_name == "Hamburger" or snack_name == "hamburger"):
#                     price_per_product = 300
#
#
#                 elif (
#                         snack_name == "Coke" or snack_name == "coke" or snack_name == "Popcorn" or snack_name == "popcorn"):
#                     price_per_product = 100
#
#                 price = int(int(amount) * price_per_product)
#                 print(user_id, snack_name, int(amount), price)
#
#                 amount = int(amount)
#                 price = int(price)
#
#                 s = session()
#                 order = Snack(name=snack_name, amount=amount, price=price, user_id=user_id)
#                 s.add(order)
#                 s.commit()
#                 s.close()
#
#                 print(
#                     "order from user with user id {}: snack_name: {} , amount: {}, price {} was added to database Snack".format(
#                         user_id, snack_name, amount, price))
#
#     def home_page(self):
#         self.parent.current = "HomeScreen"


class HomeScreen(MDScreen):

    def add_invoices(self):
        print("Add invoices button clicked")
        # self.parent.current = "MyAccountScreen"

    def filter_search_invoice(self):
        print("Filter/search invoices button clicked")
        # self.parent.current = "SnackScreen"

    def generate_reports(self):
        print("Generate reports button clicked")
        # self.parent.current = "SnackScreen"

    def log_out(self):
        self.parent.current = "LoginScreen"

    # def orders_check(self):
    #     self.parent.current = "TableScreen"


class RegisterScreen(MDScreen):

    def try_register(self):

        print("Register was attempted")
        username = self.ids.username_input.text
        password_add = self.ids.password_input.text
        password_repeat = self.ids.password_check.text
        print(username, password_add, password_repeat)

        if password_add == password_repeat:
            s = session()
            username = self.ids.username_input.text
            password = self.ids.password_input.text
            print(username, password)

            username_check = s.query(User).filter_by(username=username).first()  ##similar to fetchone()

            if username_check:
                print("User already exists")
                s.close()

            else:
                salt = hashlib.sha256(os.urandom(60)).hexdigest().encode(
                    'ascii')  # hashing a ramdom sequence with 60 bits: produces 256 bits or 64 hex chars

                pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),
                                              salt, 100000)

                pwdhash = binascii.hexlify(pwdhash)

                hashed_password = (salt + pwdhash).decode('ascii')

                user = User(username=username,
                            password=hashed_password)  # change password=hashed_password
                s.add(user)

                s.commit()
                s.close()

                self.parent.current = "LoginScreen"

        else:
            print("The passwords do not match")

    def switch_to_login(self):
        self.parent.current = "LoginScreen"


class ButtonLabel(ButtonBehavior, MDLabel):
    pass


class LoginScreen(MDScreen):
    current_user = None
    username = None

    def try_login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        print(username, password)
        s = session()

        user_check = s.query(User).filter_by(username=username).first()

        stored_password = user_check.password

        salt = stored_password[:64]
        stored_password = stored_password[64:]

        pwdhash = hashlib.pbkdf2_hmac('sha256',
                                      password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)

        pwdhash = binascii.hexlify(pwdhash).decode('ascii')

        if pwdhash == stored_password:
            s.close()
            print(f"login successful for user {username}")
            LoginScreen.current_user = user_check.username # getting the username of the current user
            self.parent.current = "HomeScreen"
        else:
            print("User does not exist or wrong password/username")


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Indigo"




MainApp().run()








```
