# Sheet.TitleBlock Property

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Property that returns the TitleBlock object associated with the sheet. This property will return Nothing in the case where the sheet doesn't have a title block.

## Syntax

Sheet.**TitleBlock**() As [TitleBlock](../TitleBlock/TitleBlock.md)

## Property Value

This is a read only property whose value is a [TitleBlock](../TitleBlock/TitleBlock.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 5.3
