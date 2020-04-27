import tabula
import smtplib, ssl

c = []; plant_c = []; animal_c = []
p = []; plant_p = []; animal_p = []
l = []; plant_l = []; animal_l = []
Check_lines = []
Check_properties = []

def app(cc,pp,ll): c.append(cc); p.append(pp);l.append(ll)
def plant_app(cc,pp,ll): plant_c.append(cc); plant_p.append(pp); plant_l.append(ll)
def animal_app(cc,pp,ll):animal_c.append(cc);animal_p.append(pp); animal_l.append(ll)

df = tabula.read_pdf("kviitung.pdf")
tabula.convert_into("kviitung.pdf", "kviitung.txt", output_format="txt")

f = open("kviitung.txt", "r")
for line in f:
    line = line.rstrip('\n')
    Check_lines.append(line)
f.close()

Check_line0 = Check_lines[0].split(",")
Check_properties.append(Check_line0)
Check_lines.pop(0)



x = len(Check_lines)
ln = 1

while ln != x:
    Check_line = Check_lines[ln].split(',"')
    Check_properties.append(Check_line)
    ln += 1

ln = 1

print(Check_properties)

# packed Check_properties[ln][0].find("") == 0:
# weighted Check_properties[ln] == "":

while ln != x:
    if Check_properties[ln][0].find("Paprika mix") == 0:
        amount = float(Check_properties[ln][0][-1]) * 5
        cc = 4.1*amount;pp = 1*amount;ll = 0.2*amount;app(cc,pp,ll); plant_app(cc,pp,ll)
        ln += 1
        #https://tka.nutridata.ee/et/toidud/1950
    elif Check_properties[ln][0].find("Kirsskobartomat") == 0:
        amount = float(Check_properties[ln][0][-1]) * 5
        cc = 3.5*amount;pp = 0.3*amount;ll = 0.6*amount;app(cc,pp,ll); plant_app(cc,pp,ll)
        ln += 1
        #https://tka.nutridata.ee/et/toidud/907
    elif Check_properties[ln][0] == "Mais värske":
        amount = round(float(Check_properties[ln][1][:-1].replace(",",".")) * 10,2)
        cc = 17*amount;pp = 3.4*amount;ll = 1.8*amount;app(cc,pp,ll); plant_app(cc,pp,ll)
        ln += 1
        #https://tka.nutridata.ee/et/toidud/516
    elif Check_properties[ln][0].find("Mango Ready to Eat") == 0:
        amount = float(Check_properties[ln][0][-1]) * 4.7
        cc = 12.4*amount;pp = 0.6*amount;ll = 0.45*amount;app(cc,pp,ll); plant_app(cc,pp,ll)
        ln += 1
        #https://tka.nutridata.ee/et/toidud/543
    elif Check_properties[ln][0] == "Lõhe liblikfilee":
        amount = round(float(Check_properties[ln][1][:-1].replace(",",".")) * 10,2)
        cc = 0*amount;pp = 20*amount;ll = 16*amount;app(cc,pp,ll); animal_app(cc,pp,ll)
        ln += 1
        #https://tka.nutridata.ee/et/toidud/1932
    elif Check_properties[ln][0] == "Forellimari":
        amount = round(float(Check_properties[ln][1][:-1].replace(",",".")) * 10,2)
        cc = 4*amount;pp = 24.6*amount;ll = 17.9*amount;app(cc,pp,ll); animal_app(cc,pp,ll)
        ln += 1
        #https://tka.nutridata.ee/et/toidud/3343
    elif Check_properties[ln][0] == "Brolerifilee":
        amount = round(float(Check_properties[ln][1][:-1].replace(",",".")) * 10,2)
        cc = 4*amount;pp = 24.6*amount;ll = 17.9*amount;app(cc,pp,ll); animal_app(cc,pp,ll)
        ln += 1
    elif Check_properties[ln][0].find("Öko Saaremaa mahej") == 0:
        amount = float(Check_properties[ln][0][-1]) * 3
        cc = 0*amount;pp = 25*amount;ll = 28*amount;app(cc,pp,ll); animal_app(cc,pp,ll)
        ln += 1
        #https://www.selver.ee/et/oko-saaremaa-mahejuust-viilud-saaremaa-150-g
    elif Check_properties[ln][0].find("Täistera Tortilla") == 0:
        amount = float(Check_properties[ln][0][-1]) * 2.45
        cc = 46.3*amount;pp = 9.3*amount;ll = 46.3*amount;app(cc,pp,ll); plant_app(cc,pp,ll)
        ln += 1
        #https://www.selver.ee/et/taistera-tortillad-4-tk-poco-loco-245-g
    elif Check_properties[ln][0].find("Hautatud oad") == 0:
        print("Yes")
        amount = float(Check_properties[ln][0][-1]) * 4
        cc = 11.2*amount;pp = 7.6*amount;ll = 1.3*amount;app(cc,pp,ll); plant_app(cc,pp,ll)
        ln += 1
        #https://www.selver.ee/et/hautatud-oad-tomatikastmes-organic-food-400-g

total = round(sum(c))+round(sum(p))+round(sum(l))
print(total)

cn = round(round(sum(c))/total * 100) #Carbohydrates %
pn = round(round(sum(p))/total * 100) #Proteins %
fn = round(round(sum(l))/total * 100) #Fats %

plant_cn = round(round(sum(plant_c))/sum(c) * 100)
plant_pn = round(round(sum(plant_p))/sum(p) * 100)
plant_fn = round(round(sum(plant_l))/sum(l) * 100)

plant_total = round((plant_cn+plant_pn+plant_fn)/3)
animal_total = 100 - plant_total

animal_cn = 100 - plant_cn
animal_pn = 100 - plant_pn
animal_fn = 100 - plant_fn

if cn < 65 or cn > 45 and pn < 35 or pn > 10 and fn < 35 or fn > 20:
    macro_result = "Your shopping card macronutrients are well-balanced"
else:
    macro_result = "Your shopping card macronutrients' balance needs improvement"
if plant_total != 100:
    origin_result = "Your shopping card plant-animal food balance needs improvement"
else:
    origin_result = "Your shopping card plant-animal food is well-balanced"

print(macro_result)
print(origin_result)

sender_email = "nutribyestonia@gmail.com"
receiver_email = input("Type your email")

message = """Subject: Your shopping cart nutrition review

Hi, 
{} 
{}
Best wishes,
NutriBy"""

port = 465  # For SSL
password = ""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("nutribyestonia@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message.format(macro_result,origin_result))
