"""
    Calculates the Proxy for Acquisition fro Conversational Transcript (PACT) values

    Very simple code to find the residuals in a regression. Has the flexibility
    to be able to determine the best fit 'line' from different orders of polynomials

    Examples:

        $ python frequency_adjusted_use.py
            When run from the command line, prints a message.

        pact = ProxyAcqConvTrscr()
            When called from other modules, can be used to calculate the PACT values
    
"""
import numpy as np

class ProxyAcqConvTrscr():
    """ Only class in module; see header for complete documentation """

    def __init__(self):
        """

        """

    def poly_residual(self, x_vars, y, poly_order):
        """

        :param x_vars:
        :param y:
        :param poly_order:
        :return:
        """

        x1 = x_vars
        y1 = y

        p = np.polyfit(x1, y1, poly_order)
        yprime = np.polyval(p, x1)
        return y - yprime



if __name__ == "__main__":
    # see file header for usage examples
    TEST_CASE = ProxyAcqConvTrscr()
    print('Creates PACT values')
