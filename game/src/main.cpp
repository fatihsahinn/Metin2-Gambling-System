// Add Top Of File

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
#include "LotteryManager.h"
#endif

// Find

CPrivManager	priv_manager;

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	CLotteryManager	LotteryManager;
#endif

// Find 

OXEvent_manager.Initialize();

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	LotteryManager.Initialize();
#endif

// Find 

item_manager.GracefulShutdown();

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	sys_log(0, "<shutdown> Shutting down LotteryManager...");
	LotteryManager.Destroy();
#endif


