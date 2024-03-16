###
# Magisk / KernelSU module generator for boot and shutdown animation
#
# This script is part of the Bootagen project.
# Visit https://github.com/spir0th/bootagen for more info.
#
# Usage:
#   make_module.py <bootanimation.zip|shutdownanimation.zip> [MODULE_ID] [MODULE_NAME] [MODULE_VER] [MODULE_DESC]
#
###
import os
import sys
import shutil
import zipfile

_script_dir = os.path.dirname(os.path.realpath(__file__))
_temp_dir = os.path.join(_script_dir, "._temp")

module_id = "bootagen.my-custom-animation"
module_name = "My Custom Animation"
module_description = "Created from Bootagen"
module_version = "v1.0"

animation_zip = None
output_zip = None

def parse_cmdline_args():
    global module_id, module_name, module_description, module_version, animation_zip, output_zip
    args = sys.argv[1:]
    
    if len(args) > 0:
        animation_zip = args[0]
    else:
        raise RuntimeError("A bootanimation / shutdownanimation must be passed through the command-line")
    if len(args) > 1:
        module_id = args[1]
    else:
        print(f"Warning: No module ID specified, defaulting to {module_id}")
        print("Warning: Module ID should be specified at all times, leaving it to default may cause conflict with other animation modules created by Bootagen.")
    if len(args) > 2:
        module_name = args[2]
    else:
        print(f"Warning: No module name specified, defaulting to {module_name}")
    if len(args) > 3:
        module_description = args[3]
    else:
        print(f"Warning: No module description specified, defaulting to {module_description}")
    if len(args) > 4:
        module_version = args[4]
    else:
        print(f"Warning: No module version specified, defaulting to {module_version}")

def validate_animation():
    global animation_zip
    
    if animation_zip.endswith("bootanimation.zip") and animation_zip.endswith("shutdownanimation.zip"):
        animations = ["bootanimation.zip", "shutdownanimation.zip"]
        raise RuntimeError(f"\"{animation_zip}\" is not equivalent to one or more values: {animations}")

def copy_files():
    global _temp_dir, animation_zip
    module = None

    if not zipfile.is_zipfile(animation_zip):
        raise FileNotFoundError(f"\"{animation_zip}\" is not a valid ZIP file.")
    if animation_zip.endswith("bootanimation.zip"):
        module = os.path.join(_script_dir, os.path.join("skeletons", "bootanimation"))
    elif animation_zip.endswith("shutdownanimation.zip"):
        module = os.path.join(_script_dir, os.path.join("skeletons", "shutdownanimation"))
    else:
        raise RuntimeError(f"\"{animation_zip}\" is not bootanimation.zip or shutdownanimation.zip")
    
    print(f"Copy: Module files to temp directory")
    shutil.copytree(module, _temp_dir, dirs_exist_ok=True)
    
    # move bootanimation.zip / shutdownanimation.zip to temp dir aswell
    media_dir = os.path.join(_temp_dir, os.path.join("system", os.path.join("product", "media")))
    print(f"Copy: {animation_zip} to temp directory")
    os.makedirs(media_dir, exist_ok=True)
    shutil.copy2(animation_zip, media_dir)

def modify_properties():
    global _temp_dir, module_id, module_name, module_description, module_version
    print("Write: Configuring module.prop")
    
    if not os.path.isfile(os.path.join(_temp_dir, "module.prop")):
        raise FileNotFoundError("Cannot locate module.prop for skeleton")
    with open(os.path.join(_temp_dir, "module.prop"), "r+") as module_prop:
        contents = module_prop.read()
        contents = contents.replace("<MODULE_ID>", module_id)
        contents = contents.replace("<MODULE_NAME>", module_name)
        contents = contents.replace("<MODULE_VER>", module_version)
        contents = contents.replace("<MODULE_DESC>", module_description)
        module_prop.seek(0)
        module_prop.write(contents)
        module_prop.truncate()
    
def compress_module():
    global _temp_dir, output_zip
    output_zip = f"{module_id}.zip"
    print(f"Creating: {output_zip}")
    
    if zipfile.is_zipfile(output_zip):
        cancel_response = input(f"{output_zip} already exists, remove? (Y/n) ").lower()
        
        if cancel_response == "y" or cancel_response == "yes":
            os.remove(output_zip)
        else:
            raise FileExistsError(f"Cannot create {output_zip} because it already exists!")
    
    zip = zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED)
    
    for root, _, files in os.walk(_temp_dir):
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
modify_properties()
compress_module()
cleanup()