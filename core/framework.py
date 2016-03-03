#! /bin/python
import argparse
from fingerprint import Fingerprint
import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("output.txt", "a")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


class Framework():
    def __init__(self):
        self.config = {}
    def runner(self, argv):
        fingerprint = Fingerprint()
        fingerprint.connect(self.config)
    def parseParameters(self, argv):
        parser = argparse.ArgumentParser()
        filesgroup = parser.add_argument_group('inputs')
        filesgroup.add_argument("--host",
            dest="HOST",
            action="store",
            help="Host to test against")
        filesgroup.add_argument("-u",
            dest="USERNAME",
            action="store",
            help="Username")
        filesgroup.add_argument("-p",
            dest="PASSWORD",
            action="store",
            help="Password")
        filesgroup.add_argument("--protocol",
            dest="protocol",
            action="store",
            help="Protocol to use (i.e., http or https)")
        filesgroup.add_argument("--port",
            dest="port",
            action="store",
            help="Port to use. Default for protocol https is port 443, and http is port 80")
        filesgroup.add_argument("-U",
            dest="UserFile",
            action="store",
            help="File containing Usernames")
        filesgroup.add_argument("-t",
            dest="threads",
            action="store",
            help="Number of threads to use for brute forcing. (not yet implemented.)")
        filesgroup.add_argument("-o",
            dest="output",
            action="store",
            help="Outfile File Name")
        args = parser.parse_args()
        self.config["USERNAME"] = args.USERNAME
        self.config["PASSWORD"] = args.PASSWORD
        self.config["HOST"] = args.HOST
        self.config["protocol"] = args.protocol
        self.config["port"] = args.port
        self.config["UserFile"] = args.UserFile
        self.config["threads"] = args.threads
        self.config["output"] = args.output
    def banner(self, argv):
        print """



                         `.-:-.`           `.-::-.`
                     `:oyhhyooooo+:`    -+osooooyhhs+.
                   `/yhhs:`      `.-.`-/:.      `./syyo.
                  `shyy:            `-.            .+yyy.
    \M:         `ohyy/             `               `/yys
    :M:          .hyyy-                              .yyy.
    :M:          -hyyy/                              .hhy`
    :M:          `shyyy:                            `ohh+
    :M:           .shyyy+.                         .shh+`
    :M:            .+hhhyyo-`                    `/yho-
    :M:             `-ohhhhhy+-`               .+yy+-
    /M:              `./syhhhhs/.          -/os+-`
                         `.-+syddho-     `:+/-`
                             `.-+yddo.  `/.
                                 `-ohh- ``
                                   `-yh.
                                     .yo
                                      -s
                                      ./
                                      `
                                   -.`--:--:..`         -.//:.:-////://:.`/o/ `.-/:--::///:://-.`o+-
                                  .hNdNNdyhmNmds.       .sMMMmMmyhhosshdm+NMh `-dMMNNMdyhyosyhdyyMM/
                                   /MMNN:  .hMMMs        oMMMMMo       `:-NM-   dMMMMN-       `:oMd`
                                   .MMMN-   +MMm-        /MMMMd`         `hM`   yMMMMo          .Mh
                                   `MNNM+ .:mMs+`        -NMMMd       ``  sm`   sMMMMo       .   No
                                   `NMMNsymMMh--``       `yMMMd      .yo  :o    .NMMM+     `:d.  s-
                                   `dMMMMMMMMNMMddho:    -NMMMy    `sNM-  .:    oMMMM:    .dNh`  :.
                                   .NMMmMd++//omMMMMM-   `NMMMNo+-+hMMm         /MMMMd+/:omMMo
                                   `MMNmM:     -NMMMM/   /MMMMMNdmNNMMd         yMMMMMmdmNMMM+
                                   `mmNds       sMMMM.   -MMMMm.``.:sNm         sMMMMs``..:dMo
                                   `hNNm:       +MMMN`   `mMMMy`     -y`        :MMMM/     `+s
                                   -MNmM:       :MMMy    -NMMMh.       `        oMMMMo
                                   .NmMM+       yMMd`    `hMMMm`                -NMMMs
      yms`.:+o` `-//`               hNMMs       hMN/     .mMMMd                 +MMMM+
      sMNssoNMhyyodmh``dm/   -+yh`  oNMNd      .dM:      `hMMMm`                :NMMMs
      /md`  +MMo  `:N: mN.    omo  `NMMMh    `sNms       :dMMMm                 oNMMMo
       dd   `mM.   -N+ sd     oMo   hMMMN/-/yddo/        :MMMMm.                sMMMMh
      .N+    /N:   sMs ym-``-oNMo  .mMMMNdmds.           /MMMMM+`               yMMMMm:
      /ms:  `oh:   /hh-:ydyyo/+No ::/yhoso:`             ohdhydhs/             `hddyhdyo.
                          `   :No                                `                     `
                              `mo
                              `mo
                              `mo
                     :-      `sN:
                    ++      -yNo
                   oy   `-+hh+.
                  -mdoooo+-`
                   ..`                                                                                                                                                   """
        print " ---a Brute Force Framework by l0gan (@kirkphayes)"
    def run(self, argv):
        self.parseParameters(argv)
        if self.config["output"]:
            sys.stdout = Logger() #logging works as output.txt, but want to make so it will log to specific file.
        self.banner(self)
        if self.config["threads"]:
            print("This function has not been implemented yet. Threads will be set to 1...Sorry...")
        self.runner(self)