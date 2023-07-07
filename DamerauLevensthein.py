def damerau_levenshtein_distance(s1, s2):
    # İki boş string arasındaki mesafe 0'dır
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    
    # İki stringin de uzunluğunu alıyoruz
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    # Mesafeyi hesaplamak için bir matris oluşturuyoruz
    dist = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
    # İlk satırı ve sütunu başlangıç değerleriyle dolduruyoruz
    for i in range(len_s1 + 1):
        dist[i][0] = i
    for j in range(len_s2 + 1):
        dist[0][j] = j
    
    # Damerau-Levenshtein mesafesi hesaplamak için dinamik programlama yöntemini kullanıyoruz
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dist[i][j] = min(dist[i - 1][j] + 1,            # Silme
                             dist[i][j - 1] + 1,            # Ekleme
                             dist[i - 1][j - 1] + cost)     # Değiştirme
            
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                dist[i][j] = min(dist[i][j], dist[i - 2][j - 2] + cost)  # Transpozisyon
    return dist[len_s1][len_s2]
while True:
    ilk=input("First word:")
    ikinci=input("Second word:")

    print("Distance between two words:",damerau_levenshtein_distance(ilk,ikinci))

    if(ilk=="0" or ikinci==0):
        break
