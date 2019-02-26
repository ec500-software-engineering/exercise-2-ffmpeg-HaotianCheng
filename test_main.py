import os
import subprocess
import json
from pathlib import Path
import main as run
from pytest import approx


currentDirectory = os.getcwd()


def ffprobe_sync(filein: currentDirectory) -> dict:
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	str(filein)], universal_newlines = True)
    return json.loads(meta)
    

# run.startThreeThreads()



def test_duration():
    fnin = 'InputVideos\\GoPro.mp4'
    fnout = 'OutputVideos\\GoPro_hd480_1M.mp4'

    orig_meta = ffprobe_sync(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])
    new_meta = ffprobe_sync(fnout)
    new_duration = float(new_meta['streams'][0]['duration'])

    print(orig_duration, "vs",new_duration)
    assert round(orig_duration,2) == approx(round(new_duration,2))
    print("the duration of the 2 are aproximately the same")

if __name__ == "__main__":
    run.startThreeThreads()
    test_duration()
