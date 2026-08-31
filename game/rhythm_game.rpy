init python:
    import time

    class RhythmNote:
        def __init__(self, key, hit_time, lane):
            self.key = key
            self.hit_time = hit_time
            self.lane = lane
            self.judged = False
            self.result = None

    class RhythmGame:
        def __init__(self, chart, song_length):
            self.chart = chart
            self.song_length = song_length
            self.start_time = None
            self.score = 0
            self.combo = 0

        def start(self):
            self.start_time = time.time()

        def get_elapsed(self):
            if self.start_time is None:
                return 0
            return time.time() - self.start_time

        def try_hit(self, key):
            elapsed = self.get_elapsed()
            best_note = None
            best_diff = 999

            for note in self.chart:
                if note.judged or note.key != key:
                    continue
                diff = abs(note.hit_time - elapsed)
                if diff < best_diff:
                    best_diff = diff
                    best_note = note

            if best_note is None:
                return None

            if best_diff <= 0.08:
                result = "perfect"
                self.score += 100
                self.combo += 1
            elif best_diff <= 0.18:
                result = "good"
                self.score += 50
                self.combo += 1
            else:
                return None

            best_note.judged = True
            best_note.result = result
            return result

        def check_misses(self):
            elapsed = self.get_elapsed()
            for note in self.chart:
                if not note.judged and elapsed - note.hit_time > 0.2:
                    note.judged = True
                    note.result = "miss"
                    self.combo = 0

# Chart pakai lane D, F, J, K (urutan umum di rhythm game 4-key)
default rg_chart = [
    RhythmNote("d", 1.0, 0),
    RhythmNote("f", 1.5, 1),
    RhythmNote("j", 2.0, 2),
    RhythmNote("k", 2.5, 3),
    RhythmNote("d", 3.0, 0),
    RhythmNote("j", 3.5, 2),
]

default rg = RhythmGame(rg_chart, song_length=5.0)


screen rhythm_screen():
    modal True
    zorder 100

    key "d" action Function(rg.try_hit, "d")
    key "f" action Function(rg.try_hit, "f")
    key "j" action Function(rg.try_hit, "j")
    key "k" action Function(rg.try_hit, "k")

    timer 0.05 repeat True action Function(rg.check_misses)

    for note in rg.chart:
        if not note.judged:
            $ time_until_hit = note.hit_time - rg.get_elapsed()
            $ travel_time = 1.5
            $ progress = 1.0 - (time_until_hit / travel_time)
            if 0 <= progress <= 1.2:
                frame:
                    xpos (200 + note.lane * 150)
                    ypos int(progress * 600)
                    xsize 100
                    ysize 50
                    background "#0ff"

    frame:
        xpos 200
        ypos 600
        xsize 550
        ysize 10
        background "#fff"

    text "Score: [rg.score]" xpos 20 ypos 20 size 30
    text "Combo: [rg.combo]" xpos 20 ypos 60 size 30


label rhythm_minigame:
    $ rg.start()
    show screen rhythm_screen
    pause 5.0
    hide screen rhythm_screen
    "Final score: [rg.score]"
    return