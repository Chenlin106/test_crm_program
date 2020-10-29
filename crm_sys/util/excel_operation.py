import xlrd
class OperationExcel:
    def __init__(self,path,sheet_name):
        # 获取excel工作簿对象
        self.workbook=xlrd.open_workbook(path)
        #获取sheet
        self.sheet=self.workbook.sheet_by_name(sheet_name)
    def get_nrows(self):
        return self.sheet.nrows
    def get_ncols(self):
        return self.sheet.ncols
    def get_cell(self,row,col):
        cell_v=self.sheet.cell_value(row,col)
        if cell_v == 'null':
            return ''
        return cell_v
# if __name__ == '__main__':
#     excel = OperationExcel('G:\\test_case.xlsx','Sheet1')
#     for row in range(0,excel.get_nrows()):
#         for col in range(0,excel.get_ncols()):
#             print(excel.get_cell(row,col),end=' ')
#         print()