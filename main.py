# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from functions import *

BIBS = dict(
    AGORA=['AGORA Silent Study 1_01', 'AGORA Silent Study 1_02', 'AGORA Silent Study 1_03', 'AGORA Silent Study 1_04',
           'AGORA Silent Study 1_05', 'AGORA Silent Study 1_06', 'AGORA Silent Study 1_07', 'AGORA Silent Study 1_08',
           'AGORA Silent Study 1_09', 'AGORA Silent Study 1_10', 'AGORA Silent Study 1_11', 'AGORA Silent Study 1_12',
           'AGORA Silent Study 1_13', 'AGORA Silent Study 1_14', 'AGORA Silent Study 1_15', 'AGORA Silent Study 1_16',
           'AGORA Silent Study 1_17', 'AGORA Silent Study 1_18', 'AGORA Silent Study 1_19', 'AGORA Silent Study 1_20',
           'AGORA Silent Study 1_21', 'AGORA Silent Study 1_22', 'AGORA Silent Study 1_23', 'AGORA Silent Study 1_24',
           'AGORA Silent Study 1_25', 'AGORA Silent Study 1_26', 'AGORA Silent Study 1_27', 'AGORA Silent Study 1_28',
           'AGORA Silent Study 1_29', 'AGORA Silent Study 1_30', 'AGORA Silent Study 1_31', 'AGORA Silent Study 1_32',
           'AGORA Silent Study 2_01', 'AGORA Silent Study 2_02', 'AGORA Silent Study 2_03', 'AGORA Silent Study 2_04',
           'AGORA Silent Study 2_05', 'AGORA Silent Study 2_06', 'AGORA Silent Study 2_07', 'AGORA Silent Study 2_08',
           'AGORA Silent Study 2_09', 'AGORA Silent Study 2_10', 'AGORA Silent Study 2_11', 'AGORA Silent Study 2_12',
           'AGORA Silent Study 2_13', 'AGORA Silent Study 2_14', 'AGORA Silent Study 2_15', 'AGORA Silent Study 2_16',
           'AGORA Silent Study 2_17', 'AGORA Silent Study 2_18', 'AGORA Silent Study 2_19', 'AGORA Silent Study 2_20',
           'AGORA Silent Study 2_21', 'AGORA Silent Study 2_22', 'AGORA Silent Study 2_23', 'AGORA Silent Study 2_24',
           'AGORA Silent Study 2_25', 'AGORA Silent Study 2_26', 'AGORA Silent Study 2_27', 'AGORA Silent Study 2_28',
           'AGORA Silent Study 2_29', 'AGORA Silent Study 2_30', 'AGORA Silent Study 2_31', 'AGORA Silent Study 2_32',
           'AGORA Silent Study 2_33', 'AGORA Silent Study 2_34', 'AGORA Silent Study 2_35', 'AGORA Silent Study 2_36',
           'AGORA Silent Study 2_37', 'AGORA Silent Study 2_38', 'AGORA Silent Study 2_39', 'AGORA Silent Study 2_40',
           'AGORA Silent Study 2_41', 'AGORA Silent Study 2_42', 'AGORA Silent Study 2_43', 'AGORA Silent Study 2_44',
           'AGORA FlexiSpace 01_Seat 01 (interactive)', 'AGORA FlexiSpace 01_Seat 02 (interactive)',
           'AGORA FlexiSpace 01_Seat 03 (interactive)', 'AGORA FlexiSpace 01_Seat 04 (interactive)',
           'AGORA FlexiSpace 01_Seat 05 (interactive)', 'AGORA FlexiSpace 02_Seat 01 (interactive)',
           'AGORA FlexiSpace 02_Seat 02 (interactive)', 'AGORA FlexiSpace 02_Seat 03 (interactive)',
           'AGORA FlexiSpace 02_Seat 04 (interactive)', 'AGORA FlexiSpace 02_Seat 05 (interactive)',
           'AGORA FlexiSpace 03_Seat 01 (interactive)', 'AGORA FlexiSpace 03_Seat 02 (interactive)',
           'AGORA FlexiSpace 03_Seat 03 (interactive)', 'AGORA FlexiSpace 03_Seat 04 (interactive)',
           'AGORA FlexiSpace 03_Seat 05 (interactive)', 'AGORA FlexiSpace 04_Seat 01 (interactive)',
           'AGORA FlexiSpace 04_Seat 02 (interactive)', 'AGORA FlexiSpace 04_Seat 03 (interactive)',
           'AGORA FlexiSpace 04_Seat 04 (interactive)', 'AGORA FlexiSpace 04_Seat 05 (interactive)',
           'AGORA FlexiSpace 05_Seat 01 (interactive)', 'AGORA FlexiSpace 05_Seat 02 (interactive)',
           'AGORA FlexiSpace 05_Seat 03 (interactive)', 'AGORA FlexiSpace 05_Seat 04 (interactive)',
           'AGORA FlexiSpace 05_Seat 05 (interactive)', 'AGORA FlexiSpace 06_Seat 01 (interactive)',
           'AGORA FlexiSpace 06_Seat 02 (interactive)', 'AGORA FlexiSpace 06_Seat 03 (interactive)',
           'AGORA FlexiSpace 06_Seat 04 (interactive)', 'AGORA FlexiSpace 06_Seat 05 (interactive)',
           'AGORA FlexiSpace 07_Seat 01 (interactive)', 'AGORA FlexiSpace 07_Seat 02 (interactive)',
           'AGORA FlexiSpace 07_Seat 03 (interactive)', 'AGORA FlexiSpace 07_Seat 04 (interactive)',
           'AGORA FlexiSpace 07_Seat 05 (interactive)', 'AGORA FlexiSpace 08_Seat 01 (interactive)',
           'AGORA FlexiSpace 08_Seat 02 (interactive)', 'AGORA FlexiSpace 08_Seat 03 (interactive)',
           'AGORA FlexiSpace 08_Seat 04 (interactive)', 'AGORA FlexiSpace 08_Seat 05 (interactive)'],
    ALMA1=['Alma 1 Seat 101', 'Alma 1 Seat 102', 'Alma 1 Seat 103', 'Alma 1 Seat 104', 'Alma 1 Seat 105',
           'Alma 1 Seat 106', 'Alma 1 Seat 107', 'Alma 1 Seat 108', 'Alma 1 Seat 109', 'Alma 1 Seat 110',
           'Alma 1 Seat 111', 'Alma 1 Seat 112', 'Alma 1 Seat 113', 'Alma 1 Seat 114', 'Alma 1 Seat 115',
           'Alma 1 Seat 116', 'Alma 1 Seat 117', 'Alma 1 Seat 118', 'Alma 1 Seat 119', 'Alma 1 Seat 120',
           'Alma 1 Seat 121', 'Alma 1 Seat 122', 'Alma 1 Seat 123', 'Alma 1 Seat 124', 'Alma 1 Seat 125',
           'Alma 1 Seat 126', 'Alma 1 Seat 127', 'Alma 1 Seat 128', 'Alma 1 Seat 129', 'Alma 1 Seat 130',
           'Alma 1 Seat 131', 'Alma 1 Seat 132', 'Alma 1 Seat 133', 'Alma 1 Seat 134', 'Alma 1 Seat 201',
           'Alma 1 Seat 202', 'Alma 1 Seat 203', 'Alma 1 Seat 204', 'Alma 1 Seat 205', 'Alma 1 Seat 206',
           'Alma 1 Seat 207', 'Alma 1 Seat 208', 'Alma 1 Seat 209', 'Alma 1 Seat 210', 'Alma 1 Seat 211',
           'Alma 1 Seat 212', 'Alma 1 Seat 213', 'Alma 1 Seat 301', 'Alma 1 Seat 302', 'Alma 1 Seat 303',
           'Alma 1 Seat 304', 'Alma 1 Seat 401', 'Alma 1 Seat 402', 'Alma 1 Seat 403', 'Alma 1 Seat 404',
           'Alma 1 Seat 405', 'Alma 1 Seat 406', 'Alma 1 Seat 407', 'Alma 1 Seat 408', 'Alma 1 Seat 409',
           'Alma 1 Seat 410', 'Alma 1 Seat 411', 'Alma 1 Seat 412', 'Alma 1 Seat 413', 'Alma 1 Seat 414',
           'Alma 1 Seat 415', 'Alma 1 Seat 416', 'Alma 1 Seat 417', 'Alma 1 Seat 418', 'Alma 1 Seat 419'],
    CBA=['CBA Study deleVille Seat 002', 'CBA Study deleVille Seat 004', 'CBA Study deleVille Seat 006',
         'CBA Study deleVille Seat 008', 'CBA Study deleVille Seat 010', 'CBA Study deleVille Seat 012',
         'CBA Study deleVille Seat 014', 'CBA Study Zolder Seat 075', 'CBA Study Zolder Seat 077',
         'CBA Study Zolder Seat 079', 'CBA Study Zolder Seat 081', 'CBA Study Zolder Seat 083',
         'CBA Study Zolder Seat 085', 'CBA Study Zolder Seat 087', 'CBA Study Zolder Seat 089',
         'CBA Study Zolder Seat 091', 'CBA Study Zolder Seat 093', 'CBA Study Zolder Seat 095',
         'CBA Study Zolder Seat 097', 'CBA Study Zolder Seat 099', 'CBA Study Zolder Seat 101',
         'CBA Study Zolder Seat 103', 'CBA Study Zolder Seat 105', 'CBA Study Zolder Seat 107',
         'CBA Study Zolder Seat 109', 'CBA Study Zolder Seat 111', 'CBA Study Zolder Seat 113',
         'CBA Study Zolder Seat 115', 'CBA Study Zolder Seat 117', 'CBA Study Zolder Seat 119',
         'CBA Study Zolder Seat 121', 'CBA Study Zolder Seat 123', 'CBA Collection Boekenzaal Seat 061',
         'CBA Collection Boekenzaal Seat 062', 'CBA Collection Boekenzaal Seat 063',
         'CBA Collection Boekenzaal Seat 064', 'CBA Collection Boekenzaal Seat 065',
         'CBA Collection Boekenzaal Seat 066', 'CBA Collection Boekenzaal Seat 067',
         'CBA Collection Boekenzaal Seat 068', 'CBA Collection Boekenzaal Seat 069',
         'CBA Collection Boekenzaal Seat 070', 'CBA Collection PC Boekenzaal Seat 071',
         'CBA Collection PC Boekenzaal Seat 072', 'CBA Collection PC Boekenzaal Seat 073', 'CBA Study Zolder Seat 074',
         'CBA Study Zolder Seat 076', 'CBA Study Zolder Seat 078', 'CBA Study Zolder Seat 080',
         'CBA Study Zolder Seat 082', 'CBA Study Zolder Seat 084', 'CBA Study Zolder Seat 086',
         'CBA Study Zolder Seat 088', 'CBA Study Zolder Seat 090', 'CBA Study Zolder Seat 092',
         'CBA Study Zolder Seat 094', 'CBA Study Zolder Seat 096', 'CBA Study Zolder Seat 098',
         'CBA Study Zolder Seat 100', 'CBA Study Zolder Seat 102', 'CBA Study Zolder Seat 104',
         'CBA Study Zolder Seat 106', 'CBA Study Zolder Seat 108', 'CBA Study Zolder Seat 110',
         'CBA Study Zolder Seat 112', 'CBA Study Zolder Seat 114', 'CBA Study Zolder Seat 116',
         'CBA Study Zolder Seat 118', 'CBA Study Zolder Seat 120', 'CBA Study Zolder Seat 122',
         'CBA Collection Boekenzaal Seat 215', 'CBA Collection Boekenzaal Seat 216', 'CBA Study Leeszaal Seat 129',
         'CBA Study Leeszaal Seat 130', 'CBA Study Leeszaal Seat 131', 'CBA Study Leeszaal Seat 132',
         'CBA Study Leeszaal Seat 133', 'CBA Study Leeszaal Seat 134', 'CBA Study Leeszaal Seat 135',
         'CBA Study Leeszaal Seat 136', 'CBA Study Leeszaal Seat 137', 'CBA Study Leeszaal Seat 138',
         'CBA Study Leeszaal Seat 139', 'CBA Study Leeszaal Seat 140', 'CBA Study Leeszaal Seat 141',
         'CBA Study Leeszaal Seat 142', 'CBA Study Leeszaal Seat 143', 'CBA Study Leeszaal Seat 144',
         'CBA Study Leeszaal Seat 145', 'CBA Study Leeszaal Seat 146', 'CBA Study Leeszaal Seat 147',
         'CBA Study Leeszaal Seat 148', 'CBA Study Leeszaal Seat 149', 'CBA Study Leeszaal Seat 150',
         'CBA Study PC Leeszaal Seat 124', 'CBA Study PC Leeszaal Seat 125', 'CBA Study PC Leeszaal Seat 126',
         'CBA Study deleVille Seat 001', 'CBA Study deleVille Seat 003', 'CBA Study deleVille Seat 005',
         'CBA Study deleVille Seat 007', 'CBA Study deleVille Seat 009', 'CBA Study deleVille Seat 011',
         'CBA Study deleVille Seat 013', 'CBA Study deleVille Seat 015', 'CBA Study deTulp Seat 016',
         'CBA Study deTulp Seat 017', 'CBA Study deTulp Seat 018', 'CBA Study deTulp Seat 019',
         'CBA Study deTulp Seat 020', 'CBA Study deTulp Seat 021', 'CBA Study deTulp Seat 022',
         'CBA Study deTulp Seat 023', 'CBA Study deTulp Seat 024', 'CBA Study deTulp Seat 025',
         'CBA Study deTulp Seat 026', 'CBA Study deTulp Seat 027', 'CBA Study deTulp Seat 028',
         'CBA Study deTulp Seat 029', 'CBA Study deTulp Seat 030', 'CBA Study deTulp Seat 031',
         'CBA Study deTulp Seat 032', 'CBA Study deTulp Seat 033', 'CBA Study deTulp Seat 034',
         'CBA Study deTulp Seat 035', 'CBA Study deTulp Seat 036', 'CBA Study deTulp Seat 037',
         'CBA Study deTulp Seat 038', 'CBA Study deTulp Seat 039', 'CBA Study deTulp Seat 040',
         'CBA Study deTulp Seat 041', 'CBA Study deTulp Seat 042', 'CBA Study deTulp Seat 043',
         'CBA Study deTulp Seat 044', 'CBA Study deTulp Seat 045'],
    EBIB=['EBIB Quiet Study Seat S002', 'EBIB Quiet Study Seat S006', 'EBIB Quiet Study Seat S010',
          'EBIB Quiet Study Seat S012', 'EBIB Quiet Study Seat S015', 'EBIB Quiet Study Seat S017',
          'EBIB Quiet Study Seat S020', 'EBIB Quiet Study Seat S022', 'EBIB Quiet Study Seat S029',
          'EBIB Quiet Study Seat S032', 'EBIB Quiet Study Seat S034', 'EBIB Quiet Study Seat S038',
          'EBIB Quiet Study Seat S042', 'EBIB Quiet Study Seat S046', 'EBIB Quiet Study Seat S052',
          'EBIB Quiet Study Seat S054', 'EBIB Quiet Study Seat S055', 'EBIB Quiet Study Seat S057',
          'EBIB Quiet Sudy Seat S060', 'EBIB Quiet Study Seat S061', 'EBIB Quiet Study Seat S063',
          'EBIB Quiet Study Seat S064', 'EBIB Quiet Study Seat S066', 'EBIB Quiet Study Seat S070',
          'EBIB Quiet Study Seat S072', 'EBIB Quiet Study Seat S074', 'EBIB Quiet Study Seat S078',
          'EBIB Quiet Study Seat S084', 'EBIB Quiet Study Seat S088', 'EBIB Quiet Study Seat S094',
          'EBIB Quiet Study Seat S098', 'EBIB Quiet Study Seat S102', 'EBIB Quiet Study Seat S109',
          'EBIB Quiet Study Seat S113', 'EBIB Quiet Study Seat S114', 'EBIB Quiet Study Seat S116',
          'EBIB Quiet Study Seat S118', 'EBIB Quiet Study Seat S120', 'EBIB Quiet Study Seat S124',
          'EBIB Quiet Study Seat S127', 'EBIB Quiet Study Seat S129', 'EBIB Quiet Study Seat S131',
          'EBIB Deloitte Seat S01', 'EBIB Deloitte Seat S05', 'EBIB Deloitte Seat S09', 'EBIB Deloitte Seat S13',
          'EBIB Deloitte Seat S17', 'EBIB ResLab Seat S001', 'EBIB ResLab Seat S005', 'EBIB ResLab Seat S009',
          'EBIB ResLab Seat S013', 'EBIB ResLab Seat S017', 'EBIB Kelder/basement Seat S01',
          'EBIB Kelder/basement Seat S05', 'EBIB Kelder/basement Seat S09', 'EBIB Kelder/basement Seat S13',
          'EBIB Kelder/basement Seat S17', 'EBIB Leuven BIBSEM5 Seat 001', 'EBIB Leuven BIBSEM5 Seat 002',
          'EBIB Leuven BIBSEM5 Seat 003', 'EBIB Leuven BIBSEM5 Seat 004', 'EBIB Leuven BIBSEM5 Seat 005',
          'EBIB Leuven Flexispace Seat 001', 'EBIB Leuven Flexispace Seat 003', 'EBIB Leuven Flexispace Seat 005',
          'EBIB Leuven Flexispace Seat 007', 'EBIB Leuven Flexispace Seat 009', 'EBIB Leuven Flexispace Seat 011',
          'EBIB Leuven Flexispace Seat 013', 'EBIB Leuven Flexispace Seat 015', 'EBIB Leuven Flexispace Seat 017',
          'EBIB Leuven Flexispace Seat 019', 'EBIB Leuven Flexispace Seat 021', 'EBIB Leuven Flexispace Seat 023',
          'EBIB Leuven Flexispace Seat 025', 'EBIB Leuven Flexispace Seat 027', 'EBIB Leuven Flexispace Seat 029',
          'EBIB Leuven Flexispace Seat 031', 'EBIB Leuven Flexispace Seat 033', 'EBIB Leuven Flexispace Seat 035',
          'EBIB Leuven Flexispace Seat 037', 'EBIB Leuven Flexispace Seat 039', 'EBIB Leuven Flexispace Seat 041',
          'EBIB Collection consult - STATA PC room Seat 001', 'EBIB Collection consult - STATA PC room Seat 002',
          'EBIB Collection consult - STATA PC room Seat 003', 'EBIB Collection consult - STATA PC room Seat 004',
          'EBIB Collection consult - STATA PC room Seat 005', 'EBIB Collection consult - STATA PC room Seat 006',
          'EBIB Collection consult - STATA PC room Seat 007', 'EBIB Collection consult - STATA PC room Seat 008',
          'EBIB Collection consult - STATA PC room Seat 009', 'EBIB Collection consult - STATA PC room Seat 010',
          'EBIB ResLab Seat S021', 'EBIB ResLab Seat S022', 'EBIB ResLab Seat S023', 'EBIB ResLab Seat S024',
          'EBIB ResLab Seat S025', 'EBIB ResLab Seat S026'],
    FAC=['FAC Study Seat 001', 'FAC Study Seat 002', 'FAC Study Seat 003', 'FAC Study Seat 004', 'FAC Study Seat 005',
         'FAC Study Seat 006', 'FAC Study Seat 007', 'FAC Study Seat 008', 'FAC Study Seat 009', 'FAC Study Seat 010',
         'FAC Study Seat 011', 'FAC Study Seat 012', 'FAC Study Seat 013', 'FAC Study Seat 014', 'FAC Study Seat 015',
         'FAC Study Seat 016', 'FAC Study Seat 017', 'FAC Study Seat 018', 'FAC Study Seat 019', 'FAC Study Seat 020',
         'FAC Study Seat 021', 'FAC Study Seat 022', 'FAC Study Seat 023', 'FAC Study Seat 024', 'FAC Study Seat 025',
         'FAC Study Seat 026', 'FAC Study Seat 027', 'FAC Study Seat 028', 'FAC Study Seat 029', 'FAC Study Seat 030',
         'FAC Study Seat 031', 'FAC Study Seat 032', 'FAC Study Seat 033', 'FAC Study Seat 034', 'FAC Study Seat 035',
         'FAC Study Seat 036', 'FAC Study Seat 037', 'FAC Study Seat 038', 'FAC Study Seat 039', 'FAC Study Seat 040',
         'FAC Study Seat 041', 'FAC Study Seat 042', 'FAC Study Seat 043', 'FAC Study Seat 044', 'FAC Study Seat 045',
         'FAC Study Seat 046', 'FAC Study Seat 047', 'FAC Study Seat 048', 'FAC Study Seat 049', 'FAC Study Seat 050',
         'FAC Study Seat 051', 'FAC Study Seat 052', 'FAC Study Seat 053', 'FAC Study Seat 055', 'FAC Study Seat 056',
         'FAC Study Seat 057', 'FAC Study Seat 058', 'FAC Study Seat 059', 'FAC Study Seat 060', 'FAC Study Seat 061',
         'FAC Study Seat 062', 'FAC Study Seat 063', 'FAC Study Seat 064', 'FAC Study Seat 065', 'FAC Study Seat 066',
         'FAC Study Seat 067', 'FAC Study Seat 068', 'FAC Study Seat 069', 'FAC Study Seat 070', 'FAC Study Seat 071',
         'FAC Study Seat 072', 'FAC Study Seat 073', 'FAC Study Seat 074', 'FAC Study Seat 075', 'FAC Study Seat 076',
         'FAC Study Seat 077', 'FAC Study Seat 078', 'FAC Study Seat 079', 'FAC Study Seat 080', 'FAC Study Seat 081',
         'FAC Study Seat 082', 'FAC Study Seat 083', 'FAC Study Seat 084', 'FAC Study Seat 085', 'FAC Study Seat 086',
         'FAC Study Seat 087', 'FAC Study Seat 088', 'FAC Study Seat 089', 'FAC Study Seat 090', 'FAC Study Seat 091',
         'FAC Study Seat 092', 'FAC Study Seat 093', 'FAC Study Seat 094', 'FAC Study Seat 095', 'FAC Study Seat 096',
         'FAC Study Seat 097', 'FAC Study Seat 098', 'FAC Study Seat 099', 'FAC Study Seat 100', 'FAC Study Seat 101',
         'FAC Study Seat 102', 'FAC Study Seat 103', 'FAC Study Seat 104'],
    LDC=['LDC Study Leeszaal Seat 004', 'LDC Study Flex Seat 011', 'LDC Study Flex Seat 013', 'LDC Study Flex Seat 015',
         'LDC Study Flex Seat 017', 'LDC Study Flex Seat 019', 'LDC Study Flex Seat 021', 'LDC Study Flex Seat 023',
         'LDC Study Flex Seat 025', 'LDC Study Flex Seat 027', 'LDC Study Flex Seat 029', 'LDC Study Flex Seat 031',
         'LDC Study Inkom Seat 044', 'LDC Study Inkom Seat 045', 'LDC Study Inkom Seat 046', 'LDC Study Inkom Seat 047',
         'LDC Study Inkom Seat 048', 'LDC Study Inkom Seat 049', 'LDC Study Inkom Seat 050', 'LDC Study Inkom Seat 051',
         'LDC Study Inkom Seat 052', 'LDC Study Inkom Seat 053', 'LDC Collection PC inkom Seat 061',
         'LDC Collection PC inkom Seat 062', 'LDC Collection Leeszaal Seat 063', 'LDC Collection Leeszaal Seat 064',
         'LDC Collection Leeszaal Seat 065', 'LDC Study Leeszaal Seat 081', 'LDC Study Leeszaal Seat 083',
         'LDC Study Leeszaal Seat 085', 'LDC Study Leeszaal Seat 087', 'LDC Study Leeszaal Seat 089',
         'LDC Study Leeszaal Seat 091'],
    PBIB=['PBIB Study Seat 001', 'PBIB Study Seat 004', 'PBIB Study Seat 005', 'PBIB Study Seat 008',
          'PBIB Study Seat 009', 'PBIB Study Seat 012', 'PBIB Study Seat 013', 'PBIB Study Seat 016',
          'PBIB Study Seat 017', 'PBIB Study Seat 020', 'PBIB Study Seat 021', 'PBIB Study Seat 024',
          'PBIB Study Seat 025', 'PBIB Study Seat 028', 'PBIB Study Seat 029', 'PBIB Study Seat 032',
          'PBIB Study Seat 033', 'PBIB Study Seat 036', 'PBIB Study Seat 037', 'PBIB Study Seat 040',
          'PBIB Collection Consult Seat 053', 'PBIB Collection Consult Seat 054', 'PBIB Collection Consult Seat 055',
          'PBIB Collection Consult Seat 056', 'PBIB Collection Consult Seat 057', 'PBIB Group Work Table 01',
          'PBIB Group Work Table 02', 'PBIB Group Work Table 03', 'PBIB Group Work Table 04',
          'PBIB Group Work Table 05', 'PBIB Group Work Table 06', 'PBIB Group Work Table 07',
          'PBIB Group Work Table 08', 'PBIB Group Work Table 09', 'PBIB Group Work Table 10',
          'PBIB Group Work Table 11', 'PBIB Group Work Table 12', 'PBIB Group Work Table 13',
          'PBIB Group Work Table 14', 'PBIB Group Work Table 15', 'PBIB Group Work Table 16',
          'PBIB Group Work Table 17', 'PBIB Group Work Table 18', 'PBIB Group Work Table 19',
          'PBIB Group Work Table 20', 'PBIB Group Work Table 07 + Covat', 'PBIB Group Work Table 08 + Covat',
          'PBIB Group Work Table 09 + Covat', 'PBIB Group Work Table 10 + Covat', 'PBIB Group Work Table 11 + Covat',
          'PBIB Group Work Table 12 + Covat', 'PBIB Group Work Table 01 + Covat', 'PBIB Group Work Table 02 + Covat',
          'PBIB Group Work Table 03 + Covat'],
    RBIB=['RBIB 1A/01', 'RBIB 1A/02', 'RBIB 1A/03', 'RBIB 1A/04', 'RBIB 1A/05', 'RBIB 1A/06', 'RBIB 1A/07',
          'RBIB 1A/08', 'RBIB 1A/09', 'RBIB 1A/10', 'RBIB 1A/11', 'RBIB 1B Seat 012', 'RBIB 1B Seat 013',
          'RBIB 1B Seat 014', 'RBIB 1B Seat 015', 'RBIB 1B Seat 016', 'RBIB 1B Seat 017', 'RBIB 1B Seat 018',
          'RBIB 1B Seat 019', 'RBIB 1B Seat 020', 'RBIB 1B Seat 021', 'RBIB 1B Seat 022', 'RBIB 1B Seat 023',
          'RBIB 1B Seat 024', 'RBIB 1B Seat 025', 'RBIB 1B Seat 026', 'RBIB 1B Seat 027', 'RBIB 1B Seat 028',
          'RBIB 2A Seat 033', 'RBIB 2A Seat 034', 'RBIB 2A Seat 035', 'RBIB 2A Seat 036', 'RBIB 2B Seat 037',
          'RBIB 2B Seat 038', 'RBIB 2B Seat 039', 'RBIB 2B Seat 040', 'RBIB 2B Seat 041', 'RBIB 2B Seat 042',
          'RBIB 2B Seat 043', 'RBIB 2B Seat 044', 'RBIB 2B Seat 045', 'RBIB 2B Seat 046', 'RBIB 2B Seat 047',
          'RBIB 2B Seat 048', 'RBIB 2B Seat 049', 'RBIB 2B Seat 050', 'RBIB 2B Seat 051', 'RBIB 2B Seat 052',
          'RBIB 2B+ Seat 063', 'RBIB 2B+ Seat 064', 'RBIB 2C Seat 053', 'RBIB 2C Seat 054', 'RBIB 2C Seat 055',
          'RBIB 2C Seat 056', 'RBIB 2C Seat 057', 'RBIB 2C Seat 058', 'RBIB 2C Seat 059', 'RBIB 2C Seat 060',
          'RBIB 2C Seat 061', 'RBIB 2C Seat 062', 'RBIB Research Space Seat 001', 'RBIB Research Space Seat 002',
          'RBIB Research Space Seat 003', 'RBIB Research Space Seat 004', 'RBIB Research Space Seat 005',
          'RBIB Research Space Seat 006', 'RBIB Research Space Seat 007', 'RBIB Research Space Seat 008',
          'RBIB Research Space Seat 009', 'RBIB Research Space Seat 010', 'RBIB Research Space Seat 011',
          'RBIB Research Space Seat 012', 'RBIB 3 HIS Seat 065', 'RBIB 3 HIS Seat 066', 'RBIB 3 HIS Seat 067',
          'RBIB 3 HIS Seat 068', 'RBIB 3 HIS Seat 069', 'RBIB 3 HIS Seat 070', 'RBIB 3 HIS Seat 071',
          'RBIB 3 HIS Seat 072', 'RBIB 3 HIS Seat 073', 'RBIB 3 HIS Seat 074', 'RBIB 3 HIS Seat 075',
          'RBIB 3 HIS Seat 079', 'RBIB 3 HIS Seat 080', 'RBIB 3 HIS Seat 081', 'RBIB 3 HIS Seat 082',
          'RBIB 3 HIS Seat 083', 'RBIB 3 HIS Seat 084', 'RBIB 3 HIS Seat 085', 'RBIB 3 HIS Seat 086'],
    SBIB=['SBIB Researchers Seat 01', 'SBIB Researchers Seat 02', 'SBIB Researchers Seat 03',
          'SBIB Researchers Seat 04', 'SBIB Researchers Seat 05', 'SBIB Researchers Seat 06', 'SBIB Seat Sociol 053',
          'SBIB Seat Sociol 054', 'SBIB Seat Sociol 055', 'SBIB Seat Sociol 056', 'SBIB Seat Sociol 057',
          'SBIB Seat Sociol 058', 'SBIB Seat Polit 044', 'SBIB Seat Sociol 047', 'SBIB Seat Sociol 048',
          'SBIB Seat Sociol 049', 'SBIB Seat Sociol 050', 'SBIB Seat Sociol 051', 'SBIB Seat Sociol 052',
          'SBIB Infodesk Seat 033', 'SBIB Infodesk Seat 029', 'SBIB Infodesk Seat 030', 'SBIB Infodesk Seat 031',
          'SBIB Infodesk Seat 032', 'SBIB PC-Room Seat 059', 'SBIB PC-Room Seat 060', 'SBIB PC-Room Seat 061',
          'SBIB PC-Room Seat 062', 'SBIB PC-Room Seat 063', 'SBIB PC-Room Seat 064', 'SBIB PC-Room Seat 065'])

from PyQt5 import QtCore, QtWidgets, QtGui
import pandas as pd

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(object):
    def __init__(self):
        self.Times = list()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 340)
        MainWindow.setProperty("QtCore.Qt.AA_EnableHighDpiScaling", True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setIndent(3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        today = QtCore.QDate.currentDate()
        self.dateEdit.setDate(today.addDays(2))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 1, 1, 1)
        self.PWinput = QtWidgets.QLineEdit(self.centralwidget)
        self.PWinput.setObjectName("PWinput")
        self.PWinput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.PWinput, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setIndent(3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setIndent(3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.USERinput = QtWidgets.QLineEdit(self.centralwidget)
        self.USERinput.setObjectName("USERinput")
        self.gridLayout.addWidget(self.USERinput, 0, 1, 1, 1)
        self.zitinput = QtWidgets.QComboBox(self.centralwidget)
        self.zitinput.setObjectName("comboBox_2")
        self.zitinput.addItems(BIBS["AGORA"])
        self.gridLayout.addWidget(self.zitinput, 3, 1, 1, 1)
        self.USERlabel = QtWidgets.QLabel(self.centralwidget)
        self.USERlabel.setIndent(3)
        self.USERlabel.setObjectName("USERlabel")
        self.gridLayout.addWidget(self.USERlabel, 0, 0, 1, 1)
        self.bibinput = QtWidgets.QComboBox(self.centralwidget)
        self.bibinput.setObjectName("bibinput")
        self.bibinput.addItems(list(BIBS.keys()))
        self.bibinput.currentTextChanged.connect(self._updateZitplaatsen)
        self.gridLayout.addWidget(self.bibinput, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setIndent(3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setIndent(3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 5, 0, 1, 1)
        self.PWlabel = QtWidgets.QLabel(self.centralwidget)
        self.PWlabel.setIndent(3)
        self.PWlabel.setObjectName("PWlabel")
        self.gridLayout.addWidget(self.PWlabel, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit_3.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_3.setTime(QtCore.QTime(13, 0, 0))
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.gridLayout_2.addWidget(self.timeEdit_3, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit_4.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_4.setTime(QtCore.QTime(17, 0, 0))
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.gridLayout_2.addWidget(self.timeEdit_4, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.timeEdit_6 = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit_6.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_6.setTime(QtCore.QTime(22, 0, 0))
        self.timeEdit_6.setObjectName("timeEdit_6")
        self.gridLayout_2.addWidget(self.timeEdit_6, 3, 1, 1, 1, QtCore.Qt.AlignRight)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit_2.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_2.setTime(QtCore.QTime(12, 0, 0))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout_2.addWidget(self.timeEdit_2, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.timeEdit_5 = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit_5.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_5.setTime(QtCore.QTime(18, 0, 0))
        self.timeEdit_5.setObjectName("timeEdit_5")
        self.gridLayout_2.addWidget(self.timeEdit_5, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.timeEdit_1 = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit_1.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_1.setTime(QtCore.QTime(8, 0, 0))
        self.timeEdit_1.setObjectName("timeEdit_1")
        self.gridLayout_2.addWidget(self.timeEdit_1, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addWidget(self.groupBox, 5, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("F*ck KURT")
        self.buttonBox.clicked.connect(self._lets_GO)
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.Times.extend((self.timeEdit_1, self.timeEdit_2, self.timeEdit_3, self.timeEdit_4, self.timeEdit_5, self.timeEdit_6))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("F*ck KURT", "F*ck KURT"))
        self.label_2.setText(_translate("MainWindow", "Zitje"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.label_3.setText(_translate("MainWindow", "Datum"))
        self.label.setText(_translate("MainWindow", "Bib"))
        self.USERlabel.setText(_translate("MainWindow", "Gebruikersnaam"))
        self.label_4.setText(_translate("MainWindow", "Tijdsloten"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:6pt; font-style:italic;\">(01:00 voor leeg)</span></p></body></html>"))
        self.PWlabel.setText(_translate("MainWindow", "Wachtwoord"))
        self.label_7.setText(_translate("MainWindow", "Einde"))
        self.timeEdit_3.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.toolButton.setText(_translate("MainWindow", "+"))
        self.timeEdit_4.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.timeEdit_6.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.timeEdit_2.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.timeEdit_5.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.label_6.setText(_translate("MainWindow", "Begin"))
        self.timeEdit_1.setDisplayFormat(_translate("MainWindow", "hh:mm"))
        self.timeEdit_6.setDisplayFormat(_translate("MainWindow", "hh:mm"))

    def _updateZitplaatsen(self, text):
        self.zitinput.clear()
        self.zitinput.addItems(BIBS[text])

    def _get_seat_num(self):
        filename = str(self.bibinput.currentText()) + ".csv"
        index = self.zitinput.currentIndex()
        location = ('seat_lists/'+filename)
        df = pd.read_csv(location, delimiter=",", header=None)
        print(df.iloc[index, 0])
        return df.iloc[index, 0]

    def _get_time_windows(self):
        time_windows = list()
        zero_str = ":00:00"
        for i in range(0, 5, 2):
            this_time = self.Times[i]
            if this_time.time().toString()[:-6] == "01":
                pass
            else:
                time_windows.append([self.Times[i].time().toString()[:-6]+zero_str,
                                     self.Times[i+1].time().toString()[:-6]+zero_str])
        return time_windows

    def _test(self):
        print(str(self.dateEdit.date().toPyDate()))

    def _lets_GO(self):
        username = self.USERinput.text()
        password = self.PWinput.text()
        times = self._get_time_windows()
        seat = str(self._get_seat_num())
        date = str(self.dateEdit.date().toPyDate()) # bv. '2020-12-30'
        subject = "Study"

        driver = webdriver.Chrome('driver/chromedriver.exe')
        driver.implicitly_wait(5)
        login(driver, username, password)

        for time in times:
            reserve(driver, date, time, seat, subject)

        driver.quit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('favicon-1.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
