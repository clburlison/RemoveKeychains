Remove Keychains
===

![logo](logo.png)

This is yet another solution for removing keychains on macOS. This is designed to run in the context of a end user GUI session. This application will backup the entire `~/Library/Keychains` folder into `~/Library/Keychain_bkup`. After the backup the keychains will be removed and a force restart will attempt to take place.

Download the latest release [here](https://github.com/clburlison/RemoveKeychains/releases).

Only tested on 10.11 and 10.12.

### Release Binary

Due to how Apple Script Editor works creating a release binary is more steps than it should be.

1. Open "Remove Keychains.app"
1. File Export with the following options:
	1. File Format: `Application`
	1. Options: `Run-only` enabled all others disabled
	1. Code Sign: select dev cert
1. Save
1. Replace default icon with `applet.icns`.
1. Command + I to open inspector
1. Drag `applet.icns` onto the default icon
1. Close the inspector
1. Compress as a zip for github

### Credits

|  Author | Link |
|---|---|
| [pudquick](https://github.com/pudquick) | [keychainlib](https://gist.github.com/pudquick/9300560) |
| [Icon Archive](http://www.iconarchive.com/) | [Lock icon](http://www.iconarchive.com/show/colorful-long-shadow-icons-by-graphicloads/Lock-icon.html) |