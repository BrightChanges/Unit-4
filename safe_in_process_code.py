```.py

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

                # trading_partner_name = MDLabel(text=str(data.trading_partner_name), halign="center")
                ##PROBLEM WITH CALL BACK THE TEXT FROM THE DOUBLE PRESSED LABEL
                trading_partner_name = DoubleClickableLabel(text=str(data.trading_partner_name), halign="center", on_double_press=self.callback,color=(0,0,1,1))
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


                s.close()


```
