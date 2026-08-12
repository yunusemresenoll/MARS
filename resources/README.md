# Resources

Bu klasör MARS veri temelinde kullanılan bütün kaynakların yerel arşividir.

Güncel katalog 29 kaynak altında 1.364.582.643 baytlık kaynak dosyası
tanımlar. Katalogdaki her dosya açılışta boyut ve SHA-256 özetiyle
doğrulanır.

## Kaynak ekleme protokolü

1. Kaynak için kalıcı bir `source_id` oluştur.
2. Kaynağın özgün dosyasını `archive/<source_id>/` altına koy.
3. Dosyanın SHA-256 özetini hesapla.
4. Kaydı `catalog/sources.json` dosyasına ekle.
5. Kaynağa dayanan her veri kaydında aynı `source_id` değerini kullan.
6. Kaynağın hangi tablo, sayfa, şekil, alan veya ürün kaydının kullanıldığını
   `source_locator` alanında belirt.

## Değişmezlik

`archive/` altındaki özgün dosyalar düzenlenmez. Yeni sürüm ayrı bir
`source_id` ile eklenir. Dönüştürülmüş veri özgün kaynak dosyasının üzerine
yazılmaz.

## Arşivlenemeyen kaynak

Lisans, boyut veya erişim kontrolü yüzünden kaynak yerel olarak
saklanamıyorsa katalog kaydı şu alanları taşımalıdır:

```json
{
  "archived": false,
  "archive_exception": "Açık ve somut gerekçe",
  "url": "Kalıcı bağlantı",
  "doi": "Varsa DOI",
  "license": "Bilinen kullanım koşulu"
}
```

Arşivlenemeyen kaynak hiçbir zaman arşivlenmiş gibi gösterilmez.

Kısmi arşivler de açıkça belirtilir. Örneğin MSL RAD kaynağında güncel
tam dizin ve belgeler bulunmasına karşın yalnızca bir gerçek yüzey-solu
veri dosyası yereldir; bu sınır hem kaynak kataloğunda hem veri ürünü
manifestinde kayıtlıdır.
