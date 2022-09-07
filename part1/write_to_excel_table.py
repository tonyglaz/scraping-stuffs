import xlsxwriter
from part1.smth import run_function


def writer(param):
    book = xlsxwriter.Workbook(r"data.xlsx")
    page = book.add_worksheet("товар")

    row, col = 0, 0
    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 20)

    for item in param():
        page.write(row, col, item[0])
        page.write(row, col+1, item[1])
        page.write(row, col+2, item[2])
        page.write(row, col+3, item[3])
        row += 1

    book.close()


writer(run_function)
