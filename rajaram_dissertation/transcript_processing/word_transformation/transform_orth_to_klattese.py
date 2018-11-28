#! /usr/bin/python

""" 
   Interfaces with the CMU Pronouncing Dictionary
   - one added benefit is that this code contains a list of 'translation
     exceptions' that will be corrected
     - phonological forms without any stressed vowels
     - phonological forms with more than one stressed vowel

    LAST EXAMINED: 8-23-18
    STATUS: - used in rajaram_dissertation
            - may not be DRY, but functions fine

"""
import re
from completed_projects.rajaram_dissertation.transcript_processing.word_transformation.cmutranslator.cmutranslator import CMUTranslator


class PhonologicalFromOrthographic():
    def __init__(self,surpress_errors=True):
        self.surpress_error = surpress_errors
        CMUdictionary = CMUTranslator("STRESS")
        self.translation_execptions = dict()
        self.load_translation_execptions()
        self.CMU = CMUdictionary.CMUDict

    def load_translation_execptions(self):
        # words that do not have stress marked in the CMU dictionary

        # OR! words with more than one stress :(

        # from OME
        self.translation_execptions["'cause"] = 'k1^z'
        self.translation_execptions['and'] = '^1nd'
        self.translation_execptions['hers'] = 'hR1z'
        self.translation_execptions['in'] = 'I1n'
        self.translation_execptions["y'all"] = 'yc1l'
        self.translation_execptions['er'] = 'R1'
        self.translation_execptions['the'] = 'D^1'
        self.translation_execptions['a'] = '^1'
        self.translation_execptions['her'] = 'hR1'
        self.translation_execptions['were'] = 'wR1'
        self.translation_execptions['mc'] = 'mI1k'
        self.translation_execptions['mhm'] = '^1mh^m'
        self.translation_execptions['ths'] = 'TI1s'
        self.translation_execptions['le'] = 'l^1'
        self.translation_execptions["'em"] = '^1m'
        self.translation_execptions["'n"] = '^1n'
        self.translation_execptions["'m"] = '^1m'
        self.translation_execptions['whats'] = 'w^1ts'
        self.translation_execptions["could've"] = 'kU1d^v'

        # in SUBTLEX
        self.translation_execptions['cogitate'] = 'ka1JItet'
        self.translation_execptions['egret'] = 'E1gr^t'
        self.translation_execptions['reeducation'] = 'riE1dy^keS^n'
        self.translation_execptions['tonsil'] = 'ta1ns^l'
        self.translation_execptions['unanswerable'] = '^n@1nsR^b^l'
        self.translation_execptions['rumour'] = 'ru1mR'
        self.translation_execptions['electrophoresis'] = 'IlE1ktrofcrIsIs'
        self.translation_execptions['marketers'] = 'ma1rk^tRz'
        self.translation_execptions['impolite'] = 'I1mp^lYt'
        self.translation_execptions['tourniquet'] = 'tR1nIkIt'
        self.translation_execptions['expressionless'] = 'I1ksprES^nlIs'
        self.translation_execptions['rehab'] = 'ri1h@b'
        self.translation_execptions['reapply'] = 'ri^1plY'
        self.translation_execptions['dyspeptic'] = 'dIspE1ptIk'
        self.translation_execptions['greediest'] = 'gri1diIst'
        self.translation_execptions['polyglot'] = 'pa1liglat'
        self.translation_execptions['sarin'] = 'sa1rIn'
        self.translation_execptions['purportedly'] = 'pRpc1rtIdli'
        self.translation_execptions['hye'] = 'hY1'
        self.translation_execptions['fs'] = 'fs1'
        self.translation_execptions['rumours'] = 'ru1mRz'
        self.translation_execptions['underinsured'] = '^1ndRInScrd'
        self.translation_execptions['greedier'] = 'gri1diR'
        self.translation_execptions['endometrial'] = 'EndomE1tri^l'
        self.translation_execptions['oceanfront'] = 'o1S^nfr^nt'
        # in Age of Acquisition
        self.translation_execptions['virago'] = 'vI1rago'
        # from ELP
        self.translation_execptions['priciest'] = 'prY1siIst'
        self.translation_execptions["who've"] ='hu1v'
        self.translation_execptions['accredit'] = '^krE1d^t'
        self.translation_execptions['gasify'] = 'g@1s^fY'
        self.translation_execptions['heterodox'] = 'hE1tR^daks'
        self.translation_execptions['aikin'] = 'e1kIn'

        # words with multiple primary stress: changed to one primary stress
        self.translation_execptions['baseball'] = 'be1sbcl'
        self.translation_execptions['downstairs'] = 'dW1nstErz'
        self.translation_execptions['downtown'] = 'dW1ntWn'
        self.translation_execptions['engineer'] = 'E1nJ^nIr'
        self.translation_execptions['homemade'] = 'ho1mmed'
        self.translation_execptions['lemonade'] = 'lE1m^ned'
        self.translation_execptions['tv'] = 'ti1vi'
        self.translation_execptions['upside'] = '^1psYd'
        self.translation_execptions['everyday'] = 'E1vride'
        self.translation_execptions['overnight'] = 'o1vRnYt'
        self.translation_execptions['cd'] = 'si1di'
        self.translation_execptions['halfway'] = 'h@1fwe'
        self.translation_execptions['birdfeeder'] = 'bR1dfidR'
        self.translation_execptions['boathouse'] = 'bo1thWs'
        self.translation_execptions['crybaby'] = 'krY1bebi'
        self.translation_execptions['faraway'] = 'fa1r^we'
        self.translation_execptions['fourteenth'] = 'fc1rtinT'
        self.translation_execptions['nineteenth'] = 'nY1ntinT'
        self.translation_execptions['fourteens'] = 'fc1rtinz'
        self.translation_execptions['goodwill'] = 'gU1dwIl'
        self.translation_execptions['lopsided'] = 'la1psYdId'
        self.translation_execptions['midair'] = 'mI1dEr'
        self.translation_execptions['minivan'] = 'mI1niv@n'
        self.translation_execptions['deedee'] = 'di1di'
        self.translation_execptions['fourteen'] = 'fc1rtin'
        self.translation_execptions['hoho'] = 'ho1ho'
        self.translation_execptions['markee'] = 'ma1rki'
        self.translation_execptions['mh'] = 'E1meC'
        self.translation_execptions['nineteen'] = 'nY1ntin'
        self.translation_execptions['ok'] = 'o1ke'
        self.translation_execptions['outside'] = 'W1tsYd'
        self.translation_execptions['seventeen'] = 'sE1v^ntin'
        self.translation_execptions['th'] = 'ti1eC'
        self.translation_execptions['thirteen'] = 'TR1tin'
        self.translation_execptions['tiki'] = 'ti1ki'
        self.translation_execptions['taiwan'] = 'tY1wan'
        self.translation_execptions['flintstone'] = 'flI1ntston'
        self.translation_execptions['mit'] = 'E1mYti'
        self.translation_execptions['oj'] = 'o1Je'
        self.translation_execptions['thankyou'] = 'T@1Gkyu'
        self.translation_execptions['pm'] = 'pi1Em'
        self.translation_execptions['cds'] = 'si1diz'
        self.translation_execptions['ls'] = 'E1lEs'
        self.translation_execptions['seventeenth'] = 'sE1v^ntinT'

        self.translation_execptions['overshadow'] = 'o1vRS@do'
        self.translation_execptions['unborn'] = '^1nbcrn'
        self.translation_execptions['straightforward'] = 'stre1tfcrwRd'
        self.translation_execptions['offbeat'] = 'c1fbit'
        self.translation_execptions['shortsighted'] = 'Sc1rtsYtId'
        self.translation_execptions['sightseeing'] = 'sY1tsiIG'
        self.translation_execptions['handmade'] = 'h@1ndmed'
        self.translation_execptions['unquote'] = '^1nkwot'
        self.translation_execptions['coronet'] = 'kc1r^nEt'
        self.translation_execptions['interrelationship'] = 'I1ntRrileS^nSIp'
        self.translation_execptions['homegrown'] = 'ho1mgron'
        self.translation_execptions['preexisting'] = 'pri1IgzIstIG'
        self.translation_execptions['infestation'] = 'InfE1steS^n'
        self.translation_execptions['yearlong'] = 'yI1rlcG'
        self.translation_execptions['bestseller'] = 'bE1stsElR'
        self.translation_execptions['archenemy'] = 'a1rCEn^mi'
        self.translation_execptions['prorate'] = 'pro1ret'
        self.translation_execptions['underwriting'] = '^1ndRrYtIG'
        self.translation_execptions['coeducational'] = 'koE1J^keS^n^l'
        self.translation_execptions['easygoing'] = 'i1zigoIG'
        self.translation_execptions['tightfisted'] = 'tY1tfIstId'
        self.translation_execptions['onetime'] = 'w^1ntYm'
        self.translation_execptions['amphitheater'] = '@1mf^TietR'
        self.translation_execptions['stateside'] = 'ste1tsYd'
        self.translation_execptions['otherworldly'] = '^1DRwRldli'
        self.translation_execptions['nonfarm'] = 'nanfa1rm'
        self.translation_execptions['overplay'] = 'o1vRple'
        self.translation_execptions['worthwhile'] = 'wR1TwYl'
        self.translation_execptions['misprint'] = 'mI1sprInt'
        self.translation_execptions['midwinter'] = 'mI1dwIntR'
        self.translation_execptions['headmaster'] = 'hE1dm@stR'
        self.translation_execptions['underestimate'] = '^ndRE1st^met'
        self.translation_execptions['regeneration'] = 'riJE1nReS^n'
        self.translation_execptions['wellborn'] = 'wE1lbcrn'
        self.translation_execptions['uncouth'] = '^nku1T'
        self.translation_execptions['backstage'] = 'b@1ksteJ'
        self.translation_execptions['ballyhoo'] = 'b@1lihu'
        self.translation_execptions['coagulation'] = 'ko@1gy^leS^n'
        self.translation_execptions['coaxial'] = 'ko@1ksi^l'
        self.translation_execptions['businessperson'] = 'bI1zn^spRs^n'
        self.translation_execptions['hospitable'] = 'ha1spIt^b^l'
        self.translation_execptions['retake'] = 'rite1k'
        self.translation_execptions['farsighted'] = 'fa1rsYt^d'
        self.translation_execptions['rerun'] = 'rir^1n'
        self.translation_execptions['bestselling'] = 'bE1stsElIG'
        self.translation_execptions['quicksilver'] = 'kwI1ksIlvR'
        self.translation_execptions['lightweight'] = 'lY1twet'
        self.translation_execptions['plainclothes'] = 'ple1nkloz'
        self.translation_execptions['retest'] = 'ritE1st'
        self.translation_execptions['forthright'] = 'fc1rTrYt'
        self.translation_execptions['draftee'] = 'dr@1fti'
        self.translation_execptions['sightseer'] = 'sY1tsiR'
        self.translation_execptions['overproduce'] = 'ovRpr^du1s'
        self.translation_execptions['archetypal'] = 'arktY1p^l'
        self.translation_execptions['overreact'] = 'ovRri@1kt'
        self.translation_execptions['outdoorsman'] = 'Wtdc1rzm^n'
        self.translation_execptions['nonnative'] = 'nane1tIv'
        self.translation_execptions['newfound'] = 'nu1fWnd'
        self.translation_execptions['engineering'] = 'E1nJ^nIrIG'
        self.translation_execptions['recheck'] = 'riCE1k'
        self.translation_execptions['franchisee'] = 'fr@1nCYzi'
        self.translation_execptions['overproduction'] = 'ovRpr^d^1kS^n'
        self.translation_execptions['handheld'] = 'h@1ndhEld'
        self.translation_execptions['goatee'] = 'go1ti'
        self.translation_execptions['miscalculation'] = 'mIsk@lky^le1S^n'
        self.translation_execptions['privatization'] = 'prY1v^t^zeS^n'
        self.translation_execptions['teleport'] = 'tE1l^pcrt'
        self.translation_execptions['downgrade'] = 'dW1ngred'
        self.translation_execptions['forthcoming'] = 'fc1rTk^mIG'
        self.translation_execptions['nearby'] = 'nI1rbY'
        self.translation_execptions['prefab'] = 'pri1f@b'
        self.translation_execptions['reattach'] = 'ri^t@1C'
        self.translation_execptions['postwar'] = 'po1stwcr'
        self.translation_execptions['overactive'] = 'ovR@1ktIv'
        self.translation_execptions['postnatal'] = 'postne1t^l'
        self.translation_execptions['overabundance'] = 'ovR^b^1nd^ns'
        self.translation_execptions['dislocation'] = 'dIsloke1S^n'
        self.translation_execptions['coworker'] = 'kowR1kR'
        self.translation_execptions['workaholic'] = 'wRk^ha1lIk'
        self.translation_execptions['whoopee'] = 'wu1pi'
        self.translation_execptions['radioactivity'] = 'redio@ktI1v^ti'
        self.translation_execptions['incantation'] = 'Ink@nte1S^n'
        self.translation_execptions['archdiocese'] = 'arCdY1^s^s'
        self.translation_execptions['transgender'] = 'tr@nzJE1ndR'
        self.translation_execptions['receptivity'] = 'risEptI1vIti'
        self.translation_execptions['rematch'] = 'rim@1C'
        self.translation_execptions['microcomputer'] = 'mYkrok^mpyu1tR'
        self.translation_execptions['handpick'] = 'h@1ndpIk'
        self.translation_execptions['oxymoron'] = 'aksimc1ran'
        self.translation_execptions['farfetched'] = 'fa1rfECt'
        self.translation_execptions['closeup'] = 'klo1s^p'
        self.translation_execptions['firstborn'] = 'fR1stbcrn'
        self.translation_execptions['inductee'] = 'Ind^kti1'
        self.translation_execptions['debutante'] = 'dE1by^tant'
        self.translation_execptions['midshipman'] = 'mIdSI1pm^n'
        self.translation_execptions['mankind'] = 'm@1nkYnd'
        self.translation_execptions['rechristen'] = 'rikrI1s^n'
        self.translation_execptions['guncotton'] = 'g^1nkat^n'
        self.translation_execptions['overdo'] = 'o1vRdu'
        self.translation_execptions['amputee'] = '@mpy^ti1'
        self.translation_execptions['overhear'] = 'o1vRhir'
        self.translation_execptions['duration'] = 'dUre1S^n'
        self.translation_execptions['smartass'] = 'sma1rt@s'
        self.translation_execptions['standby'] = 'st@1ndbY'
        self.translation_execptions['navigation'] = 'n@v^ge1S^n'
        self.translation_execptions['lowborn'] = 'lo1bcrn'
        self.translation_execptions['overdue'] = 'ovRdu1'
        self.translation_execptions['evenhanded'] = 'i1v^nh@ndId'
        self.translation_execptions['grandnephew'] = 'gr@1ndnEfyu'
        self.translation_execptions['downrange'] = 'dWnre1nJ'
        self.translation_execptions['microchip'] = 'mY1kroCIp'
        self.translation_execptions['misdeed'] = 'mIsdi1d'
        self.translation_execptions['archbishop'] = 'arCbI1S^p'
        self.translation_execptions['procreation'] = 'prokrie1S^n'
        self.translation_execptions['trainee'] = 'treni1'
        self.translation_execptions['shortwave'] = 'Sc1rtwev'
        self.translation_execptions['reactivate'] = 'ri@1kt^vet'
        self.translation_execptions['midseason'] = 'mIdsi1z^n'
        self.translation_execptions['overburden'] = 'ovRbR1d^n'
        self.translation_execptions['kowtow'] = 'kW1tW'
        self.translation_execptions['nondescript'] = 'nandIskrI1pt'
        self.translation_execptions['naturalization'] = 'n@1CR^l^zeS^n'
        self.translation_execptions['pussyfoot'] = 'pU1sifUt'
        self.translation_execptions['foregone'] = 'fcrgc1n'
        self.translation_execptions['widespread'] = 'wY1dsprEd'
        self.translation_execptions['midsummer'] = 'mIds^1mR'
        self.translation_execptions['artsy'] = 'a1rtsi'
        self.translation_execptions['circumnavigate'] = 'sRk^mn@1v^get'
        self.translation_execptions['hipbone'] = 'hI1pbon'
        self.translation_execptions['impregnation'] = 'ImprE1gneS^n'
        self.translation_execptions['nonbinding'] = 'nanbY1ndIG'
        self.translation_execptions['offshore'] = 'c1fScr'
        self.translation_execptions['freethinker'] = 'fri1TIGkR'
        self.translation_execptions['facedown'] = 'fe1sdWn'
        self.translation_execptions['sightsee'] = 'sY1tsi'
        self.translation_execptions['incarnation'] = 'Inka1rneS^n'
        self.translation_execptions['freemason'] = 'fri1mes^n'
        self.translation_execptions['overdrawn'] = 'o1vRdrcn'
        self.translation_execptions['nationwide'] = 'ne1S^nwYd'
        self.translation_execptions['grassroots'] = 'gr@1sruts'
        self.translation_execptions['ac'] = 'e1si'
        self.translation_execptions['overbearing'] = 'ovRbE1rIG'
        self.translation_execptions['overhead'] = 'ovRhE1d'
        self.translation_execptions['nonesuch'] = 'n^ns^1C'
        self.translation_execptions['midcourse'] = 'mIdkc1rs'
        self.translation_execptions['relocation'] = 'riloke1S^n'
        self.translation_execptions['motherfucker'] = 'm^DRf^1kR'
        self.translation_execptions['noncommittal'] = 'nank^mI1t^l'
        self.translation_execptions['videotape'] = 'vI1diotep'
        self.translation_execptions['fainthearted'] = 'fentha1rtId'
        self.translation_execptions['safekeeping'] = 'sefki1pIG'
        self.translation_execptions['overstock'] = 'ovRsta1k'
        self.translation_execptions['procreate'] = 'pro1kriet'
        self.translation_execptions['cofounder'] = 'kofW1ndR'
        self.translation_execptions['freemasonry'] = 'frime1s^nri'
        self.translation_execptions['reborn'] = 'ribc1rn'
        self.translation_execptions['proactive'] = 'pro@1ktIv'
        self.translation_execptions['forthrightness'] = 'fc1rTrYtn^s'
        self.translation_execptions['emcee'] = 'E1msi'
        self.translation_execptions['lukewarm'] = 'lu1kwcrm'
        self.translation_execptions['manmade'] = 'm@1nmed'
        self.translation_execptions['remake'] = 'rime1k'
        self.translation_execptions['nonfat'] = 'nanf@1t'
        self.translation_execptions['attendee'] = '^tEndi1'
        self.translation_execptions['backwoods'] = 'b@1kwUdz'
        self.translation_execptions['hardcore'] = 'ha1rdkcr'
        self.translation_execptions['rearm'] = 'ria1rm'
        self.translation_execptions['worldwide'] = 'wR1ldwYd'
        self.translation_execptions['wrongdoer'] = 'rc1GduR'
        self.translation_execptions['downhill'] = 'dW1nhIl'
        self.translation_execptions['nonchalance'] = 'nanS^la1ns'
        self.translation_execptions['pretax'] = 'prit@1ks'
        self.translation_execptions['vendee'] = 'vEndi1'
        self.translation_execptions['rustproof'] = 'r^1stpruf'
        self.translation_execptions['coauthor'] = 'koa1TR'
        self.translation_execptions['foursquare'] = 'fc1rskwEr'
        self.translation_execptions['lifelong'] = 'lY1flcG'
        self.translation_execptions['thoroughbred'] = 'TR1obrEd'
        self.translation_execptions['reread'] = 'riri1d'
        self.translation_execptions['gutsy'] = 'g^1tsi'
        self.translation_execptions['nonfatal'] = 'nanfe1t^l'
        self.translation_execptions['subcommittee'] = 's^bk^mI1ti'
        self.translation_execptions['stillborn'] = 'stI1lbcrn'
        self.translation_execptions['ceasefire'] = 'si1sfYR'
        self.translation_execptions['overseer'] = 'o1vRsiR'
        self.translation_execptions['nonevent'] = 'nanIvE1nt'
        self.translation_execptions['eyewitness'] = 'YwI1tn^s'
        self.translation_execptions['realization'] = 'ril^ze1S^n'
        self.translation_execptions['outspoken'] = 'Wtspo1k^n'
        self.translation_execptions['outdistance'] = 'WtdI1st^ns'
        self.translation_execptions['nonsmoking'] = 'nansmo1kIG'
        self.translation_execptions['shortsightedness'] = 'ScrtsY1tIdnIs'
        self.translation_execptions['handwoven'] = 'h@1ndwov^n'
        self.translation_execptions['retiree'] = 'ritYri1'
        self.translation_execptions['subchapter'] = 's^bC@1ptR'
        self.translation_execptions['actuary'] = '@1kCuEri'
        self.translation_execptions['purebred'] = 'pyU1rbrEd'
        self.translation_execptions['outdoors'] = 'W1tdcrz'
        self.translation_execptions['underhanded'] = '^ndRh@1ndId'
        self.translation_execptions['duodenal'] = 'du^di1n^l'
        self.translation_execptions['reactivated'] = 'ri@1kt^vetId'
        self.translation_execptions['overeating'] = 'ovRi1tIG'
        self.translation_execptions['hitherto'] = 'hI1DRtu'
        self.translation_execptions['overridden'] = 'ovRrI1d^n'
        self.translation_execptions['ranee'] = 'r@1ni'
        self.translation_execptions['thirteenth'] = 'TRti1nT'
        self.translation_execptions['uphill'] = '^phI1l'
        self.translation_execptions['impolitic'] = 'ImpclI1tIk'
        self.translation_execptions['underpaid'] = '^ndRpe1d'
        self.translation_execptions['coworkers'] = 'kowR1kRz'
        self.translation_execptions["baseball's"] ='be1sbclz'
        self.translation_execptions['longshoremen'] = 'lc1GScrmIn'
        self.translation_execptions['operationally'] = 'apRe1S^n^li'
        self.translation_execptions['henceforth'] = 'hE1nsfcrT'
        self.translation_execptions['outdistancing'] = 'WtdI1st^nsIG'
        self.translation_execptions['jaycee'] = 'Je1si'
        self.translation_execptions['enrollees'] = 'Enro1liz'
        self.translation_execptions['roughshod'] = 'r^1fSad'
        self.translation_execptions['inshore'] = 'I1nScr'
        self.translation_execptions['miscalculations'] = 'mIsk@lky^le1S^nz'
        self.translation_execptions['dislocations'] = 'dIsloke1S^nz'
        self.translation_execptions['draftees'] = 'dr@fti1z'
        self.translation_execptions['herewith'] = 'hI1rwIT'
        self.translation_execptions['overrode'] = 'ovRro1d'
        self.translation_execptions['overdone'] = 'ovRd^1n'
        self.translation_execptions['freethinkers'] = 'fri1TIGkRz'
        self.translation_execptions['overpaid'] = 'ovRpe1d'
        self.translation_execptions['rosettes'] = 'rozE1ts'
        self.translation_execptions['thereby'] = 'DE1rbY'
        self.translation_execptions['handymen'] = 'h@1ndimEn'
        self.translation_execptions['baseballs'] = 'be1sbclz'
        self.translation_execptions['overemphasized'] = 'ovRE1mf^sYzd'
        self.translation_execptions['addresses'] = '@drE1sIz'
        self.translation_execptions['durations'] = 'dUre1S^nz'
        self.translation_execptions['upstream'] = '^pstri1m'
        self.translation_execptions['tootsie'] = 'tu1tsi'
        self.translation_execptions['midshipmen'] = 'mIdSI1pmEn'
        self.translation_execptions['nonfood'] = 'nanfu1d'
        self.translation_execptions['overcame'] = 'ovRke1m'
        self.translation_execptions['uptown'] = '^ptW1n'
        self.translation_execptions['overran'] = 'ovRr@1n'
        self.translation_execptions['inductees'] = 'Ind^kti1z'
        self.translation_execptions['revaluation'] = 'riv@lyue1S^n'
        self.translation_execptions['excellency'] = 'E1kslEnsi'
        self.translation_execptions['actuate'] = '@1kCuet'
        self.translation_execptions['overplayed'] = 'ovRple1d'
        self.translation_execptions['downstream'] = 'dW1nstrim'
        self.translation_execptions['somewhat'] = 's^1mw^t'
        self.translation_execptions["mankind's"] ='m@1nkYndz'
        self.translation_execptions['miscount'] = 'mIskW1nt'
        self.translation_execptions['lawmen'] = 'lc1mEn'
        self.translation_execptions["longshoremen's"] ='lc1GScrmInz'
        self.translation_execptions['whereupon'] = 'wEr^pa1n'
        self.translation_execptions['redheads'] = 'rE1dhEdz'
        self.translation_execptions['engineers'] = 'EnJ^nI1rz'
        self.translation_execptions['upstate'] = '^pste1t'
        self.translation_execptions['closeups'] = 'klo1s^ps'
        self.translation_execptions['overdoing'] = 'o1vRduIG'
        self.translation_execptions['nonwhite'] = 'na1nwYt'
        self.translation_execptions['sightseers'] = 'sY1tsiRz'
        self.translation_execptions['devotees'] = 'dEv^ti1z'
        self.translation_execptions["rock'n'roll"] ='ra1k^nrol'
        self.translation_execptions['outdistanced'] = 'WtdI1st^nst'
        self.translation_execptions['peking'] = 'pi1kIG'
        self.translation_execptions['remaking'] = 'rime1kIG'
        self.translation_execptions['underestimated'] = '^ndRE1st^metId'
        self.translation_execptions['overheard'] = 'ovRhR1d'
        self.translation_execptions['overburdened'] = 'ovRbR1d^nd'
        self.translation_execptions['twofold'] = 'tu1fold'
        self.translation_execptions['forthrightly'] = 'fc1rTrYtli'
        self.translation_execptions['downgraded'] = 'dW1ngred^d'
        self.translation_execptions['offhand'] = 'c1fh@nd'
        self.translation_execptions['nondiscriminatory'] = 'nandIskrI1m^n^tcri'
        self.translation_execptions['overpowering'] = 'ovRpW1rIG'
        self.translation_execptions['outright'] = 'WtrY1t'
        self.translation_execptions['alongside'] = '^lc1GsYd'
        self.translation_execptions['overseas'] = 'ovRsi1z'
        self.translation_execptions['offstage'] = 'c1fsteJ'
        self.translation_execptions['headfirst'] = 'hE1dfRst'
        self.translation_execptions['landrover'] = 'l@1ndrovR'
        self.translation_execptions['nonwhites'] = 'nanwY1ts'
        self.translation_execptions['misprints'] = 'mIsprI1nts'
        self.translation_execptions['granduncles'] = 'gr@1nd^Gk^lz'
        self.translation_execptions['debutantes'] = 'dEby^ta1nts'
        self.translation_execptions['granduncle'] = 'gr@1nd^Gk^l'
        self.translation_execptions['jaycees'] = 'Je1siz'
        self.translation_execptions['videotaped'] = 'vI1diotept'
        self.translation_execptions['subcommittees'] = 's^bk^mI1tiz'
        self.translation_execptions['procreated'] = 'pro1kriet^d'
        self.translation_execptions['overshadowing'] = 'ovRS@1doIG'
        self.translation_execptions['kuomintang'] = 'kwo1mInt@G'
        self.translation_execptions['oilmen'] = 'O1lmEn'
        self.translation_execptions['forthwith'] = 'fc1rTwIT'
        self.translation_execptions['disputation'] = 'dIspyute1S^n'
        self.translation_execptions['coates'] = 'ko1ets'
        self.translation_execptions['outdistances'] = 'WtdI1st^nsIz'
        self.translation_execptions['pussyfoots'] = 'pU1sifUts'
        self.translation_execptions['oversold'] = 'ovRso1ld'
        self.translation_execptions['trainees'] = 'tre1niz'
        self.translation_execptions['outsides'] = 'W1tsYdz'
        self.translation_execptions['coauthors'] = 'koa1TRz'
        self.translation_execptions['ballcock'] = 'bc1lkak'
        self.translation_execptions['anchormen'] = '@1GkRmEn'
        self.translation_execptions['overplays'] = 'ovRple1z'
        self.translation_execptions['wrongdoers'] = 'rc1GduRz'
        self.translation_execptions['rerunning'] = 'rir^1nIG'
        self.translation_execptions['remakes'] = 'rime1ks'
        self.translation_execptions['overshadows'] = 'ovRS@1doz'
        self.translation_execptions['taiwanese'] = 'tY1waniz'
        self.translation_execptions['quintuplets'] = 'kwInt^1pl^ts'
        self.translation_execptions['umpteen'] = '^mpti1n'
        self.translation_execptions['sixteens'] = 'sI1kstinz'
        self.translation_execptions['procreates'] = 'pro1kriets'
        self.translation_execptions['overcharged'] = 'ovRCa1rJd'
        self.translation_execptions['upstaged'] = '^pste1Jd'
        self.translation_execptions['comiskey'] = 'komIski1'
        self.translation_execptions['eosinophilic'] = 'i^sIn^fI1lIk'
        self.translation_execptions['reactivating'] = 'ri@1ktIvetIG'
        self.translation_execptions['videotapes'] = 'vI1dioteps'
        self.translation_execptions['headmasters'] = 'hE1dm@stRz'
        self.translation_execptions['etcetera'] = 'EtsE1tR^'
        self.translation_execptions['stepchildren'] = 'stE1pCIldr^n'
        self.translation_execptions['precook'] = 'prikU1k'
        self.translation_execptions['microfossils'] = 'mYkrofa1s^lz'
        self.translation_execptions['overhears'] = 'ovRhi1rz'
        self.translation_execptions['rearming'] = 'ria1rmIG'
        self.translation_execptions['pussyfooting'] = 'pU1sifUtIG'
        self.translation_execptions['wentworth'] = 'wE1ntwRT'
        self.translation_execptions['overplaying'] = 'ovRple1IG'
        self.translation_execptions['overstocked'] = 'ovRsta1kt'
        self.translation_execptions['amphitheatre'] = '@mf^Tie1tR'
        self.translation_execptions['auctioneers'] = 'c1kS^nIrz'
        self.translation_execptions['amputees'] = '@mpy^ti1z'
        self.translation_execptions['quintuplet'] = 'kwInt^1pl^t'
        self.translation_execptions['procreating'] = 'pro1krietIG'
        self.translation_execptions['handpicked'] = 'h@1ndpIkt'
        self.translation_execptions['outdone'] = 'Wtd^1n'
        self.translation_execptions['musee'] = 'myu1zi'
        self.translation_execptions['thoroughbreds'] = 'TR1obrEdz'
        self.translation_execptions['fourfold'] = 'fc1rfold'
        self.translation_execptions['agee'] = 'e1Ji'
        self.translation_execptions['downgrades'] = 'dW1ngredz'
        self.translation_execptions['intermixing'] = 'IntRmI1ksIG'
        self.translation_execptions['cornfields'] = 'kc1rnfildz'
        self.translation_execptions['nonchalantly'] = 'nanS^la1ntli'
        self.translation_execptions['reruns'] = 'rir^1nz'
        self.translation_execptions['karlheinz'] = 'ka1rlhYnz'
        self.translation_execptions["hardee's"] ='ha1rdiz'
        self.translation_execptions['backwoodsman'] = 'b@kwU1dzm^n'
        self.translation_execptions['rustproofing'] = 'r^1stprufIG'
        self.translation_execptions['downgrading'] = 'dWngre1dIG'
        self.translation_execptions['fayette'] = 'feE1t'
        self.translation_execptions['cia'] = 'si1Ye'
        self.translation_execptions['dna'] = 'di1Ene'
        self.translation_execptions['shanghai'] = 'S@1GhY'
        self.translation_execptions['misprinted'] = 'mIsprI1nt^d'
        self.translation_execptions['satterfield'] = 's@1tRfild'
        self.translation_execptions['coronets'] = 'kc1r^nEts'
        self.translation_execptions['actuaries'] = '@1kCuEriz'
        self.translation_execptions['undervaluation'] = '^ndRv@lyue1S^n'
        self.translation_execptions['businesswomen'] = 'bI1zn^swom^n'
        self.translation_execptions['grandnephews'] = 'gr@1ndnEfyuz'
        self.translation_execptions['sixteenths'] = 'sI1kstinTs'
        self.translation_execptions['purebreds'] = 'pyU1rbrEdz'
        self.translation_execptions['pattee'] = 'p@1ti'
        self.translation_execptions['malloseismic'] = 'malosY1zmIk'
        self.translation_execptions['pawnees'] = 'pc1niz'
        self.translation_execptions['microsystems'] = 'mYkrosI1st^mz'
        self.translation_execptions['mph'] = 'E1mpieC'
        self.translation_execptions['pussyfooted'] = 'pU1sifUt^d'
        self.translation_execptions['realizations'] = 'ri1l^zeS^nz'
        self.translation_execptions['pc'] = 'pi1si'
        self.translation_execptions['ts'] = 'ti1Es'
        self.translation_execptions['retirees'] = 'ritY1riz'
        self.translation_execptions['metall'] = 'mE1tcl'
        self.translation_execptions['overspent'] = 'ovRspE1nt'
        self.translation_execptions['lp'] = 'E1lpi'
        self.translation_execptions['coauthoring'] = 'koa1TRIG'
        self.translation_execptions['grandmaster'] = 'gr@ndm@1stR'
        self.translation_execptions['rereading'] = 'riri1dIG'
        self.translation_execptions['tb'] = 'ti1bi'
        self.translation_execptions['overreacts'] = 'ovRri@1kts'
        self.translation_execptions['minivans'] = 'mIniv@1nz'
        self.translation_execptions['pawnee'] = 'pc1ni'
        self.translation_execptions['pyongyang'] = 'pyc1Gy@G'
        self.translation_execptions['bestsellers'] = 'bE1stsElRz'
        self.translation_execptions['meadowlands'] = 'mE1dol@ndz'
        self.translation_execptions['soco'] = 'so1ko'
        self.translation_execptions['coprocessors'] = 'kopra1sEsRz'
        self.translation_execptions['pitchmen'] = 'pI1CmEn'
        self.translation_execptions['renomination'] = 'rinam^ne1S^n'
        self.translation_execptions['fm'] = 'E1fEm'
        self.translation_execptions['dui'] = 'di1yuY'
        self.translation_execptions['abs'] = 'e1biEs'
        self.translation_execptions['mothballing'] = 'mc1TbclIG'
        self.translation_execptions['ph'] = 'pi1eC'
        self.translation_execptions['microchips'] = 'mYkroCI1ps'
        self.translation_execptions['motherfuckers'] = 'm^DRf^1kRz'
        self.translation_execptions['dillydally'] = 'dI1lid@li'
        self.translation_execptions['predates'] = 'pri1dets'
        self.translation_execptions['nonnatives'] = 'nane1tIvz'
        self.translation_execptions['overproduced'] = 'ovRpr^du1st'
        self.translation_execptions['microcomputers'] = 'mYkrok^mpyu1tRz'
        self.translation_execptions['vietcong'] = 'viE1tkcG'
        self.translation_execptions['attendees'] = '^tE1ndiz'
        self.translation_execptions['ballcocks'] = 'bc1lkaks'
        self.translation_execptions['coauthored'] = 'koa1TRd'
        self.translation_execptions['landsat'] = 'l@1nds@t'
        self.translation_execptions['cc'] = 'si1si'
        self.translation_execptions['razzmatazz'] = 'r@1zm^t@z'
        self.translation_execptions['asap'] = 'e1Esepi'
        self.translation_execptions['usa'] = 'yu1Ese'
        self.translation_execptions['dk'] = 'di1ke'
        self.translation_execptions['yangtze'] = 'y@1Gktsi'
        self.translation_execptions['overbuilt'] = 'ovRbI1lt'
        self.translation_execptions['reattached'] = 'ri^t@1Ct'
        self.translation_execptions['overripe'] = 'ovRrY1p'
        self.translation_execptions['mpg'] = 'E1mpiJi'
        self.translation_execptions['oad'] = 'o1edi'
        self.translation_execptions['councilmen'] = 'kW1ns^lmEn'
        self.translation_execptions['thirteenths'] = 'TR1tinTs'
        self.translation_execptions['rpm'] = 'a1rpiEm'
        self.translation_execptions['bt'] = 'bi1ti'
        self.translation_execptions['excellencies'] = 'E1kslEnsiz'
        self.translation_execptions['bellyaching'] = 'bE1liekIG'
        self.translation_execptions['overmatched'] = 'ovRm@1Ct'
        self.translation_execptions['ws'] = 'd^1b^lyuEs'

    def orthographic_with_phonological(self, orthwords):
        # returns the set of orthographic words that have a phonological_transformation translation
        # in the CMU pronunciation dictionary

        all_phonwords = set(self.CMU.keys())
        phonwords = all_phonwords & orthwords
        return phonwords

    def orth_to_phon(self,word):
        # returns the phonological_transformation translation of an orthographic form
        def double_check(trans):
            ones = len(re.findall("1",trans))
            if ones > 1:
                print("self.translation_execptions['", word, "'] ='", self.CMU[word], "'", sep="")
            elif ones < 1:
                print("self.translation_execptions['", word, "'] ='", self.CMU[word], "'", sep="")

        if word in self.CMU:
            #print(word)
            ones = len(re.findall("1",self.CMU[word]))
            if ones > 1:
                if not word in self.translation_execptions:
                    print("self.translation_execptions['", word, "'] ='", self.CMU[word], "'", sep="")
            elif ones < 1:
                if not word in self.translation_execptions:
                    print("self.translation_execptions['", word, "'] ='", self.CMU[word], "'", sep="")
            # returns the appropriate word
            if word in self.translation_execptions:
                double_check(self.translation_execptions[word])
                return self.translation_execptions[word]
            else:
                return self.CMU[word]
        else:
            if self.surpress_error:
                print(word,'not in CMU')
            return 'ERROR-PHONOLOGICAL TRANSLATOR: '+word

    def find_multiple_stress(self):
        # finds words with multiple primary stress markings to be
        # able to put them into the translation exceptions
        for orth,phon in self.CMU.items():
            if len(re.findall("1",phon))> 1:
                print(orth,phon)

if __name__ == "__main__":
    T = PhonologicalFromOrthographic()
    T.find_multiple_stress()

