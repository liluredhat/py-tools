# coding=utf-8
'''
Created on Jul 3, 2017

@author: lilu
'''
import xlrd

if __name__ == '__main__':
    data = xlrd.open_workbook('input.xls', 'r')
    #data2 = xlrd.open_workbook('output.xls', 'w')
    #table2 = data2.sheets()[0]
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    print "总行数:", nrows, ",总列数:", ncols
    print ""
    print "工号，姓名，工时"
    x = 0
    for num in range(4, nrows):
        # print num
        ghcell = table.cell(num, 1).value
        xmcell = table.cell(num, 2).value
        gscell = table.cell(num, 15).value
        if (gscell != "0.0"):
            print ghcell, "|", xmcell, "|", gscell
            # table2.put_cell(7 + x, 0, 1, ghcell, 0)
            x += 1
            # print x
