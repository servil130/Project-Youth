import json
import subprocess

week8_translations = [
    # 0 - 14 (Evening boarding house, knock on door, Trida arrives worn out)
    "Dengung berat kipas angin malam di kamar kosmu tak mampu mengusir kusutnya pikiran yang terus berputar-putar di kepalamu.",
    "Sudah seminggu penuh berlalu sejak sore yang menyesakkan di kelas PPKn itu, dan ruang hampa di antara kamu dan Trida terasa begitu janggal semenjak saat itu.",
    "Meskipun kalian berbagi ruang kelas yang sama, ia dengan lihai selalu menghindari kontak mata, menyelinap keluar ruangan sebelum kamu sempat menyusul, dan mengunci rapat-rapat celotehan cerianya yang biasa di balik senyuman dingin yang penuh jarak.",
    "Kamu tengah duduk di tepi ranjang, menatap nanar layar ponselmu sembari memutar ulang keheningan menyakitkan itu berulang-ulang, ketika tiba-tiba ketukan pintu yang tajam dan tergesa memecah kesunyian kamarmu.",
    "Sambil mengernyitkan dahi, kamu beranjak bangun dan membuka pintu, mengira itu ibu kos atau tetangga sebelah. Namun saat pintu terbuka, napasmu mendadak tercekat.",
    "Berdiri di temaramnya cahaya lampu lorong adalah Trida. Wajahnya tampak kuyu dan lelah, memperlihatkan seulas senyum kaku yang getir dan sama sekali tak sampai ke matanya.",
    "Kedua tangannya terbenam dalam-dalam di saku saku depan hoodie-nya, jemarinya meremas-remas kain dengan gelisah.",
    "Um... hai,",
    "Ia membuka suara, nadanya terdengar jauh lebih lirih dan penuh kehati-hatian dibanding biasanya seraya memindahkan tumpuan kakinya kikuk.",
    "Ini... lagi ganggu waktu istirahatmu nggak? Aku bisa balik lagi nanti kalau kamu lagi sibuk atau ada urusan.",
    "Rasa cemas seketika menepis keterkejutanmu. Sebelum ia sempat menarik diri untuk berbalik pergi, kamu menggelengkan kepala dan melangkah mundur, membuka pintu kamarmu lebar-lebar.",
    "Nggak, sama sekali nggak ganggu kok. Masuk aja.",
    "Ucapmu tegas tanpa sedikit pun keraguan, memberi isyarat agar ia melangkah masuk ke dalam.",
    "Trida mengerjap, tampak kaget kamu mengizinkannya masuk dengan begitu mudah, namun ia tetap melangkah melewati ambang pintu dengan gerakan pelan dan penuh kehati-hatian.",
    "Ia tidak berkeliling melihat mejamu atau mondar-mandir seperti kebiasaannya; sebaliknya, ia langsung melangkah menuju area santai kecil di kamar kosmu dan duduk di tepi sofa, menarik kedua lututnya merapat dan terlihat begitu rapuh serta kecil.",

    # 15 - 29 (Lounge area tension, inviting Trida to relax)
    "Area santai kecil itu terasa teramat sunyi; dengung stabil dari pendingin ruangan di dinding menjadi satu-satunya suara pengisi hening di tengah pekatnya ketegangan yang menggantung di udara.",
    "Trida duduk membeku di tepian sofa kain yang telah usang, postur tubuhnya melengkung kaku dan begitu defensif.",
    "Ia menarik sedikit kedua lututnya, mendekap tubuhnya rapat-rapat di balik hoodie kebesarannya, jemarinya mencengkeram erat ujung lengan baju yang berlawanan seolah berusaha menahan dirinya agar tidak runtuh.",
    "Kamu mendudukkan diri di ujung sofa yang berlawanan, menyisakan jarak yang cukup agar ia tidak merasa terpojok, meski tubuhmu condong menghadap ke arahnya.",
    "Santai aja, Trida, nggak apa-apa kok...",
    "Ucapmu lembut, membiarkan suaramu mengalun tenang dan menyejukkan.",
    "Kamu duduk kaku banget kayak patung gitu... Copot sepatumu, duduk yang nyaman aja.",
    "Trida melepaskan tawa getir yang terdengar lebih mirip helaan napas putus asa.",
    "Ia berusaha sedikit merilekskan tubuhnya dengan menurunkan kakinya ke lantai, namun kedua pundaknya masih tetap menegang kaku di dekat telinganya.",
    "Tatapannya bergerak gelisah menyapu kamarmu—berpindah dari mejamu, poster di dinding, hingga tepian karpet—mencari apa saja demi menghindari kontak mata langsung denganmu lebih dari sedetik.",
    "Kedutan cemas di jemarinya tak kunjung reda; kedua ibu jarinya terus menggesek-gesek ujung manset lengan bajunya dengan gugup.",
    "Iya, maaf ya...",
    "Trida bergumam lirih, nada suaranya terdengar begitu rapuh dan kehilangan seluruh keceriaannya yang biasa.",
    "Kayaknya... kebiasaan lama susah hilangnya ya. Duduk diam begini rasanya menakutkan banget pas isi kepala nggak mau berhenti berputar.",

    # 30 - 46 (Asking what's wrong, Trida recalls glasses boy's words)
    "Kamu bergeser mendekat, membuat bantalan sofa sedikit melesak di bawah beban tubuhmu, memangkas sebagian jarak di antara kalian berdua.",
    "Rasa cemas yang mengendap di dadamu kian membuncah, melihat betapa ia masih tampak begitu terluka dan rapuh seminggu penuh setelah insiden memalukan di kelas PPKn itu.",
    "Trida,",
    "Kamu berusaha menjaga nada bicaramu tetap hangat dan sama sekali bebas dari tekanan.",
    "Aku tahu kamu nggak mungkin tiba-tiba datang ke sini di malam Minggu cuma buat basa-basi nggak jelas.",
    "Seminggu ini kamu selalu ngehindar dariku, dan kamu hampir nggak ngomong sepatah kata pun...",
    "Sebenarnya ada apa di dalam kepalamu? Cerita aja ke aku.",
    "Mendengar ajakan tulus untuk terbuka itu, benteng pertahanan yang setengah mati dibangun Trida selama tujuh hari terakhir seketika retak.",
    "Napasnya tercekat di tenggorokan, tersengal tajam hingga sekujur tubuhnya bergetar nyata.",
    "Trida memejamkan matanya rapat-rapat untuk sesaat, rahangnya mengatup kuat menelan ludah melawan gelombang emosi yang tiba-tiba meluap.",
    "Saat ia membuka matanya kembali, tatapannya tak lagi bergerak liar; pandangannya terkunci lurus pada sebuah titik acak di dinding kamar.",
    "Helaan napas panjang yang gemetar lolos dari bibirnya. Tarikan napasnya bergetar pelan di keheningan kamar saat beban berat yang selama ini ia pendam sendirian akhirnya mulai tumpah ruah.",
    "Trida menunduk menatap kedua tangannya, ibu jarinya meremas kain lengan bajunya dengan cemas. Ketika ia akhirnya bersuara, ucapannya nyaris tak lebih dari bisikan parau yang hancur, kehilangan seluruh rasa percaya diri.",
    "Tiap kali aku merem, aku cuma... aku cuma terus denger kata-kata cowok itu.",
    "Ia bergumam dengan suara yang bergetar hebat. Ia melepaskan tawa getir yang basah, suara memilukan yang berniat menutupi luka, namun genangan air mata yang mulai membendung di pelupuk matanya membongkar segalanya.",
    "Konyol banget kan ya? Padahal itu cuma celetukan asal dari cowok yang bahkan nggak peduli sama sekali sama aku. Tapi... omongan dia bener.",
    "Kamu bergeser semakin merapat di sofa, dadamu berdenyut nyeri.",
    "Trida, omongan dia nggak bener sama sekali. Dia itu cuma orang brengsek yang nggak punya empati.",

    # 47 - 62 (Trida breaks down: "I am dead weight", art teacher trauma, sobbing)
    "Nggak, omongan dia itu {i}bener{/i}!",
    "Trida mendadak meninggikan suaranya, suaranya tercekat parau saat benteng kerapuhan yang ia bangun sepanjang minggu akhirnya hancur lebur.",
    "Ia menoleh menatapmu dengan mata yang dibanjiri air mata; kehancuran batin yang terlukis murni dan tanpa sekat di wajahnya membuatmu tercekat sulit bernapas.",
    "Aku ini {i}emang{/i} cuma beban! Semua hal dasar selalu kubikin kacau, buka file atau ngikutin instruksi sederhana aja aku gagal sampai kelihatan kayak badut tolol, dan begitu situasinya serius, aku cuma bisa mematung kaku!",
    "Ia menarik kedua lututnya merapat ke dada, menyembunyikan wajahnya di balik kedua lengan saat isak tangis yang kasar dan tersengal-sengal lolos dari tenggorokannya.",
    "Ketika ia mengangkat kepalanya kembali, kedua pipinya telah basah kuyup oleh air mata, dan ekspresinya terdistorsi oleh rasa benci mendalam pada dirinya sendiri.",
    "Kamu ingat kan pas aku bilang pengin bikin orang tersenyum? Pengin jadi orang yang beneran bisa ngebantu orang lain?",
    "Sebuah tawa getir dan hancur meluncur pelan laksana guyuran hujan lebat.",
    "Itu semua lelucon konyol. Itu semua cuma... caraku lari dari kenyataan betapa nggak gunanya aku ini. Sebelum pindah ke sini, aku selalu kesusahan ikut kelas seni rupa di kampung halamanku.",
    "Guru-guruku dulu menatapku dengan cara yang persis sama—menghela napas lelah, menggelengkan kepala, dan bertanya-tanya ngapain juga aku repot-repot nyoba kalau emang nggak punya bakat alami.",
    "Bertahun-tahun aku ngebohongi diriku sendiri, 'Seenggaknya kamu optimis! Seenggaknya kamu bisa bikin suasana ceria!' Tapi apa gunanya coba?",
    "Suaranya merosot menjadi bisikan yang putus asa, seluruh daya juangnya luruh tak bersisa.",
    "Kalau kamu ceria terus tiap saat, orang-orang cuma bakal nganggep kamu bodoh. Dan begitu kamu hancur terpuruk... kamu baru sadar kalau kamu nggak punya apa-apa lagi selain itu.",
    "Aku ini cuma berisik, ceroboh, dan bener-bener nggak bisa ngerjain apa pun dengan bener. Kadang... jujur aja? Kadang aku bener-bener mikir buat apa aku terus berusaha. Kenapa aku harus punya impian setinggi langit kalau ujung-ujungnya, aku cuma ngebuktiin kalau omongan mereka tentang diriku itu bener?",
    "Kepedihan dari pengakuan jujurnya menggantung begitu berat di udara; keheningan kamar hanya diisi oleh suara napas Trida yang memburu dan tak beraturan.",

    # 63 - 75 (Player holds Trida's hand, gives affirmation: "You are not useless")
    "Tanpa ragu sedetik pun, kamu bergeser semakin merapat di sofa, menghapus sisa jarak di antara kalian hingga bahumu menempel erat di samping bahunya.",
    "Kamu mengulurkan tanganmu, mencengkeram lembut lengannya untuk memberinya sandaran yang kokoh.",
    "Lihat aku, Trida.",
    "Perlahan tanganmu menggenggam jemari Trida saat kulit kalian bersentuhan, menghantarkan getaran halus yang menjalar menenangkan tangannya.",
    "Suaramu terdengar mantap penuh ketulusan mendalam, tanpa menyisakan secuil pun keraguan.",
    "Butuh beberapa detik, namun Trida perlahan mengangkat kepalanya; matanya yang basah oleh air mata mengerjap kaget saat bersitatap dengan pandanganmu.",
    "Kamu sama sekali bukan orang yang nggak berguna.",
    "Ucapmu lembut, membiarkan setiap untaian kata membawa keyakinan mutlak.",
    "Semua hal buruk yang kamu omongin tentang dirimu barusan... nggak ada satu pun yang bener. Kamu mikir kamu cuma badut atau pengacau, padahal kamu nggak tahu seberapa banyak kehangatan dan keceriaan yang kamu bawa ke dalam ruangan.",
    "Kamu bikin orang lain tersenyum, dan kehadiranmu selalu bikin aku ngerasa bahagia yang tulus. Sifat optimismu itu bukan topeng palsu—itu jati dirimu yang sebenarnya, dan itu hal yang luar biasa indah.",
    "Kamu begitu peduli sama semua orang, dan rasanya sakit banget melihatmu menyiksa dirimu sendiri cuma gara-gara satu orang picik yang bahkan nggak kenal siapa dirimu sebenarnya.",
    "Kamu meremas lembut lengannya, mengunci tatapannya lekat-lekat.",
    "Kamu berbakat, kamu kuat, dan dirimu jauh lebih berharga daripada segelintir momen buruk di dalam kelas. Aku peduli banget sama kamu, Trida. Tolong jangan pernah mikir kalau kamu sendirian menanggung semua ini, atau ngerasa kalau dirimu nggak pantas.",

    # 76 - 87 (Trida's tears turn into radiant smile, resting head on shoulder)
    "Kata-katamu menghantam sanubari Trida laksana gelombang kehangatan yang nyata. Untuk sedetik, napasnya tercekat berhenti, bibirnya sedikit terbuka saat pengakuan tulus tanpa syarat itu menyelimuti seluruh relung hatinya.",
    "Ia tampak seperti musafir yang kedinginan di tengah badai dan tiba-tiba menemukan perapian hangat. Sudah begitu lama—mungkin bertahun-tahun—sejak terakhir kali ada seseorang yang berbicara padanya dengan kelembutan yang begitu tulus dan gigih, melihat menembus segala kebisingannya dan merengkuhnya saat ia terjatuh.",
    "Gelombang emosi baru kembali menerpanya, namun kali ini kepedihan yang menindih perlahan mencair, berganti kehangatan luar biasa yang meluap memenuhi dadanya.",
    "Tawa kecil yang basah lolos dari bibir Trida, dan di tengah lelehan air mata yang masih mengalir di pipinya yang merona, senyuman lebar yang tulus merekah di parasnya—bercahaya, berantakan, dan begitu memikat.",
    "Melihat senyuman indah yang mendadak mekar menembus lelehan air matanya seketika membuat napasmu tertahan, dan jantungmu berdegup kencang menghantam tulang rusuk, berdetak tak keruan.",
    "Trida tertawa kecil seraya mengusapkan lengan baju hoodie-nya ke wajah untuk menghapus sisa air mata, sementara senyum lebarnya tetap terkembang manis di bibirnya.",
    "Sialan... Kamu bener-bener nggak adil tahu nggak?",
    "Ia berbisik lirih, suaranya sarat oleh luapan emosi, namun kini bersinar dengan kelegaan yang begitu luar biasa saat ia menyandarkan tubuhnya ke bahumu.",
    "Belum pernah... belum pernah ada orang yang ngomong hal seindah itu ke aku. Makasih banyak ya. Beneran... makasih banyak.",
    "Kamu tidak melepaskan kontak hangat itu, mempertahankan tanganmu menggenggam lengannya dan mengusapkan ibu jarimu lembut menenangkan di atas kain bajunya.",
    "Sekarang kamu beneran... kayak beneran udah baikan?",
    "Tanyamu pelan dengan nada protektif seraya mengamati wajahnya dengan saksama.",
    "Tanganmu masih dingin banget begini. Perlu kuambilkan air minum hangat? Tarik napas dalam-dalam dulu ya.",

    # 88 - 98 (Head resting on shoulder, teasing returns, intimate quiet)
    "Trida menghembuskan napas panjang sekali lagi, namun kali ini seluruh ketegangan tampak meluruh sempurna dari punggungnya yang kaku. Kilat ketakutan di matanya akhirnya mencair seutuhnya, berganti binar kehangatan yang teduh.",
    "Ia membiarkan kepalanya bersandar sepenuhnya di atas bahumu, merebah di sana dengan rasa percaya dan kenyamanan tanpa syarat yang jarang, atau bahkan belum pernah, ia perlihatkan kepada orang lain.",
    "Untuk beberapa menit yang hening, satu-satunya suara di kamar itu hanyalah dengung stabil AC dan ritme tarikan napasnya yang perlahan kembali teratur.",
    "Lalu, secercah kilau usil yang begitu familiar kembali menyala di balik bulu matanya yang masih basah oleh sisa air mata.",
    "Trida bergerak sedikit, melepaskan dengusan tawa kecil seraya nada teatrikalnya yang khas perlahan merayap kembali ke suaranya.",
    "Duh... coba lihat dirimu,",
    "Ia bergumam pelan, nada menggoda yang manis akhirnya kembali terdengar dalam intonasinya.",
    "Mendadak berubah jadi pembicara motivasi bersertifikat gini di malam Minggu. Habis ini apa lagi coba, kamu mau mulai bagi-bagi poster kutipan bijak di depan pintu kamar kos?",
    "Meski suaranya masih agak parau sehabis menangis, ledekan usil itu adalah tanda mutlak bahwa itu adalah {i}dirinya{/i}.",
    "Itu adalah kembalinya sosok Trida yang kamu kenal—bukan lagi bersembunyi di balik topeng keceriaan yang panik, melainkan berbagi lelucon intim yang sunyi hanya untuk kalian berdua, duduk berdampingan bahu-membahu di bawah temaramnya lampu kamarmu."
]

with open("/tmp/week8.rpy.json", "r", encoding="utf-8") as f:
    items = json.load(f)

d_idx = 0
for item in items:
    if item["type"] == "dialogue":
        if d_idx < len(week8_translations):
            item["indonesian"] = week8_translations[d_idx]
            d_idx += 1
        else:
            print(f"Warning: more dialogues than translations at index {d_idx}")

with open("/tmp/week8.rpy.json", "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

subprocess.run(["python3", "tools/translate_helper.py", "apply", "game/tl/indonesian/week8.rpy", "/tmp/week8.rpy.json"], check=True)
print(f"Updated week8.rpy.json: {d_idx} dialogues.")
