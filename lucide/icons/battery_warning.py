from .. import IconBase


class IconBatteryWarning(IconBase):
    class_name = "lucide lucide-battery-warning"
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
                "d": "M14 7h2a2 2 0 0 1 2 2v6c0 1-1 2-2 2h-2"
            }
        },
        {
            "path": {
                "d": "M6 7H4a2 2 0 0 0-2 2v6c0 1 1 2 2 2h2"
            }
        },
        {
            "line": {
                "x1": "22",
                "x2": "22",
                "y1": "11",
                "y2": "13"
            }
        },
        {
            "line": {
                "x1": "10",
                "x2": "10",
                "y1": "7",
                "y2": "13"
            }
        },
        {
            "line": {
                "x1": "10",
                "x2": "10",
                "y1": "17",
                "y2": "17.01"
            }
        }
    ]
}
