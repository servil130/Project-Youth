# ==============================================================================
# PROJECT YOUTH - DEBUG AUTO-SKIP SYSTEM
# ==============================================================================
# Mode debugging: Skip otomatis seluruh dialog & animasi, dan otomatis
# memilih pilihan pertama (opsi 1) pada setiap menu pertanyaan sampai akhir Week 9.

default debug_auto_skip = False

init python:
    class ToggleDebugAutoSkip(Action):
        """
        Action tombol Skip sebagai alat debugging:
        - Mengaktifkan fast-skipping tanpa henti (termasuk teks belum terbaca).
        - Mengaktifkan auto-choice (selalu memilih opsi 1 pada setiap pertanyaan).
        - Otomatis berhenti di akhir Week 9 atau saat tombol ditekan kembali.
        """
        def __call__(self):
            if store.debug_auto_skip:
                store.debug_auto_skip = False
                config.skipping = None
                renpy.notify("Debug Auto-Skip: OFF")
            else:
                store.debug_auto_skip = True
                _preferences.skip_unseen = True
                _preferences.skip_after_choices = True
                config.skipping = "fast"
                renpy.notify("Debug Auto-Skip: AKTIF (Auto-pilih opsi 1 s/d akhir Week 9)")
            renpy.restart_interaction()

        def get_selected(self):
            return bool(getattr(store, "debug_auto_skip", False))

        def get_sensitive(self):
            return not getattr(store, "main_menu", False)

    def get_first_valid_choice(items):
        """Mengambil aksi pilihan pertama yang valid dan aktif."""
        if not items:
            return None
        for i in items:
            if hasattr(i.action, "get_sensitive"):
                if i.action.get_sensitive():
                    return i.action
            else:
                return i.action
        return items[0].action

    def _debug_auto_skip_start_interact():
        """Callback setiap awal interaksi untuk menjaga kontinuitas fast-skipping."""
        if getattr(store, "debug_auto_skip", False):
            if getattr(store, "main_menu", False):
                store.debug_auto_skip = False
                config.skipping = None
                return

            _preferences.skip_unseen = True
            _preferences.skip_after_choices = True
            if not config.skipping:
                config.skipping = "fast"

    config.start_interact_callbacks.append(_debug_auto_skip_start_interact)


