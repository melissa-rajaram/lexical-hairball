"""
    Creates the variables used in Melissa Rajaram's dissertation project.

    Begins with the words in a SALT file, and produces multiple .npy
    files containing the variables used in my dissertation project.

    Examples:

        $ python create_variables.py
            When called from the command line, creates the variables and
            and serializes them to files.

        cv = CreateVariables()
            When called from other modules, reads the variables in from a
            serialized file.

"""

import numpy as np
import pandas as pd
from completed_projects.rajaram_dissertation.creating_variables.similarity import PhonemicSimilarity
from completed_projects.rajaram_dissertation.creating_variables.similarity import SONSimilarity
from completed_projects.rajaram_dissertation.creating_variables.syllabifier import Syllabifier
from completed_projects.rajaram_dissertation.creating_variables.proxy_acq_conv_trscr import ProxyAcqConvTrscr
from completed_projects.rajaram_dissertation.transcript_processing.create_lexicons import CreateLexicons
from completed_projects.rajaram_dissertation.locations import Locations

class CreateVariables:
    """ Only class in module; see header for complete documentation """

    def __init__(self):

        # project specific file locations and variable names
        self.l = Locations()
        self.findShape = Syllabifier('STRESS')
        self.sim = SONSimilarity(list())
        self.fau = ProxyAcqConvTrscr()

        # labels for columns in pandas
        self.orthographic = 'orthographic'
        self.phonological = 'phonological'
        self.syllables = 'syllables'
        self.onset_nucleus = 'onset_nucleus'
        self.onset_nucleus_coda = 'onset_nucleus_coda'

        # indexes for numeric variables
        self.length_syllables = 'length_syllables'
        self.length_phonemes = 'length_phonemes'
        self.str_pos = 'stressed_syll_position'
        self.pct_child = 'percent_child'
        self.pct_adult = 'percent_adult'
        self.token_child = 'token_child'
        self.token_adult = 'token_adult'

        # SON and PHON neighborhood density
        self.phon_n_density = 'SAD_density'
        self.onset_nucleus_density = 'onset_nucleus_density'
        self.onset_nucleus_coda_density = 'onset_nucleus_coda_density'

        # PHON neighborhood frequency
        self.son_frequency = 'SON_frequency'
        self.sad_frequency_pct_raw = 'SAD_frequency_pct_child_raw'

        # different ways of creating PACT values
        self.fau_pct_tok_p1 = 'fau_poly1'
        self.fau_pct_tok_p2 = 'fau_poly2'
        self.fau_tok_tok_p1 = 'fau_token_poly1'
        self.fau_tok_tok_p2 = 'fau_token_poly2'
        self.fau_pct_pct_p1 = 'fau_pct_poly1'
        self.fau_pct_pct_p2 = 'fau_pct_poly2'


    def create_experimental_vars(self):
        lex = CreateLexicons()
        # OME child with OME adult as frequency
        print('writing child lexicons')
        self.serialize_experimental_vars(lex.child3, lex.adult3, T.l.filebase + T.l.threename)
        self.serialize_experimental_vars(lex.child4, lex.adult4, T.l.filebase + T.l.fourname)
        self.serialize_experimental_vars(lex.child6, lex.adult6, T.l.filebase + T.l.sixname)
        # OME ADULT (with adult frequency)
        print('writing adult lexicons')
        self.serialize_experimental_vars(lex.adult3, lex.adult3, T.l.filebase + T.l.threeAdultname)
        self.serialize_experimental_vars(lex.adult4, lex.adult4, T.l.filebase + T.l.fourAdultname)
        self.serialize_experimental_vars(lex.adult6, lex.adult6, T.l.filebase + T.l.sixAdultname)
        print('finished.')

    def serialize_experimental_vars(self, child, adult, filebase):

        def find_orthographic(phon):
            return child[phon]['ORTH']

        def find_onset_nucleus(phon):
            if '_' in phon:
                trim = ""
                for syll in phon.split('_'):
                    if '1' in syll:
                        trim = self.sim.trimSyllable(syll)
                return trim

            else:
                return self.sim.trimSyllable(phon)

        def find_onset_nucleus_coda(phon):
            if '_' in phon:
                trim = ""
                for syll in phon.split('_'):
                    if '1' in syll:
                        return syll
            else:
                return phon

        def find_length_syllables(phon):
            if self.findShape.number_syllables(phon) > 1:
                return self.findShape.number_syllables(phon)
            else:
                if self.findShape.CVshape(phon) == 'cv1c':
                    return 0
                return 1

        def find_length_phonemes(phon):
            nounder = phon.replace("_","")
            nounder = nounder.replace("1","")
            return len(nounder)

        def find_stressed_syllable(phon):
            pieces = phon.split("_")
            for pos in range(0, len(pieces)):
                if "1" in pieces[pos]:
                    return pos + 1
            print(phon, 'no stress')
            return -1

        def find_log_pct_child(phon):
            return np.log(child[phon]['NUMCHILD'])

        def find_log_pct_adult(phon):
            if phon in adult.keys():
                return np.log(adult[phon]['NUMCHILD'])
            else:
                return np.nan

        def find_log_child_token(phon):
            return np.log1p(child[phon]['TOKEN'])

        def find_log_adult_token(phon):
            if phon in adult.keys():
                return np.log1p(adult[phon]['TOKEN'])
            else:
                return np.nan

        def find_syllable_representation(phon):
            return child_SON_sim.phon2syll[phon]

        def find_child_SON_density(phon):
            return len(child_SON[phon])

        def find_child_PHON_density(phon):
            return len(current_all_sim[phon])

        def find_adult_PHON_frequency_pct_raw(phon):

            # averag adult PCT frequency of SAD similar words
            freqsum = 0
            if phon in current_all_sim:
                if len(current_all_sim[phon]) >= 1:
                    neighbors = current_all_sim[phon]
                    for neighbor in neighbors:
                        if neighbor in adult:
                            freqsum += adult[neighbor]['NUMCHILD']
                    return float(freqsum) / len(neighbors)
                else:
                    return freqsum # no neighbors
            else:
                return np.nan # not in dict

        def find_adult_SON_density(phon):

            # average log adult token frequency of SON similar words
            if phon in current_all_sim:
                return len(current_all_sim[phon])
            else:
                return 0

        def adjusted_use(ause,cuse,poly):
            blank = np.zeros(len(vars))
            blank.fill(np.nan)

            adjusted = self.fau.poly_residual(ause[mask], cuse[mask], poly)
            blank[mask] = adjusted
            return blank

        vars = pd.DataFrame()
        vars[self.phonological] = child.keys()
        # variables straight from SALT files
        vars[self.orthographic] = vars.phonological.apply(find_orthographic)
        vars[self.pct_child] = vars.phonological.apply(find_log_pct_child)
        vars[self.pct_adult] = vars.phonological.apply(find_log_pct_adult)
        vars[self.token_child] = vars.phonological.apply(find_log_child_token)
        vars[self.token_adult] = vars.phonological.apply(find_log_adult_token)
        # relating to word characteristics
        vars[self.syllables] = vars.phonological.apply(find_syllable_representation)
        vars[self.length_syllables] = vars.syllables.apply(find_length_syllables)
        vars[self.length_phonemes] = vars.phonological.apply(find_length_phonemes)
        vars[self.str_pos] = vars.syllables.apply(find_stressed_syllable)
        vars[self.onset_nucleus] = vars.syllables.apply(find_onset_nucleus)
        vars[self.onset_nucleus_coda] = vars.syllables.apply(find_onset_nucleus_coda)
        # creating stressed syllable based similarity metrics
        child_SON_sim = SONSimilarity(child.keys())
        child_SON = child_SON_sim.stress_onset_nucleus_similarity_word(simtype='onset-nucleus')
        vars[self.onset_nucleus_density] = vars.phonological.apply(find_child_SON_density)
        child_SON_sim = SONSimilarity(child.keys())
        child_SON = child_SON_sim.stress_onset_nucleus_similarity_word(simtype='onset-nucleus-coda')
        vars[self.onset_nucleus_coda_density] = vars.phonological.apply(find_child_SON_density)

        child_SAD_sim = PhonemicSimilarity(child.keys())
        current_all_sim = child_SAD_sim.findPhonemicSimilarity(child.keys(), True)
        vars[self.phon_n_density] = vars.phonological.apply(find_child_PHON_density)
        # PHON neighborhood frequency variable
        vars[self.sad_frequency_pct_raw] = vars.phonological.apply(find_adult_PHON_frequency_pct_raw)

        # various versions of PACT with pct/token, token/token, pct/pct
        mask = np.isfinite(vars[self.token_adult])
        vars[self.fau_pct_tok_p1] = adjusted_use(vars[self.token_adult], vars[self.pct_child], 1)
        vars[self.fau_pct_tok_p2] = adjusted_use(vars[self.token_adult], vars[self.pct_child], 2)
        vars[self.fau_tok_tok_p1] = adjusted_use(vars[self.token_adult], vars[self.token_child], 1)
        vars[self.fau_tok_tok_p2] = adjusted_use(vars[self.token_adult], vars[self.token_child], 2)
        vars[self.fau_pct_pct_p1] = adjusted_use(vars[self.pct_adult], vars[self.pct_child], 1)
        vars[self.fau_pct_pct_p2] = adjusted_use(vars[self.pct_adult], vars[self.pct_child], 2)

        print('serializing:',filebase)
        vars.to_pickle(filebase + '_vars.pickle')

    def loadExperimentalVars(self):
        # loads the previously created variables from pickle files

        # Child OME with OME adult frequency
        self.threeVars = pd.read_pickle(self.l.filebase + self.l.threename + '_vars.pickle')
        self.fourVars = pd.read_pickle(self.l.filebase + self.l.fourname + '_vars.pickle')
        self.sixVars = pd.read_pickle(self.l.filebase + self.l.sixname + '_vars.pickle')

        self.threeAdultVars = pd.read_pickle(self.l.filebase + self.l.threeAdultname + '_vars.pickle')
        self.fourAdultVars = pd.read_pickle(self.l.filebase + self.l.fourAdultname + '_vars.pickle')
        self.sixAdultVars = pd.read_pickle(self.l.filebase + self.l.sixAdultname + '_vars.pickle')

        # MASKS: Experimental set - Multisyllabic or CVC words in child
        self.threeMulti = np.logical_and(self.threeVars[self.length_syllables] > 1, np.isfinite(self.threeVars[self.token_adult]))
        self.fourMulti = np.logical_and(self.fourVars[ self.length_syllables] > 1, np.isfinite(self.fourVars[ self.token_adult]))
        self.sixMulti = np.logical_and(self.sixVars[ self.length_syllables] > 1, np.isfinite(self.sixVars[ self.token_adult]))
        self.threeCVC = np.logical_and(self.threeVars[ self.length_syllables] == 0, np.isfinite(self.threeVars[ self.token_adult]))
        self.fourCVC = np.logical_and(self.fourVars[ self.length_syllables] == 0, np.isfinite(self.fourVars[ self.token_adult]))
        self.sixCVC = np.logical_and(self.sixVars[ self.length_syllables] == 0, np.isfinite(self.sixVars[ self.token_adult]))

        # MASKS: Descriptive set - All Multisyllabic or CVC words in child
        self.threeMultiAll = self.threeVars[self.length_syllables] > 1
        self.fourMultiAll = self.fourVars[ self.length_syllables] > 1
        self.sixMultiAll = self.sixVars[ self.length_syllables] > 1
        self.threeCVCAll = self.threeVars[ self.length_syllables] == 0
        self.fourCVCAll = self.fourVars[ self.length_syllables] == 0
        self.sixCVCAll = self.sixVars[ self.length_syllables] == 0

        # ADULT MASKS: descriptive set:

if __name__ == "__main__":
    # see file header for usage examples
    T = CreateVariables()
    T.create_experimental_vars()