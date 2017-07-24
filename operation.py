import xlrd
from  re import sub

# 函数open_excel(filename): 打开一个文件，filename为文件的地址 
def open_excel(filename):
    try:
        data = xlrd.open_workbook(filename)
        return data
    except Exception as e:
        print(str(e))

# 函数excel_table_all（filename, x, y):根据起始位置将excel文件读到listAll中，x,y表示行列起始点
def excel_table_all(filename, x, y):     # 文件名称，起始位置
    data = open_excel(filename)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    listAll = []
    for i in range(x, nrows):
        p = []
        for j in range(y, ncols):
            if isinstance(table.cell(i,j).value, float):    # 浮点数转整形
                p.append(str(int(table.cell(i,j).value)))    # 转换成字符串
            else:
                p.append(table.cell(i,j).value)
        listAll.append(p)
    return listAll  

# 函数excel_list_standard(list, num_cols, num_rows):  list：表示传入的数据列表   num_cols:表示不标准的列数,例如序号，单位，名称，地址   mun_rows:表示标准的行数：对应不标准  3:1  3行标准=一行标准
def excel_list_standard(dataList, num_cols, num_rows):
    print("行数：", len(dataList))
    print("列数：", len(dataList[0]))
    list_base = []
    for length in range(num_cols):
        list_base.append("default")
    print(list_base)
    print('length:',len(list_base))   
    for i in range(len(dataList)):
        k = i % num_rows
        if k == 0:
            for j in range(num_cols):
                list_base[j] = dataList[i][j]
        else:
            for j in range(num_cols):
                dataList[i][j] = list_base[j]
    return dataList
# 函数write_txt:将一个list中的数据写入txt文件  
def write_txt(filename,data):     # filename:数据去向，  data：数据来源
    with open(filename,'w') as f:
        for index in range(len(data)):    # 获得每行的信息，并按行写入
            strStandard = str(data[index]).replace("\'",'').replace('[','').replace(']','').replace(' ','')    # 去除字符串中的'[' ,']','\'',' '
            f.write(strStandard)
            f.write('\n')
