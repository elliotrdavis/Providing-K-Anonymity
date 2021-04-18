"""
GraphGeneration.py
Author: Elliot Davis

This file generates a graph representing the generalization lattice for the respective dataset

"""

import networkx as nx
from matplotlib import pyplot as plt
from LatticeGeneration import generateLatticeNodes, generateLatticeEdges


def latticeGraph():
    G = nx.Graph()

    age = [["Age", 0], ["Age", 1], ["Age", 2], ["Age", 3]]
    class_of_worker = [["class_of_worker", 0], ["class_of_worker", 1]]
    detailed_industry_recode = [["detailed_industry_recode", 0], ["detailed_industry_recode", 1]]
    detailed_occupation_recode = [["detailed_occupation_recode", 0], ["detailed_occupation_recode", 1]]
    education = [["education", 0], ["education", 1]]
    wage_per_hour = [["wage_per_hour", 0], ["wage_per_hour", 1]]
    enroll_in_edu_inst_last_wk = [["enroll_in_edu_inst_last_wk", 0], ["enroll_in_edu_inst_last_wk", 1]]
    marital_stat = [["marital_stat", 0], ["marital_stat", 1]]
    major_industry_code = [["major_industry_code", 0], ["major_industry_code", 1]]
    major_occupation_code = [["major_occupation_code", 0], ["major_occupation_code", 1]]
    race = [["race", 0], ["race", 1]]
    hispanic_origin = [["hispanic_origin", 0], ["hispanic_origin", 1]]
    sex = [["sex", 0], ["sex", 1]]
    member_of_a_labor_union = [["member_of_a_labor_union", 0], ["member_of_a_labor_union", 1]]
    reason_for_unemployment = [["reason_for_unemployment", 0], ["reason_for_unemployment", 1]]
    full_or_part_time_employment_stat = [["full_or_part_time_employment_stat", 0],
                                         ["full_or_part_time_employment_stat", 1]]
    capital_gains = [["capital_gains", 0], ["capital_gains", 1]]
    capital_losses = [["capital_losses", 0], ["capital_losses", 1]]
    dividends_from_stocks = [["dividends_from_stocks", 0], ["dividends_from_stocks", 1]]
    tax_filer_stat = [["tax_filer_stat", 0], ["tax_filer_stat", 1]]
    region_of_previous_residence = [["region_of_previous_residence", 0], ["region_of_previous_residence", 1]]
    state_of_previous_residence = [["state_of_previous_residence", 0], ["state_of_previous_residence", 1]]
    detailed_household_and_family_stat = [["detailed_household_and_family_stat", 0],
                                          ["detailed_household_and_family_stat", 1]]
    detailed_household_summary_in_household = [["detailed_household_summary_in_household", 0],
                                               ["detailed_household_summary_in_household", 1]]
    instance_weight = [["instance_weight", 0], ["instance_weight", 1]]
    migration_code_change_in_msa = [["migration_code_change_in_msa", 0], ["migration_code_change_in_msa", 1]]
    migration_code_change_in_reg = [["migration_code_change_in_reg", 0], ["migration_code_change_in_reg", 1]]
    migration_code_move_within_reg = [["migration_code_move_within_reg", 0], ["migration_code_move_within_reg", 1]]
    live_in_this_house_1_year_ago = [["live_in_this_house_1_year_ago", 0], ["live_in_this_house_1_year_ago", 1]]
    migration_prev_res_in_sunbelt = [["migration_prev_res_in_sunbelt", 0], ["migration_prev_res_in_sunbelt", 1]]
    num_persons_worked_for_employer = [["num_persons_worked_for_employer", 0], ["num_persons_worked_for_employer", 1]]
    family_members_under_18 = [["family_members_under_18", 0], ["family_members_under_18", 1]]
    country_of_birth_father = [["country_of_birth_father", 0], ["country_of_birth_father", 1]]
    country_of_birth_mother = [["country_of_birth_mother", 0], ["country_of_birth_mother", 1]]
    country_of_birth_self = [["country_of_birth_self", 0], ["country_of_birth_self", 1]]
    citizenship = [["citizenship", 0], ["citizenship", 1]]
    own_business_or_self_employed = [["own_business_or_self_employed", 0], ["own_business_or_self_employed", 1]]
    fill_inc_questionnaire_for_veterans_admin = [["fill_inc_questionnaire_for_veterans_admin", 0],
                                                 ["fill_inc_questionnaire_for_veterans_admin", 1]]
    veterans_benefits = [["veterans_benefits", 0], ["veterans_benefits", 1]]
    weeks_worked_in_year = [["weeks_worked_in_year", 0], ["weeks_worked_in_year", 1]]
    year = [["year", 0], ["year", 1]]
    classN = [["classN", 0], ["classN", 1]]

    # incognitoAttributeList = [[name, sex], [sex, address], [address, age], [age, postcode], [postcode, name]]
    quasiIdentifiers = [age, class_of_worker, detailed_industry_recode, detailed_occupation_recode, education,
                        wage_per_hour, enroll_in_edu_inst_last_wk, marital_stat, major_industry_code,
                        major_occupation_code, race, hispanic_origin, sex, member_of_a_labor_union,
                        reason_for_unemployment, full_or_part_time_employment_stat, capital_gains, capital_losses,
                        dividends_from_stocks, tax_filer_stat, region_of_previous_residence,
                        state_of_previous_residence, detailed_household_and_family_stat,
                        detailed_household_summary_in_household, instance_weight, migration_code_change_in_msa,
                        migration_code_change_in_reg, migration_code_move_within_reg, live_in_this_house_1_year_ago,
                        migration_prev_res_in_sunbelt, num_persons_worked_for_employer, family_members_under_18,
                        country_of_birth_father, country_of_birth_mother, country_of_birth_self, citizenship,
                        own_business_or_self_employed, fill_inc_questionnaire_for_veterans_admin, veterans_benefits,
                        weeks_worked_in_year, year, classN]
    C = []
    C = generateLatticeNodes(quasiIdentifiers, C)
    E = generateLatticeEdges(C)

    for node in C:
        string = ''.join(node)
        G.add_node(string)

    for edge in E:
        edge1 = C[edge[0]-1]
        edge2 = C[edge[1]-1]
        edge1String = ''.join(edge1)
        edge2String = ''.join(edge2)
        edge3 = (edge1String, edge2String)
        G.add_edge(*edge3)

    nx.draw(G,with_labels=False)
    plt.savefig("Graphs/incognito2attr.png")  # save as png
    plt.show()  # display
