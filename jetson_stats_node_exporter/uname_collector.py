import os
import socket
from prometheus_client.core import GaugeMetricFamily

class UnameCollector:
    def collect(self):
        uname = os.uname()
        try:
            fqdn = socket.getfqdn()
            hostname = socket.gethostname()
            domainname = fqdn.replace(hostname, "", 1).strip(".") or "(none)"
        except Exception:
            domainname = "(none)"

        labels = {
            "nodename": uname.nodename,
            "sysname": uname.sysname,
            "release": uname.release,
            "version": uname.version,
            "machine": uname.machine,
            "domainname": domainname,
        }

        metric = GaugeMetricFamily(
            "node_uname_info",
            "Labeled system information as provided by the uname system call",
            labels=list(labels.keys())
        )
        metric.add_metric(list(labels.values()), 1)

        print(labels)
        yield metric
