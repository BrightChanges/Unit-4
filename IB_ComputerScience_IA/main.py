
import hashlib, binascii, os
import sys
# import time
from datetime import datetime
from datetime import timedelta
from datetime import date

from kivy.lang import Builder
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, Date, and_
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
from kivymd.uix.behaviors import TouchBehavior

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

    invoice_number = Column(String, unique=True)

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


    # def invoices_added_date(self,value1,value2):
    #     if value



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
    trading_partner_name = None
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


        if len(self.ids.invoice_number_input.text)>0 or len(self.ids.trading_partner_name_input.text)>0 or len(self.ids.invoices_added_date_from_input.text)>0 or len(self.ids.invoices_added_date_to_input.text)>0 or len(self.ids.invoices_date_from_input.text)>0 or len(self.ids.invoices_date_to_input.text)>0 or ((FilterSearchInvoiceScreen.payment_status == "Paid") or (FilterSearchInvoiceScreen.payment_status =="Not paid") or (FilterSearchInvoiceScreen.payment_status=="Partial paid")):
            FilterSearchInvoiceScreen.display_all = 0
            print("Pls do not display all")

            FilterSearchInvoiceScreen.invoice_number = self.ids.invoice_number_input.text
            FilterSearchInvoiceScreen.trading_partner_name = self.ids.trading_partner_name_input.text
            FilterSearchInvoiceScreen.invoices_added_date_from = self.ids.invoices_added_date_from_input.text
            FilterSearchInvoiceScreen.invoices_added_date_to = self.ids.invoices_added_date_to_input.text
            FilterSearchInvoiceScreen.invoices_date_from = self.ids.invoices_date_from_input.text
            FilterSearchInvoiceScreen.invoices_date_to = self.ids.invoices_date_to_input.text
            FilterSearchInvoiceScreen.payment_status = FilterSearchInvoiceScreen.payment_status

            print(FilterSearchInvoiceScreen.payment_status)
            print(FilterSearchInvoiceScreen.invoices_added_date_from)
            if len(FilterSearchInvoiceScreen.invoices_added_date_from)==0:
                print(True)
            if FilterSearchInvoiceScreen.payment_status is None:
                print(True)

        else:
            print("Pls display all")
            FilterSearchInvoiceScreen.display_all = 1




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


# def query_invoices(*exps):
#     s = session()
#     return s.query(Invoice).filter(and_(*exps)).all()

# def callback(text):
#     print("double clicked", text)

# class MyLabel(Label):
#     def on_touch_down(self, touch):
#         if touch.is_double_tap:
#             print(self.text)

class DoubleClickableLabel(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.register_event_type('on_double_press')
        if kwargs.get("on_double_press") is not None:
            self.bind(on_double_press=kwargs.get("on_double_press"))

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.dispatch('on_double_press', touch)
            return True
        return Label.on_touch_down(self, touch)

    def on_double_press(self, *args):
        pass

class Update_trading_partner_Screen(MDScreen):
    def on_pre_enter(self, *args):
        invoice_number = Filtered_searched_display_Screen.update_invoice_number
        s = session()
        query_invoice = s.query(Invoice).filter_by(id=invoice_number).first()
        trading_partner = query_invoice.trading_partner_name

        query_trading_partner = s.query(TradingPartner).filter_by(trading_partner_name=trading_partner).first()

        self.ids.trading_partner_name_label.text = f"Trading Partner Name: {query_trading_partner.trading_partner_name}"

        self.ids.supplier_name_label.text = f"Supplier Name: {query_trading_partner.supplier_name}"

        self.ids.sector_label.text = f"Sector: {query_trading_partner.sector}"

        self.ids.contract_days_label.text = f"Contract days: {query_trading_partner.contract_days}"

        self.ids.priority_rank_label.text = f"Priority rank: {query_trading_partner.priority_rank}"

        self.ids.remit_to_bank_account_name_label.text = f"Remit to bank account name: {query_trading_partner.remit_to_bank_account_name}"

        self.ids.remit_to_bank_account_number_label.text = f"Remit to bank account number: {query_trading_partner.remit_to_bank_account_number}"

    def update_trading_partner(self):
        #Need to update any field that is updated about the Trading Partner
        #then do a for loop through every invoices with the trading partner id
        #and update all the updated information about the Trading Partner into the invoices:
        invoice_number = Filtered_searched_display_Screen.update_invoice_number
        s = session()
        query_invoice = s.query(Invoice).filter_by(id=invoice_number).first()
        trading_partner = query_invoice.trading_partner_name

        query_trading_partner = s.query(TradingPartner).filter_by(trading_partner_name=trading_partner).first()
        all_needed_to_be_update_invoices = s.query(Invoice).filter_by(trading_partner_name=trading_partner)

        for invoices in all_needed_to_be_update_invoices:
            print(invoices.trading_partner_name, invoices.invoice_number)

        if (len(self.ids.trading_partner_name_input.text) > 0 or len(self.ids.supplier_name_input.text) > 0
                or len(self.ids.sector_input.text) > 0 or len(self.ids.contract_days_input.text) > 0
                or len(self.ids.priority_rank_input.text) > 0 or len(self.ids.remit_to_bank_account_name_input.text) > 0
                or len(self.ids.remit_to_bank_account_number_input.text)>0):

            #First, if anything is changed with the trading partner, the user who upload this trading partner
            # will be updated to the user who made the new update: = TESTED
            query_trading_partner.trading_partner_added_by_user = LoginScreen.current_user

            #Second, if trading_partner_name is changed, we need to make sure
            #that it cannot be changed to an exisitng trading parter due to data integrity: = TESTED

            if len(self.ids.trading_partner_name_input.text) > 0:
                # for the update of the trading partner, there need to be 1 more code
                # to check if the updated trading partner exists already or not:
                trading_partner_check = s.query(TradingPartner).filter_by(
                    trading_partner_name=self.ids.trading_partner_name_input.text).first()
                if trading_partner_check:
                    print("The trading partner that you wanted to update to already existed. Pls update to a non-exisiting trading partner")
                else:
                    # update the trading partner name in the Trading partner data table:
                    query_trading_partner.trading_partner_name = self.ids.trading_partner_name_input.text
                    s.commit()
                    # update the trading partner name for all invoices with the updated
                    # trading partner name:
                    for invoices in all_needed_to_be_update_invoices:
                        invoices.trading_partner_name = self.ids.trading_partner_name_input.text
                        s.commit()

            #little bit more complicated code below for
            # I will need to update the "Expired Contract Date" in each invoice
            # as well:
            # (with Expired Contract Date = Invoice date plus the updated Contract Days) = TESTED
            if len(self.ids.contract_days_input.text) > 0:
                # first, update the contract days in the trading parter:
                query_trading_partner.contract_days = self.ids.contract_days_input.text
                s.commit()
                #second, update all expired contract date of each invoice:
                for invoices in all_needed_to_be_update_invoices:
                    invoice_date_datetime = datetime.strptime(invoices.invoice_date, "%Y-%m-%d")
                    expired_contract_date0 = invoice_date_datetime + timedelta(days=int(self.ids.contract_days_input.text))
                    invoices.expired_contract_date = str(expired_contract_date0)
                    s.commit()

            if len(self.ids.supplier_name_input.text) > 0: # = TESTED
                # for the update of the supplier name, there need to be 1 more code
                # to check if the updated supplier name exists already or not:
                supplier_name_check = s.query(TradingPartner).filter_by(
                    supplier_name=self.ids.supplier_name_input.text).first()
                if supplier_name_check:
                    print("The supplier name that you wanted to update to already existed. Pls update to a non-exisiting supplier name")
                else:
                    # update the trading partner name in the Trading partner data table:
                    query_trading_partner.supplier_name = self.ids.supplier_name_input.text
                    s.commit()

            if len(self.ids.sector_input.text) > 0: # = TESTED
                query_trading_partner.sector = self.ids.sector_input.text
                s.commit()

            if len(self.ids.priority_rank_input.text) > 0: # = TESTED
                query_trading_partner.priority_rank = self.ids.priority_rank_input.text
                s.commit()

            if len(self.ids.remit_to_bank_account_name_input.text) > 0: # = TESTED
                query_trading_partner.remit_to_bank_account_name = self.ids.remit_to_bank_account_name_input.text
                s.commit()

            if len(self.ids.remit_to_bank_account_number_input.text)>0: # = TESTED
                query_trading_partner.remit_to_bank_account_number = self.ids.remit_to_bank_account_number_input.text
                s.commit()


    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"



class Update_invoice_Screen(MDScreen):

    def update_trading_partner(self):


        print("To update trading partner screen")
        self.parent.current = "Update_trading_partner_Screen"


        ##Need to redirect the user to the Update trading partner Screen

    def on_pre_enter(self, *args):
        invoice_number = Filtered_searched_display_Screen.update_invoice_number

        s = session()
        query_invoice = s.query(Invoice).filter_by(id=invoice_number).first()


        self.ids.trading_partner_label.text = f"Trading Partner Name: {query_invoice.trading_partner_name}"

        # self.ids.update_trading_partner_button_text.text = f"Update trading partner's info"

        self.ids.invoice_date_label.text = f"Invoice date (Format YYYY-MM-DD): {query_invoice.invoice_date}"

        self.ids.invoice_number_label.text = f"Invoice number: {query_invoice.invoice_number}"

        self.ids.invoice_amount_label.text = f"Invoice amount: {query_invoice.invoice_amount}"

        self.ids.invoice_currency_label.text = f"Invoice currency: {query_invoice.invoice_currency}"

        self.ids.tax_input_label.text = f"Tax for invoice: {query_invoice.tax}"

        self.ids.actual_payment_date_label.text = f"Actual payment date: {query_invoice.actual_payment_date}"

        self.ids.actual_payment_accepted_by_label.text = f"Actual payment date accepted by: {query_invoice.actual_payment_accepted_by}"

        self.ids.description_label.text = f"Description: {query_invoice.description}"

        self.ids.overdue_period_label.text = f"Overdue period: {query_invoice.overdue_period}"

        self.ids.notes_for_penalty_label.text = f"Notes for penalty: {query_invoice.notes_for_penalty_overdue}"

        self.ids.occurent_label.text = f"Occurent: {query_invoice.occurent}"

        if isinstance(query_invoice.paid_amount, int):
            self.ids.paid_amount_label.text = f"Paid amount: {query_invoice.paid_amount}"
        else:
            self.ids.paid_amount_label.text = f"Paid amount: 0"

        self.ids.payment_date1_label.text = f"Payment date 1: {query_invoice.payment_date1}"

        self.ids.payment_date2_label.text = f"Payment date 2: {query_invoice.payment_date2}"

    def update_invoice(self):
        invoice_number = Filtered_searched_display_Screen.update_invoice_number

        s = session()
        query_invoice = s.query(Invoice).filter_by(id=invoice_number).first()

        #TESTED
        if (len(self.ids.invoice_date_input.text)>0 or len(self.ids.invoice_number_input.text)>0
                or len(self.ids.invoice_amount_input.text)>0 or len(self.ids.invoice_currency_input.text)>0
            or len(self.ids.tax_input.text)>0 or len(self.ids.actual_payment_date_input.text)>0
            or len(self.ids.actual_payment_accepted_by_input.text)>0 or len(self.ids.description_input.text)>0
            or len(self.ids.overdue_period_input.text)>0 or len(self.ids.notes_for_penalty_input.text)>0
            or len(self.ids.occurent_input.text)>0 or len(self.ids.paid_amount_input.text)>0
            or len(self.ids.payment_date1_input.text)>0 or len(self.ids.payment_date2_input.text)>0):

            #if there is at least 1 update in any part of the invoice, the invoices_added_date and the
            #invoices_added_user need to be update properly:
            query_invoice.invoice_added_date = str(date.today())
            query_invoice.invoice_added_by_user = LoginScreen.current_user

            s.commit()

        #TESTED
        #For data integrity, trading partner of an invoice cannot be changed.
        #However, information about a trading partner can be changed
        #after any partner's info is change, a for loop for updating
        #all invoices with that partner's info is neccessary.
        #the user who updated the trading partner will also be updated
        #as the user who entered the trading partner
        if len(self.ids.trading_partner_input.text)>0:
            #for the update of the trading partner, there need to be 1 more code
            #to check if the updated trading partner exists already or not:
            trading_partner_check = s.query(TradingPartner).filter_by(trading_partner_name=self.ids.trading_partner_input.text).first()
            if trading_partner_check:
                query_invoice.trading_partner_name = self.ids.trading_partner_input.text
                s.commit()
            else:
                print("Trading partner doesn't exist=> pls add information of your new trading partner first!")

        if len(self.ids.invoice_date_input.text) > 0:
            query_invoice.invoice_date = self.ids.invoice_date_input.text
            s.commit()

        #TESTED
        if len(self.ids.invoice_number_input.text) > 0:
            query_invoice.invoice_number = self.ids.invoice_number_input.text
            s.commit()

        #TESTED but PROBLEM with updating unpaid amount!!

        if len(self.ids.invoice_amount_input.text) > 0:
            query_invoice.invoice_amount = int(self.ids.invoice_amount_input.text)
            s.commit()

        #TESTED
        if len(self.ids.invoice_currency_input.text) > 0:
            query_invoice.invoice_currency = self.ids.invoice_currency_input.text
            s.commit()

        #TESTED
        if len(self.ids.tax_input.text) > 0:
            query_invoice.tax = int(self.ids.tax_input.text)
            s.commit()

        #TESTED
        if len(self.ids.actual_payment_date_input.text) > 0:
            query_invoice.actual_payment_date = self.ids.actual_payment_date_input.text
            s.commit()

        #TESTED
        if len(self.ids.actual_payment_accepted_by_input.text) > 0:
            query_invoice.actual_payment_accepted_by = self.ids.actual_payment_accepted_by_input.text
            s.commit()

        #TESTED
        if len(self.ids.description_input.text)>0:
            query_invoice.description = self.ids.description_input.text
            s.commit()

        #TESTED
        if len(self.ids.overdue_period_input.text)>0:
            query_invoice.overdue_period = int(self.ids.overdue_period_input.text)
            s.commit()

        #TESTED
        if len(self.ids.notes_for_penalty_input.text)>0:
            query_invoice.notes_for_penalty_overdue= self.ids.notes_for_penalty_input.text
            s.commit()
        #TESTED
        if len(self.ids.occurent_input.text )>0:
            query_invoice.occurent= self.ids.occurent_input.text
            s.commit()

        #TESTED
        if len(self.ids.paid_amount_input.text)>0:
            query_invoice.paid_amount= int(self.ids.paid_amount_input.text)
            s.commit()

            payment_unpaid_amount = int(query_invoice.invoice_amount) - int(query_invoice.paid_amount)
            query_invoice.payment_unpaid_amount = payment_unpaid_amount
            s.commit()

            if int(query_invoice.paid_amount) > 0 and int(query_invoice.paid_amount) < int(query_invoice.invoice_amount):
                paid = 0.5
                query_invoice.paid = paid
                s.commit()
            elif int(query_invoice.paid_amount) == int(query_invoice.invoice_amount):
                paid = 1
                query_invoice.paid = paid
                s.commit()


        #TESTED
        if len(self.ids.payment_date1_input.text)>0:
            query_invoice.payment_date1= self.ids.payment_date1_input.text
            s.commit()

        #TESTED
        if len(self.ids.payment_date2_input.text)>0:
            query_invoice.payment_date2= self.ids.payment_date2_input.text
            s.commit()


        #TESTED
        if len(self.ids.actual_payment_date_input.text) == 0 and len(self.ids.overdue_period_input.text) > 0:
            # s = session()
            trading_partner_check = s.query(TradingPartner).filter_by(
                trading_partner_name=query_invoice.trading_partner_name).first()
            contract_days = trading_partner_check.contract_days
            invoice_date_datetime = datetime.strptime(query_invoice.invoice_date, "%Y-%m-%d")

            expired_contract_date0 = invoice_date_datetime + timedelta(days=contract_days)


            actual_payment_date = str(expired_contract_date0 + timedelta(days=int(self.ids.overdue_period_input.text)))
            print(actual_payment_date)

            query_invoice.actual_payment_date = str(expired_contract_date0 + timedelta(days=int(self.ids.overdue_period_input.text)))
            print(query_invoice.actual_payment_date)
            #PROBLEM: the commit below doesn't really commit the changes!
            s.commit()

        s.commit()

        print("Invoice updated!")

    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"


class Filtered_searched_display_with_trading_partner_info_Screen(MDScreen):

    trading_partner_name_holding = None

    def on_pre_enter(self, *args):
        self.ids.container.clear_widgets()
        invoice_number = FilterSearchInvoiceScreen.invoice_number
        trading_partner_name = FilterSearchInvoiceScreen.trading_partner_name
        invoices_added_date_from = FilterSearchInvoiceScreen.invoices_added_date_from
        invoices_added_date_to = FilterSearchInvoiceScreen.invoices_added_date_to
        invoices_date_from = FilterSearchInvoiceScreen.invoices_date_from
        invoices_date_to = FilterSearchInvoiceScreen.invoices_date_to
        payment_status = FilterSearchInvoiceScreen.payment_status
        display_all = FilterSearchInvoiceScreen.display_all


        if display_all == 1:
            print("Received message display all and message to include further info from Trading Partner of the the invoice")
            # Getting data from the database
            s = session()
            query_all = s.query(Invoice).all()
            # print(query_all)

            # Creating labels - Headings for the columns
            id = MDLabel(text="No.", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(id)

            trading_partner_name = MDLabel(text="Trading partner name", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(trading_partner_name)
            ##

            supplier_name = MDLabel(text="Supplier name", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(supplier_name)

            sector = MDLabel(text="Sector", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(sector)

            contract_days = MDLabel(text="Contract days", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(contract_days)

            priority_rank = MDLabel(text="Trading partner name", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(priority_rank)

            remit_to_bank_account_name = MDLabel(text="Remit to bank account name", font_style="Subtitle2",
                                                 halign="center")
            self.ids.container.add_widget(remit_to_bank_account_name)

            remit_to_bank_account_number = MDLabel(text="Remit to bank account number", font_style="Subtitle2",
                                                   halign="center")
            self.ids.container.add_widget(remit_to_bank_account_number)

            trading_partner_added_by_user = MDLabel(text="Trading partner added by user:", font_style="Subtitle2",
                                                    halign="center")
            self.ids.container.add_widget(trading_partner_added_by_user)

            ###
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
            actual_payment_accepted_by = MDLabel(text="Actual payment date accepted by", font_style="Subtitle2",
                                                 halign="center")
            self.ids.container.add_widget(actual_payment_accepted_by)
            overdue_period = MDLabel(text="Overdue period", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(overdue_period)

            notes_for_penalty_overdue = MDLabel(text="Notes for penalty overdue", font_style="Subtitle2",
                                                halign="center")
            self.ids.container.add_widget(notes_for_penalty_overdue)

            paid = MDLabel(text="Paid? (1=paid, 0.5=partial paid, 0=unpaid)", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid)

            paid_amount = MDLabel(text="Paid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid_amount)

            payment_unpaid_amount = MDLabel(text="Unpaid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_unpaid_amount)

            payment_date1 = MDLabel(text="Payment date 1", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date1)

            payment_date2 = MDLabel(text="Payment date 2", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date2)

            occurent = MDLabel(text="Occurent", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(occurent)

            invoice_added_by_user = MDLabel(text="Invoices added by user:", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_added_by_user)

            print(Filtered_searched_display_Screen.query_variable)

            # display the queried data:
            for data in query_all:
                id = MDLabel(text=str(data.id), halign="center")
                self.ids.container.add_widget(id)


                trading_partner_name = DoubleClickableLabel(text=str(data.trading_partner_name), halign="center",
                                                            on_double_press=self.callback, color=(0, 0, 1, 1))
                print(trading_partner_name.text)
                self.ids.container.add_widget(trading_partner_name)
                Filtered_searched_display_with_trading_partner_info_Screen.trading_partner_name_holding = data.trading_partner_name

                print(Filtered_searched_display_with_trading_partner_info_Screen.trading_partner_name_holding)
                # query info from Trading Partner
                trading_partner_query = s.query(TradingPartner).filter_by(
                    trading_partner_name=Filtered_searched_display_with_trading_partner_info_Screen.trading_partner_name_holding).first()

                # for data in trading_partner_query:

                supplier_name = MDLabel(text=str(trading_partner_query.supplier_name), halign="center")
                self.ids.container.add_widget(supplier_name)

                sector = MDLabel(text=str(trading_partner_query.sector), halign="center")
                self.ids.container.add_widget(sector)

                contract_days = MDLabel(text=str(trading_partner_query.contract_days), halign="center")
                self.ids.container.add_widget(contract_days)

                priority_rank = MDLabel(text=str(trading_partner_query.priority_rank), halign="center")
                self.ids.container.add_widget(priority_rank)

                remit_to_bank_account_name = MDLabel(text=str(trading_partner_query.remit_to_bank_account_name),
                                                     halign="center")
                self.ids.container.add_widget(remit_to_bank_account_name)

                remit_to_bank_account_number = MDLabel(text=str(trading_partner_query.remit_to_bank_account_number),
                                                       halign="center")
                self.ids.container.add_widget(remit_to_bank_account_number)

                trading_partner_added_by_user = MDLabel(text=str(trading_partner_query.trading_partner_added_by_user),
                                                        halign="center")
                self.ids.container.add_widget(trading_partner_added_by_user)

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

                description = MDLabel(text=str(data.description), halign="center")
                self.ids.container.add_widget(description)

                expired_contract_date = MDLabel(text=str(data.expired_contract_date), halign="center")
                self.ids.container.add_widget(expired_contract_date)

                actual_payment_date = MDLabel(text=str(data.actual_payment_date), halign="center")
                self.ids.container.add_widget(actual_payment_date)

                actual_payment_accepted_by = MDLabel(text=str(data.actual_payment_accepted_by), halign="center")
                self.ids.container.add_widget(actual_payment_accepted_by)

                overdue_period = MDLabel(text=str(data.overdue_period), halign="center")
                self.ids.container.add_widget(overdue_period)

                notes_for_penalty_overdue = MDLabel(text=str(data.notes_for_penalty_overdue), halign="center")
                self.ids.container.add_widget(notes_for_penalty_overdue)

                paid = MDLabel(text=str(data.paid), halign="center")
                self.ids.container.add_widget(paid)

                paid_amount = MDLabel(text=str(data.paid_amount), halign="center")
                self.ids.container.add_widget(paid_amount)

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

                s.close()

        elif display_all == 0:
            print("Something")
            s = session()

            # Creating labels - Headings for the columns
            id = MDLabel(text="No.", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(id)

            trading_partner_name = MDLabel(text="Trading partner name", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(trading_partner_name)
            ##

            supplier_name = MDLabel(text="Supplier name", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(supplier_name)

            sector = MDLabel(text="Sector", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(sector)

            contract_days = MDLabel(text="Contract days", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(contract_days)

            priority_rank = MDLabel(text="Trading partner name", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(priority_rank)

            remit_to_bank_account_name = MDLabel(text="Remit to bank account name", font_style="Subtitle2",
                                                 halign="center")
            self.ids.container.add_widget(remit_to_bank_account_name)

            remit_to_bank_account_number = MDLabel(text="Remit to bank account number", font_style="Subtitle2",
                                                   halign="center")
            self.ids.container.add_widget(remit_to_bank_account_number)

            trading_partner_added_by_user = MDLabel(text="Trading partner added by user:", font_style="Subtitle2",
                                                    halign="center")
            self.ids.container.add_widget(trading_partner_added_by_user)

            ###
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
            actual_payment_accepted_by = MDLabel(text="Actual payment date accepted by", font_style="Subtitle2",
                                                 halign="center")
            self.ids.container.add_widget(actual_payment_accepted_by)
            overdue_period = MDLabel(text="Overdue period", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(overdue_period)

            notes_for_penalty_overdue = MDLabel(text="Notes for penalty overdue", font_style="Subtitle2",
                                                halign="center")
            self.ids.container.add_widget(notes_for_penalty_overdue)

            paid = MDLabel(text="Paid? (1=paid, 0.5=partial paid, 0=unpaid)", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid)

            paid_amount = MDLabel(text="Paid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid_amount)

            payment_unpaid_amount = MDLabel(text="Unpaid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_unpaid_amount)

            payment_date1 = MDLabel(text="Payment date 1", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date1)

            payment_date2 = MDLabel(text="Payment date 2", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date2)

            occurent = MDLabel(text="Occurent", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(occurent)

            invoice_added_by_user = MDLabel(text="Invoices added by user:", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_added_by_user)

            print(Filtered_searched_display_Screen.query_variable)

            # display the queried data:
            for data in Filtered_searched_display_Screen.query_variable:
                id = MDLabel(text=str(data.id), halign="center")
                self.ids.container.add_widget(id)

                trading_partner_name = DoubleClickableLabel(text=str(data.trading_partner_name), halign="center",
                                                            on_double_press=self.callback, color=(0, 0, 1, 1))
                print(trading_partner_name.text)
                self.ids.container.add_widget(trading_partner_name)
                Filtered_searched_display_with_trading_partner_info_Screen.trading_partner_name_holding = data.trading_partner_name

                print(Filtered_searched_display_with_trading_partner_info_Screen.trading_partner_name_holding)
                # query info from Trading Partner
                trading_partner_query = s.query(TradingPartner).filter_by(
                    trading_partner_name=Filtered_searched_display_with_trading_partner_info_Screen.trading_partner_name_holding).first()

                # for data in trading_partner_query:

                supplier_name = MDLabel(text=str(trading_partner_query.supplier_name), halign="center")
                self.ids.container.add_widget(supplier_name)

                sector = MDLabel(text=str(trading_partner_query.sector), halign="center")
                self.ids.container.add_widget(sector)

                contract_days = MDLabel(text=str(trading_partner_query.contract_days), halign="center")
                self.ids.container.add_widget(contract_days)

                priority_rank = MDLabel(text=str(trading_partner_query.priority_rank), halign="center")
                self.ids.container.add_widget(priority_rank)

                remit_to_bank_account_name = MDLabel(text=str(trading_partner_query.remit_to_bank_account_name),
                                                     halign="center")
                self.ids.container.add_widget(remit_to_bank_account_name)

                remit_to_bank_account_number = MDLabel(text=str(trading_partner_query.remit_to_bank_account_number),
                                                       halign="center")
                self.ids.container.add_widget(remit_to_bank_account_number)

                trading_partner_added_by_user = MDLabel(text=str(trading_partner_query.trading_partner_added_by_user),
                                                        halign="center")
                self.ids.container.add_widget(trading_partner_added_by_user)

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

                description = MDLabel(text=str(data.description), halign="center")
                self.ids.container.add_widget(description)

                expired_contract_date = MDLabel(text=str(data.expired_contract_date), halign="center")
                self.ids.container.add_widget(expired_contract_date)

                actual_payment_date = MDLabel(text=str(data.actual_payment_date), halign="center")
                self.ids.container.add_widget(actual_payment_date)

                actual_payment_accepted_by = MDLabel(text=str(data.actual_payment_accepted_by), halign="center")
                self.ids.container.add_widget(actual_payment_accepted_by)

                overdue_period = MDLabel(text=str(data.overdue_period), halign="center")
                self.ids.container.add_widget(overdue_period)

                notes_for_penalty_overdue = MDLabel(text=str(data.notes_for_penalty_overdue), halign="center")
                self.ids.container.add_widget(notes_for_penalty_overdue)

                paid = MDLabel(text=str(data.paid), halign="center")
                self.ids.container.add_widget(paid)

                paid_amount = MDLabel(text=str(data.paid_amount), halign="center")
                self.ids.container.add_widget(paid_amount)

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

                s.close()



    def non_include_trading_partner_info(self):
        self.parent.current = "Filtered_searched_display_Screen"

    def callback(self, *args):
        print("double clicked", *args, self.label.text)


    def back_to_menu(self):
        print("Back to menu")
        self.parent.current = "HomeScreen"


class Filtered_searched_display_Screen(MDScreen):
    # in order to not use too much of the long display codes below,
    # we will create a variable that hold the value of the
    # query after we finished with the if else,
    # simply, if some conditions is met, we could set our
    # query variable to the value of the query in that one if else,
    # and then display everything using that query variable:

    query_variable = 0
    update_invoice_number = 0

    def edit_invoice(self):
        Filtered_searched_display_Screen.update_invoice_number = self.ids.edit_invoice_number_input.text
        print(f"Update invoice number {Filtered_searched_display_Screen.update_invoice_number}")
        self.parent.current = "Update_invoice_Screen"

    def remove_invoice(self): # = TESTED
        delete_invoice_number = self.ids.delete_invoice_number_input.text
        s = session()
        s.query(Invoice).filter_by(id=delete_invoice_number).delete()
        s.commit()
        print(f"Invoice no. {delete_invoice_number} is deleted")
        self.parent.current = "HomeScreen"


    def back_to_search_screen(self):
        self.parent.current = "FilterSearchInvoiceScreen"

    def export_excel(self):
        pass

    def export_pdf(self):
        pass

    def on_pre_enter(self, *args):
        self.ids.container.clear_widgets()
        Filtered_searched_display_Screen.query_variable = 0
        #when enter the display screen, only display info from the invoices' table
        #only display more related invoices info from Trading Partner info
        #if the user requested to decrease amount of horizontal
        #scrolling the user needs to do in order to see every info about an invoice

        invoice_number = FilterSearchInvoiceScreen.invoice_number
        trading_partner_name = FilterSearchInvoiceScreen.trading_partner_name
        invoices_added_date_from = FilterSearchInvoiceScreen.invoices_added_date_from
        invoices_added_date_to = FilterSearchInvoiceScreen.invoices_added_date_to
        invoices_date_from = FilterSearchInvoiceScreen.invoices_date_from
        invoices_date_to = FilterSearchInvoiceScreen.invoices_date_to
        payment_status = FilterSearchInvoiceScreen.payment_status
        display_all = FilterSearchInvoiceScreen.display_all

        print("Display all is", display_all)


        print(invoice_number, trading_partner_name, invoices_added_date_from, invoices_added_date_to,
              invoices_date_from, invoices_date_to, payment_status, display_all)

        if display_all == 1:
            print("Received message display all")

            # Getting data from the database
            s = session()
            query_all = s.query(Invoice).all()
            print(query_all)

            Filtered_searched_display_Screen.query_variable = query_all

            #might need to put the long stupid code here
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
            actual_payment_accepted_by = MDLabel(text="Actual payment date accepted by", font_style="Subtitle2",
                                                 halign="center")
            self.ids.container.add_widget(actual_payment_accepted_by)
            overdue_period = MDLabel(text="Overdue period", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(overdue_period)

            notes_for_penalty_overdue = MDLabel(text="Notes for penalty overdue", font_style="Subtitle2",
                                                halign="center")
            self.ids.container.add_widget(notes_for_penalty_overdue)

            paid = MDLabel(text="Paid? (1=paid, 0.5=partial paid, 0=unpaid)", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid)

            paid_amount = MDLabel(text="Paid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid_amount)

            payment_unpaid_amount = MDLabel(text="Unpaid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_unpaid_amount)

            payment_date1 = MDLabel(text="Payment date 1", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date1)

            payment_date2 = MDLabel(text="Payment date 2", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date2)

            occurent = MDLabel(text="Occurent", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(occurent)

            invoice_added_by_user = MDLabel(text="Invoices added by user:", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(invoice_added_by_user)

            # display the queried data:
            for data in query_all:
                id = MDLabel(text=str(data.id), halign="center")
                self.ids.container.add_widget(id)

                # trading_partner_name = MDLabel(text=str(data.trading_partner_name), halign="center")
                ##PROBLEM WITH CALL BACK THE TEXT FROM THE DOUBLE PRESSED LABEL
                trading_partner_name = DoubleClickableLabel(text=str(data.trading_partner_name), halign="center",
                                                            on_double_press=self.callback, color=(0, 0, 1, 1))
                print(trading_partner_name.text)
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

                description = MDLabel(text=str(data.description), halign="center")
                self.ids.container.add_widget(description)

                expired_contract_date = MDLabel(text=str(data.expired_contract_date), halign="center")
                self.ids.container.add_widget(expired_contract_date)

                actual_payment_date = MDLabel(text=str(data.actual_payment_date), halign="center")
                self.ids.container.add_widget(actual_payment_date)

                actual_payment_accepted_by = MDLabel(text=str(data.actual_payment_accepted_by), halign="center")
                self.ids.container.add_widget(actual_payment_accepted_by)

                overdue_period = MDLabel(text=str(data.overdue_period), halign="center")
                self.ids.container.add_widget(overdue_period)

                notes_for_penalty_overdue = MDLabel(text=str(data.notes_for_penalty_overdue), halign="center")
                self.ids.container.add_widget(notes_for_penalty_overdue)

                paid = MDLabel(text=str(data.paid), halign="center")
                self.ids.container.add_widget(paid)

                paid_amount = MDLabel(text=str(data.paid_amount), halign="center")
                self.ids.container.add_widget(paid_amount)

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

                s.close()



        elif display_all == 0:
            print("Something")
            s=session()
            #when the user input the invoice number, it
            #means that the user already know what
            #specific invoice he is looking for,
            #thus there is no need to query other information:
            if len(invoice_number)>0:
                #the code below works
                invoice_number_query = s.query(Invoice).filter_by(invoice_number=invoice_number).all()
                print(invoice_number_query)

                Filtered_searched_display_Screen.query_variable = invoice_number_query

            else:

                print("No invoice number input")
                #if the user doesn't input an invoice number, he can search with
                #each of with a few of most general combination of other 6 inputs:

                #1. if the user only input trading partner name: =TESTED TESTED
                if len(trading_partner_name)>0 and len(invoices_added_date_from)==0 and len(invoices_added_date_to)==0 and len(invoices_date_from)==0 and len(invoices_date_to)==0 and (payment_status is None or payment_status=="Every status"):
                    print("user only input trading partner name")
                    trading_partner_name_query = s.query(Invoice).filter(Invoice.trading_partner_name==trading_partner_name).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_query

                    for data in trading_partner_name_query:
                        print(data.invoice_number)

                #2. if the user input trading partner name with two ranges for invoices_added_date: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_added_date_from) > 0 and len(invoices_added_date_to)>0 and len(invoices_date_from)==0 and len(invoices_date_to)==0 and (payment_status is None or payment_status=="Every status"):
                    trading_partner_name_with_both_added_date = s.query(Invoice).filter(Invoice.trading_partner_name==trading_partner_name,and_(Invoice.invoice_added_date >= invoices_added_date_from,Invoice.invoice_added_date <= invoices_added_date_to)).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_with_both_added_date

                    for data in trading_partner_name_with_both_added_date:
                        print(data.invoice_number)

                #3. if the user input trading partner name with only the starting range for invoices_added_date: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_added_date_from) > 0 and len(invoices_added_date_to)==0 and len(invoices_date_from)==0 and len(invoices_date_to)==0 and (payment_status is None or payment_status=="Every status"):
                    print("the user input trading partner name with only the starting range for invoices_added_date")
                    trading_partner_name_with_staring_added_date = s.query(Invoice).filter(
                        Invoice.trading_partner_name == trading_partner_name,Invoice.invoice_added_date >= invoices_added_date_from).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_with_staring_added_date

                    for data in trading_partner_name_with_staring_added_date:
                        print(data.invoice_number)

                #4. if the user input trading partner name with only the ending range for invoices_added_date: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_added_date_to) > 0 and len(invoices_added_date_from)==0 and len(invoices_date_from)==0 and len(invoices_date_to)==0 and (payment_status is None or payment_status=="Every status"):
                    print("user input trading partner name with only the ending range for invoices_added_date")
                    trading_partner_name_with_ending_added_date = s.query(Invoice).filter(
                        Invoice.trading_partner_name == trading_partner_name,Invoice.invoice_added_date <= invoices_added_date_to).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_with_ending_added_date

                    for data in trading_partner_name_with_ending_added_date:
                        print(data.invoice_number)

                #5.  if the user input trading partner name with two ranges for invoice date: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_date_from) > 0 and len(invoices_date_to)>0 and len(invoices_added_date_from)==0 and len(invoices_added_date_to)==0 and (payment_status is None or payment_status=="Every status"):
                    trading_partner_name_with_both_date = s.query(Invoice).filter(Invoice.trading_partner_name==trading_partner_name,and_(Invoice.invoice_date >= invoices_date_from,Invoice.invoice_date <= invoices_date_to)).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_with_both_date

                    for data in trading_partner_name_with_both_date:
                        print(data.invoice_number)

                #6. if the user input trading partner name with only the starting range for invoices_date: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_date_from) > 0 and len(invoices_date_to)==0 and len(invoices_added_date_from)==0 and len(invoices_added_date_to)==0 and (payment_status is None or payment_status=="Every status"):
                    trading_partner_name_with_staring_date = s.query(Invoice).filter(
                        Invoice.trading_partner_name == trading_partner_name,Invoice.invoice_date >= invoices_date_from).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_with_staring_date

                    for data in trading_partner_name_with_staring_date:
                        print(data.invoice_number)

                #7. if the user input trading partner name with only the ending range for invoices_date: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_date_to) > 0 and len(invoices_date_from)==0 and len(invoices_added_date_from)==0 and len(invoices_added_date_to)==0 and (payment_status is None or payment_status=="Every status"):
                    trading_partner_name_with_ending_date = s.query(Invoice).filter(
                        Invoice.trading_partner_name == trading_partner_name,Invoice.invoice_date <= invoices_date_to).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_with_ending_date

                    for data in trading_partner_name_with_ending_date:
                        print(data.invoice_number)


                #8. if the user input trading partner rame with 2 date ranges: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_added_date_from) > 0 and len(invoices_added_date_to)>0 and len(invoices_date_from) > 0 and len(invoices_date_to)>0 and (payment_status is None or payment_status=="Every status"):
                    print("user input trading partner rame with 2 date ranges")
                    trading_partner_name_with_both_added_invoice_added_date_and_date = s.query(Invoice).filter(Invoice.trading_partner_name==trading_partner_name,
                                                                                        and_(Invoice.invoice_added_date >= invoices_added_date_from,Invoice.invoice_added_date <= invoices_added_date_to),
                                                                                        and_(Invoice.invoice_date >= invoices_date_from,Invoice.invoice_date <= invoices_date_to)).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_name_with_both_added_invoice_added_date_and_date


                    for data in trading_partner_name_with_both_added_invoice_added_date_and_date:
                        print(data.invoice_number, data.invoice_date)
                    print(invoices_date_to)


                #9. if the user input only the payment status: = TESTED TESTED
                elif (payment_status is not None or payment_status!="Every status") and len(trading_partner_name)== 0 and len(invoices_added_date_from)==0 and len(invoices_added_date_to)==0 and len(invoices_date_from)==0 and len(invoices_date_to)==0:
                    print("if the user input only the payment status")
                    if payment_status == "Paid":
                        payment_status = 1
                    elif payment_status == "Not paid":
                        payment_status = 0
                    elif payment_status == "Partial paid":
                        payment_status = 0.5
                    payment_status_query = s.query(Invoice).filter(Invoice.paid==payment_status).all()

                    Filtered_searched_display_Screen.query_variable = payment_status_query

                    for data in payment_status_query:
                        print(data.invoice_number)


                #10. if the user input every input except the invoice_number: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_added_date_from) > 0 and len(invoices_added_date_to) > 0 and len(invoices_date_from) > 0 and len(invoices_date_to) > 0 and (payment_status is not None or payment_status!="Every status"):
                    print("if the user input every input except the invoice_number")
                    if payment_status == "Paid":
                        payment_status = 1
                    elif payment_status == "Not paid":
                        payment_status = 0
                    elif payment_status == "Partial paid":
                        payment_status = 0.5
                    query_every_thing_except_invoice_number = s.query(Invoice).filter(Invoice.trading_partner_name==trading_partner_name,
                                                                                        and_(Invoice.invoice_added_date >= invoices_added_date_from,Invoice.invoice_added_date <= invoices_added_date_to),
                                                                                        and_(Invoice.invoice_date >= invoices_date_from,Invoice.invoice_date <= invoices_date_to),
                                                                                        Invoice.paid ==payment_status).all()

                    Filtered_searched_display_Screen.query_variable = query_every_thing_except_invoice_number

                    for data in query_every_thing_except_invoice_number:
                        print(data.invoice_number)


                #11.  if the user input trading partner name with two ranges for invoices_added_date with the payment_status: = TESTED TESTED
                elif len(trading_partner_name) > 0 and len(invoices_added_date_from) > 0 and len(invoices_added_date_to) > 0 and len(invoices_date_from) == 0 and len(invoices_date_to) == 0 and (payment_status is not None or payment_status!="Every status"):
                    print("if the user if the user input trading partner name with two ranges for invoices_added_date with the payment_status")
                    if payment_status == "Paid":
                        payment_status = 1
                    elif payment_status == "Not paid":
                        payment_status = 0
                    elif payment_status == "Partial paid":
                        payment_status = 0.5
                    trading_partner_two_invoices_added_date_payment_status = s.query(Invoice).filter(Invoice.trading_partner_name==trading_partner_name,
                                                                                        and_(Invoice.invoice_added_date >= invoices_added_date_from,Invoice.invoice_added_date <= invoices_added_date_to),
                                                                                      Invoice.paid ==payment_status).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_two_invoices_added_date_payment_status

                    for data in trading_partner_two_invoices_added_date_payment_status:
                        print(data.invoice_number)


                #12. if the user input trading partner name with two ranges for invoice_date with the payment_status: = TESTED TESTED
                elif len(trading_partner_name) >0  and len(invoices_date_from) > 0 and len(invoices_date_to) > 0 and len(invoices_added_date_from) == 0 and len(invoices_added_date_to) == 0 and (payment_status is not None or payment_status!="Every status"):
                    if payment_status == "Paid":
                        payment_status = 1
                    elif payment_status == "Not paid":
                        payment_status = 0
                    elif payment_status == "Partial paid":
                        payment_status = 0.5
                    trading_partner_two_invoices_date_payment_status = s.query(Invoice).filter(Invoice.trading_partner_name==trading_partner_name,
                                                                                        and_(Invoice.invoice_date >= invoices_date_from,Invoice.invoice_date <= invoices_date_to),
                                                                                        Invoice.paid ==payment_status).all()

                    Filtered_searched_display_Screen.query_variable = trading_partner_two_invoices_date_payment_status

                    for data in trading_partner_two_invoices_date_payment_status:
                        print(data.invoice_number)

                #13 if the user only input only the two ranges for the invoices_added_date = TESTED TESTED
                elif len(trading_partner_name) == 0  and len(invoices_date_from) == 0 and len(invoices_date_to) == 0 and len(invoices_added_date_from) > 0 and len(invoices_added_date_to) > 0 and (payment_status is  None or payment_status=="Every status"):
                    only_two_ranges_invoices_added_date = s.query(Invoice).filter(and_(Invoice.invoice_added_date >= invoices_added_date_from,Invoice.invoice_added_date <= invoices_added_date_to)).all()
                    Filtered_searched_display_Screen.query_variable = only_two_ranges_invoices_added_date


                #14 if the user only input only two ranges for the invoices date = TESTED TESTED
                elif len(trading_partner_name) == 0  and len(invoices_date_from) > 0 and len(invoices_date_to) > 0 and len(invoices_added_date_from) == 0 and len(invoices_added_date_to) == 0 and (payment_status is  None or payment_status=="Every status"):
                    only_two_ranges_invoices_date = s.query(Invoice).filter(and_(Invoice.invoice_date >= invoices_date_from,Invoice.invoice_date <= invoices_date_to)).all()
                    Filtered_searched_display_Screen.query_variable =  only_two_ranges_invoices_date

            # Creating labels - Headings for the columns
            id = MDLabel(text="No.", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(id)

            trading_partner_name = MDLabel(text="Trading partner name", font_style="Subtitle2",
                                           halign="center")
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
            expired_contract_date = MDLabel(text="Expired contract date", font_style="Subtitle2",
                                            halign="center")
            self.ids.container.add_widget(expired_contract_date)
            actual_payment_date = MDLabel(text="Actual payment date", font_style="Subtitle2",
                                          halign="center")
            self.ids.container.add_widget(actual_payment_date)
            actual_payment_accepted_by = MDLabel(text="Actual payment date accepted by",
                                                 font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(actual_payment_accepted_by)
            overdue_period = MDLabel(text="Overdue period", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(overdue_period)

            notes_for_penalty_overdue = MDLabel(text="Notes for penalty overdue", font_style="Subtitle2",
                                                halign="center")
            self.ids.container.add_widget(notes_for_penalty_overdue)

            paid = MDLabel(text="Paid? (1=paid, 0.5=partial paid, 0=unpaid)", font_style="Subtitle2",
                           halign="center")
            self.ids.container.add_widget(paid)

            paid_amount = MDLabel(text="Paid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(paid_amount)

            payment_unpaid_amount = MDLabel(text="Unpaid amount", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_unpaid_amount)

            payment_date1 = MDLabel(text="Payment date 1", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date1)

            payment_date2 = MDLabel(text="Payment date 2", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(payment_date2)

            occurent = MDLabel(text="Occurent", font_style="Subtitle2", halign="center")
            self.ids.container.add_widget(occurent)

            invoice_added_by_user = MDLabel(text="Invoices added by user:", font_style="Subtitle2",
                                            halign="center")
            self.ids.container.add_widget(invoice_added_by_user)

            print(Filtered_searched_display_Screen.query_variable)
            # display the queried data:
            for data in Filtered_searched_display_Screen.query_variable:
                id = MDLabel(text=str(data.id), halign="center")
                self.ids.container.add_widget(id)

                # trading_partner_name = MDLabel(text=str(data.trading_partner_name), halign="center")
                ##PROBLEM WITH CALL BACK THE TEXT FROM THE DOUBLE PRESSED LABEL
                trading_partner_name = DoubleClickableLabel(text=str(data.trading_partner_name),
                                                            halign="center", on_double_press=self.callback,
                                                            color=(0, 0, 1, 1))
                print(trading_partner_name.text)
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

                description = MDLabel(text=str(data.description), halign="center")
                self.ids.container.add_widget(description)

                expired_contract_date = MDLabel(text=str(data.expired_contract_date), halign="center")
                self.ids.container.add_widget(expired_contract_date)

                actual_payment_date = MDLabel(text=str(data.actual_payment_date), halign="center")
                self.ids.container.add_widget(actual_payment_date)

                actual_payment_accepted_by = MDLabel(text=str(data.actual_payment_accepted_by),
                                                     halign="center")
                self.ids.container.add_widget(actual_payment_accepted_by)

                overdue_period = MDLabel(text=str(data.overdue_period), halign="center")
                self.ids.container.add_widget(overdue_period)

                notes_for_penalty_overdue = MDLabel(text=str(data.notes_for_penalty_overdue),
                                                    halign="center")
                self.ids.container.add_widget(notes_for_penalty_overdue)

                paid = MDLabel(text=str(data.paid), halign="center")
                self.ids.container.add_widget(paid)

                paid_amount = MDLabel(text=str(data.paid_amount), halign="center")
                self.ids.container.add_widget(paid_amount)

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

                s.close()

                print(data.invoice_number)

                    # print(Filtered_searched_display_Screen.query_variable)




    def include_trading_partner_info(self):
        self.parent.current = "Filtered_searched_display_with_trading_partner_info_Screen"

    def callback(self, *args):
        print("double clicked", *args, self.label.text)


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





