# IB Computer Science IA by Kien Le Trung

## Criterion A: Planning
### Defining the problem
Client Mr Lam is my father, and he works in accounting in an airline company. During Covid time, his company was unable to pay in time for many services in Japan. Because of this, he needs to take a lot more time than before to manually checks through his Oracle's invoices logs to see which invoice is overdue and which invoice needs to pay first (in order to avoid or minimize penalties based on signed contracts with those services) and fill them in Excel reports, which he will then need to send them to his company. This takes him a lot of time and he complained this to me once during our usualy family video call on May 2021. He said he wanted a program that could help him record invoices and quickly export reports to see which invoices his company needed to pay first, which invoices are paid, and more.

As he was saying, I thought that I could create that program for him through my Internal Assessment. I thought that this would be very cool because he needs a Computer Science solution to his problem, and I could bring that solution to him.

In order to understand more about the program for Mr Lam, I decided to schedule an interview with Mr Lam.
(Interview 1, 2021) in Appendix

### Rationale for Proposed Solution
...

### Stating Success Criteria 
...
The above stating success Criteria had been consulted and agreed upon with Mr Lam on our second interview. (Interview 2, 2021) in Appendix


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
