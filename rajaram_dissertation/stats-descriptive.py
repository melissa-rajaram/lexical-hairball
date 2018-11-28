"""
    Calculates descriptive statistics for dissertation project.

    Creates tables of summary statistics: mean, median, mode, range, etc.
    for the various variables used in the dissertation project. Contains
    descriptive statistics from all words, cvc words and multisyllabic
    words.

    Examples:
        Give examples of usage scenarios
        $ python stats-descriptive.py
            When run from command line, produces multiple excel files
            containing descriptive statistics.

        This module is not called from other modules.
        
"""
import numpy as np
from scipy import stats

from completed_projects.rajaram_dissertation.create_variables import CreateVariables
from completed_projects.rajaram_dissertation.creating_variables.proxy_acq_conv_trscr import ProxyAcqConvTrscr
from completed_projects.rajaram_dissertation.locations import Locations

class TabularStats():
    """ Only class in module; see header for complete documentation """

    def __init__(self):
        # project specific file locations and variable names
        self.l = Locations()
        self.cv = CreateVariables()
        self.cv.loadExperimentalVars()
        self.r = ProxyAcqConvTrscr()

        # all child words
        self.c3 = self.cv.threeVars
        self.c4 = self.cv.fourVars
        self.c6 = self.cv.sixVars

        # all adult words
        self.a3 = self.cv.threeAdultVars
        self.a4 = self.cv.fourAdultVars
        self.a6 = self.cv.sixAdultVars

        # all child with adjusted use
        self.c3a = self.cv.threeVars[self.cv.threeVars[self.cv.token_adult]>0]
        self.c4a = self.cv.fourVars[self.cv.fourVars[self.cv.token_adult] > 0]
        self.c6a = self.cv.sixVars[self.cv.sixVars[self.cv.token_adult] > 0]

        # child multisyllabic words and vars - all
        self.m3a = self.cv.threeVars[self.cv.threeMultiAll]
        self.m4a = self.cv.fourVars[self.cv.fourMultiAll]
        self.m6a = self.cv.sixVars[self.cv.sixMultiAll]

        # child multisyllabic words and vars - adult token > 0
        self.m3 = self.cv.threeVars[self.cv.threeMulti]
        self.m4 = self.cv.fourVars[self.cv.fourMulti]
        self.m6 = self.cv.sixVars[self.cv.sixMulti]

        # child CVC words and vars - adult token > 0
        self.cvc3 = self.cv.threeVars[self.cv.threeCVC]
        self.cvc4 = self.cv.fourVars[self.cv.fourCVC]
        self.cvc6 = self.cv.sixVars[self.cv.sixCVC]

        self.all_word_stats()
        self.positive_control_stats()
        self.multisyllabic_stats()

    def single_stats(self,f,age3,age4,age6,label):
        """
        prints characteristics of single distribution
        - lowest value
        - highest value
        - mean (sd)
        - median
        - mode
        - skew
        - kurtosis

        :param dist:
        :param label:
        :return:
        """

        def age_line(age,num):

            def pr(val):
                if int(val) == val:
                    return str(int(val))
                else:
                    if np.round(val,2)  == 0:
                        return (str(np.round(val, 4)))
                    else:
                        return(str(np.round(val,2)))

            res = stats.describe(age)
            f.write(num+',')
            f.write(str(res.nobs)+ ',')
            f.write(pr(res.minmax[0]) + ' to ' + pr(res.minmax[1]) + ',')
            f.write(pr(res.mean) + ' ')
            f.write('(' + pr(np.std(age)) + '),')
            f.write(pr(np.median(age))+ ',')
            #print(stats.mode(age))
            f.write(pr(stats.mode(age)[0])+' ')
            f.write('('+pr(stats.mode(age)[1])+'),')
            f.write(pr(res.skewness)+',')
            f.write(pr(res.kurtosis)+ '\n')
            return(res.nobs,res.minmax[0],res.minmax[1],res.mean, np.std(age),np.median(age),stats.mode(age)[0],
                   stats.mode(age)[1],res.skewness,res.kurtosis)

        def average_line(age3,age4,age6):

            def av(idx):
                return str(np.round((age3[idx] + age4[idx] + age6[idx])/3,2))

            f.write('average,'+ av(0)+',')
            f.write(av(1) + ' to ' + av(2) + ',')
            f.write(av(3) + ' ')
            f.write('(' + av(4) + '),')
            f.write(av(5) + ',')
            f.write(av(6) + ' ')
            f.write('(' + av(7) + '),')
            f.write(av(8) + ',')
            f.write(av(9) + '\n')

        statslabels = 'Age,Observations,Range,Mean (std),Median,Mode (number times),Skewness,Kurtosis\n'
        f.write('\n' + label + '\n')
        f.write(statslabels)
        stats3 = age_line(age3,'3')
        stats4 = age_line(age4,'4')
        stats6 = age_line(age6,'6')
        average_line(stats3,stats4,stats6)
        f.write('\n')

    def all_word_stats(self):
        """
        Prints statistics to a .csv file so that they can be easily imported into excel
        - prints one file for all variables
        :return: Nonea
        """

        filename = self.l.results_text + "stats_tables_all.csv"
        f = open(filename,'w')
        pctc = self.cv.pct_child
        ctoken = self.cv.token_child
        pact = self.cv.fau_pct_pct_p2

        self.single_stats(f,np.exp(self.c3[pctc]), np.exp(self.c4[pctc]), np.exp(self.c6[pctc]),
                     'all words: percent child (raw)')
        self.single_stats(f,np.exp(self.a3[pctc]), np.exp(self.a4[pctc]), np.exp(self.a6[pctc]),
                     'all words: percent adult (raw)')
        self.single_stats(f,np.exp(self.c3[ctoken]), np.exp(self.c4[ctoken]), np.exp(self.c6[ctoken]),
                     'all words: token child (raw)')
        self.single_stats(f,np.exp(self.a3[ctoken]), np.exp(self.a4[ctoken]), np.exp(self.a6[ctoken]),
                     'all words: token adult (raw)')
        self.single_stats(f, self.c3a[pact], self.c4a[pact], self.c6a[pact],
                     'all words: PACT values - pct/pct, poly 2')

        f.close()

    def positive_control_stats(self):
        """
        Prints statistics to a .csv file so that they can be easily imported into excel
        - prints one file for all variables
        :return: Nonea
        """
        # all CVC words from child
        allCVC3 = self.cv.threeVars[self.cv.threeCVCAll]
        allCVC4 = self.cv.fourVars[self.cv.fourCVCAll]
        allCVC6 = self.cv.sixVars[self.cv.sixCVCAll]

        # all CVC words from adult
        a3 = self.cv.threeAdultVars[self.cv.threeAdultVars[self.cv.length_syllables]==0]
        a4 = self.cv.fourAdultVars[self.cv.fourAdultVars[self.cv.length_syllables]==0]
        a6 = self.cv.sixAdultVars[self.cv.sixAdultVars[self.cv.length_syllables]==0]

        bi5_3 = np.logical_and(self.cv.threeVars[self.cv.length_syllables] == 2,
                              np.logical_and(self.cv.threeVars[self.cv.length_phonemes] == 5,
                               self.cv.threeVars[self.cv.token_adult] > 0))
        bi5_4 = np.logical_and(self.cv.fourVars[self.cv.length_syllables] == 2,
                               np.logical_and(self.cv.fourVars[self.cv.length_phonemes] == 5,
                               self.cv.fourVars[self.cv.token_adult] > 0))
        bi5_6 = np.logical_and(self.cv.sixVars[self.cv.length_syllables] == 2,
                               np.logical_and(self.cv.sixVars[self.cv.length_phonemes] == 5,
                               self.cv.sixVars[self.cv.token_adult] > 0))

        b3 = self.cv.threeVars[bi5_3]
        b4 = self.cv.fourVars[bi5_4]
        b6 = self.cv.sixVars[bi5_6]

        filename = self.l.results_text + "stats_tables_positive_control.csv"
        f = open(filename,'w')
        pctc = self.cv.pct_child
        pcta = self.cv.pct_adult
        tokc = self.cv.token_child
        toka = self.cv.token_adult
        phon_density = self.cv.phon_n_density
        phon_frequency = self.cv.phon_n_frequency
        fau_pp = self.cv.fau_pct_pct_p2

        f.write('POSITIVE CONTROL CVC EXPERIMENTS\n')
        f.write('child and adult percent and token use\n')
        # percent and token use for child and adult
        self.single_stats(f, np.exp(allCVC3[pctc]), np.exp(allCVC4[pctc]), np.exp(allCVC6[pctc]),
                          'cvc words: percent child (raw)')
        self.single_stats(f, np.exp(a3[pcta]), np.exp(a4[pcta]), np.exp(a6[pcta]),
                          'cvc words: percent adult (raw)')
        self.single_stats(f, np.exp(allCVC3[tokc]), np.exp(allCVC4[tokc]), np.exp(allCVC6[tokc]),
                          'cvc words: token child (raw)')
        self.single_stats(f, np.exp(a3[toka]), np.exp(a4[toka]), np.exp(a6[toka]),
                          'cvc words: token adult (raw)')

        f.write('independent and dependent variables\n')
        # independent and dependent variables
        self.single_stats(f, self.cvc3[fau_pp], self.cvc4[fau_pp], self.cvc6[fau_pp],
                          'CVC PACT: Percent Child & Percent Adult')
        self.single_stats(f, self.cvc3[phon_density], self.cvc4[phon_density],self.cvc6[phon_density],
                          'CVC PHON Neighborhood Density')
        self.single_stats(f, self.cvc3[phon_frequency], self.cvc4[phon_frequency], self.cvc6[phon_frequency],
                          'CVC PHON Neighborhood Frequency (pct raw)')

        f.write('post-hoc neighborhood frequency: two syllable, five phoneme words\n')
        self.single_stats(f, b3[phon_frequency], b4[phon_frequency], b6[phon_frequency],
                          'BISYLLABIC, 5 PHONEME PHON-N Frequency (pct raw)')
        self.single_stats(f, b3[fau_pp], b4[fau_pp], b6[fau_pp],
                          'BISYLLABIC, 5 PHONEME PACT: Percent Child & Percent Adult')


        f.close()

    def multisyllabic_stats(self):
        """
        Prints statistics to a .csv file so that they can be easily imported into excel
        - prints one file for all variables
        :return: Nonea
        """

        filename = self.l.results_text + "stats_tables_multisyllabic.csv"
        f = open(filename,'w')
        pctc = self.cv.pct_child
        ctoken = self.cv.token_child
        pact = self.cv.fau_pct_pct_p2
        phonnd = self.cv.phon_n_density
        sonnd = self.cv.onset_nucleus_density
        soncnd = self.cv.onset_nucleus_coda_density

        # all multi words from child
        c3a = self.cv.threeVars[self.cv.threeMultiAll]
        c4a = self.cv.fourVars[self.cv.fourMultiAll]
        c6a = self.cv.sixVars[self.cv.sixMultiAll]
        # multisyllabic words used by both children and adults
        c3 = self.cv.threeVars[self.cv.threeMulti]
        c4 = self.cv.fourVars[self.cv.fourMulti]
        c6 = self.cv.sixVars[self.cv.sixMulti]
        # all multi words from adult
        a3a = self.cv.threeAdultVars[self.cv.threeAdultVars[self.cv.length_syllables] > 1]
        a4a = self.cv.fourAdultVars[self.cv.fourAdultVars[self.cv.length_syllables] > 1]
        a6a = self.cv.sixAdultVars[self.cv.sixAdultVars[self.cv.length_syllables] > 1]



        self.single_stats(f,np.exp(c3a[pctc]), np.exp(c4a[pctc]), np.exp(c6a[pctc]),
                     'all multisyllabic words: percent child (unlogged)')
        self.single_stats(f,np.exp(a3a[pctc]), np.exp(a4a[pctc]), np.exp(a6a[pctc]),
                     'all  multisyllabic words: percent adult (unlogged)')
        self.single_stats(f,np.exp(c3a[ctoken]), np.exp(c4a[ctoken]), np.exp(c6a[ctoken]),
                     'all multisyllabic words: token child (unlogged)')
        self.single_stats(f,np.exp(a3a[ctoken]), np.exp(a4a[ctoken]), np.exp(a6a[ctoken]),
                     'all multisyllabic words: token adult (unlogged)')

        self.single_stats(f, c3[pact], c4[pact], c6[pact],
                          'multisyllabic words: PACT values - pct/pct')
        self.single_stats(f, c3[phonnd], c4[phonnd], c6[phonnd],
                          ' multisyllabic words: child phonological_transformation neighborhood density')
        self.single_stats(f, c3[sonnd], c4[sonnd], c6[sonnd],
                          ' multisyllabic words: child STRESS ONSET NUCLEUS density')
        self.single_stats(f, c3[soncnd], c4[soncnd], c6[soncnd],
                          ' POST HOC multisyllabic words: child STRESS ONSET NUCLEUS CODA density')

        f.close()

if __name__ == "__main__":
    # see file header for usage examples
    TEST_CASE = TabularStats()
