Value MAC_ADDR ([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})
Value ADDR (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value NAME (\S+)
Value INTERFACE (\S+)

Start
  ^MAC Address.*Flags\s*$$ -> ShowARP

ShowARP
  ^${MAC_ADDR}\s+${ADDR}\s+${NAME}\s+${INTERFACE}\s+ -> Record

