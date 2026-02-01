# Adjust the brightness of lighting

## Description

This sample demonstrates how to adjust lighting brightness with mini-toolbar slider.

## Code Samples

* [VBA](#VBA)

```
Sub BrightnessAdjustSample()
    ' Open a part/assembly document before running below code
    If Not (ThisApplication.ActiveDocument Is Nothing) Then
        If ThisApplication.ActiveDocument.DocumentType = kPartDocumentObject Or ThisApplication.ActiveDocument.DocumentType = kAssemblyDocumentObject Then
            Dim ocls As New clsBrightnessAdjust
            ocls.Init
        Else
            MsgBox "Please activate/open a part or assembly for the demo!"
        End If
    Else
        MsgBox "Please open a part or assembly document first for the demo!"
    End If
End Sub

'*************************************************************
' The declarations and functions below need to be copied into
' a class module whose name is "clsBrightnessAdjust".  The name
' can be changed but you'll need to change the declaration in
' the calling function "BrightnessAdjustSample" to use the new name.
Private WithEvents m_MiniToolbar As MiniToolbar
Private WithEvents m_Brightness As MiniToolbarSlider
Private WithEvents m_AppEvents As ApplicationEvents

Private m_BrightAdjustTransaction As Transaction
Private m_LastBrightnessVal As Double

Private m_Doc As Document
Private m_ActiveLightingStyle As LightingStyle
Private bStop As Boolean
Private bInitSliderVal As Boolean

Public Sub Init()
    Set m_AppEvents = ThisApplication.ApplicationEvents

    Set m_Doc = ThisApplication.ActiveDocument
    Set m_ActiveLightingStyle = m_Doc.ActiveLightingStyle

    Set m_MiniToolbar = ThisApplication.CommandManager.CreateMiniToolbar
    Set m_Brightness = m_MiniToolbar.Controls.AddSlider("Light_Brightness", "Brightness", "Adjust light brightness", kDoubleType, 1, 0, 9, 10, 100)
    m_Brightness.AutoHide = True

    ' Hide the Apply button.
    m_MiniToolbar.ShowApply = False

    ' Display the minitoobar and place it to the top-left of the view.
    m_MiniToolbar.Visible = True
    m_MiniToolbar.Position = ThisApplication.TransientGeometry.CreatePoint2d(0, 0)

    bInitSliderVal = True

    ' Remember the last brightness value
    m_LastBrightnessVal = m_ActiveLightingStyle.Brightness

    bStop = False

    Set m_BrightAdjustTransaction = ThisApplication.TransactionManager.StartTransaction(m_Doc, "Adjust brightness")

    Do
        If bInitSliderVal Then
            m_Brightness.Value = m_ActiveLightingStyle.Brightness
        End If
        ThisApplication.UserInterfaceManager.DoEvents
    Loop Until bStop

End Sub

Private Sub m_Brightness_OnValueChange()
    ' Ignore this event when the MiniToolbar value change is initialized by switching active LightingStyle
    If Not bInitSliderVal Then
        'bChangedBySlider = True
        m_ActiveLightingStyle.Brightness = m_Brightness.Value
    End If
    bInitSliderVal = False
    m_Doc.Views(1).Update

End Sub

' Cancel the brightness change
Private Sub m_MiniToolbar_OnCancel()
    bStop = True
    m_BrightAdjustTransaction.Abort
    m_Doc.Views(1).Update
End Sub

' If the brightness is changed, update the LightingStyle for this value.
Private Sub m_MiniToolbar_OnOK()
    bStop = True

    If m_LastBrightnessVal = m_ActiveLightingStyle.Brightness Then
        m_BrightAdjustTransaction.Abort
        m_Doc.Views(1).Update
    Else
        m_BrightAdjustTransaction.End
        m_Doc.Views(1).Update
    End If
End Sub
```
