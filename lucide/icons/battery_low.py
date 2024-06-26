from .. import IconBase


class IconBatteryLow(IconBase):
    class_name = "lucide lucide-battery-low"
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
                "width": "16",
                "height": "10",
                "x": "2",
                "y": "7",
                "rx": "2",
                "ry": "2"
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
                "x1": "6",
                "x2": "6",
                "y1": "11",
                "y2": "13"
            }
        }
    ]
}
