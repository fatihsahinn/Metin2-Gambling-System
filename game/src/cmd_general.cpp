// Add

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
#include "LotteryManager.h"
ACMD(do_lottery_clear_test)
{
	if(CLotteryManager::instance().ClearAllInfo() == true)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Temizleme Başarılı!");
	}
	else
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Temizleme Başarısız!");
	}
	
}
ACMD(do_lottery_draw)
{
	char arg1[256], arg2[256];
	two_arguments(argument, arg1, sizeof(arg1), arg2, sizeof(arg2));

	if (!*arg1 || !*arg2 || !ch || !ch->GetDesc())
		return;

	DWORD miktar = 0;
	BYTE renk = 0;
	str_to_number(miktar, arg1);
	str_to_number(renk, arg2);

	if (ch->IsDead() || ch->GetExchange() || ch->IsOpenSafebox() || ch->IsCubeOpen())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't do that with a window already open!"));
		return;
	}
	
	if(ch->GetMapIndex() != CLotteryManager::instance().LOTTERY_MAP_INDEX)
	{
		ch->ChatPacket(CHAT_TYPE_COMMAND, "NoMatchMapIndex_Alert");
		return;
	}
	
	if(miktar == 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "0 ep ile oynayamazsınız.");
		return;
	}

	if (ch->GetDragonCoin() < miktar)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Yeterli Ejderha Paranız Bulunmuyor."));
		return;
	}
	
	if(CLotteryManager::instance().RegisterEvent(ch,miktar,renk) == true)
	{
		ch->SetDragonCoin(ch->GetDragonCoin() - miktar);
		ch->ChatPacket(CHAT_TYPE_INFO,"%d miktarı oyun oynama başarılı.",miktar);
		
	}
	else
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Zaten kayıt yaptırdınız bekleyiniz.");
	}
	
}
ACMD(do_lottery_alert)
{
	if (!ch)
		return;
	
	if (ch->IsDead() || ch->GetExchange() || ch->IsOpenSafebox() || ch->IsCubeOpen())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't do that with a window already open!"));
		return;
	}
	
	if(ch->GetMapIndex() != CLotteryManager::instance().LOTTERY_MAP_INDEX)
		ch->WarpSet(CLotteryManager::instance().LOTTERY_BASE_X*100,CLotteryManager::instance().LOTTERY_BASE_Y*100);
	else
		ch->ChatPacket(CHAT_TYPE_INFO, "Zaten bu maptasınız.");
}
ACMD(do_lottery_pencere)
{
	if (!ch)
		return;
	
	if (ch->IsDead() || ch->GetExchange() || ch->IsOpenSafebox() || ch->IsCubeOpen())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You can't do that with a window already open!"));
		return;
	}
	
	if(thecore_pulse() - ch->GetLastLotteryTime() < PASSES_PER_SEC(3))
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("bu_kadar_seri_yapamazsin"));
		return;
	}
	ch->SetLastLotteryTime();
	
	CLotteryManager::instance().RefreshRegisterList();
	ch->ChatPacket(CHAT_TYPE_COMMAND, "LotteryOpenWindow");
}
#endif