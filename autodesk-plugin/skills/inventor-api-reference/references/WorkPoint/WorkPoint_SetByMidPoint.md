# WorkPoint.SetByMidPoint Method

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Method that redefines the work point to be at the midpoint of the input edge.

## Remarks

This method is not valid when the work point exists in an Assembly component definition.

## Syntax

WorkPoint.**SetByMidPoint**( ***Edge*** As [Edge](../Edge/Edge.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edge | [Edge](../Edge/Edge.md) | Input Edge object. Any open edge is valid as input. Inputting a closed edge, (i.e. circle), will cause and error to occur. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |