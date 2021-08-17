
import hashlib, binascii, os
import sys
# import time
from datetime import datetime
from datetime import timedelta
from datetime import date

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
from datetime import datetime
from datetime import timedelta
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivymd.color_definitions import colors

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
    remit_to_bank_account_number = Column(String)

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

    invoice_number = Column(String)

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
    occurent = Column(String)

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


class InvoiceScreen(MDScreen):

    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"

    def add_to_database(self):
        print("Add to database button clicked")

        invoice_number = self.ids.invoice_number_input.text

        invoice_date = self.ids.invoice_date_input.text

        invoice_amount = self.ids.invoice_amount_input.text
        invoice_currency = self.ids.invoice_currency_input.text
        tax = self.ids.tax_input.text
        actual_payment_date = self.ids.actual_payment_date_input.text
        actual_payment_accepted_by = self.ids.actual_payment_accepted_by_input.text
        description = self.ids.description_input.text
        overdue_period = self.ids.overdue_period_input.text
        notes_for_penalty_overdue = self.ids.notes_for_penalty_input.text
        occurent = self.ids.occurent_input.text

        paid_amount = self.ids.paid_amount_input.text
        payment_date1 = self.ids.payment_date1_input.text
        payment_date2 = self.ids.payment_date2_input.text

        # the column "invoice added date" is not filled out by
        # the user. Instead it is added by the program through
        # determining today date (in japan time)
        invoice_added_date = str(date.today())

        invoice_added_by_user = LoginScreen.current_user

        #I need to query the database to check if the trading partner
        #is added or not. If not=> send a message to the user and say
        #that they need to add information about this trading partner
        #first and then come back to this page to add info about the invoice
        #if the trading partner is in the list, set the trading_partner_name column
        #to the input for the trading partner on the program and set the
        #trading_partner_id column by querying using the trading partner name

        trading_partner_name = self.ids.trading_partner_input.text


        s = session()
        trading_partner_check = s.query(TradingPartner).filter_by(trading_partner_name=trading_partner_name).first()
        if trading_partner_check:
            print("Trading partner exists=>good")
            trading_partner_id = trading_partner_check.id
            s.close()

            print(invoice_number, invoice_date, invoice_amount, invoice_currency,
                  tax, actual_payment_date, actual_payment_accepted_by,
                  description, overdue_period, notes_for_penalty_overdue,
                  occurent, paid_amount, payment_date1, payment_date2,
                  invoice_added_by_user, trading_partner_name,
                  trading_partner_id)

            #Need to calculate using filled information to calculate for the "expired_contract_date",
            #"paid", "payment_unpaid_amount"!

            #"expired_contract_date" = "Invoice Date" + "Contract Days"
            invoice_date_datetime = datetime.strptime(invoice_date, "%Y-%m-%d")

            s = session()
            trading_partner_check = s.query(TradingPartner).filter_by(trading_partner_name=trading_partner_name).first()
            contract_days = trading_partner_check.contract_days

            expired_contract_date0 = invoice_date_datetime + timedelta(days=contract_days)
            expired_contract_date = str(expired_contract_date0)

            #"actual_payment_date" is optional and can be entered by the user or
            #calculated by taking the "expired_contract_date" + "overdue_period" (only if
            #the user didn't enter anything because actual_payment_date could be changed
            # even when overdue_period or other elements is not changed)

            #the user might entered overdue period but forgot to also enter actual payment date,
            #so the code below create the actual payment date for the user using the entered
            #overdue period.

            if len(actual_payment_date)== 0 and len(overdue_period) > 0:
                actual_payment_date = str(expired_contract_date0 + timedelta(days=int(overdue_period)))


            #"paid" = 0 if "paid_amount" = 0, = 0.5 if "paid_amount" >0 but <"invoice_amount",
            #= 1 if "paid_amount" = "invoice_amount"

            #payment_unpaid_amount is non-editable by the user, and only created in the backend
            #by the program

            paid = 0

            if len(paid_amount) > 0:

                payment_unpaid_amount = int(invoice_amount) - int(paid_amount)

                if int(paid_amount) > 0 and int(paid_amount) < int(invoice_amount):
                    paid = 0.5
                elif int(paid_amount) == int(invoice_amount):
                    paid = 1
                paid_amount=int(paid_amount)

            else:
                paid_amount = paid_amount
                payment_unpaid_amount = int(invoice_amount)
                paid = 0


            if len(overdue_period) == 0:
                overdue_period = overdue_period
            else:
                overdue_period = int(overdue_period)


            invoice = Invoice(trading_partner_id=trading_partner_id,
                              trading_partner_name=trading_partner_name,
                              invoice_number=invoice_number,
                                             invoice_date=invoice_date,
                                             invoice_amount=int(invoice_amount),
                                             invoice_currency=invoice_currency,
                                             tax=tax,
                                             actual_payment_date=actual_payment_date,
                                             actual_payment_accepted_by=actual_payment_accepted_by,
                                             description=description, overdue_period=overdue_period,
                              notes_for_penalty_overdue=notes_for_penalty_overdue,
                              occurent=occurent, paid_amount=paid_amount,
                              payment_date1=payment_date1, payment_date2=payment_date2,
                              invoice_added_by_user=invoice_added_by_user,
                              expired_contract_date=expired_contract_date,
                              payment_unpaid_amount=payment_unpaid_amount,
                              paid=paid, invoice_added_date=invoice_added_date)  # change password=hashed_password
            s.add(invoice)

            s.commit()
            s.close()

            self.parent.current = "HomeScreen"



        else:
            print("Trading partner didn't exist. Pls add it first before adding an invoice from this trading partner.")
            self.parent.current = "TradingPartnerScreen"



class TradingPartnerScreen(MDScreen):

    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"


    def add_to_database(self):
        print("Add to database button clicked")

        trading_partner_name = self.ids.trading_partner_name_input.text
        supplier_name = self.ids.supplier_name_input.text
        sector = self.ids.sector_input.text
        contract_days = self.ids.contract_days_input.text
        priority_rank = self.ids.priority_rank_input.text
        remit_to_bank_account_name = self.ids.remit_to_bank_account_name_input.text
        remit_to_bank_account_number = self.ids.remit_to_bank_account_number_input.text

        print(trading_partner_name, supplier_name, sector, contract_days, priority_rank,remit_to_bank_account_name,remit_to_bank_account_number, current_user)

        s = session()
        #checking if the trading partner is already added or not:
        trading_partner_check = s.query(TradingPartner).filter_by(trading_partner_name=trading_partner_name).first()
        if trading_partner_check:
            print("Trading partner already exists")
            s.close()
            #HERE, THERE SHOULD BE A CODE THAT SENDS OUT A POP UP ERROR MESSAGE
        else:
            trading_partner = TradingPartner(trading_partner_name=trading_partner_name,
                        supplier_name=supplier_name,
                        sector=sector,
                        contract_days=contract_days,
                        priority_rank=priority_rank,
                        remit_to_bank_account_name=remit_to_bank_account_name,
                        remit_to_bank_account_number=remit_to_bank_account_number,
                        trading_partner_added_by_user=LoginScreen.current_user)  # change password=hashed_password
            s.add(trading_partner)

            s.commit()
            s.close()

            self.parent.current = "HomeScreen"



class AddInvoiceScreen(MDScreen):

    def add_trading_partner(self):
        print("Add fixed data about Trading Partners+ button clicked")
        self.parent.current = "TradingPartnerScreen"

    def add_invoices_real(self):
        print("Add non-fixed data about Invoices+ button clicked")
        self.parent.current = "InvoiceScreen"

    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"

class HomeScreen(MDScreen):

    def add_invoices(self):
        print("Add invoices button clicked")
        self.parent.current = "AddInvoiceScreen"

    def filter_search_invoices(self):
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
            print("The current user is", LoginScreen.current_user)
            self.parent.current = "HomeScreen"
        else:
            print("User does not exist or wrong password/username")


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Indigo"





MainApp().run()





