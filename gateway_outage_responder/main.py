import logging
import subprocess
import time
import urllib2


logger = logging.getLogger(__name__)


def internet_is_accessible():
    try:
        urllib2.urlopen(
            'http://google.com',
            timeout=5
        )
        return True
    except urllib2.URLError:
        pass
    return False


def unplug_cable_modem():
    logger.debug('Turning off cable modem outlet...')
    subprocess.call([
        'stanley-outlet-control',
        '1',
        'off'
    ])


def plug_in_cable_modem():
    logger.debug('Turning on cable modem outlet...')
    subprocess.call([
        'stanley-outlet-control',
        '1',
        'on'
    ])


def unplug_router():
    logger.debug('Turning off router outlet...')
    subprocess.call([
        'stanley-outlet-control',
        '2',
        'off'
    ])


def plug_in_router():
    logger.debug('Turning on router outlet...')
    subprocess.call([
        'stanley-outlet-control',
        '2',
        'on'
    ])


def main():
    if not internet_is_accessible():
        unplug_router()
        unplug_cable_modem()

        plug_in_cable_modem()

        time.sleep(20)

        plug_in_router()
