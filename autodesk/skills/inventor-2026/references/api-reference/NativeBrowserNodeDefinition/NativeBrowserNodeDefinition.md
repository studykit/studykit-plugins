# NativeBrowserNodeDefinition Object

## Description

The BrowserNodeDefinition object contains the definition of a node in the browser.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AdditionalDisplayState](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_AdditionalDisplayState.md) | Gets and sets the additional display state of browsernodes that use this definition. |
| [AdditionalStateIconToolTipText](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_AdditionalStateIconToolTipText.md) | Gets and sets additional state icon tool tip text on a existing definition object. |
| [Application](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_BuiltIn.md) | Specifies if the node is a standard Autodesk Inventor node or not. |
| [DisplayState](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_DisplayState.md) | Gets and sets the display state of browsernodes that use this definition. |
| [ExpandedIcon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_ExpandedIcon.md) | Gets the expanded icon on a existing definition object. |
| [Icon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_Icon.md) | Gets the icon on a existing definition object. |
| [Label](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_Label.md) | Gets the label of the BrowserNode. |
| [NativeObject](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideExpandedIcon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_OverrideExpandedIcon.md) | Gets and sets expanded icon override on a existing definition object. |
| [OverrideIcon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_OverrideIcon.md) | Gets and sets icon override on a existing definition object. |
| [OverrideStateIcon](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_OverrideStateIcon.md) | Gets and sets state icon override on a existing definition object. |
| [Parent](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [StateIconToolTipText](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_StateIconToolTipText.md) | Gets and sets state icon tool tip text on a existing definition object. |
| [ToolTipText](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_ToolTipText.md) | Gets and sets tool tip text on a existing definition object. |
| [Type](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BrowserPanes.GetNativeBrowserNodeDefinition](../BrowserPanes/BrowserPanes_GetNativeBrowserNodeDefinition.md), [BrowserPanes.GetNativeBrowserNodeDefinitionWithOptions](../BrowserPanes/BrowserPanes_GetNativeBrowserNodeDefinitionWithOptions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |

## Version

Introduced in version 8
