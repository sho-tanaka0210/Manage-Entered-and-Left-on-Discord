class PostDay():
    def __init__(self, times_of_day, day_of_week):
        """
        Constructor of a class to set the time of regular posting.
        定期投稿の時刻を設定するクラスのコンストラクタ

        Parameters
        ----------
        times_of_day : string
            Time to post
            投稿する時刻

        day_of_week : DayOfWeek
            Day of the week to post
            投稿する曜日
        """
        self.times_of_day = times_of_day
        self.day_of_week = day_of_week

    def __eq__(self, other):
        if not isinstance(other, PostDay):
            return False
        return ((self.times_of_day == other.times_of_day) and
                (self.day_of_week == other.day_of_week))

    def __hash__(self):
        return hash((frozenset(self.times_of_day), frozenset(self.day_of_week)))
