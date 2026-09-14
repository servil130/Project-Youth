import json
import subprocess

week10_translations = [
    # 0 - 9 (Afternoon finish, Trida waits)
    "Enak banget ya kamu udah beres semua tugasnya. Aku masih harus nyelesein materi buat presentasi nanti...",
    "Tenang aja, aku bakal nungguin kamu di sini kok!",
    "Kamu beneran nggak apa-apa nunggu? Bakal lumayan lama lho aku di dalam nanti.",
    "Santai aja napa! Lagian emang lagi pengin nongkrong lebih lama di sekolah kok. Aku bisa cari hiburan sendiri!",
    "Oh iya, ngomong-ngomong semangat ya presentasinya! Model karakter buatanmu tadi keren banget lho!",
    "Ini semua berkat bantuanmu juga tahu. Nggak tahu gimana caranya revisi yang kamu kasih bisa langsung pas gitu, tapi ajaibnya beneran berhasil.",
    "Ya jelas berhasil dong! Penjelasanku tadi kan tergolong detail banget!",
    "Detail bukan berarti gampang dipahami ya...",
    "Waduh, aku udah hampir telat nih. Nanti kita ngobrol lagi ya, Trida.",
    "Sampai nanti, [player_name]...!",

    # 10 - 20 (Trida's monologue, feelings, running to find friends)
    "Langkah kakimu beranjak menjauh menuju gedung sekolah, meninggalkan Trida seorang diri bersama lamunannya.",
    "Pikiran yang seketika melayang pada keinginan untuk menghabiskan waktu lebih lama bersamamu... merasakan kehangatanmu di momen-momen sunyi sehari-hari, dan melihatmu tersenyum.",
    "Duh, kamu ini...",
    "Trida menghembuskan napas gemetar, jantungnya berdegup kencang diliputi getaran rasa suka seraya daun telinganya memanas di balik rambut cokelatnya yang acak-acakan.",
    "Ia menatap nanar es teh di genggamannya, memperhatikan butir-butir embun dingin yang menetes di gelas plastik saat jemarinya memainkan sedotan.",
    "Nggak—ugh—nggak apa-apa, aku nggak apa-apa! Pokoknya... jujur aja ke dia! Tinggal omongin aja, dan kalau... kalau dia nolak...",
    "Nggak, nggak! Jangan mikir aneh-aneh! Tapi harus mulai dari mana ngomongnya?! Ya ampun...",
    "Trida mengakhiri gumaman panjangnya dengan rengekan lirih, rasa cemasnya membuncah menyadari betapa asingnya situasi seperti ini baginya.",
    "Melihat jam di ponselnya, masih ada beberapa jam tersisa sebelum kamu selesai presentasi.",
    "Ia butuh rencana matang. Saran dari seseorang yang sudah berpengalaman menghadapi hal semacam ini.",
    "Didorong tekad campur panik yang membara, Trida berlari kencang menyusuri lorong menuju deretan ruang kelas di lantai dua.",

    # 21 - 38 (Meeting Hizbul & Ilham playing games)
    "Mengintip dari balik salah satu jendela kelas, Trida melihat dua teman sekelasnya tengah asyik duduk berdua dengan stik kontroler di tangan, tenggelam dalam game di laptop bersama.",
    "Hizbul! Ilham!",
    "Astagfirullah! Sumpah ya, kukira tadi guru yang masuk!",
    "Maaf, maaf! Tadi suaraku rada kekencengan ya.",
    "Pfft, rada katamu? Kayaknya anak-anak yang lagi tidur di barisan belakang pada melek semua tuh.",
    "Tumben banget nih. Kita baru aja mulai mabar. Mau ikutan, Trida?",
    "Uhm, seru sih kelihatannya, tapi—",
    "Ayo lah, udah lama kita nggak main bareng kamu, Triguy! Masih banyak waktu luang nih.",
    "I—iya, paham! Nanti match berikutnya aku ikut, tapi tujuanku ke sini bukan buat mabar! Ada hal lain...",
    "Sebenarnya aku mau... minta pendapat kalian berdua soal sesuatu, kalau kalian nggak keberatan.",
    "Oh, gitu. Mau nanya soal apa emangnya?",
    "Uhm... bukan masalah gede sih sebenarnya. Cuma butuh—butuh sedikit saran aja!",
    "Oke deh... iya, kita coba bantu sebisa kita. Ada apa?",
    "Iya, tapi—kalian berdua harus janji dulu ya jangan sampai ngebocorin ini ke siapa pun, paham?!",
    "Katanya tadi 'bukan masalah gede', tapi kok mendadak jadi rahasia negara yang harus dijaga ketat?",
    "Lagian susah juga mau jaga rahasia kalau volume suaramu aja lebih kenceng dari seisi ruangan kelas.",
    "Aduh, masalahnya tuh... a—aku nggak tahu harus ngomongnya gimana...",
    "Tarik napas dulu, Trida. Tenangin pikiranmu pelan-pelan.",

    # 39 - 52 (Confession to Hizbul and Ilham)
    "Tangan Trida merogoh ke dalam saku, meremas-remas kain dengan gugup sembari menatap lantai.",
    "...Kalian berdua tahu [player_name] kan?",
    "Ya tahulah, kamu kan nempel mulu sama [player_name]. Emangnya kenapa sama dia?",
    "Uhm... mungkin ini kedengarannya bakal bikin kaget, tapi...",
    "Ya ampun, buruan to the point aja napa.",
    "Ilham, sabar sedikit...!",
    "Aku...",
    "...aku suka banget sama [player_name]!",
    "N—nah, akhirnya kuomongin juga!",
    "Hizbul dan Ilham saling bertukar pandang geli, sama sekali tidak terkejut.",
    "Oh iya, kudu pura-pura kaget nih—",
    "Wah, masa sih? Sumpah nggak bakal ada yang nyangka!",
    "I—iya, beneran... mengejutkan banget lho!",

    # 53 - 64 (Friends roasting Trida for being obvious)
    "Ih, kalian malah ngeledek aku kan...!",
    "A—ayolah, masa kelihatan sejelas ITU sih gelagatku?",
    "Iya lah, Bro, jelas banget nggak ada obat.",
    "Maksudku, sinyal-sinyalnya udah kebaca dari kapan tahu.",
    "Kan bukan berarti gara-gara aku sering bareng dia doang! Kalian berdua juga nempel terus tiap hari tapi nggak ada yang heboh tuh!",
    "Ya bedalah, nggak kayak kamu sama [player_name], aku sama Hizbul kan nggak ngabisin tiap tarikan napas berduaan terus, ya nggak?",
    "Hahaha, lagian kamu pasti langsung bosen setengah mati sama aku.",
    "Amit-amit deh, ngebayanginnya aja aku ogah.",
    "Uh—i—iya sih, kuakui aku emang sering banget ngikutin [player_name] ke mana-mana... sampai sering jalan pulang bareng juga...",
    "Lagian kamu kelihatan jauh lebih rileks pas lagi bareng dia. Nggak tahu kamu nyadar apa nggak ya, tapi kamu tuh gampang banget cemas dan tegang, bahkan pas lagi bareng kita.",
    "Tapi pas lagi bareng [player_name], kamu kelihatan lebih... jadi dirimu sendiri. Kamu senyum lebih lepas, tanpa kelihatan beban harus jaga image.",
    "Beda banget pokoknya pembawaanmu pas lagi bareng [player_name] dibanding pas bareng orang lain.",

    # 65 - 76 (Trida gushes about player, needs confession plan)
    "Begitu ya rupanya...",
    "Iya... kurasa itu salah satu hal yang paling bikin aku jatuh hati sama [player_name].",
    "Rasanya tuh—aku selalu bisa terbuka apa adanya dan ngomongin apa pun ke [player_name]. Dia selalu tahu kata-kata yang pas buat nenangin hatiku. Bikin aku ngerasa aman dan damai.",
    "[player_name] itu sosok yang paling manis dan baik yang pernah kutemui. Tiap kali dia ketawa atau tersenyum denger lelucon konyolku, bawaannya pengin bikin dia jauh lebih bahagia lagi!",
    "Dan—tiap kali dia duduk dekat banget di sampingku, kepalaku rasanya mendadak nge-blank total, dan ujung-ujungnya tingkahku malah jadi kaku dan memalukan di depan dia!",
    "Iya deh, paham banget, Trida...",
    "Baru kali ini aku ngelihat ada orang yang mukanya kelihatan kasmaran berat tapi sekaligus kayak lagi kena serangan panik di saat yang bersamaan.",
    "Ilham, jangan gitu napa...",
    "Aduh! Aku malah keterusan ngoceh lagi, maaf ya...",
    "Tapi kayak yang kubilang tadi, aku butuh saran kalian. Aku mikir, 'bodo amat lah, mumpung ada momen pas.' Aku mau nembak [player_name] beberapa jam lagi.",
    "Tunggu, seriusan?! Secepet itu?",
    "Iya! Dia beres presentasi sekitar tiga jam lagi. Nah, kalian berdua kan anak ekskul public speaking, kan? Pasti jago merangkai kata-kata yang bagus!",

    # 77 - 88 (Hizbul & Ilham recommend the rooftop sunset)
    "Ngapain nanya ke kita berdua? Jangan lihat aku ya, cuma Hizbul yang beneran punya pengalaman pacaran di sini.",
    "Wah gila! Beneran, Kak Hizbul? Kasih tahu semua rahasianya dong!",
    "Oke oke, santai dulu, jangan kelewat heboh, aku juga baru sekali pacaran. Tapi intinya, yang penting kamu jujur dari hati. Ungkapin perasaanmu dengan jelas dan tulus.",
    "Mungkin ajak dia ke tempat yang nyaman dulu biar suasananya nggak canggung pas kamu mulai ngomong.",
    "Area rooftop di atas kafe sekolah punya pemandangan sunset yang gila kerennya, apalagi pas jam-jam sore begini.",
    "Tunggu, emang ada akses ke rooftop di sana?!",
    "Ada, lewat tangga belakang naik ke lantai paling atas gedung kafe. Dari situ kamu bisa lihat pemandangan seluruh penjuru sekolah.",
    "Ilham merobek secarik kertas dari buku catatannya lalu mencoretkan peta rute sederhana.",
    "Nih, ikutin denah ini. Terus catat beberapa poin penting yang mau kamu omongin biar nanti lidahmu nggak kelu pas di depan orangnya.",
    "Makasih banyak ya kalian berdua! Kalian penyelamat hidupku banget!",
    "Semangat, Trida! Semoga semuanya lancar jaya ya!",
    "Nanti kabari kita gimana hasilnya, oke?",

    # 89 - 100 (Player finishes rendering in 3D lab, meets Trida with tea and cookie)
    "Kembali ke Lab Komputer 3D, kamu akhirnya merebahkan punggungmu di kursi kerja dengan tarikan napas lega yang meresap hingga ke tulang.",
    "Setelah berjam-jam berkutat melakukan revisi tanpa henti, hasil render final akhirnya berhasil diekspor dan tersimpan aman di folder penyimpanan awan.",
    "Tenggorokanmu terasa kering kerontang akibat dinginnya hembusan AC ruangan lab, dan rasa pegal terasa berat membebani pundakmu saat kamu mengemasi tas dan melangkah menuju pintu keluar.",
    "Tepat saat kamu melangkah keluar dari pintu gedung, kamu melihat Trida berlari-lari kecil menghampirimu, membawa segelas es teh di satu tangan dan sekeping kukis cokelat di tangan lainnya.",
    "[player_name]...!!!",
    "Hei... kamu beneran masih nungguin di sini?",
    "Ya iya lah! Kan tadi udah janji bakal nungguin sampai selesai!",
    "Tapi kelihatannya kamu capek banget deh. Nih—kubawain minuman segar sama kukis manis dari stan kantin!",
    "Makasih banyak ya... kamu penyelamat hidupku banget, Trida.",
    "Kalian berdua berjalan santai menuju area kafe sekolah yang luas lalu menghempaskan diri di atas sofa empuk.",
    "Kamu menyeruput segarnya es teh manis itu dalam-dalam, membiarkan sensasi dinginnya membangkitkan kembali energimu yang sempat terkuras habis.",
    "Udah enakan sekarang?",

    # 101 - 110 (Walking up to the rooftop)
    "Jauh lebih mendingan. Makasih banyak ya udah mau nungguin, beneran.",
    "Uhm... kalau kamu belum terlalu capek... ada tempat keren banget yang pengin kutunjukin ke kamu di gedung ini.",
    "Eh? Dalam rangka apa nih?",
    "Anggap aja hadiah perayaan karena kamu udah berhasil nuntasin tugas beratmu! Kujamin deh rasa capek naik tangganya bakal sebanding sama pemandangannya.",
    "Awas ya kalau tempatnya nggak sekeren yang kamu gembar-gemborkan tadi.",
    "Pasti keren dong, nggak usah ragu! Gas kapan pun kamu siap!",
    "Trida menuntun langkahmu menaiki anak tangga demi anak tangga menuju lantai teratas gedung, sesekali melirik peta kecil tulisan tangan yang ia sembunyikan di telapak tangannya.",
    "Kamu yakin tahu jalan ke sana?",
    "Aku ini kapten bajak laut yang lagi memandu kamu menuju harta karun berharga tahu! Percaya deh sama aku!",
    "Iya deh, berasa lagi berburu harta karun beneran...",

    # 111 - 123 (Rooftop sunset scenery, Trida gathers courage)
    "Mendorong pintu terakhir hingga terbuka, langkah kakimu melangkah keluar menuju hamparan rooftop terbuka yang begitu luas.",
    "Cakrawala senja terbentang megah tanpa batas di depan mata, terlukis indah dalam gradasi warna keemasan mentari, semburat mawar merona, dan nila yang syahdu.",
    "Hembusan angin sepoi-sepoi yang sejuk menyapu lembut melintasi atap gedung, membawa sayup-sayup dengungan damai dari aktivitas kampus di bawah sana.",
    "Ta-daaa!! Ini dia rooftop super rahasia!",
    "Bagus banget pemandangannya... Langitnya kelihatan cantik banget, udaranya juga sejuk menenangkan.",
    "Iya kan? Tadi aku ngerasa kamu bener-bener butuh pemandangan kayak gini setelah seharian suntuk ngendon di dalam lab.",
    "Tinggi banget tempatnya ya. Dari sini seisi sekolah kelihatan semua.",
    "Keren kan? Berasa lagi berdiri di puncak dunia!",
    "Tempat ini emang boleh dimasukin ya? Nggak lucu kalau dibilang rahasia tapi ujung-ujungnya malah keciduk guru.",
    "E—eh, aman kok beneran! Tadi Ilham yang ngasih tahu lokasinya. Asal kita hati-hati nggak bakal kenapa-kenapa!",
    "...Bagus deh kalau gitu. Tempatnya bener-bener damai dan nyaman.",
    "Kamu menyandarkan tubuhmu di pagar pembatas, meresapi keindahan hening di kala senja menjelang.",
    "Di sampingmu, Trida mendadak terdiam sunyi, tak seperti biasanya. Jemarinya mengetuk-ngetuk saku celananya dengan gugup, tarikan napasnya tertahan saat ia mengumpulkan segenap keberaniannya.",

    # 124 - 138 (Trida's confession on the rooftop)
    "Uhm... [player_name]?",
    "Iya? Ada apa, Trida?",
    "Sebenarnya... ada sesuatu yang amat sangat penting yang udah lama banget pengin kuomongin ke kamu.",
    "Itu alasan kenapa aku ngajak kamu naik ke sini sore ini.",
    "Mau ngomong apa emangnya, Trida? Ngomong aja, nggak usah sungkan.",
    "Dengerin ya... Aku tahu kita baru kenal beberapa bulan di sekolah ini.",
    "Tapi rasanya udah kayak kenal lama banget. Kayak... kita emang ditakdirkan buat ketemu satu sama lain, atau hal semacam itu.",
    "Kamu selalu ada buat aku. Bahkan pas aku lagi panik dan kacau nggak keruan, kamu selalu tahu apa yang harus diucapin. Kamu bikin aku ngerasa aman.",
    "Dan belakangan ini... aku mulai menyadari banyak hal kecil di antara kita.",
    "Betapa lepasnya tawaku tiap kali bareng kamu... betapa berdegup kencangnya jantungku tiap kali kamu ada di dekatku... betapa aku berharap langkah jalan kita berdua nggak pernah berakhir.",
    "Trida menarik napas panjang yang bergetar, kedua pipinya merona merah padam di bawah pendar hangatnya semburat lembayung senja.",
    "Intinya... aku bener-bener tulus suka banget sama kamu!!",
    "Aku jatuh cinta sama kamu, [player_name]!",
    "Maaf ya aku simpan perasaan ini sendirian kelamaan... Aku cuma takut banget bakal ngerusak kedekatan yang udah kita punya selama ini.",
    "Kamu... apa kamu punya perasaan yang sama kayak yang kurasain ini?",

    # 139 - 155 (Branch A: Romance Route True Ending)
    "Nggak nyangka kamu bakal ngomong duluan... tapi sejujurnya, Trida... aku juga sayang banget sama kamu.",
    "Tunggu—beneran nih...?",
    "Tentu aja beneran! Aku udah punya perasaan ini ke kamu dari kemarin-kemarin.",
    "Senyumanmu selalu berhasil menghangatkan ruangan mana pun yang kamu masuki, dan energimu bener-bener menular bikin bahagia.",
    "Aku kagum sama semangatmu, ketangguhanmu, dan betapa tulusnya kamu peduli sama orang-orang di sekitarmu.",
    "Pas jantungku mulai berdegup nggak keruan tiap kali kamu mendekat... di saat itulah aku sadar kalau aku pengin kita lebih dari sekadar teman biasa.",
    "Trida terpaku kaku di tempatnya berdiri, butiran air mata berkaca-kaca di sepasang mata oranyenya bersamaan dengan senyuman haru yang merekah begitu indah di parasnya.",
    "Aku... aku bahagia banget. Sumpah tadi sempat kepikiran kalau perasaanku bakal bertepuk sebelah tangan...",
    "Perasaanku sama seutuhnya kayak perasaanmu kok.",
    "Berarti... sekarang kita resmi jadian ya?",
    "Jelas dong, kuharap juga begitu.",
    "Di bawah pendar megah semburat langit senja, kamu menarik tubuh Trida ke dalam dekapan hangat yang erat.",
    "Trida membenamkan wajahnya di bahumu, tertawa bahagia di sela-sela air mata harunya saat kedua tangannya melingkar mendekap erat tubuhmu.",
    "Aku sayang banget sama kamu, [player_name]... sayang banget.",
    "Seiring tenggelamnya sang surya di atas SMK Raden Umar Said, sebuah lembaran kisah yang baru resmi dimulai.",
    "Bukan lagi sekadar teman sekelas, melainkan dua hati yang kini melangkah maju beriringan.",
    "{b}— RUTE ROMANSA: TRUE ENDING —{/b}",

    # 156 - 164 (Branch B: Friendship Ending)
    "Trida... makasih banyak ya udah jujur mengutarakan perasaanmu. Aku sangat menghargai betapa besarnya rasa percayamu ke aku.",
    "Aku bener-bener peduli sama kamu, tapi... untuk saat ini, aku lebih menghargai ikatan persahabatan kita lebih dari apa pun. Aku ingin kita tetap jadi sahabat terbaik.",
    "Ah... santai aja, aku ngerti dan paham banget kok!",
    "Aku emang cuma butuh ngeluarin beban rasa ini dari dadaku aja. Tapi kita bakal tetep temenan kan?",
    "Pasti. Kamu sahabat terbaikku, Trida.",
    "Berarti kita bakal tetep jadi duo terhebat dan paling kompak di sekolah ini! Sepakat!",
    "Meski tanpa terikat asmara, ikatan yang telah kalian bangun bersama Trida tetap berdiri kokoh tak tergoyahkan.",
    "Sebuah jalinan persahabatan sejati yang ditempa oleh tawa riang, lembur tugas malam hari, dan rasa saling percaya tanpa syarat.",
    "{b}— FRIENDSHIP ENDING —{/b}",

    # 165 - 173 (Branch C: Bad Ending)
    "Kenapa... kenapa kamu harus ngomong hal kayak gitu?",
    "E—eh?",
    "Kita nggak bakal bisa temenan biasa lagi kalau ada perasaan kayak gitu di tengah-tengah kita. Mending mulai sekarang kita jaga jarak aja.",
    "M—maksudmu gimana? Kalau kamu nggak punya perasaan yang sama ke aku nggak apa-apa, tapi kenapa sampai harus berhenti temenan?!",
    "Karena ke depannya hal ini cuma bakal bikin keadaan jadi makin sakit. Maaf ya, Trida.",
    "Kamu berbalik badan dan melangkah menuju pintu tangga, meninggalkan Trida seorang diri di atas rooftop yang berangin dingin.",
    "Di belakangmu, isak tangis pilu yang pecah dari sosok sahabatmu yang paling ceria perlahan bergema menyayat dinginnya hembusan angin senja.",
    "Beberapa kata yang telah terucap, sekali terlontar, tak akan pernah bisa ditarik kembali.",
    "{b}— BAD ENDING —{/b}",

    # 174 - 186 (Branch D: Friendship Route Walk & GG discussion)
    "Di bawah siraman semburat lembayung senja yang keemasan, kamu dan Trida melangkahkan kaki santai beriringan menyusuri jalan pulang menuju kosan.",
    "Kantong plastik berisi kotak makanan malam berayun lembut mengikuti irama langkah kaki kalian, ditemani sayup-sayup deru kendaraan petang di kejauhan.",
    "Huuwah... Akhirnya ya, hari yang panjang banget! Asli deh, tugas-tugasku buat minggu ini aja masih banyak yang belum beres!",
    "Seenggaknya bagian paling susahnya udah kelar kita beresin. Mendingan daripada nggak sama sekali—malam ini kita bisa sedikit santai.",
    "Bener banget! Tapi kayaknya tenagaku masih ada sisa nih. Siapa tahu malam ini aku bisa kebut nyelesein semua sisa tugas seminggu penuh!",
    "Kadang aku bener-bener iri sama energimu yang kayak nggak ada habisnya itu...",
    "Makanya tiap mau ke mana-mana aku selalu ngajak kamu jalan kaki bareng! Biar badan ada geraknya! Nambah stamina tahu.",
    "Berguna banget ya buat nahan sabar pas main game dengan pacing lambat kayak Goblin/Goobers, iya kan?",
    "Hush, jangan asal ngejek game GG gitu napa! Kamu kan belum pernah nyoba mainin!",
    "Bukannya kamu sendiri yang kemarin bilang kalau alur ceritanya kelewat lambat bahkan buat standarmu?",
    "Ya kan nggak butuh banyak sabar kalau ceritanya udah mulai seru banget! Apalagi kalau kamu milih rute cerita faksi Goobers!",
    "Trida mulai menjelaskan dengan penuh semangat dan gestur tubuh yang heboh mengenai lore mendalam dari game tersebut.",
    "Kata-katanya mengalir deras sarat dengan antusiasme yang tulus, memberi warna ceria di sepanjang trotoar saat sinar senja mewarnai wajahnya dengan semburat jingga kemerahan.",

    # 187 - 202 (Choosing storyline, 3-month reflection)
    "Ooh, aku jadi penasaran nih!",
    "[player_name], dari cerita yang kubahas tadi, kira-kira kamu bakal milih alur cerita yang mana?",
    "Faksi Goobers. Alur ceritanya kedengaran menarik, dan aku nggak keberatan sama alur yang lambat asalkan narasi dunianya mendalam.",
    "Tuh kan bener! Kita sepemikiran banget! Makin keras perjuangan grinding-nya, makin nikmat kepuasannya pas nyampe ke titik plot cerita yang gede!",
    "Faksi Goblins. Gameplay yang solid sama mekanik game yang asyik itu kunci utama yang bikin sebuah game bener-bener seru buat dimainin.",
    "Udah ketebak sih kamu bakal jawab begitu! Kamu emang tipe pemain yang lebih mentingin gameplay dulu!",
    "Dua-duanya bakal kumainin sih, jujur aja.",
    "Hm... tipe pemain completionist ya? Atau kamu jawab begitu cuma gara-gara dari tadi nggak bener-bener nyimak omonganku nih?",
    "Yah... gimana ya...",
    "Ketahuan kan! Hahaha, tapi nggak apa-apa kok!",
    "Trida kembali menyelaraskan langkahnya dalam ritme hening yang nyaman di sampingmu, menengadah memandangi gumpalan awan senja yang kian temaram.",
    "Nggak berasa ya, Trida... rasanya belum lama banget kita baru masuk sekolah tiga bulan yang lalu, iya kan?",
    "Wah, iya juga ya pas kamu sebut gitu... Juli, Agustus, September... sekarang udah bulan September aja!",
    "Waktunya cepet banget lewat, tapi di sisi lain rasanya kayak kita udah saling kenal dari dulu.",
    "Rasanya nyaman banget punya teman kayak kamu di sampingku.",
    "Bener banget! Aku belum pernah ngerasa senyaman ini di lingkungan sekolah sebelumnya. Aku bener-bener bersyukur banget kita bisa jadi teman akrab, [player_name].",

    # 203 - 224 (Dinner boxes at boarding house, choking on rice, clubs banter)
    "Setibanya di kosan, kalian berdua mendudukkan diri di kursi santai yang nyaman dengan kotak makan malam hangat di hadapan kalian.",
    "Aroma sedap ayam goreng barbeku dan nasi katsu ayam memenuhi kehangatan ruangan itu.",
    "Ayo buruan dimakan sebelum dingin! Tadi katanya kamu udah kelaparan banget kan?",
    "Siap, langsung sikat nih.",
    "Trida menyendok nasi dalam porsi besar ke mulutnya, dan seketika tersedak suapan yang terlalu terburu-buru itu.",
    "*UHUK* *UHUK* Aduh—air—minum—!",
    "Nih, minum punyaku dulu. Pelan-pelan makannya!",
    "Kamu menyodorkan botol minummu, memperhatikan Trida yang meneguknya rakus dengan rasa lega yang berantakan.",
    "Fuihh... makasih banyak. Bener-bener layak dinobatkan jadi tenaga medis terbaik tahun ini.",
    "Ngomong-ngomong soal kegiatan, latihan teatermu gimana kabarnya belakangan ini?",
    "Teater? Seru parah! Kemarin aku direkomendasikan buat meranin karakter lucu yang agak absurd gitu.",
    "Kedengarannya emang peran yang sengaja dibikin khusus buat dirimu banget.",
    "Dih! Kuanggap itu sebagai pujian ya!",
    "Kalau kamu gimana? Tadi sempat ada kegiatan ekskul nggak?",
    "Aku belum ikut ekskul apa pun dulu buat sekarang. Takutnya malah keteteran kalau terlalu padat.",
    "Pilihan bijak sih! Tugas sekolah harian aja udah cukup bikin kepala mau pecah.",
    "Aku ikut ekskul perfilman, tapi jadwal kumpulnya di hari yang berbeda.",
    "Wah, perfilman! Kalau sewaktu-waktu kamu butuh aktor berbakat buat adegan filmmu, kamu tahu kan harus hubungi siapa!",
    "Nanti rekaman audisimu kusimpan rapi di arsip ya, Trida.",
    "Tadi aku ikut ekskul public speaking. Kita latihan debat tadi.",
    "Debat? Kayak game pengacara yang sering kamu tontonin pas aku main itu ya?",
    "Kurang lebih mirip kayak gitu sih.",

    # 225 - 246 (Deep gratitude, what player admires about Trida, Friendship True Ending)
    "Obrolan santai itu perlahan mereda menjadi keheningan yang nyaman saat kalian berdua menandaskan santap malam.",
    "Trida meletakkan kotak makannya yang sudah kosong di atas meja kopi, raut wajahnya yang usil melembut berganti ekspresi yang begitu tulus dan bersahaja.",
    "[player_name]... aku cuma mau bilang makasih banyak ya.",
    "Makasih buat apa?",
    "Buat semuanya selama beberapa pekan terakhir ini. Pas tugas kelompok kemarin berantakan dan aku ngerasa jadi manusia paling gagal sedunia...",
    "Kamu nggak menghakimiku sama sekali. Kamu nggak pernah capek ngadepin kepanikanku. Kamu selalu dengerin keluh kesahku dan ngingetin kalau aku bukan orang yang nggak berguna.",
    "Selama ini aku selalu ngerasa harus jadi orang yang berisik dan lucu biar orang lain nggak bosen temenan sama aku. Tapi pas bareng kamu, aku nggak perlu pura-pura jadi siapa pun.",
    "Kamu sahabat terbaik yang pernah kumiliki di sekolah ini.",
    "Nggak perlu berterima kasih segitunya kok, Trida. Kamu sendiri punya banyak hal luar biasa yang berharga.",
    "Hal yang paling kukagumi darimu itu...",
    "Sifat positifmu. Kamu selalu bikin ruangan mana pun jadi terasa jauh lebih hangat dan ceria cuma dengan jadi dirimu sendiri.",
    "Kamu beneran mikir begitu? Makasih ya... kata-katamu berarti banget buat aku.",
    "Ketangguhanmu. Seberat apa pun masalah yang datang, kamu selalu bisa bangkit lagi dan terus mencoba tanpa menyerah.",
    "Aku selalu berusaha yang terbaik! Punya teman kayak kamu yang selalu ngedukung bikin semuanya terasa berkali-kali lipat lebih ringan.",
    "Semangat dan passion-mu. Rasa penasaran dan antusiasmemu yang tanpa batas soal seni 3D, game, dan cerita fiksi bener-bener menular bikin orang lain ikut bersemangat.",
    "Hehehe... iya juga ya, kadang aku emang suka kelewat heboh kalau udah ngomongin hobi. Tapi aku seneng banget kalau kamu bisa ikut nikmatin ceritanya.",
    "Trida menyandarkan tubuhnya di kursi santai, seulas senyuman damai dan puas terlukis indah di wajahnya.",
    "Impianku... adalah bikin game dan animasi yang bisa ngasih kebahagiaan dan kehangatan yang sama kayak yang pernah kurasain dari cerita-cerita hebat.",
    "Dan punya sahabat kayak kamu yang melangkah beriringan di sampingku... bikin aku yakin kalau impian itu beneran bisa kuraih suatu hari nanti.",
    "Aku yakin kamu pasti bisa, Trida. Perjalanan kita di depan masih sangat panjang.",
    "Dikelilingi hangatnya keheningan malam, kamu berbagi tawa kecil nan tulus bersama sahabat terdekatmu.",
    "Rintangan apa pun yang akan menghadang di tahun ajaran baru nanti, kamu tahu bahwa kalian berdua akan selalu menghadapinya bersama-sama.",
    "{b}— RUTE PERSAHABATAN: TRUE ENDING —{/b}"
]

week10_strings = {
    "It's really nice…": "Bagus banget pemandangannya...",
    "It's really nice...": "Bagus banget pemandangannya...",
    "This is pretty high up…": "Tinggi banget tempatnya ya...",
    "This is pretty high up...": "Tinggi banget tempatnya ya...",
    "Secret?": "Rahasia?",
    "I love you too!": "Aku juga mencintaimu!",
    "I want to stay friends": "Aku ingin kita tetap berteman",
    "Why would you say that?": "Kenapa kamu ngomong begitu?",
    "The Goobers": "Faksi Goobers",
    "The Goblins": "Faksi Goblins",
    "Both": "Dua-duanya",
    "I'm not in any extracurriculars": "Aku belum ikut ekskul apa pun",
    "Not today, but a different day": "Nggak hari ini, hari yang lain",
    "I did": "Iya, tadi ada",
    "Your positivity": "Sifat positifmu",
    "Your resilience": "Ketangguhanmu",
    "Your passion": "Semangat dan passion-mu"
}

with open("/tmp/week10.rpy.json", "r", encoding="utf-8") as f:
    items = json.load(f)

d_idx = 0
for item in items:
    if item["type"] == "dialogue":
        if d_idx < len(week10_translations):
            item["indonesian"] = week10_translations[d_idx]
            d_idx += 1
        else:
            print(f"Warning: more dialogues than translations at index {d_idx}")
    elif item["type"] == "string":
        eng = item["english"]
        if eng in week10_strings:
            item["indonesian"] = week10_strings[eng]

with open("/tmp/week10.rpy.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

subprocess.run(["python3", "tools/translate_helper.py", "apply", "game/tl/indonesian/week10.rpy", "/tmp/week10.rpy.json"], check=True)
print(f"Updated week10.rpy.json: {d_idx} dialogues, {len(week10_strings)} menus.")
