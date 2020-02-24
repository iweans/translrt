
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


class MDTranslator(object):

    def __init__(self):
        self._single_delimiters = [
            '#', '*', '+', '~', '-', '|', ':', '=', '!', '`', '\n',
        ]
        self._double_delimiters = {
            '[': ']',
            '(': ')',
        }

    def parse(self, text):
        parts = []
        stack = []
        tmp_part = ''
        tmp_delimiter = ''
        # ----------------------------------------
        for idx, char in enumerate(text):
            if char not in self._single_delimiters:
                if char.isdigit() and tmp_delimiter:
                    tmp_delimiter += char
                    continue
                # --------------------
                if tmp_delimiter and not char.isspace():
                    parts.append(tmp_part)
                    stack.append(tmp_delimiter)
                    tmp_part = ''
                    tmp_delimiter = ''
                # --------------------
                if tmp_delimiter and char.isspace():
                    tmp_delimiter += char
                # --------------------
                tmp_part += char
                continue
            # ------------------------------
            tmp_delimiter += char
        # ----------------------------------------
        parts.append(tmp_part)
        if tmp_delimiter:
            stack.append(tmp_delimiter)
        else:
            stack.append('\n')
        # ----------------------------------------
        return parts, stack

    def format(self):
        pass

    def convert(self, text):
        parts, stack = self.parse(text)
        return '\n'.join(parts).strip(), stack

    def decode(self, text):
        text = '\n\n' + text
        return text.split('\n\n')


if __name__ == '__main__':
    headers = {
            'Accept': '* / *',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh-CN, zh; q=0.9',
            'Connection': 'keep - alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

    md_translator = MDTranslator()
    res, stack = md_translator.convert(test_text)
    print(res)

    recived_text = """Markdown translation cutting algorithm

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
    dres = md_translator.decode(recived_text)

    result = ''
    for content, delimiter in zip(dres, stack):
        result += (content + delimiter)

    print(result)
