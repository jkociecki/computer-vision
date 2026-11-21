"""Rysowanie maski zębów kliknięciami.

Uruchom:  python rysuj_maske.py roboflow-caries-117.jpg
Sterowanie:
  lewy klik  - dodaj punkt konturu
  Enter/spacja - zamknij wielokąt (ząb dodany do maski)
  z          - cofnij ostatni punkt
  u          - usuń ostatni zamknięty wielokąt
  s          - zapisz caries_mask.png i zakończ
  Esc        - wyjdź bez zapisu
"""
import sys
import cv2
import numpy as np

path = sys.argv[1] if len(sys.argv) > 1 else 'roboflow-caries-117.jpg'
img = cv2.imread(path)
if img is None:
    sys.exit(f'Nie mogę wczytać {path}')
h, w = img.shape[:2]
scale = min(1.0, 1400 / w, 900 / h)  # dopasowanie do ekranu
polys, cur = [], []


def redraw():
    mask = np.zeros((h, w), np.uint8)
    for p in polys:
        cv2.fillPoly(mask, [np.array(p, np.int32)], 255)
    view = img.copy()
    view[mask > 0] = (0.55 * view[mask > 0] + 0.45 * np.array([0, 200, 0])).astype(np.uint8)
    for p in polys:
        cv2.polylines(view, [np.array(p, np.int32)], True, (0, 255, 0), 1)
    if cur:
        cv2.polylines(view, [np.array(cur, np.int32)], False, (0, 0, 255), 1)
        for x, y in cur:
            cv2.circle(view, (x, y), 2, (0, 0, 255), -1)
    cv2.imshow('maska', cv2.resize(view, None, fx=scale, fy=scale))
    return mask


def on_mouse(event, x, y, *_):
    if event == cv2.EVENT_LBUTTONDOWN:
        cur.append((int(x / scale), int(y / scale)))
        redraw()


cv2.namedWindow('maska')
cv2.setMouseCallback('maska', on_mouse)
redraw()
while True:
    k = cv2.waitKey(20) & 0xFF
    if k in (13, 32) and len(cur) >= 3:
        polys.append(cur[:]); cur.clear(); redraw()
    elif k == ord('z') and cur:
        cur.pop(); redraw()
    elif k == ord('u') and polys:
        polys.pop(); redraw()
    elif k == ord('s'):
        cv2.imwrite('caries_mask.png', redraw())
        print(f'Zapisano caries_mask.png ({len(polys)} zębów, {w}x{h})')
        break
    elif k == 27:
        break
cv2.destroyAllWindows()