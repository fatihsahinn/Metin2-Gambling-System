## Add To Top with between include

if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
	import uilottery

## Find

self.wndGuildBuilding = None

## Add Below

	if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
		self.lottery = None

## Find

	self.dlgExchange.Hide()
	
## Add Below

		if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
			self.lottery = uilottery.LotteryWindow()
			self.lottery.LoadWindow()

## Find

	del self.inputDialog
	
## Add Below

		if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
			if self.lottery:
				self.lottery.Destroy()
				del self.lottery

## Find

	def DragonSoulGiveQuilification(self):

## add at the end of the function

	if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
		def ToggleLotteryWindow(self):
			if self.lottery:
				self.lottery.OpenWindow()

		def InitRollLP(self, count):
			if self.lottery:
				self.lottery.InitRollLP(count)
		
		def LotterySecondStart(self,second):
			if self.lottery:
				self.lottery.SecondStart(second)
		
		def LotteryAddStatistic(self,totalep,win,loss):
			if self.lottery:
				self.lottery.BilgiGuncelle(totalep,win,loss)
		
		def SetLotteryListData(self, isim, miktar, renk):
			self.lottery.SetLotteryListData( isim, miktar, renk)
		
		def LotteryMakeGui(self):
			self.lottery.LotteryClearData()

## Find

hideWindows += self.wndMiniMap,

## Add Below

		if app.ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM:
			if self.lottery:
				hideWindows += self.lottery,

