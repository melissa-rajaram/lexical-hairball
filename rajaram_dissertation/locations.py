""" Contains the paths used for Melissa Rajaram's dissertation

    Note that while some of these files can be downloaded from the
    internet, the data files are not included.

"""
class Locations():
    """
    Contains all the locations of the files, and consistent names so that they don't need to be
    hardcoded.
    """
    def __init__(self):
        """

        """
        self.mybase = "/home/melissa/Dropbox/experiments/"

        ## location, names to write data files
        self.filebase = self.mybase + "python/data/rajaram_dissertation/"
        self.results_text = self.mybase + "project_files/rajaram_dissertation/results_text/"
        self.descriptive_img = self.mybase + 'project_files/rajaram_dissertation/descriptive/'

        # CHILD AND ADULT LEXICON NAMES
        self.threename = "three"
        self.fourname = "four"
        self.sixname = "six"
        self.threeAdultname = "threeAdult"
        self.fourAdultname = "fourAdult"
        self.sixAdultname = "sixAdult"

        ## EVALUATION OF CHILD WORDS
        self.word_eval_base = self.mybase + 'project_files/rajaram_dissertation/word_evaluation/'
        self.prior_word_eval = self.word_eval_base + 'word_eval_previous.csv'
        self.current_eval = self.word_eval_base + 'word_eval_all.csv'

        ## CHILD AND ADULT FILES AND LEXICONS
        self.threeChildSALT = self.mybase + "lexicons/OME_expressive/pilot_data/root_word_list/three_child.CSV"
        self.fourChildSALT = self.mybase + "lexicons/OME_expressive/pilot_data/root_word_list/four_child.CSV"
        self.sixChildSALT = self.mybase + "lexicons/OME_expressive/pilot_data/root_word_list/six_child.CSV"
        self.threeAdultSALT = self.mybase + "lexicons/OME_expressive/pilot_data/root_word_list/three_adult.CSV"
        self.fourAdultSALT = self.mybase + "lexicons/OME_expressive/pilot_data/root_word_list/four_adult.CSV"
        self.sixAdultSALT = self.mybase + "lexicons/OME_expressive/pilot_data/root_word_list/six_adult.CSV"

        ## TOOLS: FILES USED
        self.closed_class = self.mybase + "resources/part_of_speech/closed_class/attachment.txt"
        self.cmutranslator = self.mybase + "resources/cmu_dictionary/cmudict.0.7a"
        self.moby_pos = self.mybase + "resources/part_of_speech/mpos/mobypos.txt"
        self.english_lexicon_project = self.mybase + "resources/english_lexicon_project/elp_everything.csv"

if __name__ == "__main__":

    LOCATIONS = Locations()
    print('Locations of all files and resources used in Melissa Rajaram dissertation')

