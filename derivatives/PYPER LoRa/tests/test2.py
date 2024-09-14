import sys
import tools

try:
    f = 1/0
except Exception as e:
    tools.log_exc(e)