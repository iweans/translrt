# Translate Rich Text
## Introduction

This projects is develop for my girl friends (gifts to **Xijun**, a web developer).

She wants a algorithm that translating the Rich Text (include XML and Markdown) using `Baidu Fanyi API`. 

If you have same problem in your projects, this is for you.

## Usage

By now, I implement `Markdown Parser` only.

**Note**: this parser is demo now, if you want use it in production, please complete it !

```
from parses import MarkdownParser

test_text = '...'
parser = MarkdownParser()
encoded_text, content_delimiters = parser.encode(test_text)

translated_text '...'  # 把encoded_text丢到翻译器中得到翻译的文本
print(encoded_text)
res = parser.decode(translated_text, content_delimiters)
print(res)
```





## Contribution

I am sorry for that I use **Python** code instead of **Javascript**, due to my time. If you want contribute this project using Javascript or other programing language, email `iweans@qq.com` to me. 