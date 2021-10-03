import os
import json
import asyncio





def getweather():
	os.system("weather yerevan am -o Files/weather.json")
	f=open("Files/weather.json")
	data = json.load(f)
	day = ""
	for i in data['forecasts']:
			if i[0:15] == data['date'][0:15]:
				day = i
	today = data['forecasts'][day]
	def td(today):
		types = {"Mostly Sunny":"🌤 Հիմնականում արևոտ 🌤","Mostly Clear":"☀️ Հիմնականում պարզ ☀️","Partly Cloudy":"⛅️ Ամպամած ⛅️"}
		try:
			text = types[today['sky text']]
		except:
			text=today['sky text']
		return text


	


	text=f"""
	🌍 Եղանակը Երևանում Հիմա 🌍

	🌡 Եղանակը հիմա {data['temperature']} է 🌡


	🌍 Սպասվող Եղանակը Երևանում 🌍

	Այսօր եղանակը {td(today)}   է

	🌡 Առավելագույն ջերմաստիճանը   {today['highest temperature']} է 
	🌡 Նվազագույն ջերմաստիճանը   {today['lowest temperature']} է 
	💨 Քամու արագությունը {data['wind speeds']} է
	💧 Օդի խոնավությունը {data['humidity']} է
	

	🌍 Մանրամասն տեսնելու համար մուտք գործեք այստեղ 🌍

	{data['url']} 
	"""
	returning = text
	return returning