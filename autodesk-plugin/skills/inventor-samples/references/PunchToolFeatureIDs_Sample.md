# Report on punch feature ID's

## Description

This program demonstrates accessing punch features and creates a report of the punch ID's used.

## Code Samples

* [VBA](#VBA)

```
Public Sub PunchFeatureReport()

    ' Get the active sheet metal document and component
    ' definition of the active document.
    On Error Resume Next
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument
    If Err Then
        MsgBox "A part must be active."
        Exit Sub
    End If

    Dim oSMDef As SheetMetalComponentDefinition
    Set oSMDef = oPartDoc.ComponentDefinition

    Dim oSMFeatures As SheetMetalFeatures
    Set oSMFeatures = oSMDef.Features

    Dim iUniquePunchCount As Integer
    iUniquePunchCount = 0
    Dim astrPunchIDs() As String
    ReDim astrPunchIDs(1, oSMFeatures.PunchToolFeatures.Count)

    Dim oPunchFeature As PunchToolFeature
    For Each oPunchFeature In oSMFeatures.PunchToolFeatures
        ' Check to see if this punch ID is already in the list.
        Dim bPunchFound As Boolean
        bPunchFound = False
        Dim i As Integer
        For i = 1 To iUniquePunchCount
            If astrPunchIDs(0, i - 1) = oPunchFeature.PunchId Then
                ' Increment the count for this punch ID.
                astrPunchIDs(1, i - 1) = astrPunchIDs(1, i - 1) + 1

                bPunchFound = True
                Exit For
            End If
        Next

        If Not bPunchFound Then
            ' Add this punch to the list.
            iUniquePunchCount = iUniquePunchCount + 1
            astrPunchIDs(0, iUniquePunchCount - 1) = oPunchFeature.PunchId
            astrPunchIDs(1, iUniquePunchCount - 1) = 1
        End If
    Next

    Dim strMessage As String
    strMessage = "Punch Report (Name, Quantity):" & vbCr & vbCr
    For i = 1 To iUniquePunchCount
       strMessage = strMessage & "   " & astrPunchIDs(0, i - 1) & ", " & _
 astrPunchIDs(1, i - 1)
    Next

    MsgBox strMessage
End Sub
```
