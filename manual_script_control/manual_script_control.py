import sys


class ManualScriptControl:
    @staticmethod
    def wait_for_user_input(massage="Просто ждем"):
        while True:
            user_input = input(massage + "\nРучное действие выполнено? (введите 'y' для ПРОДОЛЖЕНИЯ ВЫПОЛНЕНИЯ СКРИПТА "
                               "или 'n' для ЗАВЕРШЕНИЯ СКРИПТА): ").lower()
            if user_input == 'y':
                print("Продолжаем выполнение скрипта...")
                break
            elif user_input == 'n':
                print("Скрипт завершает выполнение...")
                sys.exit()
            else:
                print("Пожалуйста, введите 'y' или 'n'.")