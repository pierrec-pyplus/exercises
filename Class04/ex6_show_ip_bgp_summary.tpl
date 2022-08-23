Value Filldown ROUTERID (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
# 4 bytes ASN -> 4294967295
Value Filldown LOCAL_AS (\d{1,10})
Value NEIGH (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
Value REM_AS (\d{1,10})
Value UP_DOWN (\S+)
Value PRFX_RCVD ((\d+|Active|Idle))

Start
  ^BGP router identifier\s${ROUTERID}, local AS number\s${LOCAL_AS}\s*$$
  ^Neighbor.*State\/PfxRcd\s*$$ -> ShowIPBgp

ShowIPBgp
  ^${NEIGH}\s+\d+\s+${REM_AS}(\s+\d+){5}\s+${UP_DOWN}\s+${PRFX_RCVD}\s*$$ -> Record

EOF
