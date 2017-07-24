import xlrd
import operation

datalist = operation.excel_table_all("data.xlsx",1,0)    # 将xlsx中所有数据导入datalist

datalist_s = operation.excel_list_standard(datalist,3,3)    # 将datalist按要求标准化为datalist_s

operation.write_txt('data.txt',datalist_s)    # 将标准化的datalist_s进一步按要求写入txt文件