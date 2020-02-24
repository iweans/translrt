
class MarkdownParser:

    def __init__(self, whitelist_filters=None):
        self._delimiter = '\n'
        self._single_delimiters = \
            ('#', '*', '+', '~', '-', '|', '`', '\n')
        self._whitelist_filters = whitelist_filters or [str.isdigit]

    def encode(self, text):
        content_parts, content_delimiters = \
            self.parse(text)
        encoded_text = self._delimiter.join(content_parts)
        return encoded_text, content_delimiters

    def decode(self, text, content_delimiters):
        translated_parts = ('\n\n' + text).split('\n\n')
        result = ''
        for content, delimiter in zip(translated_parts, content_delimiters):
            result += (content + delimiter)
        return result
    def parse(self, text):
        content_parts = []
        content_delimiters = []
        tmp_delimiter = tmp_part = ''
        # ----------------------------------------
        for char in text:
            if char in self._single_delimiters:
                tmp_delimiter += char
                continue
            # ------------------------------
            if self._check_whitelist(char):
                tmp_delimiter += char
                continue
            # ------------------------------
            if char.isspace() and tmp_delimiter:
                tmp_delimiter += char
                continue
            # ------------------------------
            if not char.isspace() and tmp_delimiter:
                content_parts.append(tmp_part)
                content_delimiters.append(tmp_delimiter)
                tmp_delimiter = tmp_part = ''
            # --------------------
            tmp_part += char
        # ----------------------------------------
        tmp_part and content_parts.append(tmp_part)
        content_delimiters.append(tmp_delimiter or '\n')
        return content_parts, content_delimiters

    def _check_whitelist(self, char):
        for filter_callable in self._whitelist_filters:
            if not filter_callable(char):
                return False
        # ----------------------------------------
        return True
