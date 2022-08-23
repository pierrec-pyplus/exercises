Value DEVICE_ID (\S+)
Value LOCAL_INTF (\S+)
Value CAPABILITY (\S+)
Value PORT_ID (\S+)

Start
  ^Device ID.*Port ID.*$$ -> ShowLLDP

ShowLLDP
  ^${DEVICE_ID}\s+${LOCAL_INTF}\s+\d+\s+${CAPABILITY}\s+${PORT_ID}\s*$$ -> Record

EOF
