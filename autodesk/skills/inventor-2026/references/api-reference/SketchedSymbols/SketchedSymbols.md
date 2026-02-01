# SketchedSymbols Object

## Description

The SketchedSymbols collection object provides access to the objects on a specific sheet. It also provides the ability to place sketched symbols onto a sheet. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchedSymbols/SketchedSymbols_Add.md) | Method that places a sketched symbol onto the sheet. |
| [AddWithLeader](../SketchedSymbols/SketchedSymbols_AddWithLeader.md) | Method that places a sketched symbol with a leader. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchedSymbols/SketchedSymbols_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchedSymbols/SketchedSymbols_Count.md) | Property that returns the number of items in the collection. |
| [Item](../SketchedSymbols/SketchedSymbols_Item.md) | Method that returns the specified SketchedSymbol object from the collection. |
| [Type](../SketchedSymbols/SketchedSymbols_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.SketchedSymbols](../Sheet/Sheet_SketchedSymbols.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |

## Version

Introduced in version 5.3
