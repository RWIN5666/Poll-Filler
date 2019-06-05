# Poll Filler
A Python script to fill out form (and learn how to do it !).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

#### Python and required modules

This script works with Python 3.6 or later. 

You need to have Selenium installed in order to run it. If you have pip on your system, you can simply install or upgrade the Python bindings:
```
$ pip3 install -U selenium
```

Alternately, you can download the source distribution from [PyPI](https://pypi.org/project/selenium/#files), unarchive it, and run:
```
$ python3 setup.py install
```

#### Browser

Last (but not least), you need to install [Firefox](https://www.mozilla.org/en-US/firefox/new/) and its [geckodriver](https://github.com/mozilla/geckodriver/releases). Someday, I may add Chromium support... But for now only Firefox is supported. In order to install geckodriver, follow these steps :
```
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz 
$ tar xvf geckodriver*
$ chmod +x geckodriver
$ sudo mv geckodriver /usr/local/bin/
```

You're now ready to use the script !

## Configure your poll

You need to configure your poll by using a json configuration file. You can modify the `config.json` as base. All the keys in this file must be filled, if it's not the case, the script will fail.

```
{
    "name": "Your name",
    "email": "yourmail@somewhere.com",
    "poll_title" : "Your Title",
    "description": "Dummy description",
    "people_can_only_modify_their_vote": true,
    "receive_mail_for_each_vote": true,
    "receive_mail_for_each_comment": true,
    "use_image_instead_of_text": false,
    "language": "EN",
    "item_file": "items.txt"
}
```

## Running the script

You can run the script just like this : 
```
$ python3 run_poll_filler.py
```

You can also specify a specific configuration file by this way :
````
$ python3 run_poll_filler.py --config=my_configuration_file.json
````

## Built With

* [Selenium 3.x](https://seleniumhq.github.io/selenium/docs/api/py/index.html) - Web package that automate web browser interaction from Python

## Contributing

Please read incoming [CONTRIBUTING.md] for details.

## Versioning

I intend to use [SemVer](http://semver.org/) for versioning. As I think the script is not good enough for the moment, a future 1.0.0 version will soon see the light of day...

## Authors

* **RWIN5666** - [Github Repos](https://github.com/RWIN5666)

See also the list of [contributors](https://github.com/RWIN5666/Poll-Filler/graphs/contributors) who participated in this project.

## License

I'm thinking about licensing the project... But I don't know which one yet. Feel free to make a pull request to suggest a license. 