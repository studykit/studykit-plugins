# PrintSettingItem Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingItem.h>

## Description

Collection that provides access to the print setting parameters.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PrintSettingItem_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [description](PrintSettingItem_description.htm) | Body Preset get and set description. |
| [isValid](PrintSettingItem_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](PrintSettingItem_name.htm) | Body Preset get and set name. |
| [objectType](PrintSettingItem_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parameters](PrintSettingItem_parameters.htm) | Function that returns the parameters for reading and editing values. |

## Accessed From

[PrintSetting.duplicatePrintSettingItem](PrintSetting_duplicatePrintSettingItem.htm), [PrintSetting.getDefaultPrintSettingItem](PrintSetting_getDefaultPrintSettingItem.htm), [PrintSetting.item](PrintSetting_item.htm), [PrintSetting.itemByName](PrintSetting_itemByName.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |