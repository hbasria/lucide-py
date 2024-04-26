from .. import IconBase


class IconJoystick(IconBase):
    class_name = "lucide lucide-joystick"
    svg_data = {
    "attrs": {
        "width": "24",
        "height": "24",
        "view_box": "0 0 24 24",
        "fill": "none",
        "stroke": "currentColor",
        "stroke_width": "2",
        "stroke_linecap": "round",
        "stroke_linejoin": "round"
    },
    "items": [
        {
            "path": {
                "d": "M21 17a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-2Z"
            }
        },
        {
            "path": {
                "d": "M6 15v-2"
            }
        },
        {
            "path": {
                "d": "M12 15V9"
            }
        },
        {
            "circle": {
                "cx": "12",
                "cy": "6",
                "r": "3"
            }
        }
    ]
}
