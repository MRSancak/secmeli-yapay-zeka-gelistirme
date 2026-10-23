import json
import os

index = 1
dosya = "kisiler.json"

kisiler = json.load(open(dosya, encoding="utf-8")) if os.path.exists(dosya) else []

while True:
    secim = input("\n1-Ekle  2-Listele  3-Çıkış: ")

    if secim == "1":
        kisiler.append({
            "Numara": index,
            "yaş": int(input("Yaş: ")),
            "isim": input("İsim: "),
            "soyisim": input("Soyisim: ")
        })

        index += 1

        with open(dosya, "w", encoding="utf-8") as f:
            json.dump(kisiler, f, ensure_ascii=False, indent=4)

    elif secim == "2":
        print(*kisiler, sep="\n")

    elif secim == "3":
        break
