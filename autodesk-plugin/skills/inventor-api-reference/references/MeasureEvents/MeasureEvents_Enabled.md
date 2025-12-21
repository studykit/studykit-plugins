# MeasureEvents.Enabled Property

Parent Object: [MeasureEvents](../MeasureEvents/MeasureEvents.md)

## Description

Gets/Sets the Boolean flag indicating whether MeasureEvents is enabled. Defaults to False. This property should be set to True when the relevant field in the command's dialog gets focus and should be set to False when it loses focus.

## Syntax

MeasureEvents.**Enabled**() As Boolean

## Property Value

This is a read/write property whose value is a Boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |