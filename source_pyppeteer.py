#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Chromium initialize
# import Chromium_Initialize
# Chromium_Initialize.download_chromium()

import asyncio
import pyppeteer
import datetime
from pyppeteer import launch
import csv
import pandas as pd
import os

async def main(year_0,month_0,day_0,year_1,month_1,day_1,name):
    
    # arise the browser and the site
    Chromium_path = 'C:/Users/Oth/AppData/Local/pyppeteer/pyppeteer/local-chromium/1132420/chrome-win/chrome.exe'
    browser = await launch({'headless': True,'executablePath': Chromium_path})
    page = await browser.newPage()
    await page.goto('https://q.stock.sohu.com/zs/000001/lshq.shtml')
    
    # set period
    period = date_gen(year_0,month_0,day_0,year_1,month_1,day_1)

    while 1:
        # period iteration
        period_time = next(period)
        period_s = str(period_time[0])
        period_e = str(period_time[1])

        # set the period to inquire
        await page.evaluate("() => document.getElementById('BIZ_lshq_sd').value = ''")
        await page.evaluate("() => document.getElementById('BIZ_lshq_ed').value = ''")
        await page.type("#BIZ_lshq_sd",period_s)
        await page.type("#BIZ_lshq_ed",period_e)

        # await page.waitFor(10000)

        await page.click('input[type="button"][value="查询"]')  

        # wait
        await page.waitFor(5000)

        data = []
        element_set = await page.querySelectorAll('td')
        for element in element_set:
            data.append(await (await element.getProperty('innerText')).jsonValue())
        
        # modify data
        del data[:48]
        del data[-49:]

        # dataf = pd.DataFrame(data)
        # dataf.to_csv('test.csv',index=False)

        
        # output
        data_line = {'date':[],'opening':[],'closing':[],'Change':[],'Chg':[],'Lowest':[],'Highest':[],'Vol(hands)':[],'OBV(10k)':[]}
        i = 0
        for data_single in data:
            remainder = i % 10
            match remainder:
                case 9: pass
                case 0: data_line['date'].append(data_single)
                case 1: data_line['opening'].append(data_single)
                case 2: data_line['closing'].append(data_single)
                case 3: data_line['Change'].append(data_single)
                case 4: data_line['Chg'].append(data_single)
                case 5: data_line['Lowest'].append(data_single)
                case 6: data_line['Highest'].append(data_single)
                case 7: data_line['Vol(hands)'].append(data_single)
                case 8: data_line['OBV(10k)'].append(data_single)
            i = i + 1
        df = pd.DataFrame(data_line,columns = ['date','opening','closing','Change','Chg','Lowest','Highest','Vol(hands)','OBV(10k)'])
        # df = pd.DataFrame(data_line)
        if os.path.exists('{}.csv'.format(name)):
            df.to_csv('{}.csv'.format(name),mode='a',index=False,header=False)
        else:
            df.to_csv('{}.csv'.format(name),index=False)

        # print(data)



def date_gen(year_0,month_0,day_0,year_1,month_1,day_1):
    date_1 = datetime.date(year_0,month_0,day_0)
    date_2 = datetime.date(year_1,month_1,day_1)
    date_e = date_2

    while date_e >= date_1:
        if date_e - datetime.timedelta(days=99) >= date_1:
            date_s = date_e - datetime.timedelta(days=99)
            # print(date_e)
            yield [date_s,date_e]
            date_e = date_s - datetime.timedelta(days=1)
        else:
            # print(date_e)
            yield [date_1,date_e]
            return 0

try:
    asyncio.get_event_loop().run_until_complete(main(2018,1,1,2019,12,31,'pre-Covid-19'))
    # asyncio.get_event_loop().run_until_complete(main(2020,1,1,2023,1,1,'Covid-19'))
except:
    print('Done')