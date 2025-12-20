# FileUIEvents.OnFileOpenDialog Event

Parent Object: [FileUIEvents](../FileUIEvents/FileUIEvents.md)

## Description

The OnFileOpenDialog event notifies the client when the end-user executes the Open command to open an existing file.
By responding to this event the client can override Inventor's standard behavior of displaying the Open dialog and provide their own interface to determine the file to open. This notification is only made in cases where the Open dialog is displayed to allow the end-user to select a file. If the end-user uses the most recently used list in the File menu to open a file the Open dialog is bypassed and the file is opened directly and because the Open dialog is not used this notification is not sent.

## Remarks

Valid values for the NameValueMap in the Context argument:

| Name | Type | Document type being opened | Notes |
| --- | --- | --- | --- |
| DesignViewRepresentation | String | Part, Assembly | The name of the design view representation. |
| DesignViewAssociative | Boolean | Assembly | Specifies whether the design view is associative or not. |
| PrivateRepresentationFile | String | Assembly | Specifies the private representation file. |
| PositionalRepresentation | String | Assembly | The name of the positional representation. |
| ModelState | String | Part,Assembly | Typically, the ModelState to use should be provided in the form of a FulDocumentName (first argument). But if this is provided separately, you should make sure that it does not conflict with the FullDocumentName argument by providing FullFileName as the first argument rather than a FullDocumentName. |
| DeferUpdates | Boolean | Drawing | Indicates if any pending updates for the drawing will be deferred when the drawing is opened. |
| FileVersionOption | Value from FileVersionEnum | All | Valid values for FileVersionEnum are kOpenOldVersion, kOpenCurrentVersion and kRestoreOldVersionToCurrent. If set to kOpenOldVersion, save will not be allowed on the opened document. kRestoreOldVersionToCurrent is valid only if no other versions are open and the current version is not checked out. |
| ImportNonInventorDWG | Boolean | Imports the DWG file to an IDW if True, Opens it into Inventor DWG if False | When opening non-Inventor DWG files, this method honors the application option to decide between open and import, unless an override is specified in the Options argument. |
| Password | String | Protected DWG |  |
| ExpressModeBehavior | String | Assembly | The following values are valid for this setting:     OpenExpress - Open the assembly in express mode.     OpenFull - Open the assembly in full mode.     OpenDefault - Open the assembly in the mode it was saved in. |
| FastOpen | Boolean | Drawing | Specifies whether skip all referenced files when open a drawing document. |
| SkipAllUnresolvedFiles | Boolean | All | Specifies whether skip all unresolved referenced files when open a document. |
| DeferFlatPatternUpdate | Boolean | Part(SheetMetal) | Specifies whether defer the flat pattern update when open a sheet metal document. |

## Syntax

FileUIEvents.**OnFileOpenDialog**( ***FileTypes***() As String, ***ParentHWND*** As Long, ***FileName*** As String, ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileTypes | String | A list of the file types displayed in the "Files of Type" combo box on the Open dialog. Examples of some strings that could be provided by this arguments are: "Inventor Files (\*.iam;\*.idw;\*.ipt;\*.ipn;\*.ide)|\*.iam;\*.idw;\*.ipt;\*.ipn;\*.ide" "Assembly Files (\*.iam)|\*.iam" "Drawing Files (\*.idw)|\*.idw" "Part Files (\*.ipt)|\*.ipt" "STEP Files (\*.stp;\*.ste;\*.step)|\*.stp;\*.ste;\*.step" "All Files (\*.\*)|\*.\*" |
| ParentHWND | Long | The Windows handle of the Inventor Application window. If the client displays their own dialog they can use this to associate their dialog to the Inventor window. This results in better behavior between the client dialog and Inventor. For example, the client window will stay on top of Inventor and if the Inventor window is collapsed the client dialog will also be collapsed. |
| FileName | String | The full filename of the file to open. This must be an existing valid file and the HandlingCode must be set to kEventHandled in order to override the standard open behavior. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | See Remarks for valid NameValueMap values that can be passed back when responding to event. These control how the document will be opened. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output that indicates how you are handling the event. Can supply any of the following three values:  * kEventNotHandled: Inventor continues with its standard behavior and displays the "Open" dialog to allow the end-user to select a file. * kEventHandled: Indicates that the you are handling getting the filename. Requires that you also set the FileName argument. * kEventCanceled: Cancels the operation. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |