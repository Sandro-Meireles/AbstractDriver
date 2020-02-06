# AbstractDriver

### early warning

It is very likely that you will need to install selenium dependencies to run all of the codes mentioned below. [how to install selenium](https://pypi.org/project/selenium/).

## Start easily

```py
driver = AbstractDriver('https://exampleurl.com')
driver.start()
```

## we recommend that you inherit the AbstractDriver class

```py
from abstract import AbstractDriver

class MyDriver(AbstractDriver):
    pass

```

## Goal

my goal is to transform this project into a framework specialized in web bots and data scraping, i intend to merge ```beautifulsoup4``` and ```selenium``` in an abstract way, both are great libraries and joining them would result in a very powerful framework

By: SandroSF
