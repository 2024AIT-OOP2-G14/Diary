from diaries.DiarySample import DiarySample
from diaries.takumiDiary import takumiDiary

# ↓のリストには、メンバーの各日記が格納されます。
from diaries.kurokawaDiary import kurokawaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           takumiDiary(),
    kurokawaDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
