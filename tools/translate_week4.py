import json
import subprocess

week4_translations = [
    # 0 - 12
    "Semilir angin pagi yang berpadu dengan sejuknya pendingin ruangan menyambutmu saat melangkah masuk ke dalam kelas.",
    "Matamu mengamati deretan bangku dari depan hingga belakang, mencari sosok yang biasanya selalu menyapamu ceria.",
    "Pandanganmu akhirnya terpaku pada bangku Trida yang masih kosong melompong.",
    "Jeda hening terjadi saat kamu menyadari kemungkinan ia bakal telat lagi hari ini, dan kamu hanya bisa tertawa kecil.",
    "Ada patung baru ya dipasang di kelas?",
    "Kamu terlonjak kaget, menoleh dan mendapati seringai usil khas Radit. Ah, bener kan, dia.",
    "Pagi, Radit.",
    "Radit menatapmu sesaat, lalu mendengus geli seraya menepuk ranselmu cukup keras hingga menarik perhatian beberapa teman di sekitar.",
    "Nggak usah senyum-senyum sendiri napa. Nanti orang-orang ngira kamu udah mulai korslet saking banyaknya tugas.",
    "Oh! Iya, um... kamu lihat Trida nggak?",
    "Kamu melangkah menuju bangku biasamu, tali ransel yang berat terasa menekan pundakmu saat bergesekan dengan kemeja seragam.",
    "Radit melemparkan tasnya santai ke atas kursi dan mulai mengeluarkan buku-bukunya, tampak tak peduli dengan kegelisahanmu.",
    "Palingan telat. Kamu kan tahu sendiri dia kayak gimana. Btw, tugas matematika yang kemarin kamu udah kelar belum?",
    
    # 13 - 29 (Trida enters late)
    "RADIT!",
    "Gemrincing gantungan kunci yang berirama mengumumkan kehadirannya bahkan sebelum gagang pintu sempat ditekan.",
    "Trida meluncur masuk ke dalam kelas, dadanya naik-turun terengah-engah dan rambutnya berantakan akibat berlari terburu-buru.",
    "Napasnya bahkan belum cukup buat pidato panjang—cuma cukup buat melayangkan tatapan tajam nan menusuk ke arah Radit.",
    "Kamu... *hah*... Kamu tega banget ninggalin aku!",
    "Ia mencengkeram kedua bahu Radit, mengguncang-guncangnya dengan panik.",
    "Radit bahkan tidak bergeming sedikit pun, raut wajahnya berubah datar khas orang yang sudah kenyang menghadapi tingkah absurd Trida.",
    "Soalnya pas terakhir kali aku gedor pintumu, yang kedengeran cuma suara alarm yang kamu biarin bunyi selama empat puluh menit penuh.",
    "...Aku kesiangan.",
    "Melihat perdebatan santai dan akrab di antara mereka berdua, sesuatu mendadak menyala di benakmu.",
    "Tunggu, kalian berdua tinggal di satu kos yang sama ya?",
    "Keduanya serempak menolehkan wajah ke arahmu, namun dengan ekspresi yang sangat bertolak belakang.",
    "Sayangnya, iya...",
    "Radit menghela napas berat seraya menegakkan pundaknya yang kaku.",
    "Kedengarannya seru banget kan?",
    "Kagak, itu mimpi buruk di dunia nyata. Bayangin aja tinggal berhadapan sama player rhythm game yang mikir jam dua pagi itu waktu yang pas buat mencet tombol sekuat tenaga.",
    "Itu namanya grinding, Radit! Aku kan lagi berusaha dapet S-rank di lagu itu, paham nggak sih?!",
    
    # 30 - 63 (Rhythm game banter & player input)
    "Kamu meletakkan tasmu ke kursi dengan bunyi debuk mantap, merasakan beban familiar itu lepas dari pundakmu.",
    "Tanganmu mengusap pelan kedua matamu, menghembuskan napas panjang seraya bersandar di kursi.",
    "Udah pasti mereka berdua mulai ribut lagi...",
    "Dan asal kamu tahu ya, lore di game JRPG baru ini bener-bener gila banget alurnya. Bikin takjub!",
    "Kamu melihat Radit memutar kursinya dan menyandarkan tubuh santai dengan kedua tangan di belakang kepala.",
    "Dengan tatapan sayu yang beralih menatapmu dan seringai tipis yang tersungging, kamu tahu ia sedang bersiap melancarkan serangan balasan.",
    "Iya deh, 'bikin takjub'... Kamu ngabisin waktu tiga jam cuma buat mati di bos yang sama berulang-ulang sampai frustrasi.",
    "Trida mulai menepuk-nepuk mejamu, lalu mencondongkan tubuh mendekat dan meraih ujung seragammu untuk mencari pembelaan.",
    "Ini tuh soal progres permainan, Bos! Melihat kemampuan kita berkembang dari mekanik game—itu poin intinya!",
    "[player_name], kasih tahu dia dong! Bukannya lebih asyik kalau punya hobi yang bener-bener kita sukai daripada cuma kerjaannya ngehakimi orang doang?",
    "Kamu bergeser di kursimu, tepi kayu meja terasa menekan pinggangmu. Kamu menatap Radit yang duduk santai.",
    "Ngehakimi orang? Kagak lah. Aku kan cuma mengamati secara objektif.",
    "Persis kayak pas aku mengamati kamu kalah di bos yang sama selama empat jam berturut-turut semalam.",
    "Gerakan Trida seketika membeku, daun telinganya merona merah padam menahan malu bercampur jengkel.",
    "Kamu mengerjap, sejujurnya agak kaget mendengar pengakuan Radit itu.",
    "Berarti selama ini Radit diam-diam memperhatikan permainan Trida ya.",
    "Tunggu, apa?! Kamu bisa denger audio cue-nya nembus tembok kamar? Terus dari mana kamu tahu itu bos fight yang sama?!",
    "Radit mengedikkan bahu santai sambil terus menulis tugas matematikanya yang jelas-jelas belum rampung.",
    "Aku nggak perlu main game itu buat tahu kalau caramu main tuh salah total. Tombol yang kamu pencet asal-asalan itu kedengeran banget polanya.",
    "Lalu ia berhenti menulis, meletakkan pulpennya seraya menyunggingkan seringai mengejek ke arah Trida.",
    "Kalau aja kamu bisa lebih santai dan ngepasin timing seranganmu sama ketukan bass-nya, kamu pasti udah kelar dari sejam sebelumnya.",
    "Trida menatap Radit seolah sedang melihat hantu yang bisa berbicara. Lalu ia melemparkan tatapan memohon ke arahmu.",
    "[player_name], bilang ke dia kalau dia tuh sok tahu! Bilang ke dia kalau dia cuma ngarang cerita biar kelihatan keren doang!",
    "Ayo dong, [player_name]. Kasih tahu dia, kalau perlu biar kutunjukin langsung di mana letak kesalahannya semalam.",
    "Omongan Radit ada benernya kok, Trida. Kamu kayaknya terlalu overthinking sama mekanik game-nya. Coba dengerin sarannya sekali-kali.",
    "Seringai Radit seketika berubah menjadi cengiran puas nan jemawa. Ia menunjuk ke arah Trida dengan senyum mengejek.",
    "Tuh kan? [player_name] aja capek dengerin polusi suaramu. Akui aja kalau tebakanku bener.",
    "Mulut Trida menganga menatapmu dengan raut merasa dikhianati, pundaknya merosot lesu.",
    "Wah, tega banget. Ya udah deh, semua orang emang paling jago jadi kritikus.",
    "Jangan jahat-jahat gitu napa, Radit. Mentang-mentang kamu jago main game bukan berarti kamu bisa seenaknya ngejek cara main orang lain.",
    "Ia berhenti memutar pulpennya saat seringainya perlahan memudar, digantikan oleh ekspresi yang sulit terbaca.",
    "Elitis? Aku cuma jujur kok. Tapi ya udah terserah, lanjutin aja main salah-salah gitu kalau emang bikin hatimu seneng.",
    "Wajah Trida seketika berseri-seri penuh kemenangan, suasana hatinya berubah dari jengkel menjadi lega dalam sekejap.",
    "Tepat banget! Makasih ya! Tuh denger kan, Radit? [player_name] aja ngerasa kamu tuh nyebelin banget.",
    
    # 64 - 89 (Class ended & Radit conversation)
    "Setelah melewati pagi paling kacau yang bisa dibayangkan, kalian bertiga akhirnya berhasil bertahan melalui jam-jam pelajaran sekolah.",
    "Mulai dari materi sejarah yang membosankan sampai sesi matematika rumit di mana semua angka terasa memusingkan kepala.",
    "Saat bel berdentang menandakan jam istirahat tiba, rasanya bagaikan akhir dari sebuah pertempuran sengit.",
    "Kamu baru saja kembali dari ruang guru setelah mengumpulkan tumpukan buku tugas matematika milik seluruh kelas.",
    "Tiba-tiba saja, teman-teman lain berbalik dan langsung berhamburan keluar kelas, menyisakan Radit yang duduk sendirian di mejanya.",
    "Udah beres?",
    "Udah, semua buku tugas udah kukumpulin ke meja guru tadi.",
    "Kerja bagus. Kamu emang selalu bisa diandalkan buat beres-beres, nggak kayak seseorang tuh...",
    "Radit memasukkan kedua tangannya ke saku celana seraya memandang jauh ke arah luar jendela tempat Trida berada.",
    "Radit menghela napas pelan saat matanya memperhatikan gerak-gerik Trida di kejauhan.",
    "Dia tuh udah sibuk ngotak-ngatik party build game-nya selama tiga hari berturut-turut. Sampe begadang nggak jelas.",
    "Ia tampak bosan, tapi ada secercah rasa jengkel yang tertahan di matanya—bukan jengkel ke Trida, melainkan ke kebiasaan keras kepalanya.",
    "Bisa-bisa ntar malam aku terpaksa login ke save data game-nya terus kubenerin status build karakternya biar dia nggak kalah mulu.",
    "Ia tertawa kering dan letih, melirik sekilas ke arah ujung sepatunya sendiri.",
    "Terserah lah. Tapi jangan bilang-bilang ke dia soal itu ya.",
    "Tunggu, jadi aslinya kamu beneran mau bantuin dia nih?",
    "Ia menatapmu, sorot matanya yang biasanya datar tampak melembut sejenak. Lalu pandangannya beralih menatap lantai.",
    "Aku cuma mau dia berhenti kalah mulu. Sakit mata ngelihatnya.",
    "Sebelum kamu sempat menanggapi kalimatnya, sebuah suara lantang memecah udara. Kamu mendongak dan melihat Sabian bersandar santai di kusen pintu.",
    "Yoo, [player_name]! Akhirnya kelar juga?",
    "Oh-iya, tadi habis nganterin beberapa tugas ke ruang guru.",
    "Ayo lah, skip belajar bentar napa. Kita mau makan siang nih, lu harus ikutan nongkrong bareng kita!",
    "Sabian bahkan tidak menunggu jawabanmu. Ia langsung memasang tampang memohon yang kocak dan memintamu ikut.",
    "Kamu melirik kembali ke arah Radit, yang sedang menatapmu dengan pandangan bertanya-tanya.",
    "Kayaknya kamu udah direkrut tuh. Sejujurnya, nongkrong bareng senior di kantin jauh lebih mending dibanding bengong di kelas.",
    "Namun dari nada bicaranya, kamu tahu terselip harapan kecil agar kamu tetap menemaninya di kelas.",
    
    # 90 - 98 (Branch: Canteen with Sabian)
    "Sampai ketemu nanti ya, Radit. Aku laper banget nih, dan kayaknya kepalaku belum sanggup dengerin ocehan game Trida lagi.",
    "Radit mendengus pelan, matanya yang malas melirik ke arah langit-langit kelas.",
    "Pengkhianat. Tega-teganya ninggalin aku sendirian sama badai tornado itu? Ya udah sana makan. Awas aja kalau sampai dipungut jadi kacung senior.",
    "Kamu berlari kecil menyusul Sabian, meninggalkan studio di belakang. Kantin sekolah tampak riuh ramai dipenuhi antrean siswa.",
    "Saat melangkah masuk, Sabian menepuk pundakmu dengan ramah.",
    "Lama amat lu! Gue kira lu bakal ngabisin jam istirahat cuma buat jadi kurir tugas.",
    "Kamu memesan makanan dan duduk di bangku tepat di seberang mejanya.",
    "Obrolan pun beralih ke topik-topik santai yang jauh dari penatnya rutinitas harian sekolah. Suasananya begitu hangat dan menghibur.",
    "Ini adalah momen istirahat kecil yang sempurna, meski di dalam hati kamu sempat bertanya-tanya bagaimana nasib Radit sendirian di kelas.",
    
    # 99 - 121 (Branch: Stay with Radit in classroom)
    "Radit menatapmu, seringai sinisnya perlahan melunak menjadi sesuatu yang tampak... begitu lega.",
    "Ia mulai melangkah santai menuju deretan meja kelas, postur tubuhnya akhirnya kembali rileks.",
    "Jujur ya? Mendingan kita di sini aja. Aku masih punya sisa camilan di tas kalau kamu emang beneran laper.",
    "Kamu melangkah masuk kembali bersama Radit saat kebisingan jam istirahat perlahan memudar di luar ruangan.",
    "Radit menjatuhkan diri ke kursinya dan melemparkan sebungkus keripik kentang ke mejamu.",
    "Ia tidak mengucapkan sepatah kata pun untuk beberapa saat, hanya mengeluarkan ponselnya dan menggulir linimasa dengan santai.",
    "Kamu merebahkan kepala di atas meja, permukaan kayu yang sejuk terasa begitu nyaman menyentuh pipimu.",
    "Kamu tidak perlu menghibur siapa pun atau repot-repot memikirkan masalah orang lain. Ini adalah tipe istirahat yang paling kamu butuhkan.",
    "Tahu nggak, kamu tuh satu-satunya orang yang nggak pernah maksa aku buat terus-terusan ngomong.",
    "Matanya masih terpaku pada layar ponsel, namun kamu tahu kalimat itu ditujukan khusus untukmu.",
    "Aku bener-bener ngehargai itu.",
    "Kamu menggeser posisi kepalamu sedikit di atas meja, menatap ke arahnya. Lalu tawa lembut meluncur pelan dari bibirmu.",
    "Iya lah, harus ada yang ngimbangin sikap dinginmu itu kan. Lagian kamu jauh lebih mending pas lagi anteng gini.",
    "Enak juga bisa santai kayak gini kan? Lagipula kamu temen ngobrol yang asyik kok kalau lagi nggak mode nyinyir.",
    "Otakku beneran lagi ngebul banget buat diajak ngomong. Cuma pengen nikmatin suasana hening aja, Bro. Jangan baper ya.",
    "Radit tertawa renyah dan tulus, suara tawa yang jarang sekali kamu dengar darinya; ia tampak jauh lebih santai sekarang.",
    "Jangan kebiasaan ya. Aku masih punya sekotak amunisi sarkasme yang siap kutembak kapan aja.",
    "Ia meletakkan ponselnya di meja dan bersandar ke kursi, memejamkan matanya selama beberapa detik.",
    "Bagus deh kamu nggak ikut senior tadi. Ngelihat mukanya aja udah bikin kepalaku cenat-cenut.",
    "Dengusan geli meluncur dari hidungmu saat kamu mengunyah keripik di mejamu.",
    "Kayaknya dia tadi cuma nyari orang buat dijadiin kuli angkut barang deh.",
    "Persis. Makanya selera pertemananmu itu top-tier banget. Pertahankan ya.",
    "Ia kembali fokus ke ponselnya, namun keheningan kali ini terasa jauh lebih hangat, penuh rasa saling memahami yang tulus.",
    
    # 122 - 150 (Walk home with Trida & round tofu)
    "Sinar keemasan mentari senja terbentang panjang di atas aspal jalanan, mewarnai dunia dalam hangatnya rona madu.",
    "Semilir angin sore membawa aroma gurih tahu bulat goreng yang begitu menggoda dari gerobak pedagang di dekat gerbang.",
    "Trida melangkah dengan energi yang tak pernah habis, menenteng kantong plastik berminyak berisi camilan hangat di sebelah tangannya.",
    "Ia tampak tenggelam dalam ritme dunianya sendiri, rasa antusiasnya meluap-luap di setiap langkah kakinya.",
    "Tahu nggak, aku ngerasa empat minggu belakangan ini tuh... intens banget kan ya? Maksudku—dalam artian yang seru banget!",
    "Bener banget, nggak usah ditanya lagi.",
    "Rasanya kayak kita lagi terjebak di dalam game, cuma bedanya bukannya naikin status karakter, kita malah berusaha bertahan hidup dari tugas harian.",
    "Trida terdiam sejenak, mendongak menatap langit di mana semburat jingga perlahan mulai pudar ditelan gelapnya malam.",
    "Ia memindahkan kantong plastik camilannya, jemarinya mengetuk-ngetuk sisi wadah dengan ketukan berirama.",
    "Langkah kaki Trida melambat, ritme terburu-burunya akhirnya mereda. Ia menatap ke depan menatap jalanan yang mulai sepi.",
    "Energi heboh dari pagi hari tadi kini telah lenyap, digantikan oleh sisi kerapuhan yang tenang dan jarang sekali ia perlihatkan.",
    "Meskipun capek, kayaknya aku mulai berusaha buat bener-bener mencintai proses ini deh.",
    "Maksudku... kalau dari awal aku nggak punya passion di sini, kayaknya aku nggak bakal sanggup ngelewatin semua ini sampai sekarang.",
    "...Kalau kamu sendiri gimana? Udah mulai kebayang belum masa depanmu di sini?",
    "Namanya juga pertaruhan kan. Tapi kita kan baru jalan empat minggu—kayaknya masih kepagian buat nentuin kita bakal menang atau kalah.",
    "Iya juga sih... bener katamu. Aku yakin aku udah gila dari kemarin kalau bukan karena ada kamu yang nemenin.",
    "Menurutku semuanya sepadan kok. Apalagi kalau ngelewatinnya bareng kamu, rasanya jadi seru banget.",
    "Iya juga sih... bener katamu. Aku yakin aku udah gila dari kemarin kalau bukan karena ada kamu yang nemenin.",
    "Jangan buru-buru nyerah dong. Proyek animasi pertama kita aja belum beres, masa kamu udah cemas mikirin akhir kelulusan sih?",
    "Iya juga sih... bener katamu. Aku yakin aku udah gila dari kemarin kalau bukan karena ada kamu yang nemenin.",
    "Aku tuh sering banget overthinking apakah skill-ku beneran cukup buat jurusan ini, tapi pas lagi bareng kamu, rasanya semua beban itu menguap.",
    "Trida berhenti melangkah sejenak dengan suara pelan.",
    "Bikin semua hal berat ini nggak berasa kayak mimpi buruk lagi.",
    "Ia menyunggingkan senyum tulus yang sedikit canggung, menyenggol pelan lenganmu dengan sikunya—sebuah gestur hangat penuh kasih sayang.",
    "Tenang aja, aku nggak bakal nyerah secepet itu kok. Belum saatnya. Kita udah ngelewatin banyak hal bareng tahun ini. Kamu bakal terus nemenin aku kan?",
    "Heh, boleh juga tuh. Aku tunggu pembuktiannya ya.",
    "Melangkah beriringan menuju arah terbenamnya matahari, tatapanmu menangkap hangatnya cahaya senja yang memeluk sosok di sampingmu.",
    "Pikiranmu melayang merenungkan janji manis yang baru saja diucapkan Trida.",
    "Bakal terus barengan sama aku ya?",
]

week4_menus = {
    "Agree that Radit is right": "Setuju kalau omongan Radit memang benar",
    "Call out Radit for being rude": "Tegur Radit karena bicaranya terlalu ketus",
    "Hang out with the seniors": "Pergi nongkrong bersama para senior di kantin",
    "Head class with Radit": "Kembali ke kelas santai bersama Radit",
    "Yeah, well, someone has to balance your edge. Honestly, you're way less annoying when you aren't talking.": "Iya lah, harus ada yang ngimbangin sikap dinginmu. Lagian kamu jauh lebih asyik pas lagi anteng.",
    "It's nice to just chill, you know?. Plus, you're decent company when you aren't roasting people.": "Enak juga bisa santai kayak gini kan? Lagipula kamu temen yang asyik kok kalau lagi nggak mode nyinyir.",
    "I'm literally too fried to talk. Just enjoying the silence, man. Don't take it the wrong way.": "Otakku beneran lagi ngebul banget buat diajak ngomong. Cuma pengen nikmatin hening aja, jangan baper ya.",
    "It's a gamble, I guess. But we're only four weeks in—maybe it's too early to decide if we're winning or losing.": "Namanya juga pertaruhan kan. Tapi kita baru empat minggu—masih kepagian buat nentuin menang atau kalah.",
    "I think it's worth it. Especially with you around makes it fun.": "Menurutku semuanya sepadan kok. Apalagi kalau bareng kamu, rasanya jadi seru banget.",
    "Don't 'crash out' yet. We haven't even finished our first animation project, and you're already worried about the end?": "Jangan buru-buru nyerah dong. Proyek animasi pertama aja belum kelar, masa udah cemas mikirin akhir sih?"
}

with open('/tmp/week4.rpy.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

dialogue_idx = 0
for item in items:
    if item['type'] == 'dialogue':
        if dialogue_idx < len(week4_translations):
            item['indonesian'] = week4_translations[dialogue_idx]
            dialogue_idx += 1
    elif item['type'] == 'string':
        eng = item['english']
        if eng in week4_menus:
            item['indonesian'] = week4_menus[eng]

with open('/tmp/week4.rpy.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Updated week4.rpy.json: {dialogue_idx} dialogues, {len(week4_menus)} menus.")
subprocess.run(['python3', 'tools/translate_helper.py', 'apply', 'game/tl/indonesian/week4.rpy', '/tmp/week4.rpy.json'], check=True)
