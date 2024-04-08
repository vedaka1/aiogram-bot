import logging
from dataclasses import dataclass, field


@dataclass
class Foo:
    logger: logging.Logger = field(default_factory == logging.getLogger())
    bar: int = 1

    def test(self):
        self.logger.error("test")


test = Foo()
print(test.test())
