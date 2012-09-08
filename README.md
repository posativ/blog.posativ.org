# blog.posativ.org | acrylamid

This are most ressources from my personal blog using [Acrylamid][1] as
static blog compiler. Beside the default HTML5 theme it features an
extended acronym filter, a *planet* feed and a listing of all
[Linkschleuders][2] on a single site without summarization. And I tried
a small wiki, but Acrylamid is not real good at it …

## Requirements

- reStructuredText, Markdown, pandoc
- AsciiMathML, Jinja2
- lolcat for special colorization

## See it in action

    $ git clone https://github.com/posativ/blog.posativ.org.git && cd blog.posativ.org/
    $ acrylamid compile
    $ acrylamid view
    $ acrylamid deploy blog

It's the reason why I am developing [Acrylamid][1].

[1]: https://github.com/posativ/acrylamid/
[2]: http://blog.posativ.org/linkschleuder/full/
