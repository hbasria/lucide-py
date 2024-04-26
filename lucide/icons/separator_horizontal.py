from .. import IconBase


class IconSeparatorHorizontal(IconBase):
    class_name = "lucide lucide-separator-horizontal"
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
            "line": {
                "x1": "3",
                "x2": "21",
                "y1": "12",
                "y2": "12"
            }
        },
        {
            "polyline": {
                "points": "8 8 12 4 16 8"
            }
        },
        {
            "polyline": {
                "points": "16 16 12 20 8 16"
            }
        }
    ]
}
