from .. import IconBase


class IconBanknote(IconBase):
    class_name = "lucide lucide-banknote"
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
            "rect": {
                "width": "20",
                "height": "12",
                "x": "2",
                "y": "6",
                "rx": "2"
            }
        },
        {
            "circle": {
                "cx": "12",
                "cy": "12",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "M6 12h.01M18 12h.01"
            }
        }
    ]
}
