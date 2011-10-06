htmldiff
````````

A library that uses difflib, genshi and htmldiff to diff
arbitrary fragments of HTML inline.

    >>> from htmldiff import render_html_diff
    >>> render_html_diff('Foo <b>bar</b> baz', 'Foo <i>bar</i> baz')
    u'<div class="diff">Foo <i class="tagdiff_replaced">bar</i> baz</div>'
    >>> render_html_diff('Foo bar baz', 'Foo baz')
    u'<div class="diff">Foo <del>bar</del> baz</div>'
    >>> render_html_diff('Foo baz', 'Foo blah baz')
    u'<div class="diff">Foo <ins>blah</ins> baz</div>'
