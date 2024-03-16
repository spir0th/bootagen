# Bootagen
**This is the repository of Bootagen, currently in version 2.**

### Table of Contents
- [Overview](#overview)
- [Structure](#structure)
- [Getting Started](#getting-started)
    - [Using scripts](#using-scripts)
    - [Doing it step-by-step](#doing-it-step-by-step)
- [Installing Module(s)](#installing-modules)
- [Contribute your own animation](#contribute-your-own-animation)
- [Issues & Troubleshooting](#issues--troubleshooting)

### Overview
This project serves as a collection to replace the boot and shutdown animations. It was originally targeted specifically for my phone (TECNO CK7n) but I decided to make it support other devices afterwards.

> Installing boot and shutdown animations needs your device to be rooted because it replaces `bootanimation.zip` located in `/system/product/media`

> Beware that rooting your device causes it's warranty to void and may actually brick. **USE IT AT YOUR OWN RISK!**

> More information about rooting Android devices can be found [here.](https://www.androidauthority.com/root-android-277350)

### Structure
- `animations`
    - This is where animations reside, you can add your own animations here. See [Contribute your own animation](#contribute-your-own-animation) for more.
- `skeletons`
    - Module skeletons, they're used by `make_module.py` in order to install them on your device.

### Getting Started
#### Using scripts
> When using scripts, you must have Python 3 installed in order to execute them.

1. `python create_animation.py [boot|shutdown] <ANIMATION_ID>`
2. `python make_module.py <bootanimation.zip|shutdownanimation.zip> [ID] [NAME] [VER] [DESC]`

Examples:
```bash
$ python create_animation.py tecno.ck7n.boot.hios
$ python make_module.py bootanimation.zip "tecno.ck7n.boot.hios" "Tecno CK7n HiOS boot" "v1.0" "Created using Bootagen"
```
```bash
$ python create_animation.py shutdown tecno.ck7n.shutdown.hios
$ python make_module.py shutdownanimation.zip "tecno.ck7n.shutdown.hios" "Tecno CK7n HiOS shutdown" "v1.0" "Created using Bootagen"
```

#### Doing it step-by-step
> Before doing these steps, make sure 7zip (or a ZIP-archiver program) is installed to ensure about zipping an animation and it's corresponding module(s).

##### For creating a zipped animation:
- It should be specifically named `bootanimation.zip` (or `shutdownanimation.zip`)
- It's compression level / method must be set to 0 or "Store"

##### For making the module:
- The zipped animation must be placed inside the chosen module's `system/product/media` folder.
- For recommendation, use a temporary folder when zipping your chosen module.
- The module can be zipped, at any compression level.

### Installing Module(s)
Just simply use KernelSU or Magisk to install your animation modules.

### Contribute your own animation
You can add your animations for a specific device (or universal)
into this project, by forking it then creating a pull request.

When adding, your animation should recommend using this name convention:
> `[UNIVERSAL][BRAND].[MODEL].{BOOT|SHUTDOWN}.{CUSTOM}`

- `BRAND`, `MODEL` and `BOOT|SHUTDOWN` fields are required, if animation is device-specific or non-universal
- `BRAND` and `MODEL` fields should be empty, IF the animation is marked as universal
- `UNIVERSAL` should be used, if the animation is marked as universal
- `CUSTOM` field can be optional, it is used to describe the animation
- Everything after the `CUSTOM` field should be followed by dots, hypens, or underlines instead of spaces.

However, it's acceptable if you use different combinations with the required fields used.

An example of naming your animation according to the convention:
- tecno.ck7n.boot.simple_hios
- tecno.ck7n.shutdown.hios
- universal.boot.flower

### Issues & Troubleshooting
*Q. My phone doesn't show any boot animation!*
> Make sure bootanimation.zip's compression level is set to 0.

*Q. Cannot find bootanimation.zip (or shutdownanimation.zip) when using compress_module*
> Before even compressing the module, make sure a boot animation is created in place.

To report issues, visit [the repository](https://github.com/spir0th/bootagen) to make an issue.