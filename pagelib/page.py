"""
HTML Page module.
"""
import polyglot.text
import re
import parsel
import selectolax.parser
import sys


class HtmlPage:
    def __init__(self, html):
        self.html = html
        self.selector = parsel.Selector(text=self.html)
        self.alpha_numeric_regex = re.compile(r'[\W_]+', re.UNICODE)

    def __str__(self):
        return self.title or ''

    def __repr__(self):
        return 'HtmlPage(title={}, bytes={})'.format(self.title, self.bytes)

    @property
    def bytes(self):
        return self._get_byte_size()

    @property
    def meta_keywords(self):
        return self._get_meta_keywords()

    @property
    def docx(self):
        return polyglot.text.Text(self.text)

    @property
    def meta_description(self):
        return self._get_meta_description()

    @property
    def title(self):
        return self._get_title()

    @property
    def text(self):
        return self._get_text()

    @property
    def keywords(self):
        return self._get_keywords()

    @property
    def language_code(self):
        return self._get_language_code()

    @property
    def language_name(self):
        return self._get_language_name()

    #@property
    #def lda_tokens(self):
    #    return self._lda_tokenize()

    @property
    def words(self):
        return self._word_tokenize()

    @property
    def sentences(self):
        return self._sentence_tokenize()

    def _match_first_xpath(self, xpaths):
        """
        Return first matching xpath from `xpaths`.

        :param xpaths: list of xpaths
        :type xpaths: list
        :returns: parsel.Selector or None
        """
        for xpath in xpaths:
            try:
                #return self.sel.xpath(xpath).extract()[0]
                return self.selector.xpath(xpath).extract()[0]
            except IndexError:
                pass
        return None

    def _get_byte_size(self):
        """
        Return size of HTML page in bytes.

        returns: int
        """
        return sys.getsizeof(self.html)

    def _get_meta_keywords(self):
        """
        Return content of meta keywords tag.

        :returns: str or None
        """
        xpaths = [
            '//meta[@name="keywords"]/@content'
        ]
        return self._match_first_xpath(xpaths)

    def _get_meta_description(self):
        """
        Return content of meta description tag.

        returns: str or None
        """
        xpaths = [
            '//meta[@property="og:description"]/@content'
        ]
        return self._match_first_xpath(xpaths)

    def _get_title(self):
        """
        Return title of page.

        returns: str or None
        """
        xpaths = [
            '//title/text()',
            '//meta[@property="og:title"]/@content'
        ]
        return self._match_first_xpath(xpaths)

    def _get_text(self):
        """
        Return text of page.

        returns: str
        """
        tree = selectolax.parser.HTMLParser(self.html)

        if tree.body is None:
            return None
        for tag in tree.css('script'):
            tag.decompose()
        for tag in tree.css('style'):
            tag.decompose()
        text = tree.body.text(separator='\n')
        return text

    def _get_language_code(self):
        """
        Return language code of page.
        """
        return self.docx.language.code

    def _get_language_name(self):
        """
        Return language name of page.
        """
        return self.docx.language.name

    def _word_tokenize(self):
        """
        Return word tokens from text of page.
        """
        tokens = []
        for token in self.docx.words:
            if len(token) == 1:
                token = self.alpha_numeric_regex.sub('', token)
            if token:
                tokens.append(token)
        return tokens

    def _sentence_tokenize(self):
        """
        Return sentence tokens from text of page.
        """
        return self.docx.sentences

    # def _lda_tokenize(self):
    #     lda_tokens = []
    #     parser = English()
    #     tokens = parser(self.text)
    #     for token in tokens:
    #         if token.orth_.isspace():
    #             continue
    #         elif token.like_url:
    #             lda_tokens.append('URL')
    #         elif token.orth_.startswith('@'):
    #             lda_tokens.append('SCREEN_NAME')
    #         else:
    #             lda_tokens.append(token.lower_)
    #     return lda_tokens

    #def _get_lemma(self, word):
    #    lemma = wn.morphy(word)
    #    if lemma is None:
    #        return word
    #    else:
    #        return lemma

    #def _get_lemma2(self, word):
    #    return wordNetLemmatizer().lemmatize(word)

    #def _prepare_text_for_lda(self, text):
    #    tokens = self._lda_tokenize(text)
    #    tokens = [token for token in tokens if len(token) > 4]
    #    tokens = [token for token in tokens if token not in EN_STOP]
    #    tokens = [self._get_lemma(token) for token in tokens]
    #    return tokens
