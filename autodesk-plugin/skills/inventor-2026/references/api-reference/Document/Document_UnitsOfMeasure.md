# Document.UnitsOfMeasure Property

Parent Object: [Document](../Document/Document.md)

## Description

Property that returns the UnitsOfMeasure object.

## Syntax

Document.**UnitsOfMeasure**() As [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Property Value

This is a read only property whose value is a [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |

## Version

Introduced in version 4
