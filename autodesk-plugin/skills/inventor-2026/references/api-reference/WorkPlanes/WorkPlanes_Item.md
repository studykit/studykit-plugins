# WorkPlanes.Item Property

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Returns the specified WorkPlane object from the collection. This is the default property of the WorkPlanes collection object.

## Syntax

WorkPlanes.**Item**( ***Index*** As Variant ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Property Value

This is a read only property whose value is a [WorkPlane](../WorkPlane/WorkPlane.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be a numeric value indicating the index of the item in the collection or it can be a string indicating the WorkPlane name. If an out of range index or a name of a non-existent WorkPlane is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Extrude sketch text](../../sample-programs/ExtrudeFeatures_AddByDistanceExtent_Sample.md) | This sample demonstrates the creation of an extrude feature from sketch text. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 4
