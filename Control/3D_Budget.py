# archivo creado para generar mis estimaciones

#------------------DESIGN BASIS------------------

dbl_Print__Time=10*60 #minutos estimadas por cura
dbl_Print__weigth=68 #gramos estimados por cura
str_Material= "PLA"

#----------------- COSTS -----------------------

dbl_Printer__Consumption= 0.003125 #kW/min
dbl_Profit=0.1 #t.p.u
dbl_Electricity__Cost= 0.2 #euro/kWh
dbl_Power__Cost= 0.13 #euro/kW/dia
dbl_Power__Installed= 4.4 #kW

dbl_Printer__Cost= 600 #e
dbl_Printer__Availability= 365 #dia

dbl_Maintenance__weight=0.1 #t.p.u

dict_Material={"PLA":22,"PETG":25}

print(dict_Material[str_Material])

#----------------- MODEL -----------------------
dbl_Consumption=dbl_Printer__Consumption*dbl_Electricity__Cost #e/min
dbl_Power=dbl_Power__Installed*dbl_Power__Cost/(24*60)
dbl_Printer=dbl_Printer__Cost/dbl_Printer__Availability/(24*60) #e/min

dbl_Primary__Cost=(dbl_Consumption+dbl_Power+dbl_Printer)*dbl_Print__Time
dbl_Maintenance=dbl_Primary__Cost*dbl_Maintenance__weight

dbl_Material=dict_Material[str_Material]*dbl_Print__weigth/1000

dbl_abs__Profit=(dbl_Material+dbl_Primary__Cost+dbl_Maintenance)*dbl_Profit

dbl_Prize=(dbl_abs__Profit+dbl_Material+dbl_Primary__Cost+dbl_Maintenance)

print("Coste electrico: {} e/min".format(dbl_Consumption))
print("Coste electrico: {} e/h".format(dbl_Consumption*60))
print("Coste potencia: {} e/h".format(dbl_Power*60))
print("Coste amortizacion: {} e/h".format(dbl_Printer*60))

print("Coste horario: {} e/h".format(dbl_Primary__Cost/dbl_Print__Time*60))

print("Coste mantenimiento: {} e/h".format(dbl_Maintenance))
print("beneficio: {} e".format(dbl_abs__Profit))

print("El precio es: {} euros".format(round(dbl_Prize,2)))