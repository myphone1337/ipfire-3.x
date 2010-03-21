#!/usr/bin/python

import gettext
_ = lambda x: gettext.ldgettext("pomona", x)
N_ = lambda x: x

version = "VERSION"
name = "NAME v%s" % version
sname = "SNAME"
iname = "PNAME"
bugurl = "http://bugtracker.ipfire.org/"
wikiurl = "http://wiki.ipfire.org/"
kernelVersion = "KVER"

HARDDISK_PATH = "/mnt/target"
SOURCE_PATH = "/mnt/source"
INFO_FILE = ".%sinfo" % (sname,)
IMAGE_FILE = "%s-%s.sfs" % (sname, version)
IMAGE_FILE_LS = "%s-%s.ls" % (sname, version)

REQUIRED_FILES = (IMAGE_FILE,)

DISPATCH_BACK = -1
DISPATCH_FORWARD = 1
DISPATCH_NOOP = None

CLEARPART_TYPE_ALL = 0
CLEARPART_TYPE_NONE = -1

CB_UNDEF = -1
CB_START = 0
CB_STOP  = 1
CB_WAIT  = 2
CB_PROGRESS = 3

INSTALL_OK = 0
INSTALL_BACK = -1
INSTALL_NOOP = -2

# different types of partition requests
# REQUEST_PREEXIST is a placeholder for a pre-existing partition on the system
# REQUEST_NEW is a request for a partition which will be automatically
#              created based on various constraints on size, drive, etc
# REQUEST_RAID is a request for a raid device
# REQUEST_PROTECTED is a preexisting partition which can't change
#              (harddrive install, harddrive with the isos on it)
#
REQUEST_PREEXIST = 1
REQUEST_NEW = 2
REQUEST_RAID = 4
REQUEST_PROTECTED = 8
REQUEST_VG = 16 # volume group
REQUEST_LV = 32 # logical volume

# XXX this is made up and used by the size spinner; should just be set with
# a callback
MAX_PART_SIZE = 1024*1024*1024

lvmErrorOutput = "/tmp/lvmout"

exceptionText = _("An unhandled exception has occurred.  This "
                  "is most likely a bug.  Please save a copy of "
                  "the detailed exception and file a bug report")
if not bugurl:
    # this string will be combined with "An unhandled exception"...
    # the leading space is not a typo.
    exceptionText += _(" with the provider of this software.")
else:
    # this string will be combined with "An unhandled exception"...
    # the leading space is not a typo.
    exceptionText += _(" against pomona at %s") %(bugurl,)

class Translator:
    """A simple class to facilitate on-the-fly translation for newt buttons"""
    def __init__(self, button, check):
        self.button = button
        self.check = check

    def __getitem__(self, which):
        if which == 0:
            return _(self.button)
        elif which == 1:
            return self.check
        raise IndexError

    def __len__(self):
        return 2

TEXT_OK_STR = N_("OK")
TEXT_OK_CHECK  = "ok"
TEXT_OK_BUTTON = Translator(TEXT_OK_STR, TEXT_OK_CHECK)

TEXT_CANCEL_STR = N_("Cancel")
TEXT_CANCEL_CHECK  = "cancel"
TEXT_CANCEL_BUTTON = Translator(TEXT_CANCEL_STR, TEXT_CANCEL_CHECK)

TEXT_BACK_STR = N_("Back")
TEXT_BACK_CHECK = "back"
TEXT_BACK_BUTTON = Translator(TEXT_BACK_STR, TEXT_BACK_CHECK)

TEXT_YES_STR = N_("Yes")
TEXT_YES_CHECK = "yes"
TEXT_YES_BUTTON = Translator(TEXT_YES_STR, TEXT_YES_CHECK)

TEXT_NO_STR = N_("No")
TEXT_NO_CHECK = "no"
TEXT_NO_BUTTON = Translator(TEXT_NO_STR, TEXT_NO_CHECK)

TEXT_EDIT_STR = N_("Edit")
TEXT_EDIT_CHECK = "edit"
TEXT_EDIT_BUTTON = Translator(TEXT_EDIT_STR, TEXT_EDIT_CHECK)

TEXT_F12_CHECK = "F12"