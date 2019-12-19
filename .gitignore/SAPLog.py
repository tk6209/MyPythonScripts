
import sys, win32com.client

#-Connection--------------------------------------------------------------

SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine
connection = application.Children(0)
session = connection.Children(0)

session.findById("wnd[0]").maximize
session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "005"
session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "VTEIXEIR_BR"
session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "Vini@0718"
session.findById("wnd[0]").sendVKey(0)
session.findById("wnd[1]/usr/radMULTI_LOGON_OPT2").select()
session.findById("wnd[1]/tbar[0]/btn[0]").press()
session.findById("wnd[0]").close()
session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
session.findById("wnd[0]").sendVKey(0)

#-----------------------------------------------------------------------------
