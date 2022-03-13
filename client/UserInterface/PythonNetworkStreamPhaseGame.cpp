// Add end of file
#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
bool CPythonNetworkStream::RecvLotteryList()
{
	TPacketGCRefreshKumarList p;
	if (!Recv(sizeof(TPacketGCRefreshKumarList), &p))
	{
		Tracenf("Recv Lottery List System Packet Error");
		return false;
	}
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_LOTTERY_LIST_SYSTEM", Py_BuildValue("(sii)", p.isim, p.miktar, p.renk));

	return true;
}
#endif