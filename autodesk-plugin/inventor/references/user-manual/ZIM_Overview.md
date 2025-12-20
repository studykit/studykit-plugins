# Zero Impact Migration

### Zero Impact Migration

The idea behind Zero Impact Migration (ZIM) is to eliminate the performance and memory cost in opening
Inventor files saved with earlier versions of the software. The Document Interests mechanism has been
added to Inventor to aid ZIM.

|  |
| --- |
| **Note:** Document Interests are the recommended means of marking schema versions for application custom data in a document, and in fact is now the preferred method for an Add-in to implement a document sub-type. However, it is not recommended that applications rely on DocumentInterests when querying a document type. An application should not draw any meaning from DocumentInterests that it did not add. In other words, application A should not infer anything from application B's DocumentInterests. |

The following table lists APIs available to implement Zero Impact Migration.

|  |
| --- |
| **ZIM related APIs** |
| [Document.DocumentInterests](../api-doc/Document/Document_DocumentInterests.md) property |
| [Document.NeedsMigrating](../api-doc/Document/Document_NeedsMigrating.md) property |
| [ApprenticeServerDocument.DocumentInterests](../api-doc/ApprenticeServerDocument/ApprenticeServerDocument_DocumentInterests.md) property |
| [DocumentInterests](../api-doc/DocumentInterests/DocumentInterests.md) collection object |
| [DocumentInterest](../api-doc/DocumentInterest/DocumentInterest.md) object |
| [ApplicationAddin.DataVersion](../api-doc/ApplicationAddIn/ApplicationAddIn_DataVersion.md) property |
| [ApplicationEvent.OnMigrateDocument](../api-doc/ApplicationEvents/ApplicationEvents_OnMigrateDocument.md) event |

### Requirements

Here are the set of tasks that must be performed by an application to participate in ZIM:

1. During registration, create a DWORD key called DataVersion under
   the same key (viz. 'HKEY\_CLASSES\_ROOT\CLSID\{CLSID}\Settings') where the other keys such as
   LoadOnStartUp are currently being created for the Add-in application. The value of the DataVersion
   key is the data or schema version for the Add-in application's custom data.
2. In all code paths where the Add-in application creates any custom data for the first time and
   hence intends to mark the document as one containing its data, check whether the Add-in's Document
   Interest exists and that its DataVersion property value is correct.

   If a Document Interest does
   not already exist, register a new DocumentInterest on the document by using the DocumentInterests.Add
   method. Make sure that the DataVersion value is correct and matches the one in the add-in application's
   registry key set in step 1 and also available through the ApplicationAddin.DataVersion
   property.

   The 'Name' argument supplied during creation of the Document Interest can be used
   to define an application specific document sub-type e.g. "Application Top Level Assembly document".
3. Move any existing migration code to the OnMigrateDocument event handler.
4. Create a ChangeProcessor with ChangeType as kSchemaChangeCmdType to wrap the migration code in the
   OnMigrateDocument event handler.
5. In the OnMigrateDocument event handler, after the migration code is executed, update the value of
   the DataVersion property of the add-in application's Document Interest to match the one in the add-in
   application's registry key set in step 1 and also available through ApplicationAddin.DataVersion property.

### Migration Event

The migration event is fired when the 'File->Migrate' menu item is clicked or when an edit operation
in requested on a non-migrated document.

Whether an application's data needs migration is decided by
Inventor by comparing the DataVersion stored in the DocumentInterest registered by the application and
the DataVersion set in the registry by the application during its registration. If the DataVersion in
the registry is greater than that in the DocumentInterest in the document, a migration event will be
fired that the application can react to and migrate its data.