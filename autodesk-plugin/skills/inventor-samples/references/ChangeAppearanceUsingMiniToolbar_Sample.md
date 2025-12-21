# Change color of part, features or faces

## Description

This sample demonstrates how to use MiniToolBar to change appearance color of part or features or faces.

## Code Samples

* [VBA](#VBA)

You can either run below sample with an open part document or it will create a new part document.

```
' This sample demonstrates how to change colors using mini-toolbar
Sub ChangeAppearanceMiniToolbarSample()
    Dim oDoc As PartDocument
    If Not (ThisApplication.ActiveDocument Is Nothing) Then
        If ThisApplication.ActiveDocument.DocumentType = kPartDocumentObject Then
            If (MsgBox("Would you like to create new appearance assets with active document?", vbYesNo, "Autodesk Inventor Prompt") = vbYes) Then
                Set oDoc = ThisApplication.ActiveDocument
            Else
                Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

                ' Create a block
                Call CreateSolids(oDoc)
            End If
        End If
    Else
        Set oDoc = ThisApplication.Documents.Add(kPartDocumentObject)

        ' Create a block
        Call CreateSolids(oDoc)
    End If

    ' Create seven appearances for use
    Call CreateColors(oDoc)
    Dim oCamera As Camera
    Set oCamera = oDoc.Views(1).Camera

    oCamera.Fit
    oCamera.Apply

    Dim oMiniToolbarEvents As New clsColorChange

    Call oMiniToolbarEvents.Init(oDoc)

End Sub

Private Sub CreateSolids(oDoc As PartDocument)
    Dim oSk As PlanarSketch
    Set oSk = oDoc.ComponentDefinition.Sketches.Add(oDoc.ComponentDefinition.WorkPlanes(3))

    Call oSk.SketchLines.AddAsTwoPointRectangle(ThisApplication.TransientGeometry.CreatePoint2d(-2, -2), ThisApplication.TransientGeometry.CreatePoint2d(2, 2))

    Dim oProfile As Profile
    Set oProfile = oSk.Profiles.AddForSolid

    Dim oBlockDef As ExtrudeDefinition
    Set oBlockDef = oDoc.ComponentDefinition.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oBlockDef.SetDistanceExtent(4, kSymmetricExtentDirection)
    Dim oBlock As ExtrudeFeature
    Set oBlock = oDoc.ComponentDefinition.Features.ExtrudeFeatures.Add(oBlockDef)

    Set oSk = oDoc.ComponentDefinition.Sketches.Add(oBlock.EndFaces(1))
    Call oSk.SketchCircles.AddByCenterRadius(ThisApplication.TransientGeometry.CreatePoint2d(12, 12), 2)

    Set oProfile = oSk.Profiles.AddForSolid
    Dim oCylinderDef As ExtrudeDefinition, oCylinder As ExtrudeFeature
    Set oCylinderDef = oDoc.ComponentDefinition.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kNewBodyOperation)
    Call oCylinderDef.SetDistanceExtent(4, kSymmetricExtentDirection)
    Set oCylinder = oDoc.ComponentDefinition.Features.ExtrudeFeatures.Add(oCylinderDef)
End Sub

Private Sub CreateColors(oDoc As PartDocument)
    Dim bCreateNewAppearance As Boolean: bCreateNewAppearance = False

    Dim oCreateColors As Transaction
    Set oCreateColors = ThisApplication.TransactionManager.StartTransaction(oDoc, "Create custom colors")
        On Error Resume Next
        Dim oAsset As Asset, oColor As Color
        Set oAsset = oDoc.Assets.Item("Red")
        If Err Then
            Set oAsset = oDoc.Assets.Add(kAssetTypeAppearance, "Generic", "Red", "Red")
            ' Add Red
            Set oColor = ThisApplication.TransientObjects.CreateColor(255, 0, 0)
            oAsset.Item("generic_diffuse").Value = oColor
            bCreateNewAppearance = True
            Err.Clear
        End If

        Set oAsset = oDoc.Assets.Item("Orange")
        If Err Then
            Set oAsset = oDoc.Assets.Add(kAssetTypeAppearance, "Generic", "Orange", "Orange")
            ' Add Orange
            Set oColor = ThisApplication.TransientObjects.CreateColor(255, 165, 0)
            oAsset.Item("generic_diffuse").Value = oColor

            bCreateNewAppearance = True
            Err.Clear
        End If

        Set oAsset = oDoc.Assets.Item("Yellow")
        If Err Then
            Set oAsset = oDoc.Assets.Add(kAssetTypeAppearance, "Generic", "Yellow", "Yellow")
            ' Add Yellow
            Set oColor = ThisApplication.TransientObjects.CreateColor(255, 255, 0)
            oAsset.Item("generic_diffuse").Value = oColor

            bCreateNewAppearance = True
            Err.Clear
        End If

        Set oAsset = oDoc.Assets.Item("Green")
        If Err Then
            Set oAsset = oDoc.Assets.Add(kAssetTypeAppearance, "Generic", "Green", "Green")
            ' Add Green
            Set oColor = ThisApplication.TransientObjects.CreateColor(0, 255, 0)
            oAsset.Item("generic_diffuse").Value = oColor

            bCreateNewAppearance = True
            Err.Clear
        End If

        Set oAsset = oDoc.Assets.Item("Blue")
        If Err Then
            Set oAsset = oDoc.Assets.Add(kAssetTypeAppearance, "Generic", "Blue", "Blue")
            ' Add Blue
            Set oColor = ThisApplication.TransientObjects.CreateColor(0, 0, 255)
            oAsset.Item("generic_diffuse").Value = oColor

            bCreateNewAppearance = True
            Err.Clear
        End If

        Set oAsset = oDoc.Assets.Item("Indigo")
        If Err Then
            Set oAsset = oDoc.Assets.Add(kAssetTypeAppearance, "Generic", "Indigo", "Indigo")
            ' Add Indigo
            Set oColor = ThisApplication.TransientObjects.CreateColor(75, 0, 130)
            oAsset.Item("generic_diffuse").Value = oColor
            bCreateNewAppearance = True
            Err.Clear
        End If

        Set oAsset = oDoc.Assets.Item("Purple")
        If Err Then
            Set oAsset = oDoc.Assets.Add(kAssetTypeAppearance, "Generic", "Purple", "Purple")
            ' Add Purple
            Set oColor = ThisApplication.TransientObjects.CreateColor(160, 32, 240)
            oAsset.Item("generic_diffuse").Value = oColor

            bCreateNewAppearance = True
            Err.Clear
        End If

        If bCreateNewAppearance Then
            oCreateColors.End
        Else
            oCreateColors.Abort
        End If

End Sub

'*************************************************************
' The declarations and functions below need to be copied into
' a class module whose name is "clsColorChange".  The name
' can be changed but you'll need to change the declaration in
' the calling function "ChangeAppearanceMiniToolbarSample" to use the new name.
Private WithEvents m_MiniToolbar As MiniToolbar
Private WithEvents m_Colors As MiniToolbarComboBox
Private WithEvents m_Filter As MiniToolbarDropdown
Private WithEvents m_Preview As MiniToolbarCheckBox
Private m_PreviewColor As MiniToolbarCheckBox

Private WithEvents oInteractionEvents As InteractionEvents
Private WithEvents m_SelectEvents As SelectEvents
Private m_ChangeColorTransaction As Transaction

Private m_Doc As PartDocument
Private m_DefaultColor As Asset

Private bIsinteractionStarted As Boolean

Private bNeedTransaction As Boolean
Private bStop As Boolean

Public Sub Init(oDoc As PartDocument)
    Set m_Doc = oDoc
    Set m_DefaultColor = m_Doc.ActiveAppearance

    ' Create interaction events
    Set oInteractionEvents = ThisApplication.CommandManager.CreateInteractionEvents
    'oInteractionEvents.InteractionDisabled = False

    Set m_SelectEvents = oInteractionEvents.SelectEvents
    'm_SelectEvents.ClearSelectionFilter
    'm_SelectEvents.SingleSelectEnabled = False
    'm_SelectEvents.Enabled = True

    ' Create mini-tool bar for changing appearance
    Set m_MiniToolbar = oInteractionEvents.CreateMiniToolbar
    Call InitiateMiniToolbar

    bStop = False
    Set m_ChangeColorTransaction = ThisApplication.TransactionManager.StartTransaction(m_Doc, "Change Appearance")

    Do
        ThisApplication.UserInterfaceManager.DoEvents
    Loop Until bStop

End Sub

Private Sub InitiateMiniToolbar()
    m_MiniToolbar.ShowOK = True
    m_MiniToolbar.ShowApply = True
    m_MiniToolbar.ShowCancel = True

    Dim oControls As MiniToolbarControls
    Set oControls = m_MiniToolbar.Controls
    oControls.Item("MTB_Options").Visible = False

    Set m_Filter = m_MiniToolbar.Controls.AddDropdown("Filter", False, True, True, False)
    Call m_Filter.AddItem("Part", "Part", "Filter_Part", False, False)
    Call m_Filter.AddItem("Feature", "Feature", "Filter_Feature", False, False)
    Call m_Filter.AddItem("Face", "Face", "Filter_Face", False, False)

    Set m_Colors = oControls.AddComboBox("Colors", True, True, 50)
    Call m_Colors.AddItem("Default", "Use default color", "Default", False)
    Call m_Colors.AddItem("Red", "Red", "Red", False)
    Call m_Colors.AddItem("Orange", "Orange", "Orange", False)
    Call m_Colors.AddItem("Yellow", "Yellow", "Yellow", False)
    Call m_Colors.AddItem("Green", "Green", "Green", False)
    Call m_Colors.AddItem("Blue", "Blue", "Blue", False)
    Call m_Colors.AddItem("Indigo", "Indigo", "Indigo", False)
    Call m_Colors.AddItem("Purple", "Purple", "Purple", False)

    oControls.AddNewLine

    ' Specify if preview the color when hover a color item
    Set m_PreviewColor = m_MiniToolbar.Controls.AddCheckBox("PreviewColor", "Hover color preview", "Whether preview color when hover on it", True)

    ' Position the mini-tool bar to the top-left.
    Dim oPosition As Point2d
    Set oPosition = ThisApplication.TransientGeometry.CreatePoint2d(0, 0)

    m_MiniToolbar.Visible = True
    m_MiniToolbar.Position = oPosition
End Sub

Private Sub m_Colors_OnItemHoverStart(ByVal ListItem As MiniToolbarListItem)
    ' Preview the color when hover on it.
    If m_PreviewColor.Checked Then
        Call ChangeColor(ListItem.Text)
    End If
End Sub

Private Sub m_Colors_OnSelect(ByVal ListItem As MiniToolbarListItem)
    ' Check if the selected color is already used for the part/objects
    If m_Filter.SelectedItem.Text = "Part" Then
        If m_Doc.ActiveAppearance.Name = ListItem.Text Then
            bNeedTransaction = False
        Else
            bNeedTransaction = True
        End If
    Else
        bNeedTransaction = True
    End If

    Call ChangeColor(ListItem.Text)

End Sub
' Change filter for assigning color
Private Sub m_Filter_OnSelect(ByVal ListItem As MiniToolbarListItem)
    If ThisApplication.TransactionManager.CurrentTransaction.DisplayName = "Change Appearance" Then
        ThisApplication.TransactionManager.CurrentTransaction.Abort
    End If

    Set m_ChangeColorTransaction = ThisApplication.TransactionManager.StartTransaction(m_Doc, "Change Appearance")

    Select Case ListItem.Text
        Case "Part"
            m_Doc.SelectSet.Clear
            m_SelectEvents.ResetSelections
            m_SelectEvents.ClearSelectionFilter
            m_SelectEvents.AddSelectionFilter kPartDefaultFilter
            oInteractionEvents.SetCursor kCursorTypeDefault
        Case "Feature"
            m_Doc.SelectSet.Clear

            m_SelectEvents.ResetSelections
            m_SelectEvents.ClearSelectionFilter
            m_SelectEvents.AddSelectionFilter kPartFeatureFilter

            If Not bIsinteractionStarted Then
                oInteractionEvents.Start
                bIsinteractionStarted = True
            End If
        Case "Face"
            m_Doc.SelectSet.Clear
            m_SelectEvents.ResetSelections
            m_SelectEvents.ClearSelectionFilter
            m_SelectEvents.AddSelectionFilter kPartFaceFilter
            If Not bIsinteractionStarted Then
                oInteractionEvents.Start
                bIsinteractionStarted = True
            End If

    End Select
    m_Doc.Views(1).Update
    Call ChangeColor(ListItem.Text)

End Sub

Private Sub m_MiniToolbar_OnApply()

    If (m_Filter.SelectedItem.Text = "Feature" Or m_Filter.SelectedItem.Text = "Face") And (m_SelectEvents.SelectedEntities.Count = 0) Then
        m_ChangeColorTransaction.Abort
        m_Doc.Views(1).Update
        Set m_ChangeColorTransaction = ThisApplication.TransactionManager.StartTransaction(m_Doc, "Change Appearance")
        Exit Sub
    Else
        If bNeedTransaction Then ' Change color style
            Call ChangeColor(m_Colors.SelectedItem.Text)
            m_ChangeColorTransaction.End
        Else ' If no change to the color style
            m_ChangeColorTransaction.Abort
        End If

        ' Clear current selection for Feature and Face filter.
        If (m_Filter.SelectedItem.Text = "Feature" Or m_Filter.SelectedItem.Text = "Face") Then
            m_Doc.SelectSet.Clear
            m_SelectEvents.ResetSelections
        End If
    End If

    Set m_ChangeColorTransaction = ThisApplication.TransactionManager.StartTransaction(m_Doc, "Change Appearance")
End Sub

Private Sub m_MiniToolbar_OnCancel()
    bStop = True
    If ThisApplication.TransactionManager.CurrentTransaction Is m_ChangeColorTransaction Then
        m_ChangeColorTransaction.Abort
    End If
    m_SelectEvents.AddSelectionFilter kPartDefaultFilter
    If bIsinteractionStarted Then oInteractionEvents.Stop
    m_Doc.Views(1).Update

End Sub

Private Sub m_MiniToolbar_OnOK()
    bStop = True
    If bNeedTransaction Then ' Change color
        Call ChangeColor(m_Colors.SelectedItem.Text)
        m_ChangeColorTransaction.End
    Else ' If no change to the color style
        m_ChangeColorTransaction.Abort
    End If
End Sub

Private Sub oInteractionEvents_OnTerminate()

    If ThisApplication.TransactionManager.CurrentTransaction Is m_ChangeColorTransaction Then
        m_ChangeColorTransaction.Abort
    End If
    If bIsinteractionStarted Then
        oInteractionEvents.Stop
    End If
    m_Doc.Views(1).Update
End Sub

Private Sub ChangeColor(sColor As String)
        Debug.Print "Passed in:" & sColor
        If m_Filter.SelectedItem.Text = "Part" Then
            Select Case sColor
                Case "Default"
                    m_Doc.ActiveAppearance = m_DefaultColor
                Case "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple"
                    m_Doc.ActiveAppearance = m_Doc.AppearanceAssets.Item(sColor)
            End Select
        ElseIf m_Filter.SelectedItem.Text = "Feature" Then
            If m_SelectEvents.SelectedEntities.Count Then
                Dim oFeature As PartFeature, oSelectedObj As Object

                For Each oSelectedObj In m_SelectEvents.SelectedEntities
                    If InStr(1, TypeName(oSelectedObj), "Feature") Then
                        Set oFeature = oSelectedObj

                        Select Case sColor 'm_Colors.SelectedItem.Text
                            Case "Default"
                                oFeature.Appearance = m_DefaultColor
                            Case "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple"
                                oFeature.Appearance = m_Doc.AppearanceAssets.Item(sColor)
                        End Select
                    End If
                Next
            End If
        ElseIf m_Filter.SelectedItem.Text = "Face" Then
            If m_SelectEvents.SelectedEntities.Count Then
                Dim oFace As Face

                For Each oSelectedObj In m_SelectEvents.SelectedEntities
                    If InStr(1, TypeName(oSelectedObj), "Face") Then
                        Set oFace = oSelectedObj

                        Select Case sColor
                            Case "Default"
                                oFace.Appearance = m_DefaultColor
                            Case "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple"
                                oFace.Appearance = m_Doc.AppearanceAssets.Item(sColor)
                        End Select
                    End If
                Next
            End If
        End If
End Sub
```
