###
# Magisk / KernelSU module generator for boot and shutdown animation
#
# This script is part of the Bootagen project.
# Visit https://github.com/spir0th/bootagen for more info.
#
# Usage:
#   make_module.py <bootanimation.zip|shutdownanimation.zip> [MODULENAME]
#
###
import os
import pathlib
import sys
import shutil
import zipfile

_script_dir = os.path.dirname(os.path.realpath(__file__))
_temp_dir = os.path.join(_script_dir, "._temp")

animation_zip = None
output_zip = None

def parse_cmdline_args():
    global animation_zip, output_zip
    args = sys.argv[1:]
    
    if len(args) > 0:
        animation_zip = args[0]
    else:
        raise RuntimeError("A bootanimation / shutdownanimation must be passed through the command-line")
    if len(args) > 1:
        output_zip = args[1]

def validate_animation():
    global animation_zip
    
    if animation_zip.endswith("bootanimation.zip") and animation_zip.endswith("shutdownanimation.zip"):
        animations = ["bootanimation.zip", "shutdownanimation.zip"]
        raise RuntimeError(f"\"{animation_zip}\" is not equivalent to one or more values: {animations}")

def copy_files():
    global _temp_dir, animation_zip, output_zip
    module = None
    
    if not zipfile.is_zipfile(animation_zip):
        raise FileNotFoundError(f"\"{animation_zip}\" is not a valid ZIP file.")
    if animation_zip.endswith("bootanimation.zip"):
        module = os.path.join(_script_dir, os.path.join("module_skeletons", "bootanimation"))
    elif animation_zip.endswith("shutdownanimation.zip"):
        module = os.path.join(_script_dir, os.path.join("module_skeletons", "shutdownanimation"))
    else:
        raise RuntimeError(f"\"{animation_zip}\" is not bootanimation.zip or shutdownanimation.zip")
    
    print(f"Copy: Module files to temp directory")
    shutil.copytree(module, _temp_dir, dirs_exist_ok=True)
    
    # move bootanimation.zip / shutdownanimation.zip to temp dir aswell
    print(f"Copy: {animation_zip} to temp directory")
    shutil.copy2(animation_zip, os.path.join(_temp_dir, os.path.join("system", os.path.join("product", "media"))))

def compress_module():
    global _temp_dir, animation_zip, output_zip
    
    if output_zip is None:
        if animation_zip.endswith("bootanimation.zip"):
            output_zip = "BootAnimationModule.zip"
        elif animation_zip.endswith("shutdownanimation.zip"):
            output_zip = "ShutdownAnimationModule.zip"
    else:
        if not output_zip.endswith(".zip"):
            output_zip += ".zip"
    
    print(f"Creating: {output_zip}")
    
    if zipfile.is_zipfile(output_zip):
        cancel_response = input(f"{output_zip} already exists, remove? (Y/n) ").lower()
        
        if cancel_response == "y" or cancel_response == "yes":
            os.remove(output_zip)
        else:
            raise FileExistsError(f"Cannot create {output_zip} because it already exists!")
    
    zip = zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(_temp_dir):
        for file in files:
            filename = os.path.join(root, file)
            arcname = os.path.relpath(os.path.join(root, file), _temp_dir)
            # print(f"Writing: {file}", end="\r")
            print(f"Writing: {file}")
            zip.write(filename, arcname)
    
    print(str())
    print("Done!")
    zip.close()

def cleanup():
    global _temp_dir
    
    if os.path.isdir(_temp_dir):
        shutil.rmtree(_temp_dir)

sys.tracebacklimit = 0
parse_cmdline_args()
validate_animation()
copy_files()
compress_module()
cleanup()