# Adding Representation views

## Description

This sample demonstrates how to create a base view by specifying various representations.

## Code Samples

* [VBA](#VBA)

Before running this sample, make sure that the file C:\TempReps.iam exists (or change the path in the sample). The file must contain a level of detail representation named MyLODRep, a positional representation named MyPositionalRep and a design view representation named MyDesignViewRep.

|  |
| --- |
| Copy Code |

```
Public Sub AddBaseViewWithRepresentations()
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

  ' Set the representations to use when creating the base view.
  Call oBaseViewOptions.Add("PositionalRepresentation", "MyPositionalRep")
  Call oBaseViewOptions.Add("DesignViewRepresentation", "MyDesignViewRep")
  Call oBaseViewOptions.Add("DesignViewAssociative", True)

  ' Open the model document (corresponding to the "MyLODRep" representation).
  Dim strFullDocumentName As String
  strFullDocumentName = ThisApplication.FileManager.GetFullDocumentName("C:\tempreps.iam", "MyLODRep")

  Dim oModel As Document
  Set oModel = ThisApplication.Documents.Open(strFullDocumentName, False)

  ' Create the placement point object.
  Dim oPoint As Point2d
  Set oPoint = ThisApplication.TransientGeometry.CreatePoint2d(25, 25)

  ' Create a base view.
  Dim oBaseView As DrawingView
  Set oBaseView = oSheet.DrawingViews.AddBaseView(oModel, oPoint, 2, _
  kIsoTopLeftViewOrientation, kHiddenLineRemovedDrawingViewStyle, _
      , , oBaseViewOptions)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |