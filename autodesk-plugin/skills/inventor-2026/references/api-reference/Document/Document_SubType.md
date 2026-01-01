# Document.SubType Property

Parent Object: [Document](../Document/Document.md)

## Description

Gets/Sets the sub-Type (a published GUID. See DocCLSIDs.h) of this Document. Setting a new sub-Type will invoke a validation sequence and may fail if the operation is invalid.

## Syntax

Document.**SubType**() As String

## Property Value

This is a read/write property whose value is a String.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Style Display](../../sample-programs/SheetMetalStyle_Sample.md) | This sample illustrates getting information about sheet metal styles. |
| [Sheet Metal Style Creation](../../sample-programs/SheetMetalStyles_Sample.md) | This sample illustrates creating a new sheet metal style. It uses a bend table and assumes the sample bend table delivered with Inventor is available. You can edit the path below to reference any existing bend table. To use the sample make sure a bend table is available at the specified path, open a sheet metal document, and run the sample. |

## Version

Introduced in version 4
