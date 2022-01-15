import re
import long_responses as long


def message_1 (user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def cek_message (message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_1 (message, list_of_words, single_response, required_words)

    response('hallo!', ['halo','hallo', 'hay', 'hey', 'p', 'cek'], single_response=True)
    response('aku masih belajar,coba tanyakan sesuatu', ['bisa', 'lakukukan'], single_response=True)
    response('aku dari planet strelitza', ['asal', 'darimana', 'rumah'], single_response=True)
    response('aku adalah jarbot ?', ['siapa', 'apakah' , 'nama', 'namamu'], single_response=True)
    response('Ya, sama sama', ['terimakasih', 'thanks','makasih'], single_response=True)
    response('apa yang ingin kamu tanyakan?', ['punya', 'ingin', 'tanya','bertanya','pertanyaan'], single_response=True)
    response('aku suka makan manusia', ['makanan','kesukaan','kesukaanmu','apa','suka'], single_response=True)
    response('usiaku masih 24 jam', ['berapa', 'usia','usiamu','umur'], single_response=True) 
    response('aku tinggal di sebuah komputer', ['tinggal', 'dimana','tempat'], required_words=['kamu','tinggal'])
    response('terimakasih ya', ['membantu', 'bagus', 'sangat','wah','menarik'], single_response=True)
    response('Sipp!! :)', ['sama-sama', 'sama', 'oke','baik','ok','okay'], single_response=True)
    response('doge udah bisa buat beli mobil tesla!! :)', ['menarik', 'hal', 'sebutkan','apa','berita','terkini'], single_response=True)

    response(long.R_saran, ['sakit', 'obat','apa','dokter'], single_response=True)
    response(long.R_makan, ['makanan', 'enak', 'saran', 'beri','hari'], single_response=True)
    response(long.R_pantun, ['pantun', 'puisi', 'menarik', 'beri','punya','nyanyi','lagu'], single_response=True)


    best_match = max(highest_prob, key=highest_prob.get)
    return long.unknown() if highest_prob[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = cek_message (split_message)
    return response

while True:
    print('Bot: ' + get_response(input('You: ')))