# SaveOptions Object

## Description

The SaveOptions object provides access to properties that provide read and write access of the save related application options. This is somewhat equivalent to the Save tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SaveOptions/SaveOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DefaultToSaveForAPIChanges](../SaveOptions/SaveOptions_DefaultToSaveForAPIChanges.md) | Gets/Sets the default save condition for a document that has API changes. |
| [DefaultToSaveForFileResolutionChange](../SaveOptions/SaveOptions_DefaultToSaveForFileResolutionChange.md) | Gets/Sets the default save condition for a document that has file resolution change. |
| [DefaultToSaveForImplicitUpdate](../SaveOptions/SaveOptions_DefaultToSaveForImplicitUpdate.md) | Gets/Sets the default save condition for a document that has implicit update. |
| [DefaultToSaveForManualUpdates](../SaveOptions/SaveOptions_DefaultToSaveForManualUpdates.md) | Gets/Sets the default save condition for a document that has manual updates. |
| [DefaultToSaveForMassPropertyUpdate](../SaveOptions/SaveOptions_DefaultToSaveForMassPropertyUpdate.md) | Gets/Sets the default save condition for a document that has mass property update. |
| [DefaultToSaveForMigration](../SaveOptions/SaveOptions_DefaultToSaveForMigration.md) | Gets/Sets the default save condition for a document that has been migrated from a previous version of Autodesk Inventor is closed without being explicitly saved. |
| [DefaultToSaveForModelStateUpdates](../SaveOptions/SaveOptions_DefaultToSaveForModelStateUpdates.md) | Gets/Sets the default save condition for a document that has model state updates. |
| [DefaultToSaveForUserEdits](../SaveOptions/SaveOptions_DefaultToSaveForUserEdits.md) | Gets/Sets the default save condition for a document that has user edits. |
| [PromptSaveForAPIChanges](../SaveOptions/SaveOptions_PromptSaveForAPIChanges.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has API changes. |
| [PromptSaveForFileResolutionChange](../SaveOptions/SaveOptions_PromptSaveForFileResolutionChange.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has file resolution change. |
| [PromptSaveForImplicitUpdate](../SaveOptions/SaveOptions_PromptSaveForImplicitUpdate.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has implicit update. |
| [PromptSaveForManualUpdates](../SaveOptions/SaveOptions_PromptSaveForManualUpdates.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has manual updates. |
| [PromptSaveForMassPropertyUpdate](../SaveOptions/SaveOptions_PromptSaveForMassPropertyUpdate.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has mass property update. |
| [PromptSaveForMigration](../SaveOptions/SaveOptions_PromptSaveForMigration.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has been migrated from a previous version of Autodesk Inventor is closed without being explicitly saved. |
| [PromptSaveForModelStateUpdates](../SaveOptions/SaveOptions_PromptSaveForModelStateUpdates.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has model state updates. |
| [PromptSaveForUserEdits](../SaveOptions/SaveOptions_PromptSaveForUserEdits.md) | Gets/Sets whether a prompt to save the document should be displayed when a document that has user edits. |
| [SaveFilesInLibraryFolders](../SaveOptions/SaveOptions_SaveFilesInLibraryFolders.md) | Gets/Sets whether to save the files in library folders or not. |
| [SaveReminderTimer](../SaveOptions/SaveOptions_SaveReminderTimer.md) | Gets/Sets the save reminder timer (in minutes). |
| [ShowSaveReminder](../SaveOptions/SaveOptions_ShowSaveReminder.md) | Gets/Sets whether to display a save reminder to the user. |
| [TranslatorReportLocation](../SaveOptions/SaveOptions_TranslatorReportLocation.md) | Gets/Sets whether to create a tranlation report and where to save it. |
| [Type](../SaveOptions/SaveOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.SaveOptions](../Application/Application_SaveOptions.md), [InventorServer.SaveOptions](InventorServer_SaveOptions.md), [InventorServerObject.SaveOptions](InventorServerObject_SaveOptions.md)

## Version

Introduced in version 11
