import re
s = "<div class='allen'><span id='1'>邓伦</span></div>"

obj = re.compile(r"<div class='.*?'><span id='.*?'>(?P<mingzi>.*?)</span></div>")
result = obj.finditer(s)
for it in result:
    print(it.group("mingzi"))
