import win32com.client

hwp = win32com.client.gencache.EnsureDispatch('HWPFrame.HwpObject')

# result 파일 생성후 저장
hwp.Run("FileNew")
hwp.Run("MoveDocBegin")
hwp.HAction.GetDefault('InsertText', hwp.HParameterSet.HInsertText.HSet)
hwp.HParameterSet.HInsertText.Text = '@'
hwp.HAction.Execute('InsertText', hwp.HParameterSet.HInsertText.HSet)
hwp.HAction.Run("BreakPara")
hwp.HAction.Run("BreakPara")