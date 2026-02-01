# FusionHubExecutionBehaviors Enumerator

## Description

Enum to define the behavior when posting to Fusion hub.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| FusionHubExecutionBehavior\_ExportWithRelationship | 2 | Post to Fusion Hub while setting the parent document as a relationship. In the UI this will raise a "save document" dialog if the parent document's save state is not up to date. Cancelling the dialog, or if none is shown, will result in the document not being saved and the post result being exported without setting the relationship in Fusion Hub. This is the default value. |
| FusionHubExecutionBehavior\_ForceExportWithRelationship | 0 | Post to Fusion Hub while setting the parent document as a relationship. In the UI this will raise a "save document" dialog if the parent document's save state is not up to date. Cancelling the dialog, or if none is shown, will result in the document not being saved and the post result not being exported. |
| FusionHubExecutionBehavior\_SilentForceExportWithRelationship | 1 | Post to Fusion Hub while setting the parent document as a relationship. The document and post result are both saved in the Fusion Hub folder specified. If the document has not been saved before, then a new document named "NCProgramPostProcess\_YYYYMMDD\_HH:MM:SS" will be created with YYYYMMDD\_HH:MM:SS being substituted with the current date time. |
| FusionHubExecutionBehavior\_SkipRelationship | 3 | Post to Fusion Hub without setting the parent document as a relationship. The parent document does not need to be saved to post to Fusion Hub. |

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |