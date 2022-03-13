// Find

int					m_iMallLoadTime;

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
		int m_iLotteryLoadTime;
#endif

// Find

void	SetSafeboxLoadTime() { m_iSafeboxLoadTime = thecore_pulse(); }

// Add Below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
		int GetLastLotteryTime() const { return m_iLotteryLoadTime; }
		void SetLastLotteryTime() { m_iLotteryLoadTime = thecore_pulse(); }
#endif

