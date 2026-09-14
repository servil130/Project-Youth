import json
import subprocess

week1_translations = [
    # 0 - 8
    "Langkah kakimu kembali membawamu ke gedung-gedung megah ini. Rasanya begitu melegakan setelah seminggu penuh kegiatan MPLS akhirnya usai.",
    "Para siswa sudah ramai bercengkerama, membicarakan pembagian kelas yang baru saja diumumkan.",
    "Jantungmu berdebar saat akhirnya langkahmu tiba di depan pintu kelas barumu.",
    "Dengung pendingin ruangan memenuhi seisi ruangan, membuat dinding-dinding terasa dingin dan kaku saat matamu memandang berkeliling.",
    "Suasana kelas terasa agak tegang, semua orang tampak canggung dan tenggelam dalam pikiran masing-masing.",
    "Kamu melangkah masuk, menghirup aroma ruangan yang masih asing. Setelah memperhatikan beberapa bangku yang kosong, akhirnya kamu memilih tempat duduk.",
    "Kamu memilih duduk di barisan depan, tepat di bawah pandangan papan tulis.",
    "Kamu mengambil bangku di barisan tengah, dikelilingi riuh obrolan teman-teman sekelasmu.",
    "Kamu memilih bangku di sudut belakang, tempat di mana kamu bisa mengamati seluruh sudut kelas.",
    
    # 9 - 19
    "Sebuah suara tiba-tiba menarik perhatianmu, nadanya yang familier terngiang di telingamu.",
    "Kamu menoleh dan mendapati helaian rambut cokelat yang sama seperti saat kegiatan MPLS kemarin. Sepasang mata beriris oranye senja itu sudah terpatri jelas di ingatanmu.",
    "Hai!",
    "Jaaadi… kita beneran sekelas ya?",
    "Ia tersenyum, memperlihatkan cengiran dan deretan gigi yang belum pernah kamu lihat sebelumnya.",
    "Ingatanmu tentang dirinya yang serba canggung kini berganti menjadi sosok yang tampak lebih ceria dan percaya diri.",
    "Wah, kebetulan banget ya!",
    "Kamu baru saja hendak membalas saat suara derap langkah kaki membuatmu terdiam.",
    "Sosok yang kamu kenali sebagai wali kelasmu melangkah masuk ke dalam kelas.",
    "Duduk semuanya.",
    "Suara derit kursi yang digeser dan bunyi meja yang beradu memecah keheningan yang tersisa, menciptakan gema yang memantul di dinding.",
    
    # 20 - 32 (Sit beside nice)
    "Beberapa bangku mulai terisi, para penghuninya bergerak gelisah saat menyesuaikan posisi duduk. Kamu melirik ke arah Trida yang masih berdiri tegak di samping mejamu.",
    "Itu gurunya udah masuk kan ya?!",
    "Ia melirik ke arahmu, matanya membelalak panik dengan sedikit rasa cemas.",
    "Boleh nggak aku duduk di sebelahmu?",
    "Iya, boleh banget!",
    "Beneran?! Makasih banyak ya!",
    "Kamu mengangguk mantap saat Trida bergegas menarik kursi dan duduk di bangku tepat di sebelahmu.",
    "Ia menatapmu dengan senyum lebar penuh binar bahagia, persis seperti anak kecil yang baru saja dihadiahi permen lezat!",
    "Makasih banyak ya, aku berutang budi nih sama kamu.",
    "Ucapannya meluncur cepat dengan nada yang tulus. Kamu membalas senyumnya tepat saat guru di depan berdeham pelan.",
    "Kamu mencuri pandang lagi ke arah Trida, dan tatapan kalian bertemu sejenak.",
    "Percikan kehangatan mengalir di antara kalian, menimbulkan sensasi geli yang menjalar dari ujung kaki hingga ke ujung kepala.",
    "Rasanya bagaikan kembang api mungil meletup indah di benakmu, menyinari debar menyenangkan di momen itu.",
    
    # 33 - 38 (Sit beside bad)
    "Eh, gimana ya… Maaf, kayaknya bangku ini udah ada yang nempatin deh.",
    "Kamu menggigit bibir bawahmu, kebiasaan gugup yang membocorkan rasa cemasmu.",
    "Sorot mata Trida seketika meredup, menyiratkan rasa kecewa saat ia berusaha bersikap tenang dan mencari bangku lain yang tersisa.",
    "Namun sang guru sudah keburu berdeham, membuatnya panik hingga akhirnya tetap duduk terpaksa di bangku sebelahmu.",
    "Maaf ya, tadi aku udah nggak sempat nyari tempat lain…",
    "Ucapnya dengan senyum kecut, kekecewaan tampak jelas di raut wajahnya.",
    
    # 39 - 49
    "Apakah semuanya sudah hadir hari ini?",
    "Keheningan melanda seisi kelas saat para siswa menahan diri untuk tidak bersuara.",
    "Bapak cek kehadirannya dulu ya.",
    "Beliau lalu memanggil nama siswa satu per satu, menanyakan nama panggilan masing-masing.",
    "Saat giliranmu tiba, kamu berdiri dan memperkenalkan nama panggilan serta asal daerahmu.",
    "Setelah absensi selesai, beliau memaparkan tata tertib kelas, metode pengajaran, serta pentingnya pembelajaran interaktif.",
    "Sekian dari Bapak, sekarang kalian boleh istirahat dulu. Nanti kumpul lagi di sini, karena Bapak akan memberikan gambaran singkat mengenai kurikulum dan materi kita.",
    "Wali kelasmu melangkah keluar dari kelas, meninggalkanmu yang menghela napas panjang di bangkumu.",
    "Mau ke mana ya sekarang?",
    "Mungkin jalan-jalan keliling sekolah bentar seru juga.",
    "Melihat sekeliling, kamu sadar beberapa siswa sudah berhamburan keluar. Dengan langkah mantap, kamu melangkah keluar menghirup udara segar.",
    
    # 50 - 68 (Radit Grapos)
    "Menyusuri jalan setapak yang sudah tak asing, kamu mendapati dirimu tiba di lapangan terbuka tempat kamu mengikuti MPLS tempo hari.",
    "Di kejauhan, gedung bertuliskan 'Grapos' tampak menjulang kokoh, fasad tuanya menjadi saksi bisu perjalanan waktu. Ilalang tinggi bergoyang lembut diterpa semilir angin.",
    "Halo, [player_name].",
    "Kamu berbalik saat mendengar namamu dipanggil. Sosok yang sudah familier berjalan santai menghampirimu, menepuk ringan pundakmu.",
    "…?",
    "Kamu mengangkat kedua alismu sementara ia terkekeh pelan.",
    "Masa udah lupa sama namaku? Aku tahu kamu sering kesandung sesuatu, tapi ingatanmu jangan ikutan kesandung dong.",
    "Sekarang kita sekelas lho, jadi… mau akrab kan, sobat?",
    "Radit menatapmu dengan raut geli seraya mendengus pelan, menyelipkan sebelah tangannya ke saku celana.",
    "Langsung to the point ke negosiasi ya? Boleh juga.",
    "Oke, deal. Tapi jangan protes kalau aku yang ngambil camilan yang lebih enak ya.",
    "Radit memiringkan kepalanya, matanya yang tenang menatap lurus ke arahmu.",
    "Standar yang… cukup rendah ya.",
    "Setelah terdiam sejenak, tawa renyah meluncur pelan dari bibirnya.",
    "Tapi boleh lah. Hidup damai itu awal yang bagus.",
    "Hening sejenak sebelum kamu melihatnya mengangguk pelan, menyunggingkan seringai tipis di bibirnya.",
    "Berarti kita bakal sering barengan nih ke depannya.",
    "Ngomong-ngomong, kayaknya kita harus balik ke kelas sekarang deh.",
    "Kamu mengacungkan jempol ke arah kelas. Kalian berdua berjalan santai berdampingan kembali ke ruangan dan duduk di bangku masing-masing.",
    
    # 69 - 91 (Chie Studio)
    "Mungkin jalan-jalan keliling sekolah bentar seru juga.",
    "Kamu beranjak dari tempat dudukmu dan melangkah menuju pintu, keluar menghirup udara segar.",
    "Gedung studio animasi berdiri megah di bawah terik sinar matahari yang memancarkan hawa hangat di udara.",
    "Saat mengamati sekeliling, secercah semangat baru menyelimuti dirimu.",
    "Halo halo! Apa kabar nih?",
    "Seorang gadis berambut pirang keemasan panjang berdiri hanya dua meter di depanmu, senyum cerahnya menyinari wajahnya.",
    "Penuh energi, ia langsung meraih kedua tanganmu dan mengguncangnya dengan antusias.",
    "Kamu nggak lupa kan sama aku… Aku Chie lho, Chie!",
    "Jangan gampang lupa ya! Soalnya aku sering sibuk magang proyek, jadi agak khawatir orang-orang gampang ngelupain aku...",
    "Mendengar jawabanmu, pundaknya tampak rileks, rasa cemasnya seketika mencair.",
    "Beneran?! Kamu masih ingat?",
    "Aaa, seneng banget dengernya! Sumpah tadi aku udah overthinking duluan.",
    "Nggak usah khawatir soal itu kali. Tapi kedengarannya kamu sibuk banget ya?",
    "Iya nih… Akhir-akhir ini agak hectic banget jadi anak kelas sebelas, tapi seru juga kok. Terus kalau kamu butuh bantuan apa-apa, tanya aja ke aku ya!",
    "Yeeay!! Tuh kan, bener!",
    "Ia memekik girang, berjingkrak-jingkrak dengan tumitnya persis seperti kelinci yang lincah.",
    "Tuh kan, aku emang gampang diingat, ya nggak?",
    "Iya, bener banget kok. Terus… gimana magangnya sejauh ini?",
    "Jujur akhir-akhir ini lumayan padat sih… Tapi tenang aja, kalau kamu butuh bantuan apa pun, bilang aja ke aku!",
    "Oh! Iya juga ya, berarti aku ini seniormu dong?",
    "Tenang aja, aku senior yang baik kok! Kalau kamu butuh bantuan, kamu bisa banget ngandalin aku!",
    "Makasih banyak ya, Chie. Ngomong-ngomong, kayaknya kita harus balik ke kelas sekarang.",
    "Kamu memberi isyarat ke arah kelas. Ia melambaikan tangan saat kamu melangkah kembali dan duduk di bangkumu.",
    
    # 92 - 121 (Class lesson & pop quiz)
    "Kayaknya aku mendingan di kelas aja deh.",
    "Sebagian besar teman sekelas sudah keluar ruangan. Kamu duduk santai sambil membuka ponsel, mengisi waktu istirahat.",
    "Cahaya matahari menembus jendela, menciptakan pendar hangat di dalam kelas.",
    "Keheningan yang melingkupi kelas terpecahkan saat wali kelasmu masuk kembali dan mulai memperkenalkan materi Animasi 3D.",
    "Animasi 3D mengambil objek digital dan membuatnya tampak hidup dengan menciptakan ilusi bahwa objek tersebut bergerak dalam ruang tiga dimensi.",
    "Objek-objek buatan komputer ini memang tampil di layar dua dimensi, namun dirancang mengikuti prinsip-prinsip dunia 3D; bisa bergerak, berputar, dan berotasi layaknya benda di dunia nyata.",
    "Trida masih asyik mencoret-coret buku catatannya, menggambar sketsa sambil menjulurkan lidahnya sedikit—gambar kucing dan anjing yang saling bergandengan tangan.",
    "Kamu yang di sana…",
    "Masih fokus sama pelajaran Bapak?",
    "Teguran tiba-tiba itu membuat seisi kelas langsung menolehkan pandangan ke arah Trida.",
    "Eh-iya. Iya, Pak!",
    "Bisa tolong jelaskan ke Bapak, apa fungsi dari Animasi 3D?",
    "Fungsinya…",
    "Ia ragu-ragu, bola matanya melirik cemas ke sudut-sudut ruangan sebelum tatapan kalian berdua bertemu.",
    "Antena rambutnya tampak bergoyang-goyang, seolah sedang mengirimkan sinyal telepati meminta bantuanmu.",
    "Jadi, Animasi 3D itu…",
    "Animasi 3D bikin objek digital kelihatan bergerak di ruang 3D nyata, meskipun kita cuma ngelihatnya di layar datar.",
    "Kamu berbisik pelan ke arahnya. Trida mengerjapkan matanya berkali-kali sebelum membalas dengan senyum kikuk.",
    "Animasi 3D itu intinya ngasih kehidupan ke benda digital—kayak, 'ayo gerak, muter sana-sini'.",
    "Biar kelihatan hidup di dunia 3D nyata, padahal aslinya cuma tampil di layar datar.",
    "Penjelasan yang sangat sederhana dan tepat sasaran.",
    "Pak guru menyunggingkan senyum tipis sebelum melanjutkan penjelasan, sementara Trida melirikmu dengan seringai cerah.",
    "Ia sengaja mencondongkan tubuhnya ke arahmu.",
    "Makasih banyak ya!",
    "Animasi 3D itu bercerita lewat gambar yang digerakkan di bidang datar, frame demi frame, baik manual maupun komputer.",
    "Kamu berbisik pelan ke arahnya. Trida menolehkan kepalanya menghadap ke pak guru.",
    "Animasi 3D itu kayak membolak-balik segepok gambar dengan cepat, jadi gambarnya kelihatan bergerak dan bercerita di layar datar.",
    "Jawaban itu kurang tepat. Itu adalah prinsip dari teknik animasi 2D.",
    "Pak guru menjelaskan lebih lanjut materinya, meninggalkan Trida yang melirikmu sambil menggigit bibir dengan raut wajah pasrah.",
    "Nggak apa-apa kok, jangan dipikirin ya…",
    
    # 122 - 150 (After school & iced tea)
    "Hari itu, waktu terasa bergulir begitu cepat. Pak guru memberikan materi dasar yang masih cukup mudah dipahami oleh pemula.",
    "Menjelang siang, rasa lega menyelimuti dirimu saat kelas akhirnya selesai. Teman-teman mulai merapikan barang-barang ke dalam tas, begitu pula dirimu.",
    "Kamu merasakan seseorang melangkah mendekati mejamu.",
    "Hei, um… makasih ya buat yang tadi.",
    "Bukan bantuan yang seberapa juga kok!",
    "Bukan masalah besar kok, santai aja.",
    "Nggak usah terlalu dipikirin…",
    "Yah, mau bener atau salah, kamu tetep udah berusaha bantuin aku tadi.",
    "Trida berdiri semakin dekat, kehangatan dirinya menyelimutimu bagai selimut nyaman, memantik debar menyenangkan di udara.",
    "Sebenernya tadi agak lucu sih… Waktu aku ketahuan ngelamun… konyol banget kan ya?",
    "Haha iya, tadi emang lumayan bikin ngakak sih.",
    "Kalian berdua tertawa lepas, mengenang momen kuis dadakan yang tak terduga tadi.",
    "Ngomong-ngomong, gara-gara tegang tadi, aku jadi pengen banget minum es teh nih.",
    "Trida menatap lantai sambil memainkan dasinya, melirik dari sudut matanya menunggu reaksimu.",
    "Kebetulan hari ini emang agak gerah sih, jadi…",
    "Gimana kalau kita jajan minuman segar?",
    "Yuk, kita beli bareng-bareng!",
    "Untuk sesaat, kamu merasakan genggaman tangan Trida di pergelangan tanganmu, menarikmu penuh semangat menuju stan Teddy Cup.",
    "Area sekolah sudah mulai sepi karena sebagian besar siswa sudah pulang ke rumah.",
    "Kamu dan Trida duduk di dekat stan dan memesan dua gelas es teh manis dingin.",
    "Sambil menunggu pesanan, kalian berdua asyik mengobrol tentang materi hari ini dan membicarakan kurikulum tiga tahun ke depan.",
    "Jujur ya, waktu tadi guru nyinggung soal Tugas Akhir di kelas dua belas? Aku malah agak excited lho. Maksudku—sesusah apa sih emangnya?",
    "Bisa jadi jauh lebih berat dari yang kita bayangin lho.",
    "Mungkin malah lebih gampang dari dugaan kita?",
    "Menurutku peluangnya masih fifty-fifty sih buat sekarang.",
    "Semilir angin berdesir di sekeliling kalian, menerbangkan helai rambut dalam tarian bebas, sementara suara gemersik dedaunan terdengar renyah.",
    "Saat Trida menghela napas perlahan, raut wajahnya tampak begitu tenang dan teduh, seolah sedang hanyut dalam lamunan yang indah.",
    "Yah, bagaimanapun nanti jalannya, aku berharap kita bisa satu tim.",
    "Pasti bakal seru banget kalau bareng kamu.",
    
    # 151 - 161 (Night thoughts & part-time job)
    "Kamu baru saja tiba di kamarmu dan menghela napas perlahan.",
    "Tas sekolahmu tergeletak di kursi sementara kamu merebahkan tubuh di atas kasur yang empuk.",
    "Langit-langit kamarmu terasa lebih lapang, dan dadamu dipenuhi rasa hangat dari aktivitas hari ini, terutama karena sekarang kamu sudah punya teman.",
    "Lalu kamu teringat—ada sesuatu yang sudah lama ingin kamu coba begitu masuk SMK. Mungkin bisa buat nambah uang jajan sehari-hari.",
    "Kayaknya seru juga kalau ambil kerja sambilan.",
    "Tapi kerjaan apa yang cocok ya?",
    "Kedengarannya gampang dan lumayan buat nambah uang jajan.",
    "Mungkin kamu bakal menikmati suasana kafe yang tenang dan nyaman.",
    "Wadah yang pas buat menyalurkan kreativitas—pasti seru banget.",
    "Dengan keputusan yang sudah mantap di kepala, kamu memejamkan mata dan membiarkan lelahnya minggu pertama larut ke dalam tidur lelap.",
    "Tanpa terasa, minggu baru di sekolah pun segera dimulai...",
]

week1_menus = {
    "Sit at the front of the class": "Duduk di barisan depan kelas",
    "Sit in the middle of the class": "Duduk di barisan tengah kelas",
    "Sit at the back of the class": "Duduk di sudut belakang kelas",
    "Let them sit beside you": "Bolehkan ia duduk di sebelahmu",
    "Ask them to sit anywhere else": "Minta ia mencari bangku yang lain",
    "Go to Grapos": "Pergi ke gedung Grapos",
    "Go to RUS Animation Studio": "Pergi ke Studio Animasi RUS",
    "Stay at the Class": "Tetap diam di dalam kelas",
    "Only if there's a binding snack-sharing agreement involved.": "Boleh, asal ada perjanjian wajib bagi-bagi camilan ya.",
    "I mean… I don't fight people usually, so… that counts as getting along, right?": "Maksudku… aku biasanya nggak suka cari ribut, jadi… itu udah termasuk akrab kan?",
    "Yeah, sure. We'll be seeing each other a lot anyway, so might as well get along.": "Iya, tentu. Lagian kita bakal sering ketemu, mendingan saling akrab aja.",
    "Hey, I remember you, of course. You're not that easy to forget!": "Hei, tentu saja aku masih ingat! Kamu kan nggak gampang dilupakan!",
    "Of course I remember you!": "Tentu saja aku ingat kamu!",
    "Chie, right? About that internship… then you are my senior?": "Chie, kan? Soal magang tadi… berarti kamu ini seniorku ya?",
    "Give them the right answer": "Berikan jawaban yang benar",
    "Gave them the wrong answer": "Berikan jawaban yang keliru",
    "It's not that much of a help tho!": "Bukan bantuan yang seberapa kok!",
    "That was not a big deal": "Bukan masalah besar, santai aja",
    "Don't bother it much…": "Nggak usah terlalu dipikirin…",
    "I mean, it's kind of hot today, so…": "Maksudku, hari ini lumayan gerah sih, jadi…",
    "Should we buy something to drink?": "Gimana kalau kita jajan minuman segar?",
    "It could be worse than we thought": "Bisa jadi jauh lebih berat dari yang kita bayangkan",
    "Maybe it was easier than we imagined?": "Mungkin malah lebih gampang dari dugaan kita?",
    "I think it was still fifty-fifty for now": "Menurutku peluangnya masih fifty-fifty untuk sekarang",
    "Be an Indoapril Cashier": "Menjadi kasir minimarket Indoapril",
    "Work as a barista at a cafe": "Bekerja sebagai barista di kafe",
    "Open a commission or a merchandise store": "Buka jasa komisi gambar atau toko merchandise"
}

with open('/tmp/week1.rpy.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

dialogue_idx = 0
for item in items:
    if item['type'] == 'dialogue':
        if dialogue_idx < len(week1_translations):
            item['indonesian'] = week1_translations[dialogue_idx]
            dialogue_idx += 1
    elif item['type'] == 'string':
        eng = item['english']
        if eng in week1_menus:
            item['indonesian'] = week1_menus[eng]

with open('/tmp/week1.rpy.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Updated week1.rpy.json: {dialogue_idx} dialogues, {len(week1_menus)} menus.")
subprocess.run(['python3', 'tools/translate_helper.py', 'apply', 'game/tl/indonesian/week1.rpy', '/tmp/week1.rpy.json'], check=True)
