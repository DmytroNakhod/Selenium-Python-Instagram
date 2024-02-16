from config import Config
from selenium.common.exceptions import TimeoutException


def execute_tasks():
    try:
        with Config() as bot:
            bot.land_tempmail_page()
            bot.get_element_copy_button()
            bot.appy_registration()
            bot.close_alert_popup()
            bot.click_on_email()
            bot.copy_past_code_from_email()
            input("Press enter to finish")

    except TimeoutException as e:
        print(f"Error: Timeout Open Login Page: {e}")


if __name__ == "__main__":
    execute_tasks()
