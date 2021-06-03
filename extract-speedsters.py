import numpy as np
import pandas as pd
from scipy import stats
import zipfile
from os.path import basename

csv = pd.read_csv("speed-cam.csv", header=None, names=['timestamp', 'speed', 'speed_unit', 'media_path', 'x', 'y', 'width', 'height', 'area', 'direction', 'blank'])
csv.timestamp = pd.to_datetime(csv.timestamp)
print(csv)
speedsters = csv[(csv.speed > 30) & (~csv.media_path.str.contains("calib"))]
print(speedsters)

zf = zipfile.ZipFile('speedsters.zip', "w", zipfile.ZIP_DEFLATED)

print('generating archive')
for speedster in speedsters.itertuples():
    zf.write(speedster.media_path, str(speedster.speed) +  basename(speedster.media_path))
zf.close()
print('created speedsters.zip')
