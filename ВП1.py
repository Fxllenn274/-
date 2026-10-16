# zad 1
# a = float(input())
# discount = 2
# disc1 = a + (a*(discount/100))
# disc2 = disc1 + (disc1*(discount/100))
# print(f"{disc2:.2f}")

#zad 2
# kmav = float(input())
# kmtaxi = float(input())
# priceav = float(input())
# pricetaxi = float(input())
# totalkm = kmav + kmtaxi
# totalprice = (kmav*priceav) + (kmtaxi+pricetaxi)
# print (f"Total km: {totalkm:.2f}, Total price {totalprice:.2f}")



#zad 3
# hours = float(input())
# hwage = float(input())
# pb = float(input())
# pu = float(input())
# zaplata = hours * hwage
# zaplata += zaplata * (pb/100)
# zaplata += zaplata * (pu/100)



#zad 4
# sthrana = float(input())
# stnapitki = float(input())
# tax = float(input())
# brhora = float(input())
# obshtasmetka = sthrana + stnapitki
# obshtasmetka += obshtasmetka*(tax/100)
# sumPerPerson = obshtasmetka / brhora
# print(f"Total {obshtasmetka:.2f} Per person: {sumPerPerson:.2f}")


#zad 5
# a = float(input())
# b = float(input())
# h = float(input())
# v = a * b * h
# s = 2 * ((a*b)+(a*h)+(b*h))
# print(f"V = {v:.2f},  S = {s:.2f}")



#zad 6
# liters1 = float(input())
# price1 = float(input())
# liters2 = float(input())
# price2 = float(input())
# avgprice=(price1 + price2)/2
# totalLiters = liters1 + liters2
# print(f"Total: {totalLiters:.2f}L  Avg price: {avgprice:.2f}")

# zad 7
# distance = float(input())
# avgspeed = float(input())
# rest = float(input())
# time = (distance/avgspeed) +rest
# timeH = time/60
# print(f"Total time:{timeH:.2f} hours")

#zad 8
# length = float(input())
# width = float(input())
# height = float(input())
# windows_doors = float(input())
# coverage = float(input())
# price = float(input())
# area = 2 * (length * height + width * height) - windows_doors
# liters = area / coverage
# total_price = liters * price
# print(f"{liters:.2f}")
# print(f"{total_price:.2f}")

#zad 9
# grade1 = float(input())
# weight1 = float(input())
# grade2 = float(input())
# weight2 = float(input())
# grade3 = float(input())
# weight3 = float(input())
# average = (grade1 * weight1 + grade2 * weight2 + grade3 * weight3) / 100
# print(f"{average:.2f}")

#zad 10
# nachalnasuma = float(input())
# lihva = float(input())
# years = float(input())
# krainasuma = nachalnasuma
# i = 1
# while (i<=years):
#     krainasuma+= krainasuma*(lihva/100)
#     i+=1

# promqna = krainasuma - nachalnasuma
# print(f"Natrupana suma: {promqna:.2f}")
# print(f"Kraina suma = {krainasuma:.2f}")



#zad 11
# timesec = float(input())
# hours = timesec // 3600
# minutes = timesec // 60
# secondsleft = timesec % 3600
# print(f"hours: {hours:.2f} minutes: {minutes:.2f}  seconds left: {secondsleft:.2f}")

#zad 12
# import math
# length = float(input())
# width = float(input())
# tilearea = float(input())
# reserve = float(input())
# tileprice = float(input())
# floorarea = length * width
# neededtiles = math.ceil(floorarea * (1 + reserve / 100) / tilearea)
# totalprice = neededtiles * tileprice
# print(neededtiles)
# print(f"{totalprice:.2f}")

#zad 13 
# moshtnost = float(input())
# dailyhours = float(input())
# days = float(input())
# price = float(input())
# totalhours = days*dailyhours
# kW = (moshtnost * totalhours)/1000
# totalprice = kW * price
# print(f"Total power used: {kW:.2f}kWh, total price: {totalprice:.2f}")

#zad 14
# distance1 = float(input())
# speed1 = float(input())
# distance2 = float(input())
# speed2 = float(input())
# totaldistance = distance1 + distance2
# time1 = distance1 / speed1
# time2 = distance2 / speed2
# totaltime = time1 + time2
# averagespeed = totaldistance / totaltime
# print(f"{totaltime:.2f}")
# print(f"{averagespeed:.2f}")


#zad 15
# broiproducts = float(input())
# pricePerOne = float(input())
# dostavna = float(input())
# razhodi = float(input())
# prihod = broiproducts * pricePerOne
# razhod = (dostavna*broiproducts) + razhodi
# pechalba = prihod - razhod
# print(f"Income is: {prihod:.2f}")
# print(f"Expenses are: {razhod:.2f}")
# if (pechalba<0):
#     print(f"The loss is: {(pechalba*-1):.2f}")

# else:
#     print(f"The profit is: {pechalba:.2f}")
