import numpy as np
import pandas as pd

# CSV dosyasının yolunu belirleyin
file_path = 'ilmesafe.csv'

# CSV dosyasını yükleyin
data = pd.read_csv(file_path, encoding='iso-8859-9')

# Mesafeleri bir sözlük yapısına dönüştürün
distances = data.set_index('İL ADI').to_dict('index')

# Tüm iller arasında mesafe matrisini oluştur
def uzaklik_matrisi_hesapla(distances):
    cities = list(distances.keys())
    n = len(cities)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i, j] = distances[cities[i]][cities[j]]
            else:
                D[i, j] = float('inf')
    return D, cities

# GSP maliyet hesaplama fonksiyonu
def maliyet(rota, D):
    return sum(D[rota[i - 1], rota[i]] for i in range(len(rota)))

# 2-Opt iyileştirme fonksiyonu
def iki_opt(rota, D):
    def swap(rota, i, j):
        new_rota = rota[:i] + rota[i:j + 1][::-1] + rota[j + 1:]
        return new_rota

    def iki_opt_maliyet_hesapla(rota, D):
        return maliyet(rota, D)

    m = len(rota)
    en_iyi_rota = rota
    en_iyi_maliyet = maliyet(rota, D)

    iyilesme_var_mi = True
    while iyilesme_var_mi:
        iyilesme_var_mi = False
        for i in range(1, m - 1):
            for j in range(i + 1, m):
                yeni_rota = swap(en_iyi_rota.tolist(), i, j)
                yeni_maliyet = iki_opt_maliyet_hesapla(yeni_rota, D)
                if yeni_maliyet < en_iyi_maliyet:
                    en_iyi_rota = np.array(yeni_rota)
                    en_iyi_maliyet = yeni_maliyet
                    iyilesme_var_mi = True
    return en_iyi_rota, en_iyi_maliyet

# Kullanıcıdan başlangıç şehri isteme ve doğrulama
def get_starting_city(cities):
    while True:
        start_city = input("Lütfen bir başlangıç noktası seçin: ").strip().upper()
        if start_city in cities:
            return start_city
        else:
            print("Yanlış şehir ismi. Lütfen tekrar deneyin.")

# Main program
def main():
    D, cities = uzaklik_matrisi_hesapla(distances)

    start_city = get_starting_city(cities)
    start_index = cities.index(start_city)

    m, n = D.shape
    xD = np.copy(D)
    xD[np.isinf(xD)] = 0

    row_sum = np.sum(xD, axis=1)
    M = xD / row_sum[:, None]
    M[M == 0] = 1

    Z = np.copy(M)
    rota_mx = np.zeros(m, dtype=int)
    t = 0
    ss = start_index

    visited = set()
    while t < m:
        bx = np.argmin(Z[ss])
        while bx in visited:
            Z[ss, bx] = np.inf
            bx = np.argmin(Z[ss])
        rota_mx[t] = bx
        visited.add(bx)
        Z[:, bx] = np.inf
        ss = bx
        t += 1

    maliyet_tsp = maliyet(rota_mx, D)
    iki_opt_rota, iki_opt_maliyet = iki_opt(rota_mx, D)

    # Rota şehirlerini virgülle ayrılmış şekilde yazma
    rota_sehirler = [cities[i] for i in iki_opt_rota]
    with open('rota.txt', 'w', encoding='utf-8') as f:
        f.write(",".join(rota_sehirler))

    print("Önerilen yöntemin GSP maliyeti:", maliyet_tsp)
    print("Geliştirilen Rota:", rota_sehirler)
    print("GSP'nin Yeni Maliyet:", iki_opt_maliyet)

    input("Devam etmek için bir tuşa basın...")

if __name__ == '__main__':
    main()
