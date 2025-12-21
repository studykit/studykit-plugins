# MeasureEvents Object

## Description

The MeasureEvents object provides the ability to invoke the measure and show dimension commands during InteractionEvents.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ListParameters](../MeasureEvents/MeasureEvents_ListParameters.md) | Method that invokes the 'List Parameters' command, prompting the user to select a parameter from a list. |
| [Measure](../MeasureEvents/MeasureEvents_Measure.md) | Method that invokes the 'Measure' command and prompts the user to select entities for measure. The OnMeasure event fires as a result of the user action. |
| [ShowDimensions](../MeasureEvents/MeasureEvents_ShowDimensions.md) | Method that invokes the 'Show Dimensions' command, prompting the user to select a feature to show the dimensions for. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeasureEvents/MeasureEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Enabled](../MeasureEvents/MeasureEvents_Enabled.md) | Gets/Sets the Boolean flag indicating whether MeasureEvents is enabled. Defaults to False. This property should be set to True when the relevant field in the command's dialog gets focus and should be set to False when it loses focus. |
| [Parent](../MeasureEvents/MeasureEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../MeasureEvents/MeasureEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnMeasure](../MeasureEvents/MeasureEvents_OnMeasure.md) | Event that fires when the user selects entities for measure.. |
| [OnSelectParameter](../MeasureEvents/MeasureEvents_OnSelectParameter.md) | Event that fires when the user selects a parameter. The selected object can be a feature dimension, a 2d sketch dimension, a 3d sketch dimension or a parameter from the parameters list box. |

## Accessed From

[InteractionEvents.MeasureEvents](../InteractionEvents/InteractionEvents_MeasureEvents.md)

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