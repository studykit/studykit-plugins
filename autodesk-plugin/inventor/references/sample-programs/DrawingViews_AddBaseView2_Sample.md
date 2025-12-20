# Create flat pattern drawing view

## Description

This sample demonstrates the creation of a flat pattern base view in a drawing.

## Code Samples

* [VBA](#VBA)

Open a drawing document and run the sample. The sheet metal part must have a flat pattern within it or a folded view will still be created.

|  |
| --- |
| Copy Code |

```
Public Sub AddFlatPatternDrawingView()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Create a new NameValueMap object
    Dim oBaseViewOptions As NameValueMap
    Set oBaseViewOptions = ThisApplication.TransientObjects.CreateNameValueMap

    ' Set the options to use when creating the base view.
    Call oBaseViewOptions.Add("SheetMetalFoldedModel", False)

    ' Open the sheet metal document invisibly
    Dim oModel As Document
    Set oModel = ThisApplication.Documents.Open("C:\temp\SheetMetal.ipt", False)

    ' Create the placement point object.
    Dim oPoint As Point2d
    Set oPoint = ThisApplication.TransientGeometry.CreatePoint2d(25, 25)

    ' Create a base view.
    Dim oBaseView As DrawingView
    Set oBaseView = oSheet.DrawingViews.AddBaseView(oModel, oPoint, 1, _
    kDefaultViewOrientation, kHiddenLineRemovedDrawingViewStyle, _
    , , oBaseViewOptions)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |