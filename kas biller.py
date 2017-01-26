#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kas biller.py
#  
#  Copyright 2016 MS Rikas <msrikas@outlook.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 


# Header and Insructions of The Program
welcome = open("welcome.txt","r")
print(welcome.read())

# View The Database
def db():
    db = open("mydb.txt","r")
    print(db.read())

# Billing Function Call
def start():
    
    # Time Module
    import time

    # Initial Variables and Values
    total = 0.0
    price = 0.0
    income = 0.0

    # Getting Date in to variable 'date'
    date = time.strftime("%x")

    # Database To Save Sales Entries
    file = open("mydb.txt","a")
    file.write("\n")
    file.write(str(date))
    file.write("\n")
    file.close()

    print("\n/////////////////////////////////////////////////")
    print("\n|            Good Luck To Your Sales            |")
    print("\n/////////////////////////////////////////////////\n\n")

    # Main Program To Billing
    while (price != ''):
        price = float(input("Product Price: "))
        total += price
        print ("Balance: Rs",total)
        income += price

        # This is set of coding to end a sale and submit sale summary to database	
        if (price == 0):
            file = open("mydb.txt","a")
            file.write("\nSingle Sale Summary : Rs ")
            file.write(str(total))
            file.write("\n")
            file.close()
            print("Total Due is: Rs",total,"\n\n ** Above Billing is Completed & New Billing is Started **\n")
            total = 0.0

        # This is set of coding to end all sales and submit total sales of the day summary to db
        if (price == 0.1):
            print ("\n**********************************************")
            print("\nToday's Total Sale : Rs",income-0.1)
            print ("\nThank You For Using KAS Automated Billing System\n")
            print ("**********************************************")
            income -= 7
            file = open("mydb.txt","a")
            file.write("\nToday's Total Sale : Rs ")
            file.write(str(income+6.99))
            file.write("\n*******************************************\n")
            file.close()
            break
