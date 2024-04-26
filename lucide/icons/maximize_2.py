from .. import IconBase


class IconMaximize2(IconBase):
    class_name = "lucide lucide-maximize-2"
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
            "polyline": {
                "points": "15 3 21 3 21 9"
            }
        },
        {
            "polyline": {
                "points": "9 21 3 21 3 15"
            }
        },
        {
            "line": {
                "x1": "21",
                "x2": "14",
                "y1": "3",
                "y2": "10"
            }
        },
        {
            "line": {
                "x1": "3",
                "x2": "10",
                "y1": "21",
                "y2": "14"
            }
        }
    ]
}
