import easyocr

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext('xp.png', detail=0)

print(result)
