# WorkAxes.AddByAnalyticEdge Method

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Method that creates a new work axis based on the input analytic edge. This method is not currently supported when creating a work axis within an assembly.

## Syntax

WorkAxes.**AddByAnalyticEdge**( ***Edge*** As [Edge](../Edge/Edge.md), [***Construction***] As Boolean ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edge | [Edge](../Edge/Edge.md) | Input Edge object that can be a circle, arc, or an ellipse. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work axis as a construction axis or not. The default is False, which indicates to create a standard work axis. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |