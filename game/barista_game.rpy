## ============================================================================
## BARISTA MINIGAME  (gaya chef / cooking-order game)
##
## Cara main : pelanggan memesan minuman -> pemain memasukkan bahan ke cangkir
##             (urutan bebas) -> tekan SERVE sebelum kesabaran pelanggan habis.
## Dipanggil : call barista_minigame   (lewat label part_time_shift)
## ============================================================================

init -1 python:
    import time

    # (nama minuman, bahan-bahannya)  -- urutan bahan bebas
    BARISTA_RECIPES = [
        ("Espresso",              ["espresso"]),
        ("Americano",             ["espresso", "water"]),
        ("Latte",                 ["espresso", "milk"]),
        ("Cappuccino",            ["espresso", "milk", "foam"]),
        ("Iced Palm Sugar Latte", ["espresso", "milk", "palm", "ice"]),
    ]
    BARISTA_LABELS = {"espresso": "Espresso", "water": "Water", "milk": "Milk",
                      "foam": "Foam", "palm": "Palm Sugar", "ice": "Ice"}
    # warna lapisan di dalam cangkir
    BARISTA_COLORS = {"espresso": "#3b2314", "water": "#9bd1f0", "milk": "#f5ebdc",
                      "foam": "#ffffff", "palm": "#c27a2c", "ice": "#d6f1ff"}
    # (id bahan, teks tombol, warna tombol)
    BARISTA_INGS = [
        ("espresso", "1  Espresso",   "#4a2c17"),
        ("water",    "2  Water",      "#2b7fb0"),
        ("milk",     "3  Milk",       "#8a7968"),
        ("foam",     "4  Foam",       "#6c757d"),
        ("palm",     "5  Palm Sugar", "#a0541b"),
        ("ice",      "6  Ice",        "#4f9bbd"),
    ]
    BARISTA_BOOK_LINES = ["%s: %s" % (name, " + ".join([BARISTA_LABELS[i] for i in rec]))
                          for name, rec in BARISTA_RECIPES]

    class BaristaGame(object):
        MAX_LAYERS = 6
        ADD_SFX = "audio/sfx/ui_click.wav"
        GOOD_SFX = "audio/glass_chime.wav"
        BAD_SFX = "audio/sfx/ui_back.wav"

        def __init__(self, n_orders=5):
            self.n = n_orders
            self.orders = []
            for i in range(n_orders):
                # pesanan makin sulit: 2 resep pertama dulu, lalu bertambah
                pool = BARISTA_RECIPES[:min(len(BARISTA_RECIPES), 2 + i)]
                self.orders.append(renpy.random.choice(pool))
            self.idx = 0
            self.cup = []
            self.score = 0
            self.served = 0
            self.msg = ""
            self.msg_good = True
            self.msg_t = -9.0
            self.patience = self.patience_for(0)
            self.t_order = None
            self.end_t = None

        # --- waktu -----------------------------------------------------------
        def patience_for(self, i):
            return max(14.0, 26.0 - 3.0 * i)       # detik, makin cepat tiap pelanggan

        def start(self):
            self.t_order = time.perf_counter()

        def remaining(self):
            if self.t_order is None:
                return self.patience
            return self.patience - (time.perf_counter() - self.t_order)

        def ratio(self):
            return max(0.0, min(1.0, self.remaining() / self.patience))

        def msg_visible(self):
            return bool(self.msg) and (time.perf_counter() - self.msg_t) < 1.6

        def say(self, text, good):
            self.msg, self.msg_good, self.msg_t = text, good, time.perf_counter()

        # --- status ----------------------------------------------------------
        def current(self):
            if self.idx < self.n:
                return self.orders[self.idx]
            return None

        def percent(self):
            return float(self.score) / (150 * self.n)

        # --- aksi pemain -----------------------------------------------------
        def add(self, ing):
            if self.current() is None or self.end_t is not None:
                return
            if len(self.cup) >= self.MAX_LAYERS:
                self.say("The cup is full!", False)
                return
            self.cup.append(ing)
            renpy.sound.play(self.ADD_SFX)

        def trash(self):
            if self.cup:
                self.cup = []
                renpy.sound.play(self.BAD_SFX)

        def serve(self):
            cur = self.current()
            if cur is None or not self.cup or self.end_t is not None:
                return
            name, recipe = cur
            if sorted(self.cup) == sorted(recipe):
                pts = 100 + int(50 * self.ratio())      # bonus kalau cepat
                self.score += pts
                self.served += 1
                self.say("Perfect! +%d" % pts, True)
                renpy.sound.play(self.GOOD_SFX)
            else:
                self.say("Wrong order...", False)
                renpy.sound.play(self.BAD_SFX)
            self.next_order()

        def next_order(self):
            self.cup = []
            self.idx += 1
            if self.idx >= self.n:
                self.end_t = time.perf_counter() + 1.3
            else:
                self.patience = self.patience_for(self.idx)
                self.t_order = time.perf_counter()

        def tick(self):
            if self.end_t is not None:
                if time.perf_counter() >= self.end_t:
                    return True                          # akhiri "call screen"
                return None
            if self.remaining() <= 0:
                self.say("The customer left!", False)
                renpy.sound.play(self.BAD_SFX)
                self.next_order()
            return None

    def barista_tick():
        return store.barista_g.tick()


## --- Layar pembuka: resep + tombol START ---------------------------------------
screen barista_intro():
    modal True
    key "game_menu" action NullAction()
    add Solid("#000000bb")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 28
        text "CAFE BARISTA" size 84 xalign 0.5 color "#ffffff" outlines [(3, "#000000", 0, 0)]
        text "Customers order drinks. Add the right ingredients to the cup, then press SERVE before they lose patience.":
            size 32
            xalign 0.5
            text_align 0.5
            color "#ffffff"
        text "RECIPE BOOK" size 36 xalign 0.5 color "#ffd23f"
        for line in BARISTA_BOOK_LINES:
            text line size 30 xalign 0.5 color "#ffffff"
        text "Keys: 1-6 add ingredients, Enter = serve, Backspace = trash cup." size 26 xalign 0.5 color "#cccccc"
        textbutton "START":
            xalign 0.5
            text_size 72
            text_color "#ffffff"
            text_hover_color "#ffd23f"
            action Return(True)


## --- Layar permainan -----------------------------------------------------------
screen barista_screen():
    modal True
    default show_book = True

    key "game_menu" action NullAction()
    key "1" action Function(barista_g.add, "espresso")
    key "2" action Function(barista_g.add, "water")
    key "3" action Function(barista_g.add, "milk")
    key "4" action Function(barista_g.add, "foam")
    key "5" action Function(barista_g.add, "palm")
    key "6" action Function(barista_g.add, "ice")
    key "K_RETURN" action Function(barista_g.serve)
    key "K_BACKSPACE" action Function(barista_g.trash)
    key "r" action ToggleScreenVariable("show_book")
    timer 0.1 repeat True action Function(barista_tick)

    add Solid("#00000055")

    $ cur = barista_g.current()
    $ score_label = "Score %d" % barista_g.score
    $ cup_text = " + ".join([BARISTA_LABELS[i] for i in barista_g.cup])
    if not cup_text:
        $ cup_text = "(empty cup)"

    text score_label size 48 xpos 60 ypos 30 color "#ffffff" outlines [(3, "#000000", 0, 0)]

    # --- tiket pesanan -------------------------------------------------------
    if cur:
        $ order_label = "ORDER %d / %d" % (barista_g.idx + 1, barista_g.n)
        $ r = barista_g.ratio()
        if r > 0.5:
            $ bar_col = "#6bd36b"
        elif r > 0.25:
            $ bar_col = "#ffd23f"
        else:
            $ bar_col = "#ff5555"

        fixed:
            xpos 80
            ypos 130
            xysize (560, 420)
            add Solid("#fff8e7")
            vbox:
                xalign 0.5
                ypos 24
                spacing 18
                text order_label size 34 xalign 0.5 color "#7a6a55"
                text "Customer wants:" size 36 xalign 0.5 color "#333333"
                text cur[0] size 56 xalign 0.5 color "#8a3b12" text_align 0.5
            text "Patience" size 28 xpos 40 ypos 300 color "#333333"
            add Solid("#00000033", xysize=(480, 28)) xpos 40 ypos 345
            add Solid(bar_col, xysize=(max(1, int(480 * r)), 28)) xpos 40 ypos 345

    # --- cangkir ---------------------------------------------------------------
    fixed:
        xpos 800
        ypos 150
        xysize (320, 440)
        add Solid("#ffffff22")
        for idx, ing in enumerate(barista_g.cup):
            add Solid(BARISTA_COLORS[ing], xysize=(280, 58)) xpos 20 ypos (410 - (idx + 1) * 60)
    text cup_text size 30 xpos 960 ypos 610 xanchor 0.5 color "#ffffff" outlines [(2, "#000000", 0, 0)]

    # --- buku resep ------------------------------------------------------------
    if show_book:
        frame:
            xpos 1260
            ypos 130
            xsize 600
            padding (28, 22)
            background Solid("#000000aa")
            vbox:
                spacing 12
                text "RECIPE BOOK" size 36 color "#ffd23f"
                for line in BARISTA_BOOK_LINES:
                    text line size 28 color "#ffffff"

    # --- pesan hasil -----------------------------------------------------------
    if barista_g.msg_visible():
        $ msg_col = "#8ce99a" if barista_g.msg_good else "#ff6b6b"
        text barista_g.msg size 64 xalign 0.5 ypos 40 color msg_col outlines [(3, "#000000", 0, 0)]

    # --- tombol bahan ----------------------------------------------------------
    hbox:
        xalign 0.5
        ypos 700
        spacing 20
        for ing, lbl, col in BARISTA_INGS:
            textbutton lbl:
                xysize (280, 120)
                background Solid(col)
                hover_foreground Solid("#ffffff33")
                text_size 38
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5
                action Function(barista_g.add, ing)

    # --- serve / trash / recipe ---------------------------------------------
    hbox:
        xalign 0.5
        ypos 860
        spacing 40
        textbutton "SERVE (Enter)":
            xysize (440, 110)
            background Solid("#2f9e44")
            hover_foreground Solid("#ffffff33")
            text_size 42
            text_color "#ffffff"
            text_xalign 0.5
            text_yalign 0.5
            action Function(barista_g.serve)
        textbutton "TRASH (Backspace)":
            xysize (440, 110)
            background Solid("#c92a2a")
            hover_foreground Solid("#ffffff33")
            text_size 42
            text_color "#ffffff"
            text_xalign 0.5
            text_yalign 0.5
            action Function(barista_g.trash)
        textbutton "RECIPE BOOK (R)":
            xysize (440, 110)
            background Solid("#495057")
            hover_foreground Solid("#ffffff33")
            text_size 42
            text_color "#ffffff"
            text_xalign 0.5
            text_yalign 0.5
            action ToggleScreenVariable("show_book")


## --- Alur utama ------------------------------------------------------------------
label barista_minigame:
    $ _rollback = False
    $ quick_menu = False                     # sembunyikan HUD affection / week

    call screen barista_intro                # tunggu pemain menekan START

    $ barista_g = BaristaGame(5)
    $ barista_g.start()
    call screen barista_screen

    $ quick_menu = True
    $ _rollback = True

    $ pct = barista_g.percent()
    if pct >= 0.85:
        $ rating = "Superb!"
    elif pct >= 0.6:
        $ rating = "OK"
    else:
        $ rating = "Try Again"
    $ tip = (barista_g.score // 10) * 100
    $ player_money += tip
    $ tip_text = "{:,}".format(tip)

    scene black with dissolve
    n "Shift over! Your rating: [rating]"
    n "You served [barista_g.served] of [barista_g.n] orders and earned Rp[tip_text] in tips."
    return
