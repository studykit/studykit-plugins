# DocumentToolLibrary Object

Derived from: [ToolLibrary](ToolLibrary.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Tools/DocumentToolLibrary.h>

## Description

DocumentToolLibrary provides access to tools used by the document. It supports adding, updating and deleting tools in the document tool library.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](DocumentToolLibrary_add.htm) | Inserts a Tool at the end of the ToolLibrary. |
| [classType](DocumentToolLibrary_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createEmpty](DocumentToolLibrary_createEmpty.htm) | Creates an empty ToolLibrary. |
| [createFromJson](DocumentToolLibrary_createFromJson.htm) | Creates a ToolLibrary by given JSON-string. Raises an error if the given JSON is invalid. |
| [createQuery](DocumentToolLibrary_createQuery.htm) | Creates a new ToolQuery that is used to query the library for tools matching the query. |
| [item](DocumentToolLibrary_item.htm) | Get Tool by index in ToolLibrary. |
| [operationsByTool](DocumentToolLibrary_operationsByTool.htm) | Returns all operations that use the given tool. The tool must exist in the document tool library. Raises an error if the tool is not in the document. |
| [remove](DocumentToolLibrary_remove.htm) | Remove Tool by index from ToolLibrary. |
| [toJson](DocumentToolLibrary_toJson.htm) | Generate and return JSON string that contains all tools of that list. |
| [toolsBySetupOrFolder](DocumentToolLibrary_toolsBySetupOrFolder.htm) | Returns all tools used in a given setup or folder. Given setup or folder must belong to the document of the DocumentToolLibrary. Raises an error if given operation is not in the document. |
| [update](DocumentToolLibrary_update.htm) | Update the given tool in the document tool library. The update applies all changes to the tool in the document tool library and therefore on all operations that use the tool. Will error if the tool does not exist in the document tool library. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DocumentToolLibrary_count.htm) | The number of tools in the ToolLibrary. |
| [isValid](DocumentToolLibrary_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DocumentToolLibrary_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAM.documentToolLibrary](CAM_documentToolLibrary.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |