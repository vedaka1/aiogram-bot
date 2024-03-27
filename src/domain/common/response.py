from dataclasses import dataclass

from aiogram import md

from domain.common.base import BaseValueObject


@dataclass
class Response(BaseValueObject):
    value: str

    def validate(self):
        self.value = md.unparse(self.value)
        self.value = self.value.replace(r"\`\`\`", "```")

    def as_generic_type(self):
        return str(self.value)
