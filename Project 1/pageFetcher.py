import os
from lxml import html

class PageFetcher:
    
    def fetchPages(self,pagePath,webSite):
        xpath = "//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()"
        pages = []
        path = os.path.join(pagePath, webSite)
        files = sorted(os.listdir(path))[:50]
        
        for filename in files:
            filename = os.path.join(path,filename)
            file = open(filename, "r", encoding="UTF-8")
            page = file.read()
            tree = html.fromstring(page)
            htmlLeaves = tree.xpath(xpath)
            page = ""
            for leaf in htmlLeaves:
                page = page + " " + leaf
            pages.append(page)

        return pages
