# Document.FullFileName Property

Parent Object: [Document](../Document/Document.md)

## Description

Gets/Sets the fully qualified file-name of this Document.

## Syntax

Document.**FullFileName**() As String

## Property Value

This is a read/write property whose value is a String.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |

## Version

Introduced in version 4
