import ocrspace
api = ocrspace.API()
# Or if you have an API key or desired language, pass those:
api = ocrspace.API(open('ocr.key').read(), ocrspace.Language.Croatian)
# print(api.ocr_file('Capture.PNG'))
print(api.ocr_file('handouts/BITS_F311_1332.pdf'))