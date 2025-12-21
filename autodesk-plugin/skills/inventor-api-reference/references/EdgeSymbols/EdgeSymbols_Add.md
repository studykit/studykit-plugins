# EdgeSymbols.Add Method

Parent Object: [EdgeSymbols](../EdgeSymbols/EdgeSymbols.md)

## Description

Method that creates a new edge symbol. The newly created EdgeSymbol object is returned.

## Syntax

EdgeSymbols.**Add**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***EdgeSymbolDefinition*** As [EdgeSymbolDefinition](../EdgeSymbolDefinition/EdgeSymbolDefinition.md) ) As [EdgeSymbol](../EdgeSymbol/EdgeSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object containing a series of Point2d objects representing the leader originating at the edge symbol. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating a geometry to attach the leader to. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. The ObjectCollection must contain at least one item, else the method will fail. |
| EdgeSymbolDefinition | [EdgeSymbolDefinition](../EdgeSymbolDefinition/EdgeSymbolDefinition.md) | Input EdgeSymbolDefinition object that defines the edge symbol to create. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [EdgeSymbol Creation Sample](../../sample-programs/EdgeSymbolCreation_Sample.md) | This sample is to demonstrate how to create a EdgeSymbol in drawing document. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |