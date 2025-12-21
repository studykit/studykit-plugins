# MiniToolbarsample(VBA)

## Description

This sample demonstrates how to create sketch slot with minitoolbar.

## Code Samples

* [VBA](#VBA)

Have a sektch in edit mode before running below sample.

```
' This sample demonstrates creating sketch slot using mini-toolbar
Sub CreateSketchSlotSample()
    Dim oActiveEnv As Environment
    Set oActiveEnv = ThisApplication.UserInterfaceManager.ActiveEnvironment

    If oActiveEnv.InternalName <> "PMxPartSketchEnvironment" And _
        oActiveEnv.InternalName <> "AMxAssemblySketchEnvironment" And _
        oActiveEnv.InternalName <> "DLxDrawingSketchEnvironment" Then
        MsgBox "Please activate a sketch environment first!"
        Exit Sub
    End If

    Dim oMiniToolbar As MiniToolbar
    Set oMiniToolbar = ThisApplication.CommandManager.CreateMiniToolbar

    oMiniToolbar.ShowOK = True
    oMiniToolbar.ShowApply = True
    oMiniToolbar.ShowCancel = True

    Dim oControls As MiniToolbarControls
    Set oControls = oMiniToolbar.Controls
    oControls.Item("MTB_Options").Visible = False

    Dim oDescriptionLabel As MiniToolbarControl
    Set oDescriptionLabel = oControls.AddLabel("Description", "This toolbar is to create sketch slot:", "MiniToolbar sample to show how to create sketch slot.")
    oControls.AddNewLine

    ' Define the first center position.
    Dim oEndCenterOne As MiniToolbarButton
    Set oEndCenterOne = oControls.AddButton("FirstCenter: ", "First Center:     ", "Specify the first center of sketch slot")

    Dim oEndCenterOneX As MiniToolbarValueEditor
    Set oEndCenterOneX = oControls.AddValueEditor("FirstCenterX", "", kLengthUnits, "", "X:")
    oEndCenterOneX.Expression = "0"
    oEndCenterOneX.SetFocus

    Dim oEndCenterOneY As MiniToolbarValueEditor
    Set oEndCenterOneY = oControls.AddValueEditor("FirstCenterY", "", kLengthUnits, "", "Y:")
    oEndCenterOneY.Expression = "0"
    oControls.AddNewLine

    ' Define the second center position.
    Dim oEndCenterTwo As MiniToolbarButton
    Set oEndCenterTwo = oControls.AddButton("SecondCenter:", "Second Center:", "Specify the second center of sketch slot")

    Dim oEndCenterTwoX As MiniToolbarValueEditor
    Set oEndCenterTwoX = oControls.AddValueEditor("SecondCenterX", "", kLengthUnits, "", "X:")
    oEndCenterTwoX.Expression = "3"

    Dim oEndCenterTwoY As MiniToolbarValueEditor
    Set oEndCenterTwoY = oControls.AddValueEditor("SecondCenterY", "", kLengthUnits, "", "Y:")
    oEndCenterTwoY.Expression = "0"

    oControls.AddNewLine

    ' Define the width of sketch slot.
    Dim oWidthValue As MiniToolbarValueEditor
    Set oWidthValue = oControls.AddValueEditor("WidthValue", "", kLengthUnits, "", "Width:")
    oWidthValue.Expression = "1"

    ' Define if display the center line of sketch slot.
    Dim oDisplayCenterline As MiniToolbarCheckBox
    Set oDisplayCenterline = oControls.AddCheckBox("DisplayCenterline", "Display center line", "Check this to display center line of slot", True)

    ' Set the position of mini-toolbar
    Dim oPosition As Point2d
    Set oPosition = ThisApplication.TransientGeometry.CreatePoint2d(ThisApplication.ActiveView.Left, ThisApplication.ActiveView.Top)
    oMiniToolbar.Position = oPosition

    oMiniToolbar.Visible = True

    Dim oMiniToolbarEvents As New clsMiniToolbarEvents

    Call oMiniToolbarEvents.Init(oMiniToolbar)

End Sub

'*************************************************************
' The declarations and functions below need to be copied into
' a class module whose name is "clsMiniToolbarEvents". The name can be
' changed but you'll need to change the declaration in the
' calling function "CreateSketchSlotSample" to use the new name.
Private WithEvents m_EndCenterOneX As MiniToolbarValueEditor
Private WithEvents m_EndCenterOneY As MiniToolbarValueEditor
Private WithEvents m_EndCenterSecondX As MiniToolbarValueEditor
Private WithEvents m_EndCenterSecondY As MiniToolbarValueEditor
Private WithEvents m_Width As MiniToolbarValueEditor
Private WithEvents m_MiniToolbar As MiniToolbar
Private oDisplayCenterline As MiniToolbarCheckBox
Private m_Sketch As Sketch
Private bCenterline As Boolean
Private bStop As Boolean

Public Sub Init(oMiniToolbar As MiniToolbar)
    Set m_MiniToolbar = oMiniToolbar

    Set m_EndCenterOneX = m_MiniToolbar.Controls.Item("FirstCenterX")
    Set m_EndCenterOneY = m_MiniToolbar.Controls.Item("FirstCenterY")
    Set m_EndCenterSecondX = m_MiniToolbar.Controls.Item("SecondCenterX")
    Set m_EndCenterSecondY = m_MiniToolbar.Controls.Item("SecondCenterY")
    Set m_Width = m_MiniToolbar.Controls.Item("WidthValue")

    Set oDisplayCenterline = m_MiniToolbar.Controls.Item("DisplayCenterline")

    Set m_Sketch = ThisApplication.ActiveEditObject
    bStop = False

    Do
        ThisApplication.UserInterfaceManager.DoEvents

    Loop Until bStop

End Sub

Private Sub m_MiniToolbar_OnApply()
    CreateSlot
End Sub

Private Sub m_MiniToolbar_OnCancel()
    bStop = True

End Sub

Private Sub m_MiniToolbar_OnOK()
    bStop = True

    CreateSlot

End Sub

Private Sub CreateSlot()
    If Not (m_EndCenterOneX.IsExpressionValid And m_EndCenterOneY.IsExpressionValid And m_EndCenterSecondX.IsExpressionValid And m_EndCenterSecondY.IsExpressionValid) Then
        MsgBox "Invalid values for end center positions!"
        Exit Sub
    End If

    bCenterline = oDisplayCenterline.Checked

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oEndCenterOne As Point2d
    Dim oEndCenterTwo As Point2d

    ' Start transaction for creating slot.
    Dim oTransaction As Transaction
    Set oTransaction = ThisApplication.TransactionManager.StartTransaction(ThisApplication.ActiveDocument, "Create slot")

        ' If the two centers are vertical
        If Abs(m_EndCenterOneX.Value - m_EndCenterSecondX.Value) < 0.000001 Then
            If (m_EndCenterOneY.Value > m_EndCenterSecondY.Value) Then
                Set oEndCenterOne = oTG.CreatePoint2d(m_EndCenterOneX.Value, m_EndCenterOneY.Value)
                Set oEndCenterTwo = oTG.CreatePoint2d(m_EndCenterSecondX.Value, m_EndCenterSecondY.Value)
            Else
                Set oEndCenterOne = oTG.CreatePoint2d(m_EndCenterSecondX.Value, m_EndCenterSecondY.Value)
                Set oEndCenterTwo = oTG.CreatePoint2d(m_EndCenterOneX.Value, m_EndCenterOneY.Value)
            End If

            If oEndCenterOne.IsEqualTo(oEndCenterTwo, 0.000001) Then
                MsgBox "The two centers are coincident!"
                Exit Sub
            End If

            ' Create the top arc
            Set oEndArcOne = m_Sketch.SketchArcs.AddByCenterStartEndPoint(oEndCenterOne, oTG.CreatePoint2d(oEndCenterOne.X + 0.1, oEndCenterOne.Y), oTG.CreatePoint2d(oEndCenterOne.X - 0.1, oEndCenterOne.Y))
            ' Create the bottom arc
            Set oEndArcTwo = m_Sketch.SketchArcs.AddByCenterStartEndPoint(oEndCenterTwo, oTG.CreatePoint2d(oEndCenterTwo.X - 0.1, oEndCenterTwo.Y), oTG.CreatePoint2d(oEndCenterTwo.X + 0.1, oEndCenterTwo.Y))
        'If the two centers are not vertical
        Else
            If m_EndCenterOneX.Value < m_EndCenterSecondX.Value Then
                Set oEndCenterOne = oTG.CreatePoint2d(m_EndCenterOneX.Value, m_EndCenterOneY.Value)
                Set oEndCenterTwo = oTG.CreatePoint2d(m_EndCenterSecondX.Value, m_EndCenterSecondY.Value)
            ElseIf m_EndCenterOneX.Value > m_EndCenterSecondX.Value Then
                Set oEndCenterOne = oTG.CreatePoint2d(m_EndCenterSecondX.Value, m_EndCenterSecondY.Value)
                Set oEndCenterTwo = oTG.CreatePoint2d(m_EndCenterOneX.Value, m_EndCenterOneY.Value)
            End If

            If oEndCenterOne.IsEqualTo(oEndCenterTwo, 0.000001) Then
                MsgBox "The two centers are coincident!"
                Exit Sub
            End If

            Set oEndArcOne = m_Sketch.SketchArcs.AddByCenterStartEndPoint(oEndCenterOne, oTG.CreatePoint2d(m_EndCenterOneX.Value, m_EndCenterOneY.Value + 0.1), oTG.CreatePoint2d(m_EndCenterOneX.Value, m_EndCenterOneY.Value - 0.1))
            Set oEndArcTwo = m_Sketch.SketchArcs.AddByCenterStartEndPoint(oEndCenterTwo, oTG.CreatePoint2d(m_EndCenterSecondX.Value, m_EndCenterSecondY.Value + 0.1), oTG.CreatePoint2d(m_EndCenterSecondX.Value, m_EndCenterSecondY.Value - 0.1), False)

        End If

        Dim dWidth As Double
        dWidth = m_Width.Value

        ' Create center line if required
        If bCenterline Then
            Dim oCenterline As SketchLine
            Set oCenterline = m_Sketch.SketchLines.AddByTwoPoints(oEndArcOne.CenterSketchPoint, oEndArcTwo.CenterSketchPoint)

            oCenterline.Construction = True
        End If

        Dim oGround1 As GroundConstraint
        Dim oGround2 As GroundConstraint
        Set oGround1 = m_Sketch.GeometricConstraints.AddGround(oEndArcOne.CenterSketchPoint)
        Set oGround2 = m_Sketch.GeometricConstraints.AddGround(oEndArcTwo.CenterSketchPoint)

        ' Create sketch lines of slot
        Dim oLine1 As SketchLine
        Dim oLine2 As SketchLine
        Set oLine1 = m_Sketch.SketchLines.AddByTwoPoints(oEndArcOne.StartSketchPoint, oEndArcTwo.EndSketchPoint)
        Set oLine2 = m_Sketch.SketchLines.AddByTwoPoints(oEndArcOne.EndSketchPoint, oEndArcTwo.StartSketchPoint)

        ' Add geometric constraints to the sketch entities
        Call m_Sketch.GeometricConstraints.AddEqualRadius(oEndArcOne, oEndArcTwo)
        Call m_Sketch.GeometricConstraints.AddTangent(oLine1, oEndArcOne)
        Call m_Sketch.GeometricConstraints.AddTangent(oLine1, oEndArcTwo)
        Call m_Sketch.GeometricConstraints.AddTangent(oLine2, oEndArcOne)
        Call m_Sketch.GeometricConstraints.AddTangent(oLine2, oEndArcTwo)

        ' Add dimensional constraints to the sketch entities
        Dim oDiameter As DiameterDimConstraint
        Set oDiameter = m_Sketch.DimensionConstraints.AddDiameter(oEndArcOne, oEndArcOne.CenterSketchPoint.Geometry)
        oDiameter.Parameter.Value = dWidth

        ThisApplication.ActiveDocument.Update
        oDiameter.Delete
        oGround1.Delete
        oGround2.Delete

    oTransaction.End

End Sub
```
