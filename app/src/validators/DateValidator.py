from wtforms import ValidationError
from datetime import date
import re

from app.src.utilities.logger import logger

class DateValidator():

    def __call__(self, form, field):


        input_date = field.data

        if input_date.year < 1900:
            raise ValidationError("Year has to be bigger than 1900")

        if date.today() < input_date:
            raise ValidationError("Are you from the future?")

