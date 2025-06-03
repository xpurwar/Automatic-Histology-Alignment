from allensdk.core.reference_space_cache import ReferenceSpaceCache
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

output_dir = '.'

reference_space_key = os.path.join('annotation', 'ccf_2017')
resolution = 25
rspc = ReferenceSpaceCache(resolution, reference_space_key, manifest=Path(output_dir) / 'manifest.json')
rsp = rspc.get_reference_space()


fig, ax = plt.subplots(figsize=(10, 10))
plt.imshow(rsp.get_slice_image(1, 5000), interpolation='none')
fig.savefig('slice_1_5000.png', dpi=300, bbox_inches='tight')
