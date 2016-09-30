#coding=utf8
from __future__ import division
from openpyxl import Workbook, load_workbook
from openpyxl.cell import column_index_from_string

from api import *
import var as v

def processSheet1Xlsx():
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
        if dut == DUT[-1] or dut == DUT[-2]:
            dailyActive = getClientAPPAveDailyActive(dut)
        else:
            dailyActive = getAveDailyActive(dut)
        stab = round(1-crashUser/dailyActive, 5)

        wb[v.SHEET1].cell(row=dutX, column=newY).value = crashCount
        wb[v.SHEET1].cell(row=dutX+1, column=newY).value = crashUser
        wb[v.SHEET1].cell(row=dutX+2, column=newY).value = dailyActive
        wb[v.SHEET1].cell(row=dutX+3, column=newY).value = stab
    wb.save(v.FILE_NAME)


def processSheet2Xlsx():
    DUT = ["R1CM", "R1D", "R2D", "R1CL", "R3", "R3L", "Android", "iOS"]
    SUBTYPE = ["CrashLog次数", "CrashLog用户数"]
    try:
        wb = load_workbook(v.FILE_NAME)
    except:
        print "specific file is not exist"
        return
    for cell in wb[v.SHEET2].get_cell_collection():
        if cell.value == "new":
            _ = cell.row
            newY = column_index_from_string(cell.column)
            break
    for dut in DUT:
        for cell in wb[v.SHEET2].get_cell_collection():
            if cell.value == dut:
                dutX = cell.row
                _ = column_index_from_string(cell.column)
                break
        if dut == DUT[-1] or dut == DUT[-2]:
            specVersion, dailyActive = getClientAPPVersionMostUsedDaily(dut)
        else:
            specVersion, dailyActive = getVersionMostUsedDailyActive(dut)
        crashCount = getSpecVersionKernelCrashAveDaily(dut, specVersion, SUBTYPE[0])
        crashUser = getSpecVersionKernelCrashAveDaily(dut, specVersion, SUBTYPE[1])
        stab = round(1-crashUser/dailyActive, 5)

        wb[v.SHEET2].cell(row=dutX, column=newY).value = specVersion
        wb[v.SHEET2].cell(row=dutX+1, column=newY).value = crashCount
        wb[v.SHEET2].cell(row=dutX+2, column=newY).value = crashUser
        wb[v.SHEET2].cell(row=dutX+3, column=newY).value = dailyActive
        wb[v.SHEET2].cell(row=dutX+4, column=newY).value = stab
    wb.save(v.FILE_NAME)


def processSheet3Xlsx():
    DUT = ["R1CM", "R1D", "R2D", "R3"]
    try:
        wb = load_workbook(v.FILE_NAME)
    except:
        print "specific file is not exist"
        return
    for dut in DUT:
        for cell in wb[v.SHEET3].get_cell_collection():
            if cell.value == dut:
                dutX = cell.row
                dutY = column_index_from_string(cell.column)
                break
        specVersion, dailyActive = getVersionMostUsedDailyActive(dut)
        crashTop10 = getSpecVersionDaemonCrashUserCountTop10Daily(dut, specVersion)
        for daemon in crashTop10:
            dutX = dutX + 1
            wb[v.SHEET3].cell(row=dutX, column=dutY).value = daemon[0] # 2.12.3-trafficd|11
            wb[v.SHEET3].cell(row=dutX, column=dutY+1).value = daemon[1] # count
            wb[v.SHEET3].cell(row=dutX, column=dutY+2).value = round(daemon[1]/dailyActive, 5)
    wb.save(v.FILE_NAME)

if __name__ == '__main__':
    processSheet1Xlsx()
    processSheet2Xlsx()
    processSheet3Xlsx()