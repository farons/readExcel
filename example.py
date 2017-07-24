# -*- coding: utf-8 -*- 
 2 import xdrlib ,sys
 3 import xlrd
 4 def open_excel(file= 'file.xls'):
 5     try:
 6         data = xlrd.open_workbook(file)
 7         return data
 8     except Exception,e:
 9         print str(e)
10 #根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
11 def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
12     data = open_excel(file)
13     table = data.sheets()[by_index]
14     nrows = table.nrows #行数
15     ncols = table.ncols #列数
16     colnames =  table.row_values(colnameindex) #某一行数据 
17     list =[]
18     for rownum in range(1,nrows):
19 
20          row = table.row_values(rownum)
21          if row:
22              app = {}
23              for i in range(len(colnames)):
24                 app[colnames[i]] = row[i] 
25              list.append(app)
26     return list
27 
28 #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
29 def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
30     data = open_excel(file)
31     table = data.sheet_by_name(by_name)
32     nrows = table.nrows #行数 
33     colnames =  table.row_values(colnameindex) #某一行数据 
34     list =[]
35     for rownum in range(1,nrows):
36          row = table.row_values(rownum)
37          if row:
38              app = {}
39              for i in range(len(colnames)):
40                 app[colnames[i]] = row[i]
41              list.append(app)
42     return list
43 
44 def main():
45    tables = excel_table_byindex()
46    for row in tables:
47        print row
48 
49    tables = excel_table_byname()
50    for row in tables:
51        print row
52 
53 if __name__=="__main__":
54     main()