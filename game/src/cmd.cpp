//Add end ACMD defination

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
ACMD(do_lottery_draw);
ACMD(do_lottery_alert);
ACMD(do_lottery_pencere);
#endif

// Find

{ "user_horse_feed",	do_user_horse_feed,		0,		POS_FISHING,	GM_PLAYER	},

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	{	"lottery_draw",	do_lottery_draw,	0,	POS_DEAD,	GM_PLAYER	},
	{	"lotteryalertgit",	do_lottery_alert,	0,	POS_DEAD,	GM_PLAYER	},
	{	"lottery_pencere",	do_lottery_pencere,	0,	POS_DEAD,	GM_PLAYER	},
#endif

//LotteryManager.cpp and LotteryManager.h can put your src file.
