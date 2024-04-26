from .. import IconBase


class IconDiscAlbum(IconBase):
    class_name = "lucide lucide-disc-album"
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
                "width": "18",
                "height": "18",
                "x": "3",
                "y": "3",
                "rx": "2"
            }
        },
        {
            "circle": {
                "cx": "12",
                "cy": "12",
                "r": "5"
            }
        },
        {
            "path": {
                "d": "M12 12h.01"
            }
        }
    ]
}
