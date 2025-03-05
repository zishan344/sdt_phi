from django.core.exceptions import ValidationError

def validate_file_size(file):
  """This validator validate if file size is less then 10 mb"""
  max_size = 50
  max_size_bytes = max_size * 1024 * 1024
  if file.size > max_size_bytes:
    raise ValidationError(f"File can not be larger then {max_size} MB:")