## ============================================================================
## CASHIER MINIGAME  (Rhythm Heaven style)
##
## How to play : the cashier auto-scans items (listen) -> then the player
##               repeats the rhythm with SPACE / click as items cross the scanner.
## Called with : call cashier_minigame   (via label part_time_shift)
## ============================================================================

## Chart: (beat, who)   "a" = auto cashier (listen)   "p" = player's turn
## The first beat must be >= 4 because beats 0-3 are the count-in.
define CASHIER_BPM = 100
define CASHIER_CHART = [
    # Phrase 1: steady pattern
    (4, "a"), (5, "a"), (6, "a"), (7, "a"),
    (8, "p"), (9, "p"), (10, "p"), (11, "p"),
    # Phrase 2: fast items (half beats)
    (12, "a"), (13, "a"), (13.5, "a"), (14, "a"),
    (16, "p"), (17, "p"), (17.5, "p"), (18, "p"),
    # Phrase 3: syncopation
    (20, "a"), (20.5, "a"), (21.5, "a"), (22, "a"),
    (24, "p"), (24.5, "p"), (25.5, "p"), (26, "p"),
]

init -1 python:
    import time
    import math

    # Separate channels so beeps don't cut off other sfx
    renpy.music.register_channel("scan", mixer="sfx", loop=False)
    renpy.music.register_channel("tick", mixer="sfx", loop=False)

    class BeatGame(object):
        # --- settings you can tweak ------------------------------------------
        PERFECT = 0.07          # seconds, PERFECT tolerance
        GOOD = 0.15             # seconds, GOOD tolerance
        SPEED = 520.0           # conveyor speed (px/second)
        SCAN_X = 520            # scanner x position
        BELT_Y = 740            # conveyor surface y position
        OFFSET = 0.0            # shifts the whole chart (seconds). If hits feel
                                # late/early even when you're on beat, change this
                                # (e.g. 0.05 / -0.05)
        MUSIC = "audio/bgm/cashier.ogg"
        SCAN_SFX = "audio/sfx/ui_click.wav"     # replace with a scanner beep
        TICK_SFX = "audio/sfx/ui_hover.wav"     # metronome if the song is missing
        MISS_SFX = "audio/sfx/ui_back.wav"
        # Items: put PNGs in game/images/cashier/item_1.png, item_2.png, ... (max 8)
        # If missing, colored boxes are used as placeholders.
        # ---------------------------------------------------------------------

        def __init__(self, bpm, chart):
            self.spb = 60.0 / bpm
            self.targets = [b * self.spb + self.OFFSET for b, w in chart]
            self.who = [w for b, w in chart]
            n = len(chart)
            self.state = [None] * n     # None / "auto" / "perfect" / "good" / "miss"
            self.at = [0.0] * n         # time the item was judged (for animation)
            self.score = 0
            self.combo = 0
            self.best_combo = 0
            self.max_score = 100 * self.who.count("p")
            self.flash_t = -9.0
            self.judge = None
            self.judge_t = -9.0
            self.ticked = -1
            self.t0 = None
            self.has_music = renpy.loadable(self.MUSIC)

            colors = ["#e63946", "#f4a261", "#2a9d8f", "#457b9d", "#e9c46a", "#9b5de5", "#06d6a0", "#ef476f"]
            self.imgs = []
            for k in range(8):
                path = "images/cashier/item_%d.png" % (k + 1)
                if renpy.loadable(path):
                    self.imgs.append(renpy.displayable(path))
                else:
                    self.imgs.append(Solid(colors[k], xysize=(110, 110)))

        # --- time ------------------------------------------------------------
        def start(self):
            if self.has_music:
                renpy.music.play(self.MUSIC, channel="music", loop=False)
            self.t0 = time.perf_counter()

        def now(self):
            if self.t0 is None:
                return 0.0
            return time.perf_counter() - self.t0

        def finished(self):
            return self.t0 is not None and self.now() > self.targets[-1] + 1.5

        def percent(self):
            if self.max_score == 0:
                return 0.0
            return float(self.score) / self.max_score

        # --- input -----------------------------------------------------------
        def hit(self):
            if self.t0 is None:
                return
            n = self.now()
            best, diff = None, 999.0
            for i, t in enumerate(self.targets):
                if self.state[i] is None and self.who[i] == "p":
                    d = abs(t - n)
                    if d < diff:
                        best, diff = i, d
            if best is None or diff > self.GOOD:
                renpy.sound.play(self.MISS_SFX, channel="scan")   # pressed off-beat
                return
            if diff <= self.PERFECT:
                self.state[best] = "perfect"
                self.score += 100
            else:
                self.state[best] = "good"
                self.score += 50
            self.at[best] = n
            self.combo += 1
            self.best_combo = max(self.best_combo, self.combo)
            self.judge, self.judge_t = self.state[best], n
            self.scan_fx(n)

        def scan_fx(self, n):
            self.flash_t = n
            renpy.sound.play(self.SCAN_SFX, channel="scan")

        # --- called every frame ----------------------------------------------
        def update(self):
            n = self.now()
            # metronome if there is no song yet
            if not self.has_music:
                b = int(n / self.spb)
                if b > self.ticked:
                    self.ticked = b
                    renpy.sound.play(self.TICK_SFX, channel="tick")
            for i, t in enumerate(self.targets):
                if self.state[i] is not None:
                    continue
                if self.who[i] == "a":
                    if n >= t:                         # auto cashier scans
                        self.state[i] = "auto"
                        self.at[i] = n
                        self.scan_fx(n)
                elif n - t > self.GOOD:                # player too late -> miss
                    self.state[i] = "miss"
                    self.at[i] = n
                    self.combo = 0
                    self.judge, self.judge_t = "miss", n

        def phase_text(self, n):
            if n < 4 * self.spb:
                return ["Ready?", "3", "2", "1"][int(n / self.spb)]
            for i in range(len(self.state)):
                if self.state[i] is None:
                    return "Watch..." if self.who[i] == "a" else "Your turn!"
            return ""

    def cashier_outlined(txt, size, color, **kw):
        return Text(txt, size=size, color=color, outlines=[(3, "#000000", 0, 0)], **kw)

    def cashier_draw(st, at):
        g = store.cashier_g
        g.update()
        n = g.now()
        f = renpy.display.layout.Fixed()

        # --- conveyor + moving stripes ---------------------------------------
        f.add(Transform(Solid("#1d1d2bdd", xysize=(1920, 170)), xpos=0, ypos=g.BELT_Y))
        shift = (n * g.SPEED) % 160
        for k in range(14):
            f.add(Transform(Solid("#ffffff22", xysize=(80, 8)),
                            xpos=int(k * 160 - shift), ypos=g.BELT_Y + 80))

        # --- items -------------------------------------------------------------
        for i, t in enumerate(g.targets):
            x = g.SCAN_X + (t - n) * g.SPEED
            if not (-200 < x < 2050):
                continue
            s = g.state[i]
            hop = 0
            if s in ("auto", "perfect", "good"):
                dt = n - g.at[i]
                if dt < 0.22:
                    hop = int(70 * math.sin(math.pi * dt / 0.22))
            alpha = 0.45 if s in ("auto", "perfect", "good") else 1.0
            y = g.BELT_Y + 5 - hop
            f.add(Transform(g.imgs[i % len(g.imgs)], xpos=int(x), ypos=y,
                            xanchor=0.5, yanchor=1.0, alpha=alpha))
            if g.who[i] == "p" and s is None:          # marker: this one is yours
                f.add(Transform(Solid("#ffd23f", xysize=(26, 26)),
                                xpos=int(x), ypos=g.BELT_Y - 150, xanchor=0.5))
            if s == "miss":
                f.add(Transform(cashier_outlined("X", 60, "#ff4d4d"),
                                xpos=int(x), ypos=g.BELT_Y - 170, xanchor=0.5))

        # --- scanner -----------------------------------------------------------
        f.add(Transform(Solid("#33334a", xysize=(26, 280)),
                        xpos=g.SCAN_X, ypos=g.BELT_Y - 270, xanchor=0.5))
        f.add(Transform(Solid("#ff3355", xysize=(6, 270)),
                        xpos=g.SCAN_X, ypos=g.BELT_Y - 265, xanchor=0.5, alpha=0.35))
        fd = n - g.flash_t
        if fd < 0.15:
            a = 1.0 - fd / 0.15
            f.add(Transform(Solid("#ff3355", xysize=(90, 270)),
                            xpos=g.SCAN_X, ypos=g.BELT_Y - 265, xanchor=0.5, alpha=0.5 * a))

        # --- judgement text ----------------------------------------------------
        jd = n - g.judge_t
        if g.judge and jd < 0.55:
            label, col = {"perfect": ("Perfect!", "#ffe066"),
                          "good": ("Good", "#8ce99a"),
                          "miss": ("Miss", "#ff6b6b")}[g.judge]
            f.add(Transform(cashier_outlined(label, 64, col),
                            xpos=g.SCAN_X, ypos=int(g.BELT_Y - 330 - 40 * jd),
                            xanchor=0.5, alpha=max(0.0, 1.0 - jd / 0.55)))

        # --- HUD ---------------------------------------------------------------
        f.add(cashier_outlined("Score %d" % g.score, 44, "#ffffff", xpos=420, ypos=24))
        f.add(cashier_outlined("Combo %d" % g.combo, 44, "#ffffff", xpos=720, ypos=24))
        f.add(Transform(cashier_outlined(g.phase_text(n), 84, "#ffffff"), xalign=0.5, ypos=130))
        total = g.targets[-1] + 1.5
        f.add(Transform(Solid("#ffffff88", xysize=(int(1920 * min(1.0, n / total)), 6)), xpos=0, ypos=0))
        return f, 0     # 0 = redraw every frame (smooth)

    def cashier_tick():
        # Ends the "call screen" interaction when the chart is finished
        if store.cashier_g.finished():
            return True


## --- Intro screen: START button ----------------------------------------------
screen cashier_intro():
    modal True
    key "game_menu" action NullAction()
    add Solid("#000000bb")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 36
        text "INDOAPRIL CASHIER" size 84 xalign 0.5 color "#ffffff" outlines [(3, "#000000", 0, 0)]
        text "Watch the cashier scan the items, then repeat the rhythm.\nPress {b}SPACE{/b} or {b}click{/b} when an item {b}marked in yellow{/b} crosses the scanner.":
            size 34
            xalign 0.5
            text_align 0.5
            color "#ffffff"
        text "Tip: the scanner beep IS the beat. Listen first, then match it." size 28 xalign 0.5 color "#ffd23f"
        textbutton "START":
            xalign 0.5
            text_size 72
            text_color "#ffffff"
            text_hover_color "#ffd23f"
            action Return(True)


## --- Gameplay screen -----------------------------------------------------------
screen cashier_screen():
    modal True
    key "game_menu" action NullAction()      # block Esc pause (the timer keeps running)
    key "K_SPACE" action Function(cashier_g.hit, _update_screens=False)
    key "mousedown_1" action Function(cashier_g.hit, _update_screens=False)
    add DynamicDisplayable(cashier_draw)
    timer 0.1 repeat True action Function(cashier_tick, _update_screens=False)


## --- Main flow -------------------------------------------------------------------
label cashier_minigame:
    $ _rollback = False
    $ quick_menu = False                     # hide affection / week HUD during the minigame

    call screen cashier_intro                # wait for the player to press START

    $ cashier_g = BeatGame(CASHIER_BPM, CASHIER_CHART)
    $ cashier_g.start()                      # song + timer start NOW
    call screen cashier_screen

    stop music fadeout 1.0
    $ quick_menu = True
    $ _rollback = True

    $ pct = cashier_g.percent()
    if pct >= 0.85:
        $ rating = "Superb!"
    elif pct >= 0.6:
        $ rating = "OK"
    else:
        $ rating = "Try Again"
    $ tip = (cashier_g.score // 10) * 100
    $ player_money += tip
    $ tip_text = "{:,}".format(tip)

    scene black with dissolve
    n "Shift over! Your rating: [rating]"
    n "Best combo: [cashier_g.best_combo]. You earned Rp[tip_text] in tips."
    return
