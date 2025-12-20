# GeneralOptions Object

## Description

The GeneralOptions object provides access to properties that provide read and write access of the general application options. This is somewhat equivalent to the General tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationScale](../GeneralOptions/GeneralOptions_AnnotationScale.md) | Gets/Sets the size of non-model elements in the graphics window. |
| [Application](../GeneralOptions/GeneralOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EnableLegacyProjectCreation](../GeneralOptions/GeneralOptions_EnableLegacyProjectCreation.md) | Gets/Sets the creation of shared and semi-isolated legacy projects. |
| [EnableOptimizedSelection](../GeneralOptions/GeneralOptions_EnableOptimizedSelection.md) | Gets and sets whether enables or disables optimized selection. |
| [EnableSpellCheck](../GeneralOptions/GeneralOptions_EnableSpellCheck.md) | Gets and sets whether to enable the spell check or not. This property defaults to True to indicate the specll check is enabled. |
| [GripSnapOptions](../GeneralOptions/GeneralOptions_GripSnapOptions.md) | Property that returns the GripSnapOptions object. The GripSnapOptions object provides access to various grip snap related application level options. |
| [iMateVisibility](../GeneralOptions/GeneralOptions_iMateVisibility.md) | Gets and sets the Visibility of the iMate Glyph. |
| [SecondLevelTooltipDelay](../GeneralOptions/GeneralOptions_SecondLevelTooltipDelay.md) | Gets and sets the length of the delay time (in seconds), before the second tooltip is displayed. |
| [SelectOtherDelay](../GeneralOptions/GeneralOptions_SelectOtherDelay.md) | Gets/Sets the length of the delay time. |
| [ShowAutocompleteForCommandAlias](../GeneralOptions/GeneralOptions_ShowAutocompleteForCommandAlias.md) | Gets and sets whether the autocomplete dropdown box should be displayed for command aliases. |
| [ShowCommandAliasInputDialog](../GeneralOptions/GeneralOptions_ShowCommandAliasInputDialog.md) | Gets and sets whether the input dialog should be displayed for command aliases. |
| [ShowCommandPromptTooltips](../GeneralOptions/GeneralOptions_ShowCommandPromptTooltips.md) | Gets and sets whether tooltips should be displayed to prompt for command inputs. |
| [ShowDocumentTabTooltips](../GeneralOptions/GeneralOptions_ShowDocumentTabTooltips.md) | Gets and sets whether to show tooltips when hovering over document tabs. |
| [ShowHomeBaseOnStartup](../GeneralOptions/GeneralOptions_ShowHomeBaseOnStartup.md) | Gets and sets whether to use the MyHome Screen. |
| [ShowSecondLevelTooltips](../GeneralOptions/GeneralOptions_ShowSecondLevelTooltips.md) | Gets and sets whether to show second level tooltips when hovering over a command in the ribbon. |
| [ShowTooltips](../GeneralOptions/GeneralOptions_ShowTooltips.md) | Gets and sets whether to show tooltips when hovering over a command in the ribbon. |
| [SpellCheckOptions](../GeneralOptions/GeneralOptions_SpellCheckOptions.md) | Read-only property that returns the SpellCheckOptions object. The SpellCheckOptions object provides access to various spell check related application level options. |
| [StartupActionType](../GeneralOptions/GeneralOptions_StartupActionType.md) | Gets and sets the type of startup action to perform each time Autodesk Inventor is opened. |
| [StartupNewFileTemplateName](../GeneralOptions/GeneralOptions_StartupNewFileTemplateName.md) | Gets and sets the name of the template for the new file that will be automatically created each time Autodesk Inventor is opened. |
| [StartupProjectFileName](../GeneralOptions/GeneralOptions_StartupProjectFileName.md) | Gets and sets the name of the project file that will be used each time Autodesk Inventor is opened. |
| [TextAppearance](../GeneralOptions/GeneralOptions_TextAppearance.md) | Gets/Sets Text Appearance. |
| [TextSize](../GeneralOptions/GeneralOptions_TextSize.md) | Gets/Sets Text Size. |
| [ThreadTableQuery](../GeneralOptions/GeneralOptions_ThreadTableQuery.md) | Property that returns the ThreadTableQuery object. This object has methods to query the thread table data contained in the Thread.xls spreadsheet. |
| [ToleranceValue](../GeneralOptions/GeneralOptions_ToleranceValue.md) | Gets/Sets the distance (in pixels) where a selection of an object can occur. |
| [TooltipDelay](../GeneralOptions/GeneralOptions_TooltipDelay.md) | Gets and sets the length of the delay time (in seconds), while the cursor is hovering over a command in the ribbon, before the tooltip is displayed. |
| [Type](../GeneralOptions/GeneralOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UndoFileSize](../GeneralOptions/GeneralOptions_UndoFileSize.md) | Gets/Sets the size of the temporary file. |
| [UpdatePropertiesOnSaveForFileType](../GeneralOptions/GeneralOptions_UpdatePropertiesOnSaveForFileType.md) | Gets and sets whether properties should be updated when part or assembly files are saved. |
| [UseAutodeskOnlineHelp](../GeneralOptions/GeneralOptions_UseAutodeskOnlineHelp.md) | Gets and sets whether to use the Autodesk online help or not. This property defaults to True to indicate the online help will be used. If local help is installed set this property to False to use the local help. |
| [UseNegativeIntegralForInertialProperties](../GeneralOptions/GeneralOptions_UseNegativeIntegralForInertialProperties.md) | Gets/Sets whether the inertial properties should be calculated using the negative integral. |
| [UserName](../GeneralOptions/GeneralOptions_UserName.md) | Gets/Sets user name. |

## Accessed From

[Application.GeneralOptions](../Application/Application_GeneralOptions.md), [InventorServer.GeneralOptions](InventorServer_GeneralOptions.md), [InventorServerObject.GeneralOptions](InventorServerObject_GeneralOptions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Window Selection](../../sample-programs/SelectEventsObject_WindowSelectEnabled_Sample.md) | This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module. |
| [Creating a ThreadInfo object](../../sample-programs/ThreadTableQuery_CreateThreadInfo_Sample.md) | Demonstrates the use of a ThreadInfo object. |

## Version

Introduced in version 8

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |