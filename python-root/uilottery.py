import ui
import dbg
import app
import fRaC_Fa4AP3cA1
import IfB_R2AcVfAPa1c
import time
import rRCvfR4c_fL4e
import Dr1vC_kQfStEqAvCx
import constInfo
import uiCommon
import datetime
import wndMgr

PATH = 'd:/ymir work/loterry/'
LEGEND_TEXT = ['Yeþil Ot: x14 Ep Kazanýrsýnýz.', 'Kýrmýzý Ot: x2 Ep Kazanýrsýnýz.', 'Mavi Ot: x2 Ep Kazanýrsýnýz.']

ROLLCOUNT = 51
			   
# key : [vNum, type_border, count]
ITEMS = {
###	num	category	vnum	count
	0	:	[0,	70253,	1],
	1	:	[0,	70251,	25],
	2	:	[0,	70252,	25],
}

class LotteryWindow(ui.Window):
	_background = None
	_titleBackground55 = None
	ortabg = None
	ortabg2 = None
	ortabg3 = None
	_titleText = None
	_titleText2b = None
	_titleText22 = None
	_titleText2 = None
	_titleBackground22 = None
	_titleBackground222 = None
	_titleBackground2 = None
	ortabg = None
	_infoText_1 = None
	_infoText_2 = None
	_infoText_3 = None
	_wasRandomText = None
	_wasRandomText2 = None
	_wasRandomText3 = None
	_wasRandomText34 = None
	_wasRandomText3412 = None
	_wasRandom = None
	_wasRandom2 = None
	_wasRandom25 = None
	_wasRandom2545 = None
	_wasRandom254 = None
	tutar = None
	_backgroundCards = None
	_rollLP = -1
	_cards = []
	_startLottery = FALSE

	def __init__(self):
		ui.Window.__init__(self)
		self.SetWindowName("Lottery")
		self.listLotteryData = []
		self.starttimesearch = 0
		self.WarteGar = 0

	def __del__(self):
		ui.Window.__del__(self)
		self.Destroy()

	def LoadWindow(self):
		self.Board = ui.DragonBoardWithTitleBar()
		if app.ENABLE_WINDOW_SLIDE_EFFECT:
			self.EnableSlidingEffect()
		self.SetMainBoard()
		self.SetInterface()
		# self.__MakeListUI()
		self.MakeOrta()
		self.WarteGar = SureDialog()
		self.WarteGar.Hide()

	def MakeOrta(self):
		self.ortabg = ui.ExpandedImageBox()
		self.ortabg.SetParent(self.Board)
		self.ortabg.SetPosition(10, 245)
		self.ortabg.LoadImage(PATH + 'legend-bg.tga')
		self.ortabg.Show()
		
		self._titleBackground2 = ui.ExpandedImageBox()
		self._titleBackground2.SetParent(self.Board)
		self._titleBackground2.SetPosition(20, 255)
		self._titleBackground2.LoadImage(PATH + 'legend-title.tga')
		self._titleBackground2.Show()
		
		self._titleText = ui.TextLine()
		self._titleText.SetParent(self._titleBackground2)
		self._titleText.SetPosition(int(self._titleBackground2.GetWidth() / 2), 0)
		self._titleText.SetText("Kýrmýzý Ýsim Listesi")
		self._titleText.SetHorizontalAlignCenter()
		self._titleText.Show()
		
		self.ortabg2 = ui.ExpandedImageBox()
		self.ortabg2.SetParent(self.Board)
		self.ortabg2.SetPosition(310, 245)
		self.ortabg2.LoadImage(PATH + 'legend-bg.tga')
		self.ortabg2.Show()
		
		self._titleBackground22 = ui.ExpandedImageBox()
		self._titleBackground22.SetParent(self.Board)
		self._titleBackground22.SetPosition(320, 255)
		self._titleBackground22.LoadImage(PATH + 'legend-title.tga')
		self._titleBackground22.Show()
		
		self._titleText2 = ui.TextLine()
		self._titleText2.SetParent(self._titleBackground22)
		self._titleText2.SetPosition(int(self._titleBackground22.GetWidth() / 2), 0)
		self._titleText2.SetText("Yeþil Ýsim Listesi")
		self._titleText2.SetHorizontalAlignCenter()
		self._titleText2.Show()
		
		self.ortabg3 = ui.ExpandedImageBox()
		self.ortabg3.SetParent(self.Board)
		self.ortabg3.SetPosition(615, 245)
		self.ortabg3.LoadImage(PATH + 'legend-bg.tga')
		self.ortabg3.Show()
		
		self._titleBackground222 = ui.ExpandedImageBox()
		self._titleBackground222.SetParent(self.Board)
		self._titleBackground222.SetPosition(625, 255)
		self._titleBackground222.LoadImage(PATH + 'legend-title.tga')
		self._titleBackground222.Show()
		
		self._titleText22 = ui.TextLine()
		self._titleText22.SetParent(self._titleBackground222)
		self._titleText22.SetPosition(int(self._titleBackground222.GetWidth() / 2), 0)
		self._titleText22.SetText("Mavi Ýsim Listesi")
		self._titleText22.SetHorizontalAlignCenter()
		self._titleText22.Show()
		
		self._titleText2b = ui.ThinBoard()
		self._titleText2b.SetParent(self.Board)
		self._titleText2b.SetSize(920, 25)
		self._titleText2b.SetPosition(10, 420)
		self._titleText2b.Show()
		
		self._wasRandomText3 = ui.TextLine()
		self._wasRandomText3.SetParent(self._titleText2b)
		self._wasRandomText3.SetPosition(20, 9)
		self._wasRandomText3.SetText("Toplam Oynanan Ep Miktarý:")
		self._wasRandomText3.Show()

		self._wasRandomSlotBar23 = ui.SlotBar()
		self._wasRandomSlotBar23.SetParent(self._titleText2b)
		self._wasRandomSlotBar23.SetSize(90, 20)
		self._wasRandomSlotBar23.SetPosition(150, 5)
		self._wasRandomSlotBar23.Show()
		self._wasRandom25 = ui.TextLine()
		self._wasRandom25.SetParent(self._wasRandomSlotBar23)
		self._wasRandom25.SetSize(90, 20)
		self._wasRandom25.SetPosition((self._wasRandomSlotBar23.GetWidth()/2), 4)
		self._wasRandom25.SetLimitWidth(90)
		self._wasRandom25.SetText("0 EP")
		self._wasRandom25.SetHorizontalAlignCenter()
		self._wasRandom25.Show()
		
		self._wasRandomText34 = ui.TextLine()
		self._wasRandomText34.SetParent(self._titleText2b)
		self._wasRandomText34.SetPosition(700, 9)
		self._wasRandomText34.SetText("Kazanma:")
		self._wasRandomText34.Show()

		self._wasRandomSlotBar234 = ui.SlotBar()
		self._wasRandomSlotBar234.SetParent(self._titleText2b)
		self._wasRandomSlotBar234.SetSize(50, 20)
		self._wasRandomSlotBar234.SetPosition(750, 5)
		self._wasRandomSlotBar234.Show()
		self._wasRandom2545 = ui.TextLine()
		self._wasRandom2545.SetParent(self._wasRandomSlotBar234)
		self._wasRandom2545.SetSize(50, 20)
		self._wasRandom2545.SetPosition((self._wasRandomSlotBar234.GetWidth()/2), 4)
		self._wasRandom2545.SetLimitWidth(90)
		self._wasRandom2545.SetText("0")
		self._wasRandom2545.SetHorizontalAlignCenter()
		self._wasRandom2545.Show()
		
		self._wasRandomText3412 = ui.TextLine()
		self._wasRandomText3412.SetParent(self._titleText2b)
		self._wasRandomText3412.SetPosition(810, 9)
		self._wasRandomText3412.SetText("Kaybetme:")
		self._wasRandomText3412.Show()

		self._wasRandomSlotBar2343 = ui.SlotBar()
		self._wasRandomSlotBar2343.SetParent(self._titleText2b)
		self._wasRandomSlotBar2343.SetSize(50, 20)
		self._wasRandomSlotBar2343.SetPosition(860, 5)
		self._wasRandomSlotBar2343.Show()
		self._wasRandom254 = ui.TextLine()
		self._wasRandom254.SetParent(self._wasRandomSlotBar2343)
		self._wasRandom254.SetSize(50, 20)
		self._wasRandom254.SetPosition((self._wasRandomSlotBar2343.GetWidth()/2), 4)
		self._wasRandom254.SetLimitWidth(90)
		self._wasRandom254.SetText("0")
		self._wasRandom254.SetHorizontalAlignCenter()
		self._wasRandom254.Show()
		
		self.kirmiziButton = ui.Button()
		self.kirmiziButton.SetParent(self.Board)
		self.kirmiziButton.SetPosition(15, 205)
		self.kirmiziButton.SetUpVisual('d:/ymir work/loterry/kirmizi.png')
		self.kirmiziButton.SetOverVisual('d:/ymir work/loterry/kirmizi2.png')
		self.kirmiziButton.SetDownVisual('d:/ymir work/loterry/kirmizi3.png')
		self.kirmiziButton.SetEvent(self.PlayGameRed)
		self.kirmiziButton.Show()
		
		self.yesilButton = ui.Button()
		self.yesilButton.SetParent(self.Board)
		self.yesilButton.SetPosition(315, 205)
		self.yesilButton.SetUpVisual('d:/ymir work/loterry/yesil.png')
		self.yesilButton.SetOverVisual('d:/ymir work/loterry/yesil1.png')
		self.yesilButton.SetDownVisual('d:/ymir work/loterry/yesil2.png')
		self.yesilButton.SetEvent(self.PlayGameYesil)
		self.yesilButton.Show()
		
		self.maviButton = ui.Button()
		self.maviButton.SetParent(self.Board)
		self.maviButton.SetPosition(615, 205)
		self.maviButton.SetUpVisual('d:/ymir work/loterry/mavi.png')
		self.maviButton.SetOverVisual('d:/ymir work/loterry/mavi2.png')
		self.maviButton.SetDownVisual('d:/ymir work/loterry/mavi3.png')
		self.maviButton.SetEvent(self.PlayGameMavi)
		self.maviButton.Show()
		
	def SetMainBoard(self):
		self.Board.SetSize(940, 465)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('Kumar Sistemi')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Hide()
	
	def PlayGameRed(self):
		inputDialogRed = uiCommon.InputDialog()
		inputDialogRed.SetTitle("Ne kadar EP oynamak istiyorsun?")
		inputDialogRed.SetMaxLength(6)
		inputDialogRed.SetAcceptEvent(ui.__mem_func__(self.RedOkey))
		inputDialogRed.SetCancelEvent(ui.__mem_func__(self.RedClose))
		inputDialogRed.Open()
		self.inputDialogRed = inputDialogRed

	def RedOkey(self):
		if not self.inputDialogRed:
			return True

		if not len(self.inputDialogRed.GetText()):
			return True

		fRaC_Fa4AP3cA1.SendChatPacket("/lottery_draw "+str(self.inputDialogRed.GetText())+" 1")# done
		
		self.inputDialogRed = None
		
	def RedClose(self):
		self.inputDialogRed = None
		return True
	
	def PlayGameYesil(self):
		inputDialogYesil = uiCommon.InputDialog()
		inputDialogYesil.SetTitle("Ne kadar EP oynamak istiyorsun?")
		inputDialogYesil.SetMaxLength(6)
		inputDialogYesil.SetAcceptEvent(ui.__mem_func__(self.YesilOkey))
		inputDialogYesil.SetCancelEvent(ui.__mem_func__(self.YesilClose))
		inputDialogYesil.Open()
		self.inputDialogYesil = inputDialogYesil
	
	def YesilOkey(self):
		if not self.inputDialogYesil:
			return True

		if not len(self.inputDialogYesil.GetText()):
			return True

		fRaC_Fa4AP3cA1.SendChatPacket("/lottery_draw "+str(self.inputDialogYesil.GetText())+" 0")# done
		self.inputDialogYesil = None
	
	def YesilClose(self):
		self.inputDialogYesil = None
		return True
	
	def PlayGameMavi(self):
		inputDialogMavi = uiCommon.InputDialog()
		inputDialogMavi.SetTitle("Ne kadar EP oynamak istiyorsun?")
		inputDialogMavi.SetMaxLength(6)
		inputDialogMavi.SetAcceptEvent(ui.__mem_func__(self.MaviOkey))
		inputDialogMavi.SetCancelEvent(ui.__mem_func__(self.MaviClose))
		inputDialogMavi.Open()
		self.inputDialogMavi = inputDialogMavi
	
	def MaviOkey(self):
		if not self.inputDialogMavi:
			return True

		if not len(self.inputDialogMavi.GetText()):
			return True

		fRaC_Fa4AP3cA1.SendChatPacket("/lottery_draw "+str(self.inputDialogMavi.GetText())+" 2")# done
	
		self.inputDialogMavi = None
		
	def MaviClose(self):
		self.inputDialogMavi = None
		return True

	def SetInterface(self):
		self.SetBackgroundCards(self.Board)
		self.SetCardsPreview()
		self.arrow = ui.ExpandedImageBox()
		self.arrow.SetParent(self.Board)
		self.arrow.SetPosition(470, 35)
		self.arrow.LoadImage(PATH + 'arrow.tga')
		self.arrow.Show()

	def SecondToHM(time):
		second = int(time % 60)
		minute = int((time / 60) % 60)
		hour = int((time / 60) / 60) % 24

		if hour <= 0:
			return "%d DK %02d SN" % (minute, second)
		else:
			return "%d Saat %02d Dakika %02d Saniye" % (hour, minute, second)

	def SecondStart(self,second):
		if self.Board.IsShow():
			self.WarteGar.Open(float(second),time.clock())
		else:
			self.WarteGar.Open(float(second),time.clock())
			self.WarteGar.Hide()

		# rRCvfR4c_fL4e.AppendChat(rRCvfR4c_fL4e.CHAT_TYPE_INFO, "SecondStart: "+str(second))
		# self._wasRandom2.SetText(str(second)+" SN")
	
	def BilgiGuncelle(self,totalep,win,loss):
		self._wasRandom25.SetText(str(totalep)+ " EP")
		self._wasRandom2545.SetText(str(win))
		self._wasRandom254.SetText(str(loss))

	def __MakeListUI(self):
		# rRCvfR4c_fL4e.AppendChat(rRCvfR4c_fL4e.CHAT_TYPE_INFO, "Data Length: " + str(len(self.listLotteryData)))
		self.data = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []}
		yPos = 15
	
		for key in xrange(len(self.listLotteryData)):
			final_new_menu = list(dict.fromkeys(self.listLotteryData))
			# rRCvfR4c_fL4e.AppendChat(1," 2 for loop "+ str(constInfo.DATA_KEY_LOTTERY_LIST))
			new_key = int(key)+1
			(arg1, arg2, arg3) = final_new_menu[key]

			self.rankNumberTextLine2 = ui.TextLine()

			if int(arg3) == 0: 
				self.rankNumberTextLine2.SetParent(self._titleBackground22)
				self.rankNumberTextLine2.SetPosition(10, yPos)
				yPos += 20
			elif int(arg3) == 1:
				self.rankNumberTextLine2.SetParent(self._titleBackground2)
				self.rankNumberTextLine2.SetPosition(10, yPos)
				yPos += 20
			elif int(arg3) == 2:
				self.rankNumberTextLine2.SetParent(self._titleBackground222)
				self.rankNumberTextLine2.SetPosition(10, yPos)
				yPos += 20

			self.rankNumberTextLine2.SetText("Ýsim: "+str(arg1)+" Miktar:"+str(arg2))
			self.rankNumberTextLine2.Show()
			# rRCvfR4c_fL4e.AppendChat(1,str(int(arg3))+ " kayýt liste ekle")
			
			self.data[new_key].append(self.rankNumberTextLine2)

	def SetLegend(self):
		self.Legend = Legend(self.Board)

	def SetLottery(self):
		self.SetBackground(self.Board)
		self.SetTitleBackground()
		self.SetTitleText()
		self.SetTextInfo()
		self.SetWasRandom()
		self.SetToRandom()
		self.SetRewardButton()

	def SetBackground(self, parent):
		self._background = ui.ExpandedImageBox()
		self._background.SetParent(parent)
		self._background.SetPosition(475, 405)
		self._background.LoadImage(PATH + 'lottery-bg.tga')
		self._background.Show()

	def SetTitleBackground(self):
		self._titleBackground55 = ui.ExpandedImageBox()
		self._titleBackground55.SetParent(self._background)
		self._titleBackground55.SetPosition(14, 13)
		self._titleBackground55.LoadImage(PATH + 'lottery-title.tga')
		self._titleBackground55.Show()

	def SetTitleText(self):
		self._titleText = ui.TextLine()
		self._titleText.SetParent(self._titleBackground55)
		self._titleText.SetPosition(int(self._titleBackground55.GetWidth() / 2), 0)
		self._titleText.SetText("Bilgi")
		self._titleText.SetHorizontalAlignCenter()
		self._titleText.Show()

	def SetTextInfo(self):
		self._infoText_1 = ui.TextLine()
		self._infoText_1.SetParent(self._background)
		self._infoText_1.SetPosition(16, 33)
		self._infoText_1.SetText("Kumara baþlamak için renk seçmelisiniz.")
		self._infoText_1.Show()

		self._infoText_2 = ui.TextLine()
		self._infoText_2.SetParent(self._background)
		self._infoText_2.SetPosition(16, 55)
		self._infoText_2.SetText("Seçtiðiniz rengin ardýndan oynayacaðýnýz miktarý girip devam ediniz.")
		self._infoText_2.Show()
		
		self._infoText_3 = ui.TextLine()
		self._infoText_3.SetParent(self._background)
		self._infoText_3.SetPosition(16, 78)
		self._infoText_3.SetText("Yukarýdaki saniye bittiðinde otomatikmen baþlayacaktýr.")
		self._infoText_3.Show()

	def SetBackgroundCards(self, parent):
		self._backgroundCards = ui.ExpandedImageBox()
		self._backgroundCards.SetParent(parent)
		self._backgroundCards.SetPosition(80, 30)
		self._backgroundCards.LoadImage(PATH + 'card-bg.tga')
		self._backgroundCards.Show()

	def SetRewardButton(self):
		self._rewardButton = ui.Button()
		self._rewardButton.SetParent(self._background)
		self._rewardButton.SetPosition(350, 105)
		self._rewardButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
		self._rewardButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
		self._rewardButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
		self._rewardButton.SetText('Ödülü Al')
		self._rewardButton.SetEvent(self.RewardItem)

	def RewardBtnToggle(self):
		if self._rewardButton.IsShow():
			self._rewardButton.Hide()
		else:
			self._rewardButton.Show()

	def RewardItem(self):
		pass

	def SetCardsPreview(self):
		for x in xrange(7):
			item = ITEMS[app.GetRandom(0, len(ITEMS) - 1) ]
			self._cards.append(CardLottery(self._backgroundCards, x, item))  # (parent, index, itemVnum, border)

	# def SetWasRandomAmount(self,amunt=1):
		# self._wasRandom.SetText("%d EP" % int(Dr1vC_kQfStEqAvCx.GetDragonCoin()))

	def RollComand(self):
		if constInfo.LastColor == 0:
			rRCvfR4c_fL4e.AppendChat(rRCvfR4c_fL4e.CHAT_TYPE_INFO, "Renk seçilmedi.")
			return
		fRaC_Fa4AP3cA1.SendChatPacket("/lottery_draw "+str(self.tutar.GetText())+" "+str(constInfo.LastColor)) # done
	
	def Roll(self, speed=1):
		if self.IsLp():
			self._startLottery = TRUE
			self.InitRoll()
			# self.SetWasRandomAmount()
			self.speed = 40
			self.deley = 0.001
			self.amountCards = len(self._cards)-2
			self.StartRoll()

	def IsLp(self):
		if self._rollLP == -1:
			return FALSE
		else:
			return TRUE

	def InitRollLP(self, lp):
		
		# rRCvfR4c_fL4e.AppendChat(rRCvfR4c_fL4e.CHAT_TYPE_INFO, "Gelen: "+str(lp))
		lp = int(lp)

		if ITEMS.has_key(lp):
			if lp != -1:
				self._rollLP = lp
				
		self.Roll()
	
	def LotteryClearData(self):
		del self.listLotteryData[:]
		# del self.data[:]
		self.rankNumberTextLine2.SetText("")
		self.rankNumberTextLine2 = None
		constInfo.DATA_KEY_LOTTERY_LIST = 0
	
	def SetLotteryListData(self, isim,miktar,renk):
		key = constInfo.DATA_KEY_LOTTERY_LIST
		data = (isim,miktar,renk)
		self.listLotteryData.append(data)
		constInfo.DATA_KEY_LOTTERY_LIST += 1
		
		# rRCvfR4c_fL4e.AppendChat(1,"1 Gelen Kayýt: "+str(isim)+" Miktar:"+ str(miktar)) #çek board
		
		self.__MakeListUI()


	def InitRoll(self):
		if self.IsLp():
			del self._cards[:]
			for x in xrange(ROLLCOUNT):
				self._cards.append(CardLottery(self._backgroundCards, x, ITEMS[app.GetRandom(0, len(ITEMS)-1)]))
			self._cards.append(CardLottery(self._backgroundCards, ROLLCOUNT, ITEMS[self._rollLP]))
			for x in xrange(5):
				self._cards.append(CardLottery(self._backgroundCards, x + ROLLCOUNT + 1, ITEMS[app.GetRandom(0, len(ITEMS)-1)]))

	def StartRoll(self):
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(float(self.deley))

		if self._cards[ROLLCOUNT].IsDrawn():
			for x in xrange(ROLLCOUNT - 1 + 6):
				self._cards[x].Roll(self.speed)

			if 400 < self._cards[int(self.amountCards * 0.1)]._positionX < 600:
				self.speed = 40
			if 400 < self._cards[int(self.amountCards * 0.8)]._positionX < 600:
				self.speed = 34
			if 400 < self._cards[int(self.amountCards * 0.85)]._positionX < 600:
				self.speed = 28
			if 400 < self._cards[int(self.amountCards * 0.86)]._positionX < 600:
				self.speed = 22
			if 400 < self._cards[int(self.amountCards * 0.865)]._positionX < 600:
				self.speed = 16
			if 400 < self._cards[int(self.amountCards * 0.875)]._positionX < 600:
				self.speed = 13
			if 400 < self._cards[int(self.amountCards * 0.88)]._positionX < 600:
				self.speed = 10
			if 400 < self._cards[int(self.amountCards * 0.905)]._positionX < 600:
				self.speed = 8
			if 400 < self._cards[int(self.amountCards * 0.92)]._positionX < 600:
				self.speed = 6
				self.deley = 0.01
			if 400 < self._cards[int(self.amountCards * 0.935)]._positionX < 600:
				self.speed = 5
			if 400 < self._cards[int(self.amountCards * 0.95)]._positionX < 600:
				self.speed = 4
			if 400 < self._cards[int(self.amountCards * 0.96)]._positionX < 600:
				self.speed = 3
			if 400 < self._cards[int(self.amountCards * 0.97)]._positionX < 600:
				self.speed = 2
			if 400 < self._cards[int(self.amountCards * 0.98)]._positionX < 600:
				self.speed = 2
				self.deley = 0.02
			if 400 < self._cards[int(self.amountCards * 0.99)]._positionX < 600:
				self.speed = 1

			self.WarteSchleife.SAFE_SetTimeOverEvent(self.StartRoll)
		else:
			self.ShowAward()

	def ShowAward(self):
		fRaC_Fa4AP3cA1.SendChatPacket("/lottery_withdraw_reward")
		self._rollLP = -1

	def Destroy(self):
		pass
		# del self._background
		# del self._titleBackground55
		# del self.ortabg
		# del self.ortabg2
		# del self.ortabg3
		# del self._titleText
		# del self._titleText2b
		# del self._titleText22
		# del self._titleText2
		# del self._titleBackground22
		# del self._titleBackground222
		# del self._titleBackground2
		# del self._infoText_1
		# del self._infoText_2
		# del self._infoText_3
		# del self._wasRandomText
		# del self._wasRandomText2
		# del self._wasRandomText3
		# del self._wasRandomText34
		# del self._wasRandomText3412
		# del self._wasRandom
		# del self._wasRandom2
		# del self._wasRandom25
		# del self._wasRandom2545
		# del self._wasRandom254
		# del self.tutar
		# del self._backgroundCards
		# del self._cards[:]
		# del self.Board

	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
			self.WarteGar.Hide()
		else:
			self.Board.Show()
			self.WarteGar.Shows()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Close(self):
		listLotteryData = []
		constInfo.DATA_KEY_LOTTERY_LIST = 0
		if self.Board:
			self.Board.Hide()
		if self.WarteGar:
			self.WarteGar.Close()

	def Open(self):
		if self.Board:
			self.Board.Show()

class CardLottery:
	_background = None
	_item = None
	_border = None
	_count = None
	toolTip = None
	_index = None
	_itemVnum = None
	_typeBorder = None
	_positionX = None
	_winCard = FALSE
	_img = None
	
	def __init__(self, parent, index, item):
		self._index = index
		self._itemVnum = item[1]
		self._typeBorder = item[0]
		self._count = item[2]
		self._positionX = 40 + (self._index * 105)
		if self._index is ROLLCOUNT:
			self._winCard = TRUE
		self.SetBackground(parent)
		self.SetItem()
		self.SetBorder()

	def __del__(self):
		self.Destroy()

	def SetBackground(self, parent):
		self._background = ui.ExpandedImageBox()
		self._background.SetParent(parent)
		self._background.SetPosition(self._positionX, 28)
		self._background.LoadImage(PATH + 'card.tga')
		if self._positionX - 2 > 775:
			self._background.Hide()
		else:
			self._background.Show()

	def SetItem(self):
		self._item = ui.ExpandedImageBox()
		self._item.SetParent(self._background)
		IfB_R2AcVfAPa1c.SelectItem(self._itemVnum)
		try:
			self._img = IfB_R2AcVfAPa1c.GetIconImageFileName()
			self._item.LoadImage(self._img)
			if self._item.GetHeight() <= 32:
				self._item.SetPosition(int(self._background.GetWidth() / 2) - 16,
									   int(self._background.GetHeight() / 2) - 16)
			elif self._item.GetHeight() <= 64:
				self._item.SetPosition(int(self._background.GetWidth() / 2) - 16,
									   int(self._background.GetHeight() / 2) - 32)
			elif self._item.GetHeight() <= 96:
				self._item.SetPosition(int(self._background.GetWidth() / 2) - 16,
									   int(self._background.GetHeight() / 2) - 48)
		except:
			dbg.TraceError("No found item")
			self._item.LoadImage(PATH + '03150.tga')

		if self._positionX - 2 > 775:
			self._item.Hide()
		else:
			self._item.Show()

	def SetBorder(self):
		self._border = ui.ExpandedImageBox()
		self._border.SetParent(self._background)
		self._border.SetPosition(-2, -2)
		self._border.LoadImage(PATH + 'card-border-' + str(5-self._typeBorder + 1) + '.tga')
		if self._positionX - 2 > 775:
			self._border.Hide()
		else:
			self._border.Show()

		self._coutText = ui.TextLine()
		self._coutText.SetParent(self._item)
		self._coutText.SetPosition(int(self._item.GetWidth())-2,int(self._item.GetHeight())-2)
		self._coutText.SetText(str(self._count))
		self._coutText.SetFontName("Tahoma:11")
		if self._positionX - 2 > 775:
			self._coutText.Hide()
		else:
			if self._count == 1:
				self._coutText.Hide()
			else:
				self._coutText.Show()

	def IsDrawn(self):
		if self._winCard is TRUE and self._positionX > 360+((time.clock()%60)-30):
			return TRUE
		else:
			return FALSE
			
	def HideItems(self):
		self._border.Hide()
		self._background.Hide()
		self._item.Hide()

	def ShowItems(self):
		self._background.Show()
		self._item.Show()
		self._border.Show()

	def Roll(self, speed=1):
		if self._positionX - speed > -108:
			self._positionX = self._positionX - speed
			self._background.SetPosition(self._positionX, 28)
			if 695 < self._positionX < 776:
				Percent = float((776.0-self._positionX) / float(self._border.GetWidth())) - 1.0
				self._border.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self._background.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self._item.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self.ShowItems()
			if 300 < self._positionX <= 695:
				self._border.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
				self._background.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
				self._item.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			if 12 > self._positionX  and self._positionX >= -68:
				Percent = float(abs(self._positionX-12) / float(self._border.GetWidth()))
				self._border.SetRenderingRect(0.0-Percent,0.0, 0.0, 0.0)
				self._background.SetRenderingRect(0.0-Percent,0.0, 0.0, 0.0)
				self._item.SetRenderingRect(0.0-Percent-0.16,0.0, 0.0, 0.0)
				self.ShowItems()
			elif self._positionX < -68:
				self.HideItems()

	def Destroy(self):
		del self._index
		del self._count
		del self._border
		del self._item
		del self._background
		del self._typeBorder
		del self._itemVnum
		del self._img

class SureDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None
		self._wasRandom = None
		self._wasRandom2 = 0
		self.timer = 0
		self.starttimesearch = 0
		
		self._wasRandomText = ui.TextLine()
		self._wasRandomText.SetParent(self)
		self._wasRandomText.SetPosition(wndMgr.GetScreenWidth()-120, 200)
		self._wasRandomText.SetText("Mevcut Epin:")
		self._wasRandomText.Show()

		self._wasRandomSlotBar = ui.SlotBar()
		self._wasRandomSlotBar.SetParent(self)
		self._wasRandomSlotBar.SetSize(75, 20)
		self._wasRandomSlotBar.SetPosition(wndMgr.GetScreenWidth()-120, 225)
		self._wasRandomSlotBar.Show()
		self._wasRandom = ui.TextLine()
		self._wasRandom.SetParent(self._wasRandomSlotBar)
		self._wasRandom.SetSize(90, 20)
		self._wasRandom.SetPosition((self._wasRandomSlotBar.GetWidth()/2), 4)
		self._wasRandom.SetLimitWidth(90)
		self._wasRandom.SetText("%d EP" % int(Dr1vC_kQfStEqAvCx.GetDragonCoin()))
		self._wasRandom.SetHorizontalAlignCenter()
		self._wasRandom.Show()
		
		self._wasRandomText2 = ui.TextLine()
		self._wasRandomText2.SetParent(self)
		self._wasRandomText2.SetPosition(wndMgr.GetScreenWidth()-120, 250)
		self._wasRandomText2.SetText("Oyun Baþlamasýna Kalan:")
		self._wasRandomText2.Show()

		self._wasRandomSlotBar2 = ui.SlotBar()
		self._wasRandomSlotBar2.SetParent(self)
		self._wasRandomSlotBar2.SetSize(90, 20)
		self._wasRandomSlotBar2.SetPosition(wndMgr.GetScreenWidth()-120, 275)
		self._wasRandomSlotBar2.Show()
		self._wasRandom2 = ui.TextLine()
		self._wasRandom2.SetParent(self._wasRandomSlotBar2)
		self._wasRandom2.SetSize(90, 20)
		self._wasRandom2.SetPosition((self._wasRandomSlotBar2.GetWidth()/2), 4)
		self._wasRandom2.SetLimitWidth(90)
		self._wasRandom2.SetText("60 SN")
		self._wasRandom2.SetHorizontalAlignCenter()
		self._wasRandom2.Show()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, timer, clock):
		self.starttimesearch = clock
		
		
		
		self.timer = timer

		self.Show()

	def Shows(self):
		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)

	def OnUpdate(self):
		# rRCvfR4c_fL4e.AppendChat(rRCvfR4c_fL4e.CHAT_TYPE_INFO, "On Update Func")
		self._wasRandom.SetText("%d EP" % int(Dr1vC_kQfStEqAvCx.GetDragonCoin()))
		# timer = time.clock() - self.timer
		# self._wasRandom2.SetText(str(self.timer)+" SN")
		
		timerfs = time.clock() - self.starttimesearch
		
		b = datetime.timedelta(seconds=60)
		
		a = datetime.timedelta(seconds=timerfs)
		self._wasRandom2.SetText(str(a)+ " SN")
		if a >= b:
			self.starttimesearch = time.clock()
			# self.deadguage.Hide()
			# self.deadguagetext.Hide()
			# self.counterstartdead = 0

	def OnPressExitKey(self):
		self.Close()
		return TRUE

class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)

	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return

	def OnPressExitKey(self):
		self.Close()
		return TRUE
