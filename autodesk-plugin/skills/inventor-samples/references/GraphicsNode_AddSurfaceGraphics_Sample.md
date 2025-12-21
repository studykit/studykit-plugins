# Client graphics from SAT file body

## Description

The following sample demonstrates how to display client graphics based on bodies read in from a SAT file.

## Code Samples

* [VBA](#VBA)

Make sure you have "C:\temp\block.sat" or change the path in the code below.

|  |
| --- |
| Copy Code |

```
Public Sub ClientGraphicsFromSATFileBody()
    ' Set a reference to the TransientBRep object
    Dim oTransientBRep As TransientBRep
    Set oTransientBRep = ThisApplication.TransientBRep

    ' Get the first body from the specified sat file
    Dim oBody As SurfaceBody
    Set oBody = oTransientBRep.ReadFromFile("C:\temp\block.sat").Item(1)

    ' Create a new Part document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' Set a reference to the compdef.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create the ClientGraphics object.
    Dim oClientGraphics As ClientGraphics
    Set oClientGraphics = oCompDef.ClientGraphicsCollection.Add("Sample3DGraphicsID")

    ' Create a new graphics node within the client graphics objects.
    Dim oSurfacesNode As GraphicsNode
    Set oSurfacesNode = oClientGraphics.AddNode(1)

    ' Create client graphics based on the transient body
    Dim oSurfaceGraphics As SurfaceGraphics
    Set oSurfaceGraphics = oSurfacesNode.AddSurfaceGraphics(oBody)

    ' Update the view to see the resulting curves.
    ThisApplication.ActiveView.Update
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |