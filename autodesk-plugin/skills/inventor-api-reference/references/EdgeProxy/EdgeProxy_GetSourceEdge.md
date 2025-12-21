# EdgeProxy.GetSourceEdge Method

Parent Object: [EdgeProxy](../EdgeProxy/EdgeProxy.md)

## Description

Method that gets the source edge that has been overridden by this edge. The method returns Nothing if this edge is not an override. An error is returned if this method is called on an edge in a part.

## Syntax

EdgeProxy.**GetSourceEdge**( [***GetLeafSource***] As Boolean ) As [Edge](../Edge/Edge.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GetLeafSource | Boolean | Optional input Boolean that specifies whether to get the 'leaf' source edge in the case where there are multiple levels of override. If specified to be False, the method returns the next level override edge. If not specified, the argument defaults to True indicating that the leaf source will be returned. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |