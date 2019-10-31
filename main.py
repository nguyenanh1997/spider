from detected import Detected
from spider import Spider
from domain import *


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
            project_name = input('--->Enter your project name: ')
            base_url = input('--->Enter your base url: ')
            detec = Detected(project_name, base_url)
            detec.create_workers()
            detec.crawl()
            
        elif chose == 2:
            print ('+ You chose function 2(crawl from a site page): ')
            project_name = input('--->Enter your project name: ')
            base_url = input('--->Enter your site page url: ')
            domain_name = get_domain_name(base_url)
            spi = Spider(project_name, base_url)
            
        elif chose == 3:
            break
    
            
if __name__ == '__main__':
    main()