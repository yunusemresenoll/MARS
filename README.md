# MARS Data Foundation

MARS, Mars hakkında ölçülmüş, türetilmiş, modellenmiş ve bilinmeyen
özellikleri kaynaklarıyla birlikte saklayan bilimsel veri temelidir.
Hedef bir 3B Mars görüntüsü üretmek değil; Mars'ın fiziksel çevresini
konum, zaman, irtifa/derinlik, yöntem, kalite, belirsizlik ve kaynak
bilgisiyle sorgulanabilen bir dijital ikiz haline getirmektir.

## Ana belgeler

- [Aşırı kapsamlı araştırma yol haritası](ROADMAP.md)
- [Kaynak arşivi kuralları](resources/README.md)
- [Kaynak kataloğu](resources/catalog/sources.json)
- [Özellik kayıtları](data/registry/)
- [Normalize değerler](data/values/)
- [Kaynak ürün manifestleri](data/datasets/)
- [Doğrulama çekirdeği](src/mars_foundation/validation.py)

Roadmap'te her iş `YAPILDI`, `KISMEN YAPILDI`, `PLANLANDI` veya `BLOKE`
olarak işaretlenir. Bir alanın tek örnek ürünü bulunması, o alanın
tamamlandığı anlamına gelmez.

Şu anki doğrulanmış temel 29 kaynak, 482 özellik tanımı, 117 normalize
referans değer, 77 kaynak veri ürünü ve 179.613.936 özgün kaynak kaydı
içerir. `resources/archive` içindeki yerel kaynak kopyaları toplam
1.364.582.643 bayttır. Büyük ürünler
arasında Odyssey nötron haritaları, USGS SIM3292 küresel jeoloji
vektörleri, CRISM MICA tip spektrumları, MOLA küresel topografya
rasterleri, MRO120F yerçekimi harmonikleri, TES bolometrik albedo ve
gündüz/gece termal atalet rasterleri bulunur. MSL RAD için güncel ürün
dizini, teknik belgeler ve bir gerçek Curiosity yüzey-solu örneği;
REMS içinse Release 0041 dizini ve Sol 4709'a ait 34.258 satırlık
meteoroloji tablosu arşivlidir. MRO Mars Climate Sounder V6.2 için
17.032 ürünlük kümülatif dizin ve 105 basınç seviyeli 379 gerçek
atmosfer profilinden oluşan bir DDR örneği bulunur.
MAVEN MAG V2.38 için 7.688 ürünlük planetosentrik koleksiyon envanteri
ve 2025-12-01 gününe ait 86.401 kayıtlı, bir saniyeye alt örneklenmiş
gerçek kalibre manyetik alan zaman serisi de yereldir.
MGS MAG/ER içinse areoidin 185 km üzerinde 720×360 hücreli küresel
kabuksal alan büyüklüğü haritası, PDS etiketleri, yöntem açıklaması ve
haritanın dayandığı hakemli makale arşivlenmiştir.
MAVEN SWIA V2.16 araç-üstü survey moment koleksiyonunun 4.094 ürünlük
tam envanteri ve 2025-12-01 gününe ait 21.600 gerçek iyon moment seti
de CDF biçiminde yereldir. Yoğunluk, basınç tensörü, cihaz/MSO hız ve
sıcaklık bileşenleri ile kalite ve cihaz-durum alanları korunur.
MAVEN LPW Derived V7.2 altında LP-NT V6.2'nin 3.977 ve W-N V6.7'nin
1.089 ürünlük tam envanterleri de arşivlidir. Aynı günün gerçek CDF
örneklerinde 21.590 adet on-nicelikli IV-uyumu kaydı ve Langmuir
çizgisinin saptandığı 30 elektron yoğunluğu kaydı bulunur.
MAVEN NGIMS için Şubat 2026 PDS teslimindeki 33.583 L2 ve 27.606 L3
ürünlük tam envanterler de yereldir. Gerçek örnekler bir yörünge
geçişindeki 4.254 nötr ve 3.355 iyon bolluk kaydını; başka bir geçişte
362 yeniden örneklenmiş nötr yoğunluk ve altı türün ölçek-yüksekliği/
sıcaklık uyum kayıtlarını kapsar.
MAVEN IUVS V13.0 için 632.427 kalibre, 8.706 işlenmiş ve 6.505
türetilmiş limb ürününün tam PDS üyelik envanterleri arşivlidir. Gerçek
örnekler 33×7×512 elemanlı bir FUV kalibre spektral-radyans küpü ile
CO2, N2 ve O için 14 profil × 19 irtifa seviyeli bir L2 geri-kazanım
ürünüdür. Yoğunluk, sıcaklık, model radyansı, gözlem geometrisi ve
rastgele/sistematik belirsizlikler ayrı alanlar halinde korunur.
IUVS corona için ayrıca 18.887 üyelik calibrated V13 envanteri ile
496'şar üyelik processed/derived V7 envanterleri ve bir gerçek H/O L2
tarama ürünü yereldir. Örneğin outbound-above-limb, inbound-above-limb
ve inbound-below-limb bileşenleri sırasıyla 100, 100 ve 64 kayıt taşır.
Örnekteki H ve O model sonuçları `NaN` olduğundan sıcaklık, yoğunluk,
enerji veya kaçış değeri olarak normalize edilmemiştir.
IUVS echelle için 47.106 calibrated ve 46.662 processed ürünlük tam
envanterler ile gerçek bir V14 L1C outlimb ürünü de yereldir. Örnek
8×74×332 ana dizi, sekiz entegrasyon, H 1215,67 Å ve D 1215,34 Å
Lyman-alfa parlaklıkları, alt-sınır bir-sigma belirsizliği ve piksel
geometrisi içerir. Ürün doğrudan atmosferik D/H bolluk oranı vermediği
için H/D parlaklık oranından D/H değeri üretilmemiştir.
IUVS disk için 633.461 calibrated V13, 1.690 processed V7 ve 1.869
derived V7 ürünün tam envanterleri ile aynı apoapse taramasına ait gerçek
FUV/MUV L2 ürün çifti yereldir. FUV ürünü 11 emisyon özelliği, iki
parlaklık oranı ve `CO/CO2` ile `O/CO2` sütun oranlarını; MUV ürünü
180×90 hücreli O3 sütunu, yüzey-artı-bulut albedosu ve toz opaklığını
taşır. İncelenen ürün çiftinde doğrudan H2O alanı yoktur.

Bu aşamada proje:

- simülasyon yapmaz,
- şehir veya yapı hesabı yapmaz,
- 3B görüntü üretmez,
- kaynaksız sayısal değer kabul etmez.

## Dil

Ana uygulama dili Python 3.12+'dır. Bilimsel veri ekosistemi ve PDS,
NetCDF, raster ve tablo biçimleriyle entegrasyon için seçilmiştir.
İleride ölçülmüş bir performans ihtiyacı oluşursa sınırlı bileşenler Rust
ile yazılabilir.

## Değişmez kaynak kuralı

Her Mars değerinin en az bir `source_id` alanı olmalıdır. Bu kaynak,
`resources/catalog/sources.json` içinde kayıtlı ve mümkünse
`resources/archive/` altında özgün haliyle arşivlenmiş olmalıdır.

Bir değer ile kaynak arasında şu zincir korunur:

```text
Mars değeri
  -> source_id
  -> kaynak kataloğu
  -> yerel özgün dosya
  -> SHA-256 özeti
```

Ölçüm kapsamı da kaynak zincirinin parçasıdır. Örneğin Curiosity RAD
örneği Gale Krateri'ndeki araç konumuna bağlı bir zaman serisidir; küresel
Mars radyasyon haritası değildir. TES termal atalet ürünleri ise sıcaklık
gözlemlerinden modelle türetilmiştir; doğrudan sıcaklık rasteri değildir.
REMS MODRDR tablosu da rover konumundaki ölçümleri, düzeltmeleri ve bazı
model sonuçlarını birleştirir; her sensör alanı kendi güven koduyla
değerlendirilir ve `-999.00` eksik-veri kodu fiziksel değer sayılmaz.
MCS profilleri de ham radyans veya eşzamanlı küresel ızgara değildir;
sıcaklık, basınç ve aerosol alanları geri-kazanım sonuçlarıdır ve
değişkene özgü kalite bayraklarıyla kullanılmalıdır.
MAVEN MAG örneği ise uzay aracının değişen yörünge konumundaki alanı
ölçer; Mars yüzeyinin küresel kabuksal manyetik alan haritası veya
gezegenin sabit iç alanı olarak yorumlanamaz.
MGS ER haritası da doğrudan magnetometre vektörü değildir: elektron
reflektometrisiyle türetilmiş ve yaklaşık 200 km etkin çözünürlükte
yumuşatılmış B185 alan büyüklüğüdür. Küresel güvenilir algılama eşiği
4 nT'dir. Ham dosyadaki belgelenmemiş `-7777.7` kodu fiziksel değer
olarak kabul edilmez.
SWIA araç-üstü momentleri bütün iyonları proton varsayarak hesaplar.
Dağılımın görüş alanı ve enerji kapsamı kalite bayrağıyla denetlenir;
indüklenmiş manyetosfer sınırı içindeki key-parameter momentleri
genellikle nicel kullanılmaz. Alfa parçacığı yanlılığı nedeniyle SWIA
araç-üstü sıcaklık momentleri de nicel güneş rüzgârı sıcaklığı sayılmaz.
LPW LP-NT alanları da doğrudan ölçüm değildir: IV tarama uyumları,
ampirik düşük-yoğunluk kestirimi ve ürün birleştirme adımları içerir.
Düşük yoğunluk veya sıcak plazmada uyum başarısız olabilir. W-N yalnız
Langmuir çizgisi görüldüğünde üretilir; kalite ve belirsizlik alanları
çizginin tanımlanabilirliğini de yansıtır. Olay çalışmaları için
`flag > 50`, LP-NT istatistikleri için `flag > 46` kaynakta ayrı
önerilerdir; `NaN` fiziksel sıfır değildir.
NGIMS bollukları MAVEN yörünge izi üzerindedir; eşzamanlı küresel
atmosfer modeli değildir. İyon ürünü tür adı yerine kütle/yük kanalı
verdiği için kanallara kaynaksız kimyasal kimlik atanmaz. L3 sıcaklığı
doğrudan ölçüm değil, irtifa-log yoğunluk uyumu ve `H=mg/kT` ilişkisinden
türetilmiş sonuçtur. Ölçek-yüksekliği kalite kodu ve uyum hatasıyla
birlikte kullanılmalıdır. Nötr örnekteki belgelenmemiş `-999` değerleri
fiziksel sayım, yoğunluk veya hassasiyet kabul edilmez.
IUVS L1B spektral radyansı ham DN değildir; L2 yoğunluk ve sıcaklıkları
ise ileri model/hidrostatik geri-kazanım sonuçlarıdır. Ana IUVS web
sayfası “derived henüz arşivlenmedi” derken gerçek V13 limb derived
koleksiyonu 6.505 üyeye sahiptir; bu kaynak çelişkisi kayda geçirilmiştir.
2017 tarihli caveat belgesindeki FUV %25 ve MUV %30 mutlak kalibrasyon
belirsizlikleri yalnız v07 için bildirildiğinden v13'e otomatik
uygulanmaz. Aynı şekilde L2 XML açıklaması CO2/O2/O3 yazsa da gerçek
FITS tür tablosu CO2/N2/O içerir; fiziksel içerik FITS'ten alınır.
Corona örneğinde de XML tür açıklaması CO2/O2/O3 derken gerçek FITS
tablosu H/O içerir. Calibrated corona koleksiyonu V13 ve 2025 sonuna
kadar uzanırken processed/derived koleksiyonları V7 ve 2016'da biter;
bu ürünler aynı dönem kapsamına sahipmiş gibi birleştirilmez.
Echelle koleksiyon etiketleri V13.0 bildirirken processed envanterin
bütün üyeleri V14.0, calibrated envanterin üyeleri ise V3.0–V14.1
aralığındadır. Bu sürüm uyuşmazlığı korunur. Örnek üründeki negatif bir
D uyum parlaklığı da negatif bolluk veya D/H kabul edilmez.
Disk ürünlerinde `-1` ölçümsüz 2°×2° hücre dolgusu olarak FITS başlığında
belgelidir. Aynı maskede görülen fakat belgelenmeyen `-40` belirsizlik
sentineli fiziksel değer sayılmaz. V07 L2 disk geri-kazanımları
`SZA < 80°` ile sınırlıdır ve yüksek emisyon açılarında yüzey-kesişim
geometrisi artefaktları oluşabilir. FUV XML ve FITS stop zamanları
arasındaki uyuşmazlık da değiştirilmeden korunur.

## Bilimsel kapsam özeti

| Alan | Durum | Mevcut taban |
|---|---|---|
| Kaynak/provenans altyapısı | İleri | 29 kaynak, hash ve yapısal doğrulama |
| Gezegen sabitleri ve dönüş | Kısmi | NAIF PCK ve temel fiziksel/yörüngesel özellikler |
| Topografya ve yerçekimi | Kısmi | MOLA 16 ppd ve JGMRO-120F |
| Jeoloji ve mineraloji | Kısmi | USGS SIM3292 ve CRISM MICA |
| Su ve kriyosfer | Başlangıç | Odyssey nötron ürünleri ve SWIM kaynakları |
| Yüzey termofiziği | Kısmi | TES albedo ve termal atalet |
| Alt atmosfer/meteoroloji | Kısmi | REMS gerçek sol örneği ve MCS profil örneği |
| Üst atmosfer/iyonosfer | Kısmi | NGIMS, LPW ve IUVS limb/corona/echelle/disk |
| Plazma ve manyetik ortam | Kısmi | MAVEN MAG/SWIA ve MGS ER haritası |
| Radyasyon | Başlangıç | MSL RAD gerçek sol örneği |
| İç yapı ve sismoloji | Planlandı | InSight katmanı henüz eklenmedi |
| Astrobiyoloji | Planlandı | Organik/yaşanabilirlik katmanları henüz eklenmedi |
| Ortak uzay-zaman veri küpü | Planlandı | Kaynak katmanları henüz tek küpte birleşmedi |
| Fiziksel modeller ve veri özümseme | Planlandı | Model katmanı başlatılmadı |

Tam bilimsel dijital ikiz hedefindeki güncel tahmin yaklaşık `%4–6`'dır.
Kesin ilerleme daha sonra roadmap iş paketleri, uzamsal kapsam, zamansal
kapsam ve bilimsel güvenilirlik üzerinden otomatik hesaplanacaktır.

Kaynak yerel olarak kopyalanamıyorsa sebebi ve lisans/erişim durumu
katalogda açıkça belirtilir. Böyle kayıtlar `archived: false` taşır.

## Dizinler

```text
resources/
  archive/       Özgün belgeler ve veri ürünleri
  catalog/       Kaynak kayıtları
  schemas/       Makinece doğrulanabilir veri sözleşmeleri
src/mars_foundation/
  validation.py  Kaynak ve veri doğrulama kuralları
tests/
```

## İlk doğrulama

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m mars_foundation.validation
```

Beklenen güncel doğrulama özeti:

```text
MARS doğrulaması başarılı:
29 kaynak
482 özellik
117 değer
77 kaynak veri ürünü
179613936 kaynak kaydı
```

## Sıradaki uygulama sırası

1. IUVS stellar-occultation ürünleri; disk/echelle/corona için dönem ve
   geometri bakımından katmanlı gerçek örnek setleri.
2. MAVEN STATIC, SWEA, SEP ve EUVM plazma/uzay-havası katmanları.
3. Tam MCS ve seçilmiş REMS, MEDA ve InSight meteoroloji serileri.
4. Gerçek SWIM rasterleri ile SHARAD/MARSIS yeraltı radar ürünleri.
5. THEMIS, MARCI, OMEGA ve küresel CRISM ürünleri.
6. InSight sismoloji ve iç yapı katmanı.
7. Ortak Mars koordinat-zaman dönüşüm çekirdeği.

Ayrıntılı bağımlılıklar ve tamamlanma kriterleri [ROADMAP.md](ROADMAP.md)
dosyasındadır.
