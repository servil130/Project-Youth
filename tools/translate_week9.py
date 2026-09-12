import json
import subprocess

week9_translations = [
    # 0 - 14 (Monday noon break bell, Trida's rhythm game hype)
    "Dentang bel istirahat sekolah bergema di sekeliling ruangan dengan ritme yang begitu familiar, menandakan tibanya jam istirahat siang pukul dua belas tepat.",
    "Setelah peristiwa berharga di malam Minggu kemarin, kembalinya rutinitas sekolah terasa begitu menenangkan dan menyegarkan kembali pikiranmu.",
    "Kamu meregangkan badan di kursimu menikmati hangatnya mentari siang setelah melewati jam pelajaran yang panjang, dan tepat saat itu, matamu menangkap sosok Trida yang melangkah mendekat dengan senyum semringah dan ponsel di tangan.",
    "Meskipun rasanya kamu sudah bisa merasakan energi lincahnya bahkan sebelum sosoknya benar-benar terlihat oleh matamu.",
    "[player_name]!!!",
    "Suara lantang Trida yang menggelegar terdengar semakin nyaring karena wajahnya yang begitu dekat dengan wajahmu, matanya membelalak gembira dan napasnya terengah-engah dengan bulir keringat yang membasahi lehernya.",
    "Kamu sempat bertanya-tanya apa yang sebenarnya dilakukan Trida di dalam kelas tadi sampai bisa seheboh ini.",
    "Coba lihat ini—a—aku akhirnya berhasil dapet full combo pertama di lagu level 25!",
    "Kamu bahkan belum sempat menjawab sebelum Trida buru-buru menyodorkan layar ponselnya tepat di depan matamu.",
    "Kamu sigap memegang lengan Trida dan memundurkan layarnya sedikit sebelum matamu mendadak buta akibat terpaan cahaya neon mencolok dari game yang ia pamerkan.",
    "Kamu menyipitkan mata membaca teks bertuliskan 'FULL COMBO' yang terpampang jelas di layar. Terlihat bahwa Trida baru saja memainkan game rhythm favoritnya, 'Splashy!Scene' pada tingkat kesulitan Expert.",
    "Peningkatan pesat banget kan, ya nggak?! Masih nggak nyangka aku bisa ngelewatin tangga nada rapat-rapat itu, tadi aku bener-bener nahan napas sepanjang lagu...!",
    "Trida tertawa puas penuh kebanggaan, seringai girang tersungging di sudut bibirnya; kamu bisa melihat binar bahagia yang berpendar di matanya.",
    "Nada bicaranya terdengar jenaka, namun kamu bisa merasakan betapa ia benar-benar sangat bahagia atas pencapaian barunya itu.",
    "Pasti dong! Hehe, gila kan kerennya?",

    # 15 - 26 (Playful banter & player staring)
    "Hei! Maksudmu gimana coba ngomong begitu?!",
    "Bibir Trida mengerucut cemberut kekanak-kanakan seraya merengek manja di tiap kata yang ia ucapkan.",
    "Meskipun itu adalah reaksi khas Trida saat digoda, kamu tak kuasa merasa bahwa ekspresinya kali ini terlihat jauh lebih menggemaskan daripada biasanya.",
    "Kamu melepaskan tawa kecil yang geli.",
    "Cuma nggak nyangka aja reaksimu bakal seheboh ini.",
    "Ya wajar dong kalau aku heboh, pencapaian luar biasa gini masa nggak dirayain!",
    "Trida mendengus bangga, lalu kembali menatap layar ponselnya dengan senyuman berseri-seri seraya jemarinya berkali-kali mengambil tangkapan layar seolah bukti itu bisa lenyap sewaktu-waktu.",
    "Perubahan drastis dari sosok rapuh yang menangis di kamarmu kemarin begitu kontras terlihat di setiap gerak-gerik lincahnya saat ini.",
    "Saat alis Trida terangkat riang, kamu mendapati dirimu kembali terpaku memperhatikan setiap detail gerakannya dengan saksama.",
    "Bagaimana kakinya bergeser ke kanan dan ke kiri di lantai, bagaimana kedua ibu jarinya lincah melayang di atas layar ponsel, bagaimana pipinya berkedut menahan senyuman yang begitu lebar...",
    "Uh—[player_name]? Mukaku ada yang aneh ya?",

    # 27 - 40 (Trida leans in, glasses boy approaches)
    "Lamunanmu buyar saat wajah Trida mencondong begitu dekat hingga kamu bisa melihat semburat merah muda yang hangat mulai menjalar di daun telinganya; senyum bingung dan kerutan dahi menghiasi wajahnya saat kamu tersadar bahwa sedari tadi kamu sudah menatapnya cukup lama.",
    "Maaf, tadi aku lagi melamun.",
    "Nggak ada apa-apa kok.",
    "Cuma... lagi mikir aja.",
    "Kamu melontarkan alasan kilat itu dengan agak serak, terdengar sama sekali tidak meyakinkan jika dinilai dari tawa kecil Trida yang menggoda.",
    "Padahal tadi tatapanmu fokus banget ngeliatin aku lho...",
    "Meski kalimatnya bernada gurauan, suara lembut Trida mengisyaratkan kehangatan yang berbeda.",
    "Pandangannya sempat teralihkan sesaat, bibirnya terkatup rapat seolah sedang menahan kata-kata seraya jemarinya memainkan tombol samping ponselnya.",
    "Pertanyaan yang tak terucap menggantung lembut di udara, tentang bagaimana perasaan Trida kembali masuk ke dalam kelas ini.",
    "Trida mulai mengalihkan kembali perhatiannya ke permainannya. Ia menyandarkan sikunya di atas permukaan kayu mejamu yang kasar dan membungkuk agar nyaman bermain, mempersempit jarak di antara kalian berdua.",
    "Kamu merasakan tenggorokanmu tercekat, ingin sekali membuka obrolan, namun melihat betapa tenangnya Trida di dekatmu saat ini, kesempatan itu terus tertahan karena takut merusak suasana nyaman itu.",
    "Hm... Coba ah mainin lagu level 27 yang ini...",
    "Saat Trida kembali larut bermain, tatapan matamu secara naluriah menyapu ke sekeliling kelas, penasaran mencari keberadaan teman sekelompokmu tempo hari.",
    "Setelah melihat teman-teman sekelas lainnya yang asyik mengobrol riuh, matamu menangkap teman sekelompokmu yang berkacamata itu tengah menatap kedua tangannya yang gelisah dengan raut wajah datar sebelum ia beranjak bangkit dari tempat duduknya.",
    "Pandanganmu bergerak cepat bergantian antara Trida dan teman sekelompokmu itu. Kamu melihat cowok itu tampak melangkahkan kakinya mendekat ke arah mejamu. Kamu...",

    # 41 - 54 (Branching approach: look away, call out, or watch)
    "Kamu buru-buru memalingkan kembali pandanganmu ke arah Trida.",
    "Kamu melihat ia sudah mulai memainkan lagu baru di hadapanmu tanpa menyadari sekelilingnya; ketukan ritmis jemarinya berpadu cepat mengikuti dentuman lagu ceria yang mengalun agak terlalu kencang dari pengeras suara ponselnya.",
    "Kamu mencondongkan tubuh ke depan untuk melihat chart nada yang sedang coba diselesaikan Trida, mengamati matanya yang fokus tajam dan ujung lidahnya yang sedikit digigit ke samping.",
    "Meskipun gaya bermain Trida tampak terburu-buru, kamu bisa melihat perkembangan kemampuannya kian terasah, sekecil apa pun itu.",
    "Halo di sana!",
    "Ah—[player_name]...",
    "Kamu melongok dari balik posisi Trida yang sedang fokus bermain, berharap bisa menarik perhatian cowok itu, dan tak lama kemudian ia menatap lurus ke arahmu dengan sedikit kerutan dahi.",
    "Sorot matanya yang menyipit sempat membuang muka seraya ia terus melangkah menghampiri kalian berdua, seolah agak terkejut mendengar sapaan mendadak darimu.",
    "Trida sama sekali tidak menyadari sepatah kata pun seruanmu tadi; ia masih asyik mengerahkan seluruh fokusnya pada lagu itu dengan mata terpaku lurus dan ketukan jemari yang gesit di layar ponsel.",
    "Kamu memilih memperhatikan langkah cowok itu dari kejauhan dalam diam.",
    "Ketukan cepat jemari Trida pada layar ponsel menarik perhatian cowok itu; ia melirik ke arah mejamu dan mendapati kamu tengah mengamatinya dengan saksama.",
    "Hal itu tampaknya membuat si cowok agak salah tingkah; matanya yang menyipit melirik ragu bergantian antaramu dan teman-teman sekelas lainnya, langkah kakinya melambat penuh keraguan.",
    "Tak butuh waktu lama hingga cowok berkacamata itu akhirnya berdiri canggung di dekat meja kalian berdua, jelas-jelas ingin berbicara, namun ragu menyela melihat Trida yang sedang mati-matian menaklukkan lagu level 27 itu.",
    "Kamu menghela napas lalu mengetuk pelan permukaan meja untuk menarik perhatian Trida.",

    # 55 - 67 (Interrupting rhythm game & surprise)
    "Trida, matiin dulu Splashy-nya sebentar, kamu—",
    "Tunggu bentar, tahan dulu!! Dikit lagi mau tamat nih lagunya, tolonglah...!",
    "Trida memohon panik penuh semangat tanpa mengalihkan pandangannya dari layar, sapuan jarinya bergerak semakin membabi-buta saat alunan lagu mencapai klimaksnya.",
    "Orang yang melihat pasti bakal mengira ia sedang bertarung hidup dan mati melawan bos terakhir di game RPG, padahal saat kamu melirik bar nyawa di game itu, tinggal satu kesalahan kecil saja ia bakal langsung game over seketika.",
    "Kamu saling bertukar pandang heran dengan si cowok berkacamata yang tengah membetulkan letak kacamatanya.",
    "Trida, tolong dengerin dulu—",
    "Tepat saat kamu berniat menyela untuk kedua kalinya, Trida mendadak menegakkan punggungnya dan meletakkan ponselnya ke atas meja, menghembuskan napas panjang nan lega seiring berlalunya nada terakhir lagu.",
    "Fuihh, akhirnya kelar juga...",
    "Seolah baru kembali tersadar ke dunia nyata, Trida mengerjapkan matanya beberapa kali lalu menoleh ke samping, tempat cowok berkacamata itu tengah menatapnya dengan senyum simpul kecil, menahan tawa melihat kekonyolan situasi barusan.",
    "WAAAH! Kaget, ngapain di situ—!",
    "Trida terlonjak kaget melihat kemunculan mendadak itu, memekik kencang tanpa sadar.",
    "Nah kan, dari tadi udah dibilangin juga...",
    "E—eh, kamu... Maaf ya...",

    # 68 - 84 (Glasses boy's apology & reconciliation)
    "Trida mengalihkan pandangannya menatap cowok itu, berusaha mempertahankan senyum kecil meski rasa canggung dan bersalah masih tampak jelas dari nada suaranya yang bergetar dan jemarinya yang gelisah.",
    "Sorot mata cowok itu melembut melihat gelagat Trida yang serba salah; ia berhenti sejenak sebelum berbicara dengan suara pelan dan tenang.",
    "Nggak apa-apa kok, santai aja, nggak usah dipikirin. Cuma...",
    "Cowok itu berdeham pelan seraya menunduk menatap kedua tangannya sendiri.",
    "A—aku cuma mau ngomong... kamu tahu kan, soal tugas kelompok kemarin...",
    "Ia berbicara agak terbata-bata dengan nada yang sedikit tertahan. Trida menahan napasnya, menunggu kalimat kelanjutannya.",
    "...Aku mau minta maaf, Trida... soal omonganku pas diskusi kelompok kemarin.",
    "...!",
    "Aku cuma... waktu itu rasa bingungku berubah jadi emosi dan aku malah kelepasan ngomong kasar, padahal harusnya aku bisa... bersikap lebih dewasa dan santai.",
    "Ketegangan di wajah Trida seketika mencair mendengar permintaan maaf yang begitu tulus itu; matanya menatap cowok itu seraya menghembuskan napas lega.",
    "Nggak... nggak apa-apa kok. Maksudku, aku juga salah udah bikin beban buat kelompok kemarin, aku paham kok...",
    "Hei, jangan terlalu menyalahkan dirimu sendiri gitu. Lagian itu cuma tugas kecil biasa kan?",
    "Cowok itu menyunggingkan senyum tipis yang canggung, nada suaranya terdengar ramah dan ringan—senyuman yang terasa jauh lebih pas menghiasi wajahnya yang biasanya kaku tanpa ekspresi.",
    "Trida tampak sama terkejut dan senangnya sepertimu.",
    "...Iya, makasih banyak ya.",
    "Nggak, justru a—aku yang harusnya berterima kasih... jujur, kejadian itu bikin aku sadar betapa judes dan nggak pekanya aku selama ini. Mungkin kalau nggak ada kejadian itu, aku nggak bakal pernah sadar...",
    "Kamu memperhatikan bagaimana pembawaan cowok itu menjadi jauh lebih santai saat mengobrol dengan Trida; senyuman alami tetap bertengger di wajahnya saat ia larut dalam obrolan hangat itu.",

    # 85 - 99 (Reconciliation closure, running to canteen)
    "Beneran nih...? Ya ampun... padahal aku nggak ngelakuin hal spesial apa-apa, tapi... aku seneng banget kalau itu bisa ngebantu kamu... dengan cara apa pun!",
    "Rasa tak percaya Trida yang membuncah bahagia membuat suasana di sekitar kalian kembali terasa begitu lega dan hangat. Cowok itu mengangguk pelan sebelum menoleh menatapmu.",
    "Oh iya, dan... makasih juga ya udah jagain situasi kita tetap adem.",
    "Bukan masalah kok, aku senang kalian berdua akhirnya bisa ngobrol baik-baik.",
    "Iya, rasanya plong banget sekarang...",
    "Uhm, kalau kalian nggak keberatan, perutku udah mulai... laper nih, sampai ketemu lagi nanti ya kalian berdua.",
    "Cowok itu buru-buru pamit undur diri, mengingatkan kalian berdua bahwa jam istirahat masih berlangsung. Mendengar kata lapar, mata Trida seketika berbinar cerah, dan kamu pun baru tersadar bahwa perutmu sedari tadi juga sudah mulai keroncongan.",
    "Sampai jumpa nanti...!",
    "Mumpung dia udah ngingetin soal makan... yuk cari makan sekarang.",
    "Sepemikiran banget! Ayo buruan, aku udah kelaparan parah nih!",
    "Kamu bangkit berdiri dari kursimu, sudah tahu pasti bahwa Trida akan langsung menarikmu keluar dari kelas.",
    "Ia meraih pergelangan tanganmu dan berlari kecil menyusuri lorong bersamamu, matanya masih saja terpaku pada layar ponsel saat menuntunmu melangkah tanpa memperhatikan jalan.",
    "Bisa nggak sih matamu ngelihat jalanan sedikit napa...",
    "Bentar dulu, banner gacha baru di Splashy ini keren banget lho...!",
    "Trida menuntunmu menuju area kantin yang riuh. Meski sempat menyenggol satu anak lain di perjalanan, ia dengan cekatan mengantongi ponselnya dan melangkah mantap menghampiri stan mi.",

    # 100 - 118 (Mie Aceh order, forgotten wallet, Julia appears)
    "Bu, pesan Mi Goreng Aceh-nya satu porsi ya, pakai telur ceplok!",
    "Cukup satu lirikan pada gaya memesan Trida yang penuh semangat itu, ibu penjual stan sudah langsung sigap menyalakan kompor dan bersiap memasak.",
    "Kamu duduk di bangku panjang terdekat dan bersandar santai sementara Trida bergerak gelisah ke sana-kemari karena tak sabar menunggu.",
    "Kamu udah langganan banget ya di situ sampai hafal di luar kepala? Ibunya tadi bahkan nyaris nggak nengok mukamu lho.",
    "Hahaha, jelas dong! Coba kalau ini stan minuman boba, kartu member punyaku pasti udah penuh cap stempel dari kapan tahu!",
    "Iya deh, percaya...",
    "Sebelum kamu sempat memutuskan mau pesan makan apa, kamu melihat tangan Trida meraba-raba saku celananya yang ketat dengan raut wajah kebingungan.",
    "Gawat! Kayaknya dompetku ketinggalan—nggak, ini fiks dompetku beneran ketinggalan di kelas!",
    "Sungguh mengejutkan sekali...",
    "Jangan ke mana-mana ya, tunggu di sini!",
    "Bagai hembusan angin rahasia, Trida langsung melesat kencang membelah kerumunan orang bagai daun yang tertiup badai, hingga sosoknya menghilang dari pandangan menuju lorong kelas.",
    "Kini kamu tinggal sendirian duduk di bangku itu, menunggu pesanan mi milik Trida siap dihidangkan.",
    "Eh, halo [player_name]! Udah lama ya nggak ketemu!",
    "Julia menyapamu dengan nada yang terdengar jauh lebih ceria dan antusias dibanding biasanya untuk ukuran orang yang awalnya sangat pendiam sepertinya.",
    "Gadis itu melangkah menghampiri bangku kosong di sebelahmu dan mendudukkan dirinya di sana.",
    "Uhm, gimana kabarmu belakangan ini...? Maksudku, adaptasi sama kehidupan sekolah barumu?",
    "Iya, paham banget kok... Banyak hal baru yang harus dibiasakan kan ya...?",
    "Wah, syukurlah kalau begitu...! Orang-orang di sini ramah-ramah banget kan?",
    "Begitu ya, tapi seenggaknya jauh lebih baik daripada ngerasa tertekan kan...!",

    # 119 - 137 (Julia asks the big question: "Who is Trida to you?")
    "Kalau aku pribadi sih lagi nggak sabar nungguin bulan depan, tahu sendiri kan, ada Inktober dan segala macem... Kulihat belakangan ini kamu juga makin akrab banget ya sama Trida...",
    "Ucapan Julia menggantung pelan saat ia menyebut nama Trida; jeda hening yang sarat makna menyusul saat pandangan matanya tertunduk menatap ujung sepatunya.",
    "Iya, emangnya kenapa sama aku dan Trida?",
    "Oh, nggak kok, cuma... sejujurnya, aku udah merhatiin kalian berdua makin hari makin dekat banget.",
    "Kalian berdua tuh kelihatan serasi banget kalau barengan. Tiap kali ngelihat kalian bercanda bareng, suasananya langsung terasa lebih hidup, dan aku nggak bisa bayangin kalau kalian sampai pisah. Makanya aku sempat penasaran...",
    "Julia mendadak menolehkan kepalanya menatapmu lurus-lurus, ekspresi wajahnya yang biasanya malu kini berganti sorot mata yang begitu bersungguh-sungguh dan mantap.",
    "Mungkin ini kedengarannya terlalu to the point ya, tapi kalau kamu nggak keberatan buat jujur sedikit ke aku...",
    "...Sebenarnya Trida itu siapa sih buat kamu, [player_name]?",
    "Kamu terbata-bata mengungkapkan perasaan jujurmu, mengenang kembali betapa seringnya momen-momen kecil bersama Trida berhasil membuat jantungmu berdegup liar tak keruan.",
    "Mulai dari candaan konyol, momen-momen manis yang menyejukkan, hingga luapan emosional di malam Minggu kemarin di kamarmu... semuanya bermuara pada pengakuan pertamamu tentang perasaanmu terhadap Trida di hadapan Julia.",
    "Begitu ya rupanya...",
    "Julia tersenyum simpul mendengar pengakuan hatimu, menghembuskan napas panjang dengan rasa lega yang teramat sangat.",
    "...Kenapa senyum-senyum gitu? Jangan disebar-sebarin ke orang lain lho ya.",
    "Tentu aja nggak bakal kusebar! Tuh kan bener... dari awal aku udah punya firasat kamu bakal jawab begitu. Dari hasil pengamatanku selama ini, caramu menatap Trida itu bener-bener nggak bisa dibohongi...!",
    "Kalau boleh jujur juga, dulu aku sempat punya sedikit pengalaman asmara sama teman dekatku sendiri, jadi aku paham banget kalau sekarang perasaanmu pasti lagi campur aduk nggak karuan.",
    "Oh! Begitu ya... iya sih, tapi aku nggak nyangka aja kamu bakal sepeka ini.",
    "Ahaha iya, ceritanya agak panjang sih, tapi—bukan itu poin utamanya. Kalau kamu izinkan, aku pengin ngasih sedikit saran atau pandanganku nih.",
    "Karena... menurutku kalian berdua bener-bener bisa jadi pasangan yang sangat istimewa.",
    "Iya, dengan senang hati... makasih sarannya.",

    # 138 - 156 (Julia's relationship analysis & validation)
    "Ini cuma sedikit analisaku aja sih, tapi kurasa Trida itu paling merasa nyaman dan jadi dirinya sendiri pas lagi ada di dekatmu.",
    "Dia emang selalu senyum dan ceria ke semua orang, itu bener, tapi pas lagi bareng kamu, senyuman itu kelihatan mengalir begitu alami tanpa paksaan.",
    "Menurutku Trida sangat menghargai betapa sabar dan pengertiannya dirimu; dia ngerasa dihargai sebagai sosok yang setara, bukan seseorang yang dituntut harus selalu menyenangkan orang lain.",
    "Selama kamu terus jadi tempat bersandar yang aman buat Trida, aku rasa bukan hal yang mustahil kalau...",
    "...Trida sebenarnya punya perasaan yang sama terhadapmu.",
    "Kamu... beneran mikir begitu?",
    "Ya, itu yang kulihat sejauh ini. Aku malah bakal heran banget kalau sampai Trida ngerasa sebaliknya, apalagi kalau ngelihat cara dia menatapmu selama ini.",
    "Lagian, kamu bakal jadi pasangan yang luar biasa sempurna buat Trida kok.",
    "Begitu ya... Kelihatan banget kalau Trida bener-bener sosok yang sangat berharga buat kamu.",
    "Mungkin agak aneh ya mengomentari hubungan persahabatan orang lain, tapi aku punya firasat kuat kalau kalian berdua bakal selalu saling mendukung sampai kapan pun.",
    "Kata-kata bijak Julia terdengar begitu tak terduga datang dari sosok pendiam sepertinya, namun kamu tak bisa memungkiri kehangatan tulus yang terpancar dari ekspresi dan nada bicaranya.",
    "Iya kah? Dari mana kamu bisa tahu...?",
    "Menurutku kalian berdua saling mengeluarkan sisi terbaik dari diri masing-masing; kalian kelihatan paling rileks dan damai pas lagi berdua di sekolah.",
    "Maksudku, Trida emang anak yang gampang gaul, tapi dia kelihatan jauh lebih tenang dan jujur tiap kali ngobrol berdua sama kamu. Di saat itulah kepribadian aslinya bener-bener bersinar indah.",
    "Bisa dibilang kepribadian kalian berdua tuh saling melengkapi dengan begitu sempurna.",
    "Intinya yang mau kusampaikan... jangan pernah lepasin ikatan berhargamu sama Trida ya, janji?",
    "Makasih banyak ya, Julia... Aku seneng banget dengar pandanganmu.",
    "Sama-sama, cuma pengin yang terbaik aja buat kalian berdua!",
    "Tepat saat itu, suara napas terengah-engah dan derap langkah kaki terdengar memburu dari arah belakang.",

    # 157 - 176 (Trida returns with wallet & Mie Aceh, Nimecart banter)
    "Aku baliiik!!",
    "Seruan lantang Trida membelah riuhnya kantin saat ia berlari kencang menghampiri kalian, mengacungkan dompet yang berhasil ia temukan di tangannya laksana medali emas kejuaraan.",
    "Hanya dalam hitungan detik, Trida meluncur melewati bangku kalian berdua, membungkuk terengah-engah memburu udara seraya menghitung lembaran uang di tangannya.",
    "Panjang umur baru aja diomongin...",
    "Kurasa obrolan rahasia kita tadi mending kita simpan berdua aja ya, gimana?",
    "Julia tertawa kecil dengan binar usil di matanya, seringai penuh artinya menggoda rasa malumu.",
    "Tak lama berselang, Trida kembali ke bangku kalian membawa kotak stirofoam berisi tumpukan mi goreng yang harum mengepul dengan telur mata sapi yang menggoda selera.",
    "Maaf ya bikin kalian nunggu lama! Sumpah deh aku bener-bener {i}nggak{/i} inget kalau dompetku bisa nyelip di kolong meja gitu—",
    "Eh, Julia? Halo, Julia! Nggak nyadar kamu di sini juga!",
    "Ah, halo Trida...! Udah lama ya kita nggak ngobrol bareng?",
    "Iya banget dong!",
    "Kamu sudah bisa melihat roda antusiasme mulai berputar cepat di kepala Trida begitu bertemu sesama pecinta karya fiksi, senyumnya melebar penuh energi.",
    "Tahu nggak, aku udah nonton serial Nimecart yang tempo hari kamu rekomendasikan lho! Ah, apa itu namanya—yang seri Sanity itu kan?",
    "Wah! Kamu beneran nonton? Gimana menurutmu ceritanya?",
    "SERU BANGET! Plot storytelling-nya keren parah, terus interaksi improvisasi karakternya pada jago-jago banget—asli penasaran banget gimana kelanjutan episode-episode depannya nanti!",
    "Kan bener! Pembangunan dunianya subtle tapi dapet banget nuansanya. Wah, kalau dibahas bisa panjang nih, tapi—bentar, karakter favoritmu siapa, Trida?",
    "Aduh, semuanya punya latar belakang cerita yang menarik banget sih...",
    "Kamu terus mengamati dalam diam obrolan seru penuh antusias antara Trida dan Julia yang berlangsung lebih lama dari yang diperkirakan.",
    "Ini adalah momen paling lepas dan alami yang pernah kamu lihat dari sosok Julia, dan kamu sekali lagi dibuat kagum oleh pesona energi ceria Trida yang dengan mudahnya membuat orang di sekitarnya merasa nyaman.",
    "Kamu menikmati gelak tawa dan pertukaran pendapat mereka, meresapi hangatnya atmosfer positif yang mengalir.",

    # 177 - 194 (Playful questioning, canteen warmth, chapter closure)
    "Oh iya—ngomong-ngomong... tadi sebelum aku datang, kalian berdua lagi asyik ngomongin apa sih sebenarnya?",
    "Tadi kita cuma ngobrol santai biasa aja kok.",
    "Hmm, kenapa ya rasanya susah banget buat percaya? Kalian berdua kelihatan jauh lebih akrab dan nggak canggung sekarang.",
    "Hehehe...",
    "Tuh kan, ketawanya Julia aja kedengeran mencurigakan banget!",
    "Tadi Julia cuma lagi cerita soal Nimecart ke aku.",
    "Masa sih? Nggak nyangka deh kamu tipe orang yang suka nonton Nimecart.",
    "Coba sebutin satu hal tentang serialnya kalau emang bener!",
    "Uhm... itu, seri yang... Insanity itu kan ceritanya—",
    "Pfft, hahaha! Nyebut judul serinya aja kamu udah salah total gitu!",
    "Hehehe...",
    "Tadi kita berdua cuma lagi tersiksa nungguin kamu yang lama banget balik ngambil dompet.",
    "WOI! Kamu nggak lihat apa tadi lariku secepat kilat gitu?!",
    "Mau lari secepat kilat pun nggak bakal bisa nyelamatin matamu yang lambat nyari barang.",
    "Sumpah deh tadi dompetnya bener-bener nggak kelihatan di mana-mana!",
    "Ehehehe...",
    "Kalian bertiga tertawa riang bersama di tengah hangatnya aroma mi goreng dan riuhnya obrolan anak-anak di kantin.",
    "Saat bel masuk kelas kian mendekat, kamu menatap wajah Trida—tampak jauh lebih bahagia, lebih lepas, dan terasa begitu dekat dengan hatimu dibanding hari-hari sebelumnya."
]

week9_strings = {
    "Woah, you actually did it?!": "Wah, kamu beneran berhasil?!",
    "So THAT'S what got you fired up, huh?": "Jadi ITU yang bikin kamu heboh banget dari tadi, ya?",
    "Sorry, I was spaced out": "Maaf, tadi aku lagi melamun",
    "It's nothing": "Nggak ada apa-apa kok",
    "Just… thinking": "Cuma... lagi mikir aja",
    "Just... thinking": "Cuma... lagi mikir aja",
    "Look away and pretend you weren't watching": "Buang muka dan pura-pura nggak melihat",
    "Call out to the boy": "Panggil cowok itu",
    "Watch him get closer": "Perhatikan langkahnya yang mendekat",
    "It's been a bit much…": "Rasanya agak berat sih...",
    "It's been a bit much...": "Rasanya agak berat sih...",
    "I've been having fun!": "Seru banget kok!",
    "I'm doing just alright": "Biasa aja, aman-aman aja",
    "Someone… I want to be more than friends with": "Seseorang... yang kuharapkan bisa lebih dari sekadar teman",
    "Someone... I want to be more than friends with": "Seseorang... yang kuharapkan bisa lebih dari sekadar teman",
    "A close friend I trust a lot": "Sahabat dekat yang sangat kupercaya",
    "Nothing important": "Nggak ada yang penting kok",
    "About Nimecart": "Soal Nimecart",
    "About how slow you were": "Soal kamu yang lama banget baliknya"
}

with open("/tmp/week9.rpy.json", "r", encoding="utf-8") as f:
    items = json.load(f)

d_idx = 0
for item in items:
    if item["type"] == "dialogue":
        if d_idx < len(week9_translations):
            item["indonesian"] = week9_translations[d_idx]
            d_idx += 1
        else:
            print(f"Warning: more dialogues than translations at index {d_idx}")
    elif item["type"] == "string":
        eng = item["english"]
        if eng in week9_strings:
            item["indonesian"] = week9_strings[eng]

with open("/tmp/week9.rpy.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

subprocess.run(["python3", "tools/translate_helper.py", "apply", "game/tl/indonesian/week9.rpy", "/tmp/week9.rpy.json"], check=True)
print(f"Updated week9.rpy.json: {d_idx} dialogues, {len(week9_strings)} menus.")
