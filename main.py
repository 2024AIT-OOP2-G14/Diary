from diaries.DiarySample import DiarySample
from diaries.ShibataDiary import ShibataDiary

# ↓のリストには、メンバーの各日記が格納されます。
from diaries.takumiDiary import takumiDiary

# ↓のリストには、メンバーの各日記が格納されます。
from diaries.kurokawaDiary import kurokawaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           ShibataDiary(),
           takumiDiary(),
    kurokawaDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
