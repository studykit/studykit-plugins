# Navigation between browser and data

## Description

This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub DataModelToBrowser()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new workplane parallel to the XY plane.
    Dim oWorkPlane As WorkPlane
    Set oWorkPlane = oCompDef.WorkPlanes.AddByPlaneAndOffset(oCompDef.WorkPlanes.Item(3), 1)

    ' Get the browser node definition associated with the work plane.
    Dim oNativeBrowserNodeDef As NativeBrowserNodeDefinition
    Set oNativeBrowserNodeDef = oPartDoc.BrowserPanes.GetNativeBrowserNodeDefinition(oWorkPlane)

    ' Get the top browser node of the model pane.
    Dim oTopBrowserNode As BrowserNode
    Set oTopBrowserNode = oPartDoc.BrowserPanes.ActivePane.TopNode

    ' Get the work plane browser node.
    ' This assumes that only one node references the browser node definition.
    ' An example of multiple nodes referencing a single definition is a shared
    ' sketch. The browser may have multiple nodes that represent the same shared
    ' sketch, but all of them reference the same definition.
    Dim oWorkPlaneNode As BrowserNode
    Set oWorkPlaneNode = oTopBrowserNode.AllReferencedNodes(oNativeBrowserNodeDef).Item(1)

    ' Get the browser node definition from the browser node.
    Set oNativeBrowserNodeDef = Nothing
    Set oNativeBrowserNodeDef = oWorkPlaneNode.BrowserNodeDefinition

    ' Get the work plane from the browser node definition.
    Set oWorkPlane = Nothing
    Set oWorkPlane = oNativeBrowserNodeDef.NativeObject

    ' Select the work plane to make sure we have the right object.
    oPartDoc.SelectSet.Select oWorkPlane
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |