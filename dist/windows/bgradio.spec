# -*- mode: python -*-

a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), 'c:\\bgradio\\bgradio'],
             pathex=['c:\\bgradio\\pyinstaller', 'c:\\bgradio\\src'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\bgradio', 'bgradio.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='c:\\bgradio\\dist\\windows\\bgradio.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='bgradio')
