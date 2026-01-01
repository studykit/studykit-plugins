# MiniToolbarSlider Object

Derived from: [MiniToolbarControl](../MiniToolbarControl/MiniToolbarControl.md) Object

## Description

The MiniToolbarSlider object represents a slider control within a MiniToolbar.

![](../images/MiniToolbarSlider.png)

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MiniToolbarSlider/MiniToolbarSlider_Delete.md) | Method that deletes the control. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MiniToolbarSlider/MiniToolbarSlider_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutoHide](../MiniToolbarSlider/MiniToolbarSlider_AutoHide.md) | Read-write property that gets and sets whether the control should be automatically hidden when the user moves the cursor away from the MiniToolbar. |
| [ControlType](../MiniToolbarSlider/MiniToolbarSlider_ControlType.md) | Read-only property that returns the control type. |
| [DisplayName](../MiniToolbarSlider/MiniToolbarSlider_DisplayName.md) | Read-write property that gets and sets the display name for the control. |
| [Enabled](../MiniToolbarSlider/MiniToolbarSlider_Enabled.md) | Read-write property that gets and sets whether the control is enabled. |
| [Index](../MiniToolbarSlider/MiniToolbarSlider_Index.md) | Read-only property that returns the index this control is currently positioned at within the mini toolbar. |
| [InternalName](../MiniToolbarSlider/MiniToolbarSlider_InternalName.md) | Read-only property that returns a string uniquely identifying this control within the toolbar. |
| [LargeIcon](../MiniToolbarSlider/MiniToolbarSlider_LargeIcon.md) | Read-write property that gets and sets the large icon for the control. |
| [Maximum](../MiniToolbarSlider/MiniToolbarSlider_Maximum.md) | Read-write property that gets and sets the maximum value of the slider. If the ValueType property is kIntegerType then this value will be rounded to the nearest integer. |
| [Minimum](../MiniToolbarSlider/MiniToolbarSlider_Minimum.md) | Read-write property that gets and sets the minimum value of the slider. If the ValueType property is kIntegerType then this value will be rounded to the nearest integer. |
| [NumberOfTicks](../MiniToolbarSlider/MiniToolbarSlider_NumberOfTicks.md) | Read-write property that gets and sets the number of tick marks displayed. This does not include the start and end marks. |
| [Parent](../MiniToolbarSlider/MiniToolbarSlider_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [StandardIcon](../MiniToolbarSlider/MiniToolbarSlider_StandardIcon.md) | Read-write property that gets and sets the standard (small) icon for the control. |
| [StepsBetweenTicks](../MiniToolbarSlider/MiniToolbarSlider_StepsBetweenTicks.md) | Read-write property that gets and sets the number of steps the slider will move to go from one tick to the next. This controls the resolution and the corresponding values that can be returned by the slider. |
| [ToolTipText](../MiniToolbarSlider/MiniToolbarSlider_ToolTipText.md) | Read-write property that gets and sets the tooltip text for the control. |
| [Type](../MiniToolbarSlider/MiniToolbarSlider_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../MiniToolbarSlider/MiniToolbarSlider_Value.md) | Read-write property that gets and sets the value of the slider. If a value outside the range defined by the Minimum and Maximum properties is specified, it will be set to the close valid value. Use the ValueType property to know if the value returned should. |
| [ValueType](../MiniToolbarSlider/MiniToolbarSlider_ValueType.md) | Read-write property that gets and sets if the slider will handle integer or decimal numbers. Valid values are kDoubleType or kIntegerType. |
| [Visible](../MiniToolbarSlider/MiniToolbarSlider_Visible.md) | Read-write property that gets and sets whether the control is visible. |
| [Width](../MiniToolbarSlider/MiniToolbarSlider_Width.md) | Read-write property that gets and sets the width of the slider in pixels. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnValueChange](../MiniToolbarSlider/MiniToolbarSlider_OnValueChange.md) | Event that is fired when the value of the slider has changed. This event is fired after the user has finished any scrolling and released the left mouse button. Use the Value property to get the current value of the slider. |

## Accessed From

[MiniToolbarControls.AddSlider](../MiniToolbarControls/MiniToolbarControls_AddSlider.md)

## Version

Introduced in version 2013
