# Scripts Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

API object that provides equivalent functionality of the "Scripts and Add-Ins" dialog. Provides access to the scripts and add-ins that Fusion is aware of. It also supports loading other unknown scripts and add-ins, and creating new scripts and add-ins.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addExisting](Scripts_addExisting.htm) | Fusion looks in specific folders for scripts and add-ins, but you can manually add other scripts and add-ins to the list of known scripts and add-ins so they will be listed in the "Scripts and Add-ins" dialog. This method does that. |
| [addNew](Scripts_addNew.htm) | Creates a new script or add-in. This uses the same internal template that's used when creating a new script or add-in using the "Scripts and Add-Ins" dialog. The provided ScriptInput object defines the information needed to create a new script or add-in. |
| [classType](Scripts_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createScriptInput](Scripts_createScriptInput.htm) | Creates a new ScriptInput object. Logically, this object is equivalent to the dialog that is shown when you click the "Create" button in the "Scripts and Add-Ins" command dialog. It collects the information needed to create a new script or add-in. To create the script or add-in, call the addNew method, passing in the ScriptInput object. |
| [item](Scripts_item.htm) | Function that returns the specified script or add-in using an index into the collection. |
| [itemByPath](Scripts_itemByPath.htm) | Function that returns the script that is located in the specified folder. |
| [itemsByName](Scripts_itemsByName.htm) | Function that returns an array of scripts that have the specified name. In most cases this will return an array containing a single script, but it's possible to have more than one script with the same name in the case where the scripts are in different folders. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Scripts_count.htm) | Returns the number of scripts and add-ins. |
| [isValid](Scripts_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Scripts_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Application.scripts](Application_scripts.htm)

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |