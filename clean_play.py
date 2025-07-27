import random

# Colors
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'

# Success Message
def sukses(no1, pro, nam):
    print("     %s[%s%s%s] [%s Sent %s] %sSuccess, mulai %s from %s%s %ssended" %
          (pu, ku, no1, pu, hi, pu, pu, pro, ku, nam, hi))

# Failed Message
def gagal(no1, pro, nam):
    print("     %s[%s%s%s] [%s Failed  %s] %sFailed, mulai %s from %s%s %snot sended" %
          (pu, ku, no1, pu, me, pu, pu, pro, ku, nam, me))

# Dummy spam functions (you can replace with actual APIs)
def asakita(): fake("Asakita")
def nutriclub(): fake("Nutriclub")
def sunchila(): fake("Sunchila")
def asani(): fake("Asani")
def wintershop(): fake("Wintershop")
def datesy(): fake("Datesy")
def thaifriendly(): fake("ThaiFriendly")
def jumpstart(): fake("Jumpstart")
def kinimart(): fake("Kinimart")
def klikwa(): fake("Klikwa")
def bakmikeraton(): fake("BakmiKeraton")
def kopidulukala(): fake("KopiDuluKala")
def kredinesia(): fake("Kredinesia")
def pinjamindo(): fake("PinjamIndo")
def uangpintar(): fake("UangPintar")
def danafix(): fake("DanaFix")
def maucash(): fake("Maucash")
def omamoriexpress(): fake("OmamoriExpress")
def ktakilat(): fake("KtaKilat")
def cairin(): fake("Cairin")
def kredito(): fake("Kredito")
def kreditpedia(): fake("Kreditpedia")
def bocil(): fake("Bocil")
def duitqu(): fake("DuitQu")
def primacash(): fake("PrimaCash")
def temanprima(): fake("TemanPrima")
def maripinjam(): fake("MariPinjam")
def sobatbangun(): fake("SobatBangun")

def fake(name):
    no = random.randint(100, 999)
    if random.choice([True, False]):
        sukses(no, "SPAM", name)
    else:
        gagal(no, "SPAM", name)

# Logo Function
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

# Main Function
def main():
    logo()
    try:
        nom = input(f"{ku}Enter Target Number (e.g., 812XXXXXXX): {pu}")
        jum = int(input(f"{ku}How many times to spam?: {pu}"))
    except:
        print(f"{me}Invalid input. Exiting.")
        return

    print("%s[%s!%s] %sTarget locked >> %s%s" % (pu, me, pu, pu, ku, "+62" + nom))

    for t in range(1, jum + 1):
        print("%s[%s+%s]------------------------>>> [%s%s%s] <<<------------------------[%s+%s]" %
              (pu, ku, pu, me, t, pu, ku, pu))
        asakita()
        sunchila()
        nutriclub()
        asani()
        wintershop()
        datesy()
        thaifriendly()
        jumpstart()
        kinimart()
        klikwa()
        bakmikeraton()
        kopidulukala()
        kredinesia()
        pinjamindo()
        uangpintar()
        danafix()
        maucash()
        omamoriexpress()
        ktakilat()
        cairin()
        kredito()
        kreditpedia()
        bocil()
        duitqu()
        primacash()
        temanprima()
        maripinjam()
        sobatbangun()

# Most important line
if __name__ == "__main__":
    main()
