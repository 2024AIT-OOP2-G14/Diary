from diaries.DiarySample import DiarySample
from diaries.ShibataDiary import ShibataDiary
from diaries.takumiDiary import takumiDiary
from diaries.kurokawaDiary import kurokawaDiary
from diaries.HiyoshiDiary import HiyoshiDiary
from diaries.SatoDiary import SatoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           ShibataDiary(),
           takumiDiary(),
           kurokawaDiary(),
           SatoDiary(),
           HiyoshiDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
