"""
    Calculates the inferential statistics for the multisyllabic acquisition dissertation project

    Contains code to run all of the inferential statistics in the
    dissertation project. This entails both CVC and multisyllabic
    words. Note that create_variables.py must be run first, to
    create the variables, before the inferential statistics can
    be performed.

    Examples:

        $ python stats_inferential.py
            When called from command line, performs the statitics
            and writes the output to a file.

        Note that this is not called from other modules.

"""
import numpy as np
import statsmodels.api as sm
from completed_projects.rajaram_dissertation.locations import Locations
from completed_projects.rajaram_dissertation.create_variables import CreateVariables


class InferentialStatistics():
    """ Only class in module; see header for complete documentation """

    def __init__(self):
        # project specific file locations and variable names
        self.l = Locations()
        self.cv = CreateVariables()
        self.cv.loadExperimentalVars()
        self.bootstrap_num = 1000

    def calculate_regression(self, y, x):
        # runs multiple regression
        x = sm.add_constant(x)
        results = sm.OLS(endog=y, exog=x).fit()
        return results

    def single_regression(self, vars, fau, density, frequency):
        xvars = np.vstack((vars[density], vars[frequency])).T
        return self.calculate_regression(vars[fau], xvars)

    def write_at_age(self, orig, label, f,rci):
        # prints line for a single run of the regression

        def ft(val):
            # formats the variable for printing to 4 decimal places
            return str(np.round(val, 5))

        c = ','
        # formats the variables nicely
        # observations, df_num, def_denom, fval, pval,condition number, rsquared
        f.write(label + c + ft(orig.nobs) + c + ft(orig.df_model) + c)
        f.write(ft(orig.df_resid) + c + ft(orig.fvalue) + c + ft(orig.f_pvalue)+ c)
        f.write(ft(orig.rsquared))
        f.write(' (' + ft(rci[0]) + '-' + ft(rci[1]) + ')' + '\n') # rsquared ci

    def find_CI(self,dist,alpha):

        ordered = np.sort(dist)
        p_low = ((1.0 - alpha) / 2.0) * 100
        lower = max(0.0, np.percentile(ordered, p_low))
        p_up = (alpha + ((1.0 - alpha) / 2.0)) * 100
        upper = min(1.0, np.percentile(ordered, p_up))
        return [lower, upper]

    def regression_at_age(self, f,label, child, fau, density,alpha):
        # independent variables
        rsquareds = list()
        original = self.calculate_regression(child[fau], child[density])
        #print(original.summary())
        for count in range(0,self.bootstrap_num):
            random = child.sample(n=len(child),replace=True)
            random_regr = self.calculate_regression(random[fau],random[density])
            rsquareds.append(random_regr.rsquared)
        rci = self.find_CI(rsquareds,alpha)
        self.write_at_age(original,label,f,rci)

    def run_positive_control(self):
        # runs CVC Positive Control experiments

        phon_nd = self.cv.phon_n_density
        phon_nf = self.cv.sad_frequency_pct_raw
        pact = self.cv.fau_pct_pct_p2

        v3c = self.cv.threeVars[self.cv.threeCVC]
        v4c = self.cv.fourVars[self.cv.fourCVC]
        v6c = self.cv.sixVars[self.cv.sixCVC]

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

        alpha = 0.95

        print('known standard control conditions')

        filename = self.l.results_text + "positive_control_CVC.csv"
        f = open(filename,"w")
        # runs regressions from previously generated variables

        header = 'age,observations,df_num, def_denom, fval, pval, rsquared (95% CI)\n'

        f.write('POSITIVE CONTROL - Determine if there is an effect with known standard controls\n')

        f.write('\nCVC and PHON DENSITY - pct/pct PACT - poly 2\n')
        f.write(header)
        print('PHON density')
        self.regression_at_age(f, 'three', v3c, pact, phon_nd, alpha)
        self.regression_at_age(f, 'four', v4c, pact, phon_nd, alpha)
        self.regression_at_age(f, 'six', v6c, pact, phon_nd, alpha)

        f.write('\nCVC and PHON FREQUENCY - pct/pct PACT - poly 2\n')
        f.write(header)
        print('cvc')
        self.regression_at_age(f, 'three', v3c, pact, phon_nf, alpha)
        self.regression_at_age(f, 'four', v4c, pact, phon_nf, alpha)
        self.regression_at_age(f, 'six', v6c, pact, phon_nf, alpha)

        f.write('\n5 phoneme bisyllabic and PHON FREQUENCY - pct/pct PACT \n')
        f.write(header)
        print('multisyllabic - bisyllabic')
        self.regression_at_age(f, 'three', b3, pact, phon_nf, alpha)
        self.regression_at_age(f, 'four', b4, pact, phon_nf, alpha)
        self.regression_at_age(f, 'six', b6, pact, phon_nf, alpha)

    def run_multisyllabic(self):
        # runs CVC Positive Control experiments

        sonD = self.cv.onset_nucleus_density
        soncD = self.cv.onset_nucleus_coda_density
        pact = self.cv.fau_pct_pct_p2

        m3 = self.cv.threeVars[self.cv.threeMulti]
        m4 = self.cv.fourVars[self.cv.fourMulti]
        m6 = self.cv.sixVars[self.cv.sixMulti]

        alpha = 0.95

        print('positive control')

        filename = self.l.results_text + "multisyllabic_inf_son_sonc.csv"
        f = open(filename,"w")
        # runs regressions from previously generated variables

        header = 'age,observations,df_num, def_denom, fval, pval, rsquared (95% CI)\n'

        f.write('MULTISYLLABIC - Determine if there is an effect with either son or sonc density\n')

        f.write('\nMULTI and SON DENSITY - pct/pct fau - poly 2\n')
        f.write(header)
        print('cvc')
        self.regression_at_age(f, 'three', m3, pact, sonD, alpha)
        self.regression_at_age(f, 'four', m4, pact, sonD, alpha)
        self.regression_at_age(f, 'six', m6, pact, sonD, alpha)

        f.write('\nPOST HOC MULTI and SONC DENSITY - pct/pct fau - poly 2\n')
        f.write(header)
        print('cvc')
        self.regression_at_age(f, 'three', m3, pact, soncD, alpha)
        self.regression_at_age(f, 'four', m4, pact, soncD, alpha)
        self.regression_at_age(f, 'six', m6, pact, soncD, alpha)

if __name__ == "__main__":
    # see file header for usage examples
    TEST_CASE = InferentialStatistics()
    TEST_CASE.run_positive_control()
    TEST_CASE.run_multisyllabic()