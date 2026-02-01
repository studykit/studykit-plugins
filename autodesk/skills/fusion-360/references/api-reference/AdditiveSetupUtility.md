# AdditiveSetupUtility Object

Derived from: [ModifyUtility](ModifyUtility.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/ModifyUtility/AdditiveSetupUtility.h>

## Description

AdditiveSetupUtility provides functionality for modifications of additive setups.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [assignPartsToBodyPreset](AdditiveSetupUtility_assignPartsToBodyPreset.htm) | Assigns an array of parts to the body preset operation corresponding to the chosen PrintSettingItem in the PrintSetting. If a part has been previously assigned to a different preset (i.e. the default preset), it will be removed from its previous owner to ensure a body can only be mapped to one preset. If the previous owner preset ends up being empty, it will be removed from the setup. |
| [classType](AdditiveSetupUtility_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [removeExcessParts](AdditiveSetupUtility_removeExcessParts.htm) | Remove components from setups, that are outside of the buildroom. |
| [splitSupport](AdditiveSetupUtility_splitSupport.htm) | Splits support structure of given target bodies into separate mesh body. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](AdditiveSetupUtility_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](AdditiveSetupUtility_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |