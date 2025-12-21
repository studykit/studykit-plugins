# MiniToolbarValueEditor Object

## Description

The MiniToolbarValueEditor object represents a value edit control within a MiniToolbar.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MiniToolbarValueEditor/MiniToolbarValueEditor_Delete.md) | Method that deletes the control. |
| [SetFocus](../MiniToolbarValueEditor/MiniToolbarValueEditor_SetFocus.md) | Method that sets the focus on this control and highlights the current content of the value editor. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowMeasure](../MiniToolbarValueEditor/MiniToolbarValueEditor_AllowMeasure.md) | Read-write property that gets and sets whether to provide the ‘Measure’ command in the fly-out and right click context menus of the value editor. |
| [AllowShowDimensions](../MiniToolbarValueEditor/MiniToolbarValueEditor_AllowShowDimensions.md) | Read-write property that gets and sets whether to provide the ‘Show Dimensions’ command in the fly-out and right click context menus of the value editor. |
| [AllowToleranceEdit](../MiniToolbarValueEditor/MiniToolbarValueEditor_AllowToleranceEdit.md) | Read-write property that gets and sets whether to provide the ‘Tolerance...’ command in the fly-out and right click context menus of the value editor. |
| [Application](../MiniToolbarValueEditor/MiniToolbarValueEditor_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutoHide](../MiniToolbarValueEditor/MiniToolbarValueEditor_AutoHide.md) | Read-write property that gets and sets whether the control should be automatically hidden when the user moves the cursor away from the MiniToolbar. |
| [CanValueBeEqualToMaximumValue](../MiniToolbarValueEditor/MiniToolbarValueEditor_CanValueBeEqualToMaximumValue.md) | Read-write property that gets and sets whether the maximum value is valid value or not. |
| [CanValueBeEqualToMinimumValue](../MiniToolbarValueEditor/MiniToolbarValueEditor_CanValueBeEqualToMinimumValue.md) | Read-write property that gets and sets whether the minimum value is valid value or not. |
| [ControlType](../MiniToolbarValueEditor/MiniToolbarValueEditor_ControlType.md) | Read-only property that returns the control type. |
| [DefaultUnits](../MiniToolbarValueEditor/MiniToolbarValueEditor_DefaultUnits.md) | Read-write property that gets and sets the default units for the value editor. If the Expression includes string that has no units specified, the units of this property will be used to calculate the value. |
| [DisplayName](../MiniToolbarValueEditor/MiniToolbarValueEditor_DisplayName.md) | Read-write property that gets and sets the display name for the control. |
| [Enabled](../MiniToolbarValueEditor/MiniToolbarValueEditor_Enabled.md) | Read-write property that gets and sets whether the control is enabled. |
| [Expression](../MiniToolbarValueEditor/MiniToolbarValueEditor_Expression.md) | Read-write property that gets and sets the current, unevaluated content of the value editor. |
| [Index](../MiniToolbarValueEditor/MiniToolbarValueEditor_Index.md) | Read-only property that returns the index this control is currently positioned at within the mini toolbar. |
| [InternalName](../MiniToolbarValueEditor/MiniToolbarValueEditor_InternalName.md) | Read-only property that returns a string uniquely identifying this control within the toolbar. |
| [IsExpressionValid](../MiniToolbarValueEditor/MiniToolbarValueEditor_IsExpressionValid.md) | Read-only property that returns whether the current content of the value editor evaluates to a valid value based on the specified units, and that the evaluated value is within the range of values, if specified. The range of values can be specified using *MaximumValue* and *MinimumValue* properties. If the current content is invalid, the text in the control is displayed in red. |
| [LargeIcon](../MiniToolbarValueEditor/MiniToolbarValueEditor_LargeIcon.md) | Read-write property that gets and sets the large icon for the control. |
| [MaximumValue](../MiniToolbarValueEditor/MiniToolbarValueEditor_MaximumValue.md) | Read-write property that gets and sets the maximum valid value for this control in database units. |
| [MinimumValue](../MiniToolbarValueEditor/MiniToolbarValueEditor_MinimumValue.md) | Read-write property that gets and sets the minimum valid value for this control in database units. |
| [ModelValueType](../MiniToolbarValueEditor/MiniToolbarValueEditor_ModelValueType.md) | Read-write property that gets and sets the model value type. |
| [MostRecentValues](../MiniToolbarValueEditor/MiniToolbarValueEditor_MostRecentValues.md) | Read-write property that gets and sets an array of strings representing the most recent values associated with this control. |
| [Parent](../MiniToolbarValueEditor/MiniToolbarValueEditor_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Precision](../MiniToolbarValueEditor/MiniToolbarValueEditor_Precision.md) | Read-write property that gets and sets number of decimal places to be used when displaying the parameter associated with this control. |
| [StandardIcon](../MiniToolbarValueEditor/MiniToolbarValueEditor_StandardIcon.md) | Read-write property that gets and sets the standard (small) icon for the control. |
| [Tolerance](../MiniToolbarValueEditor/MiniToolbarValueEditor_Tolerance.md) | Read-only property that returns a Tolerance object containing tolerance values for the parameter associated with this control. This property is applicable only if the *AllowToleranceEdit* property is set to True. Use this property to set the default values for the tolerance dialog and to query the values set by the user. |
| [ToolTipText](../MiniToolbarValueEditor/MiniToolbarValueEditor_ToolTipText.md) | Read-write property that gets and sets the tooltip text for the control. |
| [Type](../MiniToolbarValueEditor/MiniToolbarValueEditor_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsType](../MiniToolbarValueEditor/MiniToolbarValueEditor_UnitsType.md) | Read-only property that returns the units type assigned to the control during creation. |
| [Value](../MiniToolbarValueEditor/MiniToolbarValueEditor_Value.md) | Read-write property that gets and sets the evaluated value of the current expression in database units. |
| [Visible](../MiniToolbarValueEditor/MiniToolbarValueEditor_Visible.md) | Read-write property that gets and sets whether the control is visible. |
| [Width](../MiniToolbarValueEditor/MiniToolbarValueEditor_Width.md) | Read-write property that gets and sets the width of the control (in pixels). |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnChange](../MiniToolbarValueEditor/MiniToolbarValueEditor_OnChange.md) | Event that is fired when the content of the value editor is changed by the user. |
| [OnEnter](../MiniToolbarValueEditor/MiniToolbarValueEditor_OnEnter.md) | Event that is fired just before the control gets focus. |
| [OnExit](../MiniToolbarValueEditor/MiniToolbarValueEditor_OnExit.md) | Event that is fired just before the control loses focus. |

## Accessed From

[MiniToolbarControls.AddValueEditor](../MiniToolbarControls/MiniToolbarControls_AddValueEditor.md)

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |