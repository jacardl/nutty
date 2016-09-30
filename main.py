#coding=utf8
from __future__ import division
from openpyxl import Workbook, load_workbook
from openpyxl.cell import column_index_from_string

from api import *
import var as v

def ProcessSheet1Xlsx():
    DUT = ["R1CM", "R1D", "R2D", "R1CL", "R3", "R3L", "Android", "iOS"]
    SUBTYPE = ["CrashLog次数", "CrashLog用户数"]
    try:
        wb = load_workbook(v.FILE_NAME)
    except:
        print "specific file is not exist"
        return
    for cell in wb[v.SHEET1].get_cell_collection():
        if cell.value == "new":
            _ = cell.row
            newY = column_index_from_string(cell.column)
            break
    for dut in DUT:
        for cell in wb[v.SHEET1].get_cell_collection():
            if cell.value == dut:
                dutX = cell.row
                _ = column_index_from_string(cell.column)
                break
        crashCount = getKernelCrashAveDaily(dut, SUBTYPE[0])
        crashUser = getKernelCrashAveDaily(dut, SUBTYPE[1])
        if dut == DUT[6] or dut == DUT[7]:
            dailyActive = getClientAPPAveDailyActive(dut.lower())
        else:
            dailyActive = getAveDailyActive(dut)
        stab = round(1-crashUser/dailyActive, 5)
        wb[v.SHEET1].cell(row=dutX, column=newY).value = crashCount
        wb[v.SHEET1].cell(row=dutX+1, column=newY).value = crashUser
        wb[v.SHEET1].cell(row=dutX+2, column=newY).value = dailyActive
        wb[v.SHEET1].cell(row=dutX+3, column=newY).value = stab
    wb.save(v.FILE_NAME)


if __name__ == '__main__':
    ProcessSheet1Xlsx()