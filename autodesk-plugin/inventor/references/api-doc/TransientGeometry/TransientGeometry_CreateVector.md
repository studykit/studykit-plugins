# TransientGeometry.CreateVector Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Vector object.

## Syntax

TransientGeometry.**CreateVector**( [***XCoord***] As Double, [***YCoord***] As Double, [***ZCoord***] As Double ) As [Vector](../Vector/Vector.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| XCoord | Double | Input Double that specifies the Vector's X-coordinate. |
| YCoord | Double | Input Double that specifies the Vector's Y-coordinate.   This is an optional argument whose default value is 0.0. |
| ZCoord | Double | Input Double that specifies the Vector's Z-coordinate.   This is an optional argument whose default value is 0.0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Assembly Add Occurrence](../../sample-programs/AddOccurrence_Sample.md) | This sample demonstrates placing an assembly occurrence. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Is cylindrical face interior or exterior?](../../sample-programs/Line_IsColinearTo_Sample.md) | This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face. |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Assembly Move Occurrence](../../sample-programs/TransformOccurrence_Sample.md) | This sample demonstrates moving a component occurrence. This sample performs a translate, but a rotate can also be performed since the transform is defined using a matrix. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |