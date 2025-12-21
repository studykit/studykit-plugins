# FlatPattern.GetEdgesOfType Method

Parent Object: [FlatPattern](../FlatPattern/FlatPattern.md)

## Description

Method that returns edges of the specified type from the flat pattern body.

## Syntax

FlatPattern.**GetEdgesOfType**( ***EdgeType*** As [FlatPatternEdgeTypeEnum](../FlatPatternEdgeTypeEnum.md), [***TopFaceEdges***] As Boolean ) As [Edges](../Edges/Edges.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EdgeType | [FlatPatternEdgeTypeEnum](../FlatPatternEdgeTypeEnum.md) | Input FlatPatternEdgeTypeEnum that specifies the type of edges to return from the flat pattern body. |
| TopFaceEdges | Boolean | Optional input Boolean that specifies whether to return the edges from the top face or the bottom face of the unfolded model. If not specified, edges from the top face are returned. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Finding Bend Extent (Tangent) Edges](../../sample-programs/FlatPattern_GetEdgesOfType_Sample.md) | This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |