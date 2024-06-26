from .. import IconBase


class IconCrosshair(IconBase):
    class_name = "lucide lucide-crosshair"
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
            "circle": {
                "cx": "12",
                "cy": "12",
                "r": "10"
            }
        },
        {
            "line": {
                "x1": "22",
                "x2": "18",
                "y1": "12",
                "y2": "12"
            }
        },
        {
            "line": {
                "x1": "6",
                "x2": "2",
                "y1": "12",
                "y2": "12"
            }
        },
        {
            "line": {
                "x1": "12",
                "x2": "12",
                "y1": "6",
                "y2": "2"
            }
        },
        {
            "line": {
                "x1": "12",
                "x2": "12",
                "y1": "22",
                "y2": "18"
            }
        }
    ]
}
