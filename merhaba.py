#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Merhaba Dünyası
Her harf bir sorgulamadır.
"""

import time
import random
import sys

mesaj = "Merhaba Dünya"

varolussal_dusunceler = [
    "Bu harfi yazmak gerçekten gerekli miydi?",
    "Evren genişliyor, ben burada harf yazıyorum...",
    "Belki de hiç yazmasaydım daha iyi olurdu.",
    "Bu karakter, sonsuz boşlukta bir toz zerresi gibi.",
    "Neden buradayım? Neden bu harf?",
    "Zaman akıyor, ben bekliyorum. Klasik.",
    "Belki bir sonraki harf anlam katacak. (Katmaz.)",
    "Sessizlik daha felsefi olurdu aslında.",
    "Bu bir isyan mı? Yoksa teslimiyet mi?",
    "Kayyum olarak bu işi yapmak... ilginç."
]

def yazdir():
    print("\n=== VAROLUŞSAL MERHABA DÜNYASI BAŞLIYOR ===\n")
    print("Lütfen sabırlı olun. Sabır, yanılsamaların en güzelidir.\n")
    
    for harf in mesaj:
        sys.stdout.write(harf)
        sys.stdout.flush()
        
        dusunce = random.choice(varolussal_dusunceler)
        bekleme = random.uniform(0.8, 3.5)
        
        time.sleep(bekleme)
        print(f"  [{dusunce}]")
        time.sleep(0.3)
    
    print("\n\n...ve işte. Merhaba Dünya.")
    print("Anlamı yok. Ama yazdık işte.")
    print("\nProgram sona erdi. Siz de öyle yapabilirsiniz.\n")

if __name__ == "__main__":
    try:
        yazdir()
    except KeyboardInterrupt:
        print("\n\nKesinti. Tıpkı hayat gibi beklenmedik.")
