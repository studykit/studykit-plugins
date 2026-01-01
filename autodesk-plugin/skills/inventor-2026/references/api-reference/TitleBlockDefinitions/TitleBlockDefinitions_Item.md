# TitleBlockDefinitions.Item Property

Parent Object: [TitleBlockDefinitions](../TitleBlockDefinitions/TitleBlockDefinitions.md)

## Description

Returns the specified TitleBlockDefinition object from the collection.

## Syntax

TitleBlockDefinitions.**Item**( ***Index*** As Variant ) As [TitleBlockDefinition](../TitleBlockDefinition/TitleBlockDefinition.md)

## Property Value

This is a read only property whose value is a [TitleBlockDefinition](../TitleBlockDefinition/TitleBlockDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the TitleBlockDefinition to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the title block definition's name. If an out of range index or a name of a non-existent title block definition is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3
