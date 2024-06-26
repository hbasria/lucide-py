from .. import IconBase


class IconSquareScissors(IconBase):
    class_name = "lucide lucide-square-scissors"
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
                "height": "20",
                "x": "2",
                "y": "2",
                "rx": "2"
            }
        },
        {
            "circle": {
                "cx": "8",
                "cy": "8",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "M9.414 9.414 12 12"
            }
        },
        {
            "path": {
                "d": "M14.8 14.8 18 18"
            }
        },
        {
            "circle": {
                "cx": "8",
                "cy": "16",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "m18 6-8.586 8.586"
            }
        }
    ]
}
