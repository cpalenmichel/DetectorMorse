import pytest

from detectormorse import detector

SENT_ROLLS = """Rolls-Royce Motor Cars Inc. said it expects its U.S. sales to remain
steady at about 1,200 cars in 1990."""
SENT_TORTURE = "Dr. F. Jones M.D. doesn't have a Ph.D. and never went to N. Korea."
SENT_BOTH = " ".join((SENT_ROLLS, SENT_TORTURE))
SENT_BOTH_WHITESPACE = ' ' + SENT_ROLLS + '  ' + SENT_TORTURE + ' '


@pytest.fixture(scope='module')
def default_model():
    return detector.default_model()


def test_single_sentence(default_model):
    sents = list(default_model.segments(SENT_ROLLS))
    assert len(sents) == 1


def test_two_sentences(default_model):
    sents = list(default_model.segments(SENT_BOTH))
    assert len(sents) == 2


def test_strip(default_model):
    """Strip non-initial whitespace by default."""
    sents = list(default_model.segments(SENT_BOTH_WHITESPACE))
    assert len(sents) == 2
    assert sents[0] == ' ' + SENT_ROLLS
    assert sents[1] == SENT_TORTURE


def test_strip_false(default_model):
    """Preserve all whitespace when strip=False."""
    sents = list(default_model.segments(SENT_BOTH_WHITESPACE, strip=False))
    assert len(sents) == 2
    assert sents[0] == ' ' + SENT_ROLLS + '  '
    assert sents[1] == SENT_TORTURE + ' '
