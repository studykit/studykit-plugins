# TransientGeometry.CreateLineSegment2d Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new LineSegment2d object. The object created is a transient mathematical object and is not displayed graphically

## Syntax

TransientGeometry.**CreateLineSegment2d**( ***StartPoint*** As [Point2d](../Point2d/Point2d.md), ***EndPoint*** As [Point2d](../Point2d/Point2d.md) ) As [LineSegment2d](../LineSegment2d/LineSegment2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the start point of the line. |
| EndPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the end point of the line. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |

## Version

Introduced in version 11
