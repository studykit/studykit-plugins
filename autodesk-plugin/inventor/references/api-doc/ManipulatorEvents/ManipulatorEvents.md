# ManipulatorEvents Object

## Description

ManipulatorEvents Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ApplyDrag](../ManipulatorEvents/ManipulatorEvents_ApplyDrag.md) | Drives manipulator to move as if it is dragged by end user. |
| [SetAppearance](../ManipulatorEvents/ManipulatorEvents_SetAppearance.md) | Sets the visible and enabled manipulator elements. |
| [SuggestedMiniToolbarPosition](../ManipulatorEvents/ManipulatorEvents_SuggestedMiniToolbarPosition.md) | Calculates a suggested position to place mini toolbar with input mini toolbar size. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ManipulatorEvents/ManipulatorEvents_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Enabled](../ManipulatorEvents/ManipulatorEvents_Enabled.md) | Gets and sets whether the manipulator events is enabled or not. |
| [Parent](../ManipulatorEvents/ManipulatorEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SelectedElement](../ManipulatorEvents/ManipulatorEvents_SelectedElement.md) | Read-write property that gets and sets the selected manipulator element. If the kAllManipulatorElements is set that no element will be selected. |
| [Transform](../ManipulatorEvents/ManipulatorEvents_Transform.md) | Gets and sets the current position and orientation of the manipulator in model space. |
| [Type](../ManipulatorEvents/ManipulatorEvents_Type.md) | Gets the constant that indicates the type of this object. |
| [Visible](../ManipulatorEvents/ManipulatorEvents_Visible.md) | Read-write property that gets and sets whether the enabled manipulator is visible or not. Set this property does not work if the Enabled equals to False. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnDrag](../ManipulatorEvents/ManipulatorEvents_OnDrag.md) | Fires fires when the manipulator moves as a result of a drag, reposition or user entering values for translation, rotation and scaling. |
| [OnEndDrag](../ManipulatorEvents/ManipulatorEvents_OnEndDrag.md) | Fires when the user ends an intermediate drag of the manipulator. |
| [OnManipulatorElementSelectionChange](../ManipulatorEvents/ManipulatorEvents_OnManipulatorElementSelectionChange.md) | Fires when a manipulator element is selected. |
| [OnStartDrag](../ManipulatorEvents/ManipulatorEvents_OnStartDrag.md) | Fires when a manipulator element is selected. |

## Accessed From

[InteractionEvents.ManipulatorEvents](../InteractionEvents/InteractionEvents_ManipulatorEvents.md)

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |