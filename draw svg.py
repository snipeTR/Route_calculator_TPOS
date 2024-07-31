import pandas as pd
import xml.etree.ElementTree as ET

# CSV dosyasının yolunu belirleyin
file_path = 'ilmesafe.csv'

# CSV dosyasını yükleyin
data = pd.read_csv(file_path, encoding='iso-8859-9')

# Rota dosyasının yolunu belirleyin
rota_file_path = 'rota.txt'

# SVG dosyasının yolunu belirleyin
svg_file_path = 'Türkiye.svg'
output_svg_file_path = 'Türkiye_rota.svg'

# Rota dosyasını oku
with open(rota_file_path, 'r', encoding='utf-8') as f:
    rota_sehirler = f.read().strip().split(',')

# SVG dosyasını yükleyin
tree = ET.parse(svg_file_path)
root = tree.getroot()

# Namespace ile ilgili olası sorunları çözmek için
ns = {'svg': 'http://www.w3.org/2000/svg'}
ET.register_namespace('', 'http://www.w3.org/2000/svg')

# Şehir isimlerinin ortasına denk gelecek koordinatları bul
city_coords = {}
for elem in root.findall('.//svg:text', ns):
    if elem.text:
        city_name = elem.text.strip().upper()
        if city_name in rota_sehirler:
            bbox = elem.attrib.get('transform', '').replace('matrix(', '').replace(')', '').split()
            if len(bbox) == 6:
                x = float(bbox[4])
                y = float(bbox[5])
                text_length = len(city_name)
                if text_length >= 3:
                    x += (text_length // 2 - 1) * 6  # Her karakter için 6 birim sağa kaydırma
                city_coords[city_name] = (x, y)

# Şehirler arası çizgileri çizme
for i in range(len(rota_sehirler) - 1):
    start_city = rota_sehirler[i]
    end_city = rota_sehirler[i + 1]

    if start_city in city_coords and end_city in city_coords:
        start_x, start_y = city_coords[start_city]
        end_x, end_y = city_coords[end_city]

        line = ET.Element('line', {
            'x1': str(start_x),
            'y1': str(start_y),
            'x2': str(end_x),
            'y2': str(end_y),
            'stroke': 'green' if i == 0 else 'blue',
            'stroke-width': '2'
        })
        root.append(line)

# Son şehirden ilk şehire kırmızı çizgi ekleme
start_city = rota_sehirler[-1]
end_city = rota_sehirler[0]
if start_city in city_coords and end_city in city_coords:
    start_x, start_y = city_coords[start_city]
    end_x, end_y = city_coords[end_city]

    line = ET.Element('line', {
        'x1': str(start_x),
        'y1': str(start_y),
        'x2': str(end_x),
        'y2': str(end_y),
        'stroke': 'red',
        'stroke-width': '2'
    })
    root.append(line)

# Güncellenmiş SVG dosyasını kaydet
tree.write(output_svg_file_path, encoding='utf-8', xml_declaration=True)

print(f"Güncellenmiş SVG dosyası kaydedildi: {output_svg_file_path}")
