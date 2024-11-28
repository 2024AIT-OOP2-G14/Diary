from diaries.AbstractDiary import AbstractDiary

class AtamaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "寝不足で睡魔と戦った1日だった"

    def get_author(self):
        return "Atama"