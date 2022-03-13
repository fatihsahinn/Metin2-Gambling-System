// Find
m_iMallLoadTime = 0;

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	m_iLotteryLoadTime = 0;
#endif

// Find

DWORD CHARACTER::GetNextExp() const

// Add Below
#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
DWORD CHARACTER::GetDragonCoin()
{
	if (!this || !this->GetDesc() || !GetDesc() || !IsPC())
	{
		// sys_err("!this || !this->GetDesc()");
		return 0;
	}

	std::unique_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT dragoncoins FROM account.account WHERE id = '%d';", GetDesc()->GetAccountTable().id));
	if (pMsg->Get()->uiNumRows == 0)
		return 0;

	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	DWORD dc = 0;
	str_to_number(dc, row[0]);
	return dc;
}

void CHARACTER::SetDragonCoin(DWORD amount)
{
	std::unique_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("UPDATE account.account SET dragoncoins = '%d' WHERE id = '%d';", amount, GetDesc()->GetAccountTable().id));
	RefreshDragonCoin();
}
#endif
