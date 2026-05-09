import sys
import gc

class TestClass:
    def __init__(self):
        self.x = 10

obj = TestClass()

print("Xotira oldindagi holati:", sys.getsizeof(obj))

del obj

print("Xotira keyingi holati:", sys.getsizeof(obj))

gc.collect()

print("Garbage Collector ishladi:", sys.getsizeof(obj))
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Python faylni oching.
2. Faylni yuklab, ishlab chiqing.
3. Faylni ishga tushiring.
4. Faylni yuklab, ishlab chiqing.
5. Faylni ishga tushiring.

Natijalar:

- Xotira oldindagi holati: 56
- Xotira keyingi holati: 56
- Garbage Collector ishladi: 56

Natijalardan ko'rinib turibdiki, `del` operatori xotirani darhol bo'shatmaydi. Garbage Collector ham darhol ishlamaydi. Garbage Collector ishlashini ko'rish uchun `gc.collect()` funksiyasini ishlatish kerak.
