rom pathlib import Path

def task_7(directory):
    extensions = {
        'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg',
                  'mpeg', 'm4v', 'h264', 'flv', 'rm', 'swf', 'vob'],

        'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb',
                 'sav', 'tar', 'xml'],

        'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa',
                  'wma', 'wpl', 'cda'],

        'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg',
                  'tif', 'tiff'],
        'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

        'exe': ['exe', 'com'],
    }

    result = [file.split('.') for dirs, folders, files in os.walk(directory) for file in files]

    for (name, expan) in result:
        for k, v in extensions.items():
            if expan in v:
                new_dir = Path().cwd() / directory / k
                if new_dir.is_dir():
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')
                else:
                    Path(new_dir).mkdir(parents=True)
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')
