"""Download licensed Pexels source photographs and create reproducible WebP crops.

Run with a Python interpreter providing Pillow. Provenance: docs/ASSETS.md.
"""
from pathlib import Path
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
import json
import sys
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ORIGINALS = ROOT / 'site/assets/originals'
PHOTOS = ROOT / 'site/assets/photos'
IDS = [6195281, 6197122, 37440103, 4440538, 4440536, 1571460, 380768, 6197123]
# Logical slot, original Pexels ID, aspect ratio, crop gravity.
SLOTS = [
    ('hero', 37440103, (16, 9), (0.5, 0.42)),
    ('hero-mobile', 37440103, (1, 1), (0.5, 0.35)),
    ('about-01', 6195281, (3, 4), (0.5, 0.5)),
    ('about-02', 4440538, (4, 3), (0.5, 0.38)),
    ('about-03', 6197123, (4, 3), (0.5, 0.5)),
    ('service-01', 1571460, (4, 3), (0.4, 0.5)),
    ('service-02', 380768, (4, 3), (0.5, 0.5)),
    ('service-03', 37440103, (4, 3), (0.6, 0.5)),
    ('service-04', 4440536, (4, 3), (0.5, 0.5)),
    ('gallery-01', 37440103, (3, 4), (0.5, 0.5)),
    ('gallery-02', 4440538, (1, 1), (0.5, 0.4)),
    ('gallery-03', 1571460, (1, 1), (0.3, 0.5)),
    ('gallery-04', 6197122, (16, 9), (0.5, 0.08)),
    ('gallery-05', 6195281, (1, 1), (0.5, 0.35)),
    ('gallery-06', 4440536, (1, 1), (0.5, 0.5)),
    ('process', 6197123, (16, 9), (0.5, 0.5)),
    ('why', 6197122, (4, 3), (0.5, 0.4)),
    ('article-01', 4440538, (3, 2), (0.5, 0.4)),
    ('article-02', 380768, (3, 2), (0.5, 0.5)),
    ('article-03', 4440536, (3, 2), (0.5, 0.5)),
]

def download(photo_id):
    target = ORIGINALS / f'{photo_id}.jpg'
    if not target.exists():
        url = f'https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=2400'
        target.write_bytes(urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read())
    with Image.open(target) as image:
        print(photo_id, image.size)

def contact_sheet():
    files = [ORIGINALS / f'{photo_id}.jpg' for photo_id in IDS]
    sheet = Image.new('RGB', (1200, ((len(files)+3)//4)*340), 'white')
    draw = ImageDraw.Draw(sheet)
    for index, file in enumerate(files):
        image = ImageOps.contain(Image.open(file).convert('RGB'), (290, 300))
        x, y = (index % 4)*300, (index//4)*340
        sheet.paste(image, (x, y+24))
        draw.text((x+8, y+5), file.stem, fill='black')
    sheet.save(PHOTOS / 'contact-sheet.jpg', quality=85)

def derivatives():
    manifest = []
    for name, photo_id, ratio, gravity in SLOTS:
        image = ImageOps.exif_transpose(Image.open(ORIGINALS / f'{photo_id}.jpg')).convert('RGB')
        for width in (640, 1280, 1920):
            size = (width, round(width * ratio[1] / ratio[0]))
            if '--hero-only' not in sys.argv or name in ('hero', 'hero-mobile'):
                crop = ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=gravity)
                crop.save(PHOTOS / f'{name}-{width}.webp', 'WEBP', quality=82, method=6)
            manifest.append({'file': f'{name}-{width}.webp', 'width': size[0], 'height': size[1], 'sourceId': photo_id, 'cropGravity': list(gravity), 'illustrative': True})
        print(name, 'ready')
    (PHOTOS / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

def prune_rejected_candidates():
    # Only named downloads from this research session; no recursive operation.
    rejected = [4440540,9462107,6195121,6195277,6195288,4440537,4008518,28576625,28576621,6197124,6197125,6197126,6197127,6197128,6195956,16898981,16898979,16898978,17041924,10092356,34517611]
    safe_root = ORIGINALS.resolve()
    for photo_id in rejected:
        target = (ORIGINALS / f'{photo_id}.jpg').resolve()
        assert target.parent == safe_root and photo_id not in IDS
        target.unlink(missing_ok=True)

def validate():
    manifest = json.loads((PHOTOS / 'manifest.json').read_text(encoding='utf-8'))
    assert len(manifest) == 60
    for asset in manifest:
        with Image.open(PHOTOS / asset['file']) as image:
            assert image.format == 'WEBP'
            assert image.size == (asset['width'], asset['height'])
            image.verify()
    gallery_sources = [photo_id for slot, photo_id, _, _ in SLOTS if slot.startswith('gallery-')]
    assert len(gallery_sources) == len(set(gallery_sources)) == 6
    print(f'Validated {len(manifest)} WebP files; six distinct gallery masters.')

if __name__ == '__main__':
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    PHOTOS.mkdir(parents=True, exist_ok=True)
    if '--clean-candidates' in sys.argv:
        prune_rejected_candidates()
    if '--validate-only' in sys.argv:
        validate()
        raise SystemExit(0)
    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(download, IDS))
    contact_sheet()
    derivatives()
    validate()
