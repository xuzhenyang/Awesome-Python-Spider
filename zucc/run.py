# -*- coding: utf-8 -*-

import login
import getGradePage
import getPlanPage

def main():
    #dosomething
    Url = login.run()
    getGradePage.run(Url)
    getPlanPage.run(Url)
    
if __name__ == "__main__":
    main()