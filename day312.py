# Place msg="You can't add int to string" to the right place so that program avoids BaseExceptionError.
#
# You can use except Exception although normally you should be careful using such powerful exception statements.


a = "Hello World!"

try:
    a + 10
except Exception:
    msg = "You can't add int to string"

print(msg)