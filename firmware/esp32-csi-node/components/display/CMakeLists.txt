set(SRCS "display_hal.c" "display_task.c" "display_ui.c")

# This component is only included if DISPLAY_ENABLE is y
idf_component_register(
    SRCS ${SRCS}
    INCLUDE_DIRS "."
    PRIV_REQUIRES esp_lcd esp_lcd_touch lvgl
)
