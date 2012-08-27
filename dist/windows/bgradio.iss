[Setup]
AppName=BGRadio
AppVerName=BGRadio 0.1.0
VersionInfoVersion=0.1.0
AppPublisher=
AppPublisherURL=https://github.com/gen2brain/bgradio
AppSupportURL=
AppUpdatesURL=
DefaultDirName={pf}\BGRadio
DefaultGroupName=BGRadio
AllowNoIcons=yes
OutputDir=.
Uninstallable=yes
WindowVisible=no
AppCopyright=Author: Milan Nikolic <gen2brain@gmail.com>
OutputBaseFilename=bgradio-0.1.0-setup
UninstallDisplayIcon={app}\bgradio.exe
LicenseFile=bgradio\COPYING
DisableStartupPrompt=yes
ChangesAssociations=yes

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";

[Files]
Source: "bgradio\*.pyd"; DestDir: "{app}";
Source: "bgradio\*.exe"; DestDir: "{app}";
Source: "bgradio\*.dll"; DestDir: "{app}";
Source: "bgradio\AUTHORS"; DestDir: "{app}";
Source: "bgradio\COPYING"; DestDir: "{app}";
Source: "bgradio\README.md"; DestDir: "{app}";
Source: "bgradio\plugins\*.dat"; DestDir: "{app}\plugins";
Source: "bgradio\plugins\access\*.dll"; DestDir: "{app}\plugins\access";
Source: "bgradio\plugins\audio_filter\*.dll"; DestDir: "{app}\plugins\audio_filter";
Source: "bgradio\plugins\audio_output\*.dll"; DestDir: "{app}\plugins\audio_output";
Source: "bgradio\plugins\codec\*.dll"; DestDir: "{app}\plugins\codec";
Source: "bgradio\plugins\demux\*.dll"; DestDir: "{app}\plugins\demux";
Source: "bgradio\plugins\mux\*.dll"; DestDir: "{app}\plugins\mux";
Source: "bgradio\plugins\packetizer\*.dll"; DestDir: "{app}\plugins\packetizer";
Source: "bgradio\qt4_plugins\codecs\*.dll"; DestDir: "{app}\qt4_plugins\codecs";
Source: "bgradio\qt4_plugins\iconengines\*.dll"; DestDir: "{app}\qt4_plugins\iconengines";
Source: "bgradio\qt4_plugins\imageformats\*.dll"; DestDir: "{app}\qt4_plugins\imageformats";
Source: "bgradio\doc\vlc\*"; DestDir: "{app}\doc";

[Icons]
Name: {group}\BGRadio; Filename: {app}\bgradio.exe; Tasks: desktopicon;
Name: {group}\{cm:ProgramOnTheWeb,bgradio}; Filename: https://github.com/gen2brain/bgradio;
Name: {group}\{cm:UninstallProgram,bgradio}; Filename: {app}\unins000.exe;
Name: {userdesktop}\BGRadio; Filename: {app}\bgradio.exe; Tasks: desktopicon;

[Run]
Filename: {app}\bgradio.exe; Description: {cm:LaunchProgram,bgradio}; Flags: nowait postinstall skipifsilent;

[Dirs]
Tasks: desktopicon; Name: C:\bgradio\dist\windows\bgradio;
