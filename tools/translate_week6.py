import json
import subprocess

week6_translations = [
    # 0 - 10 (Grapos festival crowd & Trida cheering)
    "Suasana di Grapos membuncah dengan luapan antusiasme dan energi yang membara.",
    "Dentuman musik menggelegar ke seluruh penjuru dengan ketukan bas yang berdenyut kencang, menghantarkan getaran gelombang hingga ke tanah yang kamu pijak.",
    "Lautan penonton bergerak serempak bagai ombak yang bergelora, berayun mengikuti irama dengan spanduk-spanduk warna-warni yang berkibar tinggi di atas kepala.",
    "Aroma gorengan yang gurih, semerbak keringat, dan samar wangi pita plastik murah dari stan piala berbaur di udara seiring membumbungnya semangat ratusan siswa.",
    "Kamu berdiri di area khusus peserta, meregangkan kedua lengan sembari berupaya menenangkan detak jantungmu yang berdegup kencang.",
    "Kompetisi sebentar lagi akan dimulai, dan saat pandanganmu menyapu keriuhan tribun penonton mencari secuil ketenangan, sesuatu mendadak menarik perhatianmu.",
    "Seseorang terlihat melompat-lompat girang, gerakannya begitu lincah dan bersemangat seolah kakinya melayang tanpa menyentuh lantai.",
    "Di sanalah Trida, wajahnya berseri-seri penuh antusias saat meloncat-loncat di atas bangku, menjadi pusat perhatian yang begitu mencolok di barisan paling depan.",
    "Tubuhnya praktis bergetar saking hebohnya, memicu sorak-sorai dari penonton lain; setiap jengkal raganya larut dalam kobaran euforia saat itu.",
    "WOI [player_name]!",
    "LIHAT KE SINI!",

    # 11 - 19 (Player responds: play along or stay focused)
    "Kamu tak kuasa menahan tawa. Perhatianmu beralih sepenuhnya ke arahnya, lalu kamu memasang pose pahlawan yang konyol nan dramatis—satu tangan di pinggang dan tangan lainnya menunjuk ke angkasa laksana protagonis anime klasik.",
    "Trida benar-benar lepas kendali. Ia berteriak semakin histeris, dan teman-teman di sampingnya ikut melompat-lompat heboh membuat kegaduhan, melebur menjadi satu gemuruh suara riuh bagai arena mosh pit.",
    "Kamu begitu terhanyut dalam aksi pamer itu, mengacungkan pose dua jari seraya mengedipkan mata ke arahnya, sampai-sampai hampir tak mendengar suara juri yang berdeham di depan mikrofon.",
    "Kamu memaksa diri menatap lurus ke depan dengan rahang mengeras. Fokusmu tertuju ke podium, berusaha keras menepis suara teriakan Trida yang memekakkan telinga.",
    "SEMANGAT! ITU SAHABAT TERBAIKKU TUH!",
    "Trida berteriak lantang seolah sedang menonton pertandingan kejuaraan dunia.",
    "Tepat saat hitungan mundur mencapai angka satu, kamu tak tahan untuk tidak melirik sekilas dan melemparkan senyum tipis yang tertahan ke arahnya.",
    "Saat rona merah padam menjalar cepat di kedua daun telinganya begitu ia sadar kamu melihatnya, ia langsung merunduk kikuk, tampak malu bukan main.",
    "Juri melangkah maju ke mikrofon utama di tengah panggung lalu berdeham membersihkan tenggorokannya. Suasana penonton seketika senyap.",

    # 20 - 32 (Trivia questions & responses)
    "Baiklah! Para peserta, silakan ambil posisi masing-masing. Kita akan menguji wawasan umum kalian. Peserta pertama yang meraih tiga poin berhak membawa pulang hadiahnya!",
    "Apa nama sungai terpanjang di dunia, yang kerap menjadi perdebatan antara dua kandidat utama dari benua Afrika dan Amerika Selatan?",
    "Jawaban salah!",
    "Tepat sekali!",
    "Jawaban salah!",
    "Proses apa yang dimanfaatkan oleh tumbuhan untuk mengubah energi cahaya menjadi energi kimia, yang secara efektif bertindak sebagai paru-paru bumi?",
    "Tepat sekali!",
    "Jawaban salah!",
    "Jawaban salah!",
    "Siapakah cendekiawan polimatik ikonis asal Italia yang melukis Mona Lisa dan kerap dinobatkan sebagai lambang puncak manusia Renaisans?",
    "Jawaban salah!",
    "Tepat sekali!",
    "Jawaban salah!",

    # 33 - 42 (Win branch: flowers)
    "Pembawa acara langsung melemparkan buket bunga besar tepat ke dalam pelukanmu.",
    "Buket itu sangat besar dan agak norak dengan aroma khas toko bunga yang menyengat hidung.",
    "Kamu menuruni panggung dan melihat Trida melambaikan tangannya penuh semangat ke arahmu, raut wajahnya berbinar bagai baru saja menyaksikan sebuah mukjizat.",
    "Serius deh, megang bunga segede ini berasa lagi megang properti film Hollywood di tanganku...",
    "Kedua tanganmu masih sedikit gemetar akibat ketegangan menjawab trivia barusan, namun pemandangan bunga-bunga itu tak ayal memantik kehangatan emosi di dadamu.",
    "Lagipula, kamu sama sekali tak menyangka bisa melewati babak final tanpa kesalahan fatal ataupun pikiran yang mendadak kosong melompong.",
    "Kamu sempat meneliti buket bunga itu lamat-lamat, lalu mengarahkan tatapanmu lekat-lekat pada Trida.",
    "Ia tampak begitu gembira dan bangga, seolah sedang menahan diri antara ingin menangis haru atau meledakkan tepuk tangan meriah.",
    "Perasaan hangat dan lembut mengalir menyelimutimu saat mengingat bagaimana Trida selalu menjadi sandaran andalanmu selama beberapa pekan terakhir, membantumu melewati saat-saat sulit.",
    "Jujur saja, kemenangan ini terasa kurang berarti tanpa kehadirannya. Kupikir bunga-bunga indah ini lebih cocok kuberikan padanya sebagai hadiah karena sudah menjadi pemandu sorakku yang konyol selama ini.",

    # 43 - 56 (Lose branch: buzzer, Trida comforts under bleachers)
    "Bel penanda berbunyi nyaring, dan semuanya berakhir—kamu kalah.",
    "Peserta yang menang mulai mengangkat buket bunganya tinggi-tinggi dan merayakan selebrasi. Kamu bahkan enggan untuk meliriknya sedikit pun.",
    "Kamu hanya terpaku menatap lantai, merasa begitu payah atas apa yang baru saja terjadi. Kamu melakukan kesalahan konyol pada pertanyaan yang sebenarnya kamu tahu persis jawabannya.",
    "Mendadak, sebuah sorakan lantang terdengar dari tepi lapangan. Kamu mendongak.",
    "Kamu melihat Trida berjinjit di atas ujung kakinya, melambaikan kedua tangannya ke udara sambil mengacungkan dua jempol besar ke arahmu. Wajahnya memerah terang, tampak sedikit konyol namun menggemaskan.",
    "Nggak apa-apa kok! Kamu udah keren banget!",
    "Kamu tahu betul ia sedang berusaha keras menghiburmu dari kejauhan. Ia tak ingin kamu terpuruk sedih hanya karena sebuah kekalahan.",
    "Ia menatapmu, terdiam sedetik, lalu tertawa hangat penuh keakraban.",
    "Sumpah deh, aku bener-bener berutang budi banyak sama anak itu.",
    "Ia tak menunggu kamu berjalan menghampirinya. Dengan lincah ia berlari kecil, berkelit di antara kerumunan yang mulai menyusut.",
    "Rambutnya berantakan diterpa hawa lembap. Pipinya merona merah karena sedari tadi berteriak kencang menyemangatimu. Energinya tampak meluap-luap.",
    "Ia menyodorkan segelas teh dingin kepadamu dan memegang sikumu lembut untuk menuntunmu berteduh di bawah naungan tribun penonton.",
    "Penampilanmu tadi keren banget tahu. Nggak usah dipikirin skornya. Yuk, duduk dulu sebentar. Mukamu udah pucat kayak mau pingsan gitu.",
    "Makasih ya...",

    # 57 - 69 (Snack under bleachers & intimacy thoughts)
    "Udara di bawah tribun beraroma rumput segar, berpadu dengan harum masakan yang terbawa angin dari kantin di dekat situ.",
    "Kamu mendudukkan diri di bangku panjang. Rasanya sangat melegakan bisa mengistirahatkan kedua kakimu yang pegal.",
    "Trida merogoh sebuah kantong kertas dari saku hoodie-nya, lalu membukanya perlahan.",
    "Kamu melihat jajanan favoritmu di dalamnya, namun bentuknya sudah agak remuk dan berantakan. Menyadari kamu memperhatikannya, daun telinga Trida seketika bersemu merah muda.",
    "Aku tahu bentuknya udah hancur berantakan. Tadi aku kelaparan pas nungguin kamu selesai tanding. Maaf ya... kelihatannya udah nggak menarik lagi kan?",
    "Maksudmu gimana? Kelihatan enak banget begini kok!",
    "Udah deh diam, makanan seenak ini masa diprotes.",
    "Nggak usah dipikirin, ini camilan paling mantap sedunia.",
    "Kamu mengambil satu gigitan dari jajanan itu. Masih hangat dan gurih, rasa bumbunya terasa begitu nikmat di lidah.",
    "Sembari kamu mengunyah, kebisingan dari arah lapangan perlahan mulai memudar. Penonton di luar masih riuh, namun kamu menyadari bahwa Trida kini terdiam tenang.",
    "Ia tak lagi memandangi lapangan ataupun siswa-siswa lain. Tatapannya terpaku lurus menatapmu lekat-lekat, menghadirkan atmosfer yang terasa berbeda. Tak seperti saat kalian sekadar mengobrol santai di kelas.",
    "Orang bilang kedekatan lahir dari waktu yang dihabiskan bersama, tapi aku merasa ada sesuatu yang jauh lebih dalam—sebuah ikatan batin yang hanya dimengerti oleh dua pasang mata di lorong ini lewat bahasa tanpa kata.",
    "Dulu saat ia pertama kali hadir, aku terlalu sibuk berkutat dengan rasa cemas hingga tak menyadari bahwa perlahan ia telah menjadi sosok terdekat dalam hidupku—",

    # 70 - 89 (Concert starts, Trida grabs wrist, romantic song)
    "Saat grup band sekolah mulai menghentakkan instrumen mereka dengan penuh gairah, dentuman nada mengalun menyelimuti sekeliling bagai gelombang yang mendebarkan.",
    "Musik menggelegar dengan intensitas yang begitu dahsyat, dentuman basnya berdegup begitu dalam hingga beresonansi menembus udara dan menggetarkan tanah di bawah kaki.",
    "—Kini, aku merasakan kehadirannya di setiap hal kecil yang ia lakukan, dari makanan yang ia bawakan, bantuannya di kelas, hingga tiap lambaian tangan riangnya yang menyatakan betapa bersyukurnya ia bisa mengenalku.",
    "Trida menolehkan pandangannya ke arah panggung utama, dan matanya seketika berbinar cerah. Tanpa ragu, ia mengulurkan tangannya dan menggenggam erat pergelangan tanganmu.",
    "Live music-nya udah mulai tuh, ayo buruan!",
    "E—eh tunggu, Trida!",
    "Ayo cepet, nanti kita kelewatan lagunya!",
    "Sebuah sengatan hangat menjalar saat kulitnya menyentuh tanganmu. Bagai percikan listrik yang merambat naik dari lengan hingga menembus rongga dadamu.",
    "Itu bukan sekadar sentuhan biasa. Terasa sekali betapa eratnya ia ingin menggenggam dan membawamu bersamanya. Saat ia menarikmu bangkit berdiri, lututmu mendadak terasa lemas. Jantungmu berpacu kencang.",
    "Langkah kakimu sempat tersandung canggung ke depan, gamang apakah rasa berdebar ini karena entakan irama musik atau karena kehangatan genggaman tangannya.",
    "Trida terus melangkah menembus padatnya lautan siswa hingga tubuhnya larut tertelan kerumunan, tempat di mana kamu memperhatikan segalanya dari balik pundaknya.",
    "Kalian berdua terhimpit rapat dari segala arah, nyaris tanpa ada sisa ruang untuk bernapas lega. Kerumunan itu bergoyang pelan, dan sesaknya dekapan orang banyak ditambah hentakan musik yang menggelegar seolah menciptakan dinding pelindung yang mengisolasi dunia luar.",
    "Untuk sekejap, terasa seakan hanya ada kalian berdua di dunia ini.",
    "Hentakan lagu mendadak berhenti sejenak dalam jeda hening yang menumpuk di telingamu, sebelum sang vokalis utama berdiri tegak dan melantunkan bait lirik yang begitu indah sekaligus memilukan ke udara.",
    "Jantungmu serasa berhenti berdetak saat menyadari bahwa lagu itu pastilah sebuah lagu cinta—mungkin sebuah ungkapan perasaan yang tulus, sebab alunan suara sang vokalis terdengar seolah sedang berbicara langsung kepadamu.",
    "Ya ampun... kenapa harus lagu ini yang diputar...",
    "Nuansa romantisnya begitu blak-blakan hingga kamu merasa seolah lagu itu sedang disuarakan terang-terangan kepada seluruh isi sekolah.",
    "Benakmu seketika memutar kembali rentetan momen berharga beberapa bulan terakhir—bagaimana ia selalu membawakanmu makanan, menunggumu pulang, dan menatapmu seolah kamu adalah satu-satunya orang di dunia ini.",
    "Trida mencondongkan tubuhnya merapat ke arahmu, kehangatan pundaknya bergesekan lembut dengan bahumu saat ia berbicara menembus bisingnya alunan musik.",
    "Keren banget ya vokalisnya. Cara dia nyanyi bener-bener kedengeran tulus banget... Jujur dari hati, paham kan maksudku.",

    # 90 - 109 (Under concert lights, accidental bump, tension)
    "Ia menoleh kepadamu, sepasang matanya memantulkan kilau ribuan cahaya lampu sorot panggung yang berpendar di atas kepala, berpijar hangat dan berkelebat ke segala arah.",
    "Untuk beberapa saat, kamu terpaku tak berdaya oleh pancaran tatapan matanya yang begitu mempesona.",
    "Tatapan itu seolah menembus langsung ke dalam sanubarimu, dan ketulusan nada bicaranya membuat setiap kata-kata itu terdengar seakan terucap langsung dari bibirnya, bukan dari vokalis di atas panggung.",
    "Rasanya... kayak pengin terdengar personal banget ya?",
    "Iya. Jujur banget liriknya. Malah mungkin terlalu jujur, menurutmu nggak sih?",
    "Ya ampun. Itu... itu ngena banget. Bener-bener nyentuh ke perasaan.",
    "Kamu mengamati wajahnya lamat-lamat, merekam setiap perubahan ekspresi lembut yang terlukis di parasnya.",
    "Ia masih berada begitu dekat, sangat dekat hingga hembusan napasnya terasa, menatap ke arah panggung sambil bersenandung kecil mengikuti irama lagu dengan senyum manis yang tersungging tipis di bibirnya.",
    "Bisa jadi sih. Nggak tahu ya, tapi rasanya lega banget bisa dengerin sesuatu yang bener-bener tulus sesekali, ya kan?",
    "Sebelum kamu sempat menyahut, tubuh kalian berdua kembali terombang-ambing oleh gelombang dorongan orang-orang di sekitar.",
    "Band itu lanjut memainkan lagu kedua dengan tempo yang menghentak penuh dinamika, sementara sang vokalis kembali melantunkan balada kerinduan yang begitu syahdu.",
    "Kamu begitu tak menyadari desakan kerumunan di sampingmu, hingga mendadak tubuh Trida terdorong keras dan menabrakmu dari samping hingga membuatmu kehilangan keseimbangan.",
    "Aduh, maaf! Maaf banget, beneran maaf kerumunannya lagi heboh banget dorong-dorongan!",
    "Wajahnya merona terang saat meminta maaf dengan tulus, memperlihatkan raut kaget seraya buru-buru bergeser memberi ruang dan merapikan posisinya.",
    "Permainan musik mereka keren banget ya? Gitarnya itu lho... lagunya bener-bener indah banget! Musik yang luar biasa...",
    "Jantungku berdegup kencang banget menghantam tulang rusuk, sampai-sampai aku takut suaranya bakal kedengeran jelas nembus alunan musik.",
    "Konyol banget rasanya. Tadi itu cuma senggolan biasa, cuma ketidaksengajaan. Tapi kenapa hawa di sini mendadak terasa begitu panas membara. Aku sampai bingung mau buang pandangan ke mana, serba salah harus naruh tanganku di mana...",
    "Trida berdeham pelan seraya menoleh kembali ke arahmu, jemarinya melayang ragu tepat di atas ujung lengan bajumu.",
    "Ketika nada terakhir memudar diiringi tepuk tangan membahana dari para penonton, lampu sorot seketika berganti dari lembayung temaram menjadi cahaya putih terang benderang, memecahkan magisnya suasana.",
    "Grup band mulai mengemasi instrumen di panggung seiring bisingnya obrolan grup penampil berikutnya yang menenggelamkan sisa musik, membiarkan desau ketegangan manis antara kamu dan Trida tetap menggantung lembut di udara.",

    # 110 - 134 (Under the tree, giving flowers)
    "Langkah kaki kalian berdua menyusuri jalan pulang dalam keheningan, ditemani desau gesekan dedaunan yang meredam riuhnya sisa keriuhan festival sekolah.",
    "Kalian berdua akhirnya tiba di bawah naungan sebatang pohon rindang, menghadirkan sudut dunia yang terasa begitu sunyi dan privat, seolah hanya milik kalian berdua.",
    "Kamu dan Trida berdiri di balik rindangnya keteduhan dahan pohon itu, saling berhadapan satu sama lain.",
    "Kamu merapikan tangkai-tangkai buket bunga itu untuk terakhir kalinya sebelum mengulurkannya melintasi jarak dekat di antara kalian berdua.",
    "Kamu menarik napas panjang untuk memantapkan hatimu.",
    "Hei Trida, ini buat kamu...",
    "Kamu sendiri kaget mendengar betapa lembut dan lirihnya nada suaramu terdengar.",
    "Aku serius kok. Aku sendiri nggak begitu suka nyimpen barang beginian... jadi bunganya pasti bakal jauh lebih berharga kalau dikasih ke orang yang bener-bener menghargainya.",
    "Trida menoleh menatap bunga-bunga itu dengan ekspresi keterkejutan yang begitu murni dan tanpa celah.",
    "Kedua matanya membelalak lebar, mengerjap-ngerjap cepat, dan untuk sesaat kamu sempat mengira ia akan menolak pemberian itu.",
    "Dengan ragu-ragu ia mengulurkan tangannya, menarik lembut pergelangan tanganmu mendekat sebelum menyentuh dan mengambil tangkai-tangkai bunga itu dari genggamanmu dengan sangat hati-hati.",
    "Kamu... ini kamu beneran serius?",
    "Trida bertanya pelan, suaranya sempat bergetar tertahan di ujung kalimat.",
    "Iya, buruan ambil sana.",
    "Kamu menyemangatinya dengan nada lembut, menuntun buket bunga itu bersandar di dadanya.",
    "Kamu memperhatikan bagaimana ia mendekap bunga-bunga itu dengan sentuhan yang begitu takzim dan hati-hati, sementara jemarinya terus bergetar sepanjang waktu.",
    "Ia menatap lekat-lekat kelopak-kelopak yang mekar itu, seluruh wajahnya merona merah padam, dan jemarinya memainkan pita hiasan di pangkuannya dengan salah tingkah.",
    "Ia tampak begitu menggemaskan sekaligus mempesona di saat yang bersamaan, dan kamu merasakan jantungmu berdegup liar tak keruan di dalam dada.",
    "Ia terlihat benar-benar bingung dan kehilangan kata-kata tentang apa yang harus ia lakukan pada buket bunga indah yang baru saja kamu hadiahkan untuknya.",
    "Ia menarik napas panjang, pundaknya sedikit terangkat, lalu ia mendongak menatap matamu hanya untuk sedetik kemudian buru-buru menunduk kembali menatap bunga-bunga di pelukannya.",
    "Ia tampak begitu tersentuh oleh perhatian tulusmu, begitu luruh dari sosoknya yang biasanya ceria dan berisik, hingga kamu merasa belum pernah melihatnya seindah ini seumur hidupmu.",
    "Aku...",
    "Trida tercekat lirih, tak mampu melanjutkan kata-katanya; ia hanya mengatupkan bibirnya rapat-rapat sebelum menyunggingkan senyuman manis nan tulus kepadamu.",
    "Rasa bahagia yang luar biasa meluap membuncah di dalam hatimu, melihat betapa ia begitu terpana dan tersentuh oleh pemberianmu.",
    "Ketenangan yang damai melingkupi keteduhan pohon itu saat keheningan lembut menyelimuti kalian berdua, seakan dunia sengaja berhenti berputar demi memberi Trida ruang ketenangan batin.",

    # 135 - 157 (Friends arrive, goodbye, tender closure)
    "Trida! Woi, ke sini! Dari tadi kita nyariin kamu tahu!",
    "Dua orang temannya tiba-tiba muncul dari balik sudut gedung olahraga, ponsel di tangan, sambil berteriak memanggil penuh semangat.",
    "Trida terlonjak kaget mendengar seruan mendadak itu, matanya membelalak kaget sembari mendekap erat buket bunganya di dada.",
    "Eh! U—um, halo semuanya...",
    "Lomba Radit udah mau mulai tuh. Yuk buruan kita nonton bareng!",
    "Uhm...",
    "Nggak apa-apa kok, susul aja mereka ke sana. Lagian sehabis ini masih ada urusan yang harus kuselesaikan...",
    "Beneran nih? Tapi...",
    "...beneran nggak apa-apa kok, Trida.",
    "Aduh ya ampun. Maaf ya, a—aku harus pergi dulu. Sampai ketemu lagi nanti ya.",
    "Iya, santai aja...",
    "Makasih banyak ya buat semuanya yang tadi... Sampai ketemu lagi nanti, maksudku—semoga kita bisa ketemu lagi secepatnya!",
    "Ia tak menunggu jawabanmu lebih lama; energi lincahnya yang tanpa batas langsung mendorong kakinya berlari kencang, mendekap erat buket bunga itu di dadanya laksana sebuah piala kemenangan berharga.",
    "Saat tubuhnya berbalik, sekilas raut bersalah melintas di wajahnya sebelum ia berlari kecil menghampiri teman-temannya, melemparkan satu tatapan perpisahan terakhir ke arahmu dengan pipi yang merona malu.",
    "Kamu melihatnya berbalik sekali lagi di kejauhan, memamerkan buket bunga cantiknya kepada teman-temannya yang pastinya diiringi bumbu cerita yang heboh.",
    "Salah satu temannya menyenggol jahil pinggang Trida, seringai usil merekah di wajah mereka seraya melirik ke arahmu, sementara Trida menundukkan kepala pura-pura malu.",
    "Saat mereka kembali melangkah menjauh, gelombang rasa hangat dan haru yang tak terduga menyapu lembut hatimu.",
    "Hari ini memang berakhir melelahkan setelah rentetan kompetisi yang panjang, namun di dalam hatimu terasa seolah baru saja terjadi sebuah keajaiban yang luar biasa.",
    "Sebuah ikatan manis yang terajut erat di antara kalian berdua, sesuatu yang akan membekas indah di ingatanmu untuk waktu yang sangat lama.",
    "Sembari jemarimu meraba pola-pola kasar di kulit kayu batang pohon itu, perasaan puas dan damai yang menyejukkan mengalir memenuhi rongga dadamu.",
    "Hari ini benar-benar hari yang indah. Bahkan mungkin hari terbaik yang pernah kualami setelah sekian lama.",
    "Matahari perlahan tenggelam di balik cakrawala, mewarnai langit senja dengan semburat ungu pekat dan nila yang memikat.",
    "Kenangan akan melodi musik, tawa riang, dan detik-detik keheningan yang manis itu terus terngiang hangat saat kamu akhirnya melangkahkan kaki pulang ke rumah."
]

week6_strings = {
    "Play along": "Ikuti gayanya",
    "Stay Focused": "Tetap fokus",
    "The Amazon River": "Sungai Amazon",
    "The Nile River": "Sungai Nil",
    "The Yangtze River": "Sungai Yangtze",
    "Photosynthesis": "Fotosintesis",
    "Respiration": "Respirasi",
    "Fermentation": "Fermentasi",
    "Michelangelo": "Michelangelo",
    "Leonardo Da Vinci": "Leonardo da Vinci",
    "Raphael": "Raphael",
    "What do you mean? It looks so good!": "Maksudmu gimana? Kelihatan enak banget begini kok!",
    "Oh shut up, look at those goodies": "Udah deh diam, makanan seenak ini masa diprotes.",
    "Don't mind it, it was the greatest thing ever": "Nggak usah dipikirin, ini camilan paling mantap sedunia.",
    "It feels… kinda want to sound personal, doesn't it?": "Rasanya... kayak pengin terdengar personal banget ya?",
    "Yeah. It's honest. Maybe a little too honest, don’t you think?": "Iya. Jujur banget liriknya. Malah mungkin terlalu jujur, menurutmu nggak sih?",
    "Yeah. It's honest. Maybe a little too honest, don't you think?": "Iya. Jujur banget liriknya. Malah mungkin terlalu jujur, menurutmu nggak sih?",
    "Geez. That’s—that’s really loud. Like, emotionally loud.": "Ya ampun. Itu... itu ngena banget. Bener-bener nyentuh ke perasaan.",
    "Geez. That's—that's really loud. Like, emotionally loud.": "Ya ampun. Itu... itu ngena banget. Bener-bener nyentuh ke perasaan."
}

with open("/tmp/week6.rpy.json", "r", encoding="utf-8") as f:
    items = json.load(f)

d_idx = 0
for item in items:
    if item["type"] == "dialogue":
        if d_idx < len(week6_translations):
            item["indonesian"] = week6_translations[d_idx]
            d_idx += 1
        else:
            print(f"Warning: more dialogues than translations at index {d_idx}")
    elif item["type"] == "string":
        eng = item["english"]
        if eng in week6_strings:
            item["indonesian"] = week6_strings[eng]

with open("/tmp/week6.rpy.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

subprocess.run(["python3", "tools/translate_helper.py", "apply", "game/tl/indonesian/week6.rpy", "/tmp/week6.rpy.json"], check=True)
print(f"Updated week6.rpy.json: {d_idx} dialogues, {len(week6_strings)} menus.")
