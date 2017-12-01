# zalamo photo downloader

Requirement:
- Python 2.7

### Installing:

Download zalamo.py and run:

```
pip install requests
```

### Configuration

You must get headers from already existed session in Zalamo.
Login to your account(in zalamo) and open Developer Tools -> Network Tab in Firefox, 
you need sesson_id and PHPSESSID informations from cookies.
Check also number of first and last photos from your gallery.

```
session_id = 10108274
first_photo = 100000
last_photo =  103000
```

### Run

```
python zalamo.py
```

## Author
Karol Przybylski


