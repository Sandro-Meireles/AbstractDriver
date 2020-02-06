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

By: SandroSF
