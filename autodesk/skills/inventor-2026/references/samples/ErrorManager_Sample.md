# Using Inventor's error dialog

## Description

Demonstrates using Inventor's error dialog.

## Code Samples

* [VBA](#VBA)

```
Public Sub ErrorDialog()
    ' Create a new part document
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(4, 3))

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a base extrusion 1cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kNewBodyOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kNegativeExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    Dim oErrorMgr As ErrorManager
    Set oErrorMgr = ThisApplication.ErrorManager

    Dim oMessageSection As MessageSection
    Set oMessageSection = oErrorMgr.StartMessageSection

    On Error Resume Next

    Dim oTransaction As Transaction
    Set oTransaction = ThisApplication.TransactionManager.StartTransaction(oPartDoc, "Edit Feature")

    ' Delete all sketch lines making the sketch profile invalid.
    Dim oSketchLine As SketchLine
    For Each oSketchLine In oRectangleLines
        oSketchLine.Delete
    Next

    oPartDoc.Update

    If oMessageSection.HasErrors Or oMessageSection.HasWarnings Then
        ' End section by adopting all messages in section
        Call oMessageSection.AdoptMessages("Feature edit failed", True)

        ' Display the messages
        Dim kButtonType As ButtonTypeEnum
        kButtonType = oErrorMgr.Show("Sample of Feature Edit Error", True, False)

        If kButtonType = kAcceptButtonType Then
            ' Go through with the invalid edit if user accepts
            oTransaction.End
        Else
            oTransaction.Abort
        End If
    Else
        ' End section by clearing all messages in section
        oMessageSection.ClearMessages
        oTransaction.End
    End If
End Sub
```
