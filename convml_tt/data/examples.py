from fastai.datasets import _checks


_URL_ROOT = "http://homepages.see.leeds.ac.uk/~earlcd/ml-datasets/"

class ExampleData:
    TINY10 = _URL_ROOT + "Nx256_s200000.0_N0study_N10train"
    SMALL100 = _URL_ROOT + "Nx256_s200000.0_N0study_N100train"

# add our own datasets into fastai's datastructure here so we can use fastai's
# infrastructure for loading them
_checks[ExampleData.TINY10] = (1144669, 'c599454acb4ff07fbd1551135c350ba9')
_checks[ExampleData.SMALL100] = (87250439, 'f45f9da7aa77b82e493c3289ea1ea951')