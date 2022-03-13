## Find

print "---------------------------------------------------------------------------- CLOSE GAME WINDOW"

## Add Below

	if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
		def BINARY_LOTTERY_LIST_SYSTEM(self,isim,miktar,renk):
			self.interface.SetLotteryListData(isim,miktar,renk)

## Find

self.serverCommander=stringCommander.Analyzer()

## Add To Top

		if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
			serverCommandList.update({"LotteryRegisterReward"	: self.__LotterySetLP,})
			serverCommandList["NoMatchMapIndex_Alert"] = self.AlertLottery
			serverCommandList["LotteryOpenWindow"] = self.ToggleLotteryWindow2
			serverCommandList["SaniyeBaslat"] = self.LotterySecondStart
			serverCommandList["StatisticGonder"] = self.LotteryStatisticGonder

##Add End Of File

	if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
		def AlertLottery(self):
			lotteryAlertQuestion = uiCommon.QuestionDialog2()
			lotteryAlertQuestion.SetText1("Şu anda bulunduğunuz bölge buna uygun değil.")
			lotteryAlertQuestion.SetText2("Kabul ederseniz sizi kumar bölgesine yollayacağım.")
			lotteryAlertQuestion.SetAcceptEvent(ui.__mem_func__(self.OnAcceptLotteryQuestion))
			lotteryAlertQuestion.SetCancelEvent(ui.__mem_func__(self.OnDenyLotteryQuestion))
			lotteryAlertQuestion.Open()
			self.lotteryAlertQuestion = lotteryAlertQuestion

		def OnAcceptLotteryQuestion(self):
			fRaC_Fa4AP3cA1.SendChatPacket("/lotteryalertgit")
			self.OnCloseLotteryQuestionDialog()
			return True

		def OnDenyLotteryQuestion(self):
			self.OnCloseLotteryQuestionDialog()
			return True
		
		def OnCloseLotteryQuestionDialog(self):
			self.lotteryAlertQuestion.Close()
			self.lotteryAlertQuestion = None
			return True
		
		def ToggleLotteryWindow(self):
			fRaC_Fa4AP3cA1.SendChatPacket("/lottery_pencere")
		
		def ToggleLotteryWindow2(self):
			self.interface.ToggleLotteryWindow()
		
		def __LotterySetLP(self, lp):
			if self.interface:
				self.interface.InitRollLP(lp)
		
		def LotterySecondStart(self, second):
			if self.interface:
				self.interface.LotterySecondStart(second)
		
		def LotteryStatisticGonder(self,totalep,win,loss):
			if self.interface:
				self.interface.LotteryAddStatistic(totalep,win,loss)
				self.interface.LotteryMakeGui()

