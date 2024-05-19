# Utility functions
def setup_logging(logfile='packets.log'):
    import logging
    logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s - %(message)s')