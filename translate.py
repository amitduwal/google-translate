from googletrans import Translator

translator = Translator()
# 
translations = translator.translate('धनगढी — सुदूरपश्चिममा मुख्यमन्त्री नियुक्ति एवं सरकार गठन गर्ने प्रक्रिया सोमबारसम्म अन्योलमै छ। आइतबार नागरिक उन्मुक्ति पार्टीकै दुई सांसदले बेग्लाबेग्लै समूह र समर्थक जुटाएर मुख्यमन्त्रीमा दाबी पेस गरेपछि प्रदेश प्रमुख नजिर मियाँले मुख्यमन्त्री नियुक्ति प्रक्रियालाई थाती नै राखेका छन्।', dest='hi')

print(translations)
# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)