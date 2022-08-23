Value IF_NAME (\S+)
Value LINE_STATUS ((up|down))
Value ADM_STATE ((up|down))
Value MAC_ADD (\w{4}\.\w{4}\.\w{4})
Value MTU (\d{2,4}\sbytes)
Value DUPLEX (full-duplex|half-duplex)
Value SPEED (\d{1,4}\sMb\/s)
 
Start
  ^${IF_NAME}\sis\s${LINE_STATUS}
  ^admin\sstate\sis\s${ADM_STATE}.*
  ^\s+Hardware:\s+Ethernet,\saddress:\s${MAC_ADD}\s+.*
  ^\s+MTU\s${MTU}.*
  ^\s+${DUPLEX},\s${SPEED} -> Record
