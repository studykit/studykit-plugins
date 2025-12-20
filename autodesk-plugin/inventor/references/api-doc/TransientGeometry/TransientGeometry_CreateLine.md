# TransientGeometry.CreateLine Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Line object. A Line object is infinite. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateLine**( ***RootPoint*** As [Point](../Point/Point.md), ***Direction*** As [Vector](../Vector/Vector.md) ) As [Line](../Line/Line.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RootPoint | [Point](../Point/Point.md) | Input Point object that specifies the root point of the line. |
| Direction | [Vector](../Vector/Vector.md) | Input Vector object that specifies the direction of the line. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Is cylindrical face interior or exterior?](../../sample-programs/Line_IsColinearTo_Sample.md) | This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |