import random

R_makan = "aku punya beberapa saran nih, coba makan nasi uduk pake es batu, pasti enak deh"
R_saran = "kalau kamu sedang sakit segera periksa ke dokter aja ya"
R_pantun = "aku punya sebuah pantun menarik, coba dengerin. Aku dukung Korea Selatan,Kamu dukung Jepang, Walaupun kita mantan, Tapi aku masih tetap sayang."


def unknown():
    response = ["bisa ulangi lagi? ",
                "maaf aku ngga ngerti."][
        random.randrange(2)]
    return response