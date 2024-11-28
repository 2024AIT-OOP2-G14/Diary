from diaries.AbstractDiary import AbstractDiary
class SatoDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
            return """今日は課題のしわよせのせいで寝不足の状態で授業に出席することになった。
        物理実験のレポート作成が今日になるまでに終わらず空いた時間を見つけて取り組んでいるが
        まだ終わっていない。
        今日はバイトもあるため早く物理実験レポートを終わらしたい。
        """
        
    def get_author(self):
        return "Sato"