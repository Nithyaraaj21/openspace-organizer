# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:38:22 2024

@author: nithy
"""

from openpyxl import Workbook
def create_workbook(path):
        workbook = Workbook()
        sheet = workbook.active
        sheet["A1"] = "Name"
        sheet["A2"] = "Jean Duffy"
        sheet["A3"] = "Sebastiaan Indesteege"
        sheet["A4"] = "Sahar-Mahmoudi"
        sheet["A5"] = "Sam Borms"
        sheet["A6"] = "Mark Shevchenko"
        sheet["A7"] = "Archana Singh"
        sheet["A8"] = "Luca"
        sheet["A9"] = "obohatov"
        sheet["A10"] = "Polina.Ya"
        sheet["A11"] = "Leyla DD"
        sheet["A12"] = "Julio Barizon"
        sheet["A13"] = "Jaggar YusseF"
        sheet["A14"] = "Audrey Audeha"
        sheet["A15"] = "Sisekelo KeloSise"
        sheet["A16"] = "KUGALUR PALANISAMY Nithyaraaj"
        sheet["A17"] = "Sylvain"
        sheet["A18"] = "Maarten Knaepen"
        sheet["A19"] = "Philippe Montel"
        sheet["A20"] = "Audrey Audeha"
        sheet["A21"] = "Jyoti Sharma513"
        sheet["A22"] = "Hazem Eldabaa"
        sheet["A23"] = "ME Coban"
        sheet["A24"] = "paatch woork"
        sheet["A25"] = "Mahak Behl"
        sheet["A26"] = "Nithi2"
        sheet["A27"] = "paatch woork"
        sheet["A28"] = "Mahak Behl"
        sheet["A29"] = "Nithi2"
        
create_workbook("colleagues.xlsx")