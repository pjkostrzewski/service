class Global():
    @classmethod
    def get_size(cls, bytes_int, suffix="B"):
        """Scale bytes to its proper format

        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes_int < factor:
                return f'{bytes_int:.2f}{unit}{suffix}'
            bytes_int /= factor
