# IB Computer Science IA by Kien Le Trung

## Criterion A: Planning
### Defining the problem
Client Mr Lam is my father, and he works in accounting in an airline company. During Covid time, his company couldn’t pay in time for many services. Because of this, he needs to take a lot more time than before to manually check through his Oracle's invoices logs to see which invoice is overdue and which invoice needs to pay first and fill them in Excel reports (Oracle doesn't have an export function). This takes him a lot of time, and he complained about this to me on a video call in May 2021. He said he wanted a program that could help him record invoices and automatically export various invoice reports to various platforms like Excel, PDF depending on pre-set filters.

As he was saying, I thought that I could create that program for him through my Internal Assessment. This would be very cool because I could bring a Computer Science solution to his problem. A few days later, I told him that I wanted to create the program for him, and Mr Lam accepted my offer. He then sent me an email detailing important functions he is looking for in the program, images of how Oracle kept track of his invoices, ways and formulas to export them to Excel files in order to give me an idea about the program he wants me to create. (Email, 2021) in Appendix, link to Appendix: https://docs.google.com/document/d/1jqNpTUHErdX6za0PeErWIWiXw3vw4pNfHWQNZe-BNwo/edit

In order to understand more about the program for Mr Lam and the success criterias, I scheduled an interview with Mr Lam.
(Interview 1, 2021) in Appendix, link to Appendix: https://docs.google.com/document/d/1jqNpTUHErdX6za0PeErWIWiXw3vw4pNfHWQNZe-BNwo/edit

### Rationale for Proposed Solution
I think that a Python-Kivy-Kivymd program will be an effective solution to Mr Lam’s problem.

There is a screen that lets my client input fixed data related to the Trading Partner and another screen that lets my client input non-fixed data related to the invoice. There is another screen for him to search the invoices with four filters. Searched invoices will be displayed in a data table on the screen. There are edit, clear, remove, export buttons in this screen. Finally, there is another separate screen with two buttons designed specifically to generate the two main reports my client wants to generate with the invoices. All invoices data are stored in a SQLite database and interacted through it.

According to these requirements, I decided to make the program in Python, Kivy, and Kivymd because of:

1. I am learning them at school.
2. Python provides flexibility in back end codings
3. Python has a large amount of libraries that I could use to ease the coding process
4. Kivy and Kivymd provide pleasant and easy to use front end screens and data tables 
5. Python provides compatibility with SQL and SQLAlchemy, helping me to more easily creates database and connects it to the program
6. After creating one screen with Kivy and Kivymd, it is easy to creates another screen by copying and making small changes
7. A Python, Kivy, Kivymd program could be compiled into one .exe file and used as a desktop application, which suits the program type my client wants


### Stating Success Criteria 
1. Being able to input/edit/remove/clear any or all data columns or each row of each invoice and save those data in the program
2. Being able to view all data columns of each invoices save in the column
3. Program lets the client to input fixed data columns about the Trading Partner and pre-stored data in these fixed data columns for every subsequent invoices added to the program after the first time
4. Program will show error messages and ask the client to re-input data about the invoices when there exist data entry errors (such as wrong data type for the data column)
5. Program will show warning/confirmation message asking the client if he is sure before making a change to the program
6. Each of data columns contains the required data format by the clients (some are number, string, date)
7. Let the client filtered/search invoices based on required data columns such as Invoice Number, Payment information, the Actual Payment time, Priority rank, Paid, Sector, Supplier Name into tables that are viewable on the screen
8. Let the client create 2 main types of reports: Overdue Invoice Report and Invoice Payment Schedule Report and export them to reports in Excel and PDF formats.
9. Let the client view and edit/remove all data columns of each invoices shown on the filtered/searched tables
10. Let the client export the filtered/search invoices tables to reports in Excel and PDF formats.
11. Let the client export the whole database of invoices to reports in Excel and PDF formats.
12. Each of the 2 main types of reports will need to be structured in the way that the client want (including headers, report generated time, font type)
13. The program will have a login and logout screen
14. The program will let multiple user creates their account and passwords, storing those passwords in hashed
15. The program will show a message each time the client exported a report saying that he should back it up by putting it into the hard drive or hard disk

## Criterion B: Solution Overview

### System diagram 
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_System%20diagram.png)
Image 1: System diagram of the program
Explanation: The program lets Mr Lam inputs username, password, information about various trading partners and invoices. The program will then process them through actions such as storing those inputs, categorize those data and display them on filtered/searched invoices table, calculate multiple data (such as payment_unpaid_amount = invoice_amount - paid_amount) and do multiple logical comparison (such as is report_generate_day - actuatpayment_date > 0 or <0). A lot of these actions will need to do with a SQLite Database. The program will connect with this databasae through Python and SQLAlchemy. The program will then output those processed data through an UI interface, displaying all or filtered invoices. The program will let the client export 2 unique reports as requested or any other filtered invoices table into Exce and PDF format.

### Design of the program's screens 
#### (All green colored squares in all screen designs are buttons. Anything other than them are texts or text fields. The client Mr Lam and his workers will be referred through the word "user" throughout the explanations below for easier understanding.)
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_Screens(1-4)%20(2).png)
Image 2: Design of Login Screen, Register Screen, Menu Screen, Add invoices Screen
Explanation: The Login Screen (Screen no.1) lets the user to login and use the program through inputting an username and a password. The user could then click the "Login" button for authentication process. If the user hasn't created an account yet, they can click the "Register" button to go through the Register process at the Register Screen (Screen no.2). The user can create an account with an username that hasn't been registered before, and input the password twice before clicking the "Register button". After successfully registered, the user will be redirected back to the Login Screen. After successfully logged in, the user will be redirected to the Menu Screen, where user can click on the "Add invoices +" button and go to the Add invoices Screen (Screen no.4) or click on the "Filter/search invoices" button and go to the Filter/search invoices Screen (Screen no.7) or click on the "Generate reports" button and go to the Generate reports Screen (Screen no.9) or click the "Logout" button, logging out of their account and get redirected to the Login Screen (Screen no.1). Inside the Add invoices Screen, there are 2 buttons for the user to click. The "Add fixed data about Trading Partners +" button will lead the user to the Add fixed data about trading partner Screen (Screen no.5) when clicked whereas the "Add non-fixed data about Invoices" button will lead the user to the Add non-fixed data about invoices Screen (Screen no.6) when clicked. Excluding the Login Screen (Screen no.1), the Register Screen (Screen no.2), and the Menu Screen (Screen no.3), all other screen has a “Back to menu” button that when clicked, will redirect the user back to the Menu Screen (Screen no.3). 

![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_Screens(5-6)%20(1).png)
Image 3: Design of Add fixed data about trading partner Screen, Add non-fixed data about Invoice screen
## Forgot to add the column Invoice number and Occurent into the Invoice class database. Need to add this in to the designs later.
Explanation: Once in the Add fixed data about trading partners Screen (Screen no.5), the user can add information about a Trading Partner by filling out all the text fields of “Trading partner name”, “Supplier name”, “Sector”, “Contract days”, “Priority rank”, “Remit-To Bank Account Name”, “Remit-To Bank Account Number”. The user can activate this adding trading partner information action by clicking the “Add to database +” button. Once in the Add non-fixed data about invoices Screen (Screen no.6), the user can add information about an Invoice by filling out all the text fields, choosing from choice fields such as “Trading Partner”, “Invoice date”, “Invoice number”, “Invoice currency”, “Invoice amount”, “Tax%”, “Actual payment date accepted by”, “Description”, “Overdue period (days)”, “Notes for penalty overdue”, “Occurrent”. If the invoice is paid, or paid twice, the user can input optional text fields such as the paid amount, payment date, and 2nd payment date. The user can activate this adding invoice information action by cycling the “Add to database +” button.

![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_Screens(7-8)%20(1).png)
Image 4: Design of Filter/search invoices Screen, Filtered/searched invoices Screen
Explanation: Once in the Filter/search invoices Screen (Screen no.7), the user can search multiple invoices or one invoice by filling out some or all text fields such as “Invoice number”, “Supplier name”, “Invoices added date”, “Invoices date” and choosing or not choosing an option from the choice field “Payment status”. The user can activate this searching action by clicking on the “Filter/search” button. Once in the Filtered/searched invoices Screen (Screen no.8), the user can see the filtered/searched invoices table and export that table to Excel by clicking on the “Export to Excel” button or to PDF by clicking on the “Export to PDF” button. The user can click on the “Back to previous screen” button to go back to the Filter/search invoices Screen (Screen no.7) with all input fields before filled out.

![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_Screens_real(9)%20(1).png)
Image 5: Design of Generate reports Screen
Explanation: Once in the Generate reports Screen (Screen no.9), the user can choose the type of report they want to export through the choice field “Type of report”, then filling out the “Invoice date” text field and choosing the export format through the choice field “Type of export format”. The user can activate this export process by clicking on the “Export” button.

### UML diagram/Class diagram
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_UML_ClassDiagram.png)
Image 6: UML diagram's Class diagram
Explanation: The diagram shows that the program will have 3 data tables or classes in the database called “User”, “Trading Partner”, and “Invoice” as well as the attributes and methods in each data table. The diagram also demonstrates that the User data table to the Trading Partner data table has a “one to many” relationship and that the Trading Partner data table to the Invoice data table also has a “one to many” relationship.

### UML diagram/Sequence diagram 
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_Sequence%20diagram.png)
Image 7: UML diagram/Sequence diagram of a method in the program
Explanation: This diagram shows how a method can be carried out through the 3 data tables “User”, “Trading Partner”, “Invoice”. In this diagram, the get_info() method in the User table is being carried out. First, it needs to request wanted information (all_info) from the Trading Partner data table; the Trading Partner data table then needs to request wanted information (all_info) from the Invoice data table. This method demonstrates the filter/search invoices function the user could carry out in the program.

### ER diagram 
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/ER%20diagram%20for%20CS%20IA%20(1).png)
Image 8: ER diagram of the program
## Forgot to add the column Invoice number and Occurent into the Invoice class database. Need to add this in to the designs later.
Explanation: This diagram shows the UML diagram/Class diagram (Image 6) in a way that is easier to see the various attributes (orange circles) in each data table (white rectangles). Also, each primary key attribute is in a red circle.

### Flow diagram of general processes 
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_Flow%20Diagram.png)
Image 9: Flow diagram of general processes of the program
Explanation: This diagram shows the general processes an user could carry out with the program.

### Need to add 2~3 flow diagram of some "complicated" algorithms with explanations in!!!

### Database normalization:
1. For the User class:

| id | username | password      |
|----|----------|---------------|
| 1  | Lam      | hash_password |
| 2  | X        | hash_password |
| 3  | Y        | hash_password |


Table 1: A data table of the User class in the database in the program with example data
Explanation: This table shows the User data table/class in the database. The table will contain the primary key attribute “id”, the unique attribute “username”, and a normal attribute called “password”.

2. For the Trading partner class:

| id | trading_partner_name | supplier_name | sector        | contract_days | remit_to_bank_account_name | remit_to_bank_account_number | priority_rank |
|----|----------------------|---------------|---------------|---------------|----------------------------|------------------------------|---------------|
| 1  | X partner            | X             | Entertainment | 14            | Mistsubishi                | 00012                        | 3             |
| 2  | YKJ                  | YKJ           | Financial     | 7             | Yuchou                     | 00001                        | 1             |
| 3  | ooo.com              | ooo           | Security      | 14            | Miyazaki                   | 02200                        | 1             |

Table 2: A data table of the Trading partner class in the database in the program with example data
Explanation: This table shows the Trading partner class in the database. The table will contain the primary key attribute "id", the unique attribute "trading_partner_name", and various other normal attributes such as "supplier_name", "sector".


3. For the Invoice class:
## Forgot to add the column Invoice number and Occurent into the Invoice class database. Need to add this in to the designs later.

| id | invoice_date | invoice_amount | invoice_currency | invoice_added_date | tax  | description     | expired_contract_date | actual_payment_date | actual_payment_accepted_by | overdue_period | notes_for_penalty_overdue | paid | paid_amount | payment_unpaid_amount | payment_date1 | payment_date2 | added_by_user |
|----|--------------|----------------|------------------|--------------------|------|-----------------|-----------------------|---------------------|----------------------------|----------------|---------------------------|------|-------------|-----------------------|---------------|---------------|---------------|
| 1  | 2021-07-15   | 300000         | yen              | 2021-07-15         | 10   | invoice for xyz | 2021-08-15            | 2021-12-15          | By VNA                     | 120            | plus 12.5% annually       | 0    | 0           | 300000                |               |               | Lam           |
| 2  | 2021-07-13   | 50000          | yen              | 2021-07-15         | 12.5 | ...             | 2021-08-13            | 2021-09-09          | Partner                    | 27             | plus 0.01% daily          | 0.5  | 20000       | 30000                 | 2021-08-10    |               | Mizawa        |
| 3  | 2021-07-14   | 20000          | dollars          | 2021-07-15         | 10   | ....            | 2021-08-14            | 2021-11-12          | By VNA                     | 91             | plus 1% monthly           | 1    | 20000       | 0                     | 2021-11-10    | 2021-11-11    | Konoha        |

Table 3: A data table of the Invoice class in the database in the program with example data
Explanation: This table shows the Invoice class in the database. The table will contain the primary key attribute "id", and various other normal attributes such as "invoice_date", "invoice_amount".

### Testing plan

Before presenting the program to Mr Lam, I plan to do various types of testings to make sure the program works as expected and fits for him.
I've create a plan that I followed to test my program:
1. Alpha testing (I will check the program by myself while going through Alpha, Beta testing table)
2. Beta testing with a computer science expert (I will ask my Computer Science classmate to check my program by using Alpha, Beta testing table)
3. Beta testing with an external expert (I will ask an external expert, who is not taking Computer Science and not interested in coding at all, to check my program by using Alpha, Beta testing table). This allowed me to make sure that my program could be used even by someone who is not familiar with Computer Science.
4. User acceptance testing (I will ask Mr Lam to use the program while using User acceptance testing table)



| Success Criteria (need to test all success  criteria in Criterion A)                                                                                                                                                                     | Procedures and Expected outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Criteria met? Alpha testing | Criteria met?  Beta testing with computer science  expert | Criteria met? Beta testing with  external expert |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------------|--------------------------------------------------|
| 1. Being able to input/edit/remove/clear any or all data columns or each row of each  invoice and save those data in the program                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 2. Being able to view all data columns of each invoices save in the column                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 3. Program lets the client to input fixed data columns about the Trading Partner and pre-stored  data in these fixed data columns for every subsequent invoices added to the program after  the first time                               | The program should allows the user to input info about Trading partner only once and then can add multiple invoices with that Trading partner info without having to input info about it again. => Info about the invoices will be keep relatively with info of the trading partner in the database=> when need to show all information about an invoice, using the relativeness between the 2 database tables, the program could query up info from the  Trading partner and show it alongside info of the invoice.                                                                                                                                                                                                     | Yes                         |                                                           |                                                  |
| 4. Program will show error messages and ask the client to re-input data about the invoices when there  exist data entry errors (such as wrong data type for the data column)                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 5. Program will show warning/confirmation message asking the client if he is sure before making a change  to the program                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 6. Each of data columns contains the required data format by the clients (some are number, string, date)                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 7. Let the client filtered/search invoices based on required data columns such as Invoice Number,  Payment information, the Actual Payment time, Priority rank, Paid, Sector, Supplier Name into tables  that are viewable on the screen |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 8. Let the client create 2 main types of reports: Overdue Invoice Report and Invoice Payment Schedule  Report and export them to reports in Excel and PDF formats.                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 9. Let the client view and edit/remove all data columns of each invoices shown on the filtered/searched tables                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 10. Let the client export the filtered/search invoices tables to reports in Excel and PDF formats.                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 11. Let the client export the whole database of invoices to reports in Excel and PDF formats.                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 12. Each of the 2 main types of reports will need to be structured in the way that the client want  (including headers, report generated time, font type)                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |
| 13. The program will have a login and logout screen                                                                                                                                                                                      | 1. To login when not registered an username yet: Run the program => redirected to the LOGIN screen=>click on "Register" button=>redirected to the REGISTER screen=> fill out a new username and  set up a password for it=> click on "Regsiter" button again=> redirected back to the LOGIN screen=> input your just now registered username and password  in the LOGIN screen=> click on "Log in" button=> redirected to HOME screen ;  2. To login when already registered an username: Input your registered username and password  in the LOGIN screen=> click on "Log in" button=> redirected to HOME screen  ; 3. To logout, simply click on "Log out" button in the HOME screen=> redirected to the LOGIN screen. | YES                         |                                                           |                                                  |
| 14. The program will let multiple user creates their account and passwords, storing those passwords  in hashed                                                                                                                           | If the developers go into the database of the program to the place where it keeps user information, the developer will not be able to understand the real password of the users to log in with the user's account because all he or she can she is hashed password in the form of random combinations of letters and numbers such as "a38fjx3hsj3u".                                                                                                                                                                                                                                                                                                                                                                     | YES                         |                                                           |                                                  |
| 15. The program will show a message each time the client exported a report saying that he should back  it up by putting it into the hard drive or hard disk                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                             |                                                           |                                                  |

Table 4: Alpha, Beta testing table

| No. | Success Criteria                                                                                                                                                               | Procedures | Expected Outcome | Met? |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|------------------|------|
| 1   | Being able to input/edit/remove/clear any or all data columns or each row of each invoice and save those data in the program                                                                                    |            |                  |      |
| 2   | Being able to view all data columns of each invoices save in the column                                             |            |                  |      |
| 3   | Program lets the client to input fixed data columns about the Trading Partner and pre-stored data in these fixed data columns for every subsequent invoices added to the program after the first time |            |                  |      |
| 4   | Program will show error messages and ask the client to re-input data about the invoices when there exist data entry errors (such as wrong data type for the data column)                                                   |            |                  |      |
| 5   | Program will show warning/confirmation message asking the client if he is sure before making a change to the program                                                         |            |                  |      |
| 6   | Each of data columns contains the required data format by the clients (some are number, string, date)                                                                                                  |            |                  |      |
| 7   | Let the client filtered/search invoices based on required data columns such as Invoice Number, Payment information, the Actual Payment time, Priority rank, Paid, Sector, Supplier Name into tables that are viewable on the screen                                                                                    |            |                  |      |
| 8   | Let the client create 2 main types of reports: Overdue Invoice Report and Invoice Payment Schedule Report and export them to reports in Excel and PDF formats.                                                                                                                     |            |                  |      |
| 9   | Let the client view and edit/remove all data columns of each invoices shown on the filtered/searched tables                      |            |                  |      |
| 10  | Let the client export the filtered/search invoices tables to reports in Excel and PDF formats.               |            |                  |      |
| 11  | Let the client export the whole database of invoices to reports in Excel and PDF formats.                                                                                                       |            |                  |      |
| 12  | Each of the 2 main types of reports will need to be structured in the way that the client want (including headers, report generated time, font type)                                                                                |            |                  |      |
| 13  | The program will have a login and logout screen                         |            |                  |      |
| 14  | The program will let multiple user creates their account and passwords, storing those passwords in hashed                        |            |                  |      |
| 15  | The program will show a message each time the client exported a report saying that he should back it up by putting it into the hard drive or hard disk |            |                  |      |


Table 5: User acceptance testing table

### Record of tasks (needed to be updated during the life of the program)

| Task number | Planned action                                                                                       | Planned outcome                                                                                                                                                                                                                                                                                                                                               | Time estimated | Target completion date | Criterion |
|-------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | Finding a client that is in  need of a program                                                       | Chosen a problem to create a program for. Found the client I'm creating the program for                                                                                                                                                                                                                                                                       | 1 week         | May 26, 2021           | A         |
| 2           | Have an interview with Mr Lam                                                                        | Understand about the requirements and success criteria of the program from Mr Lam                                                                                                                                                                                                                                                                             | 1 week         | June 2, 2021           | A         |
| 3           | Finish documenting Criterion A,  writing the scenario, rationale, and  success criteria              | the whole Criterion A is fully  documented with the success criteria approved by Mr Lam                                                                                                                                                                                                                                                                       | 1 week         | June 9, 2021           | A         |
| 4           | Designing the program                                                                                | Had a sketched of the program.Various  diagrams like UML, ER, system diagram is drawn.The sketch will be turned into a clean online design. Documentation explaining how these diagrams works will be written into Criterion B. A testing plan   will also be finished and added to Criterion B.  Also, a Record of tasks table will be added to Criterion B. | 1 week         | June 16, 2021          | B         |
| 5.          | Finish documenting Criterion B (adding record of tasks, diagrams, diagrams' explanations, test plan) | the whole Criterion B is fully documented                                                                                                                                                                                                                                                                                                                     | 1 day          | June 17, 2021          | B         |
| 6.          |    Code everything, following all the things in Criterion B: Planning                                                                                                  |     A working program will be coded and be ready for testing                                                                                                                                                                                                                                                                                                                                                          |    1 week            |        June 24, 2021                | C         |
| 7.          |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | C         |
| 8.          |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | C         |
| 9.          |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | D         |
| 10.         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | E/A       |
| 11.         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | E         |
| 12.         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | D         |

Table 6: Record of tasks's table

## Criterion C: Codings
##### 1.Codes to convert data in an sqlite database's table to Excel using safe query with SQLAlchemy ORM:

(Snack in the codes below is an sqlite database table)
(the Excel file will be stored in output.xlsx)
```.py

    def export_docs4(self):

        s = session()
        workbook = Workbook('output.xlsx')
        worksheet = workbook.add_worksheet()

        all_data = s.query(Snack).all()
        data_list = [to_dict(item) for item in all_data]
        print(data_list)

        worksheet.write(0, 0, "id")
        worksheet.write(0, 1, "Snack name")
        worksheet.write(0, 2, "Amount")
        worksheet.write(0, 3, "Price")
        worksheet.write(0, 4, "User id")

        # I can basically manipuulate the whole area where I should place the table
        # from the database. I can then use worksheet.write() to manually
        # write a few other value in the excel file.
        row_index = 0

        for i in range(len(data_list)):
            row_index +=1
            column_index = 0
            for key in data_list[i]:
                worksheet.write(row_index, column_index,data_list[i][key])
                column_index += 1


        workbook.close()


```



##### 2.Codes to convert data in an sqlite database's table to PDF using safe query with SQLAlchemy ORM:

(Snack in the codes below is an sqlite database table)
(the PDF file will be stored in CoinSnack2.pdf)

```.py

    def export_pdf(self):
        s = session()
        all_data = s.query(Snack).all()

        data_list = [to_dict(item) for item in all_data]
        print(data_list)


        pdf = FPDF()
        pdf.add_page()

        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times', 'B', 14.0)
        pdf.cell(page_width, 0.0, 'CoinSnack Data', align='C')
        pdf.ln(10)

        pdf.set_font('Courier', '', 12)

        col_width = page_width / 5

        pdf.ln(1)

        th = pdf.font_size


        for x in range(1):
            pdf.cell(col_width, th, txt="id", border=1)
            pdf.cell(col_width, th,  txt="name", border=1)
            pdf.cell(col_width, th,  txt="amount", border=1)
            pdf.cell(col_width, th,  txt="price", border=1)
            pdf.cell(col_width, th,  txt="user_id", border=1)
            pdf.ln(th)

        pdf.ln(1)

        for i in range(len(data_list)):
            pdf.cell(col_width, th, str(data_list[i]["id"]), border=1)
            pdf.cell(col_width, th, str(data_list[i]["name"]), border=1)
            pdf.cell(col_width, th, str(data_list[i]["amount"]), border=1)
            pdf.cell(col_width, th, str(data_list[i]["price"]), border=1)
            pdf.cell(col_width, th, str(data_list[i]["user_id"]), border=1)
            pdf.ln(th)

        s.close()
        pdf.output("Coinsnack2.pdf")

```

##### 3.Codes to package the Kivy-Python-Kivy project into exe, dmg file:
Step 1: create a spec file "something.spec" in the same directory with main.py and main.py
Step 2: install kivymd package directly in Pycharm project congigurations
Step 3: Paste the codes below into the spec file:

```.spec

# -*- mode: python ; coding: utf-8 -*-

#the hook below is very important because it connects kivymd with the package:
from kivymd import hooks_path as kivymd_hooks_path
block_cipher = None

#changes the '/Users/kienletrung/Desktop/CoinSnack_MiniIA/main.py' below to the
#path to the python python file of the whole project. change the #'/Users/kienletrung/Desktop/CoinSnack_MiniIA' below to the folder that holds the previous python file.
a = Analysis(['/Users/kienletrung/Desktop/CoinSnack_MiniIA/main.py'],
             pathex=['/Users/kienletrung/Desktop/CoinSnack_MiniIA'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[kivymd_hooks_path],
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

#adds other files that are not the main python file with the way below: (needs to change the #'/Users/kienletrung/Desktop/CoinSnack_MiniIA/main.kv' to the appropriate path to the file)
a.datas += [('main.kv', '/Users/kienletrung/Desktop/CoinSnack_MiniIA/main.kv', 'DATA')]

#needs to change '/Users/kienletrung/Desktop/CoinSnack_MiniIA' to the path that holds the data that I add in the above line. change the "coinsnack" name to appropriate app name.
exe = EXE(pyz, Tree('/Users/kienletrung/Desktop/CoinSnack_MiniIA', 'Data'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='coinsnack',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='coinsnack.app',
             icon=None,
             bundle_identifier=None)


```
The codes above is created from the combination of the 2 tutorials below:
1.https://stackoverflow.com/questions/35952595/kivy-compiling-to-a-single-executable
2.https://kivymd.readthedocs.io/en/0.104.1/unincluded/kivymd/tools/packaging/pyinstaller/index.html

Step 3: Run the below codes step by step in the terminal:
```
pyinstaller -y --clean --windowed "something".spec

```

then 

```
pushd dist

```
then

```
hdiutil create ./myapp.dmg -srcfolder myapp.app -ov
```
(change myapp to the name of your app that you wrote in your spec file)

then

```
popd

```
After this, an exe file, a dmg file will be in the "dist" folder in the main folder. To run the exe file, the user just need to click on it. Looks like data can actually be saved on an exe file.
