from detected import Detected
from spider import Spider
from domain import *
from general import *
import os


def main():
    while True:
        print ('-----------Menu:                                                                   ---------------')
        print ('-----------     1: crawl all from web(from http://example.com).                    ---------------')
        print ('-----------     2: crawl all link from site page(from http://example.com/example). ---------------')
        print ('-----------     3: exit.                                                           ---------------')
        print ('==================================================================================================')
        print ('=> What is number of your choice: ')
        chose = int(input())
        if chose == 1:
            print ('+ You chose function 1(crawl): ')
            base_url = input('--->Enter your base url("http://example.com"): ')
            project_name = 'results/' + get_domain_name(base_url)
            if check_result_exits(project_name):
                print ("result save in " + project_name)
                inp = input("want continue crawl link?(Y/n)")
                if inp == 'Y' or inp == 'y':
                    detec = Detected(project_name, base_url)
                    detec.create_workers()
                    detec.crawl()
                else:
                    pass
            else:
                detec = Detected(project_name, base_url)
                detec.create_workers()
                detec.crawl()                
            
        elif chose == 2:
            print ('+ You chose function 2(crawl from a site page): ')
            project_name = input('--->Enter your project name: ')
            base_url = input('--->Enter your site page url: ')
            project_name = 'results/' + project_name
            base_url = 'results/' + base_url
            domain_name = get_domain_name(base_url)
            spi = Spider(project_name, base_url)
            
        elif chose == 3:
            break
    
            
if __name__ == '__main__':
    main()