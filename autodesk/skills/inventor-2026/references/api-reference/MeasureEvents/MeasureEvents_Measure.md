# MeasureEvents.Measure Method

Parent Object: [MeasureEvents](../MeasureEvents/MeasureEvents.md)

## Description

Method that invokes the 'Measure' command and prompts the user to select entities for measure. The OnMeasure event fires as a result of the user action.

## Syntax

MeasureEvents.**Measure**( ***MeasureType*** As [MeasureTypeEnum](../MeasureTypeEnum.md), [***Options***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MeasureType | [MeasureTypeEnum](../MeasureTypeEnum.md) | Input MeasureTypeEnum that indicates the type of measure action to invoke. Valid values are kDistanceMeasure and kAngleMeasure. |
| Options | Variant | Optional input NameValueMap specifying additional options for measure. Currently ignored. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |

## Version

Introduced in version 2009
