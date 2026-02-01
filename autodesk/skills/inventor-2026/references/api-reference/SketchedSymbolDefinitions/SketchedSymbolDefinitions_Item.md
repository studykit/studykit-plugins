# SketchedSymbolDefinitions.Item Property

Parent Object: [SketchedSymbolDefinitions](../SketchedSymbolDefinitions/SketchedSymbolDefinitions.md)

## Description

Method that returns the specified SketchedSymbolDefinition object from the collection.

## Syntax

SketchedSymbolDefinitions.**Item**( ***Index*** As Variant ) As [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md)

## Property Value

This is a read only property whose value is a [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the SketchedSymbolDefinition to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the sketched symbol definition's name. If an out of range index or a name of a non-existent sketched symbol definition is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |

## Version

Introduced in version 5.3
