###
# bootanimation.zip / shutdownanimation.zip generator
#
# This script is part of the Bootagen project.
# Visit https://github.com/spir0th/bootagen for more info.
#
# Usage:
#   create_animation.py [boot|shutdown] <ANIMATION>
#
###
import os
import sys
import zipfile

_script_dir = os.path.dirname(os.path.realpath(__file__))

animation_dir = os.path.join(_script_dir, "animations")
animation_path = None
animation = None

type = "boot"

def parse_cmdline_args():
    global type, animation
    args = sys.argv[1:]
    
    if len(args) < 1:
        return
    if len(args) > 1:
        type = args[0].lower()
        animation = args[1]
    else:
        animation = args[0]

def check_animation_type():
    global type
    
    if type != "boot" and type != "shutdown":
        types = ["boot", "shutdown"]
        raise TypeError(f"\"{type}\" is not an animation type, use the following values: {types}")

def find_animation():
    global animation_dir, animation_path, animation, type
    path = os.path.join(animation_dir, animation)
    
    if not os.path.isdir(animation_dir):
        raise FileNotFoundError("Uncompressed animation files are missing!")
    if os.path.isdir(path):
        print(f"Found: {path}")
        animation_path = path
    else:
        raise FileNotFoundError(f"There is no such {type} animation named \"{animation}\"")

def zip_animation():
    global animation_path, type
    output = f"{type}animation.zip"
    print(f"Creating: {output}")
    
    if zipfile.is_zipfile(output):
        cancel_response = input(f"{output} already exists, remove? (Y/n) ").lower()
        
        if cancel_response == "y" or cancel_response == "yes":
            os.remove(output)
        else:
            raise FileExistsError(f"Cannot create {output} because it already exists!")
    
    zip = zipfile.ZipFile(output, "w", zipfile.ZIP_STORED)
    
    if animation_path is None:
        raise NotImplementedError("An unexpected path check has failed to pass, make sure the animation is named properly")
    for root, dirs, files in os.walk(animation_path):
        for file in files:
            filename = os.path.join(root, file)
            arcname = os.path.relpath(os.path.join(root, file), animation_path)
            # print(f"Writing: {file}", end="\r")
            print(f"Writing: {file}")
            zip.write(filename, arcname)
    
    print(str())
    print("Done!")
    zip.close()

sys.tracebacklimit = 0
parse_cmdline_args()
check_animation_type()
find_animation()
zip_animation()