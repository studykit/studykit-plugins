# DrawingView.SetIncludeStatus Method

Parent Object: [DrawingView](../DrawingView/DrawingView.md)

## Description

Method that sets the include status of the input object in the drawing view. This method automatically makes the object visible as well. After an object has been included, its visibility can be controlled using the GetVisibility and SetVisibility methods.

## Syntax

DrawingView.**SetIncludeStatus**( ***Object*** As Object, ***Include*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Object | Object | Input object to set the include status of. Valid objects are 2d and 3d sketches, work features, surface features, and proxies for all of these. The object needs to be supplied in the context of the document referenced by the drawing view. For instance, to set the include status of a 3D sketch within a part instanced in an assembly (and the drawing view is of the assembly), the input should be a Sketch3DProxy object created in context of the assembly. An error will occur if no corresponding object exists in the drawing view. |
| Include | Boolean | Input Boolean that specifies whether the input object is included in the drawing view. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |