# SurfaceTextureSymbols.AddByDefinition Method

Parent Object: [SurfaceTextureSymbols](../SurfaceTextureSymbols/SurfaceTextureSymbols.md)

## Description

Method that creates a surface texture symbol.

## Syntax

SurfaceTextureSymbols.**AddByDefinition**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***SurfaceTextureSymbolDefinition*** As [SurfaceTextureSymbolDefinition](../SurfaceTextureSymbolDefinition/SurfaceTextureSymbolDefinition.md) ) As [SurfaceTextureSymbol](../SurfaceTextureSymbol/SurfaceTextureSymbol.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing a series of Point2d objects representing the leader originating at the symbol. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating a geometry to attach the leader to. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. The ObjectCollection must contain at least one item, else the method will fail. |
| SurfaceTextureSymbolDefinition | [SurfaceTextureSymbolDefinition](../SurfaceTextureSymbolDefinition/SurfaceTextureSymbolDefinition.md) | Input SurfaceTextureSymbolDefinition object that defines the input for the SurfaceTextureSymbol. A SurfaceTextureSymbolDefinition object can be created using the SurfaceTextureSymbols.CreateDefinition method. It can also be obtained from an existing SurfaceTextureSymbol object. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |