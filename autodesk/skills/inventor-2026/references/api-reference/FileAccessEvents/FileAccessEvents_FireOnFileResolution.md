# FileAccessEvents.FireOnFileResolution Method

Parent Object: [FileAccessEvents](../FileAccessEvents/FileAccessEvents.md)

## Description

Method that fires the OnFileResolution event.

## Syntax

FileAccessEvents.**FireOnFileResolution**( ***RelativeFileName*** As String, ***LibraryName*** As String, ***CustomLogicalName***() As Byte, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***FullFileName*** As String, ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RelativeFileName | String | Input the relative filename of the document. This is typically just the filename but may also include relative path information. Inventor uses this in combination with the paths defined by the active project to resolve the location of the file. |
| LibraryName | String | Input string value that indicates the library name if necessary. |
| CustomLogicalName | Byte | Input an array of Bytes that is used by data management systems as a way to associate additional information with a file reference. In the case where a custom logical name was assigned to a reference and the associated document, this argument will return that value. The data management application that originally defined the custom logical name can use this information to help look up the file within the data management system. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating when the event is being fired. This notification is currently only provided before the document is resolved. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. Additional information is provided through this argument to help in understanding the context of the notification. Name = "DatabaseRevisionId". Value = This value should be ignored. Name = "InternalName". Value = The internal name of the document that was last resolved for this reference. This is the same value returned by the InternalName property of the document that was last used for this reference. Name = "DirectReferencingFileName". Value = This value and the value for TopLevelFilename are related. Looking at a simple example helps to explain the information they provide: In this example there is Part.ipt that's referenced by subassembly Sub.iam, which is referenced by the assembly Top.iam. When you open Top.iam, the other files also need to be resolved and loaded. When Top.iam is opened, an OnFileResolution notification is sent for Sub.iam. For Sub.iam, DirectReferencingFileName will be the full filename of Top.iam because Sub.iam is being loaded because of the direct reference from Top.iam. TopLevelFilename will also be the full filename of Top.iam since that is the top level document that was opened. An OnFileResolution notification is also sent for Part.ipt. In this case, DirectReferencingFileName will be the full filename of Sub.iam since Part.ipt is being loaded because of the direct reference from Sub.iam. TopLevelFilename will be the full filename of Top.iam, since is it the top-level document that caused the loading. Name = "TopLevelFilename". Value = See the description for DirectReferencingFileName. |
| FullFileName | String | Input string that indicates the full filename of the document you want Inventor to load. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Input HandlingCodeEnum that indicates how you want the client to hande the event. To handle this event and you need to set this argument to kEventHandled. This will cause Inventor to skip its standard resolution and load the file you spescified in the FullFileName argument. Setting the value of this argument to kEventNotHandled (the default) will cause Inventor to use its standard file resolution. Canceling this event is not supported and setting this argument to kEventCanceled has the same effect as kEventNotHandled. |

## Version

Introduced in version 2010
