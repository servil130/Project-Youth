import json
import subprocess

week5_translations = [
    # 0 - 11 (Morning CFD atmosphere)
    "Sinar matahari pagi terasa hangat dan lembut menyelinap di sela-sela pepohonan di sepanjang jalan.",
    "Hari ini hari Minggu, hari di mana deru bising mesin kendaraan sirna, berganti keriuhan tawa canda, gemerincing sepeda, dan semerbak aroma jajanan kaki lima.",
    "Saat kamu melangkah menelusuri CFD, seluruh aroma dan suara yang berpadu seakan meluap memenuhi seluruh inderamu.",
    "Bahu jalan dipadati deretan tenda penjual yang menjajakan aneka kuliner khas dan berbagai pernak-pernik.",
    "Aroma sedap kuah soto ayam berpadu harmonis dengan segarnya jus buah dan harumnya sate yang dibakar di atas arang, bagai alunan partitur nada.",
    "Ini adalah akhir pekan pertama setelah berminggu-minggu yang kamu yakini akan menjadi akhir pekan terbaik.",
    "Kamu berjalan santai di tengah kerumunan, membiarkan langkah kakimu larut dalam arus suasana.",
    "Sesekali kamu berhenti memandangi lapak-lapak unik, memperhatikan anak-anak kecil yang riang memegang balon, hingga akhirnya ikut mengantre segelas es kopi.",
    "Semuanya terasa... begitu damai.",
    "Sembari menggenggam minuman dingin di tanganmu, kamu mengedarkan pandangan ke lautan manusia—dari rombongan keluarga hingga gerombolan pelajar yang berlalu-lalang.",
    "Lalu, matamu menangkap sosok yang tak asing berdiri di dekat sebuah stan pakaian.",
    "Didorong rasa penasaran dan keberanian untuk menyapa, kamu melangkah mendekat hingga mendapati Trida yang tengah bersandar di gantungan baju, tampak jauh lebih rileks dibanding hari-hari biasanya di sekolah.",

    # 12 - 23 (Meeting Cap Boy and Braided Girl)
    "...Beneran deh, aku ngabisin tiga jam cuma buat bikin tool bridge di Blender mau nurut. Pas kelar, jaring-jaring mesh punyaku malah remuk kayak kertas lecek.",
    "Itu mah kamunya aja yang asal ekstrusi face tanpa mikirin topologi yang bener, Bro.",
    "Saat pandangan Trida tertuju padamu sebelum teman-temannya menyadari, seulas senyum terkembang di wajahnya, menghantarkan sengatan rasa hangat yang tiba-tiba berdesir di perutmu.",
    "Matanya berbinar cerah bagai percikan api yang menyalakan ruangan, sebelum mulutnya kembali berceloteh riang.",
    "Eh, halo! Coba lihat siapa yang datang!",
    "Kedua temannya saling pandang sejenak sebelum menoleh untuk melihat apa yang sedang terjadi.",
    "Ini anak yang sering kulihat nongkrong bareng kamu seharian di lab itu kan, Trida?",
    "Udah deh, jangan bikin orang risih. Maafin dia ya—dia emang rada... aneh anaknya.",
    "Aku nggak aneh ya, aku ini cuma jeli mengamati sekitar. Beda jauh tahu, makasih banyak!",
    "Terserah apa katamu deh.",
    "Gadis itu memutar bola matanya malas, lalu kembali memusatkan perhatiannya padamu dengan senyuman ramah.",
    "Ngomong-ngomong, kamu sekelas sama kita kan ya?",

    # 24 - 34 (Player responds, mingling)
    "Iya, bener.",
    "Nggak, bukan.",
    "Kamu memilih tetap diam, memperhatikan dinamika obrolan mereka berdua.",
    "Kalian berdua tolong... tenang sedikit napa. Aku tahu kita baru kenal beberapa bulan, tapi mulai sekarang kalian harus coba ingat-ingat nama teman dong!",
    "Ini [player_name], dan iya, dia sekelas sama kita.",
    "Senang bertemu dengan kalian.",
    "Suasana langsung mencair; si cowok bertopi berhenti meledek, dan raut wajah si cewek berkepang seketika berubah bersahabat.",
    "Ah, salahku deh! Nggak ada niat buat nggak sopan kok. Maklum lah, aku emang susah nginget nama sama muka orang, hehe.",
    "Iya, anak-anak di RUS kan banyak banget. Senang bisa ketemu kamu di sini, [player_name].",
    "Kalian saling bertukar sapaan ringan seputar ramainya akhir pekan dan hawa gerah khas pagi hari.",
    "Untuk beberapa saat, kalian berempat larut menikmati riuhnya energi CFD, ditemani suara obrolan yang riuh dan denting peralatan masak di kejauhan.",

    # 35 - 47 (Friends excuse themselves, leaving Trida & player)
    "Tepat saat kamu mulai menikmati suasana, cowok bertopi itu mendadak menatap jam tangannya dengan mata membelalak lebar.",
    "Gila, waktu cepet banget lewat! Aroma makanan udah manggil-manggil namaku nih, harus buru-buru sebelum kehabisan!",
    "Oh, iya juga. Lagian tujuan kita jalan-jalan hari ini masih banyak kan.",
    "Gadis itu tersenyum simpul sebelum melirik bergantian ke arahmu dan Trida.",
    "Dari tatapannya, ia jelas-jelas menangkap sinyal tertentu sedari tadi, sebelum ia menyenggol pelan lengan si cowok, yang langsung dibalas dengan anggukan paham.",
    "Oke deh! Cabut dulu ya, Trida! Jangan kalap borong barang-barang nggak guna!",
    "Kedua teman itu saling bertukar senyum penuh arti sebelum akhirnya menghilang ditelan keramaian orang.",
    "Seiring kepergian mereka berdua, keheningan yang menyejukkan mendadak menyelimuti kamu dan Trida.",
    "Trida menghembuskan napas panjang yang terdengar heran sekaligus lelah, memperhatikan langkah kedua temannya yang menjauh.",
    "Kesambet apa sih mereka mendadak kabur ninggalin kita begitu aja?",
    "Tapi mereka aslinya orang baik kok, jadi nggak usah dipikirin ya.",
    "Ia mengalihkan perhatiannya seutuhnya padamu, dan kamu bisa melihat raut wajahnya melembut perlahan.",
    "Nggak nyangka juga bakal papasan sama kamu di sini...",

    # 48 - 60 (Walking together invitation)
    "Kukira kamu tipe orang yang lebih milih rebahan di kamar buat ngecas energi tiap hari Minggu. Gimana CFD-mu sejauh ini?",
    "Asyik banget kok, santai rasanya.",
    "Duh, beneran deh, relate banget. Rasanya otakku akhirnya bisa sedikit didefrag setelah sekian lama.",
    "Trida terdiam sesaat, memandangi jalur panjang CFD yang berkelok-kelok di depan, dihiasi tenda-tenda warna-warni dan harum makanan yang dipanggang.",
    "Ia tampak ragu, jemarinya mengetuk-ngetuk cemas pinggiran buku sketsa yang dibawanya.",
    "Sebenarnya... aku masih pengin keliling-keliling lagi sih. Kamu mau jalan bareng nggak?",
    "Boleh, ayo. Asyik juga jalan ada temannya.",
    "Wajah Trida seketika berseri-seri—bukan cuma sekadar senyuman biasa, tapi pancaran rasa lega yang tulus dan jujur.",
    "Ia bergegas memasukkan ponselnya ke dalam saku dan membetulkan posisi tali tasnya.",
    "Beneran nih? Tadinya sempat kepikiran kalau aku bakal ngeganggu waktumu.",
    "Kalau gitu, kujamin deh aku bakal jadi pemandu wisata terbaikmu di sini!",
    "Wah, sebuah kehormatan dong...",

    # 61 - 76 (Cireng, tripping, and banter)
    "Hawa lembap dan terik udara Kudus mulai terasa menyengat.",
    "Kamu dan Trida terus melangkah di antara lautan orang yang bergerak laksana gerombolan semut, diiringi keriuhan suara yang tak henti-hentinya bersahutan.",
    "Kedua tangannya aktif bergerak, membagikan sekantong cireng hangat kepadamu sambil dengan lincah berkelit menghindari orang-orang yang berpapasan.",
    "Jujur ya, ini jauh lebih seru daripada nongkrong di lab bareng kamu, berasa lagi jalan-jalan beneran!",
    "Namanya juga hari Minggu. Kita butuh refreshing buat menenangkan pikiran.",
    "Menenangkan pikiran ya... Pilihan yang bijak sih ketimbang cuma bengong komat-kamit di depan monitor seharian, hehe...",
    "Sambil berjalan mundur dengan tawa riang yang mengalir dari bibirnya, ia salah memperhitungkan trotoar dan mendadak kehilangan keseimbangan.",
    "Dengan ekspresi kaget yang terpampang di wajahnya, ia jatuh terjerembap ke tanah. Tawanya seketika lenyap saat tubuhnya meluncur di atas aspal dengan tangan terayun panik sebelum akhirnya berhenti berguling kikuk.",
    "AWWW!",
    "Waduh! Kamu nggak apa-apa?!",
    "Kamu sigap mencengkeram lengannya, membantunya bangkit sebelum tubuhnya menghantam kerasnya aspal.",
    "Ia berdiri tegak dengan wajah yang memerah padam laksana tomat rebus, terburu-buru menepuk-nepuk debu yang menempel di celana jinsnya.",
    "A—aku sengaja kok begitu tadi! Itu... lagi ngetes gaya gesek lantai doang. Penting banget tahu buat, um, prinsip dasar animasi, ya kan?!",
    "Kamu bener-bener kacau deh ah.",
    "Trida tertawa canggung, meski kedua pipinya masih merona merah terang.",
    "Berisik ah! Kakiku emang lagi lemas aja, paham? Pokoknya... awas ya kalau sampai bocor ke anak-anak lain!",

    # 77 - 91 (Vulnerability on the bench)
    "Saat tawa mereka perlahan mereda, kalian berdua akhirnya menemukan sebuah bangku taman yang jauh dari hiruk-pikuk keramaian.",
    "Trida menghempaskan tubuhnya ke bangku itu dan bersandar lunglai, tampak seperti prajurit yang baru saja pulang dari medan perang.",
    "Maaf ya energiku mendadak anjlok gini. Rasanya badanku bener-bener... remuk banget, tahu nggak?",
    "Wajar kok, acaranya rame banget padatnya. Nggak heran kalau kamu capek.",
    "Asli deh. Suasananya bikin kepalaku rasanya overstimulasi banget.",
    "Ia terdiam sejenak, tatapannya menerawang jauh menatap lautan orang di alun-alun yang seolah tak pernah ada habisnya berdatangan.",
    "Mungkin apa yang mau kuomongin ini kedengarannya random banget, tapi...",
    "Perasaan capek ini bikin aku ingat pas pertama kali nekat milih jurusan Animasi 3D.",
    "Kukira dari awal kamu udah pede banget di jurusan itu?",
    "Nggak sama sekali. Makin kudalami, rasanya makin... bikin kewalahan. Sampai kadang aku mikir, apa bener ini hal yang memang kumau sedari awal.",
    "Ia mendongak, menatap langsung ke matamu. Di sana terlihat senyuman tipis yang dibayangi rasa lelah dan pengakuan lirih akan kepenatan batinnya.",
    "Makanya kalau sendirian di kamar mikirin hal-hal kayak gitu, aku kadang takut banget bakal gagal menghadapi masa depanku nanti.",
    "Tapi pas kita ada di sini, di luar ruangan lab itu... anehnya rasa takut gagal itu nggak muncul sama sekali. Untuk sesaat, rasanya bebanku kayak terangkat sedikit.",
    "Ia terdiam sejenak, tatapan oranyenya yang teduh melembut saat menatapmu lekat-lekat.",
    "Makasih banyak ya buat hari ini.",

    # 92 - 107 (Passing on CFD walk / Meeting Sabian)
    "Kayaknya aku skip dulu deh kali ini. Lagi pengin nikmatin waktu sendiri sebelum minggu baru dimulai.",
    "Trida mengerjap, secuil raut kecewa sempat melintas di wajahnya sebelum ia dengan cepat menutupinya lewat anggukan maklum.",
    "Iya, nggak apa-apa, aku ngerti banget kok. Akhir-akhir ini tugas emang lagi gila-gilaan—kamu pastinya butuh ruang buat istirahat.",
    "Trida mengambil setengah langkah mundur, perlahan menyunggingkan senyum miring yang terkesan canggung.",
    "Tapi kalau nanti malam, gimana kalau aku traktir makan malam? Anggap aja traktiran dariku.",
    "Kedengarannya seru juga tuh.",
    "Pasti seru dong! Ada warung makan deket sekolah namanya Bazinga. Kamu pasti suka. Nanti kukabari lewat chat ya...",
    "Sip, sampai nanti, Trida.",
    "Trida melambaikan tangan terakhirnya dengan kikuk sebelum sosoknya perlahan menghilang di balik kerumunan pagi.",
    "Kamu membeli beberapa camilan, seporsi cimol hangat, lalu mencari tempat duduk yang tenang untuk memandangi hiruk-pikuk kota.",
    "Saat pancaran sinar sore mulai berubah keemasan, matamu menangkap sosok seniormu, Sabian, yang sedang asyik menawar di gerobak penjual.",
    "Kak Sabian? Lagi di sini juga?",
    "Woi! Wah, ada adik kelasku yang paling rajin nih! Kukira kamu masih nangkring ngendon ngerjain tugas!",
    "Akhirnya berhasil kabur juga dari meja kerja sesekali, Kak.",
    "Mantap! Hidup itu kudu keluar cari angin, Bro. Tadi aku sempat papasan sama Trida tuh—anak itu lagi stres berat kayaknya, kan? Butuh makan banyak tuh. Coba kamu temenin deh—dia sering lupa istirahat kalau udah kelewat fokus nugas.",
    "Iya nih, dia emang lagi capek banget kayaknya belakangan ini.",
    "Nah kan, ingetin dia biar nggak overthinking mikirin hidup. Udah ya, aku cabut dulu!",

    # 108 - 120 (Evening dinner choice / KPK Cafe with Julia)
    "Ruangan kamarmu temaram, hanya diterangi pendar hangat dari layar monitormu.",
    "Kamu sudah menatap mesh UV yang belum rampung selama berjam-jam, hingga bunyi keroncongan perutmu akhirnya berhasil mengalahkan suara dengung kipas PC.",
    "Kamu meregangkan badan, bunyi gemeretak sendimu memecah keheningan kamar, dan memutuskan sudah saatnya untuk melangkah keluar. Kamu butuh makanan yang beneran bergizi—bukan mi instan cup lagi.",
    "Makan malam di mana ya enaknya malam ini?",
    "Pintu kafe berderit pelan saat didorong terbuka, membelah lantunan musik jaz berirama lembut yang mengalun dari pengeras suara.",
    "Kafe KPK menghadirkan suaka bernuansa hangat dengan semerbak aroma espresso yang manis sekaligus getir.",
    "Julia duduk menyendiri di salah satu bilik meja dekat sudut belakang. Sebuah lensa kamera kelas profesional tergeletak rapi di atas meja di samping tumpukan buku referensi, sementara pandangannya terpusat pada sebuah konsol game genggam.",
    "Ia mengenakan headphone berukuran besar, dahinya berkerut menunjukkan konsentrasi yang begitu dalam.",
    "Ia mendongak, buru-buru menarik sebelah earphone-nya ke belakang, dan seulas senyuman manis akhirnya merekah di wajahnya.",
    "Oh. Halo. Nggak nyangka bakal ketemu kamu di sini malam ini.",
    "Ia memberi isyarat ke arah kursi kosong yang berada tepat di hadapannya.",
    "Lagi ngapain di sini?",
    "Gimana kabarmu?",

    # 121 - 131 (Julia conversation)
    "Aku cuma... lagi istirahat aja sih. Milih tempat nongkrong di luar kamar biasanya cukup ngebantu buat nenangin diri.",
    "Tadi aku lagi riset sedikit buat materi projek. Aku nemu serpihan cerita tersembunyi di game ini, dan jujur keren banget cara mereka ngejelasin ceritanya lewat detail lingkungan sekitar. Makanya aku pengin telaah lebih dalam.",
    "Ia terhenti sejenak, jemarinya meremas pelan tepian meja kafe.",
    "Maaf ya. A—aku nggak bermaksud ngoceh kepanjangan gini. Soalnya kalau udah ketemu hal kayak gini, aku sering lupa waktu... Apa ceritaku tadi ngebosenin ya?",
    "Nggak usah minta maaf, cerita aja. Gimana cara kerja storytelling-nya? Siapa tahu bisa kupakai buat tugasku.",
    "Nggak apa-apa kok. Aku malah senang dengar hal-hal yang kamu sukai.",
    "Tahan dulu bedah ilmunya sampai makananku datang. Tapi nanti kita bahas tuntas ya.",
    "Julia terdiam sejenak sebelum kamu dapat melihat secercah binar kagum terpancar di matanya di bawah temaram lampu kafe.",
    "Itu... makasih banyak ya, beneran... Aku sangat menghargai itu. Baru kali ini ada orang yang beneran mau nyimak hal-hal kayak ginian.",
    "Kita kan teman, ya nggak?",
    "Kalian berdua larut dalam kehangatan suasana yang membahagiakan, pertanda lembaran baru kisah persahabatan kalian telah resmi dimulai.",

    # 132 - 149 (Bazinga Restaurant with Trida & Radit)
    "Rumah Makan Bazinga benar-benar menyajikan ledakan sensasi keramaian. Udaranya pekat dengan aroma tumisan bawang putih dan kepulan asap masakan yang sedap.",
    "Kursi-kursi kayu berat berderit nyaring bergesekan dengan lantai semen, dan riuhnya obrolan para pengunjung cukup keras untuk menenggelamkan lagu pop yang berputar di sudut ruangan.",
    "WOI! DI SINI! HEI!",
    "Suara lantang Trida membelah kebisingan laksana bunyi sirene. Ia tersenyum lebar sambil melambaikan kedua tangannya ke udara seakan sedang memandu pendaratan pesawat.",
    "Radit yang duduk tepat di hadapannya hanya bisa membenamkan wajah ke kedua telapak tangan, pasrah menghadapi drama memalukan itu.",
    "Halo semuanya...",
    "Sumpah ya, lama-lama anak ini bakal bikin kita di-blacklist dari semua tempat makan di kota ini.",
    "Santai napa! Kamunya aja yang kaku. Nih, malam ini aku lagi ngidam nasi goreng banget. Buruan pesen makan, [player_name], aku udah kelaparan parah nih.",
    "Kamu meraih buku menu berlumur minyak yang telah dilaminasi. Obrolan perlahan beralih membahas seputar dunia game.",
    "Ya kayak yang kubilang tadi, semalam aku akhirnya berhasil tamat satu run lagi di Final Fantasy VII.",
    "Iya gila, lore-nya emang nggak ngotak keren banget. Bener kata kamu sih. Ngapain juga aku nyiksa diri pusing-pusing buka Maya seharian kalau bisa hidup bahagia kecanduan main game?",
    "Nanti kamu rindu ngerasain rumput di luar.",
    "Tapi beneran deh, kalau lagi nggak mantengin layar laptop, diam-diam aku kangen juga pengin naik gunung lagi. Nikmatin alam bebas gitu lho, tanpa dikejar deadline tugas sama sekali.",
    "Ia tersadar dari lamunannya, pundaknya turun lemas saat antusiasmenya berganti senyuman kikuk yang malu-malu.",
    "Aduh maaf ya, aku malah nyerocos panjang lebar lagi. Aku cuma... lagi butuh rehat lima menit dari tuntutan jadi anak rajin aja sih, hehe.",
    "Santai aja, dengerin kamu ngoceh soal game jauh lebih asyik daripada pusing ngomongin sekolah.",
    "Relate banget, mending ngejar high score rhythm game daripada mimpi buruk tugas 3D.",
    "Kirain kamu tipe anak alam, tapi khusus malam ini celotehanmu kumaafkan deh.",

    # 150 - 162 (Trida's confession at Bazinga & Walk home)
    "Tuh kan, Radit! Kubilang juga apa, mereka pasti paham. Kamunya aja yang kerjaannya ngerusak suasana mulu.",
    "Terserah kamu deh, Bro. Buruan pesen makanannya sebelum kamu nulis esai pidato tiga jam. Aku udah laper banget nih.",
    "Meja makan itu terasa semakin hangat dan intim, terlepas dari hiruk-pikuk suara orang di sekeliling kalian.",
    "Radit mengeluarkan ponselnya untuk membalas pesan, sengaja memberi ruang obrolan berdua bagimu dan Trida.",
    "Tapi serius deh... makasih banyak ya udah mau dengerin ceritaku tadi. Aku tahu aku ini berisik dan merepotkan. Kadang aku ngerasa muak sendiri sama diriku yang terus ditekan buat serba sempurna.",
    "Aku nggak pernah cerita ini ke siapa pun, tapi kadang kalau tekanannya udah kelewat batas, aku cuma bisa duduk terdiam di lantai kamar dalam kegelapan. Cuma itu satu-satunya caraku biar nggak tenggelam dalam kepanikan yang menyesakkan.",
    "Aku bener-bener bersyukur banget malam ini bisa duduk bareng kamu.",
    "Beberapa menit kemudian, kerumunan pengunjung makan malam mulai berangsur-angsur pulang.",
    "Wah, kayaknya tenagaku udah mentok nih. Yuk cabut balik. Aku capek banget.",
    "Oke, aku cabut duluan ya. Mau mampir ke Indoapril dulu. Trida, awas ya jangan sepanjang jalan pulang kamu gangguin [player_name] pake ocehan gamemu. Sampai ketemu besok ya kalian berdua.",
    "Radit melaju pergi dengan sepedanya, meninggalkan kalian berdua yang berdiri di tepi jalanan malam yang lengang dan sunyi.",
    "Hei... kamu langsung balik ke kosan sekarang? Kalau kamu nggak keberatan... boleh jalan bareng nggak? Malam ini aku bener-bener nggak mau jalan sendirian.",
    "Suaranya terdengar begitu lirih, tak seperti biasanya. Trida berjalan merapat di sampingmu saat langkah kaki kalian mulai berayun.",

    # 163 - 171 (Night walk intimacy)
    "Kedengarannya konyol banget kan ya? Udah segede gini tapi masih aja takut sama gelapnya malam.",
    "Kenapa mikir begitu?",
    "Ini bukan cuma soal gelapnya jalan... Kalau lagi sendirian, semua pikiran soal portofolio animasi, nilai ujian, sampai tuntutan keluarga di rumah... semuanya mendadak berdengung kencang banget di kepala. Rasanya kayak mau nelan aku bulat-bulat.",
    "Ia melirikmu, seulas senyum kecil yang malu-malu tersungging di sudut bibirnya.",
    "Kayak yang kubilang tadi, kalau ada teman di sampingku atau ada orang yang bisa diajak ngobrol... suara-suara bising itu seketika sirna. Akhirnya kepalaku bisa ngerasa tenang.",
    "Kamu itu udah kayak save point di dalam game, tahu nggak? Tempat yang bikin aku bisa rehat sejenak menarik napas lega sebelum menghadapi bos fight berikutnya.",
    "Ia berhenti melangkah sesaat, menengadahkan kepala menatap langit malam, lalu kembali menatapmu dengan sorot mata yang begitu dalam dan memikat.",
    "Aku bener-bener bersyukur banget orang yang nemenin aku jalan malam ini itu kamu. Dunia rasanya jadi... entahlah, nggak semenakutkan itu lagi.",
    "Jemarinya menyentuh lembut punggung tanganmu saat kalian berjalan, tidak sepenuhnya menggenggam, namun cukup dekat hingga hangatnya kulit tangannya terasa merambat ke nadimu. Dan ia tidak menarik tangannya menjauh.",

    # 172 - 182 (Abahciek Restaurant with Chie & Sabian, then night closure)
    "Warung Makan Abahciek tidak memiliki pintu tertutup konvensional; bagian depannya berupa area lesehan terbuka yang luas dengan panggung beralas kayu dan tikar bersih.",
    "[player_name]! Nggak salah nih, beneran kamu?! Sini gabung!",
    "Chie setengah bangkit dari duduk lesehannya di lantai, melambaikan tangannya penuh semangat ke udara. Di seberangnya, Sabian bersandar santai ke dinding sambil tersenyum geli melihat tingkah temannya itu.",
    "Mau pesan apa ya enaknya?",
    "Aku pesan Ayam Geprek aja deh.",
    "Bubur Ayam kayaknya sedap nih.",
    "Tahu Goreng buatku.",
    "Ngomong-ngomong, cerita dong, gimana harimu minggu ini? Jangan cerita yang versi ngebosenin ya—aku mau denger cerita seru dan hebohnya!",
    "Gelak tawa riang mengalun hangat di sekitar meja lesehan rendah saat kalian bertiga menikmati santap malam yang ceria dan penuh kebersamaan.",
    "Kembali ke kamarmu, heningnya desau angin malam menghadirkan penutup yang menenangkan bagi akhir pekan yang panjang dan tak terlupakan ini.",
    "Kamu terlelap tidur dengan hati yang ringan dan damai, tak sabar menyambut semaraknya festival sekolah yang menanti di depan mata."
]

week5_strings = {
    "Yeah, I am": "Iya, bener.",
    "No, I am not": "Nggak, bukan.",
    "Keep silent": "Tetap diam",
    "Accept the offer": "Terima ajakan",
    "Refuse the offer": "Tolak ajakan",
    "KPK Cafe": "Kafe KPK",
    "Bazinga Food Restaurant": "Rumah Makan Bazinga",
    "Abahciek Food Restaurant": "Warung Makan Abahciek",
    "What are you doing here?": "Lagi ngapain di sini?",
    "How are you?": "Gimana kabarmu?",
    "Don't apologize, just tell me. How does storytelling work? I might use it for my project.": "Nggak usah minta maaf, cerita aja. Gimana cara kerja storytelling-nya? Siapa tahu bisa kupakai buat tugasku.",
    "You're fine. I actually enjoy hearing what you're passionate about": "Nggak apa-apa kok. Aku malah senang dengar hal-hal yang kamu sukai",
    "Save the deep dive until I get food. But we're gonna get into it really": "Tahan dulu bedah ilmunya sampai makananku datang. Tapi nanti kita bahas tuntas ya",
    "Don't sweat it, listening to you rant about games is way better than stress-talking about school.": "Santai aja, dengerin kamu ngoceh soal game jauh lebih asyik daripada pusing ngomongin sekolah.",
    "Big mood, I'd take a rhythm game high-score over a 3D nightmare any day.": "Relate banget, mending ngejar high score rhythm game daripada mimpi buruk tugas 3D.",
    "I thought you were kind of 'outdoorsy,' but I'll let the yapping slide just for tonight.": "Kirain kamu tipe anak alam, tapi khusus malam ini celotehanmu kumaafkan deh.",
    "Chicken Smackdown": "Ayam Geprek",
    "Chicken Porridge": "Bubur Ayam",
    "Fried Tofu": "Tahu Goreng"
}

with open("/tmp/week5.rpy.json", "r", encoding="utf-8") as f:
    items = json.load(f)

d_idx = 0
for item in items:
    if item["type"] == "dialogue":
        if d_idx < len(week5_translations):
            item["indonesian"] = week5_translations[d_idx]
            d_idx += 1
        else:
            print(f"Warning: more dialogues than translations at index {d_idx}")
    elif item["type"] == "string":
        eng = item["english"]
        if eng in week5_strings:
            item["indonesian"] = week5_strings[eng]

with open("/tmp/week5.rpy.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

subprocess.run(["python3", "tools/translate_helper.py", "apply", "game/tl/indonesian/week5.rpy", "/tmp/week5.rpy.json"], check=True)
print(f"Updated week5.rpy.json: {d_idx} dialogues, {len(week5_strings)} menus.")
