import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
import time
import random


def noun_scraper(link):
    url = link
    response = requests.get(url)

    singularAbsolute = None
    pluralAbsolute = None
    singularConstruct = None
    pluralConstruct = None

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    try:
        absolute_singulars = table.find(
            'div', {'id': 's'}).find_all('span', class_='menukad')
        singularAbsolute = absolute_singulars[-1].text
    except:
        print("There is no absolute singular")

    try:
        absolute_plurals = table.find(
            'div', {'id': 'p'}).find_all('span', class_='menukad')
        pluralAbsolute = absolute_plurals[-1].text
    except:
        print("There is no absolue pulral")

    try:
        construct_singulars = table.find(
            'div', {'id': 'sc'}).find_all('span', class_='menukad')
        singularConstruct = construct_singulars[-1].text
    except:
        print("There is no singular construct")

    try:
        construct_plurals = table.find(
            'div', {'id': 'pc'}).find_all('span', class_='menukad')
        pluralConstruct = construct_plurals[-1].text
    except:
        print("There is no plural construct")

    return (singularAbsolute, pluralAbsolute, singularConstruct, pluralConstruct)


def adjective_scraper(link):
    url = link
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('tbody')

    SM = None
    SF = None
    PM = None
    PF = None

    try:
        SM = table.find('div', {'id': 'ms-a'}
                        ).find_all('span', class_='menukad')[-1].text
    except:
        print(" There is no SM ")
    try:
        SF = table.find('div', {'id': 'fs-a'}
                        ).find_all('span', class_='menukad')[-1].text
    except:
        print(" There is no SF ")
    try:
        PM = table.find('div', {'id': 'mp-a'}
                        ).find_all('span', class_='menukad')[-1].text
    except:
        print(" There is no PM ")
    try:
        PF = table.find('div', {'id': 'fp-a'}
                        ).find_all('span', class_='menukad')[-1].text
    except:
        print(" There is no PF ")

    return(SM, SF, PM, PF)


def verb_scraper(link):
    url = link
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('tbody')

    ActivePresentSM = None
    ActivePresentSF = None
    ActivePresentPM = None
    ActivePresentPF = None

    ActivePastS1 = None
    ActivePastP1 = None
    ActivePastSM2 = None
    ActivePastSF2 = None
    ActivePastPM2 = None
    ActivePastPF2 = None
    ActivePastSM3 = None
    ActivePastSF3 = None
    ActivePastPM3 = None
    ActivePastPF3 = None

    ActiveFutureS1 = None
    ActiveFutureP1 = None
    ActiveFutureSM2 = None
    ActiveFutureSF2 = None
    ActiveFuturePM2 = None
    ActiveFuturePF2 = None
    ActiveFutureSM3 = None
    ActiveFutureSF3 = None
    ActiveFuturePM3 = None
    ActiveFuturePF3 = None

    ImperativeSM = None
    ImperativeSF = None
    ImperativePM = None
    ImperativePF = None

    PassivePresentSM = None
    PassivePresentSF = None
    PassivePresentPM = None
    PassivePresentPF = None

    PassivePastS1 = None
    PassivePastP1 = None
    PassivePastSM2 = None
    PassivePastSF2 = None
    PassivePastPM2 = None
    PassivePastPF2 = None
    PassivePastSM3 = None
    PassivePastSF3 = None
    PassivePastPM3 = None
    PassivePastPF3 = None

    PassiveFutureS1 = None
    PassiveFutureP1 = None
    PassiveFutureSM2 = None
    PassiveFutureSF2 = None
    PassiveFuturePM2 = None
    PassiveFuturePF2 = None
    PassiveFutureSM3 = None
    PassiveFutureSF3 = None
    PassiveFuturePM3 = None
    PassiveFuturePF3 = None

    # First scrape Active conjugations
    # Present
    try:
        ActivePresentSM = tables[0].find(
            'div', {'id': 'AP-ms'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePresentSM")
    try:
        ActivePresentSF = tables[0].find(
            'div', {'id': 'AP-fs'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePresentSF")
    try:
        ActivePresentPM = tables[0].find(
            'div', {'id': 'AP-mp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePresentSF")
    try:
        ActivePresentPF = tables[0].find(
            'div', {'id': 'AP-fp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePresentSF")

    # Past1
    try:
        ActivePastS1 = tables[0].find(
            'div', {'id': 'PERF-1s'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastS1")
    try:
        ActivePastP1 = tables[0].find(
            'div', {'id': 'PERF-1p'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastP1")

    # Past2
    try:
        ActivePastSM2 = tables[0].find(
            'div', {'id': 'PERF-2ms'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastSM2")
    try:
        ActivePastSF2 = tables[0].find(
            'div', {'id': 'PERF-2fs'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastSF2")
    try:
        ActivePastPM2 = tables[0].find(
            'div', {'id': 'PERF-2mp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastPM2")
    try:
        ActivePastPF2 = tables[0].find(
            'div', {'id': 'PERF-2fp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastPF2")

    # Past3
    try:
        ActivePastSM3 = tables[0].find(
            'div', {'id': 'PERF-3ms'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastSM3")
    try:
        ActivePastSF3 = tables[0].find(
            'div', {'id': 'PERF-3fs'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastSF3")
    try:
        ActivePastPM3 = tables[0].find(
            'div', {'id': 'PERF-3p'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastPM3")
    try:
        ActivePastPF3 = tables[0].find(
            'div', {'id': 'PERF-3p'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActivePastPF3")

    # Future1
    try:
        ActiveFutureS1 = tables[0].find(
            'div', {'id': 'IMPF-1s'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFutureS1")
    try:
        ActiveFutureP1 = tables[0].find(
            'div', {'id': 'IMPF-1p'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFutureP1")

    # Future2
    try:
        ActiveFutureSM2 = tables[0].find(
            'div', {'id': 'IMPF-2ms'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFutureSM2")
    try:
        ActiveFutureSF2 = tables[0].find(
            'div', {'id': 'IMPF-2fs'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFutureSF2")
    try:
        ActiveFuturePM2 = tables[0].find(
            'div', {'id': 'IMPF-2mp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFuturePM2")
    try:
        ActiveFuturePF2 = tables[0].find(
            'div', {'id': 'IMPF-2fp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFuturePF2")

    # Future3
    try:
        ActiveFutureSM3 = tables[0].find(
            'div', {'id': 'IMPF-3ms'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFutureSM3")
    try:
        ActiveFutureSF3 = tables[0].find(
            'div', {'id': 'IMPF-3fs'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFutureSF3")
    try:
        ActiveFuturePM3 = tables[0].find(
            'div', {'id': 'IMPF-3mp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFuturePM3")
    try:
        ActiveFuturePF3 = tables[0].find(
            'div', {'id': 'IMPF-3fp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ActiveFuturePF3")

    # Imperative
    try:
        ImperativeSM = tables[0].find(
            'div', {'id': 'IMP-2ms'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ImperativeSM")
    try:
        ImperativeSF = tables[0].find(
            'div', {'id': 'IMP-2fs'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ImperativeSF")
    try:
        ImperativePM = tables[0].find(
            'div', {'id': 'IMP-2mp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ImperativePM")
    try:
        ImperativePF = tables[0].find(
            'div', {'id': 'IMP-2fp'}).find_all('span', class_='menukad')[-1].text
    except:
        print("There is no ImperativePF")

    if len(tables) > 1:
        # Now scrape Passive conjugations (if there are)
        # Present
        try:
            PassivePresentSM = tables[1].find(
                'div', {'id': 'passive-AP-ms'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePresentSM")
        try:
            PassivePresentSF = tables[1].find(
                'div', {'id': 'passive-AP-fs'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePresentSF")
        try:
            PassivePresentPM = tables[1].find(
                'div', {'id': 'passive-AP-mp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePresentSF")
        try:
            PassivePresentPF = tables[1].find(
                'div', {'id': 'passive-AP-fp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePresentSF")

        # Past1
        try:
            PassivePastS1 = tables[1].find(
                'div', {'id': 'passive-PERF-1s'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastS1")
        try:
            PassivePastP1 = tables[1].find(
                'div', {'id': 'passive-PERF-1p'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastP1")

        # Past2
        try:
            PassivePastSM2 = tables[1].find(
                'div', {'id': 'passive-PERF-2ms'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastSM2")
        try:
            PassivePastSF2 = tables[1].find(
                'div', {'id': 'passive-PERF-2fs'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastSF2")
        try:
            PassivePastPM2 = tables[1].find(
                'div', {'id': 'passive-PERF-2mp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastPM2")
        try:
            PassivePastPF2 = tables[1].find(
                'div', {'id': 'passive-PERF-2fp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastPF2")

        # Past3
        try:
            PassivePastSM3 = tables[1].find(
                'div', {'id': 'passive-PERF-3ms'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastSM3")
        try:
            PassivePastSF3 = tables[1].find(
                'div', {'id': 'passive-PERF-3fs'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastSF3")
        try:
            PassivePastPM3 = tables[1].find(
                'div', {'id': 'passive-PERF-3p'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastPM3")
        try:
            PassivePastPF3 = tables[1].find(
                'div', {'id': 'passive-PERF-3p'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassivePastPF3")

        # Future1
        try:
            PassiveFutureS1 = tables[1].find(
                'div', {'id': 'passive-IMPF-1s'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFutureS1")
        try:
            PassiveFutureP1 = tables[1].find(
                'div', {'id': 'passive-IMPF-1p'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFutureP1")

        # Future2
        try:
            PassiveFutureSM2 = tables[1].find(
                'div', {'id': 'passive-IMPF-2ms'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFutureSM2")
        try:
            PassiveFutureSF2 = tables[1].find(
                'div', {'id': 'passive-IMPF-2fs'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFutureSF2")
        try:
            PassiveFuturePM2 = tables[1].find(
                'div', {'id': 'passive-IMPF-2mp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFuturePM2")
        try:
            PassiveFuturePF2 = tables[1].find(
                'div', {'id': 'passive-IMPF-2fp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFuturePF2")

        # Future3
        try:
            PassiveFutureSM3 = tables[1].find(
                'div', {'id': 'passive-IMPF-3ms'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFutureSM3")
        try:
            PassiveFutureSF3 = tables[1].find(
                'div', {'id': 'passive-IMPF-3fs'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFutureSF3")
        try:
            PassiveFuturePM3 = tables[1].find(
                'div', {'id': 'passive-IMPF-3mp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFuturePM3")
        try:
            PassiveFuturePF3 = tables[1].find(
                'div', {'id': 'passive-IMPF-3fp'}).find_all('span', class_='menukad')[-1].text
        except:
            print("There is no PassiveFuturePF3")

    return(ActivePresentSM,
           ActivePresentSF,
           ActivePresentPM,
           ActivePresentPF,

           ActivePastS1,
           ActivePastP1,
           ActivePastSM2,
           ActivePastSF2,
           ActivePastPM2,
           ActivePastPF2,
           ActivePastSM3,
           ActivePastSF3,
           ActivePastPM3,
           ActivePastPF3,

           ActiveFutureS1,
           ActiveFutureP1,
           ActiveFutureSM2,
           ActiveFutureSF2,
           ActiveFuturePM2,
           ActiveFuturePF2,
           ActiveFutureSM3,
           ActiveFutureSF3,
           ActiveFuturePM3,
           ActiveFuturePF3,

           ImperativeSM,
           ImperativeSF,
           ImperativePM,
           ImperativePF,

           PassivePresentSM,
           PassivePresentSF,
           PassivePresentPM,
           PassivePresentPF,

           PassivePastS1,
           PassivePastP1,
           PassivePastSM2,
           PassivePastSF2,
           PassivePastPM2,
           PassivePastPF2,
           PassivePastSM3,
           PassivePastSF3,
           PassivePastPM3,
           PassivePastPF3,

           PassiveFutureS1,
           PassiveFutureP1,
           PassiveFutureSM2,
           PassiveFutureSF2,
           PassiveFuturePM2,
           PassiveFuturePF2,
           PassiveFutureSM3,
           PassiveFutureSF3,
           PassiveFuturePM3,
           PassiveFuturePF3)


def main():
    dictionary_df = pd.read_csv("dictionary.csv")
    # Add Null conjugation columns
    dictionary_df = dictionary_df.assign(
        Noun_singularAbsolute=None, Noun_pluralAbsolute=None, Noun_singularConstruct=None, Noun_pluralConstruct=None,
        Adj_SM=None, Adj_SF=None, Adj_PM=None, Adj_PF=None,
        Verb_ActivePresentSM=None, Verb_ActivePresentSF=None, Verb_ActivePresentPM=None, Verb_ActivePresentPF=None,
        Verb_ActivePastS1=None, Verb_ActivePastP1=None, Verb_ActivePastSM2=None, Verb_ActivePastSF2=None, Verb_ActivePastPM2=None, Verb_ActivePastPF2=None, Verb_ActivePastSM3=None, Verb_ActivePastSF3=None, Verb_ActivePastPM3=None, Verb_ActivePastPF3=None,
        Verb_ActiveFutureS1=None, Verb_ActiveFutureP1=None, Verb_ActiveFutureSM2=None, Verb_ActiveFutureSF2=None, Verb_ActiveFuturePM2=None, Verb_ActiveFuturePF2=None, Verb_ActiveFutureSM3=None, Verb_ActiveFutureSF3=None, Verb_ActiveFuturePM3=None, Verb_ActiveFuturePF3=None,
        Verb_ImperativeSM=None, Verb_ImperativeSF=None, Verb_ImperativePM=None, Verb_ImperativePF=None,
        Verb_PassivePresentSM=None, Verb_PassivePresentSF=None, Verb_PassivePresentPM=None, Verb_PassivePresentPF=None,
        Verb_PassivePastS1=None, Verb_PassivePastP1=None, Verb_PassivePastSM2=None, Verb_PassivePastSF2=None, Verb_PassivePastPM2=None, Verb_PassivePastPF2=None, Verb_PassivePastSM3=None, Verb_PassivePastSF3=None, Verb_PassivePastPM3=None, Verb_PassivePastPF3=None,
        Verb_PassiveFutureS1=None, Verb_PassiveFutureP1=None, Verb_PassiveFutureSM2=None, Verb_PassiveFutureSF2=None, Verb_PassiveFuturePM2=None, Verb_PassiveFuturePF2=None, Verb_PassiveFutureSM3=None, Verb_PassiveFutureSF3=None, Verb_PassiveFuturePM3=None, Verb_PassiveFuturePF3=None
    )

    for index, row in dictionary_df.iterrows():
        print(index, row['Hebrew-Niqqud'])

        link = row["Link"]
        part_of_speech = row["Part-of-Speech"].split(" ")[0].strip()

        if part_of_speech == "Noun":
            (row["Noun_singularAbsolute"], row["Noun_pluralAbsolute"],
             row["Noun_singularConstruct"], row["Noun_pluralConstruct"]) = noun_scraper(link)
        elif part_of_speech == "Adjective":
            (row['Adj_SM'], row['Adj_SF'], row['Adj_PM'],
             row['Adj_PF']) = adjective_scraper(link)
        elif part_of_speech == "Verb":
            (row['Verb_ActivePresentSM'], row['Verb_ActivePresentSF'], row['Verb_ActivePresentPM'], row['Verb_ActivePresentPF'],
             row['Verb_ActivePastS1'], row['Verb_ActivePastP1'], row['Verb_ActivePastSM2'], row['Verb_ActivePastSF2'], row['Verb_ActivePastPM2'], row[
                 'Verb_ActivePastPF2'], row['Verb_ActivePastSM3'], row['Verb_ActivePastSF3'], row['Verb_ActivePastPM3'], row['Verb_ActivePastPF3'],
                row['Verb_ActiveFutureS1'], row['Verb_ActiveFutureP1'], row['Verb_ActiveFutureSM2'], row['Verb_ActiveFutureSF2'], row['Verb_ActiveFuturePM2'], row[
                    'Verb_ActiveFuturePF2'], row['Verb_ActiveFutureSM3'], row['Verb_ActiveFutureSF3'], row['Verb_ActiveFuturePM3'], row['Verb_ActiveFuturePF3'],
                row['Verb_ImperativeSM'], row['Verb_ImperativeSF'], row['Verb_ImperativePM'], row['Verb_ImperativePF'],
                row['Verb_PassivePresentSM'], row['Verb_PassivePresentSF'], row['Verb_PassivePresentPM'], row['Verb_PassivePresentPF'],
                row['Verb_PassivePastS1'], row['Verb_PassivePastP1'], row['Verb_PassivePastSM2'], row['Verb_PassivePastSF2'], row['Verb_PassivePastPM2'], row[
                    'Verb_PassivePastPF2'], row['Verb_PassivePastSM3'], row['Verb_PassivePastSF3'], row['Verb_PassivePastPM3'], row['Verb_PassivePastPF3'],
                row['Verb_PassiveFutureS1'], row['Verb_PassiveFutureP1'], row['Verb_PassiveFutureSM2'], row['Verb_PassiveFutureSF2'], row['Verb_PassiveFuturePM2'], row['Verb_PassiveFuturePF2'], row['Verb_PassiveFutureSM3'], row['Verb_PassiveFutureSF3'], row['Verb_PassiveFuturePM3'], row['Verb_PassiveFuturePF3']) = verb_scraper(link)
        else:
            continue

        time.sleep(random.uniform(1, 5))

    dictionary_df.to_csv("dictionary.csv", index=False)


if __name__ == "__main__":
    main()
