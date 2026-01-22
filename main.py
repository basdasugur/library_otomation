# Kütüphane Yönetimi v1.1 (Refactored)

kitap_listesi = []

print("---" * 15)
print("📚 KÜTÜPHANE SİSTEMİ")

while True:
    print("\n" + "---" * 15)
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Listele")
    print("4. Temizle")
    print("q. Çıkış")

    secim = input("Seçiminiz: ").strip().lower()

    if secim == "q":
        print("Çıkış yapılıyor. İyi okumalar!")
        break

    elif secim == "1":
        # BUG FIX: Boş girişi engelleme kontrolü
        yeni_kitap = input("Kitap Adı: ").strip().capitalize()
        if yeni_kitap == "":
            print("❌ Hata: Kitap adı boş olamaz!")
        else:
            kitap_listesi.append(yeni_kitap)
            print(f"✅ '{yeni_kitap}' rafa eklendi.")

    elif secim == "2":
        silinecek_kitap = input("Silinecek Kitap: ").strip().capitalize()
        # Güvenli Silme
        if silinecek_kitap in kitap_listesi:
            kitap_listesi.remove(silinecek_kitap)
            print(f"🗑️ '{silinecek_kitap}' silindi.")
        else:
            print("⚠️ Hata: Bu kitap zaten listede yok.")

    elif secim == "3":
        # Pythonic boş liste kontrolü
        if not kitap_listesi:
            print("📂 Raf şu an boş.")
        else:
            print("\n--- MEVCUT KİTAPLAR ---")
            # UX FIX: Saymaya 1'den başla (start=1)
            for i, kitap in enumerate(kitap_listesi, start=1):
                print(f"{i}. {kitap}")

    elif secim == "4":
        kitap_listesi.clear()
        print("🧹 Tüm raflar temizlendi.")

    else:
        print("⚠️ Hatalı seçim yaptınız, tekrar deneyin.")
