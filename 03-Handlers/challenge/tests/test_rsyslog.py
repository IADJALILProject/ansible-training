import re
import testinfra

host = testinfra.get_host("local://")

def test_rsyslog_cron_uncommented():
    f = host.file("/etc/rsyslog.d/50-default.conf")
    assert f.exists
    assert re.search(r"^\s*cron\.\*\s+/var/log/cron\.log", f.content_string, re.MULTILINE)

def test_handler_ran():
    flag = host.file("/tmp/rsyslog_handler_ran")
    assert flag.exists
