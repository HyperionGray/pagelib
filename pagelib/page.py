"""
HTML Page module.
"""
import gensim
import polyglot
#import nltk
import re
import parsel
#import selectolax.parser

from gensim import corpora

# Download lib dependencies
#nltk.download('wordnet')
#nltk.download('stopwords')
#spacy.load('en')
#from spacy.lang.en import English
#from nltk.corpus import wordnet as wn
#from nltk.stem.wordnet import WordNetLemmatizer
#EN_STOP = set(nltk.corpus.stopwords.words('english'))


class HtmlPage:
    def __init__(self, html):
        self.html = html
        self.sel = parsel.Selector(text=html)
        self.alpha_numeric_regex = re.compile('[\W_]+', re.UNICODE)

    @property
    def meta_keywords(self):
        return self._get_meta_keywords()

    @property
    def docx(self):
        return polyglot.Text(self.text)

    @property
    def meta_description(self):
        return self._get_meta_description()

    @property
    def meta_title(self):
        return self._get_meta_title()

    @property
    def meta_title(self):
        return self._get_meta_title()

    @property
    def text(self):
        return self._get_text()

    @property
    def keywords(self):
        return self._get_keywords()

    @property
    def language(self):
        return self._get_language()

    @property
    def language_name(self):
        return self._get_language_name()

    @property
    def lda_tokens(self):
        return self._lda_tokenize()

    @property
    def word_tokens(self):
        return self._word_tokenize()

    @property
    def sentence_tokens(self):
        return self._sentence_tokenize()

    def _get_meta_keywords(self):
        # TODO
        return None

    def _match_first_xpath(xpaths):
        """
        Return first matching xpath from `xpaths`.

        :param xpaths: list of xpaths
        :type xpaths: list
        :returns: parsel.Selector or None
        """
        for xpath in xpaths:
            try:
                return self.sel.xpath(xpath).extract()[0]
            except IndexError:
                pass
        return None

    def _get_meta_description(self):
        xpaths = [
            '//meta[@property="og:description"]/@content'
        ]
        return self._match_first_xpath(xpaths)

    def _get_meta_title(self):
        xpaths = [
            '//meta[@property="og:title"]/@content'
        ]
        return self._match_first_xpath(xpaths)

    def _get_text(self):
        tree = selectolax.parser.HTMLParser(self.html)

        if tree.body is None:
            return None
        for tag in tree.css('script'):
            tag.decompose()
        for tag in tree.css('style'):
            tag.decompose()
        text = tree.body.text(separator='\n')
        return text

    def _get_keywords(self):
        keywords = gensim.summarization.keywords(self.text).split('\n')
        return keywords

    def _get_language(self):
        try:
            return langdetect.detect(self.text)
        except langdetect.lang_detect_exception.LangDetectException:
            return None

    def _get_language_code(self):
       return self.docx.language.code

    def _get_language_name(self):
        return self.docx.language.name

    def _word_tokenize(self):
        tokens = []
        for token in self.docx.words:
            if len(token) == 1:
                token = self.alpha_numeric_regex.sub('', token)
            if token:
                tokens.append(token)
        return tokens

    def _sentence_tokenize(self):
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
