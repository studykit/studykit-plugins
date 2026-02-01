# DataHub Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHub.h>

## Description

Represents a hub within the data.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DataHub_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dataProjects](DataHub_dataProjects.htm) | Returns the projects within this hub. |
| [fusionWebURL](DataHub_fusionWebURL.htm) | Returns a URL that can be used to access the Fusion Web interface for this hub within a browser. The person using the URL must have an Autodesk account and have authority to access the hub. |
| [hubType](DataHub_hubType.htm) | Gets if this hub is a Personal (PersonalHubType) or Team (TeamHubType) type hub. |
| [id](DataHub_id.htm) | Returns the unique ID for this hub. This is the same id used in the APS Data Management API in an unencoded form and will look something like this: "a.45637". |
| [isCollaborativeEditingEnabled](DataHub_isCollaborativeEditingEnabled.htm) | Returns true if Concurrent Editing is enabled. |
| [isValid](DataHub_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [mfgdmId](DataHub_mfgdmId.htm) | ![Preview](../images/TestTubeSmall.png)Get the MFGDM ID for this hub. |
| [name](DataHub_name.htm) | Returns the name of the hub. |
| [objectType](DataHub_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [version](DataHub_version.htm) | Returns the version of the hub. |

## Accessed From

[Data.activeHub](Data_activeHub.htm), [DataHubs.asArray](DataHubs_asArray.htm), [DataHubs.item](DataHubs_item.htm), [DataHubs.itemById](DataHubs_itemById.htm), [DataProject.parentHub](DataProject_parentHub.htm)

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |