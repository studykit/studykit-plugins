# SketchBlockDefinition.AddArcSlotByCenterPointArc Method

Parent Object: [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md)

## Description

Method that creates an arc slot. The sketch entities represent the sketch slot are returned.

## Syntax

SketchBlockDefinition.**AddArcSlotByCenterPointArc**( ***CenterPoint*** As Object, ***StartPoint*** As Object, ***SweepAngle*** As Double, ***Width*** As Double ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input Point2d or SketchPoint object that defines the center of the slot’s center-line. |
| StartPoint | Object | Input Point2d or SketchPoint object that defines the start point of the slot’s center-line. |
| SweepAngle | Double | Input Double defines the sweep angle of the slot’s center-line in radians. The sweep angle is in a counter-clockwise direction from the start point. |
| Width | Double | Input Double that specifies the width of the slot in centimeters. |

## Version

Introduced in version 2014
