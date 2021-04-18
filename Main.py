"""
Main.py
Author: Elliot Davis

This file implements the Incognito algorithm and the Samariti algorithm, it contains a function to calculate the
k value of a given data set

"""
import copy

from ColumnConversion import createTempDataframe, updateDataframe
from GraphGeneration import latticeGraph
from LatticeGeneration import generateLatticeNodes, generateLatticeEdges
import time
from KValue import readHeader, datasetDF

"""
TODO:
Incognito not marking all nodes if kvalue true - not necessary
generate edges in pruned genLattice - not necessary


Columns: 'Name','Age','Sex','Address','Party','Postcode'
Dimension table: current requirements
Name: P0 (name), P1 (-)
Age: P0 (original), P1 (5 age range), P2 (10 age range), P3 (20 age range)
Sex: P0 (male/female), P1 (-)
Address: P0 (address), P1 (-)
Party: P0 (important info)
Postcode: P0 (original), P1 (First 3 letters), P2 (First 2 Letters)
"""


def samarati():
    nodes = []
    nodes = generateLatticeNodes(quasiIdentifiers, nodes)
    heightArray = []

    for node in nodes[0]:
        height = 0
        for index in range(1, len(node), 2):  # iterates through all the possible next node ids
            height += int(node[index])
        heightArray.append(height)
    heightSet = list(set([i for i in heightArray]))

    low = heightSet[0]
    high = heightSet[-1]
    while low < high:
        mid = round((low+high)/2)
        found = False

        for i in range(len(heightArray)):
            if heightArray[i] == mid:
                dimDataframe = updateDataframe(nodes[0][i], suppress, numeric, shorten)
                kValue = frequencySet(dimDataframe)

                if kValue >= kanonymity:
                    solution = copy.deepcopy(dimDataframe)
                    solutionKValue = kValue
                    found = True
                    break

        if found:
            high = mid - 1

        else:
            low = mid + 1

    print(solution)
    print(solutionKValue)
    print("--- %s seconds ---" % (time.time() - start_time))


def incognito():
    nodes = []
    for columnNames in incognitoAttributeList:  # Generates list of all potential nodes
        nodes = generateLatticeNodes(columnNames, nodes)
    E = generateLatticeEdges(nodes)

    queue = []
    fullDomainList = []  # List for all nodes which meet requirements

    for i, j in zip(nodes, E):
        # i is the nodes of the original lattice, j is the edges of the original lattice
        S = i[:]  # nodes of current lattice
        SE = j[:]  # edges of current lattice
        queue.append(S[0])
        visited = []

        while queue:
            node = queue[0]
            queue.pop(0)

            if node not in visited:
                dimDataframe = createTempDataframe(node, suppress, numeric, shorten)  # returns dimDataframe
                kValue = frequencySet(dimDataframe)  # returns KValue
                # Compute frequency set by replacing values in i in original table

                if kValue >= kanonymity:
                    # if meets kanonymity requirement then add direct generalizations to visited

                    # If it matches, add it to visited queue and visited
                    visitedQueue = [i.index(S[0])]
                    visited.append(S[0])
                    S.pop(0)

                    #  visited queue = searching through the parent nodes
                    while visitedQueue:
                        index = visitedQueue[0]
                        visitedQueue.pop(0)

                        for edge in SE:
                            if edge[0] == index and i[edge[1] - 1] not in visited:
                                visited.append(i[edge[1] - 1])
                                visitedQueue.append(i.index(i[edge[1] - 1]) + 1)

                    if len(S) > 0:
                        queue.append(S[0])

                else:
                    # if kvalue false then search through rest of lattice by height, removing edges along the way
                    index = i.index(S[0]) + 1
                    SE[:] = [edge for edge in SE if index != edge[0]]
                    S.pop(0)
                    if len(S) > 0:
                        queue.append(S[0])

        fullDomainList.append(visited)
    graphGen(fullDomainList)


# Generates all potential full domain generalizations which meet kanonymity requirement
def graphGen(nodeList):
    genLattice = []
    for firstNode in nodeList[0]:  # Adds first set of nodes to list
        genLattice.append(firstNode)
    nodeList.pop(0)

    for nodes in nodeList[:-1]:  # For all the other nodes
        for node in nodes:  # For each node
            for lat in genLattice:  # For each item in current list (lat) check the following
                if lat[-1] == node[1] and lat[-2] == node[0]:  # Check if matching nodes have matching dimensions
                    lat.append(node[2])
                    lat.append(node[3])
                # Check if names are matching but numbers are different, create new node if so
                if lat[-4] == node[0] and lat[-3] == node[1] and lat[-2] == node[2] and lat[-1] != node[3]:
                    newLat = lat[:]
                    newLat[-1] = node[3]
                    genLattice.append(newLat)

    # Print all full domain generalisations
    for node in genLattice:
        dimDataframe = updateDataframe(node, suppress, numeric, shorten)
        kValue = frequencySet(dimDataframe)

        if kValue >= kanonymity:
            print(node)
            print(dimDataframe)
            print(kValue)
    print("--- %s seconds ---" % (time.time() - start_time))


def simpleSearch():
    C = []
    C = generateLatticeNodes(quasiIdentifiers, C)

    for node in C[0]:  # For each potential node in lattice
        # Node are ordered by height
        dimDataframe = updateDataframe(node, suppress, numeric, shorten)
        kValue = frequencySet(dimDataframe)
        if kValue >= kanonymity:  # If a node meets requirements, print and break
            print(dimDataframe)
            print(kValue)
            print("--- %s seconds ---" % (time.time() - start_time))
            break


# Returns k-value (how secure the dataset is)
def frequencySet(dataframe):
    KValue = dataframe.groupby(list(dataframe.columns)).size().reset_index(name='Count')
    KValue = KValue['Count'].min()
    return KValue


if __name__ == '__main__':
    start_time = time.time()
    kanonymity = 2
    lines = readHeader()

    suppress = []
    numeric = []
    shorten = []
    quasiIdentifiers = []
    # Strips the newline character
    for line in lines:
        line = line.split()
        if line[1] == "{}":
            suppress.append(line[0])
            supList = [[line[0], 0],[line[0], 1]]
            quasiIdentifiers.append(supList)
        if line[1] == "NUMERIC":
            numeric.append(line[0])
            numList = [[line[0], 0], [line[0], 1], [line[0], 2]]
            quasiIdentifiers.append(numList)
        if line[1] == "SHORTEN":
            shorten.append(line[0])
            shortList = [[line[0], 0], [line[0], 1], [line[0], 2]]
            quasiIdentifiers.append(shortList)

    #print(suppress, numeric, shorten)
    #print(quasiIdentifiers)
    #print(datasetDF)


    # # # Voterlist data set
    # name = [["Name", 0], ["Name", 1]]
    # sex = [["Sex", 0], ["Sex", 1]]
    # address = [["Address", 0], ["Address", 1]]
    # age = [["Age", 0], ["Age", 1], ["Age", 2], ["Age", 3]]
    # postcode = [["Postcode", 0], ["Postcode", 1], ["Postcode", 2], ["Postcode", 3]]
    #
    # # Extra attributes for medical list data set
    # patientID = [["Patient ID", 0], ["Patient ID", 1]]
    # weight = [["Weight (kg)", 0], ["Weight (kg)", 1], ["Weight (kg)", 2]]
    # treatment = [["Treatment", 0], ["Treatment", 1]]
    #
    # incognitoAttributeList = [[name, sex], [sex, address], [address, age], [age, postcode], [postcode, name]]
    # quasiIdentifiers = [name, sex, address, age, postcode]
    # print(quasiIdentifiers)


    #incognito()
    samarati()
    # simpleSearch()

    # # Census income data set
    # age = [["Age", 0], ["Age", 1], ["Age", 2], ["Age", 3]]
    # class_of_worker = [["class_of_worker", 0], ["class_of_worker", 1]]
    # detailed_industry_recode = [["detailed_industry_recode", 0], ["detailed_industry_recode", 1]]
    # detailed_occupation_recode = [["detailed_occupation_recode", 0], ["detailed_occupation_recode", 1]]
    # education = [["education", 0], ["education", 1]]
    # wage_per_hour  = [["wage_per_hour", 0], ["wage_per_hour", 1]]
    # enroll_in_edu_inst_last_wk = [["enroll_in_edu_inst_last_wk", 0], ["enroll_in_edu_inst_last_wk", 1]]
    # marital_stat = [["marital_stat", 0], ["marital_stat", 1]]
    # major_industry_code = [["major_industry_code", 0], ["major_industry_code", 1]]
    # major_occupation_code = [["major_occupation_code", 0], ["major_occupation_code", 1]]
    # race = [["race", 0], ["race", 1]]
    # hispanic_origin = [["hispanic_origin", 0], ["hispanic_origin", 1]]
    # sex = [["sex", 0], ["sex", 1]]
    # member_of_a_labor_union = [["member_of_a_labor_union", 0], ["member_of_a_labor_union", 1]]
    # reason_for_unemployment = [["reason_for_unemployment", 0], ["reason_for_unemployment", 1]]
    # full_or_part_time_employment_stat = [["full_or_part_time_employment_stat", 0], ["full_or_part_time_employment_stat", 1]]
    # capital_gains = [["capital_gains", 0], ["capital_gains", 1]]
    # capital_losses = [["capital_losses", 0], ["capital_losses", 1]]
    # dividends_from_stocks = [["dividends_from_stocks", 0], ["dividends_from_stocks", 1]]
    # tax_filer_stat = [["tax_filer_stat", 0], ["tax_filer_stat", 1]]
    # region_of_previous_residence = [["region_of_previous_residence", 0], ["region_of_previous_residence", 1]]
    # state_of_previous_residence = [["state_of_previous_residence", 0], ["state_of_previous_residence", 1]]
    # detailed_household_and_family_stat = [["detailed_household_and_family_stat", 0], ["detailed_household_and_family_stat", 1]]
    # detailed_household_summary_in_household = [["detailed_household_summary_in_household", 0], ["detailed_household_summary_in_household", 1]]
    # instance_weight = [["instance_weight", 0], ["instance_weight", 1]]
    # migration_code_change_in_msa = [["migration_code_change_in_msa", 0], ["migration_code_change_in_msa", 1]]
    # migration_code_change_in_reg = [["migration_code_change_in_reg", 0], ["migration_code_change_in_reg", 1]]
    # migration_code_move_within_reg = [["migration_code_move_within_reg", 0], ["migration_code_move_within_reg", 1]]
    # live_in_this_house_1_year_ago = [["live_in_this_house_1_year_ago", 0], ["live_in_this_house_1_year_ago", 1]]
    # migration_prev_res_in_sunbelt = [["migration_prev_res_in_sunbelt", 0], ["migration_prev_res_in_sunbelt", 1]]
    # num_persons_worked_for_employer = [["num_persons_worked_for_employer", 0], ["num_persons_worked_for_employer", 1]]
    # family_members_under_18 = [["family_members_under_18", 0], ["family_members_under_18", 1]]
    # country_of_birth_father = [["country_of_birth_father", 0], ["country_of_birth_father", 1]]
    # country_of_birth_mother = [["country_of_birth_mother", 0], ["country_of_birth_mother", 1]]
    # country_of_birth_self = [["country_of_birth_self", 0], ["country_of_birth_self", 1]]
    # citizenship = [["citizenship", 0], ["citizenship", 1]]
    # own_business_or_self_employed = [["own_business_or_self_employed", 0], ["own_business_or_self_employed", 1]]
    # fill_inc_questionnaire_for_veterans_admin = [["fill_inc_questionnaire_for_veterans_admin", 0], ["fill_inc_questionnaire_for_veterans_admin", 1]]
    # veterans_benefits = [["veterans_benefits", 0], ["veterans_benefits", 1]]
    # weeks_worked_in_year = [["weeks_worked_in_year", 0], ["weeks_worked_in_year", 1]]
    # year = [["year", 0], ["year", 1]]
    # classN = [["classN", 0], ["classN", 1]]
    #
    # # incognitoAttributeList = [[name, sex], [sex, address], [address, age], [age, postcode], [postcode, name]]
    # quasiIdentifiers = [age, class_of_worker, detailed_industry_recode, detailed_occupation_recode, education,
    #                     wage_per_hour, enroll_in_edu_inst_last_wk, marital_stat, major_industry_code,
    #                     major_occupation_code, race, hispanic_origin, sex, member_of_a_labor_union,
    #                     reason_for_unemployment, full_or_part_time_employment_stat, capital_gains, capital_losses,
    #                     dividends_from_stocks, tax_filer_stat, region_of_previous_residence,
    #                     state_of_previous_residence, detailed_household_and_family_stat,
    #                     detailed_household_summary_in_household, instance_weight, migration_code_change_in_msa,
    #                     migration_code_change_in_reg, migration_code_move_within_reg, live_in_this_house_1_year_ago,
    #                     migration_prev_res_in_sunbelt, num_persons_worked_for_employer, family_members_under_18,
    #                     country_of_birth_father, country_of_birth_mother, country_of_birth_self, citizenship,
    #                     own_business_or_self_employed, fill_inc_questionnaire_for_veterans_admin, veterans_benefits,
    #                     weeks_worked_in_year, year, classN]
    # # quasiIdentifiers = [patientID, age, sex, weight, treatment, postcode]
    # kanonymity = 2
    # latticeGraph()
    # #incognito()
    # #samarati()
    # # simpleSearch()
