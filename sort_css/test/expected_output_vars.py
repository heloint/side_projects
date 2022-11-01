EXPECTED_HTML_DICT = {
    "html": [
        {
            "attributes": {"lang": "en"},
            "head": [
                {
                    "meta": [
                        {"attributes": {"charset": "UTF-8"}},
                        {
                            "attributes": {
                                "http-equiv": "X-UA-Compatible",
                                "content": "IE=edge",
                            }
                        },
                        {
                            "attributes": {
                                "name": "viewport",
                                "content": "width=device-width, initial-scale=1.0",
                            }
                        },
                    ],
                    "link": [
                        {
                            "attributes": {
                                "rel": ["stylesheet"],
                                "href": "./css/style.css",
                            }
                        }
                    ],
                    "title": [{}],
                }
            ],
            "body": [
                {
                    "div": [
                        {
                            "attributes": {"class": ["banner-container"]},
                            "h3": [{"u": [{}]}],
                        },
                        {
                            "attributes": {"class": ["form-container"]},
                            "div": [
                                {
                                    "attributes": {"class": ["form-wrapper"]},
                                    "form": [
                                        {
                                            "attributes": {
                                                "action": "index.php",
                                                "method": "post",
                                                "enctype": "multipart/form-data",
                                            },
                                            "div": [
                                                {
                                                    "attributes": {
                                                        "class": ["upload-field"]
                                                    },
                                                    "label": [
                                                        {
                                                            "attributes": {
                                                                "for": "file"
                                                            },
                                                            "u": [{}],
                                                        }
                                                    ],
                                                    "input": [
                                                        {
                                                            "attributes": {
                                                                "type": "file",
                                                                "name": "file",
                                                            }
                                                        }
                                                    ],
                                                },
                                                {
                                                    "attributes": {
                                                        "class": ["submit-wrapper"]
                                                    },
                                                    "button": [
                                                        {
                                                            "attributes": {
                                                                "class": ["button"],
                                                                "type": "submit",
                                                                "name": "upload",
                                                            }
                                                        }
                                                    ],
                                                },
                                            ],
                                        }
                                    ],
                                }
                            ],
                        },
                        {
                            "attributes": {
                                "id": "test_id",
                                "class": ["output-container"],
                            },
                            "div": [
                                {"attributes": {"class": ["output-wrapper"]}, "p": [{}]}
                            ],
                        },
                    ]
                }
            ],
        }
    ]
}

EXPECTED_INCOMPLETE_HTML_DICT = {
    "div": [{"attributes": {"class": ["banner-container"]}, "h3": [{"u": [{}]}]}]
}

EXPECTED_HTML_ELEMS_ORDER = (
    "body",
    "div",
    ".banner-container",
    "h3",
    "u",
    ".form-container",
    "div",
    ".form-wrapper",
    "form",
    "div",
    ".upload-field",
    "label",
    "u",
    "input",
    ".submit-wrapper",
    "button",
    ".button",
    "#test_id",
    ".output-container",
    "div",
    ".output-wrapper",
    "p",
)

EXPECTED_INCOMPLETE_HTML_ELEMS_ORDER = ("div", ".banner-container", "h3", "u")


EXPECTED_ORDERED_HTML_ELEMS = (
    "body",
    "div",
    ".banner-container",
    "h3",
    "u",
    ".form-container",
    ".form-wrapper",
    "form",
    ".upload-field",
    "label",
    "input",
    ".submit-wrapper",
    "button",
    ".button",
    "#test_id",
    ".output-container",
    ".output-wrapper",
    "p",
)

# EXPECTED_ORDERED_INCOMPLETE_HTML_ELEMS

EXPECTED_CSS_DICT = {
    ".banner-container": {"comment": "", "props": "background: #BEBEBE"},
    ".output-container, .submit-wrapper, .form-container, .form-wrapper, .banner-container": {
        "comment": "",
        "props": "display: flex;\njustify-content: center;\nalign-items: center",
    },
    ".form-wrapper": {
        "comment": "",
        "props": "border: 1px solid black;\nborder-radius: 5px;\nmargin: 0.8rem 0 0 0;\nbackground: rgb(218, 226, 218);\nbackground: linear-gradient(90deg, rgba(218, 226, 218, 1) 26%, rgba(199, 199, 209, 1) 100%, rgba(0, 255, 23, 1) 100%);\npadding: 1rem",
    },
    ".upload-field": {
        "comment": "",
        "props": "display: grid;\njustify-content: center;\nalign-items: center",
    },
    ".button": {
        "comment": "",
        "props": "align-items: center;\nborder: 1px solid #787878;\nborder-radius: 12px;\nbox-shadow: transparent 0 0 0 3px, rgba(18, 18, 18, 0.1) 0 6px 20px;\nbox-sizing: border-box;\ncolor: #121412;\ncursor: pointer;\ndisplay: inline-flex;\nfont-family: Inter, sans-serif;\nfont-size: 1rem;\nfont-weight: 500;\njustify-content: center;\nline-height: 1;\nmargin: 0.8rem 0 0 0;\noutline: none;\npadding: 0.8rem 1rem;\ntext-align: center;\ntext-decoration: none;\ntransition: box-shadow 0.2s, -webkit-box-shadow 0.2s;\nwhite-space: nowrap;\nuser-select: none",
    },
    ".button:hover": {
        "comment": "",
        "props": "box-shadow: #C0C0C0 0 0 0 3px, transparent 0 0 0 0",
    },
    ".output-container": {"comment": "", "props": "padding: 2rem"},
    ".output-wrapper": {"comment": "", "props": "width: 35rem"},
    ".output-wrapper p": {"comment": "/*TEST COMMENT*/", "props": "text-align: center"},
    ".radio-btn-wrapper": {
        "comment": "",
        "props": "display: flex;\njustify-content: space-between;\nwidth: 100%",
    },
}
