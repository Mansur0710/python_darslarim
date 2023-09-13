# savol = input("savol: ")
# if savol.find("kitob")>0 or savol.find("kutubxona") >0:
#     savol = input("sizga qanday kitoblar yoqadi: ")
#     if savol.find("detektiv")>=0:
#       savol = input("Shaytanat kitobi haqidagi fikringgiz: ")
#       print("yaxshi");
#     elif savol.find("diniy")>=0:
#       print("Sizga hadis va hayot nomli kitobni sovg'a qilamiz");
# elif savol.find("sport")>=0:
#     savol = input("siz qaysi sport turiga qiziqasiz: ")
#     if savol.find("futboll")>=0:
#       savol = input("siz qaysi komandani yoqtirasiz: ")
#       if savol.find("real")>=0 or savol.find("barsa")>=0:
#          print("Siz elkilassikoga chipta sovg'a qilamiz");
#       else:
#          print("Siz elkilassikoga chipta sovg'a qilamiz");

# soni=int(input('nechta eng yaqin do\'sting bor:'))
# dostlar=[]
# for i in range(1,soni+1):
#     son=input(f"{i}-do'stim:")
#     dostlar.append(son)
# print(dostlar)

#
# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.


# num=input("num...")
# sum=0
# for i in num:
#     sum+=int(i)
# print(sum)


# n = int(input("N xonali sonni kiriting: "))  # Foydalanuvchi kiritgan sonni o'qiymiz
# total = 0
# while n > 0:
#     total += n % 10  # Sonning eng oxirgi raqamini qo'shamiz
#     n //= 10  # Sonni eng oxirgi raqamini olib tashlaymiz
#
# print("Raqamlari yig'indisi:", total)


# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')


# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")


# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")


# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = True # mijoz salat olmadi
#
# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz
# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz


# ///////////////////
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh!")


