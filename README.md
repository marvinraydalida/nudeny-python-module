# Nudeny Python Module for Nudeny Restful API

## *detectExposed()*
- Draw bounding box to exposed parts
- Parameters:
  - paths - List of path(s).
  - urls - List of url(s).
  - save_path - Path to save images. Default value is "None".
- Return: Response dictionary.
 
*Example:* 
```python
from Nudeny import Detect

nudeny_detector = Detect()

paths = [
    'C:/Users/user/Desktop/Nudeny/nude/99115338_011_190e.jpg',
    'C:/Users/user/Desktop/Nudeny/nude/uau74uozrrw91.jpg',
]

urls = [
    'https://cdn.hegreartnudes.com/content/hegreart_d4aee5a1aa95a/cropped/9/adriana_mainthumb_vertical.jpg',
    'https://i.ibb.co/y80vhbf/kalyani-priyadarshan.jpg'
]

save_path = 'C:/Users/user/Desktop/here'

response = nudeny_detector.detectExposed(paths=paths, urls=urls, save_path=save_path)
print(response)
```
*Output:*

```json
{
    "predictions": [
        {
            "filename": "99115338_011_190e.jpg",
            "url": "http://127.0.0.1:8000/static/de72aba1-e3bb-4a26-9f90-024216a3956e-99115338_011_190e.jpg",
            "exposed_parts": {
                "female_genitalia": {
                    "confidence_score": 67.99014210700989,
                    "top": 337,
                    "left": 120,
                    "bottom": 388,
                    "right": 153,
                },
                "female_breast": {
                    "confidence_score": 53.750550746917725,
                    "top": 162,
                    "left": 85,
                    "bottom": 229,
                    "right": 234,
                },
                "buttocks": {
                    "confidence_score": 52.793073654174805,
                    "top": 388,
                    "left": 72,
                    "bottom": 433,
                    "right": 200,
                },
            },
        },
        {
            "filename": "uau74uozrrw91.jpg",
            "url": "http://127.0.0.1:8000/static/dd77fe45-285b-46c5-9679-766568b7659e-uau74uozrrw91.jpg",
            "exposed_parts": {
                "male_genitalia": {
                    "confidence_score": 74.42192435264587,
                    "top": 581,
                    "left": 193,
                    "bottom": 697,
                    "right": 276,
                }
            },
        },
        {
            "filename": "files.jpg",
            "url": "http://127.0.0.1:8000/static/9b7775ce-d25e-42fc-b1d4-4b1f1da07896-files.jpg",
            "exposed_parts": {
                "female_genitalia": {
                    "confidence_score": 70.24761438369751,
                    "top": 443,
                    "left": 201,
                    "bottom": 526,
                    "right": 253,
                },
                "female_breast": {
                    "confidence_score": 64.92639183998108,
                    "top": 267,
                    "left": 112,
                    "bottom": 395,
                    "right": 420,
                },
                "buttocks": {
                    "confidence_score": 62.286925315856934,
                    "top": 534,
                    "left": 152,
                    "bottom": 623,
                    "right": 307,
                },
            },
        },
        {
            "filename": "files.jpg",
            "url": "http://127.0.0.1:8000/static/24103b9f-8cf9-4175-80fa-8e68cd62768f-files.jpg",
            "exposed_parts": {
                "female_breast": {
                    "confidence_score": 72.48346209526062,
                    "top": 901,
                    "left": 2374,
                    "bottom": 1487,
                    "right": 3055,
                }
            },
        },
    ]
}
```

## *censorExposed()*
- Censor exposed parts
- Parameters:
  - paths - List of path(s).
  - urls - List of url(s).
  - save_path - Path to save images. Default value is "None".
- Return: Response dictionary.

*Example:* 
```python
from Nudeny import Detect

nudeny_detector = Detect()

paths = [
    'C:/Users/user/Desktop/Nudeny/nude/99115338_011_190e.jpg',
    'C:/Users/user/Desktop/Nudeny/nude/uau74uozrrw91.jpg',
]

urls = [
    'https://cdn.hegreartnudes.com/content/hegreart_d4aee5a1aa95a/cropped/9/adriana_mainthumb_vertical.jpg',
    'https://i.ibb.co/y80vhbf/kalyani-priyadarshan.jpg'
]

save_path = 'C:/Users/user/Desktop/here'

response = nudeny_detector.censorExposed(paths=paths, urls=urls, save_path=save_path)
print(response)
```
*Output:*

```json
{
    "predictions": [
        {
            "filename": "99115338_011_190e.jpg",
            "url": "http://127.0.0.1:8000/static/de72aba1-e3bb-4a26-9f90-024216a3956e-99115338_011_190e.jpg",
            "exposed_parts": {
                "female_genitalia": {
                    "confidence_score": 67.99014210700989,
                    "top": 337,
                    "left": 120,
                    "bottom": 388,
                    "right": 153,
                },
                "female_breast": {
                    "confidence_score": 53.750550746917725,
                    "top": 162,
                    "left": 85,
                    "bottom": 229,
                    "right": 234,
                },
                "buttocks": {
                    "confidence_score": 52.793073654174805,
                    "top": 388,
                    "left": 72,
                    "bottom": 433,
                    "right": 200,
                },
            },
        },
        {
            "filename": "uau74uozrrw91.jpg",
            "url": "http://127.0.0.1:8000/static/dd77fe45-285b-46c5-9679-766568b7659e-uau74uozrrw91.jpg",
            "exposed_parts": {
                "male_genitalia": {
                    "confidence_score": 74.42192435264587,
                    "top": 581,
                    "left": 193,
                    "bottom": 697,
                    "right": 276,
                }
            },
        },
        {
            "filename": "files.jpg",
            "url": "http://127.0.0.1:8000/static/9b7775ce-d25e-42fc-b1d4-4b1f1da07896-files.jpg",
            "exposed_parts": {
                "female_genitalia": {
                    "confidence_score": 70.24761438369751,
                    "top": 443,
                    "left": 201,
                    "bottom": 526,
                    "right": 253,
                },
                "female_breast": {
                    "confidence_score": 64.92639183998108,
                    "top": 267,
                    "left": 112,
                    "bottom": 395,
                    "right": 420,
                },
                "buttocks": {
                    "confidence_score": 62.286925315856934,
                    "top": 534,
                    "left": 152,
                    "bottom": 623,
                    "right": 307,
                },
            },
        },
        {
            "filename": "files.jpg",
            "url": "http://127.0.0.1:8000/static/24103b9f-8cf9-4175-80fa-8e68cd62768f-files.jpg",
            "exposed_parts": {
                "female_breast": {
                    "confidence_score": 72.48346209526062,
                    "top": 901,
                    "left": 2374,
                    "bottom": 1487,
                    "right": 3055,
                }
            },
        },
    ]
}
```
