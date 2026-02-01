# ButtonDefinition Object

## Description

The ButtonDefinition object represents any command whose user interface is a button.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AutoAddToGUI](../ButtonDefinition/ButtonDefinition_AutoAddToGUI.md) | Adds it to AddIn Toolbar. |
| [Delete](../ButtonDefinition/ButtonDefinition_Delete.md) | Method that deletes the UIDefinition Object. |
| [Execute](../ButtonDefinition/ButtonDefinition_Execute.md) | Executes this ControlDefinition object. |
| [Execute2](../ButtonDefinition/ButtonDefinition_Execute2.md) | Executes the ControlDefinition synchronously or asynchronously. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ButtonDefinition/ButtonDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../ButtonDefinition/ButtonDefinition_BuiltIn.md) | Gets the BuiltIn status for a UIDefinition. |
| [Classification](../ButtonDefinition/ButtonDefinition_Classification.md) | Gets the classification. |
| [ClientId](../ButtonDefinition/ButtonDefinition_ClientId.md) | Gets ClientID. |
| [CommandNotificationType](../ButtonDefinition/ButtonDefinition_CommandNotificationType.md) | Read-write property that gets and sets how to send the command notifications. This defaults to kBothNotifications when the ButtonDefinition is created. This property fails for built-in definitions. |
| [DefaultShortcut](../ButtonDefinition/ButtonDefinition_DefaultShortcut.md) | Gets/Sets the default (internal) shortcut assigned to the command. Setting this property fails for built-in ControlDefinitions. |
| [DefaultShortcutType](../ButtonDefinition/ButtonDefinition_DefaultShortcutType.md) | Gets the type of default shortcut assigned to this command. Possible return values are kNoShortcut (no shortcut has been assigned), kAcceleratorShortcut (a shortcut that directly launches the command), or kAliasShortcut (a command alias). |
| [DefinitionType](../ButtonDefinition/ButtonDefinition_DefinitionType.md) | Gets the ControlDefinitionType. |
| [DescriptionText](../ButtonDefinition/ButtonDefinition_DescriptionText.md) | Gets/Sets Description Text. |
| [DisplayName](../ButtonDefinition/ButtonDefinition_DisplayName.md) | Gets the Display Name. |
| [Enabled](../ButtonDefinition/ButtonDefinition_Enabled.md) | Enables/Disables the UIDefinition object. |
| [InternalName](../ButtonDefinition/ButtonDefinition_InternalName.md) | Gets the Internal Name. |
| [IntroducedInVersion](../ButtonDefinition/ButtonDefinition_IntroducedInVersion.md) | Read-write property that gets and sets the introduced in version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in. |
| [IsShortcutOverridden](../ButtonDefinition/ButtonDefinition_IsShortcutOverridden.md) | Gets whether the default (internal) shortcut has been overridden by the user or through the API. |
| [LargeIcon](../ButtonDefinition/ButtonDefinition_LargeIcon.md) | Gets/Sets LargeIcon. |
| [LastUpdatedVersion](../ButtonDefinition/ButtonDefinition_LastUpdatedVersion.md) | Read-write property that gets and sets the last updated version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in. |
| [OverrideShortcut](../ButtonDefinition/ButtonDefinition_OverrideShortcut.md) | Gets/Sets the override shortcut assigned to the command. Setting this property to a null string clears the override. |
| [OverrideShortcutType](../ButtonDefinition/ButtonDefinition_OverrideShortcutType.md) | Gets the type of override shortcut assigned to this command. Possible return values are kNoShortcut (no shortcut has been assigned), kAcceleratorShortcut (a shortcut that directly launches the command), or kAliasShortcut (a command alias). |
| [Parent](../ButtonDefinition/ButtonDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Pressed](../ButtonDefinition/ButtonDefinition_Pressed.md) | Gets/Sets Pressed property. |
| [ProgressiveToolTip](../ButtonDefinition/ButtonDefinition_ProgressiveToolTip.md) | Returns a ProgressiveToolTip object providing access to enhanced tooltip display for controls in the ribbon interface. |
| [StandardIcon](../ButtonDefinition/ButtonDefinition_StandardIcon.md) | Gets/Sets StandardIcon. |
| [ToolTipText](../ButtonDefinition/ButtonDefinition_ToolTipText.md) | Gets/Sets Tooltip. |
| [Type](../ButtonDefinition/ButtonDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnExecute](../ButtonDefinition/ButtonDefinition_OnExecute.md) | Event that fires when the ButtonDefinition is executed. |
| [OnHelp](../ButtonDefinition/ButtonDefinition_OnHelp.md) | Event that is fired when the user selects F1 while the progressive tooltip of this command is being displayed in the ribbon interface. |

## Accessed From

[ControlDefinitions.AddButtonDefinition](../ControlDefinitions/ControlDefinitions_AddButtonDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add commands to the application menu](../../sample-programs/AddButtonToAppMenu_Sample.md) | Demonstrates adding command to the application menu. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 6
