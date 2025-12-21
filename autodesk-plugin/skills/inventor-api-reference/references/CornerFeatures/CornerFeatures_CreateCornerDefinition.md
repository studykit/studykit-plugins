# CornerFeatures.CreateCornerDefinition Method

Parent Object: [CornerFeatures](../CornerFeatures/CornerFeatures.md)

## Description

Method that creates a new sheet metal corner feature.

## Syntax

CornerFeatures.**CreateCornerDefinition**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***RippedCorner*** As Boolean ) As [CornerDefinition](../CornerDefinition/CornerDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgeCollection object that contains the two edges that define the two sheet metal faces to create the corner between or the edges to create a ripped corner on. |
| RippedCorner | Boolean | Input Boolean that specifies if the corner is a ripped corner or a seam corner. A value of True indicates a ripped corner. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |