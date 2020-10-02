# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\wesle\\Documents\\TCC\\fbsTeste\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\wesle\\Documents\\TCC\\fbsTeste\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\wesle\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\wesle\\Documents\\TCC\\fbsTeste\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='AlfabetoTeste',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\wesle\\Documents\\TCC\\fbsTeste\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='AlfabetoTeste')
