
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
from kivymd.uix.datatables import MDDataTable
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
from kivy.metrics import dp


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

class FilterSearchInvoiceScreen(MDScreen):
    #variables will needed to be created in this screen
    #to hold the input filtered/searched info
    #in order to pass it to the Filtered/Searched display screen
    #where these variable can tell the class in that display screen
    #what to do in order to query up the database:
    #all the codes to logically uses these info will be in the
    #codes of the display screen

    invoice_number = None
    supplier_name = None
    invoices_added_date_from = None
    invoices_added_date_to = None
    invoices_date_from = None
    invoices_date_to = None
    payment_status = None
    display_all = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self, *args):
        self.request_items()

    def request_items(self):
        menu_items = [{"text": "Paid"}, {"text": "Not paid"}, {"text": "Partial paid"}, {"text": "Every status"}]
        self.menu = MDDropdownMenu(
            caller = self.ids.payment_status_input,
            items = menu_items,
            position = "center",
            width_mult = 2.25,
        )
        self.menu.bind(on_release=self.set_item)


    def set_item(self, instance_menu, instance_menu_item):
        self.ids.payment_status_input.set_item(instance_menu_item.text)
        FilterSearchInvoiceScreen.payment_status = instance_menu_item.text
        instance_menu.dismiss()
        print(FilterSearchInvoiceScreen.payment_status)


    def filter_search_invoices(self):
        print("Filter/search button clicked")

        # if self.ids.payment_status_no_need:
        #     print("deactivate filter/search for payment_status ")
        #     FilterSearchInvoiceScreen.payment_status = "None"
        # if (not self.ids.payment_status_no_need) or...


        if len(self.ids.invoice_number_input.text)>0 or len(self.ids.supplier_name_input.text)>0 or len(self.ids.invoices_added_date_from_input.text)>0 or len(self.ids.invoices_added_date_to_input.text)>0 or len(self.ids.invoices_date_from_input.text)>0 or len(self.ids.invoices_date_to_input.text)>0 or ((FilterSearchInvoiceScreen.payment_status == "Paid") or (FilterSearchInvoiceScreen.payment_status =="Not paid") or (FilterSearchInvoiceScreen.payment_status=="Partial paid")):
            FilterSearchInvoiceScreen.display_all = 0
            print("Pls do not display all")

            FilterSearchInvoiceScreen.invoice_number = self.ids.invoice_number_input.text
            FilterSearchInvoiceScreen.supplier_name = self.ids.supplier_name_input.text
            FilterSearchInvoiceScreen.invoices_added_date_from = self.ids.invoices_added_date_from_input.text
            FilterSearchInvoiceScreen.invoices_added_date_to = self.ids.invoices_added_date_to_input.text
            FilterSearchInvoiceScreen.invoices_date_from = self.ids.invoices_date_from_input.text
            FilterSearchInvoiceScreen.invoices_date_to = self.ids.invoices_date_to_input.text
            FilterSearchInvoiceScreen.payment_status = FilterSearchInvoiceScreen.payment_status

        else:
            print("Pls display all")



        #if no info is input in the screen and the Filter/search button is clicked,
        #this means that the client wants to see every invoices in the database.:
        #and we keep the variable "display_all" to 0, where in the codes of the display screen,
        #there will be something like if display_all = 1 =>query everything

        self.parent.current = "Filtered_searched_display_Screen"

    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"


##Magic code below:
##the code below help make all item in all_data from the table iterable:
def to_dict(row):
    if row is None:
        return None

    # creates a dictionary:
    rtn_dict = dict()
    # converts the column headers of the table into the keys of the dictionary
    keys = row.__table__.columns.keys()

    for key in keys:
        rtn_dict[key] = getattr(row, key)
    return rtn_dict

def words_extract(row):
    row = str(row)
    stripped_row = "("

    row=list(row)

    for item in row[13:]:
        if item != "]":
            stripped_row += item

    return stripped_row

class Filtered_searched_display_Screen(MDScreen):


    def on_pre_enter(self, *args):

        invoice_number = FilterSearchInvoiceScreen.invoice_number
        supplier_name = FilterSearchInvoiceScreen.supplier_name
        invoices_added_date_from = FilterSearchInvoiceScreen.invoices_added_date_from
        invoices_added_date_to = FilterSearchInvoiceScreen.invoices_added_date_to
        invoices_date_from = FilterSearchInvoiceScreen.invoices_date_from
        invoices_date_to = FilterSearchInvoiceScreen.invoices_date_to
        payment_status = FilterSearchInvoiceScreen.payment_status
        display_all = FilterSearchInvoiceScreen.display_all


        print(invoice_number, supplier_name, invoices_added_date_from, invoices_added_date_to,
              invoices_date_from, invoices_date_to, payment_status, display_all)

        if display_all == 1:
            print("Received message display all")

            # Getting data from the database
            s = session()
            query_all = s.query(Invoice).all()
            print(query_all)

            # Creating labels - Headings for the columns
            id = MDLabel(text="No.", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(id)
            trading_partner_name = MDLabel(text="Trading partner name", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(trading_partner_name)
            invoice_number = MDLabel(text="Invoice number", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_number)
            invoice_date = MDLabel(text="Invoice date", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_date)
            invoice_amount = MDLabel(text="Invoice amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_amount)
            invoice_currency = MDLabel(text="Invoice currency", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_currency)
            invoice_added_date = MDLabel(text="Invoice added date", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_added_date)
            tax = MDLabel(text="Tax", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(tax)
            description = MDLabel(text="Description", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(description)
            expired_contract_date = MDLabel(text="Expired contract date", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(expired_contract_date)
            actual_payment_date = MDLabel(text="Actual payment date", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(actual_payment_date)
            actual_payment_accepted_by = MDLabel(text="Actual payment date accepted by", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(actual_payment_accepted_by)
            overdue_period = MDLabel(text="Overdue period", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(overdue_period)

            notes_for_penalty_overdue = MDLabel(text="Notes for penalty overdue", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(notes_for_penalty_overdue)

            paid = MDLabel(text="Paid? (1=paid, 0.5=partial paid, 0=unpaid)", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid)

            paid_amount = MDLabel(text="Paid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid_amount)

            payment_unpaid_amount = MDLabel(text="Unpaid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_unpaid_amount)

            payment_date1  = MDLabel(text="Payment date 1", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date1 )

            payment_date2 = MDLabel(text="Payment date 2", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget( payment_date2)

            occurent = MDLabel(text="Occurent", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(occurent)

            invoice_added_by_user = MDLabel(text="Invoices added by user:", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_added_by_user)

            #display the queried data:
            for data in query_all:
                id = MDLabel(text=str(data.id), halign="center")
                self.ids.container.add_widget(id)
                trading_partner_name = MDLabel(text=str(data.trading_partner_name), halign="center")
                self.ids.container.add_widget(trading_partner_name)
                invoice_number = MDLabel(text=str(data.invoice_number), halign="center")
                self.ids.container.add_widget(invoice_number)

                invoice_date = MDLabel(text=str(data.invoice_date), halign="center")
                self.ids.container.add_widget(invoice_date)

                invoice_amount = MDLabel(text=str(data.invoice_amount), halign="center")
                self.ids.container.add_widget(invoice_amount)

                invoice_currency = MDLabel(text=str(data.invoice_currency), halign="center")
                self.ids.container.add_widget(invoice_currency)

                invoice_added_date = MDLabel(text=str(data.invoice_added_date), halign="center")
                self.ids.container.add_widget(invoice_added_date)

                tax = MDLabel(text=str(data.tax), halign="center")
                self.ids.container.add_widget(tax)

                description  = MDLabel(text=str(data.description), halign="center")
                self.ids.container.add_widget(description )

                expired_contract_date = MDLabel(text=str(data.expired_contract_date), halign="center")
                self.ids.container.add_widget(expired_contract_date)

                actual_payment_date = MDLabel(text=str(data.actual_payment_date), halign="center")
                self.ids.container.add_widget(actual_payment_date)

                actual_payment_accepted_by = MDLabel(text=str(data.actual_payment_accepted_by), halign="center")
                self.ids.container.add_widget(actual_payment_accepted_by)

                overdue_period  = MDLabel(text=str(data.overdue_period ), halign="center")
                self.ids.container.add_widget(overdue_period )

                notes_for_penalty_overdue = MDLabel(text=str(data.notes_for_penalty_overdue), halign="center")
                self.ids.container.add_widget(notes_for_penalty_overdue)

                paid = MDLabel(text=str(data.paid), halign="center")
                self.ids.container.add_widget(paid)

                paid_amount = MDLabel(text=str(data. paid_amount), halign="center")
                self.ids.container.add_widget( paid_amount)

                payment_unpaid_amount = MDLabel(text=str(data.payment_unpaid_amount), halign="center")
                self.ids.container.add_widget(payment_unpaid_amount)

                payment_date1 = MDLabel(text=str(data.payment_date1), halign="center")
                self.ids.container.add_widget(payment_date1)

                payment_date2 = MDLabel(text=str(data.payment_date2), halign="center")
                self.ids.container.add_widget(payment_date2)

                occurent = MDLabel(text=str(data.occurent), halign="center")
                self.ids.container.add_widget(occurent)

                invoice_added_by_user = MDLabel(text=str(data.invoice_added_by_user), halign="center")
                self.ids.container.add_widget(invoice_added_by_user)




    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"



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
        self.parent.current = "FilterSearchInvoiceScreen"

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
        self.theme_cls.primary_palette = "BlueGray"





MainApp().run()





