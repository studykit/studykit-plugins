# PunchNotes.Add Method

Parent Object: [PunchNotes](../PunchNotes/PunchNotes.md)

## Description

Method that creates a punch note on the sheet based on the \input punch edge.

## Syntax

PunchNotes.**Add**( ***Position*** As [Point2d](../Point2d/Point2d.md), ***PunchEdge*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***DimensionStyle***] As Variant ) As [PunchNote](../PunchNote/PunchNote.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the position of the punch note on the sheet. |
| PunchEdge | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that specifies the punch geomery to create the note for. The GeometryIntent object defines the geometry (typically a curve but can also be a center mark that represents the origin of a punch) and the location on the geometry where the note will point. If the GeometryIntent does not represent a punch edge or punch center, the method returns an error. |
| DimensionStyle | Variant | Optional input Variant that specifies which dimension style to use for the note. The dimension style can be specified by providing the name of an existing style or by supplying a DimensionStyle object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |