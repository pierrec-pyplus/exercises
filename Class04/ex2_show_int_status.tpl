Value PORT_NAME (\S+)
Value STATUS (connected|notconnect)
Value VLAN (\d{1,4})
Value DUPLEX (auto|full|half)
Value SPEED (auto|10|100|1000)
Value PORT_TYPE (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntStatus

ShowIntStatus
  ^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${PORT_TYPE}\s*$$ -> Record

EOF
