# blog.posativ.org | acrylamid

This are most ressources from my personal blog using [Acrylamid][1] as
static blog compiler. Beside the default HTML5 theme it features an
extended acronym filter, a [planet][3] feed and a listing of all
[Linkschleuders][2] on a single site without summarization.

## Requirements

- reStructuredText, Markdown, pandoc
- AsciiMathML, Jinja2
- lolcat for special colorization

## See it in action

    $ git clone https://github.com/posativ/blog.posativ.org.git && cd blog.posativ.org/
    $ acrylamid compile
    $ acrylamid view
    $ acrylamid deploy

You might get a lot of errors during the compilation procedure, that's because I
removed the referenced assets (image gallery and such). With about 170 articles,
I can compile a new entry in less than two seconds, layout or configuration
changes in around 3-4 seconds. Can you do that with Pelican, Tinkerer, Nikola,
whatsoever?

[1]: https://github.com/posativ/acrylamid/
[2]: http://blog.posativ.org/linkschleuder/
[3]: http://blog.posativ.org/rss/planet/
