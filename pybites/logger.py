import logging

logging.basicConfig(level=logging.INFO,
                    format='\n-> [%(levelname)s] [%(asctime)s] %(message)s\n',
                    datefmt='%Y-%m-%d %H:%M')

log = logging.getLogger(__name__)
