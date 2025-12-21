# FileAccessEvents.OnFileResolution Event

Parent Object: [FileAccessEvents](../FileAccessEvents/FileAccessEvents.md)

## Description

The OnFileResolution event notifies a client whenever Inventor is trying to find the location of a file on disk.

## Remarks

Whenever a document is opened in Inventor that contains references to other documents, the paths to the referenced documents must be determined. This process referred to as "file resolution". For example, if there is an assembly Top.iam that contains Part.ipt, when Top.iam is opened Inventor needs to find Part.ipt on the disk in order to open it too. It does this using a combination of information stored in Top.iam and the paths defined by the active project. This event allows you to override Inventors standard file resolution and perform the resolution yourself. The OnFileResolution event notification is sent at the time Inventor recognizes that a file needs to be resolved but before it begins the resolution process. Through the arguments of this event, Inventor provides you all of the information it has about this reference. You can use this information to perform your own file resolution using whatever logic you choose and then supply Inventor with the full filename to use. If you supply a valid filename Inventor skips its resolution and loads the file you specify. The intent of this event is to allow you to control how Inventor resolves files. It is not intended as a mechanism to replace parts in an assembly. The filename you provide should be the full path of the original file that was referenced.

## Syntax

FileAccessEvents.**OnFileResolution**( ***RelativeFileName*** As String, ***LibraryName*** As String, ***CustomLogicalName***() As Byte, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***FullFileName*** As String, ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RelativeFileName | String | The relative filename of the document. This is typically just the filename but may also include relative path information. Inventor uses this in combination with the paths defined by the active project to resolve the location of the file. |
| LibraryName | String | If the document is a library part, this argument provides the name of the library as defined in the active project. If it is not a library part this will be an empty string. |
| CustomLogicalName | Byte | An array of Bytes that is used by data management systems as a way to associate additional information with a file reference. In the case where a custom logical name was assigned to a reference and the associated document, this argument will return that value. The data management application that originally defined the custom logical name can use this information to help look up the file within the data management system. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. This notification is always provided with kBefore when the document is being resolved, and only provided kAfter when this event is not handled in kBefore. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification.  Name = "DatabaseRevisionId". Value = This value should be ignored.  Name = "InternalName". Value = The internal name of the document that was last resolved for this reference. This is the same value returned by the InternalName property of the document that was last used for this reference.  Name = "DirectReferencingFileName". Value = This value and the value for TopLevelFilename are related. Looking at a simple example helps to explain the information they provide: In this example there is Part.ipt that's referenced by subassembly Sub.iam, which is referenced by the assembly Top.iam. When you open Top.iam, the other files also need to be resolved and loaded. When Top.iam is opened, an OnFileResolution notification is sent for Sub.iam. For Sub.iam, DirectReferencingFileName will be the full filename of Top.iam because Sub.iam is being loaded because of the direct reference from Top.iam. TopLevelFilename will also be the full filename of Top.iam since that is the top level document that was opened. An OnFileResolution notification is also sent for Part.ipt. In this case, DirectReferencingFileName will be the full filename of Sub.iam since Part.ipt is being loaded because of the direct reference from Sub.iam. TopLevelFilename will be the full filename of Top.iam, since is it the top-level document that caused the loading.  Name = "TopLevelFilename". Value = See the description for DirectReferencingFileName.  Name = "IsForeignFile". Value = Boolean value that indicates whether the file being resolved is a foreign file.  Name = "RedirectionStreamIndex ". Value = Long value that indicates the redirection stream index of the file for native and foreign files respectively. This value is starting from 0. |
| FullFileName | String | If you are handling this event you use this argument to pass back the full filename of the document you want Inventor to load. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. To handle this event and you need to set this argument to kEventHandled. This will cause Inventor to skip its standard resolution and load the file you spescified in the FullFileName argument. Setting the value of this argument to kEventNotHandled (the default) will cause Inventor to use its standard file resolution. Canceling this event is not supported and setting this argument to kEventCanceled has the same effect as kEventNotHandled. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |