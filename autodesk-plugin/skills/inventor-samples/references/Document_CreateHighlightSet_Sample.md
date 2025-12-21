# Creating a HighlightSet

## Description

Demonstrates creating a highlight set.

## Code Samples

* [VBA](#VBA)

```
Sub Main()
  ' Check to make sure the active document is a part.
  If ThisApplication.ActiveDocumentType  kPartDocumentObject Then
     MsgBox "A part document must be open."
     End
  End If

  ' Set a reference to the active part document.
  Dim oDoc As PartDocument
  Set oDoc = ThisApplication.ActiveDocument

  ' Arbitrarily get two faces.  (Assumes a model exists that has
  ' at least 3 faces.
  Dim oFace1 As Face
  Dim oFace2 As Face
  Set oFace1 = oDoc.ComponentDefinitions(1).SurfaceBodies(1).Faces(1)
  Set oFace2 = oDoc.ComponentDefinitions(1).SurfaceBodies(1).Faces(3)

  ' Create a highlight set.
  Dim oSet1 As HighlightSet
  Set oSet1 = oDoc.CreateHighlightSet

  ' Add the first face to the highlight set.
   Call oSet1.AddItem(oFace1)

  ' Create another highlight set.
  Dim oSet2 As HighlightSet
  Set oSet2 = oDoc.CreateHighlightSet

  ' Change the color of the highlight set to green.
  oSet2.Color = ThisApplication.TransientObjects.CreateColor(0, 255, 0)

  ' Add the second face to the highlight set.
  Call oSet2.AddItem(oFace2)
End Sub
```
