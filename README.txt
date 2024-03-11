Bootagen version 1.5
-------------------------------------------------
				CONTENTS

			1: Information / Notes
			2: Project Structure
			3: Using Bootagen
				3.2: Automation scripts
				3.3: Manual instructions
			4: Installing the module(s)
			5: Contribute your own animation
			6: Issues & Troubleshooting

-------------------------------------------------
			INFORMATION / NOTES

This project serves as a collection to replace
the boot and shutdown animations. It was originally
aimed at a specific phone (TECNO CK7n) but I decided
to make it universal afterwards.

Note that installing one of these boot animations
requires your device to be rooted because it has to modify
the bootanimation.zip located in /system/product/media

Beware that rooting your device causes it's warranty to
void and may actually brick. USE IT AT YOUR OWN RISK!

For more information about rooting:
https://www.androidauthority.com/root-android-277350/
-------------------------------------------------
			PROJECT STRUCTURE

- root directory
	- animations: A directory where animations reside, put your own animation here with the boot-*/shutdown-* prefix.
		- boot-simplified: A simple fade-in boot animation displaying a TECNO logo.
		- boot-stock: The official stock boot animation.
		- shutdown-simplified: A simple fade-out boot animation displaying a TECNO logo.
		- shutdown-stock: The official stock shutdown animation.
	- modules: All the module(s) are put here. Use them with the zipped bootanimation.zip
		- bootanimation: The module for bootanimation.zip, used for boot animations.
		- shutdownanimation: The module for shutdownanimation.zip, used for shutdown animations.
	- README.txt: This file
	- CHANGELOG.txt: A list of changelogs
-------------------------------------------------
			USING BOOTAGEN

You can achieve two ways of creating animations and modules in Bootagen:
	- AUTOMATION SCRIPTS
	- MANUAL INSTRUCTIONS

*** AUTOMATION SCRIPTS
When using automation scripts, Python 3 must be installed in order to run them.

To create a zipped boot/shutdown animation:
	$ python create_animation.py [boot|shutdown] YOURSELECTEDANIMATIONHERE
Then, to make a module:
	$ python make_module.py bootanimation.zip

An example of zipping a module with a zipped boot/shutdown animation inside:
	$ python create_animation.py simplified
	$ python make_module.py bootanimation.zip MySimplifiedAnimation

*** MANUAL INSTRUCTIONS
Before doing these steps, make sure 7zip (or a ZIP-archiver program) is
installed to ensure about zipping an animation and it's corresponding module(s).

For creating a zipped animation:
	- It should be specifically named "bootanimation.zip" (or shutdownanimation.zip)
	- It's compression level / method must be set to 0 or "Store"

For making the module:
	- The zipped animation must be placed inside the chosen module's system/product/media folder.
	- For recommendation, use a temporary folder when zipping your chosen module.
	- The module can be zipped, at any compression level.

-------------------------------------------------
			INSTALLING THE MODULE(S)

Just simply use KernelSU or Magisk to install them.
-------------------------------------------------
			CONTRIBUTE YOUR OWN ANIMATION

You can add your animations for a specific device (or universal)
into this project, by forking it then creating a pull request.

When adding, your animation should recommend using this name convention:
	[UNIVERSAL][BRAND]_[MODEL]-{BOOT|SHUTDOWN}-{CUSTOM}

- [BRAND], [MODEL] and {BOOT|SHUTDOWN} fields are required, if animation is device-specific or non-universal
- [BRAND] and [MODEL] fields should be empty, IF the animation is marked as universal
- [UNIVERSAL] should be used, if the animation is marked as universal
- {CUSTOM} field can be optional, it is used to describe the animation

However, it's acceptable if you use different combinations with the required fields used.

An example of naming your animation according to the convention:
	- tecno_ck7n-boot-simple
	- tecno_ck7n-shutdown-simple
	- universal-boot-sunflower
	
	or 
	
	- TecnoCK7n-BootSimple
	- Tecno_CK7N-boot_simple
	- UniversalShutdownFishes

-------------------------------------------------
			ISSUES & TROUBLESHOOTING

I: My phone doesn't show any boot animation!
A: Make sure bootanimation.zip's compression level is set to 0.

I: Cannot find bootanimation.zip (or shutdownanimation.zip) when using compress_module
A: Before even compressing the module, make sure a boot animation is created in place.

To report issues, visit https://github.com/spir0th/bootagen to make an issue.
-------------------------------------------------
END OF README