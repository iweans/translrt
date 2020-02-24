
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


if __name__ == '__main__':
    test_text = """# Markdown 翻译切割算法

这个算法的作用是将markdown文本切割成翻译单元，再提交到翻译引擎，拿到翻译结果后再组合成原始的格式。

## 一、目前支持的特殊符号有

| 序号 | 符号   |
| ---- | ------ |
| 1    | 井字符 |
| 2    | 星号   |
| 3    | 加号   |
| 4    | 波浪号 |
| 5    | 减号   |
| 6    | 管道符 |
| 7    | 冒号   |
| 8    | 等号   |
| 9    | 感叹号 |
| 10   | 反引号 |
| 11   | 换行符 |

注意：以上符号均指的是英文符号。

## 二、联系作者

不好意思，该项目是我为我女朋友写的，不提供售后服务，有事请联系`18890306960`。"""

    translated_text = """Markdown translation cutting algorithm

The function of this algorithm is to cut markdown text into translation units, submit it to the translation engine, get the translation results, and then combine it into the original format.

1、 Currently supported special symbols are

Serial number

Symbol

Well character

Asterisk

Plus

Wave number

Minus sign

Pipe symbol

colon

Equal sign

Exclamatory mark

backquote

Newline character

Note: the above symbols refer to English symbols.

2、 Contact author

Sorry, I wrote this project for my girlfriend. No after-sales service is provided. Please contact me if you have any questions

。"""

    parser = MarkdownParser()
    encoded_text, content_delimiters = parser.encode(test_text)
    print(encoded_text)
    res = parser.decode(translated_text, content_delimiters)
    print(res)

