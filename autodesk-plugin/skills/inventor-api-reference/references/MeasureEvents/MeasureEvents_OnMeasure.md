# MeasureEvents.OnMeasure Event

Parent Object: [MeasureEvents](../MeasureEvents/MeasureEvents.md)

## Description

Event that fires when the user selects entities for measure..

## Syntax

MeasureEvents.**OnMeasure**( ***MeasureType*** As [MeasureTypeEnum](../MeasureTypeEnum.md), ***MeasuredValue*** As Double, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MeasureType | [MeasureTypeEnum](../MeasureTypeEnum.md) | Input MeasureTypeEnum that indicates the type of measure action. Possible values are kDistanceMeasure and kAngleMeasure. |
| MeasuredValue | Double | Input measured value returned in centimeters for kDistanceMeasure and in radians for kAngleMeasure. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Currently empty. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |

## Version

Introduced in version 2009
