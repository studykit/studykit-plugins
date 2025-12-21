# MiniToolbarControls.AddSlider Method

Parent Object: [MiniToolbarControls](../MiniToolbarControls/MiniToolbarControls.md)

## Description

Method that creates a new slider control within the MiniToolbar.

## Syntax

MiniToolbarControls.**AddSlider**( ***InternalName*** As String, ***DisplayName*** As String, ***ToolTipText*** As String, ***ValueType*** As [ValueTypeEnum](../ValueTypeEnum.md), ***Maximum*** As Double, ***Minimum*** As Double, ***NumberOfTicks*** As Long, ***StepsBetweenTicks*** As Long, ***Width*** As Long ) As [MiniToolbarSlider](../MiniToolbarSlider/MiniToolbarSlider.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies an internal name for the control. |
| DisplayName | String | Input String that specifies a display name for the control. If this is specified to be a null string, the control does not display any text. |
| ToolTipText | String | Input String that specifies the tooltip text for the control. |
| ValueType | [ValueTypeEnum](../ValueTypeEnum.md) | Input enum that specifies if the slider will handle integer or decimal numbers. Valid values are kDoubleType or kIntegerType. |
| Maximum | Double | Input Double that specifies the maximum value of the slider. If the ValueType argument is kIntegerType then this value will be rounded to the nearest integer. |
| Minimum | Double | Input Double that specifies the minimum value of the slider. If the ValueType argument is kIntegerType then this value will be rounded to the nearest integer. |
| NumberOfTicks | Long | Input Long that sets the number of tick marks displayed. This does not include the start and end marks. |
| StepsBetweenTicks | Long | Input Long that sets the number of steps the slider will move to go from one tick to the next. This controls the resolution and the corresponding values that can be returned by the slider. |
| Width | Long | Input Long that sets the width of the slider in pixels. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adjust the brightness of lighting](../../sample-programs/BrightnessAdjustSample_Sample.md) | This sample demonstrates how to adjust lighting brightness with mini-toolbar slider. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |