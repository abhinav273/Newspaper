# importing the pyttsx library
import pyttsx3
import requests
import json
import datetime as dt

def speak(str,n):
    # initialisation
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')           #Voice Changing
    engine.setProperty('voice', voices[n].id)
    # To Speak
    engine.say(str)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to our News Channel.\n")
    speak("Welcome to our News Channel.",0)
    print("Enter the name of the file you want to save your news in\n")
    speak("Enter the name of the file you want to save your news in!",0)
    file_name = input()
    file_name += ".txt"
    file = open(file_name,"a")
    i = 0
    while True:
        print("Enter Which category of news you want to hear.\n    Press:\n    1 - Mix\n    2 - Business\n    3 - Entertainment\n    4 - Health\n    5 - Science\n    6 - Sports\n    7 - Technology\n    0 - Exit\n")
        speak("Enter Which category of news you want to hear.",0)
        speak("Press 1 for Mix News, 2 for Business related news, 3 for Entertainment related news, 4 for Health related news, 5 for Science related news, 6 for Sports related news, 7 for Technology related news, and 0 to exit",0)
        try:
            inp2 = int(input())
        except:
            print("Enter a Valid Choice.\n")
            speak("Enter a Valid Choice.",0)
            continue
        if inp2 != 0:
            print("How many news you want to hear\n")
            speak("How many news you want to hear",0)
            try:
                n = int(input())
            except:
                n = 3
        if n > 10:
            n = 10
        url_mix = "https://newsapi.org/v2/top-headlines?country=in&apiKey=cbadf5db2b1146ab8a21324754b56ae7"
        url_bus = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cbadf5db2b1146ab8a21324754b56ae7"
        url_ent = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cbadf5db2b1146ab8a21324754b56ae7"
        url_health = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cbadf5db2b1146ab8a21324754b56ae7"
        url_sci = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cbadf5db2b1146ab8a21324754b56ae7"
        url_sports = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cbadf5db2b1146ab8a21324754b56ae7"
        url_tech = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cbadf5db2b1146ab8a21324754b56ae7"
        if inp2 == 1:
            file.write(f"{dt.datetime.now()}: Mix News\n\n")
            news = requests.get(url_mix).text
            print("Mix news begins\n")
            speak("Mix news begins",0)
        elif inp2 == 2:
            file.write(f"{dt.datetime.now()}: Business News\n")
            news = requests.get(url_bus).text
            print("Business related news begins\n")
            speak("Business related news begins",0)
        elif inp2 == 3:
            file.write(f"{dt.datetime.now()}: Entertainment News\n")
            news = requests.get(url_ent).text
            print("Entertainment related news begins\n")
            speak("Entertainment related news begins",0)
        elif inp2 == 4:
            file.write(f"{dt.datetime.now()}: Health News\n")
            news = requests.get(url_health).text
            print("Health related news begins\n")
            speak("Health related news begins",0)
        elif inp2 == 5:
            file.write(f"{dt.datetime.now()}: Science News\n")
            news = requests.get(url_sci).text
            print("Science related news begins\n")
            speak("Science related news begins",0)
        elif inp2 == 6:
            file.write(f"{dt.datetime.now()}: Sports News\n")
            news = requests.get(url_sports).text
            print("Sports related news begins\n")
            speak("Sports related news begins",0)
        elif inp2 == 7:
            file.write(f"{dt.datetime.now()}: Technology News\n")
            news = requests.get(url_tech).text
            print("Technology related news begins\n")
            speak("Technology related news begins",0)
        elif inp2 == 0:
            print("Thank you!\n")
            speak("Thank you!",0)
            break
        else:
            print("Enter a Valid Choice.\n")
            speak("Enter a Valid Choice.",0)

        news_j = json.loads(news)["articles"]
        count = 0
        for article in news_j:
            count += 1
            file.write(f"{count}. {article['title']}:    {article['description']}\n\n")
            print(article["title"])
            speak(article["title"],0)
            print("\nIf you want to hear complete news\nEnter 'yes'\nEnter anything to go to next news\n")
            speak("If you want to hear complete news. Enter 'yes'. Enter anything to go to next news.",0)
            inp1 = input()
            if inp1 == 'yes':
                if article["description"] != None:
                    print(article["description"])
                    speak(article["description"],0)
                else:
                    print("Not Available")
                    speak("Not Available",0)
            if count == n:
                print("Thank you!\n")
                speak("Thank you!",0)
                file.write("\n\n\n")
                break
            print("\nNext News is coming\n")
            speak("Next News is coming",0)
