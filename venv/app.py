from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None

class Home(Resource):
    def get(self):
        return {
            "data":[
                {
                    "Header":[
                        {
                            "nav":[
                                {
                                    "logo": [
                                        {
                                            "img":"data:image/webp;base64,UklGRiQCAABXRUJQVlA4TBgCAAAvcUAEEH8gEEgC2l9xhUEZpIlI6DiQG23/2zYvk8F8msDGuctg52z/zwtAG4gbkKUzUKJxTqW8AekJqA2ccwA0gE+JZia/4g8JK0T0fwJWeaD1DiB8zFiSdkgk6S4YeQBrKx9gpAJ2d6r4AnMHCJUH3vuMH0ZRdIukF0VSDaNNq6uUpSrW+kqSrozqwHs5wLDBuI6dbABfHmOkPLCfYiTPGsn2Eg8YrurApJyhHVsVYJrSlwKgJZ2iNa2+CYDJNw9YFjK4yhnpBrhKOdBiJwd9BUCr0H4HLJ8FYGIytHYw0gCepE3jPTlwoDqpqzxmYN5BGGQJe5aK7Ke4Cp6oAWM5aVOHsMMyz/sbGdam5zDaUY1pbIU6YdSBmUpp/2u8P87EYViHsSQFJJLUy2MUyHfVsbZVYTGAuYrsSjGJx7DGsM7EgfHDKIoukvSiaKEaRv5s8ERnrLGKjFQ8ypOA6THeeyzzMK5jJxvA24G1r5FOWst3sK0KM5XS1gf8g25g3pGFVcHIfyJtuvJpK9VjLAeYxrC82YPWuzDINneMfFfyrK20xxyoccj09Qaw+Ohlm1mMVbGGaTu5voJDhr+awHhey7YsWts7eWuuPDCU05IuwyyG96oA+3Iy9WMswJXvqgewpQYj2TGEKgFbylsPoyi6RdKLoqmuH+mJfKutDmZ5iIkBugMsSdohkaSHuSPtq2GtrWJoT6Q7RQ==",
                                            "url":"https://preview.colorlib.com/theme/webmag/index.html"
                                        }
                                    ]
                                },
                                {
                                    "right":[
                                        {
                                            "nav-news":"News",
                                            "url":"https://preview.colorlib.com/theme/webmag/category.html"
                                        },
                                        {
                                            "nav-popular":"Popular",
                                            "url":"https://preview.colorlib.com/theme/webmag/category.html"
                                        },
                                        {
                                            "nav-web_desain":"Web Design",
                                            "url":"https://preview.colorlib.com/theme/webmag/category.html"
                                        },
                                        {
                                            "nav-javascript":"JavaScript",
                                            "url":"https://preview.colorlib.com/theme/webmag/category.html"
                                        },
                                        {
                                            "nav-css":"Css",
                                            "url":"https://preview.colorlib.com/theme/pexman/contact.html"
                                        },
                                        {
                                            "nav-jquery":"Jquery",
                                            "url":"https://preview.colorlib.com/theme/pexman/contact.html"
                                        }
                                    ]   
                                }
                            ]
                        }
                    ],

                    "Body":[
                        {
                            "top-body":[
                                {
                                    "top-body-card1":[
                                        {
                                            "title":"Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "top-body-card2":[
                                        {
                                            "title":"Ask HN: Does Anybody Still Use JQuery?",
                                            "date":"March 27, 2018",
                                            "catagories":"JQUERY",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                            "recent-posts":[
                                {
                                    "recent-posts-card1":[
                                        {
                                            "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                            "date":"March 27, 2018",
                                            "catagories":"WEB DESIGN",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "recent-posts-card2":[
                                        {
                                            "title":"Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "recent-posts-card3":[
                                        {
                                            "title":"Ask HN: Does Anybody Still Use JQuery?",
                                            "date":"March 27, 2018",
                                            "catagories":"JQUERY",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "recent-posts-card4":[
                                        {
                                            "title":"Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-6.jpg.pagespeed.ic.XqKLoKE85z.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "recent-posts-card5":[
                                        {
                                            "title":"CSS Float: A Tutorial",
                                            "date":"March 27, 2018",
                                            "catagories":"CSS",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "recent-posts-card6":[
                                        {
                                            "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                            "date":"March 27, 2018",
                                            "catagories":"WEB DESIGN",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                            "mid-konten":[
                                {
                                    "mid-konten-card1":[
                                        {
                                            "title":"Ask HN: Does Anybody Still Use JQuery?",
                                            "date":"March 27, 2018",
                                            "catagories":"JQUERY",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "mid-konten-card2":[
                                        {
                                            "title":"CSS Float: A Tutorial",
                                            "date":"March 27, 2018",
                                            "catagories":"CSS",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "mid-konten-card3":[
                                        {
                                            "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                            "date":"March 27, 2018",
                                            "catagories":"WEB DESIGN",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "mid-konten-card4":[
                                        {
                                            "title":"Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "mid-konten-card5":[
                                        {
                                            "title":"Ask HN: Does Anybody Still Use JQuery?",
                                            "date":"March 27, 2018",
                                            "catagories":"JQUERY",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "mid-konten-card6":[
                                        {
                                            "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                            "date":"March 27, 2018",
                                            "catagories":"WEB DESIGN",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "mid-konten-card7":[
                                        {
                                            "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                            "widget-mid":[
                                {
                                    "widget-most_read":[
                                        {
                                            "most_read-post-1":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-1.jpg.pagespeed.ic.NYJjOYjv_V.webp",
                                                    "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "most_read-post-2":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-2.jpg.pagespeed.ic.cSUEAOhjjU.webp",
                                                    "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "most_read-post-3":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-3.jpg.pagespeed.ic.5z-SP7IbT6.webp",
                                                    "title":"Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "most_read-post-4":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-4.jpg.pagespeed.ic.i3iWR0f20S.webp",
                                                    "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ]
                                        }
                                    ],
                                    "widget-featured-posts":[
                                        {
                                            "featured_posts-card-1":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                                    "title":"Ask HN: Does Anybody Still Use JQuery?",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JQUERY"
                                                }
                                            ],
                                            "featured_posts-card-2":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                                    "title":"Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT"
                                                }
                                            ]
                                        }
                                    ],
                                    "mid-widget-iklan":[
                                        {
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xad-1.jpg.pagespeed.ic.qQJhsdJdF0.webp"
                                        }
                                    ]
                                }
                            ],
                            "featured-post":[
                                {
                                    "featured-post-card1":[
                                        {
                                            "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "featured-post-card2":[
                                        {
                                            "title":"Ask HN: Does Anybody Still Use JQuery?",
                                            "date":"March 27, 2018",
                                            "catagories":"JQUERY",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "featured-post-card3":[
                                        {
                                            "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                            "date":"March 27, 2018",
                                            "catagories":"WEB DESIGN",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                            "most-read":[
                                {
                                    "most-read-card1":[
                                        {
                                            "title":"Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "text":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "most-read-card2":[
                                        {
                                            "title":"Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date":"March 27, 2018",
                                            "catagories":"JAVASCRIPT",
                                            "text":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-6.jpg.pagespeed.ic.XqKLoKE85z.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "most-read-card3":[
                                        {
                                            "title":"CSS Float: A Tutorial",
                                            "date":"March 27, 2018",
                                            "catagories":"CSS",
                                            "text":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "most-read-card4":[
                                        {
                                            "title":"Ask HN: Does Anybody Still Use JQuery?",
                                            "date":"March 27, 2018",
                                            "catagories":"JQUERY",
                                            "text":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                            "widget-catagories":[
                                {
                                    "bottom-widget-iklan":[
                                        {
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xad-1.jpg.pagespeed.ic.qQJhsdJdF0.webp"
                                        }
                                    ],
                                    "widget-categories-1":[
                                        {
                                            "catagories":"WEB DESIGN",
                                            "total_catagories":"350"
                                        }
                                    ],
                                    "widget-categories-2":[
                                        {
                                            "catagories":"JAVASCRIPT",
                                            "total_catagories":"74"
                                        }
                                    ],
                                    "widget-categories-3":[
                                        {
                                            "catagories":"JQUERY",
                                            "total_catagories":"41"
                                        }
                                    ],
                                    "widget-categories-4":[
                                        {
                                            "catagories":"CSS",
                                            "total_catagories":"35"
                                        }
                                    ]
                                }
                            ],
                            "widget-tags":[
                                {
                                    "tags-chrome":"Chrome",
                                    "tags-css":"CSS",
                                    "tags-tutorial":"Tutorial",
                                    "tags-backend":"Backend",
                                    "tags-jquery":"JQuery",
                                    "tags-desain":"Desain",
                                    "tags-development":"Development",
                                    "tags-javascript":"JavaScript",
                                    "tags-website":"Website"
                                }
                            ]
                        }
                    ],

                    "Footer":[
                        {
                            "left1-footer": [
                                {
                                    "img":"data:image/webp;base64,UklGRiQCAABXRUJQVlA4TBgCAAAvcUAEEH8gEEgC2l9xhUEZpIlI6DiQG23/2zYvk8F8msDGuctg52z/zwtAG4gbkKUzUKJxTqW8AekJqA2ccwA0gE+JZia/4g8JK0T0fwJWeaD1DiB8zFiSdkgk6S4YeQBrKx9gpAJ2d6r4AnMHCJUH3vuMH0ZRdIukF0VSDaNNq6uUpSrW+kqSrozqwHs5wLDBuI6dbABfHmOkPLCfYiTPGsn2Eg8YrurApJyhHVsVYJrSlwKgJZ2iNa2+CYDJNw9YFjK4yhnpBrhKOdBiJwd9BUCr0H4HLJ8FYGIytHYw0gCepE3jPTlwoDqpqzxmYN5BGGQJe5aK7Ke4Cp6oAWM5aVOHsMMyz/sbGdam5zDaUY1pbIU6YdSBmUpp/2u8P87EYViHsSQFJJLUy2MUyHfVsbZVYTGAuYrsSjGJx7DGsM7EgfHDKIoukvSiaKEaRv5s8ERnrLGKjFQ8ypOA6THeeyzzMK5jJxvA24G1r5FOWst3sK0KM5XS1gf8g25g3pGFVcHIfyJtuvJpK9VjLAeYxrC82YPWuzDINneMfFfyrK20xxyoccj09Qaw+Ohlm1mMVbGGaTu5voJDhr+awHhey7YsWts7eWuuPDCU05IuwyyG96oA+3Iy9WMswJXvqgewpQYj2TGEKgFbylsPoyi6RdKLoqmuH+mJfKutDmZ5iIkBugMsSdohkaSHuSPtq2GtrWJoT6Q7RQ=="
                                },
                                {
                                    "footer-li-privacy_policy-left":"Privacy Policy",
                                    "footer-li-advertisement-left":" Advertisement",
                                    "footer-text-left":"© Copyright ©2022 All rights reserved | This template is made with  by Colorlib"
                                },
                                {
                                    "footer-h2-left1":"Connect with us"
                                }
                            ],
                            "left2-footer": [
                                {
                                "footer-h3-left":"About Us",
                                "footer-li-about_us-left":"About Us",
                                "footer-li-services-left":"Join Us",
                                "footer-li-contacts-left":"Contacts" 
                                }  
                            ],
                            "right1-footer":[
                                {
                                    "footer-h3-right":"Catagories",
                                    "footer-li-web_design-right":"Web Design",
                                    "footer-li-css-right":"Css",
                                    "footer-li-jquery-right":"Jquery"
                                }
                            ],
                            "right2-footer":[
                                {
                                    "footer-h3-join_our_newsletter":"Join Our Newsletter"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
class Javascript(Resource):
    def get(self):
        return {
            "data":[
                {
                     "Body":[
                        {
                            "main_konten":[
                                {
                                    "top_konten":[
                                        {
                                            "top_konten-card1":[
                                                {
                                                    "title":"Javascript : Prototype vs Class",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT",
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "top_konten-card2":[
                                                {
                                                    "title":"Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT",
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "top_konten-card3":[
                                                {
                                                    "title":"Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT",
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-6.jpg.pagespeed.ic.XqKLoKE85z.webp",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ]
                                        }
                                    ],
                                    "mid_iklan":[
                                        {
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xad-2.jpg.pagespeed.ic.RB_ZDhAXxh.webp"
                                        }
                                    ],
                                    "bottom_konten":[
                                        {
                                            "bottom_konten-card1":[
                                                {
                                                    "title":"Ask HN: Does Anybody Still Use JQuery?",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT",
                                                    "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "bottom_konten-card2":[
                                                {
                                                    "title":"Ask HN: Does Anybody Still Use JQuery?",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT",
                                                    "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "bottom_konten-card3":[
                                                {
                                                    "title":"Javascript : Prototype vs Class",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT",
                                                    "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "bottom_konten-card4":[
                                                {
                                                    "title":"Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                                    "date":"March 27, 2018",
                                                    "catagories":"JAVASCRIPT",
                                                    "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "widget":[
                                {
                                    "mid-widget-iklan":[
                                        {
                                            "img":"https://preview.colorlib.com/theme/webmag/img/xad-1.jpg.pagespeed.ic.qQJhsdJdF0.webp"
                                        }
                                    ],
                                    "widget-most_read":[
                                        {
                                            "most_read-post-1":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-1.jpg.pagespeed.ic.NYJjOYjv_V.webp",
                                                    "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "most_read-post-2":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-2.jpg.pagespeed.ic.cSUEAOhjjU.webp",
                                                    "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "most_read-post-3":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-3.jpg.pagespeed.ic.5z-SP7IbT6.webp",
                                                    "title":"Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ],
                                            "most_read-post-4":[
                                                {
                                                    "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-4.jpg.pagespeed.ic.i3iWR0f20S.webp",
                                                    "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                                    "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                                }
                                            ]
                                        }
                                    ],
                                    "widget-catagories":[
                                        {
                                            "widget-categories-1":[
                                                {
                                                    "catagories":"WEB DESIGN",
                                                    "total_catagories":"350"
                                                }
                                            ],
                                            "widget-categories-2":[
                                                {
                                                    "catagories":"JAVASCRIPT",
                                                    "total_catagories":"74"
                                                }
                                            ],
                                            "widget-categories-3":[
                                                {
                                                    "catagories":"JQUERY",
                                                    "total_catagories":"41"
                                                }
                                            ],
                                            "widget-categories-4":[
                                                {
                                                    "catagories":"CSS",
                                                    "total_catagories":"35"
                                                }
                                            ]
                                        }
                                    ],
                                    "widget-tags":[
                                        {
                                            "tags-chrome":"Chrome",
                                            "tags-css":"CSS",
                                            "tags-tutorial":"Tutorial",
                                            "tags-backend":"Backend",
                                            "tags-jquery":"JQuery",
                                            "tags-desain":"Desain",
                                            "tags-development":"Development",
                                            "tags-javascript":"JavaScript",
                                            "tags-website":"Website"
                                        }
                                    ],
                                    "widget-archive":[
                                        {
                                            "widget-archive-h2":"Archive",
                                            "widget-archive-januari-2018":"Jan 2018",
                                            "widget-archive-li-februari-2018":"Feb 2018",
                                            "widget-archive-li-maret-2018":"Mar 2018"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
class Blog(Resource):
    def get(self):
        return {
            "data":[
                {
                    "Body":[
                    {
                        "banner":[
                            {
                                "title-h1":"Ask HN: Does Anybody Still Use JQuery?",
                                "date":"March 27, 2018",
                                "catagories":"JAVASCRIPT",
                                "img":"https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp"
                                
                            }
                        ],
                        "artikel":[
                            {
                                "title1-h3":"Lorem Ipsum: when, and when not to use it",
                                "text1":"Do you like Cheese Whiz? Spray tan? Fake eyelashes? That's what is Lorem Ipsum to many—it rubs them the wrong way, all the way. It's unreal, uncanny, makes you wonder if something is wrong, it seems to seek your attention for all the wrong reasons. Usually, we prefer the real thing, wine without sulfur based preservatives, real butter, not margarine, and so we'd like our layouts and designs to be filled with real words, with thoughts that count, information that has value.",
                                "text2":"The toppings you may chose for that TV dinner pizza slice when you forgot to shop for foods, the paint you may slap on your face to impress the new boss is your business. But what about your daily bread? Design comps, layouts, wireframes—will your clients accept that you go about things the facile way? Authorities in our business will tell in no uncertain terms that Lorem Ipsum is that huge, huge no no to forswear forever. Not so fast, I'd say, there are some redeeming factors in favor of greeking text, as its use is merely the symptom of a worse problem to take into consideration.",
                                "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                "text3":"You begin with a text, you sculpt information, you chisel away what's not needed, you come to the point, make things clear, add value, you're a content person, you like words. Design is no afterthought, far from it, but it comes in a deserved second. Anyway, you still use Lorem Ipsum and rightly so, as it will always have a place in the web workers toolbox, as things happen, not always the way you like it, not always in the preferred order. Even if your less into design and more into content strategy you may find some redeeming value with, wait for it, dummy copy, no less.",
                                "text4":"There's lot of hate out there for a text that amounts to little more than garbled words in an old language. The villagers are out there with a vengeance to get that Frankenstein, wielding torches and pitchforks, wanting to tar and feather it at the least, running it out of town in shame.",
                                "text5":"One of the villagers, Kristina Halvorson from Adaptive Path, holds steadfastly to the notion that design cant be tested without real content:",
                                "blockquote":"I ve heard the argument that “lorem ipsum” is effective in wireframing or design because it helps people focus on the actual layout, or color scheme, or whatever. What kills me here is that we re talking about creating a user experience that will (whether we like it or not) be DRIVEN by words. The entire structure of the page or app flow is FOR THE WORDS.",
                                "text6":"If that's what you think how bout the other way around? How can you evaluate content without design? No typography, no colors, no layout, no styles, all those things that convey the important signals that go beyond the mere textual, hierarchies of information, weight, emphasis, oblique stresses, priorities, all those subtle cues that also have visual and emotional appeal to the reader. Rigid proponents of content strategy may shun the use of dummy copy but then designers might want to ask them to provide style sheets with the copy decks they supply that are in tune with the design direction they require.",
                                "title2-h3":"Summing up, if the copy is diverting attention from the design it s because it s not up to task.",
                                "text7":"Typographers of yore didn't come up with the concept of dummy copy because people thought that content is inconsequential window dressing, only there to be used by designers who can’t be bothered to read. Lorem Ipsum is needed because words matter, a lot. Just fill up a page with draft copy about the client’s business and they will actually read it and comment on it. They will be drawn to it, fiercely. Do it the wrong way and draft copy can derail your design review."
                            }
                        ],
                        "iklan":[
                            {
                                "img":"https://preview.colorlib.com/theme/webmag/img/xad-2.jpg.pagespeed.ic.RB_ZDhAXxh.webp"
                            }
                        ],
                        "author":[
                            {
                                "author_name":"John Doe",
                                "deskripsi":"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                                "img":"https://preview.colorlib.com/theme/webmag/img/xauthor.png.pagespeed.ic.-dOTrKKeTJ.webp"
                            }
                        ],
                        "widget":[
                            {
                                "mid-widget-iklan":[
                                    {
                                        "img":"https://preview.colorlib.com/theme/webmag/img/xad-1.jpg.pagespeed.ic.qQJhsdJdF0.webp"
                                    }
                                ],
                                "widget-most_read":[
                                    {
                                        "most_read-post-1":[
                                            {
                                                "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-1.jpg.pagespeed.ic.NYJjOYjv_V.webp",
                                                "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                                "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                            }
                                        ],
                                        "most_read-post-2":[
                                            {
                                                "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-2.jpg.pagespeed.ic.cSUEAOhjjU.webp",
                                                "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                                "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                            }
                                        ],
                                        "most_read-post-3":[
                                            {
                                                "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-3.jpg.pagespeed.ic.5z-SP7IbT6.webp",
                                                "title":"Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                                "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                            }
                                        ],
                                        "most_read-post-4":[
                                            {
                                                "img":"https://preview.colorlib.com/theme/webmag/img/xwidget-4.jpg.pagespeed.ic.i3iWR0f20S.webp",
                                                "title":"Tell-A-Tool: Guide To Web Design And Development Tools",
                                                "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                            }
                                        ]
                                    }
                                ],
                                "featured-post":[
                                    {
                                        "featured-post-card1":[
                                            {
                                                "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                                "date":"March 27, 2018",
                                                "catagories":"JAVASCRIPT",
                                                "img":"https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                                "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                            }
                                        ],
                                        "featured-post-card2":[
                                            {
                                                "title":"Ask HN: Does Anybody Still Use JQuery?",
                                                "date":"March 27, 2018",
                                                "catagories":"JQUERY",
                                                "img":"https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                                "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                            }
                                        ],
                                        "featured-post-card3":[
                                            {
                                                "title":"Pagedraw UI Builder Turns Your Website Design Mockup Into Code Automatically",
                                                "date":"March 27, 2018",
                                                "catagories":"WEB DESIGN",
                                                "img":"https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                                "url":"https://preview.colorlib.com/theme/webmag/blog-post.html"
                                            }
                                        ]
                                    }
                                ],
                                "widget-catagories":[
                                    {
                                        "widget-categories-1":[
                                            {
                                                "catagories":"WEB DESIGN",
                                                "total_catagories":"350"
                                            }
                                        ],
                                        "widget-categories-2":[
                                            {
                                                "catagories":"JAVASCRIPT",
                                                "total_catagories":"74"
                                            }
                                        ],
                                        "widget-categories-3":[
                                            {
                                                "catagories":"JQUERY",
                                                "total_catagories":"41"
                                            }
                                        ],
                                        "widget-categories-4":[
                                            {
                                                "catagories":"CSS",
                                                "total_catagories":"35"
                                            }
                                        ]
                                    }
                                ],
                                "widget-tags":[
                                    {
                                        "tags-chrome":"Chrome",
                                        "tags-css":"CSS",
                                        "tags-tutorial":"Tutorial",
                                        "tags-backend":"Backend",
                                        "tags-jquery":"JQuery",
                                        "tags-desain":"Desain",
                                        "tags-development":"Development",
                                        "tags-javascript":"JavaScript",
                                        "tags-website":"Website"
                                    }
                                ],
                                "widget-archive":[
                                    {
                                        "widget-archive-h2":"Archive",
                                        "widget-archive-januari-2018":"Jan 2018",
                                        "widget-archive-li-februari-2018":"Feb 2018",
                                        "widget-archive-li-maret-2018":"Mar 2018"
                                    }
                                ]
                            }
                        ]
                    }
                ]
              }
            ]
        }
class Catagories(Resource):
    def get(self):
        return {
            "data":[
                {
                    "Body":[
                    {
                        "catagories":[
                            {
                                "javascript":"JAVASCRIPT",
                                "web_design":"WEB DESIGN",
                                "css":"CSS",
                                "jquery":"JQUERY"
                            }
                        ]
                    }
                ]
              }
            ]
        }
class Catagories_Javascript(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Body": [
                        {
                            "catagories_konten_javascript": [
                                {
                                    "catagories_javascript-card1": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "JAVASCRIPT",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_javascript-card2": [
                                        {
                                            "title": "Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date": "March 27, 2018",
                                            "catagories": "JAVASCRIPT",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_javascript-card3": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "JAVASCRIPT",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-6.jpg.pagespeed.ic.XqKLoKE85z.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_javascript-card4": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "JAVASCRIPT",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_javascript-card5": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "JAVASCRIPT",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_javascript-card6": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "JAVASCRIPT",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                                    "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_javascript-card7": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "JAVASCRIPT",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                        }
                    ]
                }
            ]
        }
class Catagories_WebDesign(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Body": [
                        {
                            "catagories_konten_web_design": [
                                {
                                    "catagories_web_design-card1": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "WEB DESIGN",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_web_design-card2": [
                                        {
                                            "title": "Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date": "March 27, 2018",
                                            "catagories": "WEB DESIGN",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_web_design-card3": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "WEB DESIGN",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-6.jpg.pagespeed.ic.XqKLoKE85z.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_web_design-card4": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "WEB DESIGN",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_web_design-card5": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "WEB DESIGN",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_web_design-card6": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "WEB DESIGN",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                                    "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_web_design-card7": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "WEB DESIGN",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                        }
                    ]
                }
            ]
        }
class Catagories_Css(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Body": [
                        {
                            "catagories_konten_css": [
                                {
                                    "catagories_css-card1": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "CSS",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_css-card2": [
                                        {
                                            "title": "Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date": "March 27, 2018",
                                            "catagories": "CSS",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_css-card3": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "CSS",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-6.jpg.pagespeed.ic.XqKLoKE85z.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_css-card4": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "CSS",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_css-card5": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "CSS",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_css-card6": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "CSS",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                                    "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_css-card7": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "CSS",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                        }
                    ]
                }
            ]
        }
class Catagories_Jquery(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Body": [
                        {
                            "catagories_konten_jquery": [
                                {
                                    "catagories_jquery-card1": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "JQUERY",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_jquery-card2": [
                                        {
                                            "title": "Chrome Extension Protects Against JavaScript-Based CPU Side-Channel Attacks",
                                            "date": "March 27, 2018",
                                            "catagories": "JQUERY",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-4.jpg.pagespeed.ic.5tBCPmCJW-.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_jquery-card3": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "JQUERY",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-6.jpg.pagespeed.ic.XqKLoKE85z.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_jquery-card4": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "JQUERY",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-2.jpg.pagespeed.ic.DOAToGcDYE.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_jquery-card5": [
                                        {
                                            "title": "Ask HN: Does Anybody Still Use JQuery?",
                                            "date": "March 27, 2018",
                                            "catagories": "JQUERY",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-5.jpg.pagespeed.ic.jXTrIrIxiM.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_jquery-card6": [
                                        {
                                            "title": "Javascript : Prototype vs Class",
                                            "date": "March 27, 2018",
                                            "catagories": "JQUERY",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-3.jpg.pagespeed.ic.UjtolzGXxD.webp",
                                                    "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ],
                                    "catagories_jquery-card7": [
                                        {
                                            "title": "Why Node.js Is The Coolest Kid On The Backend Development Block!",
                                            "date": "March 27, 2018",
                                            "catagories": "JQUERY",
                                            "deskripsi": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam...",
                                            "img": "https://preview.colorlib.com/theme/webmag/img/xpost-1.jpg.pagespeed.ic.2GXRfHYjOg.webp",
                                            "url": "https://preview.colorlib.com/theme/webmag/blog-post.html"
                                        }
                                    ]
                                }
                            ],
                        }
                    ]
                }
            ]
        }


api.add_resource(Home, '/home/')
api.add_resource(Javascript, '/javascript/')
api.add_resource(Blog, '/javascript/blog/')
api.add_resource(Catagories, '/catagories/')
api.add_resource(Catagories_Javascript, '/catagories/javascript/')
api.add_resource(Catagories_WebDesign, '/catagories/web_design/')
api.add_resource(Catagories_Css, '/catagories/css/')
api.add_resource(Catagories_Jquery, '/catagories/jquery/')

@app.errorhandler(404)
def page_not_found(e):
    return {"error":"not found end point"}, 404

if __name__ == '__main__':
    app.run(debug=True)