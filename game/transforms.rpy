# ==============================================================================
# PROJECT YOUTH - TRANSFORMS & TRANSITIONS
# ==============================================================================

# Smooth move transitions (ease, easeinleft, easeoutleft, etc.)
init python:
    define.move_transitions("ease", 0.50, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)

# Stage position
transform tleft:
    xalign 0.15
    yalign 1.0

transform tcenter:
    xalign 0.5
    yalign 1.0

transform tright:
    xalign 0.85
    yalign 1.0

# Aliases for default Ren'Py positions to match DDLC / VN stage padding
transform left:
    xalign 0.15
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform right:
    xalign 0.85
    yalign 1.0

# Karakter slide dengan dynamic bounce
transform to_left:
    easein_back 0.50 xalign 0.15

transform to_center:
    easein_back 0.50 xalign 0.5

transform to_right:
    easein_back 0.50 xalign 0.85

# Versi slide halus
transform slide_left:
    easein 0.45 xalign 0.15

transform slide_center:
    easein 0.45 xalign 0.5

transform slide_right:
    easein 0.45 xalign 0.85

# Loncat / bounce ceria
transform hop:
    easein 0.15 yoffset -30
    easeout 0.18 yoffset 0

# Karakter menunduk saat malu / canggung
transform dip:
    easein 0.20 yoffset 25
    easeout 0.25 yoffset 0

# Gemetar / panik
transform panic:
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset 0

# lagi mikir
transform sway:
    transform_anchor True
    easein 0.22 rotate -3
    easeout 0.25 rotate 3
    easein 0.22 rotate 0
