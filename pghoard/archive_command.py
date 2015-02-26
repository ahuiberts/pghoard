"""
pghoard - archive_command for postgresql

Copyright (c) 2015 Ohmu Ltd
See LICENSE for details
"""

import argparse
import sys

if sys.version_info[0] >= 3:
    from http.client import HTTPConnection  # pylint: disable=import-error
else:
    from httplib import HTTPConnection  # pylint: disable=import-error


def archive(port, site, xlog_path):
    conn = HTTPConnection(host="localhost", port=port)
    conn.request("PUT", "/" + site + "/archive/" + xlog_path)
    if conn.getresponse().status == 206:
        return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=16000,
                        help="pghoard repository port")
    parser.add_argument("-s", "--site", type=str, default="default",
                        help="pghoard site")
    parser.add_argument("-x", "--xlog_path", type=str, required=True,
                        help="complete path to xlog file")
    args = parser.parse_args()
    if archive(args.port, args.site, args.xlog_path):
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
