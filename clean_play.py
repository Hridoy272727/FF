import random

# Colors
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'

def sukses(no1, pro, nam):
    print("     %s[%s%s%s] [%s Sent %s] %sSuccess, mulai %s from %s%s %ssended" % (
        pu, ku, no1, pu, hi, pu, pu, pro, ku, nam, hi))

def gagal(no1, pro, nam):
    print("     %s[%s%s%s] [%s Failed  %s] %sFailed, mulai %s from %s%s %snot sended" % (
        pu, ku, no1, pu, me, pu, pu, pro, ku, nam, me))

def fake_api_call(name):
    no = random.randint(100, 999)
    success = random.choice([True, False])
    if success:
        sukses(no, "SPAM", name)
    else:
        gagal(no, "SPAM", name)

def logo():
    print(f"""{qu}
  _________                    _________
 |   _____/                   |   _____/
 |   |_____ ________________  |   |______ __ _________
 |    ___| ' __|  ___|  ___|  |    ___|  |  '__|  ___|
 |   |   |  |  |  __|   __|   |   |   |  |  |  |  __|
 |___|   |__|  |_____|_____|  |___|   |__|__|  |_____|

 {pu}Author  : {ku}Tokicoy{qu}
 {pu}Github  : {ku}Nothing{qu}
 {pu}Youtube : {ku}Acinakongames

 {qu}Tools Demo Use ID Free Fire
""")

def main():
    logo()
    try:
        target = input(f"{ku}Enter Target Number (e.g., 812XXXXXXX): {pu}")
        count = int(input(f"{ku}How many times to spam?: {pu}"))
    except:
        print(f"{me}Invalid input. Exiting.{pu}")
        return

    print("%s[%s!%s] %sTarget locked >> %s%s" % (pu, me, pu, pu, ku, "+62" + target))

    for i in range(count):
        print("%s[%s+%s]------------------------>>> [%s%s%s] <<<------------------------[%s+%s]" %
              (pu, ku, pu, me, i+1, pu, ku, pu))
        fake_api_call("asakita")
        fake_api_call("nutriclub")
        fake_api_call("thaifriendly")

# ✅ This line is most important:
if __name__ == "__main__":
    main()
