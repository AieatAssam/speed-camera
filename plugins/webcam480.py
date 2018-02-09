# ---------------- User Configuration Settings for speed-cam.py ---------------------------------
#         Ver 8.0 speed-cam.py webcam480 Stream Variable Configuration Settings

#######################################
#    speed-cam.py plugin settings
#######################################

# Calibration Settings
# --------------------
cal_obj_px = 180       # Length of a calibration object in pixels
cal_obj_mm = 4330.0    # Length of the calibration object in millimetres

# Crop Area for motion detection Tracking
# ---------------------------------------
x_left  = 150          # Exclude event if x less than this px position Default=25
x_right = 490          # Exclude event if x greater than this px position Default=295
y_upper = 140          # Exclude event if y less that this value default=100
y_lower = 340          # Exclude event if y greater than this value default=175

# Motion Event Settings
# ---------------------
track_len_trig = 75    # Default=75 Length of track to trigger speed photo
track_timeout = 0.0    # Default=0.0 Optional seconds to wait after track End (Avoid dual tracking)
event_timeout = 0.3    # Default=0.3 seconds to wait for next motion event before starting new track

# Camera Settings
# ---------------
WEBCAM = True        # default = False False=PiCamera True=USB WebCamera

# Web Camera Settings
WEBCAM_SRC = 0        # default = 0   USB opencv connection number
WEBCAM_WIDTH = 640    # default = 640 USB Webcam Image width
WEBCAM_HEIGHT = 480   # default = 480 USB Webcam Image height

# Camera Image Settings
# ---------------------
image_font_size = 15          # Default = 15 Font text height in px for text on images
image_bigger = 1.5            # Default = 1.5 Resize saved speed image by value

# Motion Event Exclusion Settings
# -------------------------------
MIN_AREA = 170         # Exclude all contours less than or equal to this sq-px Area
x_diff_min = 1         # Exclude if min px away exceeds last event x pos
x_diff_max = 50        # Exclude if max px away for last motion event x pos

# ---------------------------------------------- End of User Variables -----------------------------------------------------
