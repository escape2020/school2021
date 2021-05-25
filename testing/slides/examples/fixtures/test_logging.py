import logging

def do_work():
    log = logging.getLogger('do_work')
    log.info('Doing work')
    log.info('Done')


def test_do_work_logs(caplog):
    with caplog.at_level(logging.INFO):
        do_work()

    assert len(caplog.records) == 2
    for record in caplog.records:
        assert record.levelno == logging.INFO
