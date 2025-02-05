# griffe-typingdoc repro

[ChecksumString][test.ChecksumString] has a pep 727 doc string embedded in typing_extensions.Doc, which does not correctly get extracted.

[ChecksumString2][test.ChecksumString2] has a normal doc string embedded in typing_extensions.Doc, which does get correctly extracted.

[NormalString][test.NormalString] is an attempt to see if the addition Pydantic StringConstraint annotation interferes somehow, which it doesn't.

[hi][test.hi] is a function which has a parameter that is annotated pep 727 style, and which does work, which confirms griffe-typingdoc is active and functioning.

[hi_no_docstring][test.hi_no_docstring] is the same as [hi][test.hi], except it is not documented with a docstring. This is to test if the parent object needs a docstring before griffe-typingdoc kicks in, but that's not the case as the parameter is still handled correctly.

::: test
