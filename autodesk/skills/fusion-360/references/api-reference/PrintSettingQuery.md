# PrintSettingQuery Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

A PrintSettingQuery can be used to search a LibraryLocation for a set of PrintSetting objects matching the required properties.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PrintSettingQuery_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [execute](PrintSettingQuery_execute.htm) | Query for specific PrintSettings. This PrintSettingQuery query. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filamentDiameter](PrintSettingQuery_filamentDiameter.htm) | \*\*RETIRED\*\* The filament diameter specifies filament diameter for FFF Printer. This should match the FFF PrintSetting filament diameter in cm. |
| [isValid](PrintSettingQuery_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [layerHeight](PrintSettingQuery_layerHeight.htm) | The layer height specifies layer height of the PrintSetting. This should match the PrintSetting layer height in cm. |
| [location](PrintSettingQuery_location.htm) | The location specifies the location to search in the PrintSetting library. Setting the location clears any previous specified URL. |
| [machine](PrintSettingQuery_machine.htm) | The machine specifies which machine the found print setting are compatible with. |
| [material](PrintSettingQuery_material.htm) | The case-insensitive material specifies material of the MPBF PrintSetting. |
| [name](PrintSettingQuery_name.htm) | The case-insensitive name specifies the name of the PrintSetting. |
| [objectType](PrintSettingQuery_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [technology](PrintSettingQuery_technology.htm) | The case-insensitive technology specifies technology of the PrintSetting. |
| [url](PrintSettingQuery_url.htm) | The URL specifies the location and folder to search for in the PrintSetting library. Setting the URL updates the location. |
| [vendor](PrintSettingQuery_vendor.htm) | The case-insensitive vendor specifies vendor of the PrintSetting. Generic FFF PrintSetting doesnt have a vendor. |

## Accessed From

[PrintSettingLibrary.createQuery](PrintSettingLibrary_createQuery.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |