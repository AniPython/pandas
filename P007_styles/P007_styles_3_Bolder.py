from openpyxl.styles import (
    Border,  # 边框
    Side,  # 边
)
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

style_list = ['dotted', 'dashDot', 'medium', 'mediumDashed', 'mediumDashDot', 'dashDotDot',
              'mediumDashDotDot', 'slantDashDot', 'hair',
              'thick', 'double', 'dashed', 'thin']

for i, style in enumerate(style_list, start=1):
    cell = ws['B' + str(i)]
    cell.value = style
    cell.border = Border(
        bottom=Side(border_style=style,
                    color='FF0000'),
        left=Side(border_style='medium',
                  color='0000FF')
    )

wb.save('border.xlsx')
