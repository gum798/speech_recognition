import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('a.wav')
with harvard as source:
    audio = r.record(source)
    print('google')
    # for i in range(0,60):
    print(r.recognize_google(audio, language='ko-KR'))
    # print('bing')
    # print(r.recognize_bing(audio, language='ko-KR'))
    # print('google_cloud')
    # print(r.recognize_google_cloud(audio, language='ko-KR'))
    # print('houndify')
    # print(r.recognize_houndify(audio, language='ko-KR'))
    # print('ibm')
    # print(r.recognize_ibm(audio, language='ko-KR'))
    # print('sphinx')
    # print(r.recognize_sphinx(audio, language="ko-KR", keyword_entries=None, show_all=False))
    # print('wit')
    # print(r.recognize_wit(audio, language='ko-KR'))
