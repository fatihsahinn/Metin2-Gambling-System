// Find

Set(HEADER_GC_DRAGON_SOUL_REFINE,		CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCDragonSoulRefine), STATIC_SIZE_PACKET));

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
			Set(HEADER_GC_LOTTERY_LIST_SYSTEM, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCRefreshKumarList), STATIC_SIZE_PACKET));
#endif