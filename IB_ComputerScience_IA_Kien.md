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

I am learning them at school.
Python provides flexibility in back end codings
Python has a large amount of libraries that I could use to ease the coding process
Kivy and Kivymd provide pleasant and easy to use front end screens and data tables 
Python provides compatibility with SQL and SQLAlchemy, helping me to more easily creates database and connects it to the program
After creating one screen with Kivy and Kivymd, it is easy to creates another screen by copying and making small changes
A Python, Kivy, Kivymd program could be compiled into one .exe file and used as a desktop application, which suits the program type my client wants


### Stating Success Criteria 
1. Being able to input/update/edit/remove any or all data columns or each row of each invoice
2. Program lets the client to input/update/edit/remove to up to 22 data columns such as Trading Partner Name, Supplier Name, Sector 
3. Program lets the client to input fixed data columns and pre-stored data in these fixed data columns for every subsequent invoices added to the program after the first time
4. Program will show error messages and ask the client to re-input data about the invoices when there exist data entry errors
5. Program will show warning/confirmation message asking the client if he is sure before making a change to the program
6. Each of the 22 data columns contains the required data format by the clients
7. Invoices are searchable through 4 data columns such as Invoice Number, Payment information
8. Let the client view Payment information about each invoice
9. Let the client filtered invoices based on required data columns such as the Actual Payment time, Priority rank, Paid, Sector, Supplier Name into tables
10. Let the client create 2 main types of reports: Overdue Invoice Report and Invoice Payment Schedule Report and export them to reports in Excel and PDF formats.
11. Let the client view the filtered/searched invoices tables on the screen
12. Let the client export the filtered/search invoices tables to reports in Excel and PDF formats.
13. Each of the 2 main types of reports will need to be structured in the way that the client want (including headers, report generated time, font type)

## Criterion B: Solution Overview

### Idea sketches
![]()
Image 1:....
Explanation:

### System diaram (digital)
![]()
Image 2:....
Explanation:

### Clean design of the sketches (digital)
![]()
Image 3:....
Explanation:

### UML diagram (digital)
![]()
Image 4:....
Explanation:

### ER diagram (digital)
![]()
Image 5:....
Explanation:

### Flow diagram of X process (digital)
![]()
Image 6:....
Explanation:

### Sequence diagram (maybe don't need) (digital)
![]()
Image 7:....
Explanation:

### Database normalization (digital)
![]()
Image 8:....
Explanation:

### Testing plan

### Record of tasks (needed to be updated during the life of the program)

| Task number | Planned action                                                                                       | Planned outcome                                                                                                                                                                                                                                                                                                                                               | Time estimated | Target completion date | Criterion |
|-------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | Finding a client that is in  need of a program                                                       | Chosen a problem to create a program for. Found the client I'm creating the program for                                                                                                                                                                                                                                                                       | 1 week         | May 26, 2021           | A         |
| 2           | Have an interview with Mr Lam                                                                        | Understand about the requirements and success criteria of the program from Mr Lam                                                                                                                                                                                                                                                                             | 1 week         | June 2, 2021           | A         |
| 3           | Finish documenting Criterion A,  writing the scenario, rationale, and  success criteria              | the whole Criterion A is fully  documented with the success criteria approved by Mr Lam                                                                                                                                                                                                                                                                       | 1 week         | June 9, 2021           | A         |
| 4           | Designing the program                                                                                | Had a sketched of the program.Various  diagrams like UML, ER, system diagram is drawn.The sketch will be turned into a clean online design. Documentation explaining how these diagrams works will be written into Criterion B. A testing plan   will also be finished and added to Criterion B.  Also, a Record of tasks table will be added to Criterion B. | 1 week         | June 16, 2021          | B         |
| 5.          | Finish documenting Criterion B (adding record of tasks, diagrams, diagrams' explanations, test plan) | the whole Criterion B is fully documented                                                                                                                                                                                                                                                                                                                     | 1 day          | June 17, 2021          | B         |
| 6.          |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | C         |
| 7.          |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | C         |
| 8.          |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | C         |
| 9.          |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | D         |
| 10.         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | E/A       |
| 11.         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | E         |
| 12.         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                               |                |                        | D         |

Table 1: Record of tasks's table

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
