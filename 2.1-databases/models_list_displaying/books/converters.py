from datetime import datetime


class DateConverter:
   regex = r'[0-9]{2}-[0-9]{2}-[0-9]{4}'
   format = '%d-%m-%Y'

   def to_python(self, value: str) -> datetime:
       return datetime.strptime(value, self.format)

   def to_url(self, value: datetime) -> str:
       return value.strftime(self.format)
