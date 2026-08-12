# MARS Araştırma Yol Haritası

> Amaç: Mars'ı görsel bir 3B model olarak değil; konum, zaman, irtifa/derinlik,
> ölçüm yöntemi, belirsizlik ve kaynak bilgisiyle sorgulanabilen bilimsel bir
> dijital ikiz olarak kurmak.

Son güncelleme: 2026-07-30

## 1. Durum dili

Bu dosyadaki bütün işler aşağıdaki dört durumdan birini taşır:

- `[x] YAPILDI`: Veri yerelde arşivlendi, kaynağı kataloglandı, SHA-256 ile
  doğrulanıyor, özellik/veri sözleşmesine bağlandı ve otomatik kontrolden geçiyor.
- `[~] KISMEN YAPILDI`: Alanın yalnız belirli ürünleri, örnek zamanları veya
  düşük çözünürlüklü katmanları var. Alan tamamlanmış sayılmaz.
- `[ ] PLANLANDI`: Henüz veri katmanına alınmadı.
- `[!] BLOKE`: Kaynak erişimi, lisans, ürün eksikliği veya bilimsel belirsizlik
  nedeniyle bekliyor. Blokaj gerekçesi yazılmadan bu durum kullanılamaz.

Bir veri alanı ancak şu zincir tamamlandığında `YAPILDI` sayılır:

```text
Birincil bilimsel kaynak
  → özgün dosyanın resources/archive altında yerel kopyası
  → URL/DOI/sürüm/tarih/lisans kaydı
  → SHA-256 ve bayt doğrulaması
  → ham/kalibre/türetilmiş/modellenmiş durumunun ayrılması
  → özellik tanımı, birim ve koordinat sistemi
  → eksik/geçersiz değer kodları
  → kalite ve belirsizlik alanları
  → ürün kapsamı ve temsil sınırları
  → otomatik yapısal test
  → en az bir bilimsel doğruluk veya tutarlılık testi
```

## 2. Projenin mevcut doğrulanmış tabanı

- `[x] YAPILDI` 29 kaynak kaydı.
- `[x] YAPILDI` 482 kaynaklı özellik tanımı.
- `[x] YAPILDI` 117 normalize referans değer.
- `[x] YAPILDI` 77 arşivlenmiş kaynak veri ürünü.
- `[x] YAPILDI` 179.613.936 doğrulanan kaynak kaydı.
- `[x] YAPILDI` 1.364.582.643 bayt yerel özgün kaynak.
- `[x] YAPILDI` 15 otomatik test.
- `[x] YAPILDI` Kaynak, değer, özellik ve veri ürünü için ayrı veri sözleşmeleri.
- `[x] YAPILDI` Dosya boyutu ve SHA-256 doğrulaması.
- `[x] YAPILDI` Metin, sabit kayıt, PDS stream, PDS dizi, PDS tablo, ZIP,
  DBF ve ikili hücre sayımı.
- `[x] YAPILDI` `MEASURED`, `DERIVED`, `MODELLED`, `UNKNOWN` ayrımı.
- `[x] YAPILDI` Kaynaksız değerlerin doğrulamada reddedilmesi.

Bu sayıların hiçbiri “Mars tamamlandı” anlamına gelmez. Bir koleksiyon envanteri
tek başına bilimsel ölçüm değildir; bir yörünge örneği de küresel alan değildir.

## 3. Ana bilimsel kapsam

Tam dijital Mars aşağıdaki boyutların birlikte temsil edilmesini gerektirir:

1. Gezegen sabitleri, zaman ve referans sistemleri
2. Şekil, jeodezi, topografya ve yerçekimi
3. Jeoloji, stratigrafi, kraterler ve yüzey süreçleri
4. Mineraloji, element bileşimi ve regolit
5. İç yapı, sismoloji, ısı akısı ve jeodinamo tarihi
6. Yeraltı, su, buz ve hidrolojik geçmiş
7. Yüzey termofiziği ve radyatif özellikler
8. Alt atmosfer, meteoroloji ve sınır tabakası
9. İklim, toz, bulutlar ve atmosfer kimyası
10. Üst atmosfer, termosfer, ekzosfer ve iyonosfer
11. Güneş rüzgârı, plazma, manyetik ortam ve atmosferik kaçış
12. Radyasyon ve uzay havası
13. Phobos, Deimos ve Mars çevresi
14. Astrobiyoloji, organikler ve yaşanabilirlik göstergeleri
15. Ortak uzay-zaman veri küpü
16. Fiziksel modeller, veri özümseme ve tahmin
17. Belirsizlik, kalite, sürümleme ve yeniden üretilebilirlik
18. Sorgulama, CLI, API ve araştırma çıktıları

## 4. Faz 0 — Veri anayasası ve kaynak güvenliği

### 0.1 Kaynak ve provenans

- `[x] YAPILDI` Merkezi `resources/catalog/sources.json` kataloğu.
- `[x] YAPILDI` Her kaynak dosyası için SHA-256 ve bayt sayısı.
- `[x] YAPILDI` Yerel kaynak zorunluluğu ve arşiv istisnası alanı.
- `[x] YAPILDI` Her değer için `source_id` ve kesin `source_locator`.
- `[x] YAPILDI` Kaynak dosyalarına dokunmama/değiştirmeme ilkesi.
- `[~] KISMEN YAPILDI` DOI, PDS LID/LIDVID, sürüm ve teslim tarihi kaydı.
- `[ ] PLANLANDI` Kaynakların içerik-adresli depolama düzenine geçirilmesi.
- `[ ] PLANLANDI` Aynı dosyanın farklı kaynaklar altında yinelenmesini algılama.
- `[ ] PLANLANDI` Kaynak URL erişilebilirlik ve yönlendirme denetimi.
- `[ ] PLANLANDI` PDS3/PDS4 ürün sürüm soy ağacı.
- `[ ] PLANLANDI` Geri çekilmiş veya superseded ürün işaretleme.
- `[ ] PLANLANDI` Kaynağın yayımlanma, teslim ve erişim tarihlerinin ayrılması.
- `[ ] PLANLANDI` Makale, veri ürünü ve kalibrasyon belgesi ilişkileri.
- `[ ] PLANLANDI` Lisans ve kullanım şartlarının makinece denetlenebilir sınıfları.
- `[ ] PLANLANDI` Arşiv manifestinin imzalanması ve değişmez sürüm etiketi.

### 0.2 Veri sözleşmeleri

- `[x] YAPILDI` Kaynak, özellik, değer ve ürün JSON sözleşmeleri.
- `[x] YAPILDI` Ölçülmüş/türetilmiş/modellenmiş/bilinmeyen durumları.
- `[x] YAPILDI` Konum, zaman, birim, belirsizlik ve kaynak alanları.
- `[~] KISMEN YAPILDI` Alan bazında özellik kayıtları.
- `[ ] PLANLANDI` SI birim sözlüğü ve boyut analizi.
- `[ ] PLANLANDI` Birim eşanlamlıları: `cm-3`, `1/cm3`, `1/(cm**3)` gibi.
- `[ ] PLANLANDI` CF/UDUNITS uyumluluğu.
- `[ ] PLANLANDI` Koordinat sistemi ve datum sözlüğü.
- `[ ] PLANLANDI` Geçersiz, doygun, alt/üst sınır ve algılanmadı durumlarının ayrımı.
- `[ ] PLANLANDI` Vektör/tensör bileşen sırası sözleşmesi.
- `[ ] PLANLANDI` Spektral eksen, bant geçişi ve tepki fonksiyonu sözleşmesi.
- `[ ] PLANLANDI` Kalite bayraklarının bit düzeyinde sözlüğü.
- `[ ] PLANLANDI` Korelasyonlu belirsizlik ve kovaryans temsili.
- `[ ] PLANLANDI` Veri soy ağacı: ham → kalibre → türetilmiş → modellenmiş.

### 0.3 Yazılım ve sürekli doğrulama

- `[x] YAPILDI` Python 3.12+ temel uygulama dili.
- `[x] YAPILDI` Standart kütüphane ile çalışan çekirdek doğrulama.
- `[x] YAPILDI` 15 birim testi.
- `[ ] PLANLANDI` JSON Schema doğrulamasını CI zorunluluğu yapmak.
- `[ ] PLANLANDI` Ruff/format/type-check hattı.
- `[ ] PLANLANDI` Linux, Windows ve macOS test matrisi.
- `[ ] PLANLANDI` Kaynak indirme komutlarının yeniden üretilebilir reçeteleri.
- `[ ] PLANLANDI` İndirme devam ettirme, retry ve checksum-before-commit.
- `[ ] PLANLANDI` Büyük dosyalar için parça/nesne deposu stratejisi.
- `[ ] PLANLANDI` Bozuk PDF/FITS/CDF/NetCDF/TIFF algılama.
- `[ ] PLANLANDI` Arşivlenen XML etiket ile gerçek ikili dosya yapısı karşılaştırması.
- `[ ] PLANLANDI` Bilinen kaynak hataları için regresyon testleri.
- `[ ] PLANLANDI` Her veri katmanı için otomatik veri kartı üretimi.

**Faz 0 kabul kriteri:** Yeni bir veri ürünü tek komutla indirilebilmeli,
doğrulanabilmeli, kaynağa bağlanabilmeli ve kaynak dosyasına dokunmadan
normalize edilebilmelidir.

## 5. Faz 1 — Gezegen kimliği, sabitler, zaman ve referans sistemleri

### 1.1 Temel fiziksel sabitler

- `[x] YAPILDI` Mars kimliği ve temel NASA tanımları.
- `[x] YAPILDI` NAIF PCK00011 yerel kopyası.
- `[x] YAPILDI` Üç eksenli yarıçaplar ve şekil parametreleri.
- `[x] YAPILDI` Dönüş kutbu ve asal meridyen katsayıları.
- `[x] YAPILDI` Temel yörünge özellikleri için kaynaklı kayıtlar.
- `[~] KISMEN YAPILDI` Kütle, GM, ortalama yoğunluk ve yüzey çekimi.
- `[ ] PLANLANDI` Sabitlerin IAU çözüm/sürüm ayrımı.
- `[ ] PLANLANDI` Zamana bağlı presesyon/nutasyon terimleri.
- `[ ] PLANLANDI` Love sayıları ve gelgit yanıtı.
- `[ ] PLANLANDI` Atmosfer/yüzey kütle değişiminin düşük derece yerçekimine etkisi.

### 1.2 Zaman sistemi

- `[x] YAPILDI` Sol, mevsim ve yerel güneş zamanı özellik tanımları.
- `[~] KISMEN YAPILDI` Ls değerlerinin bazı ürünlerden korunması.
- `[ ] PLANLANDI` UTC ↔ TAI ↔ TT ↔ TDB dönüşümleri.
- `[ ] PLANLANDI` Mars Sol Date ve Coordinated Mars Time.
- `[ ] PLANLANDI` Mars Year numaralandırma sözlüğü ve kaynak sürümü.
- `[ ] PLANLANDI` Yerel gerçek/ortalama güneş zamanı dönüşümü.
- `[ ] PLANLANDI` Artık saniye ve SPICE kernel sürüm yönetimi.
- `[ ] PLANLANDI` Görev saati/SCLK ↔ UTC dönüşüm zinciri.
- `[ ] PLANLANDI` Zaman belirsizliği ve clock-correlation kalitesi.

### 1.3 Koordinat ve referans çerçeveleri

- `[x] YAPILDI` Planetosentrik ve doğu boylamı kullanan bazı ürünlerin korunması.
- `[~] KISMEN YAPILDI` Areoid, ellipsoid ve MOLA datum ayrımları.
- `[ ] PLANLANDI` IAU_MARS, J2000, MSO, MSE, GEO ve görev çerçeveleri sözlüğü.
- `[ ] PLANLANDI` Planetografik ↔ planetosentrik enlem dönüşümü.
- `[ ] PLANLANDI` Batı ↔ doğu boylamı dönüşümü.
- `[ ] PLANLANDI` Areoid ↔ ellipsoid ↔ yarıçap irtifası dönüşümü.
- `[ ] PLANLANDI` SPICE frame kernel ve instrument kernel arşivi.
- `[ ] PLANLANDI` Her geometri dönüşümü için toleranslı test vektörleri.

**Hedef birincil kaynaklar:** NASA NAIF/SPICE, IAU Working Group,
NASA PDS Geosciences ve mission-specific kernel paketleri.

## 6. Faz 2 — Şekil, jeodezi, topografya ve yerçekimi

### 2.1 Küresel topografya

- `[x] YAPILDI` MOLA MEGDR 16 piksel/derece küresel rasterleri.
- `[x] YAPILDI` MOLA yarıçap/topografya veri ve PDS etiketleri.
- `[x] YAPILDI` Raster hücre sayısı ve ikili boyut doğrulaması.
- `[x] YAPILDI` Küresel minimum/maksimum ve sıfır hücre özetleri.
- `[~] KISMEN YAPILDI` MOLA veri kalite ve örnekleme özellikleri.
- `[ ] PLANLANDI` 64 ve 128 piksel/derece MEGDR katmanları.
- `[ ] PLANLANDI` PEDR nokta ölçümleri ve yörünge izleri.
- `[ ] PLANLANDI` Atış düzeyinde hata/quality alanları.
- `[ ] PLANLANDI` Kutuplar ve veri boşlukları için özel işlemler.
- `[ ] PLANLANDI` HRSC stereo DTM bölgesel yüksek çözünürlük katmanları.
- `[ ] PLANLANDI` HiRISE stereo DTM yerel katmanları.
- `[ ] PLANLANDI` CTX stereo DTM bölgesel katmanları.
- `[ ] PLANLANDI` DTM çözünürlük piramidi ve örtüşme öncelikleri.

### 2.2 Türetilmiş arazi özellikleri

- `[ ] PLANLANDI` Eğim, bakı ve eğrilik.
- `[ ] PLANLANDI` Pürüzlülük ve yüzey normal dağılımı.
- `[ ] PLANLANDI` Gökyüzü görüş faktörü ve ufuk profili.
- `[ ] PLANLANDI` Havza, akış yönü ve drenaj ağları.
- `[ ] PLANLANDI` Çukur/dolgu ayrımı ve kapalı havzalar.
- `[ ] PLANLANDI` Uçurum, yamaç ve kütle hareketi duyarlılığı.
- `[ ] PLANLANDI` Ölçek bağımlı arazi metrikleri.
- `[ ] PLANLANDI` DTM belirsizliğinin türetilmiş metriklere yayılması.

### 2.3 Yerçekimi ve jeodezi

- `[x] YAPILDI` JGMRO-120F katsayı ürünü.
- `[x] YAPILDI` Derece/sıra, C/S harmonikleri ve sigma alanları.
- `[x] YAPILDI` Referans yarıçapı ve GM ilişkili özellikleri.
- `[~] KISMEN YAPILDI` Serbest hava/Bouguer benzeri anomali tanımları.
- `[ ] PLANLANDI` Katsayılardan küresel yerçekimi alanı üretimi.
- `[ ] PLANLANDI` Potansiyel, ivme vektörü ve gradyan tensörü.
- `[ ] PLANLANDI` Farklı irtifalarda yerçekimi haritaları.
- `[ ] PLANLANDI` Areoid ve equipotential yüzey.
- `[ ] PLANLANDI` Yerçekimi/topografya admittance ve kabuk kalınlığı modelleri.
- `[ ] PLANLANDI` Düşük derece zamansal değişimler.
- `[ ] PLANLANDI` Phobos kaynaklı gelgit sinyali.
- `[ ] PLANLANDI` Katsayı kovaryansının alan belirsizliğine yayılması.

**Faz 2 kabul kriteri:** Her enlem-boylam ve irtifa için datum bilgili
yükseklik, yüzey normali, eğim ve yerçekimi vektörü belirsizliğiyle
sorgulanabilmelidir.

## 7. Faz 3 — Jeoloji, stratigrafi, kraterler ve yüzey süreçleri

### 3.1 Küresel jeoloji

- `[x] YAPILDI` USGS SIM3292 küresel jeoloji vektörleri.
- `[x] YAPILDI` Jeolojik birim poligonları.
- `[x] YAPILDI` Doğrusal yapılar ve temas sınırları.
- `[x] YAPILDI` Birim kodu, adı, açıklaması ve stratigrafik bağlam.
- `[~] KISMEN YAPILDI` Litoloji ve jeomorfoloji özellik sözlüğü.
- `[ ] PLANLANDI` Harita geometrilerinin tam topoloji kontrolü.
- `[ ] PLANLANDI` Antimeridyen ve kutup geometrisi düzeltmeleri.
- `[ ] PLANLANDI` Birim yaş aralıklarının ortak kronolojiye dönüştürülmesi.
- `[ ] PLANLANDI` Bölgesel USGS haritalarının küresel katmanla ilişkisi.
- `[ ] PLANLANDI` Harita ölçeği/yorum belirsizliği.

### 3.2 Kraterler ve yüzey yaşı

- `[ ] PLANLANDI` Robbins/USGS benzeri küresel krater katalogları.
- `[ ] PLANLANDI` Krater merkez, çap, derinlik, morfoloji ve bozulma derecesi.
- `[ ] PLANLANDI` İkincil krater ve zincir işaretleri.
- `[ ] PLANLANDI` Gömülü/hayalet kraterler.
- `[ ] PLANLANDI` Krater sayım alanları ve üretim fonksiyonları.
- `[ ] PLANLANDI` Neukum/Hartmann kronoloji ayrımı.
- `[ ] PLANLANDI` Model yaşları ve güven aralıkları.
- `[ ] PLANLANDI` Görüntü çözünürlüğüne bağlı tespit yanlılığı.

### 3.3 Volkanizma, tektonik ve kütle hareketleri

- `[~] KISMEN YAPILDI` Volkanik birim ve yapı sınıfları SIM3292 içinde.
- `[ ] PLANLANDI` Volkan merkezleri, kalderalar, lav akıntıları ve tüpler.
- `[ ] PLANLANDI` Faylar, grabenler, wrinkle ridge ve çatlak ağları.
- `[ ] PLANLANDI` Heyelan, çığ ve kaya düşmesi envanterleri.
- `[ ] PLANLANDI` Yamaç çizgileri ve tekrar eden eğim çizgileri.
- `[ ] PLANLANDI` Çatlak/yarık yönelim istatistikleri.
- `[ ] PLANLANDI` Jeolojik aktivite yaşı ve güven düzeyi.

### 3.4 Akarsu, göl, buzul ve rüzgâr şekilleri

- `[~] KISMEN YAPILDI` Genel jeomorfoloji sınıfları.
- `[ ] PLANLANDI` Vadi ağları, çıkış kanalları ve deltalar.
- `[ ] PLANLANDI` Paleogöl sınırları ve kıyı çizgileri.
- `[ ] PLANLANDI` Alüvyal yelpazeler ve sediment depoları.
- `[ ] PLANLANDI` Buzul/vadi dolgusu/lobate debris apron envanterleri.
- `[ ] PLANLANDI` Kumul alanları, ripples ve yardanglar.
- `[ ] PLANLANDI` Kumul hareket hızları ve yönleri.
- `[ ] PLANLANDI` Toz şeytanı izleri ve yüzey değişim zaman serileri.
- `[ ] PLANLANDI` Mevsimsel CO2 fanları ve örümcek arazileri.

## 8. Faz 4 — Mineraloji, element bileşimi ve regolit

### 4.1 Spektral mineraloji

- `[x] YAPILDI` CRISM MICA tip spektrumları arşivi.
- `[x] YAPILDI` Dalga boyu, yansıma ve mineral sınıfı tanımları.
- `[~] KISMEN YAPILDI` CRISM MRDR/atmosfer ürün katalog metadatası.
- `[ ] PLANLANDI` Küresel CRISM mineral indeks haritaları.
- `[ ] PLANLANDI` OMEGA küresel mineral haritaları.
- `[ ] PLANLANDI` Mafik mineraller: olivin ve piroksen bileşimi.
- `[ ] PLANLANDI` Fe/Mg/Al fillosilikatlar.
- `[ ] PLANLANDI` Sülfatlar, karbonatlar, silika ve klorürler.
- `[ ] PLANLANDI` Hematit, ferrik oksitler ve nanofaz bileşenler.
- `[ ] PLANLANDI` Hidratasyon ve yapısal su göstergeleri.
- `[ ] PLANLANDI` Spektral karışım ve tane boyutu etkileri.
- `[ ] PLANLANDI` Atmosfer/aerosol düzeltme sürümü.
- `[ ] PLANLANDI` Mineral tespit güveni ve yanlış pozitif kontrolleri.

### 4.2 Element ve kimyasal bileşim

- `[~] KISMEN YAPILDI` Odyssey nötron ve gamma hidrojen proxy katmanları.
- `[ ] PLANLANDI` Odyssey GRS element haritaları: H, Si, Fe, Cl, K, Th vb.
- `[ ] PLANLANDI` APXS Viking/Pathfinder/MER/MSL/Perseverance ölçümleri.
- `[ ] PLANLANDI` ChemCam LIBS bileşimleri.
- `[ ] PLANLANDI` SuperCam LIBS/Raman/IR ürünleri.
- `[ ] PLANLANDI` PIXL element haritaları.
- `[ ] PLANLANDI` SHERLOC organik/mineral floresans haritaları.
- `[ ] PLANLANDI` SAM ve TEGA uçucu/izotop analizleri.
- `[ ] PLANLANDI` İniş aracı ölçümleri ile yörünge ürünlerinin çapraz kalibrasyonu.

### 4.3 Regolit fiziksel özellikleri

- `[~] KISMEN YAPILDI` Termal atalet ve albedo.
- `[ ] PLANLANDI` Tane boyutu sınıfları.
- `[ ] PLANLANDI` Bulk density, particle density ve porozite.
- `[ ] PLANLANDI` Kohezyon, içsel sürtünme açısı ve taşıma kapasitesi.
- `[ ] PLANLANDI` Dielektrik sabiti ve radar kayıp tanjantı.
- `[ ] PLANLANDI` Isıl iletkenlik ve ısı kapasitesi.
- `[ ] PLANLANDI` Higroskopik tuzlar ve perklorat dağılımı.
- `[ ] PLANLANDI` Çimentolanma, duricrust ve kaya/regolit oranı.
- `[ ] PLANLANDI` Kaya bolluğu ve boyut dağılımı.
- `[ ] PLANLANDI` Mühendislik özelliklerinin ölçülmüş/model kaynak ayrımı.

## 9. Faz 5 — İç yapı, sismoloji, ısı akısı ve jeodinamo

### 5.1 Sismoloji

- `[ ] PLANLANDI` InSight SEIS olay kataloğu.
- `[ ] PLANLANDI` Ham, kalibre ve olay kesitlerinin ayrılması.
- `[ ] PLANLANDI` Marsquake sınıfları ve faz seçimleri.
- `[ ] PLANLANDI` Epicenter, derinlik, büyüklük ve belirsizlik.
- `[ ] PLANLANDI` Gürültü, rüzgâr ve sıcaklık korelasyonları.
- `[ ] PLANLANDI` Kabuk/manto hız modelleri.
- `[ ] PLANLANDI` Receiver function ve yüzey dalgası kısıtları.
- `[ ] PLANLANDI` Çekirdek geçişli fazlar.
- `[ ] PLANLANDI` Meteoroid çarpma olaylarının sismik/krater eşleşmesi.

### 5.2 İç yapı

- `[ ] PLANLANDI` Kabuk kalınlığı model ailesi.
- `[ ] PLANLANDI` Manto yoğunluk ve hız profilleri.
- `[ ] PLANLANDI` Çekirdek yarıçapı, yoğunluğu ve bileşim modelleri.
- `[ ] PLANLANDI` Katı/sıvı katman olasılıkları.
- `[ ] PLANLANDI` Moment of inertia ve nutation kısıtları.
- `[ ] PLANLANDI` Model ensemble ve posterior dağılımları.
- `[ ] PLANLANDI` Tek bir “doğru iç yapı” yerine model ailelerinin korunması.

### 5.3 Isı ve manyetik geçmiş

- `[ ] PLANLANDI` InSight HP3 radyometre/ısı özellikleri.
- `[ ] PLANLANDI` Jeotermal ısı akısı model haritaları.
- `[ ] PLANLANDI` Radyojenik element katkıları.
- `[ ] PLANLANDI` Litosfer elastik kalınlığı.
- `[ ] PLANLANDI` Volkanik/tektonik termal evrim modelleri.
- `[x] YAPILDI` MGS ER B185 küresel kabuksal alan büyüklüğü haritası.
- `[~] KISMEN YAPILDI` Kabuksal manyetik hassasiyet ve çözünürlük bilgisi.
- `[ ] PLANLANDI` Vektörel kabuksal alan model aileleri.
- `[ ] PLANLANDI` Farklı irtifalarda alan devamı.
- `[ ] PLANLANDI` Paleokutup ve dinamo kapanış kronolojisi.

**Hedef birincil kaynaklar:** NASA PDS Geosciences, InSight SEIS/RISE/HP3
koleksiyonları, IPGP Marsquake Service yayınları ve hakemli model ürünleri.

## 10. Faz 6 — Yeraltı, su, buz ve hidrolojik geçmiş

### 6.1 Güncel yüzey/yeraltı buzu

- `[x] YAPILDI` Odyssey NS/HEND nötron akı haritaları.
- `[x] YAPILDI` Nötron akısının doğrudan su yüzdesi olmadığı kaydı.
- `[~] KISMEN YAPILDI` SWIM kaynak/metodoloji kaydı.
- `[~] KISMEN YAPILDI` Su/buz özellik sözlüğü.
- `[ ] PLANLANDI` WEH türetilmiş haritaları ve model sürümleri.
- `[ ] PLANLANDI` SWIM raster katmanlarının gerçek yerel kopyaları.
- `[ ] PLANLANDI` Buz kararlılık derinliği.
- `[ ] PLANLANDI` Phoenix TECP/TEGA yerel buz ölçümleri.
- `[ ] PLANLANDI` Yeni çarpma kraterlerinde açığa çıkan buz envanteri.
- `[ ] PLANLANDI` Orta enlem buz örtüsü ve excess-ice olasılığı.
- `[ ] PLANLANDI` Kutuplardaki H2O ve CO2 buzunun ayrılması.

### 6.2 Radar yeraltı yapısı

- `[~] KISMEN YAPILDI` SHARAD RDR kaynak metadatası.
- `[ ] PLANLANDI` SHARAD radargram ve yüzey izleri.
- `[ ] PLANLANDI` MARSIS subsurface radar ürünleri.
- `[ ] PLANLANDI` Delay-time → derinlik dönüşümünde dielektrik model ailesi.
- `[ ] PLANLANDI` Kutuplardaki katmanlı depo radar sınırları.
- `[ ] PLANLANDI` Orta enlem gömülü buz yapıları.
- `[ ] PLANLANDI` Medusae Fossae ve volkanik birim dielektrik özellikleri.
- `[ ] PLANLANDI` Clutter simülasyonu ve yanlış yeraltı yankısı işaretleri.
- `[ ] PLANLANDI` Radar tespit güveni ve alternatif yorumlar.

### 6.3 Kutuplar ve mevsimsel buz

- `[ ] PLANLANDI` Kuzey/güney polar layered deposits geometrisi.
- `[ ] PLANLANDI` Mevsimsel CO2 başlık sınırları.
- `[ ] PLANLANDI` MARCI günlük/haftalık polar kap haritaları.
- `[ ] PLANLANDI` MOLA seasonal height değişimleri.
- `[ ] PLANLANDI` Polar kütle ve hacim tahminleri.
- `[ ] PLANLANDI` Spiral trough, basal unit ve scarp retreat.
- `[ ] PLANLANDI` Buz saflığı, toz oranı ve tabakalanma.

### 6.4 Paleohidroloji

- `[ ] PLANLANDI` Vadi ağı ve drenaj havzaları.
- `[ ] PLANLANDI` Deltalar ve göl çökeltileri.
- `[ ] PLANLANDI` Kıyı çizgisi hipotezleri ve karşıt yorumlar.
- `[ ] PLANLANDI` Mineralojiyle su geçmişi eşleştirmesi.
- `[ ] PLANLANDI` Yeraltı suyu/sapping göstergeleri.
- `[ ] PLANLANDI` Hidrotermal sistem göstergeleri.
- `[ ] PLANLANDI` Su envanteri zaman çizelgesi ve belirsizlik.

## 11. Faz 7 — Yüzey termofiziği ve radyatif özellikler

### 7.1 Termal atalet, albedo ve sıcaklık

- `[x] YAPILDI` TES küresel bolometrik albedo.
- `[x] YAPILDI` TES gündüz/gece termal atalet ürünleri.
- `[x] YAPILDI` TES TIMAP türetilmiş termal atalet haritaları.
- `[~] KISMEN YAPILDI` Kaynak kalite ve dönüşüm ayrımları.
- `[ ] PLANLANDI` THEMIS gündüz/gece sıcaklık mozaikleri.
- `[ ] PLANLANDI` THEMIS termal atalet ürünleri.
- `[ ] PLANLANDI` MCS yüzey sıcaklığı.
- `[ ] PLANLANDI` Viking, Pathfinder, MER, Phoenix, MSL ve InSight yerel sıcaklıkları.
- `[ ] PLANLANDI` Emissivity spektrumları.
- `[ ] PLANLANDI` Bond/geometrik/spektral albedo ayrımı.
- `[ ] PLANLANDI` Mevsim ve yerel saate bağlı yüzey sıcaklığı veri küpü.

### 7.2 Yüzey enerji dengesi

- `[ ] PLANLANDI` Güneş geometrisi ve gölgeleme.
- `[ ] PLANLANDI` Kısa/uzun dalga radyatif akılar.
- `[ ] PLANLANDI` Duyulur ve gizli ısı akıları.
- `[ ] PLANLANDI` Zemine ısı iletimi.
- `[ ] PLANLANDI` CO2/H2O kırağı enerji dengesi.
- `[ ] PLANLANDI` Toz örtüsünün albedo/termal atalet etkisi.
- `[ ] PLANLANDI` Alt piksel kaya-regolit karışımı.

## 12. Faz 8 — Alt atmosfer, meteoroloji ve sınır tabakası

### 8.1 Yüzey meteoroloji istasyonları

- `[x] YAPILDI` REMS MODRDR kaynak ve ürün yapısı.
- `[x] YAPILDI` Sol 4709 için 34.258 satırlık gerçek REMS tablosu.
- `[x] YAPILDI` Basınç, hava/zemin sıcaklığı, rüzgâr, nem ve UV özellikleri.
- `[x] YAPILDI` `-999` eksik veri kodunun fiziksel değer sayılmaması.
- `[~] KISMEN YAPILDI` REMS güven/kalite kodları.
- `[ ] PLANLANDI` Tam REMS görev zaman serisi.
- `[ ] PLANLANDI` MEDA tam zaman serisi.
- `[ ] PLANLANDI` InSight APSS/TWINS/PS tam zaman serisi.
- `[ ] PLANLANDI` Phoenix MET ve TECP.
- `[ ] PLANLANDI` Viking Lander meteoroloji.
- `[ ] PLANLANDI` Pathfinder ASI/MET.
- `[ ] PLANLANDI` Görevler arası basınç ve sıcaklık çapraz kalibrasyonu.

### 8.2 Dikey atmosfer profilleri

- `[x] YAPILDI` MCS V6.2 kümülatif ürün dizini.
- `[x] YAPILDI` 105 basınç seviyeli 379 gerçek profil örneği.
- `[x] YAPILDI` Sıcaklık, basınç, toz ve su-buzu profili özellikleri.
- `[~] KISMEN YAPILDI` Retrieval kalite ve belirsizlik alanları.
- `[ ] PLANLANDI` Tam MCS profil arşivi.
- `[ ] PLANLANDI` Radio occultation profilleri.
- `[ ] PLANLANDI` SPICAM stellar/solar occultation profilleri.
- `[ ] PLANLANDI` TGO ACS/NOMAD occultation profilleri.
- `[ ] PLANLANDI` Entry/Descent atmosfer profilleri.
- `[ ] PLANLANDI` Basınç ↔ irtifa dönüşüm model/belirsizlikleri.

### 8.3 Atmosfer durumu ve sınır tabakası

- `[~] KISMEN YAPILDI` Basınç, sıcaklık, rüzgâr, nem özellik modeli.
- `[ ] PLANLANDI` Planetary boundary layer yüksekliği.
- `[ ] PLANLANDI` Konvektif hücreler ve türbülans.
- `[ ] PLANLANDI` Gece inversiyonları.
- `[ ] PLANLANDI` Katabatik/anabatik akışlar.
- `[ ] PLANLANDI` Yerel topoğrafik rüzgâr sistemleri.
- `[ ] PLANLANDI` Gelgitler, Kelvin dalgaları ve baroklinik dalgalar.
- `[ ] PLANLANDI` Toz şeytanı basınç düşüş olay kataloğu.
- `[ ] PLANLANDI` Rüzgâr sensörü hasarı/yanlılık modelleri.

**Faz 8 kabul kriteri:** Belirli konum, sol, yerel saat ve irtifa için
ölçümlere dayalı atmosfer durumu ile boşluklarda model sonucu birbirine
karıştırılmadan döndürülebilmelidir.

## 13. Faz 9 — İklim, toz, bulutlar ve atmosfer kimyası

### 9.1 Toz

- `[~] KISMEN YAPILDI` MCS toz profili örneği.
- `[~] KISMEN YAPILDI` TES albedo/termal ürünleri.
- `[ ] PLANLANDI` MCS tam toz extinction profilleri.
- `[ ] PLANLANDI` TES ve THEMIS toz optik derinliği.
- `[ ] PLANLANDI` MARCI günlük küresel toz haritaları.
- `[ ] PLANLANDI` MSL/MER/Phoenix/InSight tau zaman serileri.
- `[ ] PLANLANDI` Bölgesel ve küresel toz fırtınası kataloğu.
- `[ ] PLANLANDI` Fırtına başlangıç, büyüme, taşıma ve çökme evreleri.
- `[ ] PLANLANDI` Toz parçacık boyutu ve dikey dağılım.
- `[ ] PLANLANDI` Toz kaldırma eşiği ve yüzey stresi.
- `[ ] PLANLANDI` MY25, MY28 ve MY34 küresel fırtına karşılaştırmaları.

### 9.2 Su-buzu ve CO2 bulutları

- `[x] YAPILDI` MCS örneğinde su-buzu profil/kolon özellikleri.
- `[ ] PLANLANDI` Tam MCS bulut profilleri.
- `[ ] PLANLANDI` MARCI su-buzu bulut haritaları.
- `[ ] PLANLANDI` Aphelion cloud belt zaman serisi.
- `[ ] PLANLANDI` Orographic clouds ve Arsia Mons elongated cloud.
- `[ ] PLANLANDI` Gece parlayan yüksek irtifa bulutları.
- `[ ] PLANLANDI` CO2 bulutu tespitleri.
- `[ ] PLANLANDI` Bulut parçacık boyutu ve optik özellikleri.

### 9.3 Gazlar ve fotokimya

- `[x] YAPILDI` Kaynaklı referans atmosfer bileşimi.
- `[~] KISMEN YAPILDI` NGIMS üst atmosfer nötr bileşim örnekleri.
- `[~] KISMEN YAPILDI` IUVS CO2/N2/O yoğunluk geri-kazanımları.
- `[ ] PLANLANDI` CO2, N2, Ar ve O2 yüzey/yörünge gözlemleri.
- `[ ] PLANLANDI` H2O sütun bolluğu ve dikey profilleri.
- `[ ] PLANLANDI` O3 sütun/profil haritaları.
- `[ ] PLANLANDI` CO dağılımı.
- `[ ] PLANLANDI` HDO ve D/H alt atmosfer dağılımı.
- `[ ] PLANLANDI` CH4 tespitleri, üst sınırlar ve araçlar arası uyuşmazlık.
- `[ ] PLANLANDI` HCl ve diğer iz gazlar.
- `[ ] PLANLANDI` O2 nightglow/dayglow ürünleri.
- `[ ] PLANLANDI` Fotokimyasal reaksiyon ağı ve hız katsayı kaynakları.
- `[ ] PLANLANDI` İzotoplar: D/H, 13C/12C, 15N/14N, 38Ar/36Ar vb.

### 9.4 İklim tarihi ve paleoiklim

- `[ ] PLANLANDI` Orbital forcing: obliquity, eccentricity, perihelion.
- `[ ] PLANLANDI` Polar tabaka iklim kayıtları.
- `[ ] PLANLANDI` Buzul birikim çağları.
- `[ ] PLANLANDI` Göl/delta oluşum iklim koşulları.
- `[ ] PLANLANDI` Erken Mars sera senaryoları.
- `[ ] PLANLANDI` Model ensemble ve senaryo belirsizlikleri.

## 14. Faz 10 — Üst atmosfer, termosfer, ekzosfer ve iyonosfer

### 10.1 NGIMS

- `[x] YAPILDI` Şubat 2026 L2: 33.583 üyelik tam envanteri.
- `[x] YAPILDI` L3: 27.606 üyelik tam envanteri.
- `[x] YAPILDI` Gerçek nötr ürün: Ar, CO2, N2, He, CO ve O.
- `[x] YAPILDI` Gerçek iyon kütle/yük kanalı ürünü.
- `[x] YAPILDI` L3 yeniden örneklenmiş yoğunluk profili.
- `[x] YAPILDI` L3 ölçek yüksekliği/sıcaklık uyumu.
- `[x] YAPILDI` Belgelenmemiş `-999` değerlerinin fiziksel sayılmaması.
- `[x] YAPILDI` Kütle kanalına kaynaksız iyon kimliği atanmaması.
- `[~] KISMEN YAPILDI` Yalnız seçilmiş gerçek ürünler yerel.
- `[ ] PLANLANDI` Tam NGIMS bilim ürün koleksiyonları.
- `[ ] PLANLANDI` Orbit/season/local-time binned nötr climatology.
- `[ ] PLANLANDI` İyon bileşimi için güvenli kütle dekonvolüsyonu.
- `[ ] PLANLANDI` Deep-dip kampanyalarının ayrı katmanı.

### 10.2 IUVS limb

- `[x] YAPILDI` V13 kalibre limb: 632.427 üyelik tam envanteri.
- `[x] YAPILDI` V13 işlenmiş limb: 8.706 üyelik tam envanteri.
- `[x] YAPILDI` V13 türetilmiş limb: 6.505 üyelik tam envanteri.
- `[x] YAPILDI` Gerçek 33×7×512 FUV spektral radyans küpü.
- `[x] YAPILDI` Gerçek CO2/N2/O yoğunluk profili ürünü.
- `[x] YAPILDI` Sıcaklık, model radyansı, 29 emisyon ve geometri yapısı.
- `[x] YAPILDI` Rastgele ve sistematik belirsizliklerin ayrılması.
- `[x] YAPILDI` Web/derived koleksiyon çelişkisinin korunması.
- `[x] YAPILDI` XML tür açıklaması/FITS içeriği çelişkisinin korunması.
- `[~] KISMEN YAPILDI` Yalnız iki gerçek FITS ürün yerel.
- `[ ] PLANLANDI` Tam veya temsilî stratified limb örnek seti.
- `[ ] PLANLANDI` Retrieval kalite/başarısızlık maskeleri.
- `[ ] PLANLANDI` Tür bazında sezon ve yerel zaman climatology.

### 10.3 IUVS diğer modları

- `[x] YAPILDI` Corona calibrated V13: 18.887 üyelik tam envanter.
- `[x] YAPILDI` Corona processed ve derived V7: 496'şar üyelik tam envanter.
- `[x] YAPILDI` Gerçek H/O L2 corona tarama ürünü ve üç tarama bileşeni.
- `[x] YAPILDI` `H_1216`/`O_1304`, sütun/yoğunluk, radyans ve geometri
  alanlarının kaynaklı özellik sözlüğü.
- `[x] YAPILDI` Örnek model sonuçlarındaki IEEE `NaN` alanların fiziksel
  sıcaklık, yoğunluk, enerji veya kaçış değeri olarak reddedilmesi.
- `[x] YAPILDI` Corona V13/V7 dönem asimetrisinin ve XML/FITS tür
  çelişkisinin korunması.
- `[~] KISMEN YAPILDI` H ve O sıcak korona haritaları: tek gerçek L2 tarama
  örneği yerel; küresel/mevsimsel harita kapsamı henüz yok.
- `[ ] PLANLANDI` Dönem, yörünge, yerel zaman ve geometri bakımından
  katmanlı gerçek corona örnek seti.
- `[x] YAPILDI` Echelle calibrated: 47.106 üyelik tam envanter.
- `[x] YAPILDI` Echelle processed: 46.662 üyelik tam envanter.
- `[x] YAPILDI` Gerçek V14 L1C outlimb ürünü: 8×74×332 ana dizi ve
  sekiz entegrasyon.
- `[x] YAPILDI` H 1215,67 Å ve D 1215,34 Å Lyman-alfa parlaklıkları,
  alt-sınır bir-sigma belirsizliği ve piksel geometrisi.
- `[x] YAPILDI` Echelle V13 koleksiyon etiketi/V14 üye sürümü
  uyuşmazlığının korunması.
- `[~] KISMEN YAPILDI` D/H ölçümleri ve belirsizlikleri: gerçek H/D
  parlaklıkları var; doğrudan atmosferik D/H bolluk oranı yok.
- `[x] YAPILDI` H/D parlaklık oranından kaynaksız D/H türetilmemesi.
- `[ ] PLANLANDI` Echelle dönem, irtifa, yerel zaman ve gözlem türüne göre
  katmanlı gerçek örnek seti.
- `[x] YAPILDI` Disk calibrated V13: 633.461 üyelik tam envanter.
- `[x] YAPILDI` Disk processed V7: 1.690 üyelik tam envanter.
- `[x] YAPILDI` Disk derived V7: 1.869 üyelik tam envanter.
- `[~] KISMEN YAPILDI` Disk mapping FUV/MUV radyansları: eşleşmiş gerçek
  FUV/MUV L2 harita çifti yerel; gerçek calibrated radyans örneği henüz yok.
- `[x] YAPILDI` FUV 11 emisyon, iki parlaklık oranı, `CO/CO2` ve `O/CO2`
  sütun oranı haritaları ile rastgele/sistematik belirsizlik yapısı.
- `[x] YAPILDI` MUV 180×90 O3 sütunu, yüzey-artı-bulut albedosu ve toz
  opaklığı haritaları; bir-sigma ve ki-kare alanları.
- `[~] KISMEN YAPILDI` Disk O3/H2O ilişkili türetilmiş ürünleri: O3 gerçek
  örnekte var, doğrudan H2O alanı yok.
- `[x] YAPILDI` Belgeli `-1` boş-hücre dolgusu ile belgesiz `-40`
  belirsizlik sentinelinin fiziksel değerlerden ayrılması.
- `[x] YAPILDI` V07 `SZA < 80°`, yüksek-emisyon-açısı geometri caveat'ları
  ve FUV XML/FITS zaman çelişkisinin korunması.
- `[ ] PLANLANDI` Disk dönem, sezon, yerel zaman ve kanal bakımından
  katmanlı gerçek örnek seti.
- `[ ] PLANLANDI` Stellar occultation transmission ve profilleri.
- `[ ] PLANLANDI` Phobos ve Siding Spring özel gözlemleri.

### 10.4 LPW ve iyonosfer

- `[x] YAPILDI` LP-NT V6.2: 3.977 üyelik envanteri.
- `[x] YAPILDI` W-N V6.7: 1.089 üyelik envanteri.
- `[x] YAPILDI` 21.590 adet on-nicelikli IV uyumu.
- `[x] YAPILDI` 30 Langmuir-line yoğunluk tespiti.
- `[x] YAPILDI` `flag > 50` ve `flag > 46` kullanım ayrımı.
- `[x] YAPILDI` NaN değerlerinin fiziksel sıfır sayılmaması.
- `[~] KISMEN YAPILDI` Bir günlük gerçek örnekler.
- `[ ] PLANLANDI` LPW tam görev zaman serileri.
- `[ ] PLANLANDI` Elektron yoğunluğu/sıcaklığı climatology.
- `[ ] PLANLANDI` Total electron content ve ionopause.
- `[ ] PLANLANDI` Radio occultation iyonosfer profilleri.
- `[ ] PLANLANDI` Gün/gece, SZA, crustal-field ve solar forcing ayrımları.

## 15. Faz 11 — Güneş rüzgârı, plazma, manyetik ortam ve kaçış

### 11.1 Manyetik alan

- `[x] YAPILDI` MAVEN MAG V2.38 planetosentrik envanter.
- `[x] YAPILDI` 2025-12-01 gerçek 1 saniyelik örnek.
- `[x] YAPILDI` Vektör, konum, koordinat ve kalite özellikleri.
- `[x] YAPILDI` MGS ER B185 kabuksal alan haritası.
- `[~] KISMEN YAPILDI` Yörünge örneği ve tek türetilmiş küresel harita.
- `[ ] PLANLANDI` Tam MAVEN MAG görev zaman serisi.
- `[ ] PLANLANDI` MSO/MSE/planetosentrik dönüşümler.
- `[ ] PLANLANDI` Shock, magnetic pileup boundary ve induced magnetosphere sınırları.
- `[ ] PLANLANDI` Crustal-field topology ve mini-magnetosphere olayları.
- `[ ] PLANLANDI` Manyetik alan model ensemble.

### 11.2 SWIA ve iyon plazması

- `[x] YAPILDI` SWIA V2.16: 4.094 üyelik tam envanteri.
- `[x] YAPILDI` 21.600 gerçek onboard moment seti.
- `[x] YAPILDI` Yoğunluk, hız, sıcaklık ve basınç tensörü.
- `[x] YAPILDI` Proton varsayımı ve alfa sıcaklık yanlılığı uyarıları.
- `[x] YAPILDI` Kalite ve cihaz durum alanları.
- `[~] KISMEN YAPILDI` Bir günlük örnek.
- `[ ] PLANLANDI` Tam SWIA moment ve dağılım arşivi.
- `[ ] PLANLANDI` Güneş rüzgârı upstream seçim algoritması.
- `[ ] PLANLANDI` Shock geçişleri ve sheath özellikleri.
- `[ ] PLANLANDI` Heavy-ion kaçışla ortak analiz.

### 11.3 Diğer MAVEN plazma cihazları

- `[ ] PLANLANDI` STATIC iyon kütle/enerji/açı dağılımları.
- `[ ] PLANLANDI` SWEA elektron spektrumları ve pitch-angle.
- `[ ] PLANLANDI` SEP enerjik parçacık akıları.
- `[ ] PLANLANDI` EUVM güneş EUV irradiance.
- `[ ] PLANLANDI` PWS dalga ve elektrik alan ürünleri.
- `[ ] PLANLANDI` KP birleşik ürünleri ve kaynak bileşen ilişkileri.
- `[ ] PLANLANDI` Araç potansiyeli ve şarj etkileri.

### 11.4 Atmosferik kaçış

- `[~] KISMEN YAPILDI` Kaçışla ilişkili nötr/iyon/plazma niceliklerinin temeli.
- `[ ] PLANLANDI` İyon kaçış akısı ve türleri.
- `[ ] PLANLANDI` Fotokimyasal kaçış.
- `[ ] PLANLANDI` Sputtering.
- `[ ] PLANLANDI` Jeans ve hidrodinamik kaçış sınırları.
- `[ ] PLANLANDI` H/O korona ile escape-rate ilişkisi.
- `[ ] PLANLANDI` Solar storm etkileri.
- `[ ] PLANLANDI` Güncel kaçıştan tarihsel su kaybına model geçişi.
- `[ ] PLANLANDI` Mekanizma bazında belirsizlik bütçesi.

## 16. Faz 12 — Radyasyon ve uzay havası

### 12.1 Yüzey radyasyonu

- `[x] YAPILDI` MSL RAD güncel ürün dizini ve teknik belgeler.
- `[x] YAPILDI` Bir gerçek Curiosity yüzey solu örneği.
- `[x] YAPILDI` Doz, doz eşdeğeri, parçacık akısı ve kalite özellikleri.
- `[~] KISMEN YAPILDI` Yalnız tek-sol gerçek veri.
- `[ ] PLANLANDI` Tam RAD yüzey görev zaman serisi.
- `[ ] PLANLANDI` Cruise ve yüzey dönemlerinin ayrılması.
- `[ ] PLANLANDI` GCR, SEP ve albedo neutron bileşenleri.
- `[ ] PLANLANDI` MEDA/RAD atmosfer basıncı modülasyonu.
- `[ ] PLANLANDI` Curiosity konum/topografya kalkanlama etkisi.

### 12.2 Yörünge ve uzay havası

- `[ ] PLANLANDI` MAVEN SEP tam zaman serisi.
- `[ ] PLANLANDI` Mars Odyssey HEND yüksek enerji olayları.
- `[ ] PLANLANDI` Solar flare/CME/SEP olay kataloğu.
- `[ ] PLANLANDI` Güneş rüzgârı geliş zamanı ve Mars bağlantısı.
- `[ ] PLANLANDI` Forbush decrease olayları.
- `[ ] PLANLANDI` Solar cycle ve heliospheric modulation.

### 12.3 Radyasyon alan modeli

- `[ ] PLANLANDI` Atmosfer kolon derinliğine bağlı doz.
- `[ ] PLANLANDI` Yükseklik/topografya etkisi.
- `[ ] PLANLANDI` Regolit bileşimi ve ikincil nötronlar.
- `[ ] PLANLANDI` Parçacık türü/enerji spektrumu.
- `[ ] PLANLANDI` Organ doz ve kalite faktörlerinin kaynaklı ayrımı.
- `[ ] PLANLANDI` BFO, cilt, göz ve elektronik doz modelleri.
- `[ ] PLANLANDI` Kubbe/şehir hesabından bağımsız doğal çevre radyasyon haritası.
- `[ ] PLANLANDI` Ölçüm, transport modeli ve mühendislik sınırının ayrılması.

## 17. Faz 13 — Phobos, Deimos ve Mars çevresi

- `[ ] PLANLANDI` Phobos/Deimos şekil modelleri.
- `[ ] PLANLANDI` Kütle, GM, yoğunluk ve dönme durumu.
- `[ ] PLANLANDI` Yörünge ve gelgit evrimi.
- `[ ] PLANLANDI` Yüzey jeolojisi, spektrum ve termal özellikler.
- `[ ] PLANLANDI` Phobos grooves ve Stickney morfolojisi.
- `[ ] PLANLANDI` Deimos yüzey birimleri.
- `[ ] PLANLANDI` Mars gölgesi ve tutulmalar.
- `[ ] PLANLANDI` Phobos transit gözlemleri.
- `[ ] PLANLANDI` Toz halkası için gözlemsel üst sınırlar.
- `[ ] PLANLANDI` Mars Trojan ve çevresel küçük cisim bağlamı.
- `[ ] PLANLANDI` MMX verileri yayımlandığında sürümlü entegrasyon.

## 18. Faz 14 — Astrobiyoloji, organikler ve yaşanabilirlik

Bu faz “Mars'ta yaşam var” gibi kaynaksız bir sonuç üretmeyecek. Ölçüm,
tespit, üst sınır, kontaminasyon olasılığı ve yorum birbirinden ayrılacaktır.

### 14.1 Organik kimya

- `[ ] PLANLANDI` Viking GCMS sonuçları ve algılama sınırları.
- `[ ] PLANLANDI` Phoenix TEGA sonuçları.
- `[ ] PLANLANDI` MSL SAM organik bileşikleri.
- `[ ] PLANLANDI` Curiosity drill/sample bağlamı.
- `[ ] PLANLANDI` Perseverance SHERLOC organik göstergeleri.
- `[ ] PLANLANDI` Meteoritik organik girdi modelleri.
- `[ ] PLANLANDI` Perklorat kaynaklı piroliz ürünleri.
- `[ ] PLANLANDI` Dünya kaynaklı kontaminasyon ve blank ölçümleri.

### 14.2 Yaşanabilirlik göstergeleri

- `[ ] PLANLANDI` Sıvı su etkinliği.
- `[ ] PLANLANDI` Sıcaklık ve basınç pencereleri.
- `[ ] PLANLANDI` pH, redoks ve tuzluluk göstergeleri.
- `[ ] PLANLANDI` Enerji kaynakları ve elektron donor/acceptor çiftleri.
- `[ ] PLANLANDI` UV ve iyonlaştırıcı radyasyon yükü.
- `[ ] PLANLANDI` Organik korunma potansiyeli.
- `[ ] PLANLANDI` Kil, silika, sülfat ve evaporit ortamları.
- `[ ] PLANLANDI` Hidrotermal ve yeraltı yaşam alanı olasılıkları.
- `[ ] PLANLANDI` “Yaşanabilir”, “yaşanmış” ve “yaşam tespit edildi” ayrımı.

### 14.3 Biyoişaretler ve gezegen koruma

- `[ ] PLANLANDI` Morfolojik, organik, izotopik ve mineral biyoişaret sınıfları.
- `[ ] PLANLANDI` Abiyotik taklit süreçleri.
- `[ ] PLANLANDI` Tespit güven seviyesi.
- `[ ] PLANLANDI` Special Regions tanımları ve sürümleri.
- `[ ] PLANLANDI` İleri/geri kontaminasyon kısıtları.
- `[ ] PLANLANDI` Numune alma/önbellekleme zinciri.
- `[ ] PLANLANDI` Mars meteoriti laboratuvar verileri.

## 19. Faz 15 — Ortak uzay-zaman veri küpü

### 15.1 Ortak ızgara

- `[ ] PLANLANDI` Küresel hiyerarşik hücre sistemi seçimi.
- `[ ] PLANLANDI` Eşit açılı ve eşit alan ızgara seçenekleri.
- `[ ] PLANLANDI` Çok çözünürlüklü tile/pyramid düzeni.
- `[ ] PLANLANDI` Antimeridyen ve kutup davranışı.
- `[ ] PLANLANDI` Yüzey, atmosfer, yeraltı ve yörünge örneklerinin aynı adresleme sistemi.
- `[ ] PLANLANDI` İrtifa ve basınç dikey koordinatlarının birlikte desteği.
- `[ ] PLANLANDI` Yeraltı derinlik ekseni.
- `[ ] PLANLANDI` Spektral/enerji/kütle ek eksenleri.

### 15.2 Uzay-zaman indeksleme

- `[ ] PLANLANDI` UTC, sol, Mars yılı, Ls ve yerel saat indeksleri.
- `[ ] PLANLANDI` Anlık, aralık, climatology ve time-invariant ayrımı.
- `[ ] PLANLANDI` Nokta, yörünge izi, swath, profil, raster ve hacim geometrileri.
- `[ ] PLANLANDI` En yakın komşu, alan örtüşmesi ve hacim kesişimi.
- `[ ] PLANLANDI` Ölçüm footprint ve point-spread function.
- `[ ] PLANLANDI` Farklı çözünürlüklerin yeniden örnekleme politikasının kaydı.
- `[ ] PLANLANDI` Veri boşluğu ile fiziksel sıfırın kesin ayrılması.

### 15.3 Depolama

- `[ ] PLANLANDI` Zarr/NetCDF/Parquet/COG aday değerlendirmesi.
- `[ ] PLANLANDI` Sıkıştırma ve chunk stratejisi.
- `[ ] PLANLANDI` Ham kaynak ile normalize cache ayrımı.
- `[ ] PLANLANDI` Petabayta büyüyebilir nesne depolama tasarımı.
- `[ ] PLANLANDI` İçerik adresli immutable sürümler.
- `[ ] PLANLANDI` Delta güncellemeleri ve yeniden üretilebilir build.
- `[ ] PLANLANDI` Yerel/offline çalışma modu.

**Faz 15 kabul kriteri:** Her veri değeri kaynak dosyasına geri izlenebilir
olacak şekilde konum-zaman-dikey eksen üzerinden sorgulanabilmelidir.

## 20. Faz 16 — Modeller, veri özümseme ve fiziksel dijital ikiz

Bu faz mevcut verileri değiştirmez. Model çıktıları daima `MODELLED`
olarak ayrı tutulur.

### 16.1 Atmosfer modelleri

- `[ ] PLANLANDI` Mars Climate Database/GCM çıktıları.
- `[ ] PLANLANDI` MGCM model aileleri.
- `[ ] PLANLANDI` Mesoscale ve LES model ürünleri.
- `[ ] PLANLANDI` Fotokimya modelleri.
- `[ ] PLANLANDI` Termosfer/iyonosfer modelleri.
- `[ ] PLANLANDI` Toz kaldırma/taşıma/çökme modelleri.
- `[ ] PLANLANDI` Su döngüsü ve bulut mikrofiziği.

### 16.2 Plazma ve kaçış modelleri

- `[ ] PLANLANDI` MHD/hybrid induced-magnetosphere modelleri.
- `[ ] PLANLANDI` Test-particle ve kinetic modeller.
- `[ ] PLANLANDI` Neutral corona/exosphere modelleri.
- `[ ] PLANLANDI` İyon üretim/taşıma/kayıp ağı.
- `[ ] PLANLANDI` Model-observation residual ürünleri.

### 16.3 Yüzey/yeraltı modelleri

- `[ ] PLANLANDI` 1D/3D ısı iletimi.
- `[ ] PLANLANDI` Buz kararlılığı ve difüzyon.
- `[ ] PLANLANDI` Regolit gaz/nem taşınımı.
- `[ ] PLANLANDI` Erozyon ve sediment taşınımı.
- `[ ] PLANLANDI` Krater yaş ve yüzey yenilenme modelleri.

### 16.4 Veri özümseme ve tahmin

- `[ ] PLANLANDI` Observation operator sözleşmesi.
- `[ ] PLANLANDI` Bias correction ve cross-calibration.
- `[ ] PLANLANDI` Ensemble veri özümseme.
- `[ ] PLANLANDI` Posterior alan ve kovaryans.
- `[ ] PLANLANDI` Hindcast/reanalysis.
- `[ ] PLANLANDI` Forecast ile climatology ayrımı.
- `[ ] PLANLANDI` Model sürüm ve başlangıç koşulu kaydı.
- `[ ] PLANLANDI` Fizik yasası/korunum kontrolleri.

## 21. Faz 17 — Kalite, belirsizlik ve bilimsel doğrulama

### 17.1 Belirsizlik bütçesi

- `[~] KISMEN YAPILDI` Birçok üründe kaynak belirsizlik alanları korunuyor.
- `[x] YAPILDI` IUVS rastgele/sistematik belirsizlik ayrımı.
- `[x] YAPILDI` NGIMS fit ve kalite sınırlamaları.
- `[x] YAPILDI` LPW kalite eşikleri.
- `[ ] PLANLANDI` Ölçüm, kalibrasyon, retrieval ve model belirsizliği ayrımı.
- `[ ] PLANLANDI` Korelasyon ve kovaryans.
- `[ ] PLANLANDI` Yeniden örnekleme belirsizliği.
- `[ ] PLANLANDI` Birim dönüşüm ve datum dönüşüm belirsizliği.
- `[ ] PLANLANDI` Detection limit ve upper/lower bound türleri.
- `[ ] PLANLANDI` Veri ürünü güven seviyesi sözlüğü.

### 17.2 Kaynak çelişkileri

- `[x] YAPILDI` IUVS web sayfası/derived koleksiyon çelişkisi kaydı.
- `[x] YAPILDI` IUVS XML/FITS tür çelişkisi kaydı.
- `[x] YAPILDI` NGIMS XML alan/file-size tutarsızlıkları.
- `[x] YAPILDI` Belgelenmemiş NGIMS `-999`.
- `[x] YAPILDI` Belgelenmemiş MGS ER `-7777.7`.
- `[ ] PLANLANDI` Genel machine-readable anomaly ledger.
- `[ ] PLANLANDI` Kaynak düzeltmesi yayımlandığında kapanış/supersession alanı.
- `[ ] PLANLANDI` Çelişen bilimsel yorumların model ailesi olarak tutulması.

### 17.3 Çapraz doğrulama

- `[ ] PLANLANDI` MOLA ↔ HRSC/HiRISE DTM karşılaştırması.
- `[ ] PLANLANDI` TES ↔ THEMIS ↔ MCS sıcaklık/termal ürünleri.
- `[ ] PLANLANDI` REMS ↔ MCS ↔ GCM atmosfer karşılaştırması.
- `[ ] PLANLANDI` NGIMS ↔ IUVS ↔ occultation yoğunlukları.
- `[ ] PLANLANDI` MAG ↔ kabuksal alan modelleri.
- `[ ] PLANLANDI` Odyssey neutron ↔ SWIM ↔ radar buz göstergeleri.
- `[ ] PLANLANDI` RAD ↔ SEP ↔ transport model olayları.
- `[ ] PLANLANDI` Rover mineraloji ↔ CRISM/OMEGA.

### 17.4 Fiziksel tutarlılık testleri

- `[ ] PLANLANDI` Basınç/yoğunluk/sıcaklık boyut ve işaret kontrolleri.
- `[ ] PLANLANDI` Hidrostatik denge residual.
- `[ ] PLANLANDI` Atmosfer bileşimi toplamları.
- `[ ] PLANLANDI` Hız/alan koordinat dönüşüm norm koruması.
- `[ ] PLANLANDI` Yerçekimi potansiyel/ivme türev tutarlılığı.
- `[ ] PLANLANDI` Enerji dengesi kapanışı.
- `[ ] PLANLANDI` Kütle/element bütçesi.
- `[ ] PLANLANDI` Zamansal süreklilik ve ani sıçrama tespiti.

## 22. Faz 18 — Siyah ekran araştırma arayüzü

Kullanıcının istediği biçim gereği öncelik 3B görselleştirme değil, metinsel
ve sayısal araştırma arayüzüdür.

### 18.1 CLI

- `[ ] PLANLANDI` `mars source list/show/verify`.
- `[ ] PLANLANDI` `mars property list/show`.
- `[ ] PLANLANDI` `mars value get`.
- `[ ] PLANLANDI` `mars dataset inspect`.
- `[ ] PLANLANDI` `mars query --lat --lon --alt --time`.
- `[ ] PLANLANDI` `mars provenance <record_id>`.
- `[ ] PLANLANDI` `mars conflicts`.
- `[ ] PLANLANDI` `mars coverage`.
- `[ ] PLANLANDI` `mars validate`.
- `[ ] PLANLANDI` Siyah terminalde tablo/JSON/CSV çıktı seçenekleri.

### 18.2 Araştırma API'si

- `[ ] PLANLANDI` Salt-okunur Python API.
- `[ ] PLANLANDI` Kaynak, özellik, değer ve dataset sorguları.
- `[ ] PLANLANDI` Uzamsal/zamansal filtreler.
- `[ ] PLANLANDI` Unit-aware dönüşümler.
- `[ ] PLANLANDI` Ham kaynak locator ve checksum çıktısı.
- `[ ] PLANLANDI` Büyük veri için lazy/chunked erişim.
- `[ ] PLANLANDI` REST/Arrow Flight değerlendirmesi.

### 18.3 Bilimsel raporlar

- `[ ] PLANLANDI` Bir bölge için otomatik çevre dosyası.
- `[ ] PLANLANDI` Bir zaman aralığı için atmosfer/plazma özeti.
- `[ ] PLANLANDI` Kaynak ve belirsizlik tablosu.
- `[ ] PLANLANDI` Coverage/gap raporu.
- `[ ] PLANLANDI` Model-observation karşılaştırma raporu.
- `[ ] PLANLANDI` Tekrarlanabilir araştırma paketleri.

## 23. Faz 19 — Sürümleme ve yayın

- `[ ] PLANLANDI` Semantik veri sürümü.
- `[ ] PLANLANDI` Her release için immutable manifest.
- `[ ] PLANLANDI` Veri ekleme/değişiklik changelog'u.
- `[ ] PLANLANDI` DOI üretilebilen release arşivi.
- `[ ] PLANLANDI` Kaynakların lisans uyum raporu.
- `[ ] PLANLANDI` Bilimsel yöntem belgesi.
- `[ ] PLANLANDI` Veri sözlüğü ve kullanıcı kılavuzu.
- `[ ] PLANLANDI` Yeniden üretilebilir build tarifi.
- `[ ] PLANLANDI` Harici bilimsel inceleme.
- `[ ] PLANLANDI` Benchmark veri ve beklenen sonuç paketi.

## 24. Faz 20 — Kubbe şehir araştırmasına geçiş kapısı

Bu faz şimdilik kapsam dışıdır. Aşağıdaki doğal Mars katmanları yeterli
olmadan şehir veya yapı hesabı başlatılmayacaktır:

- `[ ] PLANLANDI` Aday konumlarda yüksek çözünürlüklü topoğrafya.
- `[ ] PLANLANDI` Zemin/regolit geoteknik özellikleri.
- `[ ] PLANLANDI` Yeraltı buzu ve erişilebilir su belirsizliği.
- `[ ] PLANLANDI` Yüzey ve yeraltı radyasyon alanı.
- `[ ] PLANLANDI` Basınç, sıcaklık, rüzgâr ve toz aşırı olayları.
- `[ ] PLANLANDI` Mevsimsel enerji ve güneşlenme koşulları.
- `[ ] PLANLANDI` Deprem, eğim, çökme ve darbe tehlikesi.
- `[ ] PLANLANDI` Gezegen koruma ve special-region kısıtları.
- `[ ] PLANLANDI` Tüm katmanlarda ortak koordinat/zaman ve belirsizlik.

Bu kapı açıldıktan sonra yaşam destek, yapı, enerji, lojistik ve 1.000 kişilik
nüfus sistemi ayrı bir proje fazı olarak tanımlanacaktır.

## 25. Öncelik sırası

### Yakın dönem — veri kapsamını büyüt

1. IUVS stellar-occultation koleksiyonları; disk/echelle/corona için
   katmanlı gerçek örnek setleri.
2. MAVEN STATIC, SWEA, SEP ve EUVM.
3. Tam MCS ve seçilmiş REMS/MEDA/InSight meteoroloji serileri.
4. Gerçek SWIM rasterleri ile SHARAD/MARSIS radar örnekleri.
5. THEMIS sıcaklık/termal atalet ve MARCI günlük atmosfer haritaları.
6. InSight SEIS/RISE iç yapı katmanı.
7. OMEGA/CRISM küresel mineral haritaları.

### Orta dönem — ortak Mars veri küpü

1. Zaman ve koordinat dönüşüm çekirdeği.
2. Çok çözünürlüklü küresel hücre sistemi.
3. Yüzey/atmosfer/yeraltı/yörünge indeksleri.
4. Birim, kalite ve belirsizlik standardizasyonu.
5. Terminal tabanlı sorgulama arayüzü.

### Uzun dönem — çalışan fiziksel ikiz

1. Atmosfer reanalysis ve veri özümseme.
2. Yüzey enerji dengesi ve yeraltı ısı/buz modelleri.
3. Plazma ve atmosferik kaçış modelleri.
4. Radyasyon transport modeli.
5. Model-observation residual ve sürekli kalibrasyon.
6. Bölgesel yüksek çözünürlüklü Mars çevre dosyaları.

## 26. İlerleme ölçümü

Tek bir dosyanın eklenmesiyle yüzde yükseltilmez. İlerleme dört ayrı eksende
ölçülür:

| Eksen | Ölçüm |
|---|---|
| Bilim alanı kapsamı | Yukarıdaki atomik iş paketlerinin tamamlanma oranı |
| Uzamsal kapsam | Nokta, bölge, küresel ve 3B/hacim kapsama oranı |
| Zamansal kapsam | Tek örnek, dönemsel örnek, tam görev, climatology ve reanalysis |
| Güvenilirlik | Kaynak, kalite, belirsizlik, çapraz doğrulama ve fizik testi |

Genel ilerleme bu dört eksenin ağırlıklı bileşimidir. Mevcut taban güçlü bir
provenans çekirdeğine sahip olsa da tam bilimsel dijital ikiz hedefinin yaklaşık
`%4–6` aralığındadır. Bu oran, yol haritasındaki işler tamamlandıkça otomatik
hesaplanan bir coverage raporuyla değiştirilecektir.

## 27. Değişmez araştırma ilkeleri

1. Kaynaksız değer eklenmez.
2. Tahmin, ölçüm gibi gösterilmez.
3. Model çıktısı gerçek gözlemle aynı tabloda statüsüz tutulmaz.
4. Eksik değer fiziksel sıfır kabul edilmez.
5. İyon kütle kanalı kaynaksız kimyasal türe çevrilmez.
6. Proxy doğrudan fiziksel miktar gibi sunulmaz.
7. Tek rover/yörünge örneği küresel Mars olarak genellenmez.
8. Aynı niceliğin çelişen kaynakları silinmez; bağlamıyla birlikte korunur.
9. Belirsizlik yoksa “sıfır belirsizlik” yazılmaz; `NOT_AVAILABLE` kullanılır.
10. Kaynak dosyası değiştirilmez; dönüşümler ayrı ve yeniden üretilebilir olur.
11. Her normalize değer özgün dosya, ürün ve alanına geri izlenebilir.
12. Mars'ın bilinmeyen yönleri açıkça `UNKNOWN` olarak temsil edilir.
