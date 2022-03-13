// Find 

HEADER_GC_RESPOND_CHANNELSTATUS		= 210,

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	HEADER_GC_LOTTERY_LIST_SYSTEM		= 251,
#endif

// Find end of file

#pragma pack()

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

