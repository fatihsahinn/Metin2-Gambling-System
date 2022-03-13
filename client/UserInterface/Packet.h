// Find

HEADER_GC_HANDSHAKE_OK						= 0xfc,

// Add to top

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	HEADER_GC_LOTTERY_LIST_SYSTEM				= 251,
#endif

// Find

#pragma pack(pop)

// Add to top

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
typedef struct packet_lottery_system
{
	BYTE	header;
	char	isim[CHARACTER_NAME_MAX_LEN + 1];
	DWORD	miktar;
	BYTE	renk;
} TPacketGCRefreshKumarList;
#endif



