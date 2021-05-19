# IB Computer Science IA by Kien Le Trung


##### Codes to convert data in an sqlite database's table to Excel using safe query with SQLAlchemy ORM:

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
