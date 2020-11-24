import covid
import pyttsx3
import speech_recognition as sr
import json

covid = covid.Covid(source="john_hopkins")
engine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as src:
	print("Say country name or if you want global cases, say global cases.")
	engine.say("Say country name or if you want global cases, say global cases.")
	engine.runAndWait()
	userInp = r.recognize_google(r.listen(src))

if userInp.lower() == "global cases":
	print(f"{'{:,}'.format(covid.get_total_confirmed_cases())} confirmed cases")
	engine.say(f"{'{:,}'.format(covid.get_total_confirmed_cases())} confirmed cases")
	engine.runAndWait()

	print(f"{'{:,}'.format(covid.get_total_deaths())} deaths")
	engine.say(f"{'{:,}'.format(covid.get_total_deaths())} deaths")
	engine.runAndWait()

	print(f"{'{:,}'.format(covid.get_total_recovered())} recoveries")
	engine.say(f"{'{:,}'.format(covid.get_total_recovered())} recoveries")
	engine.runAndWait()
else:
	data = covid.get_status_by_country_name(userInp)

	print(f"{'{:,}'.format(data['confirmed'])} confirmed cases")
	engine.say(f"{'{:,}'.format(data['confirmed'])} confirmed cases")
	engine.runAndWait()

	print(f"{'{:,}'.format(data['deaths'])} deaths")
	engine.say(f"{'{:,}'.format(data['deaths'])} deaths")
	engine.runAndWait()

	print(f"{'{:,}'.format(data['recovered'])} recoveries")
	engine.say(f"{'{:,}'.format(data['recovered'])} recoveries")
	engine.runAndWait()
