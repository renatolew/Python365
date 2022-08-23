# This time write a regex to get only the part of the email before the "@" sign and include the "@" sign.
# i.e: only mike@ part from mike@protonmail.com

import re

str= 'The advancements in biomarine studies franky@google.com, with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'


regex = r'\S+@'
emails = re.findall(regex, str)


print(emails)