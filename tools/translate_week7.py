import json
import subprocess

week7_translations = [
    # 0 - 10 (Morning light, Trida eating yesterday's chocolate)
    "Sinar lembut mentari pagi menyinari deretan bangku kelas yang masih lengang, berpadu dengan dengung kipas desktop PC dan ketukan halus tuts papan ketik.",
    "Di sudut belakang ruangan, Trida duduk di bangku biasanya dengan bahu agak membungkuk di depan laptopnya yang tebal.",
    "Sorot matanya bergerak lincah menyapu layar, terfokus sepenuhnya pada potongan animasi yang baru setengah jadi.",
    "Ia tampak begitu tenggelam dalam Maya; dunianya menyusut hanya sebatas pendar monitor dan ketukan ritmis pengerjaan tugasnya, persis seperti bayangan orang tentang anak animasi sejati.",
    "Di salah satu tangannya, jemarinya tanpa sadar membolak-balik sebatang cokelat yang sudah agak lecek dan baru dimakan setengah.",
    "Itu adalah camilan spesial yang kamu berikan padanya kemarin.",
    "Kemarin rasanya begitu tegang hingga perutmu mulas bagai terikat simpul, dan detak jantung serta tarikan napasmu kerap tertahan.",
    "Kamu melangkah menghampirinya tanpa suara sebelum menyandarkan tubuhmu di tepian mejanya.",
    "Kamu beneran masih makan cokelat itu?",
    "Kamu melipat kedua tangan di dada dengan senyuman tipis khas sapaan pagi, diiringi secuil nada menggoda.",
    "Pasti dari kemarin cokelat itu cuma kamu diemin di dalam tas kan?",

    # 11 - 26 (Trida startled, teasing & chocolate defense)
    "Trida tersentak tegak di kursinya, sekujur tubuhnya terlonjak kaget saat suaramu membelah konsentrasinya.",
    "Matanya membelalak lebar, dan rona merah padam seketika merambat naik dari leher hingga ke ujung daun telinganya.",
    "Jemarinya gelagapan memegang cokelat itu sampai hampir terjatuh, sebelum akhirnya ia melepaskan tawa riang bernada tinggi.",
    "Jari-jemarinya mengetuk-ngetuk meja dengan cemas, berusaha menutupi rasa salah tingkahnya di balik ledakan panik yang dibuat-buat.",
    "E—eh?! Maksudmu gimana coba?!",
    "Makanan enak itu punya waktunya sendiri tahu! Namanya juga dinikmati pelan-pelan, cari tahu sana!",
    "Ia menggerakkan tangannya heboh sambil memegang cokelat yang tinggal setengah itu, sampai-sampai hampir menjatuhkannya ke atas keyboard.",
    "Lagian cokelatnya belum basi juga kok!",
    "Kamu tertawa kecil, geli melihat tingkahnya yang kalang kabut membela kebiasaan makannya.",
    "Iya deh, terserah apa katamu. Jangan nangis ngadu ke aku ya kalau perutmu melilit pas jam pelajaran ketiga nanti.",
    "Trida tersenyum lebar, ketegangan yang tadi sempat kaku seketika luruh dari pundaknya saat ia kembali bersandar rileks di kursi.",
    "Ia mengulurkan tangan, menyenggol pelan lenganmu dengan sikunya—kebiasaan sentuhan fisik akrab yang selalu ia lakukan tanpa sadar.",
    "Dih, lihat deh gayamu, sok-sokan khawatir gitu. Sejak kapan kamu peduli amat sama kesehatan pencernaanku?",
    "Ia tertawa renyah, namun tatapannya mendadak bergeser, melirik kikuk ke tepian meja sebelum kembali menatap matamu.",
    "Nada bicaranya yang ceria mendadak terhenti, berganti keraguan yang aneh.",
    "Ia berdeham pelan, dan mendadak cokelat setengah gigitan itu terlihat menjadi objek yang amat sangat menarik untuk dipandangi.",

    # 27 - 42 (Trida's vulnerable confession about saving the chocolate)
    "Um... sebenarnya...",
    "Nada suaranya merendah satu oktaf, terdengar jauh lebih lirih, tanpa ada sisa tingkah konyolnya yang biasanya.",
    "Ia mengusap tengkuknya dengan tangan yang bebas, jemarinya meremas kerah bajunya dengan canggung.",
    "Sebenarnya... aku sengaja nyimpan cokelat ini.",
    "Kamu mengerjap, terkejut mendengar perubahan nada bicaranya yang tiba-tiba begitu serius.",
    "Sengaja disimpan?",
    "Kenapa? Kan cuma cokelat biasa.",
    "Mata Trida mendongak menatap matamu, mempertahankan tatapan lekat tanpa berkedip yang selalu ia tunjukkan tiap kali berusaha jujur dari lubuk hatinya.",
    "Daun telinganya kini merona merah terang.",
    "Nggak ada yang namanya 'cuma biasa' kalau cokelat itu... kamu tahu kan. Kamu yang ngasih.",
    "Ia tertawa kecil mencela dirinya sendiri, pandangannya kembali menunduk ke meja berusaha menepis rasa canggung.",
    "Dengerin deh omonganku, ugh... kedengerannya geli dan lebay banget ya. Udah, lupain aja.",
    "Ia mencoba memalingkan wajah, namun kamu tetap bergeming di tempatmu, dan ia terus berbicara terburu-buru seakan ingin lari dari kerentanan hatinya sendiri.",
    "Nggak, tapi serius deh—aku jarang banget dapet perlakuan kayak gitu. Sebelumnya nggak pernah ada orang yang... tiba-tiba ngasih sesuatu yang manis begini tanpa ada maunya.",
    "Pemberianmu kemarin bener-bener bikin semingguku jadi jauh lebih indah, tahu nggak?",

    # 43 - 57 (Trida's feeling of being seen & class bell)
    "Untuk sesaat, keriuhan obrolan anak-anak di kelas seolah senyap sepenuhnya.",
    "Kejujuran polos tanpa pertahanan itu benar-benar membuatmu terperangah tak menduga.",
    "Hal itu bikin aku ngerasa... mungkin selama ini aku nggak sepenuhnya nggak dianggap di sini.",
    "Kamu terpaku berdiri di sana, mendadak kelu mencari kata-kata santai untuk membalasnya, merasakan sengatan hangat yang menjalar naik ke lehermu saat balik menatapnya.",
    "Menyadari keheninganmu, mata Trida membelalak panik; kedua tangannya buru-buru ia sembunyikan ke dalam saku hoodie seolah ingin menghilang ditelan kursinya.",
    "P—pokoknya gitu deh! Balik nugas lagi yuk! Nanti keburu gurunya masuk dan nerangin materi baru!",
    "Kita kan nggak mau sampai nggak lulus, ya nggak?",
    "Iya juga sih...",
    "Jelas nggak lah.",
    "Tentu aja nggak.",
    "Sepanjang jam pelajaran kamu sama sekali tidak bisa fokus; suara penjelasan guru di depan kelas hanya berlalu bagai dengung lebah di kepalamu.",
    "Pandanganmu berulang kali mencuri lirik ke meja Trida, tempat cokelat itu berada.",
    "Tanpa kamu sadari, pengeras suara sekolah sudah mengumandangkan bel istirahat, membuyarkan seluruh lamunanmu.",
    "Mending lupain dulu soal itu deh. Mumpung lagi istirahat, mending nikmatin waktu luang...",
    "Ke mana ya enaknya sekarang?",

    # 58 - 74 (Branch A: Grapos field with Radit)
    "Lapangan Grapos di luar berdenyut penuh kehidupan, hamparan siswa-siswi yang meregangkan otot dan bersandar di pilar-pilar semen tua, menikmati jeda singkat yang berharga dari padatnya jadwal mereka.",
    "Gerombolan siswa berbondong-bondong menuju kantin bagai laron yang tertarik pada nyala lentera, tawa canda mereka menciptakan simfoni riuh khas anak muda.",
    "Udara siang yang hangat menyelimutimu, berpadu dengan aroma sedap makanan dan sayup-sayup celotehan siswa SMK animasi yang heboh membahas antrean render dan tenggat projek yang kian mencekik.",
    "Kamu menyandarkan tubuh di pagar semen yang sejuk, menikmati kelegaan jeda istirahat saat hiruk-pikuk di sekelilingmu perlahan memudar menjadi dengungan latar yang lembut.",
    "Tiba-tiba, suara derap langkah pelan terdengar mendekat di atas paving.",
    "Radit muncul dengan gaya santainya yang khas, berjalan menghampirimu dengan kedua tangan terbenam di saku jaket.",
    "Sambil menggelengkan kepalanya pelan, ia mengibaskan sisa-sisa tetesan air dari wajahnya setelah buru-buru membasuh muka di toilet.",
    "Duh gila... kadang aku kepikiran pengin drop out aja terus daftar jadi atlet tidur profesional.",
    "Radit berbicara dengan nada santai dan pelan, mengalun lembut mengikuti ritme pembawaannya yang tenang tanpa beban.",
    "Setelah merenung sejenak, ia membiarkan keheningan menggantung sebelum melanjutkan kembali ucapannya yang lambat dan tanpa beban, seakan menikmati tiap silabel katanya.",
    "Rasanya kasur di kosanku dari tadi manggil-manggil namaku terus tuh.",
    "Kamu tertawa geli sambil melirik ke arahnya dari samping.",
    "Kasurmu itu cuma kasur busa tipis di lantai kamar kos yang sempit, Radit. Mana ada manggil-manggil, yang ada dia lagi minta ampun ditindih terus.",
    "Bener juga sih. Tapi seenggaknya kasurku nggak bakal pernah crash pas lagi asyik nge-save file.",
    "Radit menyunggingkan senyum malas seraya bahunya berguncang menahan tawa.",
    "Ngomong-ngomong soal pilihan hidup yang salah...",
    "Ia terdiam sejenak, memindahkan tumpuan berat badannya ke kaki yang lain, tatapannya menerawang ke cakrawala sebelum kembali menatapmu dengan kilau jenaka di matanya.",

    # 75 - 92 (Radit garage band banter)
    "Kemarin aku nggak sengaja nemu band garasi antah-berantah dari Shimokitazawa. Konsep estetikanya bener-bener cuma empat cowok berdiri di ruang bawah tanah gelap mainin gitar fals.",
    "Terus?",
    "Terus... jujur aja? Musiknya bener-bener nyentuh jiwaku banget.",
    "Kamu mengangkat sebelah alis lalu melipat kedua tangan di dada dengan senyum penuh arti.",
    "Biar kutebak. Band lain lagi yang pendengar bulanannya di Spotify cuma dua digit, dan kamu udah siap ngabisin setengah uang saku bulananmu buat beli piringan hitam impor yang butuh tiga bulan buat lolos bea cukai?",
    "Radit menatapmu beberapa detik tanpa berkedip, sudut bibirnya berkedut menahan tawa geli.",
    "Pertama-tama ya, itu kaset pita, bukan piringan hitam. Belajar dulu format rilisan anak indie sana.",
    "Kedua... wah gila ya! Kamu sampai hafal kebiasaan belanjaku kayak auditor keuangan aja.",
    "Ia memiringkan kepalanya sedikit, kedua tangannya tetap setia di dalam saku saat ia menyandarkan bahunya di sampingmu pada pagar pembatas.",
    "Kira-kira aku harus bangga karena kamu ingat sampah apa aja yang kubeli, atau harus waspada jangan-jangan kamu sekarang jadi stalker-ku nih?",
    "Ngapain juga aku nge-stalk kamu kalau aroma kamarmu aja udah jelas-jelas bau plastik sampul kaset sama penyesalan hidup.",
    "Kamu membalas celotehannya sambil menyenggolkan siku ke lengan Radit. Radit tersenyum simpul dengan ketulusan hangat yang terpancar sekilas menembus tampang dinginnya, meski sedetik kemudian kembali ia tutupi dengan candaan santai.",
    "Ya gimana ya, harus ada yang rela berkorban demi ngehidupin skena musik bawah tanah lokal kan...",
    "Ia melirik ke arah pintu kelas, menangkap sekilas energi kesibukan tugas yang masih berdenyut di dalam sana.",
    "Udahlah, mending kita balik ke kelas sebelum pintunya dikunci guru dan kita disangka kabur buat bikin band indie sendiri.",
    "Padahal kalau dipikir-pikir... bukan rencana cadangan yang buruk juga sih.",
    "Dengan mengedikkan bahu santai, Radit menjauhkan tubuhnya dari pagar pembatas, menarik sebelah tangannya keluar dari saku untuk menunjuk ke arah pintu kelas.",
    "Tanpa terburu-buru, kalian berdua berbalik dan melangkah santai kembali ke dalam kelas bersama-sama.",

    # 93 - 109 (Branch B: Staying in class with Trida, storyboard struggles)
    "Ketimbang berpanas-panas di bawah terik hawa siang atau jajan ke kantin, kamu memilih tetap tinggal di ruang kelas yang sunyi dan ber-AC dingin.",
    "Kamu menarik sebuah kursi kayu kosong ke samping meja Trida.",
    "Ia tampak terpaku memandangi buku catatannya yang terbuka, penuh coretan sketsa karakter dan draf papan cerita yang semrawut, larut dalam lamunannya.",
    "Kalau kamu pelototin terus kertasnya begitu, nanti tintanya bisa kabur ketakutan lho.",
    "Ucapmu seraya memangku dagu dengan tangan sambil bersandar di tepi mejanya.",
    "Trida terlonjak kaget; pensilnya jatuh berdenting di atas meja saat ia buru-buru memutar kursinya ke arahmu.",
    "Ia memekik kaget bernada tinggi sambil mengangkat kedua tangannya dramatis ke udara.",
    "Astagfirullah, kamu bikin jantungan aja deh!",
    "Jangan suka ngagetin orang gitu napa kalau orang lagi berusaha fokus—atau tepatnya lagi gagal fokus!",
    "Ia tertawa panik, tatapannya menyapu sekeliling ruangan yang lengang sebelum kembali terpaku lurus menatapmu.",
    "Lagian ya, tintanya kabur bukan gara-gara takut sama mukaku. Tapi gara-gara susunan layout-ku ini ancur lebur parah. Coba lihat coretan nggak jelas ini.",
    "Ia menyodorkan buku sketsanya lebih dekat ke arahmu, mengetuk-ngetuk kasar salah satu panel yang masih berantakan.",
    "Sumpah deh, tiap kali aku nyoba ngatur tempo buat adegan ini, otakku rasanya langsung korslet total.",
    "Kenapa sih bikin struktur cerita itu susah banget? Padahal niat awalnya cuma pengin bikin animasi keren yang bikin penonton ngerasa bisa naklukin dunia, tapi hasilnya malah sampah begini.",
    "Ia menjatuhkan tubuhnya ke depan, membiarkan dahinya bersandar lemas di tepian meja tepat di samping lenganmu seraya menghembuskan napas putus asa.",
    "Kadang aku mikir, ngapain juga ya aku pasang target ketinggian. Coba lihat anak-anak lain di jurusan kita—mereka udah bisa bikin animasi gila-gilaan dengan konsep luar biasa, sementara aku... bikin timeline sederhana aja masih megap-megap.",
    "Rasanya aku bodoh banget, tahu nggak...",

    # 110 - 128 (Comforting Trida & break time conversation)
    "Kamu tersenyum hangat lalu mengulurkan tangan, memberikan remasan lembut yang menenangkan di pundaknya.",
    "Kamu terlalu keras sama dirimu sendiri, Trida. Kamu cuma lagi butuh istirahat sejenak kok.",
    "Merasakan sentuhan hangatmu, Trida langsung menegakkan badannya; senyuman cerah kembali merekah di wajahnya, seolah awan kelabu keraguannya tadi sirna seketika.",
    "Ia menyandarkan tubuhnya ke arah sentuhanmu, tanpa sadar menyentuhkan bahunya ke bahumu.",
    "Tuh kan! Itu kenapa kamu emang yang terbaik. Selalu aja hadir dengan kata-kata yang pas di saat yang tepat.",
    "Ia tertawa riang, tempo bicaranya mendadak melesat cepat saat kembali berceloteh penuh semangat, tangannya bergerak ke sana-kemari.",
    "Mungkin agak random ya kedengarannya...",
    "Tapi aku udah pernah cerita belum soal video bedah lore yang kutonton semalam? Itu mahakarya RPG klasik yang luar biasa banget, plot twist-nya muncul terus tiada henti—?",
    "Ia mendadak berhenti, menyipitkan matanya menatapmu, meski seulas senyum puas tetap terkembang di sudut bibirnya.",
    "Ia baru tersadar betapa dekatnya kalian duduk berdua dan fakta bahwa kamu sama sekali tidak pergi keluar istirahat seperti anak-anak lainnya.",
    "Ujung daun telinganya bersemu merah muda samar, dan ia buru-buru mengusap tengkuk lehernya yang canggung.",
    "Tunggu sebentar... baru nyadar, kamu beneran milih diam di dalam kelas pas jam istirahat gini?",
    "Iya, kenapa emangnya... Ada masalah?",
    "Maksudku, daripada keluar cari angin segar atau nongkrong bareng yang lain kayak biasanya?",
    "Kamu mendengar nada suaranya kehilangan sedikit sifat teatrikalnya, digantikan kehangatan yang begitu tulus.",
    "Kamu nggak perlu maksain nemenin aku di sini kalau nggak mau lho. Aku beneran nggak apa-apa kok.",
    "Aku cuma mau nemenin kamu aja biar kamu nggak panik terus nggak sengaja ngebelah buku sketsamu jadi dua.",
    "Sahutmu dengan seringai tipis, melihat Trida tertawa tersipu penuh rasa hangat.",
    "Dasar, ada-ada aja kelakuanmu. Tapi... iya, aku seneng banget kamu ada di sini.",

    # 129 - 147 (Afternoon Civics class, indifferent glasses boy)
    "Ruang kelas bermandikan hangatnya semburat keemasan mentari sore yang menerobos melalui jendela-jendela tinggi, menciptakan siluet kontras antara terang dan bayangan.",
    "Bayangan-bayangan panjang merayap malas di atas lantai, berdampingan dengan deretan drawing tablet tebal yang untuk sementara waktu disingkirkan ke pinggir meja.",
    "Sebagai gantinya, buku-buku catatan warna-warni dan buku paket tebal yang telah lusuh terhampar di atas meja, menandakan ruang tempat kreativitas berpadu dengan tuntutan akademis.",
    "Guru PPKn melangkah ke depan kelas, sepatu pantofel hitamnya berderit pelan di atas lantai linoleum saat ia meletakkan setumpuk lembar panduan ke meja guru.",
    "Tolong tenang semuanya. Untuk tugas hari ini, kalian tidak perlu menyalakan komputer. Cukup buka buku paket kalian pada bab Undang-Undang Dasar 1945.",
    "Instruksinya sederhana: perhatikan tugas kelompok, lingkari bagian instruksinya, lalu koordinasikan dengan kelompok kalian untuk memilih menjawab soal latihan, menyusun makalah singkat, atau meringkas materi. Silakan mulai.",
    "Dengan bunyi klik pulpen yang tegas, beliau berbalik ke papan tulis untuk menuliskan nomor halaman tugas.",
    "Di sekeliling ruangan, bunyi derit kursi yang bergesekan dengan lantai terdengar saat para siswa mulai mengeluarkan kertas folio dan membuka buku paket mereka.",
    "Namun, di meja kelompokmu, hawa ketegangan mendadak menggantung pekat dan menyesakkan di udara.",
    "Siswa laki-laki yang duduk tepat di hadapanmu—sosok pendiam yang biasanya begitu samar hingga nyaris tak kasat mata di kelas—menghembuskan napas panjang yang terdengar berat dan menusuk keheningan.",
    "Dengan pembawaan dingin yang tampak begitu terbiasa, seolah menganggap kerja kelompok ini murni beban administratif yang menyebalkan ketimbang wadah kolaborasi, ia membuka buku PPKn-nya yang tebal dengan bunyi debuk hampa.",
    "Pandangannya terpaku lurus pada lembaran buku di depannya, sengaja menghindari kontak mata seraya membetulkan letak kacamata dengan gerakan teratur.",
    "Dengan ketenangan khas orang yang sudah terbiasa diabaikan, ia langsung membuka halaman yang ditugaskan tanpa sepatah kata pun keluar dari bibirnya.",
    "Di sampingnya, Trida duduk membeku kaku.",
    "Ia menatap nanar ke arah buku paketnya, namun pandangan matanya tampak kosong melompong, tak sanggup mencerna satu kata pun dari deretan teks yang tercetak di sana.",
    "Kedua tangannya terkunci rapat di pangkuan, sedikit gemetar saat tatapannya melirik cemas ke sudut-sudut meja, enggan bertatapan dengan siapa pun.",
    "Tanpa menunggu kalian berdua mengambil inisiatif, tangan Trida yang gemetar terulur ragu untuk membuka halaman yang sama di bukunya, melewatkan perintah guru untuk melingkari instruksi terlebih dahulu.",
    "Ia terburu-buru meraih pensil, gerakannya terlalu panik dan tergesa-gesa, hingga tanpa sengaja menyenggol penghapusnya jatuh dari meja.",
    "Penghapus itu memantul pelan mengenai sepatumu sebelum mendarat di lantai.",

    # 148 - 166 (Glasses boy's cold dismissal & Trida crushed)
    "Cowok berkacamata itu bahkan tidak repot-repot mengangkat kepalanya dari buku. Raut wajahnya tetap datar tanpa ekspresi emosi sedikit pun, melontarkan kritik dingin dengan nada datar bagai sistem otomatis yang membaca prompt teks.",
    "Penghapusmu jatuh. Dan kamu lupa ngelingkari instruksinya. Padahal instruksi gampang gitu doang.",
    "Tangan Trida membeku di udara tepat di atas lantai. Ujung daun telinganya seketika berubah merah padam karena malu bukan kepalang, dan ia langsung menarik tangannya kembali, membiarkannya terkulai lemas di atas lutut.",
    "Trida tidak membungkuk untuk memungut penghapusnya. Yang bisa ia lakukan hanyalah menatap hampa lipatan tengah buku paketnya, menggigit bibir bawahnya rapat-rapat hingga memutih.",
    "Segala ketakutan terbesarnya yang selama ini ia kubur rapat-rapat di balik lelucon konyol dan tawa riang—kini terkoyak telanjang bulat oleh ketidakpedulian dingin dari teman sekelompoknya sendiri.",
    "Trida bahkan tak mampu memaksakan tawa kecil, lidahnya kelu tak sanggup merangkai sepatah kata pun untuk membela diri.",
    "Cowok itu membalik halaman bukunya dengan bunyi gesekan kertas yang pelan, sama sekali tidak terganggu oleh atmosfer membeku yang tiba-tiba melanda meja itu.",
    "Terserah deh. Kita harus milih mau ngejawab soal atau bikin ringkasan materi. Aku mau ngerjain ringkasan aja biar bisa pulang cepet. Kasih tahu aja kalau kalian mau ngerjain yang lain, atau kalau kalian emang cuma mau bengong doang di situ.",
    "Suaranya tidak terdengar memusuhi, namun justru hal itulah yang membuatnya terasa berkali-kali lipat lebih menyakitkan.",
    "Itu adalah sikap acuh tak acuh yang menghancurkan dari seseorang yang bahkan tidak menganggap Trida sebagai rintangan yang menjengkelkan, melainkan sekadar sistem eror kecil yang cukup dilewati begitu saja.",
    "Kamu duduk tepat di samping Trida, dan rasa gamang yang menusuk tiba-tiba merambat naik menyumbat tenggorokanmu.",
    "Sudah begitu lama kamu menjadi temannya, dan melihat hancurnya raut wajah Trida yang biasanya begitu ceria seketika membuat gumpalan sesak menyesakkan rongga dadamu.",
    "Kamu belum pernah melihat Trida sehancur dan seputus asa ini, terbungkam mati kutu oleh seseorang yang bahkan tidak peduli untuk sekadar marah padanya.",
    "Trida menatap nanar halaman terbuka itu, tenggorokannya bergerak menelan ludah seolah sedang menelan pecahan kaca tajam.",
    "Beban telak dari perasaan bahwa dirinya benar-benar tidak berguna—diperlakukan bagai mesin yang rusak—akhirnya memaksa sebuah gumaman lirih yang rapuh lolos dari bibirnya.",
    "A—aku tadi mau ngelingkari kok...",
    "Trida berbisik dengan suara yang sedikit bergetar parau, begitu lirih hingga nyaris ditelan bisingnya suara kelas.",
    "Ia terus menunduk menatap mejanya, jemarinya mencengkeram erat pinggiran buku paket bagai tali penyelamat, mati-matian berusaha mencari pembenaran atas kepanikannya.",
    "Aku cuma... lagi buru-buru tadi. Aku masih bisa ngerjainnya kok. Aku... aku nggak sengaja bikin kacau...",

    # 167 - 186 (Total withdrawal, asking "Are you okay?")
    "Cowok berkacamata itu tak bergeming dari bukunya, hanya menghembuskan napas panjang yang mencemooh lewat hidungnya seraya mengetuk-ngetukkan pulpen di pinggir halaman.",
    "Ya udahlah, nggak penting juga, buruan kelarin aja biar cepet selesai.",
    "Datar nada suaranya menyisakan sengatan rasa jengkel yang tajam, jatuh bagai beban timah berat di atas meja kelompok kalian.",
    "Seketika itu juga, sisa-sisa suara di sudut mejamu lenyap tak berbekas. Keheningan yang menyusul terasa begitu canggung, menyesakkan, dan membuat udara serasa menipis.",
    "Trida tersentak mundur seolah baru saja dihantam pukulan fisik yang keras. Segala ocehan ceria dan energi lincahnya yang biasa sirna tak berbekas.",
    "Ia hanya bisa menunduk menahan malu, matanya perih memanas dan tangannya yang gemetar berusaha memegang pensil untuk kembali bekerja.",
    "Ia membuat lingkaran asal-asalan di sekitar kalimat instruksi, namun jemarinya tak kunjung tenang, dan isi kepalanya benar-benar kosong melompong.",
    "Deretan teks di halaman buku melebur menjadi gumpalan tinta yang tak bermakna, dan setiap goresan tangannya yang kikuk seakan membenarkan ucapan dingin cowok tadi.",
    "Ia akhirnya menyerah, membiarkan tangannya jatuh lunglai ke pangkuan dengan pundak yang merosot lesu.",
    "Kamu terdiam kaku di sampingnya, gumpalan rasa resah dan getir melilit erat di dalam dadamu.",
    "Setelah berjam-jam kamu menemani pasang surut emosinya, menjadi tempatnya bersandar melewati badai perasaannya, kamu belum pernah melihat Trida seterpuruk ini.",
    "Ia benar-benar hancur, seluruh pertahanan dirinya terkoyak habis; beban kepedihan hatinya tumpah ruah saat ia diam-diam runtuh tepat di sebelahmu.",
    "Kamu nggak apa-apa?",
    "Trida tidak mendongak saat kamu memanggilnya.",
    "Untuk beberapa detik yang terasa begitu menyiksa, satu-satunya tanda kehidupan hanyalah kedutan halus jemarinya yang mengepal erat di pangkuannya.",
    "Ketika ia akhirnya mengangkat kepalanya sedikit, kedua matanya tampak berkaca-kaca menahan tangis, sengaja menghindari tatapanmu dan terpaku pada goresan noda di meja kayu.",
    "Aku... iya. Aku nggak apa-apa kok,",
    "Trida membalas lirih dengan suara tercekat yang sama sekali tidak meyakinkan.",
    "Ia memaksakan seulas senyum getir yang begitu rapuh dan tak sampai ke matanya, sebelum menggelengkan kepalanya samar.",
    "Udah... nggak usah dipikirin sekarang ya. Kita harus kelarin ini sebelum bel bunyi. Ayo kita... kita selesaikan tugasnya.",

    # 187 - 206 (Trida holding by a thread, alternative choices: "What did you just do?" / Silence)
    "Kamu melihat tangan Trida memungut kembali pensilnya, buku-buku jarinya memutih saking eratnya menggenggam, dan ia memaksa sepasang mata oranyenya menatap kembali garis-garis kosong di kertas.",
    "Namun kamu bisa membaca topeng kerapuhan itu dengan jelas.",
    "Kamu tahu betul ia sedang tidak bisa berpikir jernih untuk mengerjakan tugas; Trida hanya sedang mati-matian menahan diri agar tidak runtuh, takut jika ia bergerak atau berbicara sepatah kata lagi, ia akan benar-benar pecah menangis di depan semua orang.",
    "Duduk tepat di sampingnya, gelombang rasa tak berdaya yang begitu dalam menyapu hatimu.",
    "Kamu ingin memperbaiki keadaan, meruntuhkan tembok pertahanannya dan mengusir rasa malu yang mencekiknya, namun melihatnya meringkuk ke dalam cangkang pelindungnya membuatmu bingung bagaimana cara menggapainya.",
    "Kamu barusan ngapain?",
    "Trida tidak langsung merespons.",
    "Ia mendadak mematung kaku, pensil di tangannya melayang kikuk di atas kertas kosong bagai bandul jam yang tertahan di titik tertinggi ayunannya.",
    "Celotehan cemas yang biasanya selalu mengisi ruang seketika lenyap tak bersisa.",
    "Sebaliknya, ketegangan yang pekat memancar dari tubuhnya; rahangnya mengatup rapat, dan dahinya berkerut dalam menunjukkan pergulatan batin yang berkecamuk hebat di dalam kepalanya.",
    "Saat ia akhirnya bergerak, gerakannya bukan untuk menatap wajahmu.",
    "Sepasang mata Trida bergeser cemas menghindar, melirik panik ke arah jendela luar lalu buru-buru menunduk menatap meja seolah permukaan kayu itu bisa memberinya jalan keluar dari tatapanmu.",
    "Ia menelan ludah dengan susah payah, gerakan di lehernya memperlihatkan kepedihan yang ia tahan, dan jemarinya mencengkeram kuat kain celana seragamnya hingga buku-buku jarinya memutih.",
    "Keheningan pekat menyelimuti kalian berdua, waktu terasa merayap lambat dan berubah menjadi ketegangan canggung yang merayap ke pikiranmu sendiri, memperberat beban kata-kata yang tak terucap.",
    "Apa aku salah ngomong ya...",
    "Apa nanya 'kamu barusan ngapain' tadi kedengeran terlalu galak?",
    "Apa aku kedengeran kayak lagi nginterogasi?",
    "Tiap detik yang berlalu tanpa sepatah kata jawaban terasa begitu memekakkan telinga.",
    "Kamu mulai meragukan nada bicaramu sendiri, cemas jangan-jangan kamu baru saja membuat situasi yang sudah rapuh ini menjadi sepuluh kali lebih buruk.",
    "Trida tetap menundukkan kepalanya, tenggelam dalam kepedihan hatinya sendiri, meninggalkanmu terdiam dalam pusaran overthinking.",

    # 207 - 220 (Silence alternative & bell rings, chapter end)
    "Saat kamu memilih untuk tetap diam, keheningan yang menindih menyelimuti meja kalian, jatuh bagai selimut tebal yang membungkam sisa-sisa bisikan obrolan.",
    "Trida menghembuskan napas gemetar yang lolos tertahan dari bibirnya.",
    "Menyadari ketiadaan respons darimu, ia perlahan mengalihkan kembali perhatiannya ke buku paket yang terbuka di hadapannya, matanya yang memerah menatap nanar deretan kertas tebal itu seakan mencari jawaban hidup di sana.",
    "Ia berusaha kembali mengerjakan tugas, namun tiap gerakannya terasa begitu lambat dan menyiksa.",
    "Setiap goresan tangannya dipenuhi keraguan dan kekakuan yang nyata.",
    "Ia bersusah payah menuliskan sebaris kalimat, lalu terpaku menatapnya, melamun dalam waktu yang terasa bagai keabadian.",
    "Setelah jeda panjang, ia menghapus setengah tulisannya; jemarinya bergetar saat menulis ulang, seakan takut goresan yang tak sempurna akan memicu komentar pedas lainnya.",
    "Bahunya tetap menegang rapat, membungkuk ke dalam seakan berusaha melindungi dirinya dari tatapan orang-orang di ruangan itu.",
    "Di sampingnya, kamu menyaksikan perjuangan pedih dan melelahkan yang ia curahkan hanya demi merangkai beberapa patah kata.",
    "Sebagian hatimu terenyuh ingin mengatakan sesuatu, mengangkat beban rasa malu yang menindihnya, namun berbicara terasa begitu berbahaya—seolah bisa menghancurkan sisa-sisa kendali diri yang sedang dipertahankan Trida mati-matian.",
    "Maka pada akhirnya kamu hanya bisa mengirimkan dukungan dalam diam, doa tulus dari lubuk hatimu yang berharap bisa tersampaikan lewat kehangatan batin kepada Trida.",
    "Keheningan yang menyakitkan di meja itu terus bertahan hingga bel pulang sekolah akhirnya berdering memecah suasana kelas.",
    "Tanpa mengucap sepatah kata pun, Trida langsung menyapu buku-bukunya masuk ke dalam tas, tatapannya tetap terpaku ke lantai saat ia melangkah cepat keluar dari pintu kelas.",
    "Kamu berdiri sendirian di samping mejamu, rasa sesak yang berat masih membekas mengganjal di dadamu.",
    "Kamu tahu betul bahwa kamu tidak bisa membiarkan masalah ini menggantung begitu saja..."
]

week7_strings = {
    "Right...": "Iya juga sih...",
    "Obviously not": "Jelas nggak lah",
    "Of course, we don't": "Tentu aja nggak",
    "Go To Grapos": "Pergi ke Lapangan Grapos",
    "Stay in The Class": "Tetap di Dalam Kelas",
    "Are you okay?": "Kamu nggak apa-apa?",
    "What did you just do?": "Kamu barusan ngapain?",
    "Say Nothing": "Diam saja",
    "Did I say the wrong thing...": "Apa aku salah ngomong ya...",
    "Was asking 'what did you just do' too aggressive?": "Apa nanya 'kamu barusan ngapain' tadi kedengeran terlalu galak?",
    "Did I sound too interrogating?": "Apa aku kedengeran kayak lagi nginterogasi?"
}

with open("/tmp/week7.rpy.json", "r", encoding="utf-8") as f:
    items = json.load(f)

d_idx = 0
for item in items:
    if item["type"] == "dialogue":
        if d_idx < len(week7_translations):
            item["indonesian"] = week7_translations[d_idx]
            d_idx += 1
        else:
            print(f"Warning: more dialogues than translations at index {d_idx}")
    elif item["type"] == "string":
        eng = item["english"]
        if eng in week7_strings:
            item["indonesian"] = week7_strings[eng]

with open("/tmp/week7.rpy.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

subprocess.run(["python3", "tools/translate_helper.py", "apply", "game/tl/indonesian/week7.rpy", "/tmp/week7.rpy.json"], check=True)
print(f"Updated week7.rpy.json: {d_idx} dialogues, {len(week7_strings)} menus.")
