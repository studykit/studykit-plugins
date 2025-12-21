# TransactionManager.StartTransaction Method

Parent Object: [TransactionManager](../TransactionManager/TransactionManager.md)

## Description

Starts a new transaction.

## Syntax

TransactionManager.**StartTransaction**( ***Document*** As [Document](../Document/Document.md), ***DisplayName*** As String ) As [Transaction](../Transaction/Transaction.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Document | [Document](../Document/Document.md) | Input object in which to start the transaction. |
| DisplayName | String | Input String that specifies the human-readable name for the transaction. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |

## Version

Introduced in version 4
