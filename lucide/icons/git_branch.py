from .. import IconBase


class IconGitBranch(IconBase):
    class_name = "lucide lucide-git-branch"
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
                "x1": "6",
                "x2": "6",
                "y1": "3",
                "y2": "15"
            }
        },
        {
            "circle": {
                "cx": "18",
                "cy": "6",
                "r": "3"
            }
        },
        {
            "circle": {
                "cx": "6",
                "cy": "18",
                "r": "3"
            }
        },
        {
            "path": {
                "d": "M18 9a9 9 0 0 1-9 9"
            }
        }
    ]
}
