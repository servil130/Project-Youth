import json
import subprocess

prologue_translations = [
    # 0 - 9
    "Cahaya temaram dari lampu belajar membiaskan bayangan di atas meja.",
    "Pendar hangat kekuningan menyelimuti seisi ruangan, menciptakan rasa nyaman di tengah dinginnya malam yang mulai merayap di luar.",
    "Jantungmu berdegup kencang saat jemarimu menyentuh permukaan laptop yang terbuka.",
    "Detak dada yang berdebar kencang menggema tatkala jemarimu meluncur di atas permukaannya yang sejuk dan mulus.",
    "Suara ketukan tuts keyboard yang berirama memecah keheningan malam.",
    "Saat matamu menelusuri isi layar, kamu membiarkan dirimu terhanyut semakin dalam.",
    "Kursormu melayang di atas tombol refresh, rasa tak sabar terpancar dari sedikit getaran di ujung jemarimu.",
    "Di setiap klik, rasa antisipasi terasa begitu pekat di udara, begitu mendebarkan.",
    "Tepat ketika kamu hendak menyegarkan laman web itu sekali lagi, sebuah bunyi \"ting!\" tiba-tiba membuatmu terperanjat.",
    "Suara itu menggema di ruangan yang hening bagaikan sinyal dari dunia lain.",
    
    # 10 - 14
    "Oh, ini pesan dari sekolah yang kemarin aku daftarin...",
    "Kamu membuka ponselmu dengan penuh rasa antusias...",
    "Kamu menggulir pesan demi pesan... Jantungmu berdegup semakin kencang saat layar ponsel menyala terang.",
    "Tertulis bahwa kamu dinyatakan diterima di sekolah ini. Rasa lega, bangga, dan semangat membuncah membayangkan masa depan.",
    "Yes! Berhasil! Aku beneran diterima!",
    
    # 15 - 23
    "Dua bulan kemudian…",
    "Semilir angin berhembus pelan, membuat helai rambutmu bergerak bergelombang.",
    "Langkah sepatumu berderap di atas tanah saat kamu melangkah dengan rasa gugup bercampur antusias menuju gedung sekolah barumu.",
    "Hari ini menandai hari pertamamu resmi menjadi siswa di SMK Raden Umar Said.",
    "Melangkah semakin dalam ke area sekolah, deretan gedung megah berwarna merah dan abu-abu menjulang di depanmu, memancarkan kesan modern dan penuh semangat.",
    "Udara dipenuhi riuh energi para siswa dan orang tua yang berlalu-lalang, mengobrol, dan menurunkan perlengkapan.",
    "Tawa riang dan derap langkah kaki mengisi suasana, mengingatkanmu bahwa kamu tidak sendirian di sini.",
    "Setiap orang yang kamu temui menyiratkan campuran rasa cemas dan antusias yang serupa, siap memulai perjalanan baru mereka di masa sekolah ini.",
    "Semua ini berasa kayak mimpi…",
    
    # 24 - 30
    "Kamu memeriksa papan pengumuman di depan lobi, mencari informasi lebih lanjut.",
    "Semakin banyak orang mulai berkerumun di sekitar papan; kamu berusaha menyusup ke tengah kerumunan untuk membacanya.",
    "Setelah diperhatikan lebih dekat, tampak deretan nama yang terbagi ke dalam beberapa kelompok gugus.",
    "Setelah semenit mencari-cari, akhirnya kamu menemukan namamu sendiri.",
    "[[Gugus 01: 1. [player_name]]",
    "Kamu menghela napas panjang, mencerna informasi penting itu baik-baik di kepala.",
    "Dengan tekad untuk tidak melupakan kelompokmu, kamu melangkah lebih jauh ke area dalam gedung sekolah.",
    
    # 31 - 45
    "Mengikuti arahan panitia, kamu bergegas menuju barisan kursi yang tertata rapi di lapangan sekolah.",
    "Di tengah riuh suara pengumuman bahwa upacara akan segera dimulai, kamu terburu-buru mencari tempat duduk yang telah ditentukan.",
    "Kamu duduk bersama teman-teman satu gugusmu.",
    "Saat akhirnya bisa duduk di bangkumu, helaan napas lega meluncur dari bibirmu.",
    "Ketegangan yang sempat menumpuk sejak pertama kali tiba di gedung sekolah perlahan menguap.",
    "Pundakmu sedikit turun saat tubuhmu mulai merasa lebih rileks.",
    "Udara di sekitarmu dipenuhi simfoni obrolan hangat para siswa baru.",
    "Hawa hangat di dalam tenda yang padat membuat butir-butir keringat perlahan mengalir di punggungmu.",
    "Dengan lirikan perlahan, kamu menyadari ada seseorang seusiamu yang duduk tepat di sebelahmu.",
    "Matanya berbinar penuh semangat saat ia memandang berkeliling tenda, menikmati atmosfer yang begitu hidup.",
    "Kilau jingga terang dari manik matanya berkilau bak senja hari, menarik perhatianmu.",
    "Rambut cokelatnya memantul berirama seiring gerak tubuhnya yang tak bisa diam karena antusias.",
    "Sosoknya yang penuh energi begitu kontras dengan dirimu yang tenang dan diam.",
    "Tepat saat kamu menatapnya sepersekian detik terlalu lama, suara lantang terdengar memecah keriuhan.",
    "Suara itu seketika menarik perhatian seisi ruangan.",
    
    # 46 - 54
    "Selamat pagi semuanya!",
    "Udah pada sarapan belum nih?",
    "Kelihatannya energinya masih pada belum terisi penuh, ya!",
    "Itu salah satu kakak panitia OSIS. Nada bicaranya tegas namun ramah, membelah kebisingan tenda dengan begitu luwes.",
    "Ya sudah kalau begitu...",
    "Selamat datang, adik-adik siswa baru di SMK Raden Umar Said!",
    "Tepuk tangan meriah langsung membahana memenuhi ruangan, bagai gelombang sorak yang mendorongmu untuk ikut bertepuk tangan.",
    "Kamu tak kuasa menahan debar semangat kerumunan saat suasana mulai bergerak dinamis.",
    "Hanyut bersama teman-teman seangkatanmu saat upacara pembukaan resmi dimulai.",
    
    # 55 - 66
    "Selama beberapa jam berikutnya, rangkaian upacara pembukaan berlangsung dengan lancar dan apik.",
    "Setiap sesinya dirancang untuk mengenalkan semangat dan budaya sekolah kepada para siswa baru.",
    "Spanduk warna-warni berkibar pelan di atas kepala.",
    "Presentasi ceria dari berbagai klub dan ekstrakurikuler mengisi udara dengan obrolan yang seru.",
    "Namun di tengah ramainya suasana, pikiranmu perlahan melayang melamun, hanya mendengarkan setengah hati seiring berjalannya waktu.",
    "Waktunya istirahat! Sekali lagi, sudah waktunya istirahat!",
    "Bagi yang membawa bekal dari rumah, silakan dinikmati sekarang.",
    "Tapi buat yang mau ke kantin sekolah, stan TeddyCup, atau RB Mart, semuanya juga sudah buka buat kalian!",
    "Keriuhan kembali pecah saat para siswa serempak beranjak dari tempat duduk mereka.",
    "Semua bersemangat menikmati jeda kebebasan dan mencicipi berbagai pilihan jajanan yang menanti.",
    "Perutmu mulai terasa berkeroncongan saat orang-orang di sekitarmu mulai menyebar dan mengeluarkan kotak bekal mereka.",
    "Pikiranmu sempat bimbang sejenak sebelum akhirnya kamu memutuskan untuk...",
    
    # 67 - 89 (Trida Lunch Route)
    "Kamu tetap duduk di situ, perlahan membuka kotak bekal birumu yang berhiaskan stiker kelinci yang kamu gambar waktu kecil.",
    "Aroma gurih dan segar dari sandwich buatan rumah langsung menggelitik hidungmu.",
    "Sebelum sempat mengambilnya, kamu merasakan ada sepasang mata yang diam-diam melirik ke arahmu.",
    "Kamu mengerjap saat melihat sosok yang tadi rupanya sedang menatap makananmu dengan tatapan terpana.",
    "Sadar sedang diperhatikan, ia langsung mengalihkan pandangannya sepenuhnya ke arahmu.",
    "Matanya seketika berbinar penuh rasa antusias saat kamu melontarkan pertanyaan itu.",
    "Kilaunya mengingatkanmu pada permata yang berkilau di bawah sinar mentari, seolah baru saja menemukan harta karun berharga.",
    "Beneran nih?!",
    "Kamu melirik sejenak ke arahnya, merasakan desiran hangat melihat antusiasmenya yang begitu spontan.",
    "Lalu, kamu menatap kembali kotak bekal di depanmu, warnanya yang cerah tampak begitu menggugah selera.",
    "Perlahan, seolah terhipnotis oleh binar matanya, kamu menganggukkan kepalamu.",
    "Pandanganmu kembali ke arahnya, di mana cahaya ceria tampak berpendar indah di matanya.",
    "Campuran antara rasa penasaran dan kehangatan yang membuat hatimu berdesir pelan.",
    "Makasih banyak ya...!",
    "Kamu juga boleh kok ambil bekalku!",
    "Ia tersenyum ceria seraya menunjukkan kotak bekal miliknya.",
    "Nasi goreng yang tampak lezat bertabur telur dadar yang matang sempurna membuat perutmu semakin berbunyi.",
    "Mungkin karena kamu memang lapar, tapi itu adalah nasi goreng paling menggoda yang pernah kamu lihat.",
    "Oh, makasih! Ngomong-ngomong, namaku [player_name]. Senang kenal sama kamu.",
    "Sosok itu tersenyum lebar seraya menggeser duduknya sedikit lebih dekat.",
    "Kamu bisa panggil aku Trida, [player_name]. Salam kenal juga ya!",
    "Pertemuan sederhana itu menjadi percikan awal yang manis di sekolah baru ini.",
    "Kalian berdua lanjut mengobrol asyik sambil menikmati makan siang, saat benih pertemanan pertama mulai tumbuh bersemi.",
    
    # 90 - 92 (Trida Lunch Bad)
    "Kamu perlahan memalingkan pandangan dan mendekap kotak bekalmu lebih rapat ke tubuhmu.",
    "Orang itu sempat tertegun sejenak, lalu perlahan kembali memfokuskan perhatian pada kotak bekalnya sendiri.",
    "Keheningan canggung tercipta di antara kalian berdua. Mungkin setelah ini kamu hampir tidak akan pernah berinteraksi lagi dengannya.",
    
    # 93 - 118 (Radit TeddyCup Route)
    "Kamu bangkit dari kursi dan melangkah keluar dari tenda.",
    "Banyak siswa berlalu-lalang seperti barisan semut, sama-sama mencari pengisi perut kosong.",
    "Tanpa ragu lagi, langkah kakimu berbelok menuju salah satu stan makanan yang ramai dikerumuni siswa baru.",
    "Papan nama besar terpampang jelas di atas stan: \"Teddy Cups\".",
    "Kayaknya aku harus coba ini deh.",
    "Sebelum sempat memesan, tubuhmu mendadak oleng karena tersenggol bahu seseorang.",
    "Eits, hati-hati dong...",
    "Matamu melirik ke samping dan menatap sosok pemuda yang barusan menyenggolmu.",
    "Lupa ikat tali sepatu ya, sobat?",
    "Eh, iya...",
    "Hmm, pantesan aja. Emang tanah di sini ramah banget sampai mau dipeluk.",
    "Ucapnya diiringi tawa renyah yang memberi kehangatan pada nada bicaranya.",
    "Ia tampak begitu luwes dan ramah, aura hangat terpancar dari ekspresinya saat ia perlahan mendekat.",
    "Kenalin, aku Radit. Salam kenal ya...?",
    "Ia sengaja menggantung suku kata terakhirnya, memberi jeda agar kamu bisa memperkenalkan diri.",
    "Aku [player_name]. Salam kenal juga, Radit.",
    "Kamu menyambut uluran tangannya, saling berjabat tangan singkat yang tak terduga.",
    "Jadi, kamu mau ikutan antre?",
    "Ia mengangkat sebelah alisnya, membuatmu sadar kalau antrean di stan makin panjang sementara kamu belum juga masuk barisan.",
    "Iya juga ya. Aku harus buru-buru antre nih!",
    "Kamu baru saja hendak melangkah ke barisan saat tersadar kalau meninggalkan Radit begitu saja terasa kurang sopan.",
    "Kamu nggak mau ikutan beli makan juga?",
    "Santai aja, aku udah kenyang kok. Selamat antre ya.",
    "Ia menepuk pelan pundakmu sebelum melangkah pergi. Pandanganmu terus mengikuti langkah Radit sampai ia menjauh.",
    "Kamu sempat bertanya-tanya apakah ia satu jurusan denganmu, tapi kamu segera tersadar kembali ke kenyataan.",
    "Beberapa siswa sudah kembali membawa pesanan mereka—dan kamu sendiri bahkan belum sempat memesan apa-apa.",
    
    # 119 - 121 (Radit Bad)
    "Tanpa mengucap sepatah kata pun, kamu membalikkan badan meninggalkan pemuda tenang itu dan mencari stan lain untuk menepi.",
    "Dari sudut matamu, sekilas kamu melihat senyum santai di wajahnya perlahan memudar menjadi kerutan kecil.",
    "Meskipun sudah kabur ke stan sebelah, hawa canggung barusan masih terasa membekas di udara.",
    
    # 122 - 151 (Chie Bathroom Route)
    "Kamu bangkit dari tempat dudukmu, mengikuti arus kerumunan yang melangkah keluar.",
    "Riuh suasana membuat keinginanmu mencari toilet terasa semakin mendesak, memaksamu untuk segera bergegas.",
    "Kamu berhenti sejenak, baru menyadari betapa luasnya area sekolah ini.",
    "Matamu memandang ke sekeliling, menoleh ke kanan dan ke kiri mengamati lingkungan sekitar.",
    "Sebelum sempat menentukan arah mana yang harus dituju, sebuah tepukan pelan mendarat di bahumu, membuatmu agak terlonjak kaget.",
    "Pandanganmu langsung tertuju pada helaian rambut bernuansa kuning keemasan yang cerah bagaikan kelopak bunga dandelion.",
    "Kamu terpaku saat melihat seorang gadis berwajah ceria berdiri tepat di hadapanmu.",
    "Hai! Kamu nyasar ya?",
    "Dengan raut geli nan jenaka, ia tersenyum ramah seraya menatapmu dengan gerak-gerik yang luwes.",
    "Santai aja kali! Semua orang pasti ngalamin hal kayak gini di hari pertama.",
    "Ia meraih tanganmu, genggamannya lembut namun mantap, menyalurkan rasa hangat dan ramah.",
    "Sini, kuantar ke toilet. Kenalin, namaku Chie ya!",
    "Kamu hampir tak sempat menjawab saat gadis itu langsung menarikmu melangkah bersamanya. Energi Chie benar-benar tak terbendung.",
    "Rasanya baru melangkah beberapa langkah, tiba-tiba kalian berdua sudah sampai tepat di depan deretan bilik toilet.",
    "Tadaa! Udah sampai nih!",
    "Ia merentangkan kedua tangannya dengan gaya dramatis; kamu sampai hampir lupa kalau tempat yang ditunjukkannya ini cuma toilet.",
    "Yaah, emang nggak keren-keren amat sih. Tapi hei, toilet yang ini jauh lebih mending dibanding yang di sebelah sana...",
    "Anggap aja... yang di sana aromanya lumayan bikin merem melek.",
    "Ia menoleh ke arahmu dengan senyum usil di bibirnya. Tawa kecil meluncur saat memperhatikan postur tubuhmu yang masih kaku.",
    "Makasih banyak ya, eh... Chie.",
    "Sama-sama! Eh iya, tadi aku belum sempat nanya namamu!",
    "Kamu terdiam sejenak. Chie ternyata orang yang sangat baik dan ramah.",
    "Mungkin ia tampak lincah seperti kelinci yang melompat ke sana kemari, tapi ia hanyalah sosok gadis yang penuh semangat hidup.",
    "Namaku [player_name]. Sekali lagi makasih banyak bantuannya ya, Chie.",
    "Salam kenal kalau gitu, [player_name]!",
    "Tiba-tiba, suara pengumuman terdengar sayup-sayup menyapa telingamu.",
    "Itu pasti tanda kalau waktu istirahat sebentar lagi berakhir. Chie menepuk ringan punggungmu.",
    "Kayaknya aku juga harus buru-buru balik nih. Semangat ya!",
    "Kamu melambaikan tangan ke arahnya seraya memperhatikan langkah riangnya yang berlari dan menghilang di balik tikungan.",
    "Kamu tersenyum, berharap suatu saat nanti kalian berdua bisa bertemu lagi.",
    
    # 152 - 163 (Chie Bad)
    "Kamu hanya membalas singkat dan datar, lalu segera berbalik pergi.",
    "Oh...",
    "Ekspresi cerianya seketika lenyap, menyisakan gurat kekecewaan di wajahnya.",
    "Ia memainkan jemarinya seraya mengalihkan pandangannya dari jari ke arah wajahmu.",
    "Ah, maaf ya kalau lancang. Aku cuma khawatir kamu bingung aja tadi.",
    "Keheningan canggung yang menyesakkan menggantung di antara kalian berdua.",
    "Y-ya udah deh, semangat ya...",
    "Ia memaksakan senyum tipis di bibirnya.",
    "Sudut mulutnya berkedut sedikit, seolah berusaha keras menahan rasa tidak nyaman yang tiba-tiba datang.",
    "Kamu hanya membalas dengan anggukan pelan, sengaja menjaga ekspresimu tetap datar, lalu melangkah pergi.",
    "Rasa canggung dari momen barusan terasa terus membayangi langkahmu bagaikan bayangan gelap.",
    "Rasa malu yang begitu dalam, yang rasanya bakal terus membekas di ingatanmu untuk waktu yang lama.",
    
    # 164 - 165 (MPLS End)
    "Sisa hari MPLS berlalu cepat dalam balutan sesi perkenalan, games seru, dan hangatnya suasana sekolah yang mulai menemukan ritmenya.",
    "Saat langkah kakimu akhirnya membawamu pulang ke rumah, benih pertama dari babak baru ini telah tertanam—dan tahun ajaran baru baru saja dimulai.",
]

menu_translations = {
    "Please enter your name:": "Silakan masukkan namamu:",
    "I'll just eat my lunch box": "Makan bekal sendiri saja",
    "Maybe we can check out the TeddyCup stall?": "Mungkin kita bisa cek stan TeddyCup?",
    "I'm not that hungry, but I might go to the bathroom": "Aku nggak terlalu lapar, tapi mau ke toilet dulu",
    "Do you want some?": "Kamu mau coba?",
    "Silently ignore them": "Diam saja dan abaikan",
    "Yes... The ground calls for me, you see.": "Iya... Soalnya tanahnya manggil-manggil aku barusan.",
    "Did not answer and walk away": "Tidak menjawab dan langsung melangkah pergi",
    "Not really, I just... need the bathroom": "Nggak juga kok, aku cuma... butuh ke toilet",
    "No. Thank you": "Tidak. Terima kasih"
}

with open('/tmp/prologue.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

dialogue_idx = 0
for item in items:
    if item['type'] == 'dialogue':
        if dialogue_idx < len(prologue_translations):
            item['indonesian'] = prologue_translations[dialogue_idx]
            dialogue_idx += 1
    elif item['type'] == 'string':
        eng = item['english']
        if eng in menu_translations:
            item['indonesian'] = menu_translations[eng]

with open('/tmp/prologue.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Updated prologue.json: translated {dialogue_idx} dialogues and {len(menu_translations)} menu strings.")
subprocess.run(['python3', 'tools/translate_helper.py', 'apply', 'game/tl/indonesian/prologue_mpls.rpy', '/tmp/prologue.json'], check=True)
