from datamining.module.controller import Parser
from datamining.module.logger import logger
from bs4 import BeautifulSoup


class ParserName(Parser):
    def __init__(self):
        super().__init__()

    async def main(self):
        r = await self.session.get('https://mxat.ru/timetable/')

        soup = BeautifulSoup(r.text, 'lxml')

        divs = soup.find_all('div', class_='ttl')

        for div in divs:
            text = div.text
            logger.info(text)