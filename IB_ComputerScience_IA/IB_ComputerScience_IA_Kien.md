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


### Stating Success Criteria (checked and agreed upon by the client) 
1. Being able to view all data columns of each invoices save in the column
2. Let the client add/edit/remove invoices.
3. Program lets the client to input fixed data columns about the Trading Partner and pre-stored data in these fixed data columns for every subsequent invoices added to the program after the first time
4. Each of data columns contains the required data format by the clients (some are number, string, date)
5. Let the client filtered/search invoices based on required data columns such as Invoice Number, Payment information, the Actual Payment time, Priority rank, Paid, Sector, Supplier Name into tables that are viewable on the screen
6. Let the client export the filtered/search invoices tables (the invoices don't need to include trading partner data columns) to reports in Excel format.
7. Let the client export the whole database of invoices to reports in Excel format.
8. Let the client create 2 main types of reports: Overdue Invoice Report and Invoice Payment Schedule Report and export them to reports in Excel format.
9. Each of the 2 main types of reports will need to be structured in the way that the client want (including headers, report generated time, font type)
10. The program will have a login and logout screen
11. The program will let multiple user creates their account and passwords, storing those passwords in hashed


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
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/ER%20diagram%20for%20CS%20IA%20(2).png)
Image 8: ER diagram of the program
Explanation: This diagram shows the UML diagram/Class diagram (Image 6) in a way that is easier to see the various attributes (orange circles) in each data table (white rectangles). Also, each primary key attribute is in a red circle.

### Flow diagram of general processes 
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CSIA_Flow%20Diagram.png)
Image 9: Flow diagram of general processes of the program
Explanation: This diagram shows the general processes an user could carry out with the program.

### Need to add 2~3 flow diagram of some "complicated" algorithms with explanations in!!!

### Diagram 1: a diagram showing the algorithm that receives certain values from the Filter/Search Screen and uses certain conditions (only 3 conditions in this diagram) to query/shows  appropriate invoices on to the Filtered/Seacrhed Screen:
![](https://github.com/BrightChanges/Unit-4/blob/main/IB_ComputerScience_IA/CS%20IA-Algorithm%20Diagram%201.png)
Explanation: ......




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

| id | trading_partner_name | supplier_name | sector        | contract_days | remit_to_bank_account_name | remit_to_bank_account_number | priority_rank | trading_partner_added_by_user |
|----|----------------------|---------------|---------------|---------------|----------------------------|------------------------------|---------------|------|  
| 1  | X partner            | X             | Entertainment | 14            | Mistsubishi                | 00012                        | 3             | Kien |
| 2  | YKJ                  | YKJ           | Financial     | 7             | Yuchou                     | 00001                        | 1             | Kien |
| 3  | ooo.com              | ooo           | Security      | 14            | Miyazaki                   | 02200                        | 1             | Son  |

Table 2: A data table of the Trading partner class in the database in the program with example data
Explanation: This table shows the Trading partner class in the database. The table will contain the primary key attribute "id", the foreign key attribute "trading_partner_added_by_user", the unique attribute "trading_partner_name", and various other normal attributes such as "supplier_name", "sector".


3. For the Invoice class:

| id | trading_partner_id | trading_partner_name | invoice_number | invoice_date | invoice_amount | invoice_currency | invoice_added_date | tax | description              | expired_contract_date | actual_payment_date | actual_payment_accepted_by | overdue_period | notes_for_penalty_overdue | paid | paid_amount | payment_unpaid_amount | payment_date1 | payment_date2 | occurent | invoice_added_by_user |
|----|--------------------|----------------------|----------------|--------------|----------------|------------------|--------------------|-----|--------------------------|-----------------------|---------------------|----------------------------|----------------|---------------------------|------|-------------|-----------------------|---------------|---------------|----------|-----------------------|
| 5  | 1                  | XX partner           | UUII777        | 2021-05-05   | 30000          | yen              | 2021-10-04         | 11  | Invoice for X calculator | 2021-05-20 00:00:00   | 2021-05-20 00:00:00 |                            |                |                           | 0    |             | 30000                 |               |               |          | Kien                  |
| 2  | 1                  | XX partner           | HJSE234HD1     | 2021-08-08   | 72500          | yen              | 2021-08-17         | 10  | Invoice for X sandwiches | 2021-08-23 00:00:00   | 2021-08-23 00:00:00 | Partner                    | 30             | +1% every late month      | 0.5  | 30000       | 42500                 | 2021-08-15    | 2021-08-17    |          | Kien                  |

Table 3: A data table of the Invoice class in the database in the program with example data
Explanation: This table shows the Invoice class in the database. The table will contain the primary key attribute "id", foreign key attribute "trading_partner_id", "trading_partner_name", "invoice_added_by_user" and various other normal attributes such as "invoice_date", "invoice_amount".

### Testing plan

Before presenting the program to Mr Lam, I plan to do various types of testings to make sure the program works as expected and fits for him.
I've create a plan that I followed to test my program:
1. Alpha testing (I will check the program by myself while going through Alpha, Beta testing table)
2. Beta testing with a computer science expert (I will ask my Computer Science classmate to check my program by using Alpha, Beta testing table)
3. Beta testing with an external expert (I will ask an external expert, who is not taking Computer Science and not interested in coding at all, to check my program by using Alpha, Beta testing table). This allowed me to make sure that my program could be used even by someone who is not familiar with Computer Science.
4. User acceptance testing (I will ask Mr Lam to use the program while using User acceptance testing table)


Table 4: Alpha, Beta testing table: https://docs.google.com/document/d/1-_ISVS1W7aH0rCwRt42uZ0E67l6drlf5NMVLlh5MSxs/edit?usp=sharing

| No. |                                                                                                            Success Criteria                                                                                                            | Procedures | Expected Outcome | Met? |
|:---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------:|:----------------:|:----:|
| 1   |   Being able to view all data columns of each invoices save in the column                                                                                                                                                              |            |                  |      |
| 2   |   Let the client add/edit/remove invoices.                                                                                                                                                                                             |            |                  |      |
| 3   |   Program lets the client to input fixed data columns about the Trading Partner and pre-stored data in these fixed data columns for every subsequent invoices added to the program after the first time                                |            |                  |      |
| 4   |   Each of data columns contains the required data format by the clients (some are number, string, date)                                                                                                                                |            |                  |      |
| 5   |   Let the client filtered/search invoices based on required data columns such as Invoice Number, Payment information, the Actual Payment time, Priority rank, Paid, Sector, Supplier Name into tables that are viewable on the screen  |            |                  |      |
| 6   |   Let the client export the filtered/search invoices tables (the invoices don't need to include trading partner data columns) to reports in Excel format.                                                                              |            |                  |      |
| 7   |   Let the client export the whole database of invoices to reports in Excel format.                                                                                                                                                     |            |                  |      |
| 8   |   Let the client create 2 main types of reports: Overdue Invoice Report and Invoice Payment Schedule Report and export them to reports in Excel format.                                                                                |            |                  |      |
| 9   |   Each of the 2 main types of reports will need to be structured in the way that the client want (including headers, report generated time, font type)                                                                                 |            |                  |      |
| 10  |   The program will have a login and logout screen                                                                                                                                                                                      |            |                  |      |
| 11  |   The program will let multiple user creates their account and passwords, storing those passwords in hashed                                                                                                                            |            |                  |      |

Table 5: User acceptance testing table

### Record of tasks (needed to be updated during the life of the program)

| Task number |                                             Planned action                                            |                                                                                                                                                                         Planned outcome                                                                                                                                                                         | Time estimated | Target completion date | Criterion |
|:-----------:|:-----------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------:|:----------------------:|:---------:|
| 1           | Finding a client that is in need of a program                                                         | Chosen a problem to create a program for.  Found the client I'm creating the program for                                                                                                                                                                                                                                                                        | 1 week         | May 26, 2021           | A         |
| 2           | Have an interview with Mr Lam                                                                         | Understand about the requirements and success  criteria of the program from Mr Lam                                                                                                                                                                                                                                                                              | 1 week         | June 2, 2021           | A         |
| 3           | Finish documenting Criterion A,  writing the scenario, rationale, and success criteria                | the whole Criterion A is fully documented with  the success criteria approved by Mr Lam                                                                                                                                                                                                                                                                         | 1 week         | June 9, 2021           | A         |
| 4           | Designing the program                                                                                 | Had a sketched of the program.Various diagrams  like UML, ER, system diagram is drawn.The sketch  will be turned into a clean online design. Documentation  explaining how these diagrams works will be written into  Criterion B. A testing plan will also be finished and added  to Criterion B. Also, a Record of tasks table will be added  to Criterion B. | 1 week         | June 16, 2021          | B         |
| 5.          | Finish documenting Criterion B  (adding record of tasks, diagrams, diagrams' explanations, test plan) | the whole Criterion B is fully documented                                                                                                                                                                                                                                                                                                                       | 1 week         | June 24, 2021          | B         |
| 6.          | Code everything, following all the things in Criterion B: Planning                                    | A working program will be coded and be ready for testing                                                                                                                                                                                                                                                                                                        | 3 months       | September 24, 2021     | C         |
| 7.          | Finish documenting Criterion C (explain codes that help meet the  client's criteria)                  | the whole Criterion C is fully documented                                                                                                                                                                                                                                                                                                                       | 2 weeks        | October 8, 2021        | C         |
| 8.          |                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                 |                |                        | C         |
| 9.          |                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                 |                |                        | D         |
| 10.         |                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                 |                |                        | E/A       |
| 11.         |                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                 |                |                        | E         |
| 12.         |                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                 |                |                        | D         |

Table 6: Record of tasks's table

## Criterion C: Codings
#### Link to the whole 1000 words documentation: https://docs.google.com/document/d/1jljeTFvTt6mOSC_bktE919fQCcQA4goVmXHe-pQ79y8/edit?usp=sharing

