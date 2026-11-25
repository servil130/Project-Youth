init python:
    import time

    class BeatGame(object):
        PERFECT = 0.07
        GOOD = 0.15

        def __init__(self, bpm, beats, offset=0.0):
            self.spb = 60.0 / bpm
            self.targets = [b * self.spb + offset for b in beats]
            self.judged = [None] * len(beats)
            self.score = 0
            self.combo = 0
            self.t0 = time.perf_counter()

        def now(self):
            return time.perf_counter() - self.t0

        def hit(self):
            n = self.now()
            best, diff = None, 999
            for i, t in enumerate(self.targets):
                if self.judged[i] is None and abs(t - n) < diff:
                    best, diff = i, abs(t - n)
            if best is None or diff > self.GOOD:
                return
            if diff <= self.PERFECT:
                self.judged[best] = "perfect"; self.score += 100
            else:
                self.judged[best] = "good"; self.score += 50
            self.combo += 1
            renpy.sound.play("audio/sfx/ui_click.wav")   # ganti jadi beep scanner
            renpy.restart_interaction()

        def update(self):
            n = self.now()
            for i, t in enumerate(self.targets):
                if self.judged[i] is None and n - t > self.GOOD:
                    self.judged[i] = "miss"; self.combo = 0

        def finished(self):
            return self.now() > self.targets[-1] + 1.0

    def cashier_draw(st, at):
        g = store.cashier_g
        g.update()
        f = renpy.display.layout.Fixed()
        for i, t in enumerate(g.targets):
            if g.judged[i] is None:
                x = 600 + (t - g.now()) * 500        # 500 px/detik
                if -150 < x < 1950:
                    f.add(Transform("images/dot.png", xpos=int(x), ypos=600))
        return f, 0     # 0 = redraw tiap frame

screen cashier_screen():
    modal True
    key "K_SPACE" action Function(cashier_g.hit)
    key "mousedown_1" action Function(cashier_g.hit)
    add DynamicDisplayable(cashier_draw)
    add Solid("#fff", xsize=6, ysize=200, xpos=600, ypos=560)   # garis scanner
    text "Score: [cashier_g.score]   Combo: [cashier_g.combo]" xpos 20 ypos 20
    if cashier_g.finished():
        timer 0.01 action Return(cashier_g.score)

label cashier_minigame:
    $ _rollback = False
    $ cashier_g = BeatGame(bpm=100, beats=[4,5,6,7, 8,9,10,10.5,11, 12,13,14,15], offset=0.0)
    play music "audio/bgm/cashier.ogg" noloop
    call screen cashier_screen
    $ result = _return
    $ _rollback = True
    $ player_money += result // 10
    n "Shift selesai. Kamu dapat Rp[result // 10]00 dari tip!"
    return
