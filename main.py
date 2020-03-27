from os import system, name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass


def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def intro():
    clear()
    print("The")
    print("   .g8" "8q.                                       ")
    print(".dP'    `YM.                                     ")
    print('dM\'      `MM `7MM  `7MM  ,pW"Wq.`7Mb,od8 ,6"Yb.  ')
    print("MM        MM   MM    MM 6W'   `Wb MM' \"'8)   MM  ")
    print("MM.      ,MP   MM    MM 8M     M8 MM     ,pm9MM  ")
    print("`Mb.    ,dP'   MM    MM YA.   ,A9 MM    8M   MM  ")
    print('  `"bmmd"\'     `Mbod"YML.`Ybmd9\'.JMML.  `Moo9^Yo.')
    print("       MMb                                        ")
    print("        R0b0tZ!")
    print("              Automatic Question Writer!\n")
    print("Automatically Ask your Question on Quora with one button!")
    print("* This application Does NOT store any data.")
    sleep(3)
    clear()


def instructions():
    print("This uses Facebook Authencation (SSO) to Sign on to Quora.")
    sleep(1)
    print(
        "If you have 2-Step Authencation turned on with Facebook, you would need to Allow the sesion for this to work."
    )
    sleep(3)
    clear()


def automation():
    print("Facebook Login")
    user_name = input("Email or Phone:")
    password = getpass.getpass()

    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    element = driver.find_element_by_id("email")
    element.send_keys(user_name)

    element = driver.find_element_by_id("pass")
    try:
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
    except:
        print("User/Password not accepted, User/Password might be wrong.")
    else:
        print("Inserted User & Password!")

    sleep(20)

    try:
        driver.get("https://www.quora.com")
    except:
        print("Can't Go to Quora. Quora might be Down.")
    else:
        print("Going to Quora!")

    sleep(5)

    Question_button = driver.find_elements_by_xpath(
        '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/div[2]'
    )[0]
    Question_button.click()
    sleep(3)
    with open("Question.txt", "r") as f:
        lines = f.readlines()
        inputElement = driver.find_element_by_xpath(
            '//textarea[@placeholder = \'Start your question with "What", "How", "Why", etc.\']'
        )
        try:
            inputElement.send_keys(lines)
            inputElement.send_keys(Keys.RETURN)
        except:
            print("Question not asked. Something Broke.")
        else:
            print("Question Asked!")
    sleep(1)

    sleep(7)
    driver.close()


def main():
    intro()
    instructions()
    automation()


if __name__ == "__main__":
    main()
